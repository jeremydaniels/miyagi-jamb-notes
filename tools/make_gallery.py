#!/usr/bin/env python3
"""Write subjects/<subject>/images/GALLERY-<subject>.md: every placed image with its alt text, by notes file, for browsing on a phone.
Also lists placeholders that are still in the notes, with the reason (from .image-work/jobs when available).
CRK and IRK images are marked "Needs teacher review"."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
subject = sys.argv[1] if len(sys.argv) > 1 else "biology"
sdir = os.path.join(REPO, "subjects", subject)
review = subject in ("crk", "irk")
WORK = os.environ.get("IMAGE_WORK_DIR") or os.path.join(REPO, ".image-work")
reasons = {}
for f in glob.glob(os.path.join(WORK, "jobs", "*.json")):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if d.get("status") in ("failed", "skipped"):
        reasons[os.path.basename(f)[:-5]] = (d["status"], d.get("reason", ""))
L = [f"# {subject.title()} images gallery\n", "Every image placed in the notes, grouped by notes file. Tap an image to enlarge. The caption under each image is its alt text.\n"]
if review:
    L.append("**All images in this subject need teacher review** (religious scenes drawn under the rules in IMAGES-PLAN.md).\n")
left = []; tot = 0
for f in sorted(glob.glob(os.path.join(sdir, "[A-Z][0-9]*.md"))):
    t = open(f).read(); topic = os.path.basename(f)[:-3]
    if subject == "biology" and topic[0] == "A":
        continue                                    # Section A has its own earlier run
    imgs = re.findall(r"!\[(.*?)\]\(images/([^)]+\.png)\)", t)
    ph = [l for l in t.split("\n") if l.startswith("[IMAGE:")]
    if not imgs and not ph:
        continue
    L.append(f"\n## {topic}\n")
    for alt, fn in imgs:
        L.append(f"![{alt}]({fn})\n"); L.append(f"*{alt}*" + (" - **Needs teacher review**" if review else "") + "\n"); tot += 1
    slot_names = [n for n in reasons if n.startswith(topic.split("-")[0] + "-")]
    for p in ph:
        left.append((topic, p[7:150].strip()))
L.insert(2, f"**{tot} images placed.** {len(left)} placeholders are still in the notes (listed at the end).\n")
if left:
    L.append("\n## Not made (placeholder still in the notes)\n")
    for topic, p in left:
        L.append(f"- `{topic}`: {p}...")
open(os.path.join(sdir, "images", f"GALLERY-{subject}.md"), "w").write("\n".join(L) + "\n")
print(subject, tot, "images,", len(left), "placeholders left")
