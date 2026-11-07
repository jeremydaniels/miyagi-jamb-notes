#!/usr/bin/env python3
"""Write the notes for every file in an approved subjects/<subject>/PLAN.md with Gemini.

    python tools/write_notes.py mathematics                 # whole subject (resumes where it stopped)
    python tools/write_notes.py mathematics --only C3-loci.md B3-inequalities.md
    python tools/write_notes.py mathematics --mode sync --workers 3   # immediate (full price) instead of Batch
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
    required = "<!-- code-execution -->" in first          # tool on; maths-style checks on
    optional = "<!-- code-execution:optional -->" in first  # tool on, but a file may have nothing to calculate
    body = t.replace("<!-- code-execution -->", "").replace("<!-- code-execution:optional -->", "").strip()
    return "======== SUBJECT-SPECIFIC RULES ========\n" + body, (required or optional), required


def transcription_notes(syllabus):
    m = re.search(r"(?ms)^## Transcription notes\s*$(.*)", syllabus)
    return m.group(1).strip() if m else "(none)"


def status_of(subject, entry, outdir, wdir):
    if (outdir / entry["file"]).exists():
        return "done"
    if (wdir / "flagged" / subject / entry["file"]).exists():
        return "flagged"
    return "pending"


COVERAGE_REPAIR = """Below are the headings of a finished notes file and a list of syllabus ids it must cover. For each id, choose the ONE heading (copied exactly from the list) under which that objective or content item is explained. Reply with one line per id in exactly this format and nothing else:
obj <id> | <heading text>
item <id> | <heading text>
Use "obj" for objectives and "item" for content items. Two objectives must not share one heading unless the file really explains them together.

IDS TO MAP:
{ids}

SYLLABUS TEXT:
{syllabus}

HEADINGS IN THE FILE:
{headings}
"""


def build_parts(entry, ctx, prev=None):
    sec, block = su.find_topic(ctx["syllabus"], entry["topic_heading"])
    sib = "\n".join(f"- `{e['file']}`: {e.get('title','')}" for e in ctx["plan"] if e["file"] != entry["file"])
    split = f"- Split topic: {entry['split']}\n" if entry.get("split") else ""
    parts = [{"text": USER_EXAMPLE.format(example=ctx["example"])},
             {"text": USER_TOPIC.format(
                 file=entry["file"], title=entry.get("title", ""), section=entry.get("section", sec),
                 scope=entry.get("scope", ""), contents=", ".join(entry["contents"]) or "(none)",
                 objectives=", ".join(entry["objectives"]) or "(none)", split=split,
                 est_words=entry.get("est_words", 6000), siblings=sib, syllabus_block=block,
                 transcription_notes=ctx["notes"])}]
    if prev:
        parts.append({"text": USER_RETRY.format(problems="\n".join(f"- {p}" for p in prev["problems"]),
                                                previous=prev["text"])})
    return parts


def make_body(entry, ctx, args, prev=None):
    system = SYSTEM.format(title=ctx["title"], claude_rules=ctx["rules"], subject_rules=ctx["srules"])
    return g.build_body(build_parts(entry, ctx, prev), system=system, code_execution=ctx["code"],
                        thinking=args.thinking)


def repair_coverage(subject, entry, text, ctx, args):
    """Cheap fix for coverage-map-only failures: ask a Flash model to map ids to the file's headings."""
    clean, cov = nc.split_coverage(text)
    heads = [t for lvl, t in nc.headings(clean) if lvl in (2, 3, 4)]
    ids = [f"obj {x}" for x in entry.get("objectives", [])] + [f"item {x}" for x in entry.get("contents", [])]
    _, block = su.find_topic(ctx["syllabus"], entry["topic_heading"])
    try:
        r = g.call_gemini([{"text": COVERAGE_REPAIR.format(ids="\n".join(ids), syllabus=block,
                                                             headings="\n".join(heads))}],
                          model=g.load_pricing().get("flash_model"), thinking="low", subject=subject,
                          file=entry["file"], task="coverage-repair")
    except Exception:
        return None
    block_txt = "<!-- COVERAGE\n" + r["text"].strip().strip("`") + "\n-->"
    return clean.rstrip() + "\n\n" + block_txt + "\n"


