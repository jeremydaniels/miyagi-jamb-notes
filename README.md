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
| [Chemistry](subjects/chemistry/syllabus.md) | 23 topic files | Placeholders only. |
| [Physics](subjects/physics/syllabus.md) | 48 topic files | Placeholders only. |
| [Mathematics](subjects/mathematics/syllabus.md) | 23 topic files | Placeholders only. |
| [Economics](subjects/economics/syllabus.md) | 23 topic files | Placeholders only. |
| [Government](subjects/government/syllabus.md) | 33 topic files | Placeholders only. |
| [Literature in English](subjects/literature-in-english/syllabus.md) | 19 topic files (set-text guides are partly marked placeholders) | Placeholders only. |
| [CRK](subjects/crk/syllabus.md) | 52 topic files | Placeholders only. |
| [IRK](subjects/irk/syllabus.md) | 27 topic files | Placeholders only. |
| [Accounting (Principles of Accounts)](subjects/accounting/syllabus.md) | 18 topic files | Placeholders only. |
| [Commerce](subjects/commerce/syllabus.md) | 18 topic files | Placeholders only. |
| [Geography](subjects/geography/syllabus.md) | 24 topic files covering Parts I to IV | Placeholders only. |
| [Agricultural Science](subjects/agricultural-science/syllabus.md) | 45 topic files covering Sections A to E | Placeholders only. |
| [History](subjects/history/syllabus.md) | 42 topic files covering Sections A to G | Placeholders only. |
| [Computer Studies](subjects/computer-studies/syllabus.md) | 42 topic files covering Sections A to I (verified) | 78 of 86 placeholders have images; 8 still carry `[IMAGE: ...]` placeholders. Gallery: `subjects/computer-studies/images/GALLERY-computer-studies.md`. |

History facts that could not be confirmed are listed in `HISTORY-VERIFICATION-LOG.md`.

In Use of English, `A5-approved-reading-text.md` has the novel sections left as marked placeholders, to be filled in by someone who has read the book. The recommended text must be confirmed with JAMB each exam year.

## Image tools

Images are made with Gemini (`GEMINI_API_KEY`) and Pillow; code-drawn diagrams use **matplotlib** (added with approval; `pip install matplotlib`). See `tools/README.md`, `IMAGES-PLAN.md` and `PILOT-GALLERY.md`.
