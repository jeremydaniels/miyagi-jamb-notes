#!/usr/bin/env python3
"""Write the notes for every file in an approved subjects/<subject>/PLAN.md with Gemini.

    python tools/write_notes.py mathematics                 # whole subject (resumes where it stopped)
    python tools/write_notes.py mathematics --only C3-loci.md B3-inequalities.md
    python tools/write_notes.py mathematics --workers 3 --budget 25
    python tools/write_notes.py mathematics --status        # done / flagged / pending
    python tools/write_notes.py mathematics --dry-run       # prompt size and cost estimate, no API call
    python tools/write_notes.py --cost                      # tokens and USD per file and subject

For each topic it sends Gemini: the notes rules from CLAUDE.md, that topic's exact
syllabus text, one finished Biology file as the style example, and any subject rules
from tools/rules/<subject>.md. A file is saved only after it passes tools/notes_checks.py.
A failing file is re-asked with the problems listed (up to --retries, default 2), then
flagged: the attempt is kept in .gemini-work/flagged/<subject>/ and nothing is written
to subjects/. A file that already exists in subjects/<subject>/ is skipped, so an
interrupted run continues where it stopped. The tool never touches git.
"""
import argparse
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gemini_common as g
import notes_checks as nc
import syllabus_utils as su

SYSTEM = """You are an expert JAMB UTME {title} teacher and textbook author. You write detailed study notes for Miyagi Labs, read by Nigerian secondary school students in an app. Accuracy matters most.

Write ONE complete Markdown file for the topic you are given. Output ONLY the file: no preface, no closing remarks, no code fence around it.

======== NOTES RULES (from the project's CLAUDE.md; obey every one) ========
{claude_rules}

======== FILE FORMAT (checked automatically; a file that breaks these is rejected) ========
1. First line: `# JAMB {title} Notes: <Topic title>`.
2. Then `## What JAMB expects`: say which section and topic of the syllabus this file covers, list the content items it covers, then "By the end of these notes, you should be able to:" with a numbered list of the objectives in the syllabus wording. If the syllabus wording has a typing error or is odd (see the transcription notes you are given), say so in a short "Note on the syllabus wording" paragraph, as in the style example. If this file is one part of a split topic, say which part and point to the other parts by file name.
3. EVERY objective this file covers gets its own clearly headed section (`##` or `###`) that fully explains it, and every content item and named example gets its own heading or a clearly explained section. Use comparison tables wherever the syllabus says compare, differentiate or contrast. Explain processes step by step.
4. Put each `[IMAGE: ...]` placeholder on its own line, in one line, starting with `[IMAGE:` and ending with `]`, with a detailed description (what to show, exact values, labels, style: clean flat textbook illustration, white background). Never write real images (`![...]`).
5. The file ends with exactly these four `##` sections, in this order, and nothing else after them except the coverage block below:
   `## Key terms` (a Markdown table with columns Term | Meaning)
   `## Exam tips and common mistakes` (bullet list)
   `## Quick summary` (5 to 8 numbered points)
   `## Practice questions` (exactly 10). Each question: a bold line `**1. Question text**`, a blank line, four options as a bullet list `- A. ...` to `- D. ...`, a blank line, then `**Answer: B.** explanation`. See the style example.
6. After the practice questions, add this block (the tool removes it before saving). One line for EACH objective and EACH content item id in "THIS FILE COVERS", giving the exact text of the heading in your file where it is explained:
<!-- COVERAGE
obj i | Exact heading text
obj ii | Exact heading text
item a | Exact heading text
-->
   Use the ids exactly as given. Two objectives must not share one heading.
7. Write the whole topic. Big topics are long and that is fine; never shorten or skim. Do not repeat material that another file in the plan covers; link to it by file name instead.
8. The style example is a finished file from another subject. Copy its voice, depth, headings style and layout, NOT its content. In it, diagrams may appear as placeholders; you write placeholders too.

{subject_rules}
"""

USER_EXAMPLE = """STYLE EXAMPLE (a finished file; copy style, depth and structure only)
<<<EXAMPLE
{example}
EXAMPLE>>>
"""

USER_TOPIC = """NOW WRITE THIS FILE

File name: {file}
Title: {title}
Section: {section}

THIS FILE COVERS
- Scope: {scope}
- Content item ids: {contents}
- Objective ids: {objectives}
{split}
Target length: about {est_words} words or more. Write as much as the topic needs.

OTHER FILES IN THIS SUBJECT (for cross-references; do not duplicate their content):
{siblings}

EXACT SYLLABUS TEXT FOR THIS TOPIC (source of truth; the topic may be split over several files, cover only the ids listed above):
<<<SYLLABUS
{syllabus_block}
SYLLABUS>>>

TRANSCRIPTION NOTES (known typing errors and oddities in the syllabus):
<<<NOTES
{transcription_notes}
NOTES>>>
"""