def evaluate(subject, entry, raw, finish, code_runs, ctx, args):
    """-> (clean_text | None, problems, warnings). Tries a cheap coverage repair before asking for a rewrite."""
    text = raw
    i = text.find("# JAMB ")
    if i > 0:
        text = text[i:]
    text = g.strip_fence(text)
    clean, problems = nc.check_notes(text, entry, math=ctx["code_required"], code_runs=None)
    warnings = []
    if ctx["code_required"] and code_runs == 0:
        warnings.append("no code execution run (the independent verifier will recompute the numbers)")
    if finish != "STOP":
        problems.insert(0, f"output stopped early ({finish}); the file is truncated or too long. Be complete but efficient.")
    if problems and all(p.startswith("COVERAGE map") for p in problems):
        fixed = repair_coverage(subject, entry, text, ctx, args)
        if fixed:
            clean2, problems2 = nc.check_notes(fixed, entry, math=ctx["code_required"], code_runs=None)
            if not problems2:
                return clean2, [], warnings + ["coverage map repaired by a cheap Flash call"]
    return text, problems, warnings


def save_ok(entry, clean, ctx):
    ctx["outdir"].mkdir(parents=True, exist_ok=True)
    tmp = ctx["outdir"] / (entry["file"] + ".tmp")
    tmp.write_text(clean)
    tmp.replace(ctx["outdir"] / entry["file"])


def save_flagged(subject, entry, text, problems):
    fdir = g.WORK / "flagged" / subject
    fdir.mkdir(parents=True, exist_ok=True)
    (fdir / entry["file"]).write_text(text)
    (fdir / (entry["file"] + ".problems.json")).write_text(json.dumps(problems, indent=1))


def run_sync(subject, pending, ctx, args):
    results = {}
    def one(entry):
        f = entry["file"]
        prev = None
        for attempt in range(args.retries + 1):
            if _stop.is_set():
                results[f] = "stopped"; return
            with ctx["lock"]:
                try:
                    g.check_safety(subject, 1.5)
                except SystemExit as e:
                    _stop.set(); print(e, flush=True); results[f] = "stopped"; return
            print(f"[{f}] attempt {attempt + 1} ...", flush=True)
            try:
                r = g.call_gemini(build_parts(entry, ctx, prev), system=SYSTEM.format(title=ctx["title"], claude_rules=ctx["rules"], subject_rules=ctx["srules"]),
                                  model=args.model, code_execution=ctx["code"], thinking=args.thinking, subject=subject, file=f,
                                  task="notes" if attempt == 0 else f"notes-retry{attempt}")
            except Exception as e:
                print(f"[{f}] API error: {g.scrub(str(e))[:300]}", flush=True); results[f] = "error"; return
            text, problems, warns = evaluate(subject, entry, r["text"], r["finish"], r["code_runs"], ctx, args)
            print(f"[{f}] {len(text.split())} words, ${r['cost']:.2f}, code runs {r['code_runs']}, "
                  f"{'OK' if not problems else str(len(problems)) + ' problem(s)'}", flush=True)
            if not problems:
                save_ok(entry, text, ctx); results[f] = "done"; return
            prev = {"text": text, "problems": problems}
        save_flagged(subject, entry, prev["text"], prev["problems"]); results[f] = "flagged"
        print(f"[{f}] FLAGGED: {prev['problems'][:3]}", flush=True)
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        list(ex.map(one, pending))
    return results


