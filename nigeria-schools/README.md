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
| `data/final/` | Merged dataset (not built yet) |
| `scripts/` | All code. Python standard library only |

## Sources

| Source | File | Where from | Licence | Status |
|---|---|---|---|---|
| GRID3 Nigeria Education Facilities | `data/sources/grid3.csv` | HDX, <https://data.humdata.org/dataset/nigeria-education-facilities> | CC BY 4.0 (attribution: GRID3, NMIS, OSGOF, Proxy Logistics, eHA Polio, Bauchi JSI MCSP) | Cleaned: 24,098 schools |

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

## Sources considered and skipped

- **OpenStreetMap** (`amenity=school`, checked Nov 2026): only about 4,000 schools in Nigeria, of which about 400–600 look secondary and about half are unnamed, and its ODbL share-alike licence would bind any merged dataset. Not worth it.

## Schema

| Field | Meaning |
|---|---|
| `name` | School name as given by the source |
| `level` | `junior`, `senior`, or `junior+senior` |
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
| `source_id` | The record's ID in its source (GRID3: `globalid`) |
