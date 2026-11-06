# CLAUDE.md

## Project

Detailed JAMB UTME study notes for Miyagi Labs, written from the official JAMB syllabus. Students read them in the Miyagi Labs app.

- Official syllabi live in `syllabi/` (e.g. `syllabi/biology-syllabus.md`). They are the source of truth for what must be covered.
- The style and depth reference is `samples/sample-living-organisms.md`. Match it.

## Workflow

- Always show a plan and wait for approval before writing any content.
- Commit to `main` after each topic is finished (one commit per topic file).
- Before committing a topic, check it against the syllabus (see "Coverage check" below).

## File structure

- Each subject gets its own folder: `biology/`, `chemistry/`, `physics/`, etc.
- One Markdown file per syllabus topic, numbered in syllabus order (e.g. `biology/A1-living-organisms.md`, `biology/A2-...md`).

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
