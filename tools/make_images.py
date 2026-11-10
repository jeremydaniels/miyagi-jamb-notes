#!/usr/bin/env python3
"""Make, check, label and place the images for a set of notes files (Gemini only).

  python tools/make_images.py --subject biology --files B3a B5 --run            # standard mode
  python tools/make_images.py --subject biology --files B2a --batch-test 20 --run
  python tools/make_images.py --subject biology --status

Per AI image: generate (no text) -> Gemini vision check against the placeholder (re-roll up to 2 times,
Pro for re-rolls) -> if there is a label list, Gemini vision finds each part and label.py draws the labels
and pointer lines (Gemini never writes label text) -> Gemini vision checks the labelled image (wrong labels
are re-placed up to 2 times, then the image is flagged). Per code-drawn image: Gemini writes matplotlib code,
it runs in a sandbox-ish subprocess, and the same vision check runs (layout fixed up to 2 times).
Passed images are placed into the notes with place_images.py, compressed, and committed per notes file.
A failed image leaves its [IMAGE: ...] placeholder in the notes. All state is kept in .image-work/jobs/.
"""
import argparse, ast, base64, glob, io, json, os, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gemini_common as g
import generate as gen
import label as lab
import extract_prompts as ex
from common import RAW, WORK, REPO
from PIL import Image

SUBJECT = "biology"
SUBJ = "biology-images2"           # name under which text/vision calls are logged (per subject)
CAP = 120.0                      # total spend cap for the whole run (all subjects), USD
PILOT_OFFSET = 0.0
FLASH_IMG, PRO_IMG = "gemini-3.1-flash-image", "gemini-3-pro-image"
TXT_FLASH = g.load_pricing().get("flash_model", "gemini-3.8-flash")
TXT_PRO = g.default_model()
JOBS_DIR = os.path.join(WORK, "jobs"); os.makedirs(JOBS_DIR, exist_ok=True)
CODE_DIR = os.path.join(WORK, "code"); os.makedirs(CODE_DIR, exist_ok=True)
FAIL_DIR = os.path.join(WORK, "failed"); os.makedirs(FAIL_DIR, exist_ok=True)
LOCK = threading.Lock(); GITLOCK = threading.Lock()
STOP = threading.Event()

OVERRIDES = {  # image name -> (model, extra prompt text): the four pilot problems
    "B3a-05-mammalian-heart-internal-section": (PRO_IMG, "The muscular wall of the left ventricle must be drawn clearly the thickest part of the heart, about three times thicker than the wall of the right ventricle and visibly thicker than the walls of the atria."),
    "B5-08-nephron-structure-detailed": (PRO_IMG, "The afferent arteriole (entering the glomerulus) must be drawn WIDE and bright red; the efferent arteriole (leaving the glomerulus) must be drawn clearly NARROWER and a darker red, so the two are obviously different, entering and leaving at the Bowman's capsule."),
    "B9c-10-coleoptile-phototropism-experiments": (PRO_IMG, "Experiment 6: the thin grey mica sheet stands VERTICALLY (upright, like a thin wall) inserted into the coleoptile from its shaded left side just below the tip, blocking the left half of the stem. Experiment 4: the black sleeve wraps the stem below the tip, and the whole coleoptile bends clearly towards the light. Do not write numbers."),
    "B4a-04-tadpole-external-internal-gills": (PRO_IMG, "Draw only the outside of the tadpoles, as solid opaque bodies. Do not show any internal organs, no cutaway, no see-through body."),
}


ACCEPT = set()
ROUNDS = 2            # AI generation rounds (--rounds 1: one more try only)
CODE_ATTEMPTS = None  # limit code attempts (--code-attempts)
PRO_CODE = False      # use the Pro text model from the first code attempt
SIMPLIFIED = {}       # name -> simplified description (cleanup retries)          # image names whose raw picture I have looked at and accepted despite the automatic check (human override)
CODE_OVERRIDE = {       # AI placeholders better drawn in code: name -> extra instructions
    "B9c-10-coleoptile-phototropism-experiments": "Draw each of the seven experiments as a coleoptile (a pale green tube with a rounded tip) standing in a small pot, in ONE row, with yellow light arrows from the RIGHT in experiments 1 to 6 and a grey panel (darkness) behind experiment 7. Experiment 4: black sleeve around the stem BELOW the tip and the coleoptile bends towards the light (right). Experiment 6: a thin grey mica sheet drawn VERTICALLY inside the stem on its left (shaded) side just below the tip; the coleoptile stays straight. Number the experiments 1 to 7 under the pots and give each a short caption.",
}


AI_OVERRIDE = {"B1-01-dicot-root-transverse-section", "B1-05-dicot-leaf-transverse-section", "B1-06-leaf-epidermis-stomata"}  # anatomy sections the code route could not draw well


SUBJECT_RULES = {
    "crk": "Christian Religious Knowledge illustration. Show Jesus and angels, where the scene needs them, in a respectful, simple flat style (kind faces, modest dress, no ridicule). NEVER depict God the Father: show God only through symbols such as rays of light, a cloud, a hand-less glow. Biblical-era dress, Middle-Eastern setting. No text.",
    "irk": "Islamic Religious Knowledge illustration. Draw every human figure WITHOUT a face (smooth blank faces, modest dress). Never draw the Prophet Muhammad or any prophet or angel. Prayer and ablution positions as clear simple step figures. No Arabic script, no calligraphy, no text of any kind.",
}
SENSITIVE = {"crk", "irk"}


def style_of():
    sub = SUBJECT.replace("-", " ")
    return gen.STYLE.format(subject=sub) + (" " + SUBJECT_RULES[SUBJECT] if SUBJECT in SUBJECT_RULES else "")


