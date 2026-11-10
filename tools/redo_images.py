#!/usr/bin/env python3
"""Regenerate pictures that have a factual drawing mistake or a crowded multi-panel layout (Gemini Pro image model, Batch API).

  python tools/redo_images.py [--only NAME ...] [--limit N] [--budget 29]

Per picture: generate with gemini-3-pro-image (the exact mistake to avoid is written into the prompt) -> check with Gemini PRO against the
description, the labels and the notes text (up to 2 tries) -> place label points (Gemini vision) and draw labels with label.py (panel
names become captions under their panels) -> check the labels. If it still fails, the picture is removed and the [IMAGE: ...] placeholder is
put back in the notes.
"""
import argparse, glob, io, json, os, re, subprocess, sys, shutil
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
import audit_panels as ap, fix_panels as fp, verify_panels as vp, redo_common as rc, label as lab
from common import RAW, WORK, REPO

PANEL_NOTE = (" LAYOUT: draw every panel or organism separately, far apart from the others, with wide empty white space between them, and leave an empty white band under each one for a caption. "
              "Do not let drawings touch or overlap. Do not draw arrows or lines between panels unless the description requires them.")


def pre_commit():
    h = subprocess.check_output(["git", "log", "--grep", "Panel audit tools", "--format=%H", "-1"], cwd=REPO, text=True).strip()
    return h + "^"


def old_spec(sub, topic, name, pre):
    r = subprocess.run(["git", "show", f"{pre}:tools/specs/{sub}/{topic}-labels.json"], cwd=REPO, capture_output=True, text=True)
    return json.loads(r.stdout).get(name, {}) if r.returncode == 0 else {}


def build_jobs(only=None):
    audit = json.load(open(os.path.join(WORK, "audit.json"))); tri = json.load(open(os.path.join(WORK, "triage.json")))
    unres = json.load(open(os.path.join(WORK, "panel_final.json")))["unres"]
    pre = pre_commit(); jobs = []
    names = [n for n, t in tri.items() if t["category"] == "factual"] + [n for n in unres if not (n in tri and tri[n]["category"] == "factual")]
    for n in names:
        if only and n not in only: continue
        a = audit[n]; sub, topic = a["subject"], a["topic"]
        spec = old_spec(sub, topic, n, pre) or rc.spec_for(n, sub, topic)
        base = rc.prompt_for(n, sub, topic)
        if not base: continue
        fix = tri[n]["fix"] if n in tri and tri[n]["category"] == "factual" else ""
        panel = n in unres
        labels_all = [e[0] for e in spec.get("labels", [])]
        notes = rc.notes_excerpt(sub, topic, base + " " + " ".join(labels_all), 1400)
        jobs.append(dict(name=n, subject=sub, topic=topic, prompt=m.clean_prompt(base), fix=fix, panel=panel, labels=labels_all, spec=spec, notes=notes,
                         code=False, group="AI", kind=("factual" if fix else "") + ("+panel" if panel and fix else "panel" if panel else ""), model=m.PRO_IMG, status="working", log=[]))
    return jobs


def prompt_of(j):
    p = j["prompt"]
    if j["fix"]: p += " IMPORTANT, exact mistake to avoid: " + j["fix"]
    if j["panel"]: p += PANEL_NOTE
    if j.get("fb"): p += " IMPORTANT corrections from the previous attempt (fix these): " + j["fb"]
    return m.clean_prompt(p)


def check_pro(j, path):
    pr = ("You are a careful science teacher checking a NEW textbook illustration (made by an image model, no text allowed in it; labels are added later in code).\n"
          f"DESCRIPTION IT MUST MATCH: {j['prompt'][:1500]}\n"
          + (f"A PREVIOUS VERSION HAD THIS MISTAKE, which must NOT appear again: {j['fix']}\n" if j["fix"] else "")
          + (f"LABELS THAT WILL BE ADDED (each named part must be visible): {', '.join(j['labels'][:30])}\n" if j["labels"] else "")
          + (f"NOTES TEXT STUDENTS READ (the picture must not contradict it):\n{j['notes']}\n" if j["notes"] else "")
          + "Set ok=true only if the picture is accurate and usable for teaching: all required parts present and correct (counts, positions, colours, connections, directions), the specific mistake above is absent, nothing contradicts the notes, and it contains NO text, letters or numbers. "
          + ("It must show separate panels clearly apart from each other with free space under each. " if j["panel"] else "")
          + "Do not fail for style, colour tone, small proportions or details the description and notes do not require. problems: list only real errors. stray_text: 'none', 'tiny' (isolated marks) or 'significant'; for tiny give tiny_boxes [x0,y0,x1,y1] on a 0-1000 scale. alt: plain alt text, at most 30 words, no brackets or quotes.")
    return m.vision(pr, [path], m.S_RAW, "redo-check-pro", model=m.TXT_PRO, thinking="low")


