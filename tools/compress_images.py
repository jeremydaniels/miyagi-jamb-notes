"""Shrink labelled PNGs in place with no visible quality loss.

Usage:
  python tools/compress_images.py biology/images [--min-psnr 36]

Converts each PNG to a 256-colour palette (median cut, Floyd-Steinberg
dithering) and saves it optimised. File names and links stay the same. An image
is left untouched if the result would be bigger, or if it differs too much from
the original (PSNR below --min-psnr dB). Running it twice is safe.
"""
import argparse, io, math, os
from PIL import Image, ImageChops, ImageStat


def psnr(a, b):
    mse = sum(v * v for v in ImageStat.Stat(ImageChops.difference(a, b)).rms) / 3
    return 99.0 if mse == 0 else 20 * math.log10(255 / math.sqrt(mse))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--min-psnr", type=float, default=36.0)
    a = ap.parse_args()
    before = after = 0
    for f in sorted(os.listdir(a.folder)):
        if not f.lower().endswith(".png"):
            continue
        p = os.path.join(a.folder, f)
        size = os.path.getsize(p)
        before += size
        im = Image.open(p)
        if im.mode == "P":  # already compressed
            after += size
            continue
        rgb = im.convert("RGB")
        q = rgb.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
        buf = io.BytesIO()
        q.save(buf, "PNG", optimize=True)
        score = psnr(rgb, q.convert("RGB"))
        if buf.tell() < size and score >= a.min_psnr:
            with open(p, "wb") as out:
                out.write(buf.getvalue())
            after += buf.tell()
            print(f"{f}: {size // 1024}K -> {buf.tell() // 1024}K (PSNR {score:.1f} dB)")
        else:
            after += size
            print(f"{f}: kept original (PSNR {score:.1f} dB, {buf.tell() // 1024}K vs {size // 1024}K)")
    print(f"Total: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