class Capped(Exception):
    pass


def spent(subject=None):
    """Spend of this run: image generation (costs.jsonl in .image-work) plus every logged Gemini call whose subject ends -images2.
    With subject: only that subject's share."""
    img = 0.0
    if os.path.exists(gen.COST_LOG):
        for line in open(gen.COST_LOG):
            if line.strip():
                r = json.loads(line)
                if subject is None or r.get("subject") == subject:
                    img += r["cost"]
    txt = sum(r["cost_usd"] for r in g.read_costs() if r["subject"].endswith("-images2") and (subject is None or r["subject"] == subject + "-images2"))
    return img + txt


def check_cap(extra=0.15):
    if STOP.is_set() or spent() + extra > CAP:
        STOP.set(); raise Capped(f"image spend ${spent():.2f} reached the ${CAP:.0f} cap")


# ---------------------------------------------------------------- jobs

def load_jobs(subject, prefixes):
    sdir = os.path.join(REPO, "subjects", subject)
    files = sorted(f for f in glob.glob(os.path.join(sdir, "[A-Z][0-9]*.md")))
    if prefixes:
        files = [f for f in files if any(os.path.basename(f).startswith(p) for p in prefixes)]
    jobs = []
    for f in files:
        fname = os.path.basename(f); topic = fname[:-3]; prefix = topic.split("-")[0]
        lines = open(f).read().split("\n"); cls = ex.load_classes(subject, fname)
        for slot, idx in enumerate(ex.slots(lines), 1):
            if not lines[idx].startswith("[IMAGE:"):
                continue
            c = cls.get(slot, {}); grp = c.get("group", "AI")
            body, labels = ex.parse_placeholder(lines[idx])
            full = " ".join(lines[idx][7:].rstrip().rstrip("]").split())
            name = f"{prefix}-{slot:02d}-{ex.slug(c.get('kind') or body)}"
            caption = ""; regions = []
            if c.get("parts", "") != "":                       # reclassified: pointer labels only on real parts, notes go to a caption
                labels = json.loads(c["parts"]); regions = json.loads(c.get("regions") or "[]"); caption = c.get("caption", "")
            base = dict(subject=subject, file=fname, topic=topic, slot=slot, name=name, kind=c.get("kind", ""), prompt=body, full=full,
                        labels=labels, regions=regions, caption=caption, template=c.get("template", ""), model=FLASH_IMG, sensitive=subject in SENSITIVE)
            if name in SIMPLIFIED:
                base["prompt"] = SIMPLIFIED[name]; base["full"] = SIMPLIFIED[name]
            if grp == "SKIP":
                jobs.append(dict(base, group="SKIP", code=False, skip=True)); continue
            code = grp in ("CODE", "FLAG")
            if code and name in AI_OVERRIDE: code = False
            if name in CODE_OVERRIDE: code = True; base["full"] += " " + CODE_OVERRIDE[name]
            if code and grp == "FLAG": base["template"] = "map"
            ov = OVERRIDES.get(name)
            if ov: base["model"] = ov[0]; base["prompt"] += " " + ov[1]
            jobs.append(dict(base, group=grp, code=code, skip=False))
    return jobs


def jpath(name):
    return os.path.join(JOBS_DIR, name + ".json")


def load_state(job):
    p = jpath(job["name"])
    return json.load(open(p)) if os.path.exists(p) else {"status": "pending", "cost_note": 0}


def save_state(job, st):
    with LOCK:
        json.dump(st, open(jpath(job["name"]), "w"), indent=1)


# ---------------------------------------------------------------- vision helpers

def jpeg_b64(path_or_img, size=1024):
    im = Image.open(path_or_img) if isinstance(path_or_img, str) else path_or_img
    im = im.convert("RGB")
    if max(im.size) > size:
        im.thumbnail((size, size))
    b = io.BytesIO(); im.save(b, "JPEG", quality=88)
    return base64.b64encode(b.getvalue()).decode()


def vision(prompt, imgs, schema, task, model=None, thinking="low"):
    check_cap(0.01)
    parts = [{"text": prompt}] + [{"inline_data": {"mime_type": "image/jpeg", "data": jpeg_b64(i)}} for i in imgs]
    r = g.call_gemini(parts, model=model or TXT_FLASH, json_schema=schema, thinking=thinking, subject=SUBJ, task=task, timeout=300, attempts=4)
    return json.loads(r["text"])


S_RAW = {"type": "OBJECT", "properties": {"ok": {"type": "BOOLEAN"}, "problems": {"type": "ARRAY", "items": {"type": "STRING"}},
         "stray_text": {"type": "STRING", "enum": ["none", "tiny", "significant"]},
         "tiny_boxes": {"type": "ARRAY", "items": {"type": "ARRAY", "items": {"type": "INTEGER"}}},
         "alt": {"type": "STRING"}}, "required": ["ok", "problems", "stray_text", "alt"]}
S_PTS = {"type": "OBJECT", "properties": {"points": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
         "label": {"type": "STRING"}, "x": {"type": "INTEGER"}, "y": {"type": "INTEGER"}}, "required": ["label", "x", "y"]}}}, "required": ["points"]}
S_LCHK = {"type": "OBJECT", "properties": {"labels": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
          "label": {"type": "STRING"}, "ok": {"type": "BOOLEAN"}, "issue": {"type": "STRING"}}, "required": ["label", "ok"]}},
          "overlap": {"type": "BOOLEAN"}, "unreadable": {"type": "BOOLEAN"}}, "required": ["labels", "overlap", "unreadable"]}


