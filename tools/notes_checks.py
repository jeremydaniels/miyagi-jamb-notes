"""Automatic checks for a finished notes file. Used by write_notes.py; also
runnable on its own:  python tools/notes_checks.py subjects/biology/D3-biotechnology.md
(structure checks only; the coverage-map checks need a PLAN entry)."""
import re
import sys

CLOSING = ["Key terms", "Exam tips and common mistakes", "Quick summary", "Practice questions"]
COVERAGE_RE = re.compile(r"<!--\s*COVERAGE\b(.*?)-->", re.S)


def split_coverage(text):
    """Return (text without the coverage comment, {('obj'|'item', id): heading})."""
    m = COVERAGE_RE.search(text)
    cov = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^\s*(obj|item)\s+(\S+)\s*\|\s*(.+?)\s*$", line)
            if mm:
                cov[(mm.group(1), mm.group(2).strip(".)").lower())] = mm.group(3)
        text = (text[:m.start()] + text[m.end():]).rstrip() + "\n"
    return text, cov


def _norm(s):
    s = re.sub(r"[*_`]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def headings(text):
    return [(len(m.group(1)), m.group(2)) for m in re.finditer(r"(?m)^(#{1,6}) (.+?)\s*$", _strip_fences(text))]


def _strip_fences(text):
    return re.sub(r"(?s)```.*?```", "", text)


def section(text, name):
    m = re.search(rf"(?ms)^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text)
    return m.group(1) if m else None


def check_math_delimiters(text):
    probs = []
    t = _strip_fences(text)
    blocks = re.findall(r"(?s)\$\$.*?\$\$", t)
    rest = re.sub(r"(?s)\$\$.*?\$\$", " ", t)
    if "$$" in rest:
        probs.append("unbalanced $$ display-math delimiters")
    for n, line in enumerate(rest.splitlines(), 1):
        if len(re.findall(r"(?<!\\)\$", line)) % 2:
            probs.append(f"odd number of $ on a line (unbalanced inline maths): {line.strip()[:80]!r}")
            if len(probs) > 5:
                break
    for b in blocks:
        if b.count("{") != b.count("}") and "\\{" not in b and "\\}" not in b:
            probs.append(f"unbalanced braces in display maths: {b.strip()[:60]!r}")
    return probs


def check_notes(text, entry=None, *, math=False, code_runs=None):
    """Return (clean_text, problems). `entry` is a PLAN entry dict (or None)."""
    text, cov = split_coverage(text)
    probs = []
    h = headings(text)
    if not text.startswith("# JAMB "):
        probs.append("file must start with a title line '# JAMB <Subject> Notes: <Topic>'")
    if not any(t == "What JAMB expects" for lvl, t in h if lvl == 2):
        probs.append("missing '## What JAMB expects' section")
    # closing sections: present once, in order, and the last four H2s
    h2 = [t for lvl, t in h if lvl == 2]
    for c in CLOSING:
        if h2.count(c) != 1:
            probs.append(f"closing section '## {c}' must appear exactly once (found {h2.count(c)})")
    if h2[-4:] != CLOSING:
        probs.append("the last four '##' sections must be, in order: " + " / ".join(CLOSING))
    # key terms table
    kt = section(text, "Key terms")
    if kt is not None and not re.search(r"(?m)^\|.*\|\s*$", kt):
        probs.append("Key terms must be a Markdown table")
    # summary
    qs = section(text, "Quick summary")
    if qs is not None:
        n = len(re.findall(r"(?m)^\d+\.\s", qs))
        if not 5 <= n <= 8:
            probs.append(f"Quick summary has {n} numbered points (needs 5 to 8)")
    # practice questions
    pq = section(text, "Practice questions")
    if pq is not None:
        starts = list(re.finditer(r"(?m)^\*\*(\d+)\.\s", pq))
        nums = [int(m.group(1)) for m in starts]
        if nums != list(range(1, 11)):
            probs.append(f"practice questions must be numbered 1 to 10 exactly (found {nums})")
        for i, m in enumerate(starts):
            chunk = pq[m.start(): starts[i + 1].start() if i + 1 < len(starts) else len(pq)]
            opts = re.findall(r"(?m)^- ([A-Z])\.\s+\S", chunk)
            if opts != ["A", "B", "C", "D"]:
                probs.append(f"question {m.group(1)}: needs options A to D as a bullet list (found {opts})")
            ans = re.findall(r"\*\*Answer:\s*([A-D])\.?\*\*", chunk)
            if len(ans) != 1:
                probs.append(f"question {m.group(1)}: needs exactly one '**Answer: X.**' line (found {len(ans)})")
            else:
                expl = chunk.split(f"**Answer: {ans[0]}", 1)[-1]
                expl = re.sub(r"^\.?\*\*", "", expl).strip()
                if len(expl) < (80 if math else 25):
                    probs.append(f"question {m.group(1)}: answer has no explanation/working")
                if math and "$" not in expl:
                    probs.append(f"question {m.group(1)}: maths answer shows no worked $...$ working")
    # image placeholders
    ph = re.findall(r"(?m)^\[IMAGE:.*$", text)
    if not ph:
        probs.append("no [IMAGE: ...] placeholders")
    for p in ph:
        if len(p) < 120 or not p.rstrip().endswith("]"):
            probs.append(f"weak or unterminated image placeholder: {p[:70]!r}")
    if re.search(r"(?m)^!\[", text):
        probs.append("contains real images '![...]'; use [IMAGE: ...] placeholders instead")
    # narration leaked from the tool-using model
    if re.search(r"(?mi)^(let me |i will |i'll |now i |running the code|executing |i have verified|i verified)", text):
        probs.append("narration such as 'Let me verify...' leaked into the file")
    if re.search(r"(?i)code execution|python script|```python", text):
        probs.append("mentions code execution or Python code; remove it")
    if math:
        probs += check_math_delimiters(text)
        if code_runs == 0:
            probs.append("code execution tool was never used, so nothing was verified")
    # length and coverage map
    words = len(text.split())
    if entry:
        est = entry.get("est_words") or 0
        if est and words < 0.4 * est:
            probs.append(f"too short: {words} words (plan estimate {est}); never shorten a topic")
        need = [("obj", x) for x in entry.get("objectives", [])] + [("item", x) for x in entry.get("contents", [])]
        titles = {_norm(t) for _, t in h}
        for kind, ident in need:
            key = (kind, ident.lower())
            if key not in cov:
                probs.append(f"COVERAGE map is missing '{kind} {ident}'")
            elif _norm(cov[key]) not in titles:
                probs.append(f"COVERAGE map: heading for '{kind} {ident}' not found in the file: {cov[key]!r}")
        if need:
            objs_h = {_norm(cov[k]) for k in cov if k[0] == "obj"}
            if len(objs_h) < len({x for k, x in need if k == "obj"}) and entry.get("objectives"):
                probs.append("every objective needs its OWN heading (two objectives share one heading)")
    return text, probs


if __name__ == "__main__":
    for path in sys.argv[1:]:
        t, p = check_notes(open(path).read(), None, math="mathematics" in path)
        print(path, "OK" if not p else "")
        for x in p:
            print("  -", x)
