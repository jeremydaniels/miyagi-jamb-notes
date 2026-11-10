#!/usr/bin/env python3
"""Rebuild raws for every labelled Biology B-E image from the OLD finished image (git commit 41deb1c) and re-render the labels.
Uses the current saved specs (captions and regions kept). python tools/rebuild_all.py [--workers 4]"""
import json, glob, os, sys, subprocess, io, contextlib
from concurrent.futures import ProcessPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import REPO, RAW
OLD = os.path.join(REPO, ".image-work", "old"); os.makedirs(OLD, exist_ok=True)


def work(item):
    name, spec = item
    import rebuild_raw as rb, label
    old = rb.old_label()
    p = os.path.join(OLD, name + ".png")
    if not os.path.exists(p):
        r = subprocess.run(["git", "show", f"41deb1c:subjects/biology/images/{name}.png"], cwd=REPO, capture_output=True)
        if r.returncode: return name, "not in old commit"
        open(p, "wb").write(r.stdout)
    with contextlib.redirect_stdout(io.StringIO()):
        raw, msg = rb.rebuild(name, spec, p, old)
        if raw is None: return name, msg
        raw.save(os.path.join(RAW, name + ".png"))
        s = {k: v for k, v in spec.items()}
        s["regions"] = [e[0] for e in spec["labels"] if any(w in e[0].lower() for w in rb.REGION_WORDS)]
        label.render(name, s, os.path.join(REPO, "subjects", "biology", "images"))
    return name, "ok"


if __name__ == "__main__":
    items = []
    for f in sorted(glob.glob(os.path.join(REPO, "tools", "specs", "biology", "[B-E]*-labels.json"))):
        for n, sp in json.load(open(f)).items():
            if sp.get("labels"): items.append((n, sp))
    w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
    res = {}
    with ProcessPoolExecutor(w) as ex:
        for n, m in ex.map(work, items): res[n] = m
    bad = {n: m for n, m in res.items() if m != "ok"}
    print(len(res), "done;", len(bad), "skipped/failed")
    for n, m in bad.items(): print(" ", n, m)