def check_raw(job, path):
    pr = ("You are checking an UNLABELLED textbook illustration against the description it must match.\n"
          f"DESCRIPTION: {job['prompt']}\n"
          + (f"PARTS THAT WILL BE LABELLED LATER (each must be visible and distinguishable): {', '.join(job['labels'])}\n" if job["labels"] else "")
          + "Arrows, step numbers, captions and label text named in the description will be added LATER in code: do not require them, and do not fail the picture because they are absent or because simple arrows are drawn. "
          "Rules: the picture must contain NO text, letters, numbers, labels or captions. Check (1) every part and panel named in the description is present, "
          "correctly drawn, in the stated positions, counts, relative sizes and colours; (2) nothing extra or contradictory (for example organs shown when only the outside was asked); "
          "(3) the biology or science drawn is accurate. Judge it as a teacher choosing a textbook figure: set ok=true if it is accurate and usable for teaching, even if it is not perfect. "
          "Do NOT fail the picture for colour differences from the description (colours are soft guidance), artistic style, small differences of proportion, small differences in the number of minor repeated details (for example the exact number of cilia or gill filaments), or for things you cannot see clearly. "
          "Set ok=false only for a clear error that would mislead a student: a named part missing, a clearly wrong count of main structures, a wrong position or connection of main structures, extra contradictory content, or text in the picture. List only those errors in problems. "
          "ok=true only if the picture is accurate and usable. stray_text: 'none'; 'tiny' if there are only isolated small marks or a few characters; 'significant' if there are words or many characters. "
          "For tiny stray text give tiny_boxes as [x0,y0,x1,y1] integers on a 0-1000 scale (x right, y down) around each mark. "
          "alt: a plain-English alt text for the picture, at most 30 words, no brackets, no quotation marks."
          + (f"\nSUBJECT RULES (set ok=false if broken): {SUBJECT_RULES[SUBJECT]}" if SUBJECT in SUBJECT_RULES else ""))
    return vision(pr, [path], S_RAW, "check-raw")


def place_points(job, path, labels, feedback=""):
    pr = ("This is an unlabelled textbook illustration. Description: " + job["prompt"] + "\n"
          "For EACH label name below, give the point (x, y) on a 0-1000 scale (x right, y down, origin top-left of the image) where a pointer line should END: "
          "inside the named part (or exactly on the line for a vessel, wall or surface), at its most recognisable spot, clear of the edges of neighbouring parts. If the label names a REGION, layer or area (such as cortex, medulla, a chamber, a zone), put the point well inside the middle of that region, not on its edge. "
          "If a part appears more than once, choose the clearest one. If the label names a whole panel, stage or organism, give its centre. If the label is an annotation about a process, result or condition (for example a direction of flow, inspiration, oxygen in, a test result, a measurement), point to the arrow, region or structure where that happens. "
          "Return one entry per label, using the label text exactly as given.\nLABELS: " + json.dumps(labels)
          + (f"\nCORRECTIONS from the last attempt (fix these): {feedback}" if feedback else ""))
    r = vision(pr, [path], S_PTS, "place-labels", thinking="low")
    return {p["label"]: (p["x"], p["y"]) for p in r["points"]}


def check_labelled(job, path, labels):
    pr = ("This textbook image has text labels with pointer lines. Each pointer line ends in a dot on the part being named. "
          "Required labels: " + json.dumps(labels) + "\nDescription of the picture: " + job["prompt"] + "\n"
          "Be reasonable, not pixel-strict: a dot anywhere on the named part counts, and for region or process annotations (flow direction, inspiration, oxygen in, test results, measurements, whole-panel names) a dot on or right beside the relevant arrow, region or structure counts. For each label say ok=true only if its pointer dot sits on the correct part or region (not on a clearly different part, and not far out on empty background); otherwise ok=false and say in 'issue' which part it is actually on and where the right part is "
          "(left/right/above/below the dot). overlap=true if any label text overlaps another label or the picture. unreadable=true if any label is cut off or hard to read.")
    return vision(pr, [path], S_LCHK, "check-labelled", thinking="low")


# ---------------------------------------------------------------- generation

def gen_standard(job, model, prompt):
    check_cap()
    data, usage = gen.call_image(model, prompt + "\n\nStyle: " + style_of())
    cost = gen.cost_of(model, usage)
    Image.open(io.BytesIO(data)).convert("RGB").save(os.path.join(RAW, job["name"] + ".png"))
    with LOCK:
        with open(gen.COST_LOG, "a") as f:
            f.write(json.dumps({"name": job["name"], "subject": job["subject"], "model": model, "usage": usage, "cost": cost}) + "\n")
    return cost




def _reg_path():
    return os.path.join(WORK, f"batches-{SUBJECT}.json")          # one registry per subject, so parallel runs never touch each other's batches


def _reg():
    return json.load(open(_reg_path())) if os.path.exists(_reg_path()) else {}


def _reg_save(r):
    with LOCK:
        json.dump(r, open(_reg_path(), "w"), indent=1)


def _consume(resp, names, model):
    res = g.batch_results(resp); ok = {}
    for n in names:
        r, e = res.get(n, (None, {"message": "missing"}))
        try:
            cands = (r or {}).get("candidates") or []
            img = None
            for p_ in cands[0]["content"]["parts"]:
                d = p_.get("inlineData") or p_.get("inline_data")
                if d and d.get("data"):
                    img = base64.b64decode(d["data"]); break
            if not img:
                raise RuntimeError("no image")
            Image.open(io.BytesIO(img)).convert("RGB").save(os.path.join(RAW, n + ".png"))
            cost = gen.cost_of(model, r.get("usageMetadata", {})) * 0.5
            with LOCK:
                with open(gen.COST_LOG, "a") as f:
                    f.write(json.dumps({"name": n, "subject": SUBJECT, "model": model + "-batch", "usage": r.get("usageMetadata", {}), "cost": cost}) + "\n")
            ok[n] = True
        except Exception as ex_:
            print(f"[batch] {n}: {e or ex_}", flush=True); ok[n] = False
    return ok


