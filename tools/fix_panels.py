#!/usr/bin/env python3
"""Fix labels on multi-panel pictures from the saved label coordinates (pictures are never regenerated).

  python tools/fix_panels.py [--dry] [--only NAME ...]      uses .image-work/audit.json (tools/audit_panels.py)

Rules: names of panels or organisms become captions under their own panel; every pointer label goes to the side (left, right,
above) whose straight line to its dot does not pass through another panel; if no side works the image is listed as 'unavoidable'.
Writes the new spec back to tools/specs/<subject>/<topic>-labels.json and re-renders the image.
"""
import argparse, glob, json, os, re, sys, textwrap
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import label as lab
from common import RAW, WORK, REPO

K = 1.024
FORCE = False


def seg_hits_box(p, q, box, shrink=0.08):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    x0, x1, y0, y1 = x0 + w * shrink, x1 - w * shrink, y0 + h * shrink, y1 - h * shrink
    # Liang-Barsky clip of segment p-q against the box
    dx, dy = q[0] - p[0], q[1] - p[1]; t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0: return False
        else:
            r = qq / pp
            if pp < 0:
                if r > t1: return False
                t0 = max(t0, r)
            else:
                if r < t0: return False
                t1 = min(t1, r)
    return t0 < t1


def panel_of(pt, boxes):
    for i, b in enumerate(boxes):
        if b[0] <= pt[0] <= b[2] and b[1] <= pt[1] <= b[3]: return i
    cs = [((b[0] + b[2]) / 2, (b[1] + b[3]) / 2) for b in boxes]
    return min(range(len(boxes)), key=lambda i: (cs[i][0] - pt[0]) ** 2 + (cs[i][1] - pt[1]) ** 2)


def ink_rows(arr, b, pad=0):
    x0, y0, x1, y1 = [int(v) for v in b]
    sub = arr[max(0, y0):min(arr.shape[0], y1 + pad), max(0, x0):min(arr.shape[1], x1)]
    return sub, max(0, y0)


def ink_bottom(arr, b):
    """Last row of the panel that holds real drawing (at least 12% of the panel width inked)."""
    sub, y0 = ink_rows(arr, b, 12)
    if not sub.size: return int(b[3])
    frac = (sub < 225).any(axis=2).mean(axis=1)
    rows = np.flatnonzero(frac > 0.12)
    return y0 + int(rows.max()) if len(rows) else int(b[3])


def strip_free(arr, x0, x1, y0, y1):
    x0, x1, y0, y1 = max(0, int(x0)), min(arr.shape[1], int(x1)), max(0, int(y0)), min(arr.shape[0], int(y1))
    if y1 > arr.shape[0] - 1: return True
    sub = arr[y0:y1, x0:x1]
    return not (sub < 225).any(axis=2).sum() > 6


def row_free(arr, y0, y1):
    return strip_free(arr, 0, arr.shape[1], y0, y1)


