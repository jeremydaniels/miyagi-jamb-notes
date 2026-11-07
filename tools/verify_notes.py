#!/usr/bin/env python3
"""Independent check of finished notes with Gemini (code execution on).

    python tools/verify_notes.py mathematics               # Batch API (about half price, slower), default
    python tools/verify_notes.py mathematics --mode sync   # immediate calls at full price
    python tools/verify_notes.py mathematics --only D1-differentiation.md --redo
    python tools/verify_notes.py mathematics --report      # print the combined report again
    python tools/verify_notes.py mathematics --status
    python tools/verify_notes.py mathematics --dry-run

For every notes file in subjects/<subject>/PLAN.md, one fresh Gemini call re-checks every
worked example, every practice answer, every explanation of a wrong option, and the
formulas and facts, recomputing anything numerical with the code execution tool.
It NEVER edits notes. It writes one JSON report per file to
.gemini-work/verify/<subject>/ and one combined VERIFY-REPORT.md there, listing
file, location, issue, evidence and a suggested fix. Claude (or a human) then confirms
each problem before fixing it: Gemini's checker can be wrong too.

There is no per-run budget. Only the safety limit in tools/gemini_pricing.json (default $100 per
subject, writing and verification together) can stop a run.
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
import syllabus_utils as su

SYSTEM = """You are an independent, sceptical checker of JAMB UTME {title} study notes written by someone else. Your only job is to find real mistakes. You do not edit or rewrite the notes.

You MUST use the code execution tool. Recompute with Python (use `fractions`, `decimal`, `itertools`, `math`, and `sympy` if it is available) rather than trusting the notes or your own mental arithmetic. A report produced without any code-tool run is rejected.

CHECK ALL OF THE FOLLOWING, one by one:
1. Every WORKED EXAMPLE: every line of working, every intermediate number, the final answer and the units.
2. Every PRACTICE QUESTION (there are 10): recompute the correct answer from the question alone, confirm it is the option the notes label as the answer, and confirm EXACTLY ONE option is correct (no second option equal to it, no question that is ambiguous or has no correct option). Check the working shown under the answer line by line.
3. EVERY EXPLANATION OF A WRONG OPTION (sentences such as "Option C comes from forgetting the sign" or "Option A is the probability of ..."). For each one, work out what that stated mistake or quantity really produces and confirm it equals the value in the option named. Report any explanation that is false or does not match the option.
4. Formulas, definitions, rules, theorems, tables, values quoted in "Exam tips", "Key terms", "Quick summary" and numbers given in the [IMAGE: ...] descriptions (coordinates, lengths, angles, labels): check they are correct and consistent with the text.
5. UNITS AND CHEMICAL/ECONOMIC CONSISTENCY: every numerical answer and every intermediate quantity must carry the correct unit, and units must be consistent through each calculation (check dimensions, prefixes and conversions such as cm to m, g to kg, minutes to seconds, dm3 to cm3). Every chemical equation must be balanced (atoms and charge) with correct formulas, charges and state symbols; molar masses, mole ratios and gas volumes must be recomputed. Economic formulas and calculations (elasticity, national income, costs and revenue, index numbers, growth rates, multipliers) must be recomputed and the signs and units (for example ₦, %, units of output) must be right. Dated facts, institutions and figures must be correct or clearly hedged.
6. Statements that contradict the syllabus limits or each other. Convention differences between textbooks are NOT errors if the notes say so.

DO NOT report style, wording preferences, length, or things that are merely optional. Report only problems you are confident about; if you are not sure, give severity "low" and say "unsure". Do not invent problems: if everything is correct, return an empty list.

OUTPUT: only one JSON object, no code fence, no text before or after:
{{"file": "<file name>",
  "checked": {{"worked_examples": <n>, "practice_questions": <n>, "distractor_explanations": <n>, "other_claims": <n>}},
  "problems": [
    {{"where": "<section / Example number / Question number>",
      "type": "wrong_answer | wrong_working | wrong_distractor_explanation | multiple_correct | ambiguous_question | formula_or_fact | image_description | inconsistency | other",
      "severity": "high | medium | low",
      "numeric": true or false,
      "issue": "<what is wrong, with the value you computed>",
      "evidence": "<the computation or fact that shows it, short>",
      "suggested_fix": "<exact replacement text or the corrected value>"}}
  ]}}