def _wait(name, poll=30):
    t0 = time.time()
    while True:
        resp = g.get_batch(name); st = g.batch_state(resp)
        if resp.get("done") or st in ("BATCH_STATE_SUCCEEDED", "BATCH_STATE_FAILED", "BATCH_STATE_CANCELLED", "BATCH_STATE_EXPIRED"):
            break
        time.sleep(poll)
    print(f"[batch] {name} {st} after {time.time()-t0:.0f}s", flush=True)
    return resp


def recover_batches():
    """Fetch the results of any batch that was submitted but not consumed (for example after a restart)."""
    reg = _reg()
    for name, info in list(reg.items()):
        if info.get("done"):
            continue
        print(f"[batch] recovering {name} ({len(info['jobs'])} images)", flush=True)
        resp = _wait(name)
        _consume(resp, info["jobs"], info["model"])
        reg[name]["done"] = True; _reg_save(reg)


def batch_generate(jobs, model, label="imgs", poll=30, prompts=None):
    """Generate with the Batch API; returns {name: ok}. Cost assumed half of standard (unverified)."""
    reqs = {}
    for j in jobs:
        prompt = (prompts or {}).get(j["name"], j["prompt"]) + "\n\nStyle: " + style_of()
        reqs[j["name"]] = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
                           "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": "1:1"}}}
    name, _ = g.submit_batch(reqs, model, f"{SUBJ}-{label}")
    reg = _reg(); reg[name] = {"model": model, "jobs": list(reqs), "done": False}; _reg_save(reg)
    print(f"[batch] submitted {len(reqs)} {model} request(s) as {name}", flush=True)
    resp = _wait(name, poll)
    ok = _consume(resp, [j["name"] for j in jobs], model)
    reg = _reg(); reg[name]["done"] = True; _reg_save(reg)
    return ok


# ---------------------------------------------------------------- AI image processing (rounds)

def clean_prompt(s):
    s = re.sub(r"\bnumbered\b", "", s)
    s = re.sub(r"\bnumber(?:s|ing)? (?:1|one) to \w+\b", "", s)
    return re.sub(r"\s+", " ", s)


def raw_path(job):
    return os.path.join(RAW, job["name"] + ".png")


def label_stage(job, st, chk):
    """Place and check labels for a job whose raw image passed. Sets st['status'] to passed or failed."""
    name = job["name"]; raw = raw_path(job)
    spec = {}
    if chk["stray_text"] == "tiny" and chk.get("tiny_boxes"):
        spec["whiten"] = [[max(0, int(b[0] * 1.024) - 8), max(0, int(b[1] * 1.024) - 8), min(1024, int(b[2] * 1.024) + 8), min(1024, int(b[3] * 1.024) + 8)] for b in chk["tiny_boxes"] if len(b) == 4]
    st["alt"] = re.sub(r"[\[\]\"\n]", " ", chk["alt"]).strip()
    out = os.path.join(REPO, "subjects", job["subject"], "images")
    if job.get("caption"): spec["caption_below"] = job["caption"]
    if job.get("regions"): spec["regions"] = job["regions"]
    if not job["labels"]:
        lab.render(name, spec, out); st["spec"] = spec; st["status"] = "passed"; save_state(job, st); return
    labels = job["labels"]; pts = {}; feedback = ""; todo = list(labels); bad = []
    for attempt in range(3):
        newp = place_points(job, raw, todo, feedback)
        for l in todo:
            pts[l] = newp.get(l) or next((v for k, v in newp.items() if k.lower() == l.lower()), None)
        missing = [l for l in labels if pts.get(l) is None]
        if missing:
            feedback = "no point returned for: " + ", ".join(missing); todo = missing; continue
        spec2 = dict(spec)
        spec2["labels"] = [[l, [int(pts[l][0] * 1.024), int(pts[l][1] * 1.024)], "L" if pts[l][0] < 500 else "R"] for l in labels]
        lab.render(name, spec2, out)
        res = check_labelled(job, os.path.join(out, name + ".png"), labels)
        bad = [r for r in res["labels"] if not r["ok"]]
        st["log"].append({"label_attempt": attempt, "bad": [(b["label"], b.get("issue", "")) for b in bad], "overlap": res["overlap"], "unreadable": res["unreadable"]})
        if not bad and not res["unreadable"]:
            st["spec"] = spec2; st["status"] = "passed"; st["overlap_flag"] = bool(res["overlap"]); save_state(job, st); return
        todo = [b["label"] for b in bad] or labels
        feedback = "; ".join(f"{b['label']}: {b.get('issue','wrong part')}" for b in bad)
    if len(bad) == 1 and len(labels) >= 4 and bad[0]["label"] in labels:      # one part is not visible in the picture: leave that label out and say so
        keep = [e for e in spec2["labels"] if e[0] != bad[0]["label"]]
        spec3 = dict(spec2); spec3["labels"] = keep
        lab.render(name, spec3, out)
        st["spec"] = spec3; st["status"] = "passed"; st["dropped_labels"] = [bad[0]["label"]]; save_state(job, st); return
    st["status"] = "failed"; st["reason"] = "labels still wrong after 3 placements: " + "; ".join(b["label"] for b in bad)
    try:
        os.replace(os.path.join(out, name + ".png"), os.path.join(FAIL_DIR, name + "-labelled.png"))
    except OSError:
        pass
    save_state(job, st)


