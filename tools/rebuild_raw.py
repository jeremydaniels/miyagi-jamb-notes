"""Recover the raw (unlabelled) picture from a finished labelled image, then re-render its labels with the current label.py.

The raw pictures are not stored in the repo, but a finished image is the raw picture plus leader lines and label columns
that were drawn from the saved label spec (tools/specs/<subject>/<topic>-labels.json) by the OLD label.py (git commit
41deb1c). The old layout is replayed to find where the picture sits and exactly which pixels the leader lines and dots
cover; those pixels are filled in from their neighbours. The recovered picture is put back in a 1024x1024 canvas at its
original position, so the saved raw coordinates still fit, and label.render() draws the labels again.

  python tools/rebuild_raw.py biology B3a-transport-in-animals [--only NAME ...] [--dry]
"""
import argparse, importlib.util, json, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import REPO, RAW
import label as new

OLD_COMMIT = "41deb1c"
REGION_WORDS = ("cortex", "medulla", "pith", "endosperm", "lumen", "cytoplasm", "cavity", "zone", "region", "layer", "chamber", "matrix", "stroma", "cambium", "tissue", "space")


def old_label():
    src = subprocess.check_output(["git", "show", f"{OLD_COMMIT}:tools/label.py"], cwd=REPO).decode()
    d = tempfile.mkdtemp(); p = os.path.join(d, "old_label.py"); open(p, "w").write(src)
    spec = importlib.util.spec_from_file_location("old_label", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def inkmask(a, tol=40):
    return (np.abs(a.astype(int) - np.array([40, 44, 52])).max(axis=2) <= tol)


def inpaint(arr, mask, iters=12):
    arr = arr.astype(float); known = ~mask
    for _ in range(iters):
        if known.all(): break
        s = np.zeros_like(arr); c = np.zeros(mask.shape)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0: continue
                k = np.roll(np.roll(known, dy, 0), dx, 1); v = np.roll(np.roll(arr, dy, 0), dx, 1)
                s += v * k[..., None]; c += k
        fill = (~known) & (c > 0)
        arr[fill] = s[fill] / c[fill][:, None]; known = known | fill
    return arr.clip(0, 255).astype(np.uint8)


def _interp(arr, union, flag, axis, maxrun=44):
    """Fill the pixels in `flag` by linear interpolation across the band (axis 0: between the pixel above and below in each column;
    axis 1: left and right in each row). `union` is every pixel that is not trustworthy."""
    if axis == 1:
        arr = arr.transpose(1, 0, 2); union = union.T; flag = flag.T
    H = union.shape[0]; done = np.zeros_like(flag)
    for x in range(union.shape[1]):
        col = union[:, x]
        if not col.any():
            continue
        ys = np.flatnonzero(col)
        starts = ys[np.r_[True, np.diff(ys) > 1]]; ends = ys[np.r_[np.diff(ys) > 1, True]]
        for y0, y1 in zip(starts, ends):
            if y0 == 0 or y1 == H - 1 or y1 - y0 + 1 > maxrun:
                continue
            xl, xr = max(0, x - 2), min(union.shape[1], x + 3)
            top = arr[max(0, y0 - 3):y0, xl:xr].reshape(-1, arr.shape[2]).astype(float).mean(0)
            bot = arr[y1 + 1:min(H, y1 + 4), xl:xr].reshape(-1, arr.shape[2]).astype(float).mean(0)
            for y in range(y0, y1 + 1):
                if flag[y, x]:
                    t = (y - (y0 - 1)) / (y1 + 1 - (y0 - 1)); arr[y, x] = ((1 - t) * top + t * bot).round(); done[y, x] = True
    if axis == 1:
        arr = arr.transpose(1, 0, 2); done = done.T
    return arr, done


def repair(pic, segs, box, size, grow=11):
    """Remove leader lines: horizontal-ish lines are filled by vertical interpolation, steep lines by horizontal interpolation,
    dots by diffusion from the surrounding pixels."""
    W, H = size
    mh, mv, md = (Image.new("L", (W, H), 0) for _ in range(3))
    dh, dv, dd = ImageDraw.Draw(mh), ImageDraw.Draw(mv), ImageDraw.Draw(md)
    for s_, e_ in segs:
        (dh if abs(e_[0] - s_[0]) >= abs(e_[1] - s_[1]) else dv).line([s_, e_], fill=255, width=grow)
        dd.ellipse([e_[0] - 12, e_[1] - 12, e_[0] + 12, e_[1] + 12], fill=255)
    crop = lambda im: np.asarray(im.crop(box)) > 0
    H_, V_, D_ = crop(mh), crop(mv), crop(md)
    union = H_ | V_ | D_
    arr = np.asarray(pic).copy()
    arr, d1 = _interp(arr, union, H_ & ~D_, 0)
    arr, d2 = _interp(arr, union, V_ & ~D_ & ~d1, 1)
    left = union & ~d1 & ~d2
    return inpaint(arr, left)


def rebuild(name, spec, img_path, old):
    im = Image.open(img_path).convert("RGB"); W, H = im.size
    labs = [e for e in spec.get("labels", []) if e[2] != "F"]
    if not labs: return None, "no labels"
    d0 = ImageDraw.Draw(im)
    def width(e):
        bb = d0.multiline_textbbox((0, 0), e[0], font=old.FONT, spacing=4); return bb[2] - bb[0]
    wl = max([width(e) for e in labs if e[2] == "L"], default=0); wr = max([width(e) for e in labs if e[2] == "R"], default=0)
    padL = wl + 60 if wl else 24; padR = wr + 60 if wr else 24
    iw, ih = W - padL - padR, H - 48
    D = inkmask(np.asarray(im))
    core = np.ones_like(D)
    for dy in range(-3, 4):
        for dx in range(-3, 4):
            if dx * dx + dy * dy <= 9: core &= np.roll(np.roll(D, dy, 0), dx, 1)
    P = np.pad(core.astype(np.int32), 2000)
    CL, CT = 1024 - iw, 1024 - ih
    if CL < 0 or CT < 0: return None, "picture larger than 1024"
    score = np.zeros((CT + 1, CL + 1))
    for e in labs:
        x, y = e[1]
        rows = np.arange(CT + 1); cols = np.arange(CL + 1)
        score += P[np.ix_(y + 24 - rows + 2000, x + padL - cols + 2000)]
    ct, cl = np.unravel_index(score.argmax(), score.shape)
    if score.max() < 0.6 * len(labs): return None, f"dots not found (score {score.max():.0f}/{len(labs)})"
    segs = []
    old.leader = lambda dr, s, e: segs.append((s, e)); old.crop_box = lambda i: (int(cl), int(ct), int(cl) + iw, int(ct) + ih)
    tmpname = f"_rb{os.getpid()}"; Image.new("RGB", (1024, 1024), "white").save(os.path.join(RAW, tmpname + ".png"))
    tmp = tempfile.mkdtemp(); s2 = dict(spec); s2["src"] = tmpname; s2.pop("whiten", None)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()): old.render(tmpname, s2, tmp)
    if Image.open(os.path.join(tmp, tmpname + ".png")).size != (W, H): return None, "layout size mismatch"
    m = Image.new("L", (W, H), 0); dm = ImageDraw.Draw(m)
    for s, e in segs:
        dm.line([s, e], fill=255, width=9); dm.ellipse([e[0] - 9, e[1] - 9, e[0] + 9, e[1] + 9], fill=255)
    box = (padL, 24, padL + iw, 24 + ih)
    pic = repair(im.crop(box), segs, box, (W, H))
    raw = Image.new("RGB", (1024, 1024), "white"); raw.paste(Image.fromarray(pic), (int(cl), int(ct)))
    return raw, f"ok score {score.max():.0f}/{len(labs)} at ({cl},{ct})"


