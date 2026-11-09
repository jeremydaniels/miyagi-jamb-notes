"""Pull the [IMAGE: ...] placeholders out of notes files and write prompt files for generate.py.

Usage:
  python tools/extract_prompts.py subjects/biology/B3a-transport-in-animals.md
  python tools/extract_prompts.py subjects/biology/B3a-....md --only 5 7     # slot numbers (see below)
  python tools/extract_prompts.py subjects/biology/B3a-....md --group ALL    # ignore IMAGES-CLASSIFICATION.csv

Writes, next to the other specs:
  tools/specs/<subject>/<topic>-prompts.json      [[name, prompt], ...]  (labels removed: images are made with no text)
  tools/specs/<subject>/<topic>-labels-todo.json  {name: [label, ...]}   (the label list to place later with label.py)

Slot numbers count every image slot in the file in order: an [IMAGE: ...] line
or an already placed ![alt](images/x.png) line. They are the same numbers that
place_images.py uses with the N:NAME=alt form, and they do not change when
other slots are filled.

By default only placeholders classed AI in IMAGES-CLASSIFICATION.csv are used
(the CSV is matched by subject, file and the order of the placeholders).
Names are <topic prefix>-<slot>-<short slug>, for example B3a-05-mammalian-heart.
"""
import argparse, csv, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLOT = re.compile(r"^(\[IMAGE:.*\]\s*$|!\[.*\]\(images/.*\.png\)\s*$)")
LABELS = re.compile(r"\bLabels?(?: to add(?: later)?)?\s*:\s*(.*?)(?=\s*(?:Clean flat|Use contrasting|Style:|$))", re.S)
STOP = {"a", "an", "the", "of", "and", "with", "in", "on", "showing", "diagram", "illustration", "to", "for", "side", "by"}


def slots(lines):
    return [i for i, l in enumerate(lines) if SLOT.match(l)]


def split_labels(s):
    q = re.findall(r'"([^"]+)"', s)
    if q:
        return [x.strip() for x in q]
    return [x.strip(" .") for x in re.split(r",\s*(?![^()]*\))", s.rstrip(". ")) if x.strip(" .")]


def slug(text, n=4):
    w = [x for x in re.findall(r"[a-z]+", text.lower()) if x not in STOP]
    return "-".join(w[:n]) or "image"


def load_classes(subject, fname):
    path = os.path.join(REPO, "IMAGES-CLASSIFICATION.csv")
    out = {}
    if os.path.exists(path):
        for r in csv.DictReader(open(path)):
            if r["subject"] == subject and r["file"] == fname:
                out[int(r["n_in_file"])] = r
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("notes", nargs="+")
    ap.add_argument("--only", nargs="+", type=int, help="slot numbers to extract")
    ap.add_argument("--group", default="AI", help="AI (default), CODE, FLAG or ALL")
    a = ap.parse_args()
    for md in a.notes:
        md = os.path.relpath(os.path.abspath(md), REPO)
        subject, fname = md.split(os.sep)[1], os.path.basename(md)
        topic = fname[:-3]
        prefix = topic.split("-")[0]
        lines = open(os.path.join(REPO, md)).read().split("\n")
        classes = load_classes(subject, fname)
        ph_no = 0
        prompts, todo = [], {}
        for slot_no, idx in enumerate(slots(lines), 1):
            line = lines[idx]
            if not line.startswith("[IMAGE:"):
                continue
            ph_no += 1
            if a.only and slot_no not in a.only:
                continue
            grp = classes.get(ph_no, {}).get("group", "AI")
            if a.group != "ALL" and grp != a.group:
                continue
            body = line[len("[IMAGE:"):].rstrip().rstrip("]").strip()
            labels = []
            m = LABELS.search(body)
            if m:
                labels = split_labels(m.group(1))
                body = (body[:m.start()] + body[m.end():]).strip()
            body = re.sub(r"\s*Clean flat textbook style,? white background,?[^.]*\.?", "", body).strip()
            body = re.sub(r"\s+", " ", body)
            name = f"{prefix}-{slot_no:02d}-{slug(classes.get(ph_no, {}).get('kind') or body)}"
            prompts.append([name, body])
            if labels:
                todo[name] = labels
        d = os.path.join(REPO, "tools", "specs", subject)
        os.makedirs(d, exist_ok=True)
        if prompts:
            json.dump(prompts, open(os.path.join(d, f"{topic}-prompts.json"), "w"), indent=1, ensure_ascii=False)
            json.dump(todo, open(os.path.join(d, f"{topic}-labels-todo.json"), "w"), indent=1, ensure_ascii=False)
        print(f"{fname}: {len(prompts)} prompt(s) -> tools/specs/{subject}/{topic}-prompts.json")


if __name__ == "__main__":
    sys.exit(main())