def run_ai(jobs, workers, use_batch=True, pre_generated=()):
    """Generate -> check (rounds 0..2, retries on Pro with the problems fed back) -> label. Returns nothing; state in job files."""
    jobs = [j for j in jobs if not j["code"] and load_state(j)["status"] not in ("passed", "failed")]
    if not jobs:
        return
    states = {j["name"]: load_state(j) for j in jobs}
    for s in states.values():
        s.setdefault("log", []); s["status"] = "working"
    fb = {}; chks = {}; active = list(jobs); passed = []
    def prompt_of(j):
        return clean_prompt(j["prompt"]) + ("" if j["name"] not in fb else " IMPORTANT corrections from the previous attempt (fix these): " + fb[j["name"]])
    for rnd in range(ROUNDS):
        if not active or STOP.is_set():
            break
        need = [j for j in active if not os.path.exists(raw_path(j))]
        pro_round = rnd > 0
        for model in (FLASH_IMG, PRO_IMG):
            grp = [j for j in need if (PRO_IMG if rnd >= 1 else j["model"]) == model]
            if not grp:
                continue
            ok = {}
            try:
                if use_batch:
                    check_cap(0.04 * len(grp))
                    ok = batch_generate(grp, model, label=f"r{rnd}-{model[-9:]}", prompts={j["name"]: prompt_of(j) for j in grp})
            except Capped:
                break
            def one(j, model=model):
                if ok.get(j["name"]):
                    return
                try:
                    gen_standard(j, model, prompt_of(j))
                except Capped:
                    pass
                except Exception as e:
                    print(f"[gen-error] {j['name']}: {g.scrub(str(e))[:200]}", flush=True)
            with ThreadPoolExecutor(workers) as ex_:
                list(ex_.map(one, grp))
        def chk_one(j):
            if not os.path.exists(raw_path(j)):
                return j, None
            try:
                c = check_raw(j, raw_path(j))
            except Capped:
                return j, None
            except Exception as e:
                print(f"[check-error] {j['name']}: {g.scrub(str(e))[:200]}", flush=True); return j, None
            if j["name"] in ACCEPT and c["stray_text"] != "significant":
                c["ok"] = True
            return j, c
        with ThreadPoolExecutor(workers) as ex_:
            results = list(ex_.map(chk_one, active))
        nxt = []
        for j, c in results:
            s = states[j["name"]]
            if c is None:
                continue
            s["log"].append({"round": rnd, "ok": c["ok"], "problems": c["problems"], "stray": c["stray_text"]})
            if c["ok"] and c["stray_text"] != "significant":
                chks[j["name"]] = c; passed.append(j)
            else:
                fb[j["name"]] = "; ".join(c["problems"][:5]) or "the picture must contain no text, letters or numbers"
                s["reason"] = "raw check: " + fb[j["name"]]
                os.replace(raw_path(j), os.path.join(FAIL_DIR, f"{j['name']}-try{rnd}.png"))
                nxt.append(j)
        active = nxt
        print(f"[round {rnd}] passed so far {len(passed)}, still to fix {len(active)}, spend ${spent():.2f}", flush=True)
    for j in active:
        s = states[j["name"]]; s["status"] = "failed"; save_state(j, s)
    def lab_one(j):
        s = states[j["name"]]
        try:
            label_stage(j, s, chks[j["name"]])
        except Capped:
            s["status"] = "pending"; save_state(j, s)
        except Exception as e:
            print(f"[label-error] {j['name']}: {g.scrub(str(e))[:200]}", flush=True)
            s["status"] = "failed"; s["reason"] = "label error: " + g.scrub(str(e))[:150]; save_state(j, s)
    with ThreadPoolExecutor(workers) as ex_:
        list(ex_.map(lab_one, passed))


# ---------------------------------------------------------------- code-drawn images

ALLOWED = {"numpy", "matplotlib", "math", "style", "itertools", "textwrap", "colorsys"}
BANNED = {"open", "exec", "eval", "compile", "__import__", "input", "globals", "locals", "getattr", "setattr", "breakpoint"}
CODE_SYS = """You write Python (matplotlib + numpy) functions that draw exact textbook diagrams as PNG files.
Write ONE file that defines `def draw(out):` and nothing else executable (no top-level code besides imports and helper functions). Begin with `from style import *` (this gives: plt, np via `import numpy as np` which you must import yourself, canvas(w,h), save(fig, path), the colours INK, GREEN, BLUE, PINK, LAV, CREAM, ORANGE, GREY, the dict DEEP with keys green/blue/pink/orange/lav, and the helpers axes_clean(ax, xlabel, ylabel, xmax, ymax), country_polys(*names), continent_polys('Africa'|'World'|...), nigeria_poly()). Always finish with save(fig, out).
Rules: only import numpy, matplotlib, math, itertools, textwrap and style. No file or network access. Use the soft palette (GREEN, BLUE, PINK, LAV, CREAM, ORANGE, GREY, ink text, white background; DEEP colours for lines). Use fontsize 14 to 18 (never smaller than 14) so all text is readable on a phone; never let text overlap other text or lines (use white bbox behind labels where lines pass); keep everything inside the canvas. Include EVERY title, label, axis name, key and annotation that the description names, spelled exactly as in the description, and nothing that contradicts it. Maps are simplified sketches: use the Natural Earth helpers for real outlines, shade zones as simple bands or polygons, add a small caption 'Sketch map: zones are approximate' where positions are schematic. Apply scientific accuracy (curve shapes, labelled structure positions, cycle direction, flow arrows). Output ONLY the Python code, no markdown fences."""
CODE_EX = open(os.path.join(HERE, "codedraw", "samples.py")).read()
CODE_EX = CODE_EX[CODE_EX.index("def bio_photosynthesis_graph(out):"):CODE_EX.index("def hist_timeline(out):")]