def generate(jobs, rnd):
    todo = [j for j in jobs if j["status"] == "working"]
    for j in todo:
        p = os.path.join(RAW, j["name"] + ".png")
        if os.path.exists(p): os.remove(p)
    for k in range(0, len(todo), 60):
        chunk = todo[k:k + 60]
        ok = {}
        try:
            m.check_cap(0.1 * len(chunk))
            ok = m.batch_generate(chunk, m.PRO_IMG, label=f"redo-r{rnd}-{k}", prompts={j["name"]: prompt_of(j) for j in chunk})
        except m.Capped:
            for j in chunk: j["status"] = "capped"
            continue
        for j in chunk:
            if not ok.get(j["name"]) and not os.path.exists(os.path.join(RAW, j["name"] + ".png")):
                try: m.gen_standard(j, m.PRO_IMG, prompt_of(j))
                except Exception as e: print("gen error", j["name"], str(e)[:100], flush=True)


def check_all(jobs, rnd, workers):
    def one(j):
        if j["status"] != "working": return
        p = os.path.join(RAW, j["name"] + ".png")
        if not os.path.exists(p): j["log"].append({"round": rnd, "ok": False, "problems": ["no image returned"]}); j["fb"] = ""; return
        try: c = check_pro(j, p)
        except m.Capped: j["status"] = "capped"; return
        except Exception as e: print("check error", j["name"], str(e)[:100], flush=True); return
        j["log"].append({"round": rnd, "ok": c["ok"], "problems": c["problems"], "stray": c["stray_text"]})
        if c["ok"] and c["stray_text"] != "significant":
            j["chk"] = c; j["status"] = "checked"
        else:
            j["fb"] = "; ".join(c["problems"][:5]) or "the picture must contain no text, letters or numbers"
            j["reason"] = "Pro check: " + j["fb"]
    with ThreadPoolExecutor(workers) as ex: list(ex.map(one, jobs))


def label_new(j):
    n = j["name"]; raw = os.path.join(RAW, n + ".png"); out = os.path.join(REPO, "subjects", j["subject"], "images")
    spec_old = j["spec"]; chk = j["chk"]
    base = {}
    if chk["stray_text"] == "tiny" and chk.get("tiny_boxes"):
        base["whiten"] = [[max(0, int(b[0] * 1.024) - 8), max(0, int(b[1] * 1.024) - 8), min(1024, int(b[2] * 1.024) + 8), min(1024, int(b[3] * 1.024) + 8)] for b in chk["tiny_boxes"] if len(b) == 4]
    for k in ("regions", "caption_below"):
        if spec_old.get(k): base[k] = spec_old[k]
    labels = j["labels"]
    if not labels:
        lab.render(n, base, out); j["spec_new"] = base; j["status"] = "passed"; j["alt"] = chk["alt"]; return
    job = dict(name=n, subject=j["subject"], prompt=j["prompt"], labels=labels, code=False)
    pts = {}; feedback = ""; todo = list(labels); bad = []
    for att in range(3):
        newp = m.place_points(job, raw, todo, feedback)
        for l in todo: pts[l] = newp.get(l) or next((v for k_, v in newp.items() if k_.lower() == l.lower()), None)
        missing = [l for l in labels if pts.get(l) is None]
        if missing: feedback = "no point returned for: " + ", ".join(missing); todo = missing; continue
        spec0 = dict(base); spec0["labels"] = [[l, [int(pts[l][0] * 1.024), int(pts[l][1] * 1.024)], "L" if pts[l][0] < 500 else "R"] for l in labels]
        spec = spec0
        if j["panel"]:
            au = ap.audit(n, j["prompt"], labels)
            if len(au["panels"]) >= 2:
                spec, info = fp.plan(n, spec0, au, False)
                for k in ("regions", "caption_below", "whiten"):
                    if k in base: spec[k] = base[k]
        lab.render(n, spec, out)
        ptr = [e[0] for e in spec["labels"]]
        res = m.check_labelled(job, os.path.join(out, n + ".png"), ptr) if ptr else {"labels": [], "unreadable": False}
        bad = [r for r in res["labels"] if not r["ok"]]
        pv = {}
        if j["panel"]:
            pv = m.vision(vp.PR, [os.path.join(out, n + ".png")], vp.SCHEMA, "redo-panels", thinking="low")
        panel_bad = bool(pv and (pv.get("caption_overlaps") or pv.get("line_through_other_panel") or pv.get("names_as_pointer_labels")))
        j["log"].append({"label_attempt": att, "bad": [(b["label"], b.get("issue", "")) for b in bad], "panel": pv.get("details", "") if pv else ""})
        if not bad and not res.get("unreadable") and not panel_bad:
            j["spec_new"] = spec; j["status"] = "passed"; j["alt"] = chk["alt"]; j["panel_note"] = pv.get("details", ""); return
        todo = [b["label"] for b in bad] or labels
        feedback = "; ".join(f"{b['label']}: {b.get('issue', 'wrong part')}" for b in bad)
        if panel_bad and not bad: feedback = "panel layout: " + pv.get("details", "")
    j["status"] = "failed"; j["reason"] = "labels or layout still wrong after 3 placements: " + "; ".join(b["label"] for b in bad) + (" " + j.get("panel_note", ""))


