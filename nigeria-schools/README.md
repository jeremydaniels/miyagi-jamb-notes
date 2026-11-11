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
| GRID3 Nigeria Education Facilities | `data/sources/grid3.csv` | HDX, <https://data.humdata.org/dataset/nigeria-education-facilities> | CC BY 4.0 (attribution: GRID3, NMIS, OSGOF, Proxy Logistics, eHA Polio, Bauchi JSI MCSP) | Downloaded and profiled; mapping awaiting approval |

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

Scripts:

- `scripts/grid3_download.py`: download the files from HDX into `data/raw/grid3/`.
- `scripts/grid3_profile.py`: print row counts, columns, categories and % missing.
- `scripts/shapefile_lite.py`: small standard-library shapefile reader.

## Schema

| Field | Meaning |
|---|---|
| `name` | School name as given by the source |
| `level` | `junior`, `senior` (see the source notes for schools offering both) |
| `region` | Geopolitical zone: North Central, North East, North West, South East, South South, South West |
| `state` | State name (36 states + FCT) |
| `lga` | Local Government Area name |
| `ward` | Ward name |
| `exam_code` | WAEC/NECO centre code (empty for now) |
| `institution_type` | `PUBLIC` or `PRIVATE` |
| `accommodation_type` | Day, boarding, or both |
| `gender` | Boys, girls, or mixed |
| `lat`, `lon` | WGS84 decimal degrees |
| `source` | Source of the row (e.g. `grid3`) |
