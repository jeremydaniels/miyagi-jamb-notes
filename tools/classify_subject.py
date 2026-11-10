#!/usr/bin/env python3
"""Classify the [IMAGE: ...] placeholders of ONE subject (Gemini Flash, same rules as reclassify.py) and add or replace
that subject's rows in IMAGES-CLASSIFICATION.csv. Rows of other subjects are not touched.

  python tools/classify_subject.py computer-studies
"""
import csv, json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gemini_common as g
import extract_prompts as ex
import reclassify as rc

EXTRA = {"computer-studies": """
SUBJECT ADDENDUM (Computer Studies): logic gates, logic circuits, comparators, truth-table figures, flowcharts, algorithm and SDLC diagrams, network topologies (star, bus, ring as nodes and lines), network layouts, number-conversion layouts (repeated-division tables, place-value tables), memory and register block diagrams, the fetch-decode-execute and input-process-output cycles, timelines of computer history, storage-unit ladders, charts and tables = CODE (flowchart, cycle, hub, chart, table, timeline templates, or 'free' for circuits and block diagrams). Screens and software interfaces (Word, Excel, Access, PowerPoint, CorelDraw, Dreamweaver, browsers, e-mail) = CODE with template 'free' when they are simple window mock-ups, because they must show exact labelled regions. Pictures of devices and hardware (abacus, slide rule, Jacquard loom, computers, printers, scanners, drives, cables, connectors, robots, ATMs, satellites, people using computers) = AI. Portraits of real people (Babbage, Pascal, Hollerith and so on) = SKIP."""}


def main():
    subject = sys.argv[1]
    sdir = os.path.join(ex.REPO, "subjects", subject)
    rows, items = [], []
    for fname in sorted(os.listdir(sdir)):
        if not (fname.endswith(".md") and fname[0].isalpha() and fname[1:2].isdigit()):
            continue
        lines = open(os.path.join(sdir, fname), encoding="utf8").read().split("\n")
        for n, idx in enumerate(ex.slots(lines), 1):
            if not lines[idx].startswith("[IMAGE:"):
                continue
            full = " ".join(lines[idx][7:].rstrip().rstrip("]").split())
            body, labels = ex.parse_placeholder(lines[idx])
            rows.append(dict(subject=subject, file=fname, n_in_file=n, group="AI", kind=ex.slug(body)[:40].replace("-", " "),
                             alternative_for_FLAG="", placeholder_start=full[:120], old_group="", template="", parts="", regions="", caption="", reclass_note=""))
            items.append({"id": len(rows) - 1, "subject": subject, "old_group": "", "kind": rows[-1]["kind"], "description": body[:1100], "labels": labels})
    print(len(items), "placeholders in", len({r["file"] for r in rows}), "files", flush=True)
    res = {}
    def run(chunk):
        out = g.call_gemini([{"text": json.dumps(chunk, ensure_ascii=False)}], system=rc.SYS + EXTRA.get(subject, ""), model=g.load_pricing().get("flash_model"),
                            json_schema=rc.SCHEMA, thinking="low", subject="classify-images2", task="classify", timeout=600, attempts=4)
        for it in json.loads(out["text"])["items"]:
            res[it["id"]] = it
    chunks = [items[k:k + 12] for k in range(0, len(items), 12)]
    with ThreadPoolExecutor(6) as p:
        list(p.map(run, chunks))
    miss = [it for it in items if it["id"] not in res]
    if miss:
        with ThreadPoolExecutor(6) as p:
            list(p.map(run, [miss[k:k + 6] for k in range(0, len(miss), 6)]))
    for i, r in enumerate(rows):
        it = res.get(i)
        if not it:
            continue
        grp = it["group"]
        r["group"] = {"AI": "AI", "CODE": "CODE", "MAP": "FLAG", "SKIP": "SKIP"}[grp]
        r["template"] = it["template"] if grp == "CODE" else ("map" if grp == "MAP" else "")
        r["parts"] = json.dumps(it["parts"], ensure_ascii=False); r["regions"] = json.dumps(it["regions"], ensure_ascii=False)
        r["caption"] = it["caption"]; r["reclass_note"] = it["note"] + (" | annotations: " + "; ".join(it["annotations"]) if it["annotations"] else "")
    path = rc.CSV
    old = list(csv.DictReader(open(path, encoding="utf8")))
    fields = list(old[0].keys())
    keep = [r for r in old if r["subject"] != subject]
    with open(path, "w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(keep + rows)
    import collections
    print(collections.Counter((r["group"], r["template"]) for r in rows))


if __name__ == "__main__":
    main()
