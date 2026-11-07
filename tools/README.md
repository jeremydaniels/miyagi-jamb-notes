# Tools

Two toolkits live here:

1. **Gemini text tools** (this section): turn a subject's syllabus PDF into finished notes.
2. **Image tools** (second half of this file): labelled diagrams. **Image generation is paused**, so notes only carry `[IMAGE: ...]` placeholders for now.

## Gemini workflow: adding a new subject

Gemini does the heavy work (reading the PDF, planning, writing). Claude acts as manager: runs the tools, checks the results and commits.

Setup: `export GEMINI_API_KEY=...` (never print, log or commit it). Python standard library only; no packages to install. Prices are in `gemini_pricing.json` (currently marked unverified: check them against the Google pricing page).

```bash
# 0. Put the official PDF in inbox/ named after the subject folder
#    inbox/chemistry.pdf

# 1. Exact text copy of the syllabus -> subjects/chemistry/syllabus.md
python tools/transcribe_syllabus.py chemistry
#    Check it against the PDF (pdftotext) and fix the "Transcription notes" if needed.

# 2. Proposed file list -> subjects/chemistry/PLAN.md   (human approves / edits it)
python tools/plan_subject.py chemistry

# 3. Write all the notes (resumes where it stopped; never touches git)
python tools/write_notes.py chemistry --workers 3 --budget 25
python tools/write_notes.py chemistry --status        # done / flagged / pending
python tools/write_notes.py --cost                    # tokens and USD per file and subject
```

| Tool | What it does |
|---|---|
| `transcribe_syllabus.py` | Sends `inbox/<subject>.pdf` to Gemini; saves `subjects/<subject>/syllabus.md` as a word-for-word copy (mistakes kept) with a "Transcription notes" section for typing errors and anything that looks unofficial or out of date. |
| `plan_subject.py` | Gemini proposes the topic files (syllabus order, big topics split into parts `a`, `b`, `c`) and writes `PLAN.md`. Checks that every topic, content item and objective is assigned to exactly one file. |
| `write_notes.py` | For each file in `PLAN.md`: sends the notes rules from `CLAUDE.md`, that topic's exact syllabus text, one finished Biology file (`subjects/biology/D3-biotechnology.md`) as the style example and the subject rules in `tools/rules/<subject>.md`; saves the file only if `notes_checks.py` passes. |
| `notes_checks.py` | The automatic checks: closing sections in order, 5 to 8 summary points, exactly 10 questions each with options A to D and an answer with explanation, a heading for every objective and content item (via a hidden coverage map), image placeholders, balanced `$` maths, no leaked narration. |
| `gemini_common.py`, `syllabus_utils.py` | Shared REST client (standard library), cost log, syllabus and plan parsing. |

**Subject rules.** `tools/rules/<subject>.md` holds extra rules for that subject. If its first line is `<!-- code-execution -->`, Gemini's code execution tool is switched on and the file must use it (used for Mathematics, where every calculation is verified). Add a rules file for Physics or Chemistry the same way.

**Failures.** A file that fails the checks is re-asked with the problem list (up to 2 retries). If it still fails it is *flagged*: the attempt is kept in `.gemini-work/flagged/<subject>/` with a `.problems.json` file and nothing is written to `subjects/`. Fix by hand or run `--retry-flagged`.

**Cost control.** Every call is logged to `.gemini-work/costs.jsonl` (git-ignored; tokens and USD, never the key). `write_notes.py` stops before a call that could take the subject's total spend over `--budget` (default $25). Stop and ask before raising it. Logged costs use list prices and ignore cached-token discounts, so they are an upper bound.

---

# Image tools (paused)

These scripts make the labelled diagrams in `subjects/<subject>/images/` (for example `subjects/biology/images/`). They work the same way for any subject.

The process: generate each picture **with no text**, look at it, add the labels yourself with Pillow, look again, and fix anything wrong. The model often puts parts in slightly odd places, so never place labels without looking at the image first.

## Setup

```bash
pip install openai pillow
export OPENAI_API_KEY=...        # never print, log or commit it
```

Working files go in `.image-work/` at the repo root, which is git-ignored. To put them somewhere else, set `IMAGE_WORK_DIR`. That folder holds:

- `raw/`: unlabelled images from the API
- `costs.jsonl`: one line per API call, with its token usage and cost in USD
- `preview/`: gridded and zoomed copies for reading coordinates

