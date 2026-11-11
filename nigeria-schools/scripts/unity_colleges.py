"""Build data/sources/unity_colleges.csv from the ministry's NEMIS report.

Source: Federal Ministry of Education, Statistics & NEMIS, "Federal Unity
Colleges" report, March 2021 (2020/21 session):
https://nemis.education.gov.ng/reports/FUCs.pdf

- Table 9 (staff by state and school) gives the 110 colleges and their states.
- Table 7 (enrolment by school and gender) helps fill `gender`.
- Gender for the 38 colleges it covers comes first from the ministry's
  "Unity Spotlight: History of Unity Schools" (2022), whose list is a scanned
  image, so it is typed in below (SPOTLIGHT_GENDER).
- lga, ward, lat, lon come from a matching row in data/sources/grid3.csv.
  Every match decision is written to data/sources/unity_colleges_grid3_match.csv.

Needs `pdftotext` (poppler-utils) on the PATH. Otherwise standard library only.

    python nigeria-schools/scripts/unity_colleges.py
"""
import csv
import pathlib
import re
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from grid3_clean import FIELDS, REGION  # noqa: E402

ROOT = HERE.parent
URL = "https://nemis.education.gov.ng/reports/FUCs.pdf"
RAW = ROOT / "data" / "raw" / "unity_colleges"
GRID3 = ROOT / "data" / "sources" / "grid3.csv"
OUT = ROOT / "data" / "sources" / "unity_colleges.csv"
MATCH_OUT = ROOT / "data" / "sources" / "unity_colleges_grid3_match.csv"

STATES = {
    "ABIA", "ADAMAWA", "AKWA IBOM", "ANAMBRA", "BAUCHI", "BAYELSA", "BENUE", "BORNO",
    "CROSS RIVER", "DELTA", "EBONYI", "EDO", "EKITI", "ENUGU", "FCT", "GOMBE", "IMO",
    "JIGAWA", "KADUNA", "KANO", "KATSINA", "KEBBI", "KOGI", "KWARA", "LAGOS",
    "NASARAWA", "NIGER", "OGUN", "ONDO", "OSUN", "OYO", "PLATEAU", "RIVERS", "SOKOTO",
    "TARABA", "YOBE", "ZAMFARA",
}

# In Table 9 a state label sits in the middle of its group of colleges, so
# states are assigned to the nearest label. These four land on the wrong
# label and are fixed by hand (checked against the towns).
STATE_FIX = {
    "FGBC GARKI": "FCT",
    "FSTC OROZO": "FCT",
    "FGC IJANIKIN": "LAGOS",
    "FSTC KUTA SHIRORO": "NIGER",
}

TYPES = {
    "FGC": "Federal Government College",
    "FGGC": "Federal Government Girls College",
    "FGBC": "Federal Government Boys College",
    "FGA": "Federal Government Academy",
    "FSTC": "Federal Science and Technical College",
    "FSC": "Federal Science College",
    "KC": "King's College",
    "QC": "Queen's College",
}

# Town spellings corrected from the report (documented in README.md).
TOWN_FIX = {
    "IJEBUN MUSIN": "Ijebu-Mushin",      # typo in the report
    "NKWELLE EZUNAKA": "Onitsha",        # Table 9 uses the site; the college is FGGC Onitsha
    "KUTA SHIRORO": "Kuta, Shiroro",
}

# Table 7 spells a few colleges differently from Table 9 (keys: letters only).
ENROLMENT_ALIAS = {
    "FGGCNKWELLEEZUNAKA": "FGGCONITSHA",
    "KCLAGOS": "KINGSCOLLEGELAGOS",
    "QCLAGOS": "QUEENSCOLLEGELAGOS",
    "FGCODI": "FGCEODI",
}

