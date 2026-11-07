"""Replace the [IMAGE: ...] placeholder lines in a notes file, in order, with images.

Usage:
  python tools/place_images.py subjects/biology/A1-living-organisms.md "NAME=alt text" "NAME=alt text" ...

Give exactly one NAME=alt pair per placeholder, in the order they appear.
Each image must already exist in the images/ folder next to the notes file.
"""
import os, sys

md, pairs = sys.argv[1], [a.split("=", 1) for a in sys.argv[2:]]
with open(md) as f:
    lines = f.read().split("\n")
slots = [i for i, line in enumerate(lines) if line.startswith("[IMAGE:")]
if len(slots) != len(pairs):
    sys.exit(f"{md} has {len(slots)} placeholders but {len(pairs)} images were given")
for i, (name, alt) in zip(slots, pairs):
    if not os.path.exists(os.path.join(os.path.dirname(md), "images", name + ".png")):
        sys.exit(f"missing image: images/{name}.png")
    lines[i] = f"![{alt}](images/{name}.png)"
with open(md, "w") as f:
    f.write("\n".join(lines))
print(f"placed {len(pairs)} images in {md}")
