#!/usr/bin/env python3
"""Audit labelled AI images for multi-panel layout (Gemini Flash vision on the raw picture).

  python tools/audit_panels.py [--only NAME ...]      -> .image-work/audit.json

For each labelled image (not Biology Section A): the separate panels / organisms with boxes (0-1000 of the raw picture),
which labels only name a whole panel or organism, and clear drawing mistakes (reported, never fixed).
"""
import argparse, glob, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
from common import RAW, WORK, REPO

SCHEMA = {"type": "OBJECT", "properties": {
    "panels": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {"name": {"type": "STRING"}, "x0": {"type": "INTEGER"}, "y0": {"type": "INTEGER"}, "x1": {"type": "INTEGER"}, "y1": {"type": "INTEGER"}}, "required": ["name", "x0", "y0", "x1", "y1"]}},
    "name_labels": {"type": "ARRAY", "items": {"type": "STRING"}},
    "problems": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {"what": {"type": "STRING"}, "confidence": {"type": "STRING", "enum": ["high", "medium"]}}, "required": ["what", "confidence"]}}},
    "required": ["panels", "name_labels", "problems"]}


def audit(name, desc, labels):
    pr = ("This is an unlabelled textbook illustration (labels will be added later in code). Description it was made from: " + desc[:1200] + "\n"
          "Labels to be added: " + json.dumps(labels, ensure_ascii=False) + "\n"
          "1) panels: list every SEPARATE panel, organism, specimen or drawing that stands on its own (for example three animals in three boxes, two test tubes drawn apart, stage 1 / stage 2 / stage 3). "
          "An enlarged inset or magnified circle belongs to the drawing it magnifies, and parts of one organism are NOT separate panels. A picture of one organism, one organ or one apparatus is ONE panel. "
          "Give each a short name and a box x0,y0,x1,y1 on a 0-1000 scale (x right, y down) covering its whole drawing. "
          "2) name_labels: which of the labels merely NAME a whole panel, organism or stage (such as 'Toad', 'stage 2', 'Amoeba', 'male') instead of naming a part inside it. Copy the label text exactly. "
          "3) problems: clear mistakes in the DRAWING itself that would mislead a student: a structure drawn as the wrong thing (for example bristles drawn as legs), wrong number of main structures, wrong colour for a real organism (for example a green blood cell), an organ in the wrong place, anatomy that is wrong. "
          "Report only mistakes you are sure of; confidence 'high' only if a biology or science teacher would immediately call it wrong. Do not report style, simplification, missing detail, or things you cannot see clearly.")
    return m.vision(pr, [os.path.join(RAW, name + ".png")], SCHEMA, "audit-panels", thinking="low")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only", nargs="*"); ap.add_argument("--workers", type=int, default=8); a = ap.parse_args()
    m.SUBJECT = "audit"; m.SUBJ = "audit-images2"
    desc = {}
    for f in glob.glob(os.path.join(REPO, "tools", "specs", "*", "*-prompts.json")):
        for n, p in json.load(open(f)): desc[n] = p
    items = []
    for f in sorted(glob.glob(os.path.join(REPO, "tools", "specs", "*", "*-labels.json"))):
        sub = f.split("/")[-2]
        if sub == "biology" and re.search(r"/A\d", f): continue
        for n, sp in json.load(open(f)).items():
            if sp.get("labels") and os.path.exists(os.path.join(RAW, n + ".png")) and (not a.only or n in a.only):
                items.append((n, sub, os.path.basename(f)[:-12], desc.get(n, ""), [e[0] for e in sp["labels"]]))
    out_p = os.path.join(WORK, "audit.json"); res = json.load(open(out_p)) if os.path.exists(out_p) else {}
    todo = [i for i in items if i[0] not in res]
    print(len(items), "labelled images;", len(todo), "to audit", flush=True)
    def one(it):
        n, sub, topic, d, labels = it
        try:
            r = audit(n, d, labels); r.update(subject=sub, topic=topic); res[n] = r
        except Exception as e:
            print("error", n, str(e)[:120], flush=True)
    with ThreadPoolExecutor(a.workers) as p: list(p.map(one, todo))
    json.dump(res, open(out_p, "w"), indent=1, ensure_ascii=False)
    multi = [n for n, r in res.items() if len(r["panels"]) >= 2]
    print(len(res), "audited;", len(multi), "multi-panel;", sum(1 for r in res.values() if any(p["confidence"] == "high" for p in r["problems"])), "with high-confidence drawing problems")


if __name__ == "__main__":
    main()
