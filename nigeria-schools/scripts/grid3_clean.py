"""Clean the GRID3 Nigeria_-_Schools layer into data/sources/grid3.csv.

Keeps formal/integrated secondary schools and maps them to the shared schema
(see README.md, "GRID3 mapping"). Standard library only.

    python nigeria-schools/scripts/grid3_download.py   # once
    python nigeria-schools/scripts/grid3_clean.py
"""
import collections
import csv
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from shapefile_lite import read_layer  # noqa: E402

ROOT = HERE.parent
LAYER = ROOT / "data" / "raw" / "grid3" / "nigeria_-_schools" / "Nigeria_-_Schools"
OUT = ROOT / "data" / "sources" / "grid3.csv"

FIELDS = ["name", "level", "region", "state", "lga", "ward", "exam_code",
          "institution_type", "accommodation_type", "gender", "lat", "lon",
          "source", "source_id"]

SECONDARY_CATEGORIES = {"Secondary", "Mixed"}
KEEP_EDUCATION = {"Formal", "Integrated"}

# Schools filed under another category whose name clearly says secondary.
SECONDARY_NAME = re.compile(
    r"\b(secondary|sec sch|grammar|high school|g?jss|g?sss|gss|gdss|cgss|cdss)\b", re.I)
PRIMARY_NAME = re.compile(r"\b(nursery|primary|pry)\b", re.I)

JUNIOR_NAME = re.compile(r"\b(junior|jss|gjss|jnr)\b", re.I)
SENIOR_NAME = re.compile(r"\b(senior|sss|gsss|snr)\b", re.I)
GIRLS_NAME = re.compile(r"\bgirls?\b", re.I)
BOYS_NAME = re.compile(r"\bboys?\b", re.I)

PUBLIC = {"Public", "State Government", "Federal Government"}
PRIVATE = {"Private", "Private Faith Based", "Private NGO Funded", "NGO Funded"}
# Left empty: "Faith Based", "Faith Based NGO Funded", "Public Private",
# "Public Faith Based", "Public NGO Funded", "Unknown", blank.

ZONES = {
    "North Central": ["Benue", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau", "FCT"],
    "North East": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
    "North West": ["Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Sokoto", "Zamfara"],
    "South East": ["Abia", "Anambra", "Ebonyi", "Enugu", "Imo"],
    "South South": ["Akwa Ibom", "Bayelsa", "Cross River", "Delta", "Edo", "Rivers"],
    "South West": ["Ekiti", "Lagos", "Ogun", "Ondo", "Osun", "Oyo"],
}
REGION = {state: zone for zone, states in ZONES.items() for state in states}


def tidy(s):
    return re.sub(r"\s+", " ", s).strip()


def is_secondary(r):
    if r["education"] not in KEEP_EDUCATION:
        return False
    if r["category"] in SECONDARY_CATEGORIES:
        return True
    return bool(SECONDARY_NAME.search(r["name"])) and not PRIMARY_NAME.search(r["name"])


def level(r):
    j, s = bool(JUNIOR_NAME.search(r["name"])), bool(SENIOR_NAME.search(r["name"]))
    if j != s:
        return "junior" if j else "senior"
    if not (j or s) and r["subtype"] in ("Junior", "Senior"):
        return r["subtype"].lower()
    return "junior+senior"


def gender(name):
    g, b = bool(GIRLS_NAME.search(name)), bool(BOYS_NAME.search(name))
    if g != b:
        return "girls" if g else "boys"
    return ""


def institution_type(m):
    return "PUBLIC" if m in PUBLIC else "PRIVATE" if m in PRIVATE else ""


def main():
    rows = []
    for r in read_layer(str(LAYER)):
        if not is_secondary(r):
            continue
        state = "FCT" if r["statename"] == "Fct" else tidy(r["statename"])
        rows.append({
            "name": tidy(r["name"]),
            "level": level(r),
            "region": REGION[state],
            "state": state,
            "lga": tidy(r["lganame"]),
            "ward": tidy(r["wardname"]),
            "exam_code": "",
            "institution_type": institution_type(r["management"]),
            "accommodation_type": "",
            "gender": gender(r["name"]),
            "lat": f"{r['lat']:.6f}",
            "lon": f"{r['lon']:.6f}",
            "source": "grid3",
            "source_id": r["globalid"],
        })
    rows.sort(key=lambda x: (x["state"], x["lga"], x["ward"], x["name"].lower()))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows):,} rows to {OUT.relative_to(ROOT.parent)}")
    for col in ("level", "region", "institution_type", "gender"):
        print(col, dict(collections.Counter(x[col] or "(empty)" for x in rows).most_common()))


if __name__ == "__main__":
    main()
