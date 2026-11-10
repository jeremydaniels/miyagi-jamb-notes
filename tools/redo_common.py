"""Shared helpers for the redo pass: notes excerpts, placeholder restore, spec access."""
import glob, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import REPO

STOPW = {"with", "from", "that", "this", "into", "each", "their", "which", "shown", "showing", "diagram", "picture", "image"}


def spec_for(name, sub, topic):
    p = os.path.join(REPO, "tools", "specs", sub, topic + "-labels.json")
    return json.load(open(p)).get(name, {}) if os.path.exists(p) else {}


def prompt_for(name, sub, topic):
    p = os.path.join(REPO, "tools", "specs", sub, topic + "-prompts.json")
    return dict(json.load(open(p))).get(name, "") if os.path.exists(p) else ""


def notes_excerpt(sub, topic, text, limit=1400):
    """Lines of the notes file that share distinctive words with the figure description or its labels."""
    md = os.path.join(REPO, "subjects", sub, topic + ".md")
    if not os.path.exists(md): return ""
    words = {w.lower() for w in re.findall(r"[A-Za-z]{5,}", text)} - STOPW
    best = []
    for line in open(md).read().split("\n"):
        if line.startswith(("![", "[IMAGE")) or len(line) < 40: continue
        ws = {w.lower() for w in re.findall(r"[A-Za-z]{5,}", line)}
        sc = len(ws & words)
        if sc >= 2: best.append((sc, line.strip()))
    best.sort(key=lambda x: -x[0])
    out = ""
    for _, l in best:
        if len(out) + len(l) > limit: break
        out += l + "\n"
    return out


def restore_placeholder(sub, topic, name):
    """Put the original [IMAGE: ...] line back in the notes in place of the image line. Returns True if done."""
    md = os.path.join(REPO, "subjects", sub, topic + ".md")
    rel = os.path.relpath(md, REPO)
    lines = open(md).read().split("\n")
    slot = None; k = 0
    slots = [i for i, l in enumerate(lines) if re.match(r"^(\[IMAGE:.*\]\s*$|!\[.*\]\(images/.*\.png\)\s*$)", l)]
    idx = next((i for i in slots if f"images/{name}.png)" in lines[i]), None)
    if idx is None: return False
    slot = slots.index(idx)
    revs = subprocess.check_output(["git", "log", "--format=%H", "-S", f"images/{name}.png", "--", rel], cwd=REPO, text=True).split()
    if not revs: return False
    first = revs[-1]
    old = subprocess.run(["git", "show", f"{first}^:{rel}"], cwd=REPO, capture_output=True, text=True)
    if old.returncode: return False
    ol = old.stdout.split("\n")
    oslots = [i for i, l in enumerate(ol) if re.match(r"^(\[IMAGE:.*\]\s*$|!\[.*\]\(images/.*\.png\)\s*$)", l)]
    if slot >= len(oslots) or not ol[oslots[slot]].startswith("[IMAGE:"): return False
    lines[idx] = ol[oslots[slot]]
    open(md, "w").write("\n".join(lines))
    return True