"""

USER = """FILE: {file}

SYLLABUS TOPIC THE FILE COVERS (for scope only):
<<<SYLLABUS
{syllabus}
SYLLABUS>>>

NOTES TO CHECK (the whole file):
<<<NOTES
{notes}
NOTES>>>
"""

_stop = threading.Event()
VERIFY_DIR = lambda subject: g.WORK / "verify" / subject


def verify_spend(subject):
    return sum(r["cost_usd"] for r in g.read_costs(subject) if r["task"].startswith("verify"))


def parse_json(text):
    i, j = text.find("{"), text.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("no JSON object in reply")
    return json.loads(text[i:j + 1])


def make_body(entry, notes_path, syllabus, title, args, note=""):
    _, block = su.find_topic(syllabus, entry["topic_heading"])
    user = USER.format(file=entry["file"], syllabus=block or "", notes=notes_path.read_text())
    return g.build_body([{"text": user + note}], system=SYSTEM.format(title=title), code_execution=True,
                        thinking=args.thinking)


RETRY_NOTE = "\n\nYour previous reply was rejected (it was not valid JSON or you did not run code). Run the code tool and reply with ONLY the JSON object."


def accept(subject, f, r):
    """Parse a verification result; return the report dict or None if it must be redone."""
    try:
        rep = parse_json(r["text"])
        rep.setdefault("problems", [])
    except Exception as e:
        print(f"[{f}] bad JSON ({e})", flush=True)
        return None
    if r["code_runs"] == 0:
        print(f"[{f}] no code run; will retry", flush=True)
        return None
    rep["file"] = f
    rep["code_runs"] = r["code_runs"]
    rep["cost_usd"] = round(r["cost"], 4)
    d = VERIFY_DIR(subject)
    d.mkdir(parents=True, exist_ok=True)
    (d / (f + ".json")).write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print(f"[{f}] {len(rep['problems'])} problem(s), code runs {r['code_runs']}, ${r['cost']:.2f}", flush=True)
    return rep


def run_sync(subject, title, pending, ndir, syllabus, args):
    lock = threading.Lock()
    def one(entry):
        f = entry["file"]
        for attempt in range(3):
            if _stop.is_set():
                return
            with lock:
                try:
                    g.check_safety(subject, 1.0)
                except SystemExit as e:
                    _stop.set(); print(e, flush=True); return
            print(f"[{f}] verify attempt {attempt + 1} ...", flush=True)
            try:
                body = make_body(entry, ndir / f, syllabus, title, args, "" if attempt == 0 else RETRY_NOTE)
                resp = g._http("POST", f"{g.API}/models/{args.model}:generateContent", body)
                r = g.parse_response(resp, args.model, subject=subject, file=f,
                                     task="verify" if attempt == 0 else f"verify-retry{attempt}")
            except Exception as e:
                print(f"[{f}] API error: {g.scrub(str(e))[:300]}", flush=True)
                return
            if accept(subject, f, r):
                return
        print(f"[{f}] verification FAILED to produce a report", flush=True)
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        list(ex.map(one, pending))


def run_batch(subject, title, pending, ndir, syllabus, args):
    by = {e["file"]: e for e in pending}
    def mk(key, attempt, prev):
        return make_body(by[key], ndir / key, syllabus, title, args, "" if attempt == 0 else RETRY_NOTE)
    def handle(key, result, error, attempt):
        if result is None:
            print(f"[{key}] request error: {(error or {}).get('message','?')[:200]}", flush=True)
            return "retry", None
        return ("done", None) if accept(subject, key, result) else ("retry", None)
    g.run_batch_rounds(subject, "verify", list(by), mk, handle, 2, args.model, poll=args.poll)


def build_report(subject, plan):
    d = VERIFY_DIR(subject)
    out = [f"# Verification report: {subject}", ""]
    total, missing = 0, []
    rows = []
    for e in plan:
        p = d / (e["file"] + ".json")
        if not p.exists():
            missing.append(e["file"])
            continue
        rep = json.loads(p.read_text())
        probs = rep.get("problems", [])
        total += len(probs)
        c = rep.get("checked", {})
        out_head = (f"## {e['file']}: {len(probs)} problem(s) "
                    f"(checked {c.get('worked_examples','?')} examples, {c.get('practice_questions','?')} questions, "
                    f"{c.get('distractor_explanations','?')} option explanations; code runs {rep.get('code_runs','?')})")
        rows.append(out_head)
        for i, q in enumerate(probs, 1):
            rows.append(f"{i}. **{q.get('where','?')}** [{q.get('severity','?')}, {q.get('type','?')}, "
                        f"{'numeric' if q.get('numeric') else 'non-numeric'}]  \n"
                        f"   Issue: {q.get('issue','')}  \n   Evidence: {q.get('evidence','')}  \n"
                        f"   Suggested fix: {q.get('suggested_fix','')}")
        rows.append("")
    out += [f"**{total} problem(s) reported in {len(plan) - len(missing)} file(s).**"]
    if missing:
        out.append(f"Not yet verified: {', '.join(missing)}")
    out += [""] + rows
    text = "\n".join(out)
    (d / "VERIFY-REPORT.md").write_text(text)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subject")
    ap.add_argument("--only", nargs="+", metavar="FILE")
    ap.add_argument("--model", default=g.default_model())
    ap.add_argument("--mode", choices=["batch", "sync"], default="batch",
                    help="batch = Batch API (about half price, slower, default); sync = immediate calls at full price")
    ap.add_argument("--poll", type=int, default=60, help="seconds between Batch status checks")
    ap.add_argument("--workers", type=int, default=3, help="parallel calls in sync mode")
    ap.add_argument("--thinking", choices=["low", "medium", "high"], default=None,
                    help="Gemini thinking level (default: the model default)")
    ap.add_argument("--notes-dir", help="read notes from this folder instead of subjects/<subject> (for tests)")
    ap.add_argument("--redo", action="store_true", help="verify again even if a report exists")
    ap.add_argument("--report", action="store_true", help="print the combined report and exit")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    sdir = g.ROOT / "subjects" / a.subject
    plan = su.parse_plan((sdir / "PLAN.md").read_text())
    syllabus = (sdir / "syllabus.md").read_text()
    ndir = Path(a.notes_dir) if a.notes_dir else sdir
    title = g.subject_title(a.subject)
    if a.report:
        print(build_report(a.subject, plan))
        return
    todo = [e for e in plan if (not a.only or e["file"] in a.only) and (ndir / e["file"]).exists()]
    d = VERIFY_DIR(a.subject)
    if a.status:
        for e in plan:
            s = "verified" if (d / (e["file"] + ".json")).exists() else ("pending" if (sdir / e["file"]).exists() else "no notes")
            print(f"{s:<10}{e['file']}")
        print(f"verification spend so far: ${verify_spend(a.subject):.2f} (list price)")
        return
    pending = [e for e in todo if a.redo or not (d / (e["file"] + ".json")).exists()]
    print(f"{len(pending)} file(s) to verify (mode {a.mode}; thinking {a.thinking or 'default'}). "
          f"Spent so far on {a.subject}: ${g.subject_spend(a.subject):.2f} (list price); safety limit ${g.safety_limit():.0f}.")
    if a.dry_run or not pending:
        return
    if a.mode == "batch":
        run_batch(a.subject, title, pending, ndir, syllabus, a)
    else:
        run_sync(a.subject, title, pending, ndir, syllabus, a)
    print()
    print(build_report(a.subject, plan))
    g.cost_report(a.subject)
    print(f"\nReport saved to {d / 'VERIFY-REPORT.md'}")


if __name__ == "__main__":
    main()