def relabel_spec(spec):
    s = {"labels": spec["labels"]}
    s["regions"] = [e[0] for e in spec["labels"] if any(w in e[0].lower() for w in REGION_WORDS)]
    return s


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("subject"); ap.add_argument("topics", nargs="*"); ap.add_argument("--only", nargs="*"); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--out"); a = ap.parse_args()
    old = old_label(); sd = os.path.join(REPO, "tools", "specs", a.subject); imgs = os.path.join(REPO, "subjects", a.subject, "images")
    out = a.out or imgs
    ok = bad = 0
    import glob
    files = sorted(glob.glob(os.path.join(sd, "[B-E]*-labels.json")))
    for f in files:
        if a.topics and not any(os.path.basename(f).startswith(t) for t in a.topics): continue
        for name, spec in json.load(open(f)).items():
            if a.only and name not in a.only: continue
            p = os.path.join(imgs, name + ".png")
            if not os.path.exists(p) or not spec.get("labels"): continue
            raw, msg = rebuild(name, spec, p, old)
            print(name, msg, flush=True)
            if raw is None: bad += 1; continue
            ok += 1
            if a.dry: continue
            raw.save(os.path.join(RAW, name + ".png"))
            new.render(name, relabel_spec(spec), out)
    print("rebuilt", ok, "failed", bad)


if __name__ == "__main__":
    main()
