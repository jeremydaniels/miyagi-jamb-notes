"""Merge the cleaned sources into the final tables.

Inputs:  data/sources/grid3.csv, data/sources/unity_colleges.csv,
         data/sources/unity_colleges_grid3_match.csv
Outputs: data/final/nigeria_schools.csv               (shared schema + name_original)
         data/final/nigeria_schools_kenya_format.csv  (Kenya schools table columns)
         data/final/merge_log.csv                     (every dropped or merged row)

Steps (see README.md, "Final dataset"):
1. GRID3 names: word-level typo fixes (TYPOS), then display tidying (tidy()).
   The source name is kept in name_original.
2. Unity Colleges replace their matched GRID3 row (Unity name/gender, GRID3
   lga/ward/coordinates); 5 more GRID3 copies of matched colleges are dropped;
   unmatched colleges are added as new rows.
3. GRID3 rows with the same name and LGA less than 0.5 km apart are merged.

Standard library only.

    python nigeria-schools/scripts/build_final.py
"""
import collections
import csv
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from grid3_clean import FIELDS  # noqa: E402

ROOT = HERE.parent
SOURCES = ROOT / "data" / "sources"
FINAL = ROOT / "data" / "final"

# Approved word-level typo fixes: correct word -> misspellings (whole words only).
TYPOS = {
    "Government": "goverment governmemt govenment governement governent govermment governtment "
                  "govermemt governmnet govermen govrnment govermkent govermnet governmet "
                  "governmement ggovernment governmen govovernment governmenr govertment governemt",
    "College": "collage colledge colloge collge collete callege coleege cellege colldge coledge "
               "collegde colleage",
    "Secondary": "secondry seconday scondary secodary secoundary secondsry secomdary secondery "
                 "secndary seconary secpndary seondary seconadry secondray srcondary secoondary "
                 "seecondary decondary seconadary seccondary secondaey seconsary secondar "
                 "secodanry seconsry sececondary seciondary seaondary scoendary",
    "School": "shool schooll schoolool schoool schoo scool schlool sechool schol chool schpool dchool",
    "Junior": "junoir juniour jinior jounior junlor juinor journior junor jnuior junioir junionr "
              "jusnior junikr jonior",
    "Senior": "senoir seniour sinior",
    "Grammar": "grammer gramar granmar grammr gammar grammwr garmmar grammaf gramnar",
    "Comprehensive": "comprehesive comprehsive comphensive comprensive commprehensive comphrensive "
                     "conprehensive comperehensive comprehenive comprenhensive comphrehensive "
                     "comprehemsive comprehencive comprehensivee comperhensive comprrehensive "
                     "compehensive cpmprehensive comprihensive comrehensive comprhensive",
    "Community": "comunity commmunity comminity communty commuity communoty commnuity comnunity "
                 "conmunity commununity communnity commumity communiy communnty",
    "Academy": "accademy acedemy acadamy aademy agademy adademy",
    "International": "internatonal lnternational internationl interntional internationall "
                     "inetrnational internstional intetnational internatiomsl internatioal "
                     "internatinal internarional internatkomal internatial interanational "
                     "internetional intnational",
    "Commercial": "comercial commerial commerical commercal coommercial commarcial commetcial",
    "Memorial": "memoral memmorial memrial memoraial memofial memomrial memoriial",
    "Technical": "techincal techinical tecthnical",
    "Christian": "christain chrisrian",
    "Demonstration": "demostration demosntration",
    "Foundation": "fundation foundatoon foundantion foudation",
    "Nursery": "nusery nursary nursrey nursey nursuery nurery",
    "Primary": "primry pirmary primarty pramary prinary pimary ptimary piramary",
    "Girls": "gilrs girlds girlss",
    "Islamic": "isamic lslamic",
    "Modern": "morden mordern moderm",
    "Science": "sceince secince sciene",
    "Success": "sucess",
    "Education": "edution educatiom",
    "Federal": "fedral",
    "Anglican": "anlican",
    "Baptist": "bapist",
    "Apostolic": "apostelic",
    "Vocational": "vacational voketional",
    "Excellence": "exellence",
    "Centre": "centtre",
    "Central": "centeral",
    "Technology": "techology",
    "Methodist": "methhodist",
    "Pentecostal": "penticostal",
    "Polytechnic": "polytechic",
    "Universal": "univeral",
    "Private": "prvate",
    "Quranic": "quaranic",
    "Standard": "stardard",
}
TYPO_MAP = {bad: good for good, bads in TYPOS.items() for bad in bads.split()}