USER_RETRY = """Your previous attempt was rejected by the automatic checks. Problems found:
{problems}

Here is your previous attempt:
<<<PREVIOUS
{previous}
PREVIOUS>>>

Return the corrected COMPLETE file (the whole file again, not a patch), fixing every problem above and keeping everything that was already right. Keep the same length or longer."""

_stop = threading.Event()


def claude_rules():
    t = (g.ROOT / "CLAUDE.md").read_text()
    a = t.index("## Content rules")
    b = t.index("## Image rules")
    return t[a:b].strip()


def subject_rules(subject):
    p = g.ROOT / "tools" / "rules" / f"{subject}.md"
    if not p.exists():
        return "", False, False
    t = p.read_text()
    first = t.splitlines()[0]
    required = "<!-- code-execution -->" in first          # tool must be used; maths-style checks on
    optional = "<!-- code-execution:optional -->" in first  # tool on, but a file may have nothing to calculate
    body = t.replace("<!-- code-execution -->", "").replace("<!-- code-execution:optional -->", "").strip()
    return "======== SUBJECT-SPECIFIC RULES ========\n" + body, (required or optional), required


def transcription_notes(syllabus):
    m = re.search(r"(?ms)^## Transcription notes\s*$(.*)", syllabus)
    return m.group(1).strip() if m else "(none)"


def est_call_cost(subject):
    rows = [r["cost_usd"] for r in g.read_costs(subject) if r["task"].startswith("notes")]
    return max(0.75, 1.5 * (sum(rows) / len(rows))) if rows else 1.5


def status_of(subject, entry, outdir, wdir):
    if (outdir / entry["file"]).exists():
        return "done"
    if (wdir / "flagged" / subject / entry["file"]).exists():
        return "flagged"
    return "pending"


