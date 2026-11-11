# Nigeria secondary schools dataset

A list of Nigerian secondary schools (junior and senior) with location,
ownership and other details, built by combining public sources. Each source
is cleaned on its own into `data/sources/<source>.csv` using the shared
schema below. A merged, de-duplicated file will later go in `data/final/`.

This project is separate from the JAMB notes in this repository and never
modifies them.

## Folder layout

| Path | Contents |
|---|---|
| `data/raw/` | Raw downloads (git-ignored; re-create with the download scripts) |
| `data/sources/` | One cleaned CSV per source, in the shared schema |
| `data/final/` | Merged dataset: `nigeria_schools.csv`, `nigeria_schools_kenya_format.csv`, `merge_log.csv` |
| `scripts/` | All code. Python standard library only |

## Sources

| Source | File | Where from | Licence | Status |
|---|---|---|---|---|
| GRID3 Nigeria Education Facilities | `data/sources/grid3.csv` | HDX, <https://data.humdata.org/dataset/nigeria-education-facilities> | CC BY 4.0 (attribution: GRID3, NMIS, OSGOF, Proxy Logistics, eHA Polio, Bauchi JSI MCSP) | Cleaned: 24,098 schools |
| Federal Unity Colleges (Federal Ministry of Education, NEMIS 2021) | `data/sources/unity_colleges.csv` | <https://nemis.education.gov.ng/reports/FUCs.pdf> | Government publication, no licence stated | Cleaned: 110 colleges (64 matched to GRID3) |

### GRID3 notes

The HDX page has three files:

- `Nigeria_-_Schools.zip`: point shapefile, 107,670 schools, one row per school,
  with state, LGA and ward **names**. Uploaded 2023-08-17 (records stamped 2020).
- `NGA_Education.zip`: point shapefile, 204,513 rows, but only 103,586 unique
  schools: each school appears once per layer it belongs to (e.g. both
  `primary-schools` and `public-schools`). It has no Niger State records,
  only ward codes (no names), and every one of its schools is also in
  `Nigeria_-_Schools`.
- `NGA_Education_Facilities.xlsx`: the same table as `NGA_Education`, without
  coordinates.

We use `Nigeria_-_Schools`.

### GRID3 mapping

Rows kept: GRID3 `education` is Formal or Integrated, and `category` is
Secondary or Mixed (23,990). Also kept: 108 schools filed under another category
whose name clearly says secondary ("Secondary", "Grammar", "High School",
JSS/SSS/GSS and similar) and does not mention primary or nursery.

| Field | From GRID3 |
|---|---|
| `name` | `name`, extra spaces removed (spelling unchanged) |
| `level` | The name decides first: "Junior"/"JSS" gives `junior`, "Senior"/"SSS" gives `senior`. Otherwise `subtype` Junior/Senior. Everything else gives `junior+senior` (one row per school). GRID3's `subtype` is unreliable, so the name wins. |
| `region` | From the state (FCT is in North Central) |
| `state` | `statename` ("Fct" becomes "FCT") |
| `lga`, `ward` | `lganame`, `wardname` |
| `exam_code`, `accommodation_type` | Empty (not in GRID3) |
| `institution_type` | `PUBLIC`: Public, State Government, Federal Government. `PRIVATE`: Private, Private Faith Based, Private NGO Funded, NGO Funded. Empty: plain Faith Based (mission schools may have been taken over by government), Unknown, Public Private, Public Faith Based, Public NGO Funded. |
| `gender` | `girls` or `boys` only when the name says "Girls" or "Boys" (not both); otherwise empty, not assumed mixed |
| `lat`, `lon` | Shapefile point, 6 decimal places |
| `source` | `grid3` |
| `source_id` | GRID3 `globalid` |

GRID3's labels are kept as given. Some look wrong (e.g. a "Junior Secondary
School" marked Private); they are not corrected here.

Scripts:

- `scripts/grid3_download.py`: download the files from HDX into `data/raw/grid3/`.
- `scripts/grid3_profile.py`: print row counts, columns, categories and % missing.
- `scripts/grid3_clean.py`: write `data/sources/grid3.csv` using the mapping below.
- `scripts/shapefile_lite.py`: small standard-library shapefile reader.

### Federal Unity Colleges notes

Federal Unity Colleges (Federal Government Colleges, Girls Colleges, Science
and Technical Colleges, King's and Queen's College Lagos, etc.) are run by
the Federal Ministry of Education. All are `PUBLIC` and `junior+senior`.