def check_code_ast(code):
    tree = ast.parse(code)
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name.split(".")[0] not in ALLOWED: raise ValueError("import not allowed: " + a.name)
        elif isinstance(n, ast.ImportFrom):
            if (n.module or "").split(".")[0] not in ALLOWED: raise ValueError("import not allowed: " + str(n.module))
        elif isinstance(n, ast.Name) and n.id in BANNED:
            raise ValueError("name not allowed: " + n.id)
        elif isinstance(n, ast.Attribute) and n.attr.startswith("__"):
            raise ValueError("dunder attribute not allowed")


def write_code(job, prev_code="", problems=None, pro=False):
    check_cap(0.05)
    parts = [{"text": f"Example of the expected style (a different image):\n{CODE_EX}\n\nNow write the file for this description:\n{job['full']}"}]
    if prev_code:
        parts.append({"text": f"\nYour previous code:\n{prev_code}\n\nProblems found when it was run and checked (fix all of them, keep what was right):\n- " + "\n- ".join(problems or [])})
    r = g.call_gemini(parts, system=CODE_SYS, model=TXT_PRO if pro else TXT_FLASH, thinking="low", subject=SUBJ, task="code-draw", timeout=600, attempts=4)
    t = r["text"].strip()
    m = re.match(r"^```(?:python)?\s*\n(.*)\n```$", t, re.S)
    return (m.group(1) if m else t)


def run_code(job, code):
    check_code_ast(code)
    d = os.path.join(CODE_DIR, "gen"); os.makedirs(d, exist_ok=True)
    pyf = os.path.join(d, job["name"] + ".py"); out = os.path.join(CODE_DIR, job["name"] + ".png")
    if os.path.exists(out): os.remove(out)
    header = f"import sys\nsys.path.insert(0, {os.path.join(HERE, 'codedraw')!r})\n"
    open(pyf, "w").write(header + code + "\n\nif __name__ == '__main__':\n    draw(sys.argv[1])\n")
    p = subprocess.run([sys.executable, "-I", pyf, out], capture_output=True, text=True, timeout=120, cwd=d)
    if p.returncode != 0 or not os.path.exists(out):
        raise RuntimeError((p.stderr or "no output")[-600:])
    return out


def check_code_img(job, path):
    pr = ("You are checking a code-drawn textbook diagram against its description.\n"
          f"DESCRIPTION: {job['full']}\n"
          "Judge as a teacher choosing a textbook figure. ok=true if the content is correct and complete enough to teach from: every main item, label, title and axis in the description is present, shapes, directions and values are right, all text is readable and nothing overlaps (text on text, text on lines, text cut off by the edge), and nothing contradicts the description. Do NOT fail for paraphrased or slightly shortened wording, colours, style, plain text without a box, or empty space; fail only for a missing or wrong main item, a wrong direction or connection, a misleading shape, unreadable or overlapping text. "
          "List every problem concisely in 'problems' (what is wrong and where). stray_text: set to 'none'. alt: plain-English alt text, at most 30 words, no brackets, no quotation marks.")
    return vision(pr, [path], S_RAW, "check-code", thinking="medium")


TEMPLATE_NAMES = {"flowchart", "cycle", "hub", "graph", "chart", "table", "timeline", "taccount"}
sys.path.insert(0, os.path.join(HERE, "codedraw"))
import templates as tpl
TPL_SYS = ("You turn a textbook figure description into a JSON spec for a FIXED drawing template. Output ONLY one JSON object, no markdown.\n"
           "The object must have \"template\": the template name you are told to use, and the fields documented below. The template does the layout, so you give only content.\n"
           "Rules: include EVERY item, label, title, axis name, value and annotation the description names, spelled exactly as in the description, and nothing that contradicts it. "
           "Keep each text short (under 8 words); put detail in separate nodes only when the description lists it. Flowcharts: at most 4 nodes in one row and 9 layers; give every edge a from and to; label decision branches (yes/no). "
           "Graphs: give coordinates on a 0-10 scale (xmax and ymax 10) so curves have the right shape (demand slopes down, supply up, U-shaped cost curves, S-curves etc.); name every curve with 'label'; mark intersections with 'guides' (dashed lines to the axes with x_text and y_text). "
           "Tables: put the column headings in 'columns' and one list per row. Scientific and factual accuracy matters: do not invent facts beyond the description.\n\nTEMPLATE DOCUMENTATION:\n" + tpl.__doc__)


def write_spec(job, prev="", problems=None, pro=False):
    check_cap(0.05)
    parts = [{"text": f"Use template: {job['template']}\nDescription of the figure:\n{job['full']}"}]
    if prev:
        parts.append({"text": f"\nYour previous JSON:\n{prev}\n\nProblems found in the drawn result (fix all of them, keep what was right):\n- " + "\n- ".join(problems or [])})
    r = g.call_gemini(parts, system=TPL_SYS, model=TXT_PRO if pro else TXT_FLASH, thinking="low", subject=SUBJ, task="code-spec", timeout=600, attempts=4)
    t = r["text"].strip()
    m = re.match(r"^```(?:json)?\s*\n(.*)\n```$", t, re.S)
    t = m.group(1) if m else t
    spec = json.loads(t)
    if isinstance(spec, list): spec = spec[0]
    spec["template"] = job["template"]
    return json.dumps(spec, ensure_ascii=False, indent=1)