def plan(name, spec, au, allow_below):
    im = Image.open(os.path.join(RAW, name + ".png")).convert("RGB"); arr = np.asarray(im)
    Wr, Hr = im.size
    boxes = [[p["x0"] * K, p["y0"] * K, p["x1"] * K, p["y1"] * K] for p in au["panels"]]
    names = set(au["name_labels"])
    ink = lab.crop_box(im); cx_mid = (ink[0] + ink[2]) / 2
    new = dict(spec); new["labels"] = []; caps = list(spec.get("captions", [])); notes = []
    capmap = {}
    old_cross = 0; unavoid = []
    for e in spec["labels"]:
        e = list(e); pt = e[1]; pi = panel_of(pt, boxes)
        others = [b for i, b in enumerate(boxes) if i != pi]
        # the old rule: left if the dot is left of the picture centre
        oldp = (0, pt[1]) if pt[0] < cx_mid else (Wr, pt[1])
        if any(seg_hits_box(oldp, pt, b) for b in others): old_cross += 1
        if e[0] in names:
            capmap.setdefault(pi, []).append(e[0].replace("\n", " ")); continue
        cands = [("L", (0, pt[1])), ("R", (Wr, pt[1])), ("T", (pt[0], 0))]
        cands.sort(key=lambda c: abs(c[1][0] - pt[0]) + abs(c[1][1] - pt[1]) if c[0] in "LR" else 1.25 * (abs(c[1][0] - pt[0]) + abs(c[1][1] - pt[1])))
        pick = None
        for sd, ep in cands:
            if not any(seg_hits_box(ep, pt, b) for b in others):
                pick = sd; break
        if pick is None:
            pick = cands[0][0]; unavoid.append(e[0].replace("\n", " "))
        e = e[:2] + [pick]
        new["labels"].append(e)
    splits = []; cap_flags = []
    for pi, texts in capmap.items():
        b = boxes[pi]; bottom = ink_bottom(arr, b)
        pw = max(160, b[2] - b[0])
        text = "; ".join(texts)
        wrapw = max(14, int(pw / 20))
        text = "\n".join(textwrap.fill(t, wrapw, break_long_words=False) for t in text.split("\n"))
        lines = text.count("\n") + 1
        cap_h = 52 * lines; cap_w = min(pw, max(len(t) for t in text.split("\n")) * 21)
        cx = (b[0] + b[2]) / 2
        placed = None
        for off in range(10, 170, 10):                     # lowest spot below the panel's drawing where the caption touches nothing
            if strip_free(arr, cx - cap_w / 2, cx + cap_w / 2, bottom + off, bottom + off + cap_h):
                placed = bottom + off; break
        below_others = [o for i, o in enumerate(boxes) if i != pi and o[1] > bottom - 20 and not (o[2] < b[0] or o[0] > b[2])]
        if placed is None and FORCE:
            if below_others:
                splits.append(int(bottom + 6)); placed = bottom + 14                 # open a white row for the caption (may cut a thin line)
            else:
                for off in range(170, 420, 10):
                    if strip_free(arr, cx - cap_w / 2, cx + cap_w / 2, bottom + off, bottom + off + cap_h):
                        placed = bottom + off; break
        if placed is None:
            placed = bottom + 14; cap_flags.append(texts[0])
        caps.append([text, int(cx), int(placed)])
        need_end = placed + cap_h
        if below_others and min(o[1] for o in below_others) < need_end + 20 and row_free(arr, placed - 6, placed):
            splits.append(int(placed - 4))
    if capmap: notes.append(f"{sum(len(v) for v in capmap.values())} panel name(s) to captions")
    if splits:
        merged = []
        for y in sorted(splits):
            if not merged or y - merged[-1] > 50: merged.append(y)
        new["split"] = [[y, 120] for y in merged]
    new["captions"] = caps; new["fixed_sides"] = True
    new["capsize"] = 0
    return new, dict(old_cross=old_cross, named=sum(len(v) for v in capmap.values()), unavoidable=unavoid, cap_overlap=cap_flags, notes=notes)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry", action="store_true"); ap.add_argument("--only", nargs="*"); ap.add_argument("--force", action="store_true"); a = ap.parse_args()
    global FORCE
    FORCE = a.force
    audit = json.load(open(os.path.join(WORK, "audit.json")))
    report = {}
    for f in sorted(glob.glob(os.path.join(REPO, "tools", "specs", "*", "*-labels.json"))):
        sub = f.split("/")[-2]
        data = json.load(open(f)); ch = False
        for n, sp in data.items():
            au = audit.get(n)
            if not au or len(au["panels"]) < 2 or not sp.get("labels") or (a.only and n not in a.only): continue
            allow_below = not sp.get("caption_below")
            new, info = plan(n, sp, au, allow_below)
            need = info["named"] > 0 or info["old_cross"] > 0
            report[n] = dict(info, subject=sub, topic=os.path.basename(f)[:-12], panels=len(au["panels"]), need=need)
            if need and not a.dry:
                if "regions" in sp: new["regions"] = sp["regions"]
                data[n] = new; ch = True
                import io, contextlib
                with contextlib.redirect_stdout(io.StringIO()): lab.render(n, new, os.path.join(REPO, "subjects", sub, "images"))
        if ch: json.dump(data, open(f, "w"), indent=1, ensure_ascii=False)
    json.dump(report, open(os.path.join(WORK, "panel_report.json"), "w"), indent=1)
    need = [n for n, r in report.items() if r["need"]]
    print(len(report), "multi-panel labelled;", len(need), "need changes;", sum(1 for n in need if report[n]["named"]), "with names to captions;", sum(1 for n in need if report[n]["old_cross"]), "with crossing lines;", sum(1 for n in need if report[n]["unavoidable"]), "unavoidable")


if __name__ == "__main__":
    main()
