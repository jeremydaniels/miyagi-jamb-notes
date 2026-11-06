# CLAUDE.md

## Project

Detailed JAMB UTME study notes for Miyagi Labs, written from the official JAMB syllabus. Students read them in the Miyagi Labs app.

- Official syllabi live in `syllabi/` (e.g. `syllabi/biology-syllabus.md`, and `syllabi/biology-section-a.md` for Section A only). They are the source of truth for what must be covered. Syllabus files are typed exactly as written, mistakes included; errors are explained in a "Transcription notes" section, never silently corrected.
- The style and depth reference is `samples/sample-living-organisms.md`. Match it.

## Workflow

- Always show a plan and wait for approval before writing any content.
- Always work on `main`. No other branches. Commit and push to `main` after every task (one commit per topic file, and one commit per topic's images).
- Write all the notes for a batch first, then generate images topic by topic in the same order. Every finished topic must look complete on its own.
- Before committing a topic, check it against the syllabus (see "Coverage check" below).

## File structure

- Each subject gets its own folder: `biology/`, `chemistry/`, `physics/`, etc.
- One Markdown file per syllabus topic, numbered in syllabus order (e.g. `biology/A1-living-organisms.md`, `biology/A2-...md`). A topic too big for one file is split with letter suffixes (e.g. `A2a-`, `A2b-`, `A2c-`).
- Images live in `biology/images/` with clear names prefixed by the topic file (e.g. `A1-plant-cell.png`).

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

- The Gemini API key is in the `GEMINI_API_KEY` environment variable. Never print, log or commit it.
- Use the cheapest current Gemini image model that gives clean, accurate illustrations. Check the available models first.
- Style for every image: clean, flat educational illustration, white background, consistent soft colour palette, like a modern textbook. Not photorealistic.
- Generate every image WITH NO TEXT OR LABELS. Then:
  1. Look at the image.
  2. Add the labels with a Python script (Pillow): clear text and thin leader lines pointing to the right parts.
  3. Look at the labelled image again and check every label points to the right part. Fix any that don't.
- Save final images in `biology/images/` and replace each `[IMAGE: ...]` placeholder in the notes with the real image (keep a descriptive alt text).
- Budget: stay under $5 total per batch. Track the running cost, and stop and ask before going over.
- Allowed Python packages: Pillow and the Google GenAI package (`google-genai`). Ask before adding any other dependency.
