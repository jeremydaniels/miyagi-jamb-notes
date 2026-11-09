"""Replace [IMAGE: ...] placeholders in a notes file with images.

Usage:
  # every placeholder, in order (one NAME=alt pair per placeholder):
  python tools/place_images.py subjects/biology/A1-living-organisms.md "NAME=alt text" "NAME=alt text" ...

  # only some slots (N is the slot number, 1 = the first image slot in the file):
  python tools/place_images.py subjects/biology/B3a-transport-in-animals.md "5:B3a-05-heart=alt text" "9:B3a-09-vein=alt"

Slot numbers count every image slot in the file in order: an [IMAGE: ...] line
or an already placed ![alt](images/x.png) line. They do not change when other
slots are filled, so images can be placed in several runs. Replacing a slot that
already holds an image needs --force. Each image must already exist in the
images/ folder next to the notes file. All pairs in one call must use the same
form (all with N: or none).
"""
import os, re, sys

SLOT = re.compile(r"^(\[IMAGE:.*\]\s*$|!\[.*\]\(images/.*\.png\)\s*$)")
args = [a for a in sys.argv[1:] if a != "--force"]
force = "--force" in sys.argv
md, raw = args[0], args[1:]
numbered = [bool(re.match(r"^\d+:", a)) for a in raw]
if any(numbered) and not all(numbered):
    sys.exit("use N:NAME=alt for every pair, or none of them")
with open(md) as f:
    lines = f.read().split("\n")
slots = [i for i, line in enumerate(lines) if SLOT.match(line)]
if all(numbered) and raw:
    pairs = []
    for a in raw:
        n, rest = a.split(":", 1)
        name, alt = rest.split("=", 1)
        pairs.append((int(n), name, alt))
else:
    pairs = [(k + 1, *a.split("=", 1)) for k, a in enumerate(raw)]
    if len(slots) != len(pairs):
        sys.exit(f"{md} has {len(slots)} image slots but {len(pairs)} images were given")
for n, name, alt in pairs:
    if not 1 <= n <= len(slots):
        sys.exit(f"{md} has no slot {n} (it has {len(slots)})")
    if not os.path.exists(os.path.join(os.path.dirname(md), "images", name + ".png")):
        sys.exit(f"missing image: images/{name}.png")
    i = slots[n - 1]
    if not lines[i].startswith("[IMAGE:") and not force:
        sys.exit(f"slot {n} already holds an image; use --force to replace it")
for n, name, alt in pairs:
    lines[slots[n - 1]] = f"![{alt}](images/{name}.png)"
with open(md, "w") as f:
    f.write("\n".join(lines))
print(f"placed {len(pairs)} image(s) in {md}")
