#!/usr/bin/env python3
"""Step 2 of the image run: reclassify every placeholder with the new rules and rewrite IMAGES-CLASSIFICATION.csv.

Rules (Gemini Flash reads each placeholder):
  AI    anatomy, organs, cells, plant and animal sections, organisms, apparatus and lab set-ups, realistic objects, machines,
        tools, landforms and scenes (including Bible and history scenes).
  CODE  graphs, charts, tables, flowcharts, cycles, timelines, T-accounts (fixed templates in tools/codedraw/templates.py),
        and exact drawings with no template (geometry, circuits, ray and force diagrams, structures): free-form code.
  MAP   any map: drawn in code as a simplified sketch (Natural Earth outlines), labelled as a sketch.
  SKIP  portraits of real people and anything with Arabic script: the placeholder stays.
For AI pictures with a label list the labels are split into `parts` (real parts that get a pointer line) and
`annotations` (process notes, directions, test results, measurements), which become one caption under the picture.

New CSV columns: template, parts, regions, caption, reclass_note (parts and regions are JSON lists).
"""
import csv, json, os, sys, re
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gemini_common as g
import extract_prompts as ex
REPO = ex.REPO
SUBJ = "reclassify-images2"
CSV = os.path.join(REPO, "IMAGES-CLASSIFICATION.csv")

SYS = """You sort textbook figure descriptions (from Nigerian secondary-school notes) into how the picture will be made.
For each item return group, template, parts, regions, annotations, caption, note.
group: 'AI' = drawn by an image model: anatomy, organs, cells, tissues, plant and animal sections (transverse and longitudinal sections of roots, stems, leaves), organisms, life cycles drawn as pictures, apparatus and laboratory set-ups, realistic objects, machines, farm tools, buildings, landforms, scenes (including Bible and history scenes), people doing things, specimens.
 'CODE' = drawn in code because it must be exact: graphs and curves, bar/pie charts, tables, flowcharts, cycles shown as boxes and arrows, concept maps, organisation charts, timelines, T-accounts and ledger layouts, number lines, geometry and constructions, circuits, ray/wave/force/vector diagrams, chemical structural formulae, atoms and energy profiles, Venn diagrams, forms and statements (cheque, invoice, balance sheet).
 'MAP' = any map or route/territory diagram. 'SKIP' = portraits or photographs of real people, or anything that must show Arabic script (Qur'an, hadith, manuscripts).
 A picture of apparatus or an object with realistic appearance is AI even if the description says 'diagram'; a schematic of boxes, arrows or symbols is CODE.
template (only for CODE): flowchart | cycle | hub | graph | chart | table | timeline | taccount | free. flowchart = steps, trees, organisation charts, classification charts and any boxes-and-arrows diagram; cycle = a closed loop of 3-8 stages; hub = one central idea with 3-8 spokes; graph = x-y axes with curves/lines/shading (economics curves, physics graphs, equilibrium); chart = bar/pie/stacked chart; table = a comparison or data table; timeline = dated events; taccount = ledger T accounts; free = anything else exact (geometry, circuits, rays, forces, number lines, structures, atoms). Use '' for AI, MAP and SKIP.
For AI items that have a label list: parts = the labels that name a real part, object, organism or panel (these get pointer lines; keep each label text EXACTLY as given). annotations = labels that are NOT a part: process notes, directions of flow or movement, 'oxygen in', 'inspiration', test results, measurements, conditions, times, titles of whole experiments. caption = one short caption (max 25 words) built ONLY from the annotation words, to go under the picture ('' if no annotations). regions = those parts that are areas or layers (cortex, medulla, tissue layers, chambers, zones) rather than points or lines. If there is no label list, parts=[] annotations=[] caption=''.
note: at most 12 words saying why this group (and why it moved if the old group differs)."""

SCHEMA = {"type": "OBJECT", "properties": {"items": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
    "id": {"type": "INTEGER"}, "group": {"type": "STRING", "enum": ["AI", "CODE", "MAP", "SKIP"]},
    "template": {"type": "STRING"}, "parts": {"type": "ARRAY", "items": {"type": "STRING"}}, "regions": {"type": "ARRAY", "items": {"type": "STRING"}},
    "annotations": {"type": "ARRAY", "items": {"type": "STRING"}}, "caption": {"type": "STRING"}, "note": {"type": "STRING"}},
    "required": ["id", "group", "template", "parts", "regions", "annotations", "caption", "note"]}}}, "required": ["items"]}


def full_text(subject, fname, n):
    lines = open(os.path.join(REPO, "subjects", subject, fname)).read().split("\n")
    k = 0
    for i in ex.slots(lines):
        k += 1
        if k == n and lines[i].startswith("[IMAGE:"):
            return " ".join(lines[i][7:].rstrip().rstrip("]").split())
    return None


def main():
    rows = list(csv.DictReader(open(CSV)))
    todo = []
    for i, r in enumerate(rows):
        t = full_text(r["subject"], r["file"], int(r["n_in_file"]))
        r["_full"] = t if t is not None else r["placeholder_start"]
        r["_placed"] = t is None
        todo.append(i)
    # biology Sections A and already placed images keep their old classification (nothing left to do for them)
    todo = [i for i in todo if not rows[i]["_placed"]]
    print(len(todo), "placeholders to classify", flush=True)
    res = {}
    def run(chunk):
        items = []
        for i in chunk:
            r = rows[i]; body, labels = ex.parse_placeholder("[IMAGE: " + r["_full"] + "]")
            items.append({"id": i, "subject": r["subject"], "old_group": r["group"], "kind": r["kind"], "description": body[:1100], "labels": labels})
        out = g.call_gemini([{"text": json.dumps(items, ensure_ascii=False)}], system=SYS, model=g.load_pricing().get("flash_model"),
                            json_schema=SCHEMA, thinking="low", subject=SUBJ, task="reclassify", timeout=600, attempts=4)
        for it in json.loads(out["text"])["items"]:
            res[it["id"]] = it
    chunks = [todo[k:k + 12] for k in range(0, len(todo), 12)]
    with ThreadPoolExecutor(8) as p:
        list(p.map(run, chunks))
    miss = [i for i in todo if i not in res]
    if miss:
        with ThreadPoolExecutor(8) as p:
            list(p.map(run, [miss[k:k + 6] for k in range(0, len(miss), 6)]))
    new_cols = ["old_group", "template", "parts", "regions", "caption", "reclass_note"]
    for i, r in enumerate(rows):
        r["old_group"] = r["group"]; r.setdefault("template", ""); r["parts"] = r["regions"] = r["caption"] = r["reclass_note"] = ""
        it = res.get(i)
        if it:
            grp = it["group"]
            r["group"] = {"AI": "AI", "CODE": "CODE", "MAP": "FLAG", "SKIP": "SKIP"}[grp]
            r["template"] = it["template"] if grp == "CODE" else ("map" if grp == "MAP" else "")
            r["parts"] = json.dumps(it["parts"], ensure_ascii=False); r["regions"] = json.dumps(it["regions"], ensure_ascii=False)
            r["caption"] = it["caption"]; r["reclass_note"] = it["note"]
            if it["annotations"]: r["reclass_note"] += " | annotations: " + "; ".join(it["annotations"])
    fields = [f for f in rows[0].keys() if not f.startswith("_")]
    for c in new_cols:
        if c not in fields: fields.append(c)
    with open(CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    import collections
    c = collections.Counter((r["subject"], r["old_group"], r["group"]) for r in rows)
    for k in sorted(c): print(k, c[k])


if __name__ == "__main__":
    main()
