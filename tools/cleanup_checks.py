#!/usr/bin/env python3
"""Vision checks used in the image cleanup pass (Gemini Flash).

  python tools/cleanup_checks.py scars   [--only NAME ...]   leftover leader-line marks in the recovered Biology pictures
  python tools/cleanup_checks.py changed NAME [NAME ...]     re-check finished images: raw markup, overlapping text, wrong labels

Results: .image-work/scars.json / .image-work/changed.json
"""
import argparse, glob, io, json, os, sys, base64
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
from PIL import Image, ImageChops
from common import RAW, WORK, REPO

SC = {"type": "OBJECT", "properties": {"marks": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
      "kind": {"type": "STRING", "enum": ["leftover_line", "leftover_dot_or_ring", "white_scar", "smudge"]},
      "x0": {"type": "INTEGER"}, "y0": {"type": "INTEGER"}, "x1": {"type": "INTEGER"}, "y1": {"type": "INTEGER"}, "why": {"type": "STRING"}},
      "required": ["kind", "x0", "y0", "x1", "y1", "why"]}}}, "required": ["marks"]}
CH = {"type": "OBJECT", "properties": {"ok": {"type": "BOOLEAN"}, "problems": {"type": "ARRAY", "items": {"type": "STRING"}}}, "required": ["ok", "problems"]}


def tiles(path):
    im = Image.open(path).convert("RGB")
    bb = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).convert("L").point(lambda p: 255 if p > 18 else 0).getbbox()
    im = im.crop(bb)
    w, h = im.size; out = []
    nx, ny = (2 if w > 520 else 1), (2 if h > 520 else 1)
    tw, th = w / nx, h / ny
    for j in range(ny):
        for i in range(nx):
            box = (int(max(0, i * tw - 30)), int(max(0, j * th - 30)), int(min(w, (i + 1) * tw + 30)), int(min(h, (j + 1) * th + 30)))
            t = im.crop(box); s = 1000 / max(t.size); t = t.resize((int(t.width * s), int(t.height * s)), Image.LANCZOS)
            out.append((bb[0] + box[0], bb[1] + box[1], box[2] - box[0], box[3] - box[1], s, t))
    return out


def scars(name):
    marks = []
    for ox, oy, tw, th, s, t in tiles(os.path.join(RAW, name + ".png")):
        pr = ("This is a crop of a textbook illustration. Thin dark pointer lines (about 3 px wide, ending in a round dot) were digitally removed and the gap was repainted from neighbouring pixels. "
              "Find any REMAINING artefacts of that: (a) a leftover thin straight dark or white line segment that is not part of the drawing, (b) a leftover round dot or ring, (c) a thin white straight scar cutting across coloured areas, (d) a smudge or blur streak. "
              "Ignore the normal drawing: outlines, vessels, hairs, veins, fibres, bones and shading are NOT artefacts. Report only artefacts you are sure of (they are straight and thin, or round and tiny, unlike the surrounding artwork). Coordinates are on a 0-1000 scale of this crop. If there are none, return an empty list.")
        r = m.vision(pr, [t], SC, "scar-check", thinking="low")
        for k in r["marks"]:
            marks.append(dict(kind=k["kind"], why=k["why"], box=[ox + k["x0"] / s, oy + k["y0"] / s, ox + k["x1"] / s, oy + k["y1"] / s]))
    return marks


def changed(name, path, desc):
    pr = ("Check this finished textbook image. Report problems only if clear: (1) raw markup in text such as underscores, carets, LaTeX, dollar signs, stray quotation marks or stray numbers; chemical formulas and units that lack proper subscripts or superscripts (CO2 instead of CO₂, m2 instead of m²); "
          "(2) text that overlaps other text or lines, is cut off, or is unreadably small; (3) a pointer line whose dot is clearly on the wrong part; (4) leftover line marks or smudges in the picture; (5) text that is dark on a dark fill. "
          + (f"The image should show: {desc[:700]}" if desc else ""))
    r = m.vision(pr, [path], CH, "changed-check", thinking="low")
    return r


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("mode"); ap.add_argument("names", nargs="*"); ap.add_argument("--only", nargs="*"); ap.add_argument("--subject", default="biology"); ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    m.SUBJECT = a.subject; m.SUBJ = a.subject + "-images2"
    if a.mode == "scars":
        names = sorted(os.path.basename(f)[:-4] for f in glob.glob(os.path.join(RAW, "*.png")))
        done = set()
        spec_names = set()
        for f in glob.glob(os.path.join(REPO, "tools", "specs", "biology", "[B-E]*-labels.json")):
            spec_names |= {k for k, v in json.load(open(f)).items() if v.get("labels")}
        names = [n for n in names if n in spec_names and (not a.only or n in a.only)]
        res = {}
        def one(n):
            try: res[n] = scars(n)
            except Exception as e: res[n] = [dict(kind="error", why=str(e)[:100], box=[])]
        with ThreadPoolExecutor(a.workers) as p: list(p.map(one, names))
        json.dump(res, open(os.path.join(WORK, "scars.json"), "w"), indent=1)
        print(len(res), "images,", sum(1 for v in res.values() if v), "with marks,", sum(len(v) for v in res.values()), "marks")
    else:
        prompts = {}
        for f in glob.glob(os.path.join(REPO, "tools", "specs", "*", "*-prompts.json")):
            for n, p in json.load(open(f)): prompts[n] = p
        res = {}
        def one(n):
            sub = [d for d in os.listdir(os.path.join(REPO, "subjects")) if os.path.exists(os.path.join(REPO, "subjects", d, "images", n + ".png"))][0]
            res[n] = changed(n, os.path.join(REPO, "subjects", sub, "images", n + ".png"), prompts.get(n, ""))
        with ThreadPoolExecutor(a.workers) as p: list(p.map(one, a.names))
        json.dump(res, open(os.path.join(WORK, "changed.json"), "w"), indent=1)
        for n, r in res.items(): print(n, "OK" if r["ok"] else "PROBLEMS: " + "; ".join(r["problems"])[:250])


if __name__ == "__main__":
    main()