def run_batch(subject, pending, ctx, args):
    by_file = {e["file"]: e for e in pending}
    last = {}
    def mk(key, attempt, prev):
        return make_body(by_file[key], ctx, args, prev)
    def handle(key, result, error, attempt):
        entry = by_file[key]
        if result is None:
            print(f"[{key}] request error: {(error or {}).get('message','?')[:200]}", flush=True)
            return "retry", last.get(key)
        text, problems, warns = evaluate(subject, entry, result["text"], result["finish"], result["code_runs"], ctx, args)
        print(f"[{key}] {len(text.split())} words, ${result['cost']:.2f} (list), code runs {result['code_runs']}, "
              f"{'OK' if not problems else str(len(problems)) + ' problem(s)'}", flush=True)
        if not problems:
            save_ok(entry, text, ctx)
            return "done", None
        last[key] = {"text": text, "problems": problems}
        if attempt >= args.retries:
            save_flagged(subject, entry, text, problems)
            print(f"[{key}] FLAGGED: {problems[:3]}", flush=True)
            return "fail", None
        return "retry", last[key]
    return g.run_batch_rounds(subject, "notes", list(by_file), mk, handle, args.retries, args.model, poll=args.poll)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subject", nargs="?")
    ap.add_argument("--only", nargs="+", metavar="FILE", help="only these plan files")
    ap.add_argument("--limit", type=int, help="stop after this many files")
    ap.add_argument("--model", default=g.default_model())
    ap.add_argument("--mode", choices=["batch", "sync"], default="batch",
                    help="batch = Batch API (about half price, slower, default); sync = immediate calls at full price")
    ap.add_argument("--thinking", choices=["low", "medium", "high"], default=None,
                    help="Gemini thinking level (default: the model default)")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--workers", type=int, default=3, help="files written in parallel in sync mode (default 3)")
    ap.add_argument("--poll", type=int, default=60, help="seconds between Batch status checks")
    ap.add_argument("--example", default="subjects/biology/D3-biotechnology.md", help="style example file")
    ap.add_argument("--plan", help="PLAN.md path (default subjects/<subject>/PLAN.md)")
    ap.add_argument("--out-dir", help="write here instead of subjects/<subject>/ (for tests)")
    ap.add_argument("--retry-flagged", action="store_true", help="try flagged files again")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cost", action="store_true", help="print the cost report and exit")
    a = ap.parse_args()

    if a.cost:
        if a.subject:
            g.cost_report(a.subject)
        else:
            g.print_costs()
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
           "wdir": g.WORK, "lock": threading.Lock(), "rules": claude_rules(), "title": title,
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
        print(f"spent so far on {subject}: ${g.subject_spend(subject):.2f} (list price)")
        return

    pending = [e for e in todo if status_of(subject, e, outdir, g.WORK) == "pending"
               or (a.retry_flagged and status_of(subject, e, outdir, g.WORK) == "flagged")]
    if a.limit:
        pending = pending[:a.limit]
    in_tokens = len((ctx["example"] + ctx["rules"] + ctx["srules"] + syllabus).split()) * 1.5
    print(f"{len(pending)} file(s) to write, {len(todo) - len(pending)} already done or flagged. "
          f"Model {a.model}; mode {a.mode}; thinking {a.thinking or 'default'}; "
          f"code execution {('required' if ctx['code_required'] else 'optional') if ctx['code'] else 'off'}.")
    print(f"Spent so far on {subject}: ${g.subject_spend(subject):.2f} (list price). Safety limit ${g.safety_limit():.0f} per subject.")
    if a.dry_run:
        words = sum(e.get("est_words", 6000) for e in pending)
        print(f"Dry run. About {in_tokens:,.0f} input tokens per call. Planned output {words:,} words. No API call made.")
        return
    if not pending:
        return

    results = run_batch(subject, pending, ctx, a) if a.mode == "batch" else run_sync(subject, pending, ctx, a)
    done = [k for k, v in results.items() if v == "done"]
    flagged = [k for k, v in results.items() if v in ("flagged", "fail")]
    other = {k: v for k, v in results.items() if v not in ("done", "flagged", "fail")}
    print(f"\nFinished: {len(done)} written, {len(flagged)} flagged, {len(other)} not completed {sorted(set(other.values())) if other else ''}.")
    if flagged:
        print("Flagged:", ", ".join(flagged), f"(see {g.WORK}/flagged/{subject}/)")
    g.cost_report(subject)


if __name__ == "__main__":
    main()