def run_spec(job, text):
    d = os.path.join(CODE_DIR, "gen"); os.makedirs(d, exist_ok=True)
    pj = os.path.join(d, job["name"] + ".json"); out = os.path.join(CODE_DIR, job["name"] + ".png")
    if os.path.exists(out): os.remove(out)
    open(pj, "w").write(text)
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, "codedraw", "render_spec.py"), pj, out], capture_output=True, text=True, timeout=180, cwd=d)
    if p.returncode != 0 or not os.path.exists(out):
        raise RuntimeError((p.stderr or "no output")[-600:])
    return out


def process_code(job):
    st = load_state(job)
    if st["status"] in ("passed", "failed"):
        return st
    name = job["name"]; st["status"] = "working"; st.setdefault("log", [])
    tpl_first = job["template"] in TEMPLATE_NAMES
    routes = ["tpl", "tpl", "tpl", "free", "free"] if tpl_first else ["free"] * 3      # a template that cannot express the figure falls back to free-form code
    if CODE_ATTEMPTS: routes = routes[:CODE_ATTEMPTS]
    code = ""; problems = []; out = None; last = None
    for attempt, route in enumerate(routes):
        use_tpl = route == "tpl"
        if route != last: code = ""                  # new route: start from scratch but keep the problems as hints
        last = route
        try:
            if use_tpl:
                code = write_spec(job, code, problems, pro=PRO_CODE or attempt == 2); out = run_spec(job, code)
            else:
                code = write_code(job, code, problems, pro=PRO_CODE or attempt >= len(routes) - 1); out = run_code(job, code)
        except Capped:
            raise
        except Exception as e:
            problems = [f"the code failed: {str(e)[-300:]}"]; st["log"].append({"attempt": attempt, "error": problems[0]}); out = None; continue
        w_, h_ = Image.open(out).size
        if h_ / w_ > (4.5 if tpl_first and job["template"] in ("flowchart", "cycle", "timeline") else 2.2) or w_ / h_ > 3.2:
            problems = [f"the drawing is stretched ({w_}x{h_} px): keep annotations close to the drawing, with no long leader lines, and a roughly square or landscape layout"]
            st["log"].append({"attempt": attempt, "ok": False, "problems": problems}); continue
        chk = check_code_img(job, out)
        st["log"].append({"attempt": attempt, "ok": chk["ok"], "problems": chk["problems"]})
        if chk["ok"]:
            dest = os.path.join(REPO, "subjects", job["subject"], "images", name + ".png")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            Image.open(out).convert("RGB").save(dest, optimize=True)
            st["alt"] = re.sub(r"[\[\]\"\n]", " ", chk["alt"]).strip(); st["status"] = "passed"; st["code_ext"] = "json" if use_tpl else "py"
            cdir = os.path.join(REPO, "tools", "specs", job["subject"], "code"); os.makedirs(cdir, exist_ok=True)
            open(os.path.join(cdir, name + "." + st["code_ext"]), "w").write(code + "\n")
            save_state(job, st); return st
        problems = chk["problems"]
    st["status"] = "failed"; st["reason"] = "code image: " + "; ".join(problems[:4])
    if out and os.path.exists(out):
        os.replace(out, os.path.join(FAIL_DIR, name + "-code.png"))
    save_state(job, st); return st


# ---------------------------------------------------------------- notes, commit

import fcntl, contextlib