# Unity Spotlight 2022 (education.gov.ng), "Federal Unity Colleges in Nigeria",
# entries 1-39 (the published list stops there). "Boys and Girls" -> mixed.
# Entry 15, FSTC Misau, is not in the 2021 report and FSTC Misau has no gender given.
SPOTLIGHT_GENDER = {
    "fggc-umuahia": "girls", "fgc-ohafia": "mixed", "fstc-ohanso": "mixed",
    "fgc-ganye": "mixed", "fggc-yola": "girls", "fstc-michika": "mixed",
    "fgc-ikot-ekpene": "mixed", "fggc-ikot-obio-itong": "girls", "fstc-uyo": "girls",
    "fgc-nise": "mixed", "fggc-onitsha": "girls", "fstc-awka": "mixed",
    "fgc-azare": "mixed", "fggc-bauchi": "girls",
    "fgc-odi": "mixed", "fggc-imiringi": "girls", "fstc-tungbo": "mixed",
    "fgc-vandeikya": "mixed", "fggc-gboko": "girls", "fstc-otukpo": "mixed",
    "fgc-otobi": "mixed", "fgc-maiduguri": "mixed", "fstc-lassa": "mixed",
    "fggc-monguno": "girls", "fgc-ikom": "mixed", "fggc-calabar": "girls",
    "fsc-ogoja": "mixed", "fggc-ibusa": "girls", "fgc-warri": "mixed",
    "fgc-ibillo": "mixed", "fstc-uromi": "mixed", "fggc-benin": "girls",
    "fgc-enugu": "mixed", "fggc-lejja": "girls", "fgc-okposi": "mixed",
    "fggc-ezzamgbo": "girls", "fstc-amuzu": "mixed", "fgc-ikole-ekiti": "mixed",
}

# Matches reviewed by hand (grid3 source_id, or None to force "unmatched").
MANUAL_MATCH = {
    # Only one college of that type in the state; place checked and accepted.
    "fstc-uromi": "5a0145dd-cb5c-499e-b939-4c8630bcd9c3",   # Esan North-East
    "fstc-yaba": "dfced3fc-8347-4f83-9171-1b871653e44f",    # Lagos Mainland
    "fgc-ogbomoso": "6d1b5ea0-5ab8-457a-aeda-d39af03db32b", # Ogbomosho North
    "fggc-abuloma": "9893e9e6-4f49-45cc-ac0d-658b310013f5", # Port-Harcourt
    "fstc-otukpo": "0a7f40d6-896b-408f-bf3b-9cc5aad5fba3",  # "Federal Technical College Oturkpo"
    # Two GRID3 rows name the town; this one is the full official name.
    "fggc-oyo": "30f6cbe9-d454-4d8a-9ed1-7902028bd760",
    # Rejected: the only candidate is in the wrong or an uncertain place.
    "fggc-bauchi": None,     # candidate is a girls' school in Azare
    "fgc-vandeikya": None,   # candidate is in Oturkpo
    "fggc-gusau": None,      # candidate is in Bungudu LGA; not confirmed
    "fgc-new-bussa": None,   # candidates are in Minna (Bosso LGA)
}


def pdf_text():
    RAW.mkdir(parents=True, exist_ok=True)
    pdf = RAW / "FUCs.pdf"
    if not pdf.exists():
        print(f"downloading {URL}")
        urllib.request.urlretrieve(URL, pdf)
    txt = RAW / "FUCs.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
    return txt.read_text(encoding="utf-8").splitlines()


def table_start(lines, title):
    # The last match skips the table of contents.
    return max(i for i, line in enumerate(lines) if title in line)


