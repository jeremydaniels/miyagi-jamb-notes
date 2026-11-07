"""Parsing helpers: syllabus.md topic blocks, PLAN.md entries, plan checks."""
import re

H = re.compile(r"^(#{2,3}) (.*)$")


def topic_blocks(syllabus):
    """Return list of (section_heading, topic_heading, text) for every `###` topic.
    A block runs until the next `##` or `###` heading (or end of file)."""
    lines = syllabus.splitlines()
    out, section, i = [], "", 0
    while i < len(lines):
        m = H.match(lines[i])
        if m and m.group(1) == "##":
            section = m.group(2).strip()
        elif m and m.group(1) == "###":
            j = i + 1
            while j < len(lines) and not H.match(lines[j]):
                j += 1
            text = "\n".join(l for l in lines[i:j] if l.strip() != "---").strip()
            out.append((section, m.group(2).strip(), text))
            i = j
            continue
        i += 1
    return out


def find_topic(syllabus, heading):
    heading = heading.strip()
    for sec, h, text in topic_blocks(syllabus):
        if h == heading:
            return sec, text
    return None, None


def item_ids(block):
    """Content item ids and objective ids printed in a topic block (best effort)."""
    contents, objectives, mode = [], [], "c"
    for l in block.splitlines():
        s = l.strip()
        if re.search(r"candidates should be able to", s, re.I):
            mode = "o"
            continue
        # a doubled marker such as "iv. iii. text" (a numbering slip) is read as the second one
        m = re.match(r"^[*\-]\s+\(?(?:[a-z]{1,4}[.)]\s+)?([a-z]{1,4})[.)]\s", s)
        if m:
            (contents if mode == "c" else objectives).append(m.group(1))
    return contents, objectives


def check_plan(files, syllabus):
    problems = []
    names = [f["file"] for f in files]
    if len(set(names)) != len(names):
        problems.append("duplicate file names")
    blocks = topic_blocks(syllabus)
    headings = [h for _, h, _ in blocks]
    used = {}
    for f in files:
        if not re.match(r"^[A-Z]\d+[a-z]?-[a-z0-9-]+\.md$", f["file"]):
            problems.append(f"bad file name: {f['file']}")
        if f["topic_heading"] not in headings:
            problems.append(f"{f['file']}: topic_heading not found in syllabus: {f['topic_heading']!r}")
        used.setdefault(f["topic_heading"], []).append(f)
    for h in headings:
        if h not in used:
            problems.append(f"syllabus topic not covered by any file: {h!r}")
    for sec, h, text in blocks:
        if h not in used:
            continue
        c, o = item_ids(text)
        got_c = [x for f in used[h] for x in f["contents"]]
        got_o = [x for f in used[h] for x in f["objectives"]]
        for x in c:
            if x not in got_c:
                problems.append(f"{h}: content item {x} not assigned to any file")
        for x in o:
            if x not in got_o and "only" not in got_o:
                problems.append(f"{h}: objective {x} not assigned to any file")
        for lst, name in ((got_c, "content item"), (got_o, "objective")):
            dup = {x for x in lst if lst.count(x) > 1}
            if dup:
                problems.append(f"{h}: {name}(s) {sorted(dup)} assigned to more than one file")
    return problems


def parse_plan(text):
    """Parse PLAN.md (as written by plan_subject.py) into a list of dicts."""
    entries = []
    for chunk in re.split(r"(?m)^### ", text.split("\n## Files", 1)[-1])[1:]:
        lines = chunk.splitlines()
        e = {"file": lines[0].strip(), "contents": [], "objectives": []}
        for l in lines[1:]:
            m = re.match(r"^- (Title|Section|Topic|Scope|Contents|Objectives|Split|Est\. words): ?(.*)$", l)
            if not m:
                continue
            k, v = m.group(1), m.group(2).strip()
            if k == "Topic":
                v = v.strip("`")
                e["topic_heading"] = v
            elif k in ("Contents", "Objectives"):
                e[k.lower()] = [x.strip() for x in v.split(",") if x.strip()]
            elif k == "Est. words":
                e["est_words"] = int(re.sub(r"\D", "", v) or 0)
            else:
                e[k.lower()] = v
        entries.append(e)
    return entries
