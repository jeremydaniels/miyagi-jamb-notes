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
5. After approval, run `python tools/write_notes.py <subject>`. It resumes where it stopped, checks every file automatically and flags failures. Commit each passing file on its own (one commit per topic file) and push to `main` after each chunk. The tools never run git.
6. **Verify every file.** Run `python tools/verify_notes.py <subject>` (separate budget, default $10; tell the user the estimate first). Gemini re-checks every worked example, practice answer and explanation of the wrong options with code execution and lists problems (file, location, issue, suggested fix); it never edits. Confirm numerical problems by recomputing them in Python; use judgement on wording and factual ones and list anything unsure for the user. Fix only confirmed problems, commit each fixed file separately, and re-run `verify_notes.py --only <file> --redo` on the fixed files. Do this before telling the user the subject is finished.
7. Spot-check a few files yourself (recompute any calculations with Python, compare the style with Biology), and report flagged or failed files, problems found and fixed, and cost.

Rules for this workflow:
- `GEMINI_API_KEY` is in the environment. Never print, log or commit it. The tools use the Gemini REST API with the Python standard library only.
- Budget: the user sets a total for each subject (default $25 for the whole subject: transcription, plan and notes) and a separate budget for verification (default $10). `write_notes.py --budget` enforces it. Stop and ask before going over, and before any single run that would cost more than the user has allowed. Costs are logged in `.gemini-work/costs.jsonl` (git-ignored); prices live in `tools/gemini_pricing.json` and must be checked against Google's price page.
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

- **Image generation is paused until further notice** (this applies to every subject, including those written with Gemini). Do not call any image API and do not spend money on images. Only write detailed `[IMAGE: ...]` placeholders in the notes, so the images can be generated later with the `tools/` pipeline.
- Images are generated with OpenAI (no longer Gemini). The OpenAI API key is in the `OPENAI_API_KEY` environment variable. Never print, log or commit it.
- Use OpenAI's current image model (currently `gpt-image-2`; check the available models first), size 1024x1024, quality "medium".
- Style for every image: clean, flat educational illustration, white background, consistent soft colour palette, like a modern textbook. Not photorealistic.
- Generate every image WITH NO TEXT OR LABELS. Then:
  1. Look at the image.
  2. Add the labels with a Python script (Pillow): clear text and thin leader lines pointing to the right parts.
  3. Look at the labelled image again and check every label points to the right part. Fix any that don't.
- Save final images in `subjects/<subject>/images/` and replace each `[IMAGE: ...]` placeholder in the notes with the real image (keep a descriptive alt text).
- Budget: stay under $5 total per batch. Work out the real cost of each call from the token usage the API returns, keep a running total, and stop and ask before going over.
- Use the scripts in `tools/` (see `tools/README.md`) and save each topic's prompts and label specs under `tools/specs/<subject>/`.
- Allowed Python packages: Pillow and the OpenAI package (`openai`). Ask before adding any other dependency.