@contextlib.contextmanager
def filelock():
    """One git writer at a time across all running processes."""
    with open(os.path.join(WORK, "git.lock"), "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def finalize_file(topic, jobs, push=False):
    subject = jobs[0]["subject"]; md = os.path.join("subjects", subject, topic + ".md")
    done = []
    for j in jobs:
        st = load_state(j)
        if st["status"] == "passed" and not st.get("placed"):
            done.append((j, st))
    if not done:
        return
    with GITLOCK, filelock():
        args = [f"{j['slot']}:{j['name']}={st['alt'] or j['kind']}" for j, st in done]
        r = subprocess.run([sys.executable, os.path.join(HERE, "place_images.py"), os.path.join(REPO, md)] + args, capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print("PLACE FAILED", topic, r.stdout[-300:], r.stderr[-300:], flush=True); return
        subprocess.run([sys.executable, os.path.join(HERE, "compress_images.py"), os.path.join("subjects", subject, "images")], capture_output=True, text=True, cwd=REPO)
        sd = os.path.join(REPO, "tools", "specs", subject); os.makedirs(sd, exist_ok=True)
        specs = {j["name"]: st["spec"] for j, st in done if st.get("spec") is not None}
        if specs:
            p = os.path.join(sd, topic + "-labels.json"); old = json.load(open(p)) if os.path.exists(p) else {}
            old.update(specs); json.dump(old, open(p, "w"), indent=1)
        pj = os.path.join(sd, topic + "-prompts.json")
        old = {n: pr for n, pr in (json.load(open(pj)) if os.path.exists(pj) else [])}
        for j, st in done: old[j["name"]] = j["prompt"]
        json.dump([[n, pr] for n, pr in old.items()], open(pj, "w"), indent=1, ensure_ascii=False)
        add = [md, os.path.join("tools", "specs", subject, topic + "-prompts.json")]
        if specs: add.append(os.path.join("tools", "specs", subject, topic + "-labels.json"))
        for j, st in done:
            add.append(os.path.join("subjects", subject, "images", j["name"] + ".png"))
            cf = os.path.join("tools", "specs", subject, "code", j["name"] + "." + st.get("code_ext", "py"))
            if j["code"] and os.path.exists(os.path.join(REPO, cf)): add.append(cf)
        subprocess.run(["git", "add"] + add, cwd=REPO)
        n_ai = sum(1 for j, _ in done if not j["code"]); n_code = len(done) - n_ai
        subprocess.run(["git", "commit", "-q", "-m", f"Add images to {subject} {topic}: {n_ai} AI, {n_code} code-drawn\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01AuzkMMKKHsgCscpXnvCsGG"], cwd=REPO, capture_output=True)
        for j, st in done:
            st["placed"] = True; save_state(j, st)
        if push:
            subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=REPO, capture_output=True)
    print(f"[done] {topic}: placed {len(done)} image(s), spend ${spent():.2f}", flush=True)


# ---------------------------------------------------------------- main

def run(jobs, workers, use_batch=True, chunk=45, push_every=2):
    """Process jobs in chunks of whole notes files: AI images by rounds, code images in parallel, then place and commit each file."""
    by_file = {}
    for j in jobs:
        if j.get("skip"):
            st = load_state(j); st["status"] = "skipped"; st["reason"] = "portrait of a real person or Arabic script: placeholder kept"; save_state(j, st); continue
        by_file.setdefault(j["topic"], []).append(j)
    chunks, cur, n = [], [], 0
    for topic, js in by_file.items():
        cur.append(topic); n += len(js)
        if n >= chunk: chunks.append(cur); cur, n = [], 0
    if cur: chunks.append(cur)
    recover_batches()
    done_files = 0
    for ch in chunks:
        if STOP.is_set(): break
        cj = [j for t_ in ch for j in by_file[t_]]
        print(f"[chunk] {len(cj)} images in {', '.join(ch)}", flush=True)
        run_ai(cj, workers, use_batch)
        def cwork(j):
            try:
                if STOP.is_set(): return
                process_code(j)
            except Capped as e:
                print(f"[stop] {j['name']}: {e}", flush=True)
            except Exception as e:
                print(f"[error] {j['name']}: {type(e).__name__}: {g.scrub(str(e))[:300]}", flush=True)
                s = load_state(j); s["status"] = "failed"; s["reason"] = "error: " + g.scrub(str(e))[:200]; save_state(j, s)
        with ThreadPoolExecutor(workers) as ex_:
            list(ex_.map(cwork, [j for j in cj if j["code"] and load_state(j)["status"] not in ("passed", "failed")]))
        for t_ in ch:
            done_files += 1
            finalize_file(t_, by_file[t_], push=(done_files % push_every == 0))
    subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=REPO, capture_output=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--subject", default="biology"); ap.add_argument("--files", nargs="*", default=[])
    ap.add_argument("--run", action="store_true"); ap.add_argument("--status", action="store_true")
    ap.add_argument("--workers", type=int, default=6); ap.add_argument("--limit", type=int)
    ap.add_argument("--no-batch", action="store_true", help="use standard calls instead of the Batch API")
    ap.add_argument("--chunk", type=int, default=45, help="images per chunk (whole notes files)")
    ap.add_argument("--only", nargs="*", help="only these image names")
    ap.add_argument("--accept", nargs="*", default=[], help="names of raw images accepted after I looked at them")
    ap.add_argument("--rounds", type=int, default=2); ap.add_argument("--code-attempts", type=int); ap.add_argument("--pro", action="store_true", help="Pro for AI round 0 and for code from the first attempt"); ap.add_argument("--simplified", help="JSON file name -> simplified description")
    ap.add_argument("--no-code", action="store_true"); ap.add_argument("--no-ai", action="store_true")
    ap.add_argument("--retry-failed", choices=["code", "ai", "all"], help="reset failed jobs of this kind to pending and run them again (new generation, new tries)")
    a = ap.parse_args()
    ACCEPT.update(a.accept)
    global SUBJECT, SUBJ, ROUNDS, CODE_ATTEMPTS, PRO_CODE
    SUBJECT = a.subject; SUBJ = a.subject + "-images2"; ROUNDS = a.rounds; CODE_ATTEMPTS = a.code_attempts; PRO_CODE = a.pro
    if a.simplified: SIMPLIFIED.update(json.load(open(a.simplified)))
    jobs = load_jobs(a.subject, a.files)
    if a.pro:
        for j in jobs: j["model"] = PRO_IMG
    if a.only: jobs = [j for j in jobs if j["name"] in a.only]
    if a.no_code: jobs = [j for j in jobs if not j["code"]]
    if a.no_ai: jobs = [j for j in jobs if j["code"]]
    if a.limit: jobs = jobs[: a.limit]
    if a.retry_failed:
        for j in jobs:
            st = load_state(j)
            if st["status"] == "failed" and (a.retry_failed == "all" or (a.retry_failed == "code") == j["code"]):
                for p in (os.path.join(RAW, j["name"] + ".png"),):
                    if os.path.exists(p): os.remove(p)
                save_state(j, {"status": "pending", "cost_note": 0, "retry": st.get("retry", 0) + 1})
    if a.status:
        c = {}
        for j in jobs: c[load_state(j)["status"]] = c.get(load_state(j)["status"], 0) + 1
        print(len(jobs), "jobs", c, f"spend ${spent():.2f}"); return
    todo = [j for j in jobs if load_state(j)["status"] not in ("passed", "failed", "skipped")]
    if a.run:
        run(todo, a.workers, use_batch=not a.no_batch, chunk=a.chunk)
    print(f"spend ${spent():.2f}")


if __name__ == "__main__":
    main()