def read_table9(lines):
    """Return [(state, raw_name)] for the 110 colleges, in report order."""
    start = table_start(lines, "Table 9: Number of Teaching")
    end = next(i for i in range(start, len(lines)) if lines[i].strip().startswith("Total"))
    colleges, labels = [], []
    for line in lines[start + 3:end]:
        s = line.strip()
        if not s or s.startswith("STATISTICS") or s.isdigit():
            continue
        m = re.match(r"^(?:([A-Z][A-Z ]+?)\s{2,})?((?:FG|FS|KC|QC)[A-Z ,.\-]+?)\s{2,}[\d,]", s)
        if m:
            if m.group(1) and m.group(1).strip() in STATES:
                labels.append((len(colleges), m.group(1).strip()))
            colleges.append(m.group(2).strip())
        elif s in STATES:
            labels.append((len(colleges) - 0.5, s))
    out = []
    for pos, raw in enumerate(colleges):
        key = re.sub(r"[ ,]+", " ", raw).strip()
        state = STATE_FIX.get(key) or min(labels, key=lambda lab: abs(lab[0] - pos))[1]
        out.append((state, raw))
    return out


def read_table7(lines):
    """Return {letters-only school name: (boys, girls)} from Table 7."""
    start = table_start(lines, "Table 7: Enrolment by School")
    end = next(i for i in range(start, len(lines)) if lines[i].strip().startswith("Table 8"))
    enrol = {}
    for line in lines[start:end]:
        m = re.match(r"^\s*([A-Z][A-Z'’ ,.\-]+?)\s{2,}([\d,]+(?:\s+[\d,]+){12,})\s*$", line)
        if m:
            nums = [int(x.replace(",", "")) for x in m.group(2).split()]
            enrol[re.sub(r"[^A-Z]", "", m.group(1))] = (nums[-3], nums[-2])
    return enrol


def college_name(raw):
    abbr, town = re.match(r"^(FGC|FGGC|FGBC|FGA|FSTC|FSC|KC|QC)[ ,]+(.*)$", raw).groups()
    town = re.sub(r"[ ,.]+$", "", town).strip()
    town = TOWN_FIX.get(town, town.title())
    return abbr, town, f"{TYPES[abbr]}, {town}"


def slug(abbr, town):
    return abbr.lower() + "-" + re.sub(r"[^a-z]+", "-", town.lower()).strip("-")


def gender(sid, abbr, enrol):
    if sid in SPOTLIGHT_GENDER:
        return SPOTLIGHT_GENDER[sid], "spotlight_2022"
    if abbr in ("FGGC", "QC"):
        return "girls", "name"
    if abbr in ("FGBC", "KC"):
        return "boys", "name"
    boys, girls = enrol
    if boys and girls:
        return "mixed", "enrolment_2021"
    if girls >= 200 and not boys:
        return "girls", "enrolment_2021"
    return "", "unknown"


# ---- matching to grid3.csv -------------------------------------------------

EXCLUDE = (r"staff|education|polytechnic|animal|agric|nursing|health|university|business|"
           r"church|permanent|forestry|fisheries|survey|petroleum|aviation|veterinary|"
           r"cooperative|tourism|hospitality|wildlife|produce")


def norm(s):
    s = s.lower().replace("'", "").replace("’", "")
    s = re.sub(r"governe?ment|govt|\bgov\b", "government", s)
    s = re.sub(r"coll?age|colledge|collge", "college", s)
    s = re.sub(r"\bgirl\b", "girls", s).replace("&", "and")
    return re.sub(r"[^a-z ]", " ", s)


def same_type(abbr, n):
    if re.search(EXCLUDE, n):
        return False
    if abbr == "KC":
        return bool(re.search(r"\bkings? college\b", n)) and not re.search(r"christ|luther|commerce", n)
    if abbr == "QC":
        return bool(re.search(r"\bqueens? college\b", n))
    if not re.search(r"\bfed|\bfg|\bfs", n):
        return False
    return {
        "FGGC": lambda: bool(re.search(r"girls|\bfggc\b", n)),
        "FGBC": lambda: bool(re.search(r"boys|\bfgbc\b", n)),
        "FSTC": lambda: bool(re.search(r"science|technical|\bfstc\b", n)) and "girls" not in n,
        "FSC": lambda: bool(re.search(r"science|\bfsc\b", n)) and "technical" not in n,
        "FGA": lambda: bool(re.search(r"academy|\bfga\b", n)),
        "FGC": lambda: bool(re.search(r"government college|\bfgc\b", n))
        and not re.search(r"girls|boys|science|technical", n),
    }[abbr]()


