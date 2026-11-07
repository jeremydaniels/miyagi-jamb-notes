"""Helpers for looking at images while placing labels.

  python tools/preview.py grid NAME [NAME ...]       raw image with a coordinate grid
  python tools/preview.py zoom NAME X0 Y0 X1 Y1 [S]  enlarged crop (scale S, default 3) with a fine grid
  python tools/preview.py small NAME [NAME ...]      smaller copy of the FINAL labelled image

Output goes to <work>/preview/. Grid numbers are raw-image pixel coordinates,
which is what label specs use.
"""
import os, sys
from PIL import Image, ImageDraw
from common import REPO, RAW, PREVIEW, font

RED, PINK, FAINT = (200, 0, 0), (255, 120, 120), (255, 210, 210)


def grid(name):
    im = Image.open(os.path.join(RAW, name + ".png")).convert("RGB")
    d, f = ImageDraw.Draw(im), font("medium", 13)
    for v in range(50, max(im.size), 50):
        c = PINK if v % 100 == 0 else FAINT
        d.line([(v, 0), (v, im.height)], fill=c)
        d.line([(0, v), (im.width, v)], fill=c)
        if v % 100 == 0:
            d.text((v + 2, 2), str(v), fill=RED, font=f)
            d.text((2, v + 2), str(v), fill=RED, font=f)
    return im, f"grid-{name}.png"


def zoom(name, x0, y0, x1, y1, s=3.0):
    x0, y0, x1, y1 = map(int, (x0, y0, x1, y1)); s = float(s)
    im = Image.open(os.path.join(RAW, name + ".png")).convert("RGB").crop((x0, y0, x1, y1))
    im = im.resize((int((x1 - x0) * s), int((y1 - y0) * s)))
    d, f = ImageDraw.Draw(im), font("medium", 14)
    step = 10 if (x1 - x0) <= 200 else 20
    for x in range(x0 - x0 % step + step, x1, step):
        X = (x - x0) * s
        d.line([(X, 0), (X, im.height)], fill=FAINT if x % 50 else RED)
        if x % 50 == 0: d.text((X + 2, 2), str(x), fill=RED, font=f)
    for y in range(y0 - y0 % step + step, y1, step):
        Y = (y - y0) * s
        d.line([(0, Y), (im.width, Y)], fill=FAINT if y % 50 else RED)
        if y % 50 == 0: d.text((2, Y + 2), str(y), fill=RED, font=f)
    return im, f"zoom-{name}.png"


def small(name, out_dir=os.path.join(REPO, "subjects", "biology", "images")):
    im = Image.open(os.path.join(out_dir, name + ".png"))
    return im.resize((int(im.width * 0.6), int(im.height * 0.6)), Image.LANCZOS), f"small-{name}.png"


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    jobs = [zoom(*args)] if cmd == "zoom" else [{"grid": grid, "small": small}[cmd](n) for n in args]
    for im, fname in jobs:
        im.save(os.path.join(PREVIEW, fname))
        print(os.path.join(PREVIEW, fname))
