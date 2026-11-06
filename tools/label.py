"""Add text labels and thin leader lines to raw images with Pillow.

Usage:
  python tools/label.py SPEC.json [name ...] [--out biology/images]

Reads <work>/raw/<name>.png, writes <out>/<name>.png. The image is trimmed to
its content, and label columns are added on the left and right.

All coordinates are in the RAW 1024x1024 image's pixels. Use
`python tools/preview.py grid NAME` to read them off a gridded copy.

SPEC.json maps each image name to an object with any of these keys:
  "labels":   [[text, [x, y], side, label_y?, [r, g, b]?], ...]
      side "L" or "R": the label goes in the left or right column, at height
        label_y (default y), with a leader line to the dot at (x, y).
        Overlapping labels are pushed apart automatically.
      side "F": free label; the 4th item is the [cx, cy] centre of the text.
  "captions": [[text, x, y], ...]   centred text with no line. y = 0 puts it in
      a title row above the image.
  "capsize":  font size for captions (default 26).
  "arrows":   [[[x1, y1], [x2, y2]], ...]   solid arrows, e.g. for life cycles.
  "whiten":   [[x1, y1, x2, y2], ...]   paint rectangles white (remove frames).
  "rings":    [[cx, cy, r, width], ...]  paint white circles (remove a drawn ring).
  "split":    [y, gap]   insert `gap` white pixels at raw row y (more room
      between two rows of pictures); coordinates below y shift automatically.
  "src":      use a different raw file name.
"""
import argparse, json, math, os
from PIL import Image, ImageDraw, ImageChops
from common import REPO, RAW, font

FONT = font("medium", 26)
TITLE = font("semibold", 32)
INK, WHITE = (40, 44, 52), (255, 255, 255)
GAP, MARGIN = 10, 24


def crop_box(im):
    diff = ImageChops.difference(im, Image.new("RGB", im.size, WHITE)).convert("L")
    l, t, r, b = diff.point(lambda p: 255 if p > 18 else 0).getbbox() or (0, 0, *im.size)
    return max(0, l - 20), max(0, t - 20), min(im.width, r + 20), min(im.height, b + 20)


def layout(items, lo, hi):
    """Push side labels apart so none overlap, keeping them inside [lo, hi]."""
    items.sort(key=lambda d: d["y"])
    for i, d in enumerate(items):
        top = d["y"] - d["h"] / 2
        if i:
            top = max(top, items[i - 1]["top"] + items[i - 1]["h"] + GAP)
        d["top"] = max(top, lo)
    over = (items[-1]["top"] + items[-1]["h"]) - hi if items else 0
    if over > 0:
        items[-1]["top"] -= over
        for i in range(len(items) - 2, -1, -1):
            if items[i]["top"] + items[i]["h"] + GAP > items[i + 1]["top"]:
                items[i]["top"] = items[i + 1]["top"] - GAP - items[i]["h"]


def leader(dr, start, end):
    """Thin dark line with a white halo, ending in a dot on the labelled part."""
    dr.line([start, end], fill=WHITE, width=5)
    dr.line([start, end], fill=INK, width=2)
    x, y = end
    dr.ellipse([x - 6, y - 6, x + 6, y + 6], fill=WHITE)
    dr.ellipse([x - 4, y - 4, x + 4, y + 4], fill=INK)


def apply_split(raw, spec):
    sy, gap = spec["split"]
    big = Image.new("RGB", (raw.width, raw.height + gap), WHITE)
    big.paste(raw.crop((0, 0, raw.width, sy)), (0, 0))
    big.paste(raw.crop((0, sy, raw.width, raw.height)), (0, sy + gap))
    sh = lambda y: y + gap if y > sy else y
    spec = dict(spec)
    spec["captions"] = [[t, x, sh(y)] for t, x, y in spec.get("captions", [])]
    labels = []
    for e in spec.get("labels", []):
        e = list(e)
        e[1] = [e[1][0], sh(e[1][1])]
        if len(e) > 3:
            e[3] = [e[3][0], sh(e[3][1])] if e[2] == "F" else sh(e[3])
        labels.append(e)
    spec["labels"] = labels
    spec["arrows"] = [[[a[0], sh(a[1])], [b[0], sh(b[1])]] for a, b in spec.get("arrows", [])]
    return big, spec


