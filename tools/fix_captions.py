#!/usr/bin/env python3
"""Move panel captions into free space (below the panel, further below, or above it) for images where a caption touched an arrow or drawing.
Each image is re-rendered, checked by Gemini vision; if it is still not clean the previous version (before the panel audit) is restored.
python tools/fix_captions.py NAME ..."""
import io, json, os, subprocess, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m, fix_panels as fp, verify_panels as vp, label as lab, redo_images as ri
from common import WORK, REPO


def main():
    names = sys.argv[1:]
    m.SUBJECT = "captions"; m.SUBJ = "captions-images2"
    audit = json.load(open(os.path.join(WORK, "audit.json"))); pre = ri.pre_commit()
    fp.EXT = True
    res = {}
    for n in names:
        a = audit[n]; sub, topic = a["subject"], a["topic"]
        spec_old = ri.old_spec(sub, topic, n, pre)
        spf = os.path.join(REPO, "tools", "specs", sub, topic + "-labels.json")
        cur = json.load(open(spf))
        new, info = fp.plan(n, spec_old, a, not spec_old.get("caption_below"))
        for k in ("regions", "caption_below", "whiten"):
            if spec_old.get(k): new[k] = spec_old[k]
        out = os.path.join(REPO, "subjects", sub, "images")
        keep_png = open(os.path.join(out, n + ".png"), "rb").read()
        with contextlib.redirect_stdout(io.StringIO()): lab.render(n, new, out)
        v = m.vision(vp.PR, [os.path.join(out, n + ".png")], vp.SCHEMA, "caption-verify", thinking="low")
        bad = v.get("caption_overlaps") or v.get("line_through_other_panel") or v.get("text_cut_off")
        if not bad:
            cur[n] = new; json.dump(cur, open(spf, "w"), indent=1, ensure_ascii=False); res[n] = "moved"
        else:
            # restore the version before the panel audit
            b = subprocess.run(["git", "show", f"{pre}:subjects/{sub}/images/{n}.png"], cwd=REPO, capture_output=True)
            if b.returncode == 0:
                open(os.path.join(out, n + ".png"), "wb").write(b.stdout)
                cur[n] = spec_old; json.dump(cur, open(spf, "w"), indent=1, ensure_ascii=False); res[n] = "reverted: " + v.get("details", "")
            else:
                open(os.path.join(out, n + ".png"), "wb").write(keep_png); res[n] = "kept: " + v.get("details", "")
        print(n, res[n][:120], flush=True)
    json.dump(res, open(os.path.join(WORK, "captions_results.json"), "w"), indent=1)
    import collections; print(collections.Counter(v.split(":")[0] for v in res.values()))


if __name__ == "__main__":
    main()
