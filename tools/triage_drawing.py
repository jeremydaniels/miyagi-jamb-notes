#!/usr/bin/env python3
"""Triage the confirmed drawing mistakes into factual (fix) and cosmetic (list only) with Gemini Pro.
python tools/triage_drawing.py -> .image-work/triage.json   {name: {category, reason, fix}}"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gemini_common as g
import redo_common as rc
from common import WORK

SYS = """You triage reported drawing mistakes in textbook illustrations for Nigerian secondary-school notes (JAMB exam preparation).
For each item decide:
FACTUAL (will be fixed by regenerating the picture, which costs money, so be strict) = a student looking at the picture would learn something FALSE about what the notes or labels teach: a wrong count of structures that the notes or labels count (ribs, toes, teeth, chambers, segments), a structure the notes or labels name that is missing or drawn as something else, a structure in the wrong place or wrongly connected, a wrong colour for a real organism or substance that the notes describe, or a result, direction or process drawn the wrong way round when that is the point of the figure. It must be clearly visible and central to the figure.
COSMETIC = everything else: style, rendering glitches or pixelation, lighting, minor proportions, gaps or breaks in lines, decorative or background details, apparatus details that do not change the lesson, missing arrows or extras not required by the notes or labels, panels or scenes where the exact count or position is not taught, things only the description (not the notes or labels) asked for.
When in doubt choose cosmetic. 'fix' (factual only, else ''): one imperative instruction of at most 40 words for the image generator that names the exact mistake to avoid and says what to draw instead (for example 'The horse foot skeleton has a single toe with two tiny splint bones; do not draw four toes.'). reason: at most 20 words."""
SC = {"type": "OBJECT", "properties": {"items": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {"id": {"type": "INTEGER"}, "category": {"type": "STRING", "enum": ["factual", "cosmetic"]}, "reason": {"type": "STRING"}, "fix": {"type": "STRING"}}, "required": ["id", "category", "reason", "fix"]}}}, "required": ["items"]}
GAP = re.compile(r"gap|broken|disconnect|disjoint|interrupt|severed", re.I)


def main():
    audit = json.load(open(os.path.join(WORK, "audit.json"))); dp = json.load(open(os.path.join(WORK, "drawing_problems.json")))
    items = []
    for n, v in dp.items():
        c = [x for x in v if x["verdict"] == "confirmed" and not GAP.search(x["claim"] + x["explanation"])]
        if not c: continue
        r = audit[n]; spec = rc.spec_for(n, r["subject"], r["topic"]); desc = rc.prompt_for(n, r["subject"], r["topic"])
        labels = [e[0] for e in spec.get("labels", [])] + [c_[0] for c_ in spec.get("captions", [])]
        items.append(dict(id=len(items), name=n, subject=r["subject"], description=desc[:700], labels=labels[:25], claims=[x["claim"][:300] + " || " + x["explanation"][:200] for x in c][:3], notes=rc.notes_excerpt(r["subject"], r["topic"], desc + " " + " ".join(labels), 900)))
    print(len(items), "items to triage", flush=True)
    out = {}
    def run(chunk):
        o = g.call_gemini([{"text": json.dumps(chunk, ensure_ascii=False)}], system=SYS, model=g.default_model(), json_schema=SC, thinking="low", subject="triage-images2", task="triage", timeout=600, attempts=4)
        for it in json.loads(o["text"])["items"]: out[it["id"]] = it
    chunks = [items[i:i + 8] for i in range(0, len(items), 8)]
    with ThreadPoolExecutor(6) as ex: list(ex.map(run, chunks))
    res = {it["name"]: dict(category=out[it["id"]]["category"], reason=out[it["id"]]["reason"], fix=out[it["id"]]["fix"], claims=it["claims"], subject=it["subject"]) for it in items if it["id"] in out}
    json.dump(res, open(os.path.join(WORK, "triage.json"), "w"), indent=1, ensure_ascii=False)
    print(len(res), "triaged;", sum(1 for v in res.values() if v["category"] == "factual"), "factual;", sum(1 for v in res.values() if v["category"] == "cosmetic"), "cosmetic")


if __name__ == "__main__":
    main()