def render(name, spec, out_dir):
    raw = Image.open(os.path.join(RAW, spec.get("src", name) + ".png")).convert("RGB")
    if "split" in spec:
        raw, spec = apply_split(raw, spec)
    dw = ImageDraw.Draw(raw)
    for r in spec.get("whiten", []):
        dw.rectangle(r, fill=WHITE)
    for cx, cy, rr, w in spec.get("rings", []):
        dw.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=WHITE, width=w)

    cl, ct, cr, cb = crop_box(raw)
    free = [e for e in spec.get("labels", []) if e[2] == "F"]
    for e in free:  # keep room for free labels placed in white space
        ct = max(0, min(ct, e[3][1] - 45))
        cb = min(raw.height, max(cb, e[3][1] + 45))
    img = raw.crop((cl, ct, cr, cb)).point(lambda v: 255 if v > 243 else v)  # clean near-white background
    d0 = ImageDraw.Draw(img)

    labs = []
    for e in spec.get("labels", []):
        if e[2] == "F":
            continue
        text, (x, y), side = e[0], e[1], e[2]
        bb = d0.multiline_textbbox((0, 0), text, font=FONT, spacing=4)
        labs.append(dict(text=text, tx=x - cl, ty=y - ct, side=side,
                         y=(e[3] if len(e) > 3 else y) - ct,
                         col=tuple(e[4]) if len(e) > 4 else INK,
                         w=bb[2] - bb[0], h=bb[3] - bb[1] + 6))
    wl = max([l["w"] for l in labs if l["side"] == "L"], default=0)
    wr = max([l["w"] for l in labs if l["side"] == "R"], default=0)
    padL = wl + 60 if wl else MARGIN
    padR = wr + 60 if wr else MARGIN
    captions = spec.get("captions", [])
    cap_font = font("semibold", spec.get("capsize", 26))
    title_h = 60 if any(c[2] == 0 for c in captions) else 0
    W, H = img.width + padL + padR, img.height + title_h + 2 * MARGIN
    for text, x, y in captions:  # grow the canvas if a caption sits below the image
        if y:
            bb = d0.multiline_textbbox((0, 0), text, font=cap_font, spacing=4)
            H = max(H, int(y - ct + MARGIN + title_h + bb[3] + MARGIN))

    can = Image.new("RGB", (W, H), WHITE)
    ox, oy = padL, MARGIN + title_h
    can.paste(img, (ox, oy))
    dr = ImageDraw.Draw(can)
    to_canvas = lambda x, y: (x - cl + ox, y - ct + oy)

    for side in "LR":
        group = [l for l in labs if l["side"] == side]
        for l in group:
            l["y"] += oy
        layout(group, MARGIN, H - MARGIN)
        for l in group:
            cy = l["top"] + l["h"] / 2
            if side == "L":
                dr.multiline_text((padL - 40 - l["w"], l["top"]), l["text"], font=FONT, fill=l["col"], spacing=4, align="right")
                sx = padL - 32
            else:
                lx = ox + img.width + 40
                dr.multiline_text((lx, l["top"]), l["text"], font=FONT, fill=l["col"], spacing=4)
                sx = lx - 8
            leader(dr, (sx, cy), (l["tx"] + ox, l["ty"] + oy))

    for p, q in spec.get("arrows", []):
        a, b = to_canvas(*p), to_canvas(*q)
        dr.line([a, b], fill=INK, width=4)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        head = [(b[0] - 22 * math.cos(ang + s), b[1] - 22 * math.sin(ang + s)) for s in (-0.45, 0.45)]
        dr.polygon([b, *head], fill=INK)

    for e in free:
        text, (x, y), (fx, fy) = e[0], e[1], e[3]
        bb = dr.multiline_textbbox((0, 0), text, font=FONT, spacing=4)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        cx, cy = to_canvas(fx, fy)
        dr.multiline_text((cx - w / 2, cy - h / 2), text, font=FONT, fill=INK, spacing=4, align="center")
        tx, ty = to_canvas(x, y)
        leader(dr, (cx, cy + h / 2 + 8 if ty > cy else cy - h / 2 - 8), (tx, ty))

    for text, x, y in captions:
        f = TITLE if y == 0 else cap_font
        bb = dr.multiline_textbbox((0, 0), text, font=f, spacing=4)
        cx = x - cl + ox
        top = MARGIN + 6 if y == 0 else y - ct + oy
        left = min(max(cx - (bb[2] - bb[0]) / 2, 8), W - 8 - (bb[2] - bb[0]))
        dr.multiline_text((left, top), text, font=f, fill=INK, spacing=4, align="center")

    os.makedirs(out_dir, exist_ok=True)
    can.save(os.path.join(out_dir, name + ".png"), optimize=True)
    print("saved", os.path.relpath(os.path.join(out_dir, name + ".png"), REPO), can.size)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("names", nargs="*")
    ap.add_argument("--out", default=os.path.join(REPO, "biology", "images"))
    a = ap.parse_args()
    with open(a.spec) as f:
        spec = json.load(f)
    for n in a.names or spec:
        render(n, spec[n], a.out)


if __name__ == "__main__":
    main()
