#!/usr/bin/env python3
"""Second opinion (Gemini Pro) on the drawing mistakes reported by tools/audit_panels.py. Never fixes anything.
python tools/verify_drawing_problems.py -> .image-work/drawing_problems.json"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
import gemini_common as g
from common import WORK, REPO
SC = {"type": "OBJECT", "properties": {"claims": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {"claim": {"type": "STRING"}, "verdict": {"type": "STRING", "enum": ["confirmed", "not_confirmed"]}, "explanation": {"type": "STRING"}}, "required": ["claim", "verdict", "explanation"]}}}, "required": ["claims"]}


def main():
    audit = json.load(open(os.path.join(WORK, "audit.json")))
    items = {n: [p["what"] for p in r["problems"] if p["confidence"] == "high"] for n, r in audit.items()}
    items = {n: v for n, v in items.items() if v}
    res = {}
    def one(n):
        r = audit[n]; p = os.path.join(REPO, "subjects", r["subject"], "images", n + ".png")
        if not os.path.exists(p): return
        parts = [{"text": "You are a careful biology/science teacher reviewing a textbook illustration for secondary students. A reviewer reported the mistakes below in the DRAWING. For each claim, decide: 'confirmed' only if you can see the mistake clearly in this picture and it is a real scientific error a teacher would correct (not style, simplification or something you cannot see); otherwise 'not_confirmed'. Then a one-sentence explanation.\nCLAIMS:\n" + "\n".join(f"- {c}" for c in items[n])},
                 {"inline_data": {"mime_type": "image/jpeg", "data": m.jpeg_b64(p, 1400)}}]
        try:
            o = g.call_gemini(parts, model=g.default_model(), json_schema=SC, thinking="low", subject="drawingcheck-images2", task="verify-drawing", timeout=300, attempts=3)
            res[n] = json.loads(o["text"])["claims"]
        except Exception as e:
            res[n] = [{"claim": "error", "verdict": "not_confirmed", "explanation": str(e)[:80]}]
    with ThreadPoolExecutor(8) as ex: list(ex.map(one, items))
    json.dump(res, open(os.path.join(WORK, "drawing_problems.json"), "w"), indent=1, ensure_ascii=False)
    conf = {n: [c for c in v if c["verdict"] == "confirmed"] for n, v in res.items()}
    conf = {n: v for n, v in conf.items() if v}
    print(len(res), "images checked;", len(conf), "with a confirmed mistake")


if __name__ == "__main__":
    main()