**Source.** The ministry website (education.gov.ng) has no full list. Its
Senior School Education Department page (2026) only gives a count: "83
conventional Federal Unity Colleges" (= 110 minus the 27 Science and Technical
Colleges). Its "Unity Spotlight: History of Unity Schools" (2022) has a list,
but the PDF is scanned images and the list stops at entry 39 (Ekiti). The full
list used here is the ministry's NEMIS statistics report, March 2021 (2020/21
session): 110 colleges, with state (Table 9) and boys/girls enrolment by school
(Table 7). Both ministry domains allow crawling in robots.txt; neither has a
terms page. One public PDF is downloaded; nothing is scraped.

**Not current.** News reports mention about 115 colleges by 2024, so about 5
colleges founded since 2021 are missing (e.g. FSTC Misau, Bauchi, which is in the
2022 Spotlight). They are not added from unofficial lists.

**Errors in the report, handled in the script:**

- Table 2 leaves out FGGC Owerri and has a bare "FGC" line instead; Tables 7
  and 9 list FGGC Owerri. Table 1's totals (110) count the bare line.
- State labels sit in the middle of each state's group, so states are taken
  from the nearest label; 4 land wrong and are fixed by hand (FGBC Garki and
  FSTC Orozo: FCT; FGC Ijanikin: Lagos; FSTC Kuta, Shiroro: Niger).
- Town spellings fixed: "Ijebun Musin" is Ijebu-Mushin; "Nkwelle Ezunaka" (the site of
  FGGC Onitsha, as Table 9 calls it) is written as Onitsha, the college's name in
  Table 2 and the Spotlight; "Kuta Shiroro" is written "Kuta, Shiroro". Table 7's
  "FGCE, ODI" is FGC Odi.
- Abbreviations are written out: FGC = Federal Government College, FGGC =
  Federal Government Girls College, FGBC = Federal Government Boys College,
  FGA = Federal Government Academy, FSTC = Federal Science and Technical College,
  FSC = Federal Science College, KC/QC = King's/Queen's College.

**Mapping.**

| Field | How |
|---|---|
| `name` | Type + town, e.g. "Federal Government College, Ohafia" |
| `level`, `institution_type` | `junior+senior`, `PUBLIC` |
| `region`, `state` | State from the report; zone from the state |
| `gender` | In order: the 2022 Spotlight (38 colleges; typed in by hand because it is a scanned image); the name (Girls, Boys, King's, Queen's); 2021 enrolment (boys and girls both enrolled gives `mixed`; FSTC Uyo has girls only). 7 newer FSTCs with no 2021 enrolment are left empty. Two Spotlight entries disagree with the enrolment table and the Spotlight is kept: FGGC Gboko (enrolment shows 1,259 boys, 0 girls, likely swapped columns) and FSTC Amuzu (50 girls, 0 boys). |
| `accommodation_type`, `exam_code` | Empty (neither list says) |
| `lga`, `ward`, `lat`, `lon` | From the matching row in `grid3.csv`; empty if no match |
| `source`, `source_id` | `unity_colleges`, a slug such as `fgc-ohafia` (the report has no IDs) |

**Matching to GRID3.** A GRID3 row matches if it is in the same state, is the
same type of college (spelling-tolerant: "Governement", "Collage", "Fed Govt"),
and its name, or failing that its LGA or ward, contains the town. 64 of 110
matched: 40 by town in name, 18 by town in LGA/ward, 6 reviewed by hand (5 where GRID3
has just one college of that type in the state, plus FGGC Oyo, which had two
candidate rows). 4 single candidates were rejected after review (FGGC Bauchi,
FGC Vandeikya, FGGC Gusau, FGC New Bussa). The other 42 colleges are not in
`grid3.csv`. Every decision is in `data/sources/unity_colleges_grid3_match.csv`
(`unity_source_id`, `grid3_source_id`, `match_method`, `gender_basis`).

Script: `scripts/unity_colleges.py` (downloads the PDF to `data/raw/unity_colleges/`;
needs the `pdftotext` command from poppler-utils).

## Final dataset

Built by `scripts/build_final.py` from `data/sources/grid3.csv`,
`data/sources/unity_colleges.csv` and `data/sources/unity_colleges_grid3_match.csv`.
It powers the "pick your school" list in the Miyagi app.

**Result: 24,114 schools** (24,004 from GRID3, 110 Federal Unity Colleges).
Level: 16,322 `junior+senior`, 5,776 `junior`, 2,016 `senior`.

