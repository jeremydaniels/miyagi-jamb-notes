#!/usr/bin/env python3
"""Gemini Flash vision check of the re-rendered multi-panel images: caption overlaps, lines through other panels, cut-off text.
python tools/verify_panels.py  -> .image-work/verify_panels.json"""
import glob, json, os, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
from common import WORK, REPO
SCHEMA = {"type": "OBJECT", "properties": {"caption_overlaps": {"type": "BOOLEAN"}, "line_through_other_panel": {"type": "BOOLEAN"}, "text_cut_off": {"type": "BOOLEAN"}, "names_as_pointer_labels": {"type": "BOOLEAN"}, "details": {"type": "STRING"}},
          "required": ["caption_overlaps", "line_through_other_panel", "text_cut_off", "names_as_pointer_labels", "details"]}
PR = ("This is a textbook image with several panels or organisms. Captions sit under panels; pointer labels have a thin line ending in a dot on a part. Answer strictly from what you see: "
      "caption_overlaps = a caption or label text overlaps a drawing, an arrow or other text so it is hard to read; "
      "line_through_other_panel = a pointer line passes over a different panel or organism than the one its dot is on; "
      "text_cut_off = any text is cut off or outside the picture; "
      "names_as_pointer_labels = the name of a whole panel or organism (such as 'Toad') is drawn as a pointer label with a line and dot instead of a caption under its panel. details: one short sentence naming the worst problem.")


def main():
    rep = json.load(open(os.path.join(WORK, "panel_report.json")))
    names = [n for n, r in rep.items() if r["need"]]
    res = {}
    def one(n):
        r = rep[n]; p = os.path.join(REPO, "subjects", r["subject"], "images", n + ".png")
        try: res[n] = m.vision(PR, [p], SCHEMA, "verify-panels", thinking="low")
        except Exception as e: res[n] = {"error": str(e)[:100]}
    m.SUBJECT = "verify"; m.SUBJ = "verify-images2"
    with ThreadPoolExecutor(8) as ex: list(ex.map(one, names))
    json.dump(res, open(os.path.join(WORK, "verify_panels.json"), "w"), indent=1)
    bad = {n: v for n, v in res.items() if any(v.get(k) for k in ("caption_overlaps", "line_through_other_panel", "text_cut_off", "names_as_pointer_labels"))}
    print(len(res), "checked;", len(bad), "with problems;", {k: sum(1 for v in res.values() if v.get(k)) for k in ("caption_overlaps", "line_through_other_panel", "text_cut_off", "names_as_pointer_labels")})


if __name__ == "__main__":
    main()
