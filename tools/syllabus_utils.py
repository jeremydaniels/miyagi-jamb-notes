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


_SKIP_SECTIONS = ("general objectives", "detailed syllabus", "recommended texts", "transcription notes")


def extra_blocks(syllabus):
    """`##` sections that have no `###` topics inside (for example Literature's list of selected
    texts). A plan entry may name one of these as its topic_heading. Returns (heading, text)."""
    lines = syllabus.splitlines()
    out, i = [], 0
    while i < len(lines):
        m = H.match(lines[i])
        if m and m.group(1) == "##":
            j = i + 1
            while j < len(lines) and not (H.match(lines[j]) and H.match(lines[j]).group(1) == "##"):
                j += 1
            body = lines[i:j]
            has_topics = any(H.match(l) and H.match(l).group(1) == "###" for l in body)
            name = m.group(2).strip()
            if not has_topics and not name.lower().startswith(_SKIP_SECTIONS):
                out.append((name, "\n".join(l for l in body if l.strip() != "---").strip()))
            i = j
            continue
        i += 1
    return out


def find_topic(syllabus, heading):
    heading = heading.strip()
    for sec, h, text in topic_blocks(syllabus):
        if h == heading:
            return sec, text
    for h, text in extra_blocks(syllabus):
        if h == heading:
            return h, text
    return None, None


def norm_id(x):
    return re.sub(r"[().\s]", "", x).lower()


def item_ids(block):
    """Top-level content item ids and objective ids printed in a topic block (best effort).
    Nested sub-items (indented deeper than the top level, e.g. i, ii under (a)) are ignored."""
    found = {"c": [], "o": []}
    mode = "c"
    for l in block.splitlines():
        s = l.strip()
        if re.search(r"candidates should be able to", s, re.I):
            mode = "o"
            continue
        # a doubled marker such as "iv. iii. text" (a numbering slip) is read as the second one
        m = re.match(r"^[*\-]\s+\(?(?:[a-z]{1,4}[.)]\s+)?([a-z]{1,4})[.)]", s)
        if m:
            found[mode].append((len(l) - len(l.lstrip()), m.group(1)))
    out = []
    for mode in ("c", "o"):
        items = found[mode]
        top = min((i for i, _ in items), default=0)
        out.append([x for i, x in items if i == top])
    return out[0], out[1]


def check_plan(files, syllabus):
    """Structural errors only (file names, topic headings, topics not covered)."""
    problems = []
    names = [f["file"] for f in files]
    if len(set(names)) != len(names):
        problems.append("duplicate file names")
    headings = [h for _, h, _ in topic_blocks(syllabus)]
    used = set()
    for f in files:
        f["topic_heading"] = f["topic_heading"].strip()
        if not re.match(r"^[A-Z]\d+[a-z]?-[a-z0-9-]+\.md$", f["file"]):
            problems.append(f"bad file name: {f['file']}")
        if f["topic_heading"] not in headings and f["topic_heading"] not in [h for h, _ in extra_blocks(syllabus)]:
            problems.append(f"{f['file']}: topic_heading not found in syllabus: {f['topic_heading']!r}")
        used.add(f["topic_heading"])
    for h in headings:
        if h not in used:
            problems.append(f"syllabus topic not covered by any file: {h!r}")
    return problems


def check_plan_items(files, syllabus):
    """Warnings about content items / objectives that look unassigned or assigned twice.
    Only warnings: some syllabi have irregular numbering."""
    warns = []
    used = {}
    for f in files:
        used.setdefault(f["topic_heading"].strip(), []).append(f)
    for sec, h, text in topic_blocks(syllabus):
        if h not in used:
            continue
        c, o = item_ids(text)
        got_c = [norm_id(x) for f in used[h] for x in f["contents"]]
        got_o = [norm_id(x) for f in used[h] for x in f["objectives"]]
        for ids, got, name in ((c, got_c, "content item"), (o, got_o, "objective")):
            for x in ids:
                if norm_id(x) not in got and "only" not in got and len(got) < len(ids):
                    warns.append(f"{h}: {name} {x} may not be assigned to any file")
            if len(set(ids)) == len(ids):   # only meaningful when the syllabus ids are unique
                dup = {x for x in got if got.count(x) > 1}
                if dup:
                    warns.append(f"{h}: {name}(s) {sorted(dup)} assigned to more than one file")
    return warns


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