| File | Contents |
|---|---|
| `data/final/nigeria_schools.csv` | The shared schema plus `name_original` (the name exactly as in the source file) |
| `data/final/nigeria_schools_kenya_format.csv` | Same rows in the Kenya schools table's columns (below) |
| `data/final/merge_log.csv` | Every row dropped or merged: kept and dropped source/ID, dropped name, reason |

**Steps.**

1. **Unity Colleges.** Each of the 64 colleges matched to GRID3 becomes one
   row: Unity name, gender, level and state plus GRID3's LGA, ward and
   coordinates (`source` = `unity_colleges`). The matched GRID3 row is dropped,
   and so are 5 more GRID3 copies of matched colleges (FGC Ohafia, FSTC Ohanso,
   FGGC Lejja, FGGC Tambuwal, FGGC Oyo). "Federal Government College Tungan Goru"
   near FGC Minna is kept because it may be a different school. The 46
   unmatched colleges are added with LGA, ward and coordinates empty.
2. **GRID3 duplicates.** Rows with the same name (ignoring case, spaces and
   punctuation, after the typo fixes) in the same LGA and less than 0.5 km apart are
   merged into one: 25 pairs, mostly the same school spelled two ways or
   listed once per section. The merged level combines both (junior + senior
   gives `junior+senior`); `institution_type` and `gender` are kept only if both
   rows agree, otherwise left empty. 105 other same-name groups are 0.5 km or
   more apart (generic names such as "Government Junior Secondary School") and are
   kept as separate schools; the ward tells them apart.
3. **Names (GRID3 rows only; Unity names are already clean).** `name_original` keeps the source
   name. 1,772 rows changed:
   - **Typo fixes, 878 rows.** Whole words only, from an approved list of
     misspellings of common words (e.g. Goverment → Government, Grammer → Grammar,
     Collage → College, Secondry → Secondary, Morden → Modern; full list in
     `TYPOS` in the script). Nothing else is respelled: place and personal names,
     spelling variants (Islamiya, Ahmadiyyah), abbreviations (Schl) and real
     words (Academic, Collegiate, Saints) are left alone.
   - **Tidying, 918 rows.** Small joining words (and, of, the, in, for, on,
     at, by) in lowercase unless first; words starting in lowercase
     capitalised; run-together words split (SchoolKawo → School Kawo);
     apostrophes that GRID3 turned into capitals restored (SaintS → Saint's, JamaAre →
     Jama'are). All-caps abbreviations (UBE, NKST, ECWA) and stray single
     letters are left as they are.

**Kenya-format file.** Columns: `name`, `level`, `region`, `county` (= state),
`sub_county` (= LGA), `ward_name` (= ward), `knec_code` (empty), `institution_type`,
`accommodation_type`, `gender`, `lat`, `lon`. Values follow the Kenya table:
`gender` in capitals (`MIXED`, `GIRLS`, `BOYS`); `institution_type` `PUBLIC` /
`PRIVATE`; `accommodation_type` would be `DAY` / `BOARDING` / `HYBRID` but is
empty for now. `level` keeps `junior+senior` as a third value. `region` is the
geopolitical zone. Left out: `id`, `created_at`, `fts`, `name_original`.

## Sources considered and skipped

- **OpenStreetMap** (`amenity=school`, checked Nov 2026): only about 4,000 schools in Nigeria, of which about 400–600 look secondary and about half are unnamed, and its ODbL share-alike licence would bind any merged dataset. Not worth it.

## Schema

| Field | Meaning |
|---|---|
| `name` | School name as given by the source |
| `level` | One of three values: `junior`, `senior`, or `junior+senior` (a school with both junior and senior sections; the app is adding support for it) |
| `region` | Geopolitical zone: North Central, North East, North West, South East, South South, South West |
| `state` | State name (36 states + FCT) |
| `lga` | Local Government Area name |
| `ward` | Ward name |
| `exam_code` | WAEC/NECO centre code (empty for now) |
| `institution_type` | `PUBLIC` or `PRIVATE` |
| `accommodation_type` | Day, boarding, or both |
| `gender` | `boys`, `girls` or `mixed` (empty if unknown) |
| `lat`, `lon` | WGS84 decimal degrees |
| `source` | Source of the row (e.g. `grid3`) |
| `source_id` | The record's ID in its source (GRID3: `globalid`; Unity Colleges: a slug) |
