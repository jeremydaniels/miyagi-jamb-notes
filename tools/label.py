"""Add text labels and thin leader lines to raw images with Pillow.

Usage:
  python tools/label.py SPEC.json [name ...] [--out subjects/biology/images]

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
  "capsize":  minimum font size for captions (default: the label font).
  "caption_below": "text"  a wrapped caption under the picture (use for process notes such as "oxygen in",
      "inspiration", test results: things that are not a part of the picture).
  "regions":  [label text, ...]  labels of regions (cortex, medulla): the dot goes inside the region and is drawn bigger.
  "arrows":   [[[x1, y1], [x2, y2]], ...]   solid arrows, e.g. for life cycles.
  "whiten":   [[x1, y1, x2, y2], ...]   paint rectangles white (remove frames).
  "rings":    [[cx, cy, r, width], ...]  paint white circles (remove a drawn ring).
  "split":    [y, gap]   insert `gap` white pixels at raw row y (more room
      between two rows of pictures); coordinates below y shift automatically.
  "src":      use a different raw file name.
"""
import argparse, json, math, os, re, textwrap
from PIL import Image, ImageDraw, ImageChops
from common import REPO, RAW, font

INK, WHITE = (40, 44, 52), (255, 255, 255)
GAP, MARGIN = 12, 24
MIN_FRAC = 0.022      # text height as a share of the final image width: keeps labels readable on a phone
MIN_FONT, MAX_FONT = 28, 60
WRAP = 18             # characters per line in label columns


def crop_box(im):
    diff = ImageChops.difference(im, Image.new("RGB", im.size, WHITE)).convert("L")
    l, t, r, b = diff.point(lambda p: 255 if p > 18 else 0).getbbox() or (0, 0, *im.size)
    return max(0, l - 20), max(0, t - 20), min(im.width, r + 20), min(im.height, b + 20)


SUB = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")


def clean(text):
    """Strip stray quotes left by the placeholder parser and turn CO_2 style subscripts into real subscripts."""
    text = text.strip().strip("\"'").strip()
    return re.sub(r"_\{?([0-9+-]+)\}?", lambda m: m.group(1).translate(SUB), text)


def wrap(text, width=WRAP):
    text = clean(text)
    return "\n".join(textwrap.fill(p, width) for p in text.split("\n"))


def layout(items, lo, hi):
    """Slots for side labels: stacked in order of anchor y, pushed apart so none overlap, inside [lo, hi]."""
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


def _ccw(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])


def segs_cross(p1, p2, p3, p4):
    d1, d2 = _ccw(p1, p2, p3), _ccw(p1, p2, p4)
    d3, d4 = _ccw(p3, p4, p1), _ccw(p3, p4, p2)
    return d1 * d2 < 0 and d3 * d4 < 0


def uncross(group, sx, lo, hi):
    """Swap which label sits in which slot until no two leader lines cross (each swap shortens the total
    line length, so this ends). Slots keep their positions; the labels move between them."""
    slots = [(d["top"], d["top"] + d["h"] / 2) for d in group]     # (top, centre y) per slot, in slot order
    order = list(range(len(group)))                               # order[slot] = label index
    def line(slot):
        return ((sx, slots[slot][1]), group[order[slot]]["dot"])
    for _ in range(200):
        changed = False
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                if segs_cross(*line(i), *line(j)):
                    order[i], order[j] = order[j], order[i]; changed = True
        if not changed:
            break
    res = []
    for slot, li in enumerate(order):                 # labels differ in height: restack them in slot order
        d = group[li]; d["y"] = slots[slot][1]; res.append(d)
    layout(res, lo, hi)
    return res


def count_cross(group, sx):
    n = 0
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if segs_cross((sx, group[i]["top"] + group[i]["h"] / 2), group[i]["dot"], (sx, group[j]["top"] + group[j]["h"] / 2), group[j]["dot"]):
                n += 1
    return n