## Scripts

| Script | What it does |
|---|---|
| `generate.py` | Calls OpenAI (`gpt-image-2`, 1024x1024, quality "medium"), adds the house style to each prompt, saves `raw/<name>.png` and logs the real cost from the returned token usage. It skips a call if the running total plus that call could go over `--budget` (default $5). |
| `preview.py` | `grid` draws a pixel grid on a raw image. `zoom` enlarges a small area. `small` shrinks a finished labelled image so you can check it. |
| `label.py` | Reads a label spec and draws the labels, leader lines, captions and arrows. Saves the final PNG to `subjects/biology/images/` by default (change with `--out`, e.g. `--out subjects/chemistry/images`). |
| `compress_images.py` | Shrinks the finished PNGs in place (256-colour palette with dithering, no visible loss; about 60% smaller). File names stay the same, so links still work. |
| `place_images.py` | Replaces the `[IMAGE: ...]` lines in a notes file, in order, with `![alt](images/NAME.png)`. |
| `common.py` | Shared paths and fonts. Uses Inter if it is installed, otherwise DejaVu Sans. |

## Doing a topic (example: chemistry C1)

1. **Write the prompts.** Read every `[IMAGE: ...]` placeholder in the notes and make `tools/specs/chemistry/C1-prompts.json`, a list of `[name, prompt]` pairs. Name each image after its topic file (e.g. `C1-...`). Describe what to draw, where each part goes and the colours. Don't ask for labels, because the style text already forbids any text in the image.
2. **Generate:**
   ```bash
   python tools/generate.py tools/specs/chemistry/C1-prompts.json --subject chemistry
   python tools/generate.py tools/specs/chemistry/C1-prompts.json C1-some-image   # redo just one image
   python tools/generate.py --total                                               # running cost
   ```
3. **Look at every raw image** and check it is accurate (correct number of parts, correct shapes, no stray text). Regenerate any that are wrong with a stricter prompt; for example, "EXACTLY THREE lips" fixed the Ascaris head.
4. **Find coordinates:**
   ```bash
   python tools/preview.py grid C1-some-image
   python tools/preview.py zoom C1-some-image 400 300 520 420 4
   ```
   Then check that each dot will land on the right part, not on the white background next to it.
5. **Write the label spec** `tools/specs/chemistry/C1-labels.json`. All the options are listed at the top of `label.py`. A short example:
   ```json
   {"C1-some-image": {
      "labels":   [["Nucleus", [430, 380], "L", 320], ["Cell wall", [283, 620], "R"]],
      "captions": [["Plant cell", 255, 0]],
      "arrows":   [[[100, 500], [200, 500]]]
   }}
   ```
6. **Render, then check the result:**
   ```bash
   python tools/label.py tools/specs/chemistry/C1-labels.json --out subjects/chemistry/images
   python tools/preview.py small C1-some-image   # only for images in subjects/biology/images; otherwise open the PNG directly
   ```
   Look at every labelled image. Fix any dot that misses its part, any lines that cross and any text that overlaps, then render again.
7. **Place the images in the notes:**
   ```bash
   python tools/place_images.py chemistry/C1-....md "C1-image-a=Alt text for image a" "C1-image-b=..."
   ```
8. **Compress** the finished images: `python tools/compress_images.py chemistry/images`. Running it twice is safe; images that are already compressed are skipped.
9. Commit the notes, images and specs for that topic, then push.

## The biology specs

`specs/biology/` holds the prompts and label specs used for A1 to A3. They are worked examples. The label coordinates only fit the original raw images, which are not committed because they take a lot of space. If you regenerate an image you get a different picture, so its labels must be placed again.

Two raw images were also edited by hand before labelling:

- `A2c-tapeworm-life-cycle`: the model kept drawing 4 hooks on the embryo, so the hooks were painted over and redrawn as 6.
- `A2c-ascaris`: regenerated with a stricter prompt (already in `A2c-prompts.json`).

## Cost

With `gpt-image-2` at 1024x1024 and quality "medium", each image used about 1,756 output image tokens and about 250 text input tokens, which is about $0.054. The rates in `generate.py` (`PRICE`) are per 1M tokens: $5 text input and $30 image output. Check them against OpenAI's pricing page before each batch. The 69 calls for A1 to A3 cost $3.71.