def process(subject, title, entry, ctx, args):
    f = entry["file"]
    outdir, wdir = ctx["outdir"], ctx["wdir"]
    sec, block = su.find_topic(ctx["syllabus"], entry["topic_heading"])
    if block is None:
        print(f"[{f}] topic heading not found in syllabus.md: {entry['topic_heading']!r}", flush=True)
        return "error"
    sib = "\n".join(f"- `{e['file']}`: {e.get('title','')}" for e in ctx["plan"] if e["file"] != f)
    split = f"- Split topic: {entry['split']}\n" if entry.get("split") else ""
    user = [{"text": USER_EXAMPLE.format(example=ctx["example"])},
            {"text": USER_TOPIC.format(
                file=f, title=entry.get("title", ""), section=entry.get("section", sec), scope=entry.get("scope", ""),
                contents=", ".join(entry["contents"]) or "(none)", objectives=", ".join(entry["objectives"]) or "(none)",
                split=split, est_words=entry.get("est_words", 6000), siblings=sib,
                syllabus_block=block, transcription_notes=ctx["notes"])}]
    system = SYSTEM.format(title=title, claude_rules=ctx["rules"], subject_rules=ctx["srules"])
    problems, prev, last_text = [], None, ""
    for attempt in range(args.retries + 1):
        if _stop.is_set():
            return "stopped"
        with ctx["lock"]:
            spent = g.subject_spend(subject)
            if spent + est_call_cost(subject) > args.budget:
                _stop.set()
                print(f"BUDGET: spent ${spent:.2f}, next call could exceed ${args.budget:.2f}. Stopping. "
                      f"Ask before raising --budget.", flush=True)
                return "stopped"
        parts = list(user)
        if prev is not None:
            parts.append({"text": USER_RETRY.format(problems="\n".join(f"- {p}" for p in problems), previous=prev)})
        print(f"[{f}] attempt {attempt + 1} ...", flush=True)
        try:
            r = g.call_gemini(parts, system=system, model=args.model, code_execution=ctx["code"],
                              subject=subject, file=f, task=f"notes{'' if attempt == 0 else '-retry%d' % attempt}")
        except Exception as e:
            print(f"[{f}] API error: {g.scrub(str(e))[:300]}", flush=True)
            return "error"
        text = r["text"]
        i = text.find("# JAMB ")
        if i > 0:
            text = text[i:]
        text = g.strip_fence(text)
        last_text = text
        clean, problems = nc.check_notes(text, entry, math=ctx["code_required"], code_runs=r["code_runs"])
        if r["finish"] != "STOP":
            problems.insert(0, f"output stopped early ({r['finish']}); the file is truncated or too long. Be complete but efficient.")
        words = len(clean.split())
        print(f"[{f}] {words} words, ${r['cost']:.2f}, code runs {r['code_runs']}, "
              f"{'OK' if not problems else str(len(problems)) + ' problem(s)'}", flush=True)
        if not problems:
            outdir.mkdir(parents=True, exist_ok=True)
            tmp = outdir / (f + ".tmp")
            tmp.write_text(clean)
            tmp.replace(outdir / f)
            return "done"
        prev = text
    fdir = wdir / "flagged" / subject
    fdir.mkdir(parents=True, exist_ok=True)
    (fdir / f).write_text(last_text)
    (fdir / (f + ".problems.json")).write_text(json.dumps(problems, indent=1))
    print(f"[{f}] FLAGGED after {args.retries + 1} attempts:", flush=True)
    for p in problems[:8]:
        print(f"     - {p}", flush=True)
    return "flagged"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subject", nargs="?")
    ap.add_argument("--only", nargs="+", metavar="FILE", help="only these plan files")
    ap.add_argument("--limit", type=int, help="stop after this many files")
    ap.add_argument("--model", default=g.default_model())
    ap.add_argument("--budget", type=float, default=25.0,
                    help="stop before total spend on this subject (all tasks) would pass this many USD (default 25)")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--workers", type=int, default=1, help="files written in parallel (default 1)")
    ap.add_argument("--example", default="subjects/biology/D3-biotechnology.md", help="style example file")
    ap.add_argument("--plan", help="PLAN.md path (default subjects/<subject>/PLAN.md)")
    ap.add_argument("--out-dir", help="write here instead of subjects/<subject>/ (for tests)")
    ap.add_argument("--retry-flagged", action="store_true", help="try flagged files again")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cost", action="store_true", help="print the cost log and exit")
    a = ap.parse_args()

    if a.cost:
        g.print_costs(a.subject)
        return
    if not a.subject:
        ap.error("subject is required")
    subject = a.subject
    sdir = g.ROOT / "subjects" / subject
    title = g.subject_title(subject)
    plan_path = Path(a.plan) if a.plan else sdir / "PLAN.md"
    plan = su.parse_plan(plan_path.read_text())
    syllabus = (sdir / "syllabus.md").read_text()
    outdir = Path(a.out_dir) if a.out_dir else sdir
    ctx = {"plan": plan, "syllabus": syllabus, "notes": transcription_notes(syllabus), "outdir": outdir,
           "wdir": g.WORK, "lock": threading.Lock(), "rules": claude_rules(),
           "example": (g.ROOT / a.example).read_text()}
    ctx["srules"], ctx["code"], ctx["code_required"] = subject_rules(subject)

    probs = su.check_plan(plan, syllabus)
    if probs:
        sys.exit("PLAN.md does not match syllabus.md:\n - " + "\n - ".join(probs))
    warns = su.check_plan_items(plan, syllabus)
    if warns:
        print(f"Note: {len(warns)} numbering warning(s) in PLAN.md (not fatal), e.g. {warns[0]}")
    todo = [e for e in plan if (not a.only or e["file"] in a.only)]
    if a.only:
        missing = set(a.only) - {e["file"] for e in plan}
        if missing:
            sys.exit(f"Not in PLAN.md: {sorted(missing)}")

    if a.status:
        for e in plan:
            s = status_of(subject, e, outdir, g.WORK)
            w = len((outdir / e["file"]).read_text().split()) if s == "done" else ""
            print(f"{s:<8}{e['file']:<62}{w}")
        print(f"spent so far on {subject}: ${g.subject_spend(subject):.2f}")
        return

    pending = [e for e in todo if status_of(subject, e, outdir, g.WORK) == "pending"
               or (a.retry_flagged and status_of(subject, e, outdir, g.WORK) == "flagged")]
    if a.limit:
        pending = pending[:a.limit]
    in_tokens = len((ctx["example"] + ctx["rules"] + ctx["srules"] + syllabus).split()) * 1.5
    print(f"{len(pending)} file(s) to write, {len(todo) - len(pending)} already done or flagged. "
          f"Model {a.model}; code execution {('required' if ctx['code_required'] else 'optional') if ctx['code'] else 'off'}.")
    print(f"Spent so far on {subject}: ${g.subject_spend(subject):.2f} of ${a.budget:.2f} budget.")
    if a.dry_run:
        words = sum(e.get("est_words", 6000) for e in pending)
        print(f"Dry run. About {in_tokens:,.0f} input tokens per call. Planned output {words:,} words "
              f"(about {int(words * 1.8):,} tokens plus thinking). No API call made.")
        return
    if not pending:
        return

    results = {}
    def run(e):
        results[e["file"]] = process(subject, title, e, ctx, a)
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        list(ex.map(run, pending))
    done = [k for k, v in results.items() if v == "done"]
    flagged = [k for k, v in results.items() if v == "flagged"]
    other = {k: v for k, v in results.items() if v not in ("done", "flagged")}
    print(f"\nFinished: {len(done)} written, {len(flagged)} flagged, {len(other)} not completed {sorted(set(other.values())) if other else ''}.")
    print(f"Total spent on {subject}: ${g.subject_spend(subject):.2f}")
    if flagged:
        print("Flagged:", ", ".join(flagged), f"(see {g.WORK}/flagged/{subject}/)")


if __name__ == "__main__":
    main()
