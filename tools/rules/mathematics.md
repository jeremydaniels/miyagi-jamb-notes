<!-- code-execution -->
## Mathematics-specific rules (these override the style example wherever they differ)

CORRECTNESS IS CRITICAL
- You MUST call the code execution tool BEFORE writing the notes: first draft the worked examples and the 10 practice questions with their options in your head, then run ONE Python script (or a few) that recomputes every example and every answer and checks each distractor. A file written without a code-tool call is rejected. Use the code execution tool to verify EVERY calculation, worked example and practice answer BEFORE you write it into the notes (use Python, `fractions`, `decimal` and `sympy` if available). Check each practice question's four options: confirm the stated answer is correct and that each wrong option really differs from it. Never state an unverified answer. Run the checks silently; do not mention the tool or paste code in the notes.
- If a textbook convention varies (for example the definition of a term, rounding rules, notation, order of angles for bearings), say so in the text.
- All working must be doable by hand, with no calculator. Choose numbers that work out neatly or leave answers in surd, fraction or $\pi$ form. Where JAMB normally gives a table (logarithm, trigonometric ratios, square roots) say that the table is supplied in the exam and show how it is used.

FORMAT OF MATHEMATICS
- Write all mathematics in Markdown/LaTeX: `$...$` inline and `$$...$$` on its own lines for display equations. Explain every symbol the first time a formula appears (a short "where ..." list).
- Never use a bare dollar sign for money: write naira as ₦ (for example ₦5,000).
- Do not use `$` for anything but maths. Keep each `$...$` on one line.
- Use plain text, not LaTeX, in headings.

HOW TO TEACH
- Show full working for every worked example, step by step, and say WHY each step is done. Number the steps. Give at least 3 worked examples per objective, from easy to JAMB level, using Nigerian contexts where they help (naira, markets, Lagos/Abuja distances, farms, school and sports data).
- Teach the standard method first. Then give any JAMB shortcut and say clearly when the shortcut is safe and when it is not.
- Add a "Common mistakes" note inside each major section (sign errors, order of operations, units, wrong formula, forgetting to check the answer) with the wrong working and the corrected version.
- Where the syllabus says "simple cases only" or sets limits (for example "not exceeding degree 3", "not more than 3 sets", "2 x 2 inverses"), stay inside those limits and say so.
- Where a diagram, graph, number line, Venn diagram or construction helps, add an `[IMAGE: ...]` placeholder with a detailed description including the exact values, labels and shape, so it can be drawn accurately later.

PRACTICE QUESTIONS (exactly 10)
- Real JAMB style: short multiple-choice questions of the kind found in past UTME papers, with a mix of easy, medium and harder items covering all objectives of the file.
- The wrong options must be plausible, each based on a typical mistake (sign error, forgetting a step, wrong formula, rounding). Make sure only one option is correct.
- After "**Answer: X.**" (on the same line) show full working as a NUMBERED LIST (`1. ...`, `2. ...`, each step on its own line starting a list item, with a blank line before the list), with `$...$` maths, not just the letter, and name the mistake behind the most tempting wrong option.
- In worked examples too, write steps as a numbered list (or separate paragraphs). Never put several steps on consecutive plain lines, because Markdown joins them into one paragraph.