SMALL_WORDS = {"and", "of", "the", "in", "for", "on", "at", "by"}
SPECIAL_TOKENS = {"JamaAre": "Jama'are", "GirlS": "Girls"}

# GRID3 copies of matched Unity Colleges besides the matched row (approved).
EXTRA_UNITY_DUPLICATES = {
    "436d1726-7f03-47d3-a698-4b0f52a5b38b": "fgc-ohafia",
    "e37bff96-360e-4f50-83f4-11df417c3d7a": "fstc-ohanso",
    "ce4d8bae-7480-4ba9-9f02-8c44d75d7712": "fggc-lejja",
    "963f9262-fdb5-4be1-9f1c-447c26e1fde3": "fggc-tambuwal",
    "aec10f63-df25-4ceb-9208-807d9c5249ee": "fggc-oyo",
}
MERGE_KM = 0.5

KENYA_FIELDS = ["name", "level", "region", "county", "sub_county", "ward_name", "knec_code",
                "institution_type", "accommodation_type", "gender", "lat", "lon"]
KENYA_ACCOMMODATION = {"day": "DAY", "boarding": "BOARDING", "day+boarding": "HYBRID"}


def read(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def same_case(template, word):
    if template.isupper() and len(template) > 1:
        return word.upper()
    if template[:1].islower():
        return word.lower()
    return word


def fix_typos(name):
    return re.sub(r"[A-Za-z]+",
                  lambda m: same_case(m.group(0), TYPO_MAP[m.group(0).lower()])
                  if m.group(0).lower() in TYPO_MAP else m.group(0), name)


def tidy(name):
    words = []
    for i, w in enumerate(name.split()):
        w = SPECIAL_TOKENS.get(w, w)
        w = re.sub(r"^([A-Z][a-z]{2,})S$", r"\1's", w)                        # SaintS -> Saint's
        w = re.sub(r"^([A-Z][a-z]{2,})([A-Z][a-z]{2,})$", r"\1 \2", w)          # SchoolKawo
        if i > 0 and w.lower() in SMALL_WORDS and not w.isupper():
            w = w.lower()
        elif len(w) > 1 and w[0].islower():
            w = w[0].upper() + w[1:]
        words.append(w)
    return " ".join(words)


def km(a, b):
    la1, lo1, la2, lo2 = (float(a["lat"]), float(a["lon"]), float(b["lat"]), float(b["lon"]))
    return math.hypot((la1 - la2) * 111.32, (lo1 - lo2) * 111.32 * math.cos(math.radians(la1)))


def merge_level(levels):
    parts = {p for lv in levels for p in lv.split("+") if p}
    return "+".join(p for p in ("junior", "senior") if p in parts)


def agreed(values):
    vals = {v for v in values}
    return vals.pop() if len(vals) == 1 else ""


def main():
    grid3 = read(SOURCES / "grid3.csv")
    unity = read(SOURCES / "unity_colleges.csv")
    matches = {m["unity_source_id"]: m for m in read(SOURCES / "unity_colleges_grid3_match.csv")}
    grid3_by_id = {g["source_id"]: g for g in grid3}
    log, counts = [], collections.Counter()

    # 1. GRID3 names
    for g in grid3:
        original = g["name"]
        typo_fixed = fix_typos(original)
        g["name"] = tidy(typo_fixed)
        g["name_original"] = original
        counts["typo"] += typo_fixed != original
        counts["tidy"] += g["name"] != typo_fixed
        counts["any"] += g["name"] != original

    # 2. Unity Colleges
    drop = {}
    rows = []
    for u in unity:
        u = dict(u, name_original=u["name"])
        m = matches[u["source_id"]]
        if m["grid3_source_id"]:
            gid = m["grid3_source_id"]
            drop[gid] = (u["source_id"], f"replaced by Unity College ({m['match_method']})")
        rows.append(u)
    for gid, sid in EXTRA_UNITY_DUPLICATES.items():
        assert gid in grid3_by_id, gid
        drop[gid] = (sid, "second GRID3 copy of a Unity College")
    for gid, (sid, reason) in drop.items():
        g = grid3_by_id[gid]
        log.append({"kept_source": "unity_colleges", "kept_source_id": sid,
                    "dropped_source": "grid3", "dropped_source_id": gid,
                    "dropped_name": g["name_original"], "reason": reason})
    remaining = [g for g in grid3 if g["source_id"] not in drop]

    # 3. Same name + same LGA, less than MERGE_KM apart
    groups = collections.defaultdict(list)
    for g in remaining:
        groups[(g["state"], g["lga"], re.sub(r"[^a-z0-9]", "", g["name"].lower()))].append(g)
    merged_away = set()
    for members in groups.values():
        if len(members) < 2:
            continue
        if max(km(a, b) for i, a in enumerate(members) for b in members[i + 1:]) >= MERGE_KM:
            counts["same_name_kept"] += 1
            continue
        keep, others = members[0], members[1:]
        counts["merged_groups"] += 1
        conflicts = [f for f in ("institution_type", "gender")
                     if len({m[f] for m in members}) > 1]
        keep["level"] = merge_level(m["level"] for m in members)
        keep["institution_type"] = agreed(m["institution_type"] for m in members)
        keep["gender"] = agreed(m["gender"] for m in members)
        for o in others:
            merged_away.add(o["source_id"])
            reason = f"same name and LGA, {km(keep, o):.2f} km apart; merged"
            if conflicts:
                reason += " (" + ", ".join(conflicts) + " disagreed; left empty)"
            log.append({"kept_source": "grid3", "kept_source_id": keep["source_id"],
                        "dropped_source": "grid3", "dropped_source_id": o["source_id"],
                        "dropped_name": o["name_original"], "reason": reason})
    rows += [g for g in remaining if g["source_id"] not in merged_away]

    rows.sort(key=lambda r: (r["state"], r["lga"], r["name"].lower(), r["source_id"]))
    FINAL.mkdir(parents=True, exist_ok=True)
    write(FINAL / "nigeria_schools.csv", rows, FIELDS + ["name_original"])
    kenya = [{
        "name": r["name"], "level": r["level"], "region": r["region"], "county": r["state"],
        "sub_county": r["lga"], "ward_name": r["ward"], "knec_code": "",
        "institution_type": r["institution_type"],
        "accommodation_type": KENYA_ACCOMMODATION.get(r["accommodation_type"], ""),
        "gender": r["gender"].upper(), "lat": r["lat"], "lon": r["lon"],
    } for r in rows]
    write(FINAL / "nigeria_schools_kenya_format.csv", kenya, KENYA_FIELDS)
    write(FINAL / "merge_log.csv", log, ["kept_source", "kept_source_id", "dropped_source",
                                         "dropped_source_id", "dropped_name", "reason"])

    print(f"final rows: {len(rows):,}")
    print("level:", dict(collections.Counter(r["level"] for r in rows).most_common()))
    print("source:", dict(collections.Counter(r["source"] for r in rows)))
    print(f"GRID3 names changed: typo fixes {counts['typo']:,} rows, tidying {counts['tidy']:,} rows, "
          f"either {counts['any']:,} rows")
    print(f"dropped for Unity Colleges: {len(drop)}; same-name groups merged: "
          f"{counts['merged_groups']} ({len(merged_away)} rows); same-name groups kept apart: "
          f"{counts['same_name_kept']}")


if __name__ == "__main__":
    main()
