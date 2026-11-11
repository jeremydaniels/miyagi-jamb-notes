# CLAUDE.md

## Project

Detailed JAMB UTME study notes for Miyagi Labs, written from the official JAMB syllabus. Students read them in the Miyagi Labs app.

- Each subject's official syllabus lives in its own subject folder as `syllabus.md` (e.g. `subjects/biology/syllabus.md`, `subjects/use-of-english/syllabus.md`). It is the source of truth for what must be covered. Syllabus files are typed exactly as written, mistakes included; errors are explained in a "Transcription notes" section, never silently corrected.
- The style and depth reference is `samples/sample-living-organisms.md`. Match it.

## Workflow

- Always show a plan and wait for approval before writing any content. For a new subject the plan is `subjects/<subject>/PLAN.md` (the file list) plus a cost estimate.
- **Gemini writes, Claude manages.** From now on, Gemini reads the syllabus PDFs and writes the notes through the scripts in `tools/`; Claude builds and runs the tools, checks the results and commits. Do not write whole notes files by hand unless fixing a flagged file. See "Gemini workflow" below.
- Always work on `main`. No other branches. Commit and push to `main` after every task (one commit per topic file, and one commit per topic's images).
- Write all the notes for a batch first, then generate images topic by topic in the same order. Every finished topic must look complete on its own.
- Before committing a topic, check it against the syllabus (see "Coverage check" below). For Gemini-written files, `tools/notes_checks.py` does the structural checks automatically (steps 2 and 3), and `tools/verify_notes.py` re-checks the maths, facts and option explanations (step 4); Claude spot-checks the rest.

## Gemini workflow (new subject)

1. The user adds `inbox/<subject>.pdf` (the folder name is the subject name, e.g. `inbox/chemistry.pdf`).
2. Run `python tools/transcribe_syllabus.py <subject>` and check `subjects/<subject>/syllabus.md` against the PDF (`pdftotext`). Fix the "Transcription notes" by hand if they are wrong or incomplete; never edit the syllabus text itself. Flag in the notes anything that looks unofficial or out of date, and tell the user.
3. Run `python tools/plan_subject.py <subject>` and show the user the file list in `PLAN.md`. Wait for approval.
4. Add `tools/rules/<subject>.md` if the subject needs extra rules (Mathematics has one; first line `<!-- code-execution -->` turns on Gemini's code execution for verified calculations). Give an estimate of the cost before the run.
5. After approval, run `python tools/write_notes.py <subject>` (Batch API by default: about half price, takes minutes to hours; use `--mode sync` only if the user needs it immediately). It resumes where it stopped (including a batch already submitted), checks every file automatically and flags failures. For a long batch run it in the background and wait to be notified. Commit each passing file on its own (one commit per topic file) and push to `main` after each chunk. The tools never run git.
6. **Verify every file.** Run `python tools/verify_notes.py <subject>` (Batch API by default; keep the model's default thinking level, because lower levels missed real errors). Gemini re-checks every worked example, practice answer and explanation of the wrong options with code execution and lists problems (file, location, issue, suggested fix); it never edits. Confirm numerical problems by recomputing them in Python; use judgement on wording and factual ones and list anything unsure for the user. Fix only confirmed problems, commit each fixed file separately, and re-run `verify_notes.py --only <file> --redo` only on files whose fix changed a number or a fact (wording-only fixes need no re-run). Do this before telling the user the subject is finished.
7. **Report the cost.** At the end of every subject give the user the writing, verification and setup totals from `python tools/write_notes.py <subject> --cost` (quote the list figure; the est figure applies assumed discounts).
8. Spot-check a few files yourself (recompute any calculations with Python, compare the style with Biology), and report flagged or failed files, problems found and fixed, and cost.

Rules for this workflow:
- `GEMINI_API_KEY` is in the environment. Never print, log or commit it. The tools use the Gemini REST API with the Python standard library only.
- Cost: there are no per-subject budgets. Runs go to the end of the subject. The only stop is the safety limit of $100 per subject (writing and verification together, list price) in `tools/gemini_pricing.json`; if a subject would reach it, stop and tell the user. Costs are logged in `.gemini-work/costs.jsonl` (git-ignored). Prices and the cached and Batch discount rates in `tools/gemini_pricing.json` are unverified assumptions until checked against Google's price page.
- Cost-saving settings are tested and fixed: Batch API by default, default thinking level for writing and verification, Pro for writing, verification and transcription, Flash only for planning and coverage repair. Do not lower the thinking level or switch models for writing or verification without a new test showing no loss in note length or in problems found.
- The style example sent to Gemini is `subjects/biology/D3-biotechnology.md`.

## File structure

- `inbox/` holds the source PDFs (`inbox/<subject>.pdf`). `subjects/<subject>/PLAN.md` is the approved file list for a subject.
- All subjects live under `subjects/`. Each subject gets its own folder: `subjects/biology/`, `subjects/chemistry/`, `subjects/physics/`, etc. A new subject's folder holds its `syllabus.md`, its topic files and its `images/` folder. `tools/`, `samples/` and `release/` stay at the repo root.
- One Markdown file per syllabus topic, numbered in syllabus order (e.g. `subjects/biology/A1-living-organisms.md`, `subjects/biology/A2a-...md`). A topic too big for one file is split with letter suffixes (e.g. `A2a-`, `A2b-`, `A2c-`).
- Images live in `subjects/<subject>/images/` (e.g. `subjects/biology/images/`) with clear names prefixed by the topic file (e.g. `A1-plant-cell.png`).

## Content rules

- Notes must cover EVERY topic, content item and objective in the syllabus. Nothing skipped.
- Accuracy matters most. Never invent facts. If something varies between textbooks (definitions, numbers, classifications, spellings), say so in the notes.
- Use simple, clear English for Nigerian secondary school students. Use Nigerian examples where they help (local plants, animals, foods, places, diseases).
- Match the style and depth of `samples/sample-living-organisms.md`.

## Depth rules (very important)

- Every objective in the syllabus gets its own clearly headed section that fully explains it. Don't just mention it.
- Every content item and named example in the syllabus (e.g. specific organisms, processes, diseases) must be explained, not just listed.
- Use comparison tables wherever the syllabus says "compare", "differentiate" or "contrast".
- Explain processes step by step (e.g. digestion, photosynthesis, fertilisation).
- Add `[IMAGE: ...]` placeholders wherever a diagram would help, each with a detailed description (what to show, labels, style) so it can be AI-generated later.
- Every file ends with, in this order:
  1. Key terms table
  2. Exam tips and common mistakes
  3. Quick summary (5 to 8 points)
  4. 10 practice questions (options A to D as a bullet list, then the answer and a short explanation)
- Big topics will be long. That's fine. Never shorten a topic to save space.

## Coverage check (before every commit)

1. List every content item, named example and objective for the topic from the syllabus file.
2. Confirm each one has its own heading or a clearly explained section in the notes, and each "compare/differentiate/contrast" objective has a table.
3. Confirm the four closing sections are present, the summary has 5 to 8 points, and there are exactly 10 practice questions with answers.
4. Re-read for factual accuracy and flag any textbook variations in the text.

## Image rules

Decisions are recorded in `IMAGES-PLAN.md`. The notes carry `[IMAGE: ...]` placeholders until their images are made and placed.

- **Gemini only.** All AI images use `GEMINI_API_KEY`. No OpenAI. Never print, log or commit the key. Check the available image models first (`python tools/generate.py --models`).
- **Models:** `gemini-3.1-flash-image` by default; `gemini-3-pro-image` for complex anatomy, multi-panel experiment diagrams and retries. Square image. Prices are unverified; the real cost comes from the token counts the API returns. Batch mode is used when it works and the quality matches (test it first).
- **Style:** clean, flat educational illustration, white background, soft palette, like a modern textbook. Not photorealistic.
- **Every AI image is generated with NO text, letters, numbers or labels in the picture.** Stray marks are painted out with `label.py`'s `whiten` only if tiny; anything structurally wrong is re-rolled.
- **Pipeline for every AI image:**
  1. Generate (no text).
  2. Check the unlabelled image with Gemini vision (Flash) against its placeholder: correct parts and structure, nothing extra, no stray text. Re-roll up to 2 times.
  3. If it has a label list: Gemini vision finds where each part is, then `label.py` draws the labels and pointer lines with Pillow. Gemini never writes the label text.
  4. Check the labelled image (each label points at the right part, readable, no overlap). Re-run the placement for a wrong label up to 2 times, then flag it.
  5. If an image still fails, leave the placeholder in the notes and list it in the report.
  6. Spot-check a sample yourself.
- **Code-drawn images** (graphs, charts, geometry, circuits, structures, flowcharts, timelines, tables, and maps as simplified sketches): draw with matplotlib (shared style in `tools/codedraw/style.py`) or Pillow, then run the same check (correct content, readable labels, no overlap) and fix the layout up to 2 times. Use Natural Earth data (public domain) where real outlines matter.
- **Skipped:** portraits of real people and images with Arabic script keep their placeholder text.
- **Sensitive images, marked "Needs teacher review":** CRK shows Jesus and angels in a respectful flat style and never depicts God (use symbols such as light or clouds). IRK shows faceless figures, no prophets, and prayer and ablution positions as simple step diagrams.
- Save final images in `subjects/<subject>/images/`, named `<topic prefix>-<slot>-<slug>`, and place them with `place_images.py` (`N:NAME=alt` for single slots) with good alt text. Compress with `compress_images.py`.
- Save each topic's prompts and label specs under `tools/specs/<subject>/`.
- **Budget:** stop and ask before the image spend of a run passes its stated cap (the Biology B to E run: $40). Work out the real cost of each call from the token usage the API returns and keep a running total.
- Allowed Python packages: Pillow and matplotlib. Ask before adding any other dependency.

## Nigeria schools project

A separate project in this repo: a dataset of Nigerian secondary schools. All work for it (data, scripts, docs) lives in `nigeria-schools/` (see `nigeria-schools/README.md`). It must never modify JAMB notes files or anything else outside `nigeria-schools/`. All work for it is done directly on `main` (no branches); commit and push to `main` after each task. The other JAMB rules above (Gemini workflow, notes, images) do not apply to it.
