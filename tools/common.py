"""Shared paths and helpers for the image tools.

Working files (raw unlabelled images, the cost log, previews) go in a work
directory that is NOT committed: $IMAGE_WORK_DIR if set, otherwise
<repo>/.image-work/ (listed in .gitignore).
"""
import os
from PIL import ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get("IMAGE_WORK_DIR") or os.path.join(REPO, ".image-work")
RAW = os.path.join(WORK, "raw")
PREVIEW = os.path.join(WORK, "preview")
COST_LOG = os.path.join(WORK, "costs.jsonl")

for d in (RAW, PREVIEW):
    os.makedirs(d, exist_ok=True)

# Label font: Inter if installed, else DejaVu Sans, else Pillow's built-in font.
_FONT_CANDIDATES = {
    "medium": ["/usr/share/fonts/opentype/inter/Inter-Medium.otf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "semibold": ["/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
}


def font(weight="medium", size=26):
    for path in _FONT_CANDIDATES[weight]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)
