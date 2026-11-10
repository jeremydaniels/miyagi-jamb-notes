#!/usr/bin/env python3
"""Redraw saved code-drawn images with the current style.py (minimum font 14 pt, text de-cluttering).

  python tools/redraw_code.py biology [--only NAME ...]

For each tools/specs/<subject>/code/<name>.py the drawing is run again; the new picture is checked by Gemini vision against
its saved description (readable, no overlaps, nothing cut off, content unchanged). It replaces the old image only if it passes;
otherwise the old image stays and the name is listed.
"""
import argparse, glob, json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
from PIL import Image


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("subject"); ap.add_argument("--only", nargs="*"); a = ap.parse_args()
    m.SUBJECT = a.subject; m.SUBJ = a.subject + "-images2"
    desc = {}
    for f in glob.glob(os.path.join(m.REPO, "tools", "specs", a.subject, "*-prompts.json")):
        for n, p in json.load(open(f)): desc[n] = p
    names = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(m.REPO, "tools", "specs", a.subject, "code", "*.py")))
    names = [n for n in names if not a.only or n in a.only]
    res = {}
    def one(n):
        code = open(os.path.join(m.REPO, "tools", "specs", a.subject, "code", n + ".py")).read()
        job = dict(name=n, full=desc.get(n, n), subject=a.subject)
        try:
            out = m.run_code(job, code)
            chk = m.check_code_img(job, out)
        except Exception as e:
            res[n] = ("error", str(e)[-200:]); return
        if chk["ok"]:
            Image.open(out).convert("RGB").save(os.path.join(m.REPO, "subjects", a.subject, "images", n + ".png"), optimize=True)
            res[n] = ("redrawn", "")
        else:
            res[n] = ("kept old", "; ".join(chk["problems"][:3]))
        print(n, res[n][0], res[n][1][:150], flush=True)
    with ThreadPoolExecutor(6) as p: list(p.map(one, names))
    json.dump(res, open(os.path.join(m.WORK, f"redraw-{a.subject}.json"), "w"), indent=1)
    import collections; print(collections.Counter(v[0] for v in res.values()))


if __name__ == "__main__":
    main()
