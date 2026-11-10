#!/usr/bin/env python3
"""Cleanup pass for the failed placeholders: (1) accept pictures I judged right after looking at them, (2) simplify the
descriptions of the others for one more Pro attempt.  python tools/cleanup_failed.py accept|simplify  (see lists below)."""
import json, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import make_images as m
import gemini_common as g
from common import RAW, REPO

# AI pictures judged accepted after looking at them: name -> the saved failed picture to use
ACCEPT_AI = {
    "B1-11-rabbit-digestive-system-dissection": "B1-11-rabbit-digestive-system-dissection-try0.png",
    "B1-12-mammalian-urinary-system": "B1-12-mammalian-urinary-system-try1.png",
    "B2e-06-hepatobiliary-pancreatic-ducts": "B2e-06-hepatobiliary-pancreatic-ducts-try0.png",
    "B3b-13-bubble-potometer-apparatus": "B3b-13-bubble-potometer-apparatus-try0.png",
    "B7b-16-fruit-seed-dispersal-mechanisms": "B7b-16-fruit-seed-dispersal-mechanisms-try0.png",
    "C7a-02-anopheles-mosquito-life-cycle": "C7a-02-anopheles-mosquito-life-cycle-try0.png",
    "A5-02-prismatic-compass": "A5-02-prismatic-compass-try1.png",
    "B5-04-oxbow-lake-sequential": "B5-04-oxbow-lake-sequential-try0.png",
    "C6-03-rabbit-handling-housing": "C6-03-rabbit-handling-housing-try1.png",
    "B8-02-prophet-ezekiel-calling-scene": "B8-02-prophet-ezekiel-calling-scene-try1.png",
    "B2-01-elijah-fire-mount-carmel": "B2-01-elijah-fire-mount-carmel-try1.png",
}
# code drawings judged accepted: name -> alt text (the saved failed picture is used)
ACCEPT_CODE = {
    "D1-12-abo-blood-transfusion-compatibility": "Diagram of ABO blood groups: O donates to A, B and AB; A and B each donate to AB; AB is the universal recipient.",
    "A7-01-feudal-system-social-pyramid": "Pyramid of the feudal system with the king at the top, then nobles and lords, knights and vassals, and peasants and serfs at the base, with arrows for land granted down and loyalty and labour up.",
    "C1-01-map-nigeria-protectorates": "Sketch map of Nigeria around 1906 showing the Northern and Southern Nigeria protectorates, the dashed boundary between them, the Niger and Benue rivers, the Satiru uprising and the Asaba hinterland resistance.",
    "B4-01-timeline-th-century-benin": "Timeline of 19th-century Benin showing the reigns of Obas Obanosa, Osemwende, Adolo and Ovonramwen between 1804 and 1897.",
}
RETRY = ["B2d-02-types-human-teeth", "B6a-18-coleoptile-tropism-experiments", "B7b-12-fruit-placentation-types", "B7c-09-contraceptive-methods-overview", "E2-06-analogous-insect-bird-wings", "A18-02-capillary-action-meniscus-comparison", "A34-01-fleming-left-hand-rule", "A14a-03-hydrogen-chloride-fountain-experiment", "C2a-03-consonant-articulation-sagittal-diagrams", "A3-01-joseph-interpreting-pharaoh-dream"]

SUBJECTS = ['biology', 'physics', 'chemistry', 'mathematics', 'economics', 'government', 'use-of-english', 'literature-in-english', 'crk', 'irk', 'accounting', 'commerce', 'geography', 'agricultural-science', 'history']


def all_failed():
    L = json.load(open(os.path.join(REPO, ".image-work", "failed59.json")))
    return {x[1][:60]: x for x in L}


def simplify(names):
    """Gemini Flash writes a simpler description for each failed figure (facts kept, clutter removed)."""
    out = {}
    jobs = {}
    for s in SUBJECTS:
        m.SUBJECT = s
        for j in m.load_jobs(s, []):
            if j["name"] in names: jobs[j["name"]] = j
    for n, j in jobs.items():
        st = m.load_state(j)
        pr = ("A figure for a Nigerian secondary-school textbook failed an automatic check twice. Rewrite its description as a SIMPLER version that a drawing tool can get right, in at most 130 words. "
              "Keep every key fact and the main parts; remove clutter: no legends, no callout boxes, at most 8 text labels, short label wording, big simple shapes, clear spacing. "
              + ("For a map: draw only the country outline, the few named places as dots with short labels and the main routes or zones as simple shapes; do NOT draw internal state borders. " if j["template"] == "map" else "")
              + ("It is a picture drawn by an image model: describe the objects and their positions plainly; do not ask for exact counts above 4 (say 'several'), arrows or text. " if not j["code"] else "It is drawn in code: keep exact labels, but simple layout. ")
              + f"\n\nORIGINAL DESCRIPTION:\n{j['full'][:1800]}\n\nWHY IT FAILED:\n{st.get('reason','')[:500]}\n\nReturn only the new description.")
        r = g.call_gemini([{"text": pr}], model=g.load_pricing().get("flash_model"), thinking="low", subject="cleanup-images2", task="simplify", timeout=300, attempts=3)
        out[n] = r["text"].strip()
    json.dump(out, open(os.path.join(REPO, ".image-work", "simplified.json"), "w"), indent=1, ensure_ascii=False)
    print(len(out), "simplified")


def accept():
    for s in SUBJECTS:
        m.SUBJECT = s; m.SUBJ = s + "-images2"
        jobs = {j["name"]: j for j in m.load_jobs(s, [])}
        ai = [jobs[n] for n in ACCEPT_AI if n in jobs]
        for j in ai:
            shutil.copy(os.path.join(REPO, ".image-work", "failed", ACCEPT_AI[j["name"]]), os.path.join(RAW, j["name"] + ".png"))
            m.save_state(j, {"status": "pending", "cost_note": 0})
            m.ACCEPT.add(j["name"])
        for n, alt in ACCEPT_CODE.items():
            if n in jobs:
                j = jobs[n]
                dest = os.path.join(REPO, "subjects", s, "images", n + ".png")
                from PIL import Image
                Image.open(os.path.join(REPO, ".image-work", "failed", n + "-code.png")).convert("RGB").save(dest, optimize=True)
                m.save_state(j, {"status": "passed", "alt": alt, "log": [{"accepted_by_review": True}], "code_ext": "py"})
        if ai or any(n in jobs for n in ACCEPT_CODE):
            m.run([j for j in jobs.values() if j["name"] in ACCEPT_AI or j["name"] in ACCEPT_CODE], 4)


if __name__ == "__main__":
    {"accept": accept, "simplify": lambda: simplify([n for x in all_failed().values() for n in [x[1]] if n not in ACCEPT_AI and n not in ACCEPT_CODE])}[sys.argv[1]]()
