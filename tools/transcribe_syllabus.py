#!/usr/bin/env python3
"""Transcribe a subject's official syllabus PDF (inbox/<subject>.pdf) into
subjects/<subject>/syllabus.md using Gemini.

    python tools/transcribe_syllabus.py mathematics
    python tools/transcribe_syllabus.py chemistry --title Chemistry --force

The text is copied exactly (mistakes included). Errors, oddities and anything
that looks unofficial or out of date go in a "Transcription notes" section at
the end. Nothing is summarised or skipped.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gemini_common as g

PROMPT = """You are transcribing a JAMB UTME {title} syllabus PDF into Markdown. Your job is an EXACT text copy, not a summary.

RULES
1. Copy every word, number, symbol, list marker and item in the original, in the original order, including spelling, grammar and punctuation mistakes. NEVER correct, reword, merge, reorder or skip anything. If a page has a header, footer, exam structure, recommended texts or any other section, include it too.
2. Where the PDF lays out contents and objectives side by side in columns (or in a table), put each topic's contents first, then its objectives (keep the original wording and numbering of both). Keep tables as tables if the content is genuinely tabular.
3. Mathematics and science notation: write it as Markdown maths ($...$ inline) when the original uses symbols, fractions, powers, roots or Greek letters, so no information is lost. Do not change the meaning.
4. Use EXACTLY this layout so that tools can parse it:
   - `# JAMB UTME {title} Syllabus` as the title.
   - One short paragraph saying what was transcribed (the PDF file name `{pdf_name}` and page numbers if you can tell) and that wording and spelling are kept as in the original.
   - `## GENERAL OBJECTIVES` (or whatever the original calls its introductory sections: use `##` for each).
   - `## DETAILED SYLLABUS`, then one `##` heading per syllabus section (for example `## A: SECTION NAME`) exactly as printed.
   - One `###` heading per topic, exactly as numbered and titled in the original (for example `### 1. Number bases`). Under it: `**Topics / Contents / Notes**` followed by the contents as a nested bullet list with the original markers (a., i., etc.), then a line `**Candidates should be able to:**` (or the original wording) followed by the objectives, numbered as in the original.
   - Use `---` between sections.
   - Do not use `##` or `###` headings for anything else except the final notes section.
5. End with `## Transcription notes`. Start it with: "These are not part of the syllabus. They flag places where the original wording looks like a typing error or is unclear, so the notes can handle them correctly. The syllabus text above is left exactly as printed." Then a bullet list, each bullet naming the place (topic and item) and what is wrong, with the probable correct reading. Include:
   - typing, spelling, numbering, bracket and formatting errors;
   - mathematical or factual errors, ambiguous items, objectives that do not match their content, items placed under the wrong topic;
   - anything that looks UNOFFICIAL or OUT OF DATE for a JAMB UTME syllabus: for example no JAMB branding or title page, a third-party author or tool in the document, an edition year or exam years that look old, wording that does not match the JAMB syllabus style, sections that belong to other exams (WAEC, NECO), or topics you would not expect in the current JAMB UTME {title} syllabus. State only what you can see in the document or know with confidence; if you are unsure, say "unsure".
   - If you find nothing in a category, do not invent items.
6. Output ONLY the Markdown file. No commentary before or after, no code fence around it.

Before finishing, re-read the PDF page by page and confirm that every item on every page appears in your output.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subject", help="folder name, e.g. mathematics (PDF is inbox/<subject>.pdf)")
    ap.add_argument("--pdf", help="PDF path (default inbox/<subject>.pdf)")
    ap.add_argument("--title", help="subject title used in headings (default from folder name)")
    ap.add_argument("--model", default=g.default_model())
    ap.add_argument("--force", action="store_true", help="overwrite an existing syllabus.md")
    ap.add_argument("--out", help="write here instead of subjects/<subject>/syllabus.md (for tests)")
    a = ap.parse_args()

    pdf = Path(a.pdf) if a.pdf else g.ROOT / "inbox" / f"{a.subject}.pdf"
    out = Path(a.out) if a.out else g.ROOT / "subjects" / a.subject / "syllabus.md"
    if not pdf.exists():
        sys.exit(f"Missing {pdf}")
    if out.exists() and not a.force:
        sys.exit(f"{out} exists. Use --force to overwrite.")
    title = a.title or g.subject_title(a.subject)
    print(f"Transcribing {pdf.name} with {a.model} ...")
    r = g.call_gemini([g.pdf_part(pdf), {"text": "Transcribe this syllabus now."}],
                      system=PROMPT.format(title=title, pdf_name=pdf.name),
                      model=a.model, subject=a.subject, task="transcribe")
    if r["finish"] != "STOP":
        sys.exit(f"Stopped early ({r['finish']}); nothing saved.")
    text = g.strip_fence(r["text"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"Saved {out} ({len(text.split())} words). Cost ${r['cost']:.3f} "
          f"({r['usage'].get('promptTokenCount',0)} in / "
          f"{r['usage'].get('candidatesTokenCount',0)+r['usage'].get('thoughtsTokenCount',0)} out tokens)")


if __name__ == "__main__":
    main()