def leader(dr, start, end, region=False):
    """Thin dark line with a white halo, ending in a dot on the labelled part (bigger dot for a region)."""
    dr.line([start, end], fill=WHITE, width=6)
    dr.line([start, end], fill=INK, width=3)
    x, y = end
    r = 9 if region else 7
    dr.ellipse([x - r - 2, y - r - 2, x + r + 2, y + r + 2], fill=WHITE)
    dr.ellipse([x - r, y - r, x + r, y + r], fill=INK)
    if region:
        dr.ellipse([x - 3, y - 3, x + 3, y + 3], fill=WHITE)


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


def split_sides(labs, cx, ox_pad):
    """Choose a side for every label (left of the picture's centre line goes left) and remove line crossings."""
    return [l for l in labs if l["tx"] < cx], [l for l in labs if l["tx"] >= cx]


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
    # small pictures are enlarged so the labels do not dwarf them
    scale = 1.0
    if img.width < 700:
        scale = 700 / img.width
        img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    S = lambda v: v * scale
    regions = {t.lower() for t in spec.get("regions", [])}
    side_labels = [e for e in spec.get("labels", []) if e[2] != "F"]
    captions = spec.get("captions", [])
    below = spec.get("caption_below", "")

    fsize = MIN_FONT
    for _ in range(4):                     # grow the font until it is at least MIN_FRAC of the final width
        FONT, TITLE = font("medium", fsize), font("semibold", int(fsize * 1.2))
        d0 = ImageDraw.Draw(img)
        labs = []
        for e in side_labels:
            text, (x, y) = wrap(e[0]), e[1]
            bb = d0.multiline_textbbox((0, 0), text, font=FONT, spacing=6)
            labs.append(dict(text=text, tx=S(x - cl), ty=S(y - ct), side=e[2], y0=S((e[3] if len(e) > 3 and not isinstance(e[3], list) else y) - ct), y=0,
                             col=tuple(e[4]) if len(e) > 4 else INK, region=e[0].lower() in regions,
                             w=bb[2] - bb[0], h=bb[3] - bb[1] + 8, dot=None))
        sides = {"L": [], "R": []}
        centre = img.width / 2
        for l in labs:                     # a label goes to the side its dot is on
            sides["L" if l["tx"] < centre else "R"].append(l)
        wl = max([l["w"] for l in sides["L"]], default=0)
        wr = max([l["w"] for l in sides["R"]], default=0)
        padL = wl + 70 if wl else MARGIN
        padR = wr + 70 if wr else MARGIN
        W = img.width + padL + padR
        if fsize >= MIN_FRAC * W or fsize >= MAX_FONT:
            break
        fsize = min(MAX_FONT, int(MIN_FRAC * W) + 1)
    cap_font = font("semibold", max(fsize, spec.get("capsize", 0)))
    title_h = int(fsize * 1.2) + 40 if any(c[2] == 0 for c in captions) else 0
    H = img.height + title_h + 2 * MARGIN
    can_probe = ImageDraw.Draw(img)
    below_txt = ""
    if below:
        wrapw = max(20, int(img.width / (fsize * 0.52)))
        below_txt = textwrap.fill(below, wrapw)
        bb = can_probe.multiline_textbbox((0, 0), below_txt, font=cap_font, spacing=8)
        H += bb[3] + 30
    for text, x, y in captions:  # grow the canvas if a caption sits below the image
        if y:
            bb = can_probe.multiline_textbbox((0, 0), text, font=cap_font, spacing=6)
            H = max(H, int(S(y - ct) + MARGIN + title_h + bb[3] + MARGIN))

    can = Image.new("RGB", (W, H), WHITE)
    ox, oy = padL, MARGIN + title_h
    can.paste(img, (ox, oy))
    dr = ImageDraw.Draw(can)
    to_canvas = lambda x, y: (S(x - cl) + ox, S(y - ct) + oy)
    lo, hi = MARGIN, MARGIN + title_h + img.height + MARGIN

    def place(group, sx):
        for l in group:
            l["y"] = l["y0"] + oy; l["dot"] = (l["tx"] + ox, l["ty"] + oy)
        if not group:
            return []
        layout(group, lo, hi)
        return uncross(group, sx, lo, hi)

    sxL, sxR = padL - 40, ox + img.width + 40
    left, right = place(sides["L"], sxL), place(sides["R"], sxR)
    # if a side still has crossings, try moving the labels nearest the centre line to the other side
    for _ in range(3):
        bad = count_cross(left, sxL) + count_cross(right, sxR)
        if not bad:
            break
        pool = sorted(left + right, key=lambda l: l["tx"])
        best = None
        for k in range(max(1, len(pool) // 3), max(2, len(pool) * 2 // 3 + 1)):
            L_, R_ = pool[:k], pool[k:]
            for l in L_: l["top"] = 0
            gl, gr = place(list(L_), sxL), place(list(R_), sxR)
            sc = count_cross(gl, sxL) + count_cross(gr, sxR)
            if best is None or sc < best[0]:
                best = (sc, gl, gr)
        left, right = best[1], best[2]
        break
    for side, group in (("L", left), ("R", right)):
        for l in group:
            cy = l["top"] + l["h"] / 2
            if side == "L":
                dr.multiline_text((padL - 44 - l["w"], l["top"]), l["text"], font=FONT, fill=l["col"], spacing=6, align="right")
                sx = padL - 36
            else:
                lx = ox + img.width + 44
                dr.multiline_text((lx, l["top"]), l["text"], font=FONT, fill=l["col"], spacing=6)
                sx = lx - 8
            leader(dr, (sx, cy), l["dot"], l["region"])

    for p, q in spec.get("arrows", []):
        a, b = to_canvas(*p), to_canvas(*q)
        dr.line([a, b], fill=INK, width=5)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        head = [(b[0] - 26 * math.cos(ang + s), b[1] - 26 * math.sin(ang + s)) for s in (-0.45, 0.45)]
        dr.polygon([b, *head], fill=INK)

    for e in free:
        text, (x, y), (fx, fy) = wrap(e[0], 24), e[1], e[3]
        bb = dr.multiline_textbbox((0, 0), text, font=FONT, spacing=6)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        cx, cy = to_canvas(fx, fy)
        dr.multiline_text((cx - w / 2, cy - h / 2), text, font=FONT, fill=INK, spacing=6, align="center")
        tx, ty = to_canvas(x, y)
        leader(dr, (cx, cy + h / 2 + 8 if ty > cy else cy - h / 2 - 8), (tx, ty))

    for text, x, y in captions:
        f = TITLE if y == 0 else cap_font
        bb = dr.multiline_textbbox((0, 0), text, font=f, spacing=6)
        cx = S(x - cl) + ox
        top = MARGIN + 6 if y == 0 else S(y - ct) + oy
        left_ = min(max(cx - (bb[2] - bb[0]) / 2, 8), W - 8 - (bb[2] - bb[0]))
        dr.multiline_text((left_, top), text, font=f, fill=INK, spacing=6, align="center")
    if below_txt:
        bb = dr.multiline_textbbox((0, 0), below_txt, font=cap_font, spacing=8)
        dr.multiline_text((ox + (img.width - (bb[2] - bb[0])) / 2, oy + img.height + 18), below_txt, font=cap_font, fill=INK, spacing=8, align="center")

    os.makedirs(out_dir, exist_ok=True)
    can.save(os.path.join(out_dir, name + ".png"), optimize=True)
    print("saved", os.path.relpath(os.path.join(out_dir, name + ".png"), REPO), can.size, "font", fsize)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("names", nargs="*")
    ap.add_argument("--out", default=os.path.join(REPO, "subjects", "biology", "images"))
    a = ap.parse_args()
    with open(a.spec) as f:
        spec = json.load(f)
    for n in a.names or spec:
        render(n, spec[n], a.out)


if __name__ == "__main__":
    main()
