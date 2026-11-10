#!/usr/bin/env python3
"""Decide which removed multi-panel images to restore: take the version before the panel audit and check the DRAWING only (Gemini Pro)
against its placeholder and the notes text. Correct drawing -> restore image, notes line and label spec. Factual mistake -> keep placeholder.
python tools/restore_removed.py"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m, redo_common as rc, redo_images as ri
from common import WORK, REPO

SC = {"type": "OBJECT", "properties": {"correct": {"type": "BOOLEAN"}, "mistakes": {"type": "ARRAY", "items": {"type": "STRING"}}}, "required": ["correct", "mistakes"]}
SLOT = r"^(\[IMAGE:.*\]\s*$|!\[.*\]\(images/.*\.png\)\s*$)"


def git_show(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def main():
    m.SUBJECT = "restore"; m.SUBJ = "restore-images2"
    cands = json.load(open(os.path.join(WORK, "restore_cands.json")))
    audit = json.load(open(os.path.join(WORK, "audit.json"))); pre = ri.pre_commit(); last = "83e367a"
    res = {}
    def check(n):
        a = audit[n]; sub, topic = a["subject"], a["topic"]
        img = git_show(pre, f"subjects/{sub}/images/{n}.png")
        md = open(os.path.join(REPO, "subjects", sub, topic + ".md")).read().split("\n")
        old_md = (git_show(last, f"subjects/{sub}/{topic}.md") or b"").decode().split("\n")
        slots = [i for i, l in enumerate(md) if re.match(SLOT, l)]; oslots = [i for i, l in enumerate(old_md) if re.match(SLOT, l)]
        oi = next((i for i in oslots if f"images/{n}.png)" in old_md[i]), None)
        if img is None or oi is None: res[n] = dict(status="missing", why="no earlier version"); return
        slot = oslots.index(oi)
        if slot >= len(slots) or not md[slots[slot]].startswith("[IMAGE:"): res[n] = dict(status="missing", why="placeholder not found"); return
        ph = md[slots[slot]]; body = " ".join(ph[7:].rstrip().rstrip("]").split())
        spec = ri.old_spec(sub, topic, n, pre); labels = [e[0] for e in spec.get("labels", [])]
        notes = rc.notes_excerpt(sub, topic, body + " " + " ".join(labels), 1600)
        tmp = os.path.join(WORK, "restore_tmp", n + ".png"); os.makedirs(os.path.dirname(tmp), exist_ok=True); open(tmp, "wb").write(img)
        pr = ("You are a careful science teacher. Check ONLY THE DRAWING of this textbook illustration (ignore the layout, position and tidiness of labels, captions and lines, and ignore style, colour tone and small proportions). "
              f"PLACEHOLDER DESCRIPTION IT MUST MATCH:\n{body[:1800]}\n"
              + (f"NOTES TEXT STUDENTS READ (the picture must not contradict it):\n{notes}\n" if notes else "")
              + "Set correct=true if the drawing shows what the description asks and contains no factual mistake that would teach something false (wrong count of main structures, a required structure missing or drawn as something else, a structure in the wrong place or wrongly connected, a wrong colour for a real organism, a process drawn the wrong way round). "
              "Set correct=false and list the mistakes only if you can clearly see a factual mistake. Do not fail for missing minor detail.")
        try: v = m.vision(pr, [tmp], SC, "restore-check-pro", model=m.TXT_PRO, thinking="low")
        except Exception as e: res[n] = dict(status="error", why=str(e)[:100]); return
        res[n] = dict(status="restore" if v["correct"] else "keep", why="; ".join(v["mistakes"])[:300], slot=slot, old_line=old_md[oi], sub=sub, topic=topic, ph_idx=slots[slot], spec=spec)
    with ThreadPoolExecutor(6) as ex: list(ex.map(check, cands))
    for n, v in res.items():
        if v["status"] != "restore": continue
        sub, topic = v["sub"], v["topic"]
        out = os.path.join(REPO, "subjects", sub, "images", n + ".png"); open(out, "wb").write(git_show(pre, f"subjects/{sub}/images/{n}.png"))
        mdp = os.path.join(REPO, "subjects", sub, topic + ".md"); lines = open(mdp).read().split("\n")
        slots = [i for i, l in enumerate(lines) if re.match(SLOT, l)]
        lines[slots[v["slot"]]] = v["old_line"]; open(mdp, "w").write("\n".join(lines))
        sp = os.path.join(REPO, "tools", "specs", sub, topic + "-labels.json"); d = json.load(open(sp)); d[n] = v["spec"]; json.dump(d, open(sp, "w"), indent=1, ensure_ascii=False)
    json.dump({n: {k: v for k, v in x.items() if k not in ("spec",)} for n, x in res.items()}, open(os.path.join(WORK, "restore_results.json"), "w"), indent=1, ensure_ascii=False)
    import collections; print(collections.Counter(v["status"] for v in res.values()), f"spend ${m.spent('restore'):.2f}")
    for n, v in res.items(): print(v["status"], n[:50], v["why"][:110])


if __name__ == "__main__":
    main()