def remove_image(j):
    p = os.path.join(REPO, "subjects", j["subject"], "images", j["name"] + ".png")
    if os.path.exists(p): os.remove(p)
    ok = rc.restore_placeholder(j["subject"], j["topic"], j["name"])
    sp = os.path.join(REPO, "tools", "specs", j["subject"], j["topic"] + "-labels.json")
    d = json.load(open(sp)); d.pop(j["name"], None); json.dump(d, open(sp, "w"), indent=1, ensure_ascii=False)
    return ok


def main():
    ap_ = argparse.ArgumentParser(); ap_.add_argument("--only", nargs="*"); ap_.add_argument("--limit", type=int); ap_.add_argument("--budget", type=float, default=29.0); ap_.add_argument("--workers", type=int, default=8)
    a = ap_.parse_args()
    m.SUBJECT = "redo"; m.SUBJ = "redo-images2"
    base = m.spent(); m.CAP = base + a.budget
    jobs = build_jobs(a.only)
    outp0 = os.path.join(WORK, "redo_results.json")
    if os.path.exists(outp0) and not a.only:
        done = {n for n, v in json.load(open(outp0)).items() if v["status"] in ("passed", "failed")}
        jobs = [j for j in jobs if j["name"] not in done]
    if a.limit: jobs = jobs[:a.limit]
    print(len(jobs), "jobs;", sum(1 for j in jobs if j["fix"]), "factual;", sum(1 for j in jobs if j["panel"]), "panel", flush=True)
    m.recover_batches() if False else None
    for rnd in range(2):
        generate(jobs, rnd); check_all(jobs, rnd, a.workers)
        print(f"[round {rnd}] checked ok: {sum(1 for j in jobs if j['status']=='checked')}, to retry: {sum(1 for j in jobs if j['status']=='working')}, spend ${m.spent()-base:.2f}", flush=True)
    for j in jobs:
        if j["status"] == "working": j["status"] = "failed"
    def lab_one(j):
        if j["status"] != "checked": return
        try: label_new(j)
        except m.Capped: j["status"] = "capped"
        except Exception as e: j["status"] = "failed"; j["reason"] = "label error: " + str(e)[:150]
    with ThreadPoolExecutor(a.workers) as ex: list(ex.map(lab_one, jobs))
    removed = []
    for j in jobs:
        if j["status"] == "failed":
            ok = remove_image(j); j["removed"] = True; j["restored"] = ok; removed.append(j["name"])
        elif j["status"] == "passed":
            sp = os.path.join(REPO, "tools", "specs", j["subject"], j["topic"] + "-labels.json")
            d = json.load(open(sp)); d[j["name"]] = j["spec_new"]; json.dump(d, open(sp, "w"), indent=1, ensure_ascii=False)
    res = {j["name"]: {k: j.get(k) for k in ("subject", "topic", "status", "kind", "fix", "reason", "removed", "restored", "log", "alt", "panel_note")} for j in jobs}
    outp = os.path.join(WORK, "redo_results.json"); old = json.load(open(outp)) if os.path.exists(outp) else {}
    old.update(res); json.dump(old, open(outp, "w"), indent=1, ensure_ascii=False)
    import collections
    print(collections.Counter(j["status"] for j in jobs), f"spend ${m.spent()-base:.2f}")


if __name__ == "__main__":
    main()
