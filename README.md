# Miyagi JAMB Notes

Detailed JAMB UTME study notes for Miyagi Labs, written from the official JAMB syllabus. Students read them in the Miyagi Labs app. The working rules are in `CLAUDE.md`.

## Folder layout

```
subjects/
  <subject>/
    syllabus.md        official syllabus, typed exactly as written, with "Transcription notes"
    <topic>.md         one notes file per syllabus topic, in syllabus order (A1, A2a, A2b, B1 ...)
    images/            diagrams used by the notes (only where images have been generated)
samples/               style and depth reference for the notes
tools/                 scripts for generating and labelling images (see tools/README.md)
  specs/<subject>/     image prompts and label specs for each subject
release/               exported ZIP packages of finished notes
```

New subjects go in `subjects/<subject>/`, with `syllabus.md` inside.

## Subjects done so far

| Subject | Notes | Images |
| --- | --- | --- |
| [Biology](subjects/biology/syllabus.md) | 42 topic files covering Sections A to E | Section A has images. Sections B to E have `[IMAGE: ...]` placeholders only. |
| [Use of English](subjects/use-of-english/syllabus.md) | 30 topic files covering Sections A to C | Placeholders only. |

In Use of English, `A5-approved-reading-text.md` has the novel sections left as marked placeholders, to be filled in by someone who has read the book. The recommended text must be confirmed with JAMB each exam year.
