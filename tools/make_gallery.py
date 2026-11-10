#!/usr/bin/env python3
"""Write subjects/<subject>/images/GALLERY-<subject>.md: every placed image with its alt text, by notes file, for browsing on a phone.
Also lists images that failed (placeholder still in the notes)."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
subject = sys.argv[1] if len(sys.argv) > 1 else "biology"
sdir = os.path.join(REPO, "subjects", subject)
SEC = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E"}
L = [f"# {subject.title()} images gallery\n", "Every image placed in the notes, grouped by notes file. Tap an image to enlarge. The caption under each image is its alt text.\n"]
failed = []
tot = 0
for f in sorted(glob.glob(os.path.join(sdir, "[A-Z][0-9]*.md"))):
    t = open(f).read(); topic = os.path.basename(f)[:-3]
    imgs = re.findall(r"!\[(.*?)\]\(images/([^)]+\.png)\)", t)
    ph = [l for l in t.split("\n") if l.startswith("[IMAGE:")]
    if topic[0] == "A" or (not imgs and not ph):
        continue
    L.append(f"\n## {topic}\n")
    for alt, fn in imgs:
        L.append(f"![{alt}]({fn})\n"); L.append(f"*{alt}*\n"); tot += 1
    for p in ph:
        failed.append((topic, p[7:140].strip()))
L.insert(2, f"**{tot} images** from Sections B to E.\n")
if failed:
    L.append("\n## Not made (placeholder still in the notes)\n")
    for topic, p in failed:
        L.append(f"- `{topic}`: {p}...")
open(os.path.join(sdir, "images", f"GALLERY-{subject}.md"), "w").write("\n".join(L) + "\n")
print(tot, "images,", len(failed), "placeholders left")