def match(sid, abbr, towns, state, grid3_by_state, grid3_by_id):
    """towns: the cleaned town and the report's spelling (both are searched)."""
    if sid in MANUAL_MATCH:
        gid = MANUAL_MATCH[sid]
        if gid is None:
            return None, "rejected_after_review"
        return grid3_by_id[gid], "manual_reviewed"
    words = norm(" ".join(towns)).split()
    tokens = [t for t in words if len(t) > 2 and t not in ("ekiti", "state")] or words
    cands = [g for g in grid3_by_state.get(state, []) if same_type(abbr, norm(g["name"]))]
    in_name = [g for g in cands if any(t in norm(g["name"]) for t in tokens)]
    if len(in_name) == 1:
        return in_name[0], "town_in_name"
    if not in_name:
        in_admin = [g for g in cands if any(t in norm(g["lga"] + " " + g["ward"]) for t in tokens)]
        if len(in_admin) == 1:
            return in_admin[0], "town_in_lga_or_ward"
    return None, "no_match"


def main():
    lines = pdf_text()
    colleges = read_table9(lines)
    enrol = read_table7(lines)
    assert len(colleges) == 110, len(colleges)

    with open(GRID3, encoding="utf-8") as f:
        grid3 = list(csv.DictReader(f))
    by_state, by_id = {}, {g["source_id"]: g for g in grid3}
    for g in grid3:
        by_state.setdefault(g["state"].upper(), []).append(g)

    rows, matches, conflicts = [], [], []
    for state_upper, raw in colleges:
        abbr, town, name = college_name(raw)
        report_town = re.sub(r"^[A-Z]+[ ,]+", "", raw)
        sid = slug(abbr, town)
        key = re.sub(r"[^A-Z]", "", raw)
        boys_girls = enrol[ENROLMENT_ALIAS.get(key, key)]
        g, basis = gender(sid, abbr, boys_girls)
        boys, girls = boys_girls
        if basis == "spotlight_2022" and (boys or girls) and (
                (g == "girls" and boys) or (g == "mixed" and not (boys and girls))):
            conflicts.append((sid, g, boys_girls))
        state = "FCT" if state_upper == "FCT" else state_upper.title()
        hit, method = match(sid, abbr, (town, report_town), state_upper, by_state, by_id)
        rows.append({
            "name": name, "level": "junior+senior", "region": REGION[state], "state": state,
            "lga": hit["lga"] if hit else "", "ward": hit["ward"] if hit else "",
            "exam_code": "", "institution_type": "PUBLIC", "accommodation_type": "",
            "gender": g, "lat": hit["lat"] if hit else "", "lon": hit["lon"] if hit else "",
            "source": "unity_colleges", "source_id": sid,
        })
        matches.append({
            "unity_source_id": sid, "unity_name": name, "state": state,
            "grid3_source_id": hit["source_id"] if hit else "",
            "grid3_name": hit["name"] if hit else "", "grid3_lga": hit["lga"] if hit else "",
            "match_method": method, "gender_basis": basis,
        })

    assert len({r["source_id"] for r in rows}) == len(rows), "duplicate slugs"
    used = [m["grid3_source_id"] for m in matches if m["grid3_source_id"]]
    assert len(used) == len(set(used)), "a GRID3 row matched twice"

    rows.sort(key=lambda r: (r["state"], r["name"]))
    matches.sort(key=lambda m: (m["state"], m["unity_name"]))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    with open(MATCH_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(matches[0]))
        w.writeheader()
        w.writerows(matches)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT.parent)}")
    print(f"wrote {len(matches)} rows to {MATCH_OUT.relative_to(ROOT.parent)}")
    if conflicts:
        print("spotlight gender vs 2021 enrolment (boys, girls):", conflicts)


if __name__ == "__main__":
    main()
