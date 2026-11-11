"""Summarise the raw GRID3 layers: row count, columns, categories, % missing.

    python nigeria-schools/scripts/grid3_profile.py
"""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from shapefile_lite import read_layer  # noqa: E402

RAW = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw" / "grid3"
LAYERS = {
    "NGA_Education": RAW / "nga_education" / "NGA_Education",
    "Nigeria_-_Schools": RAW / "nigeria_-_schools" / "Nigeria_-_Schools",
}
SKIP_COUNTS = {"id", "name", "global_id", "globalid", "uniq_id", "FID", "lon", "lat",
               "path", "ward_code", "wardcode", "wardname", "no_of_teac",
               "no_of_stud", "student_ct", "teacher_ct", "lganame", "lgacode"}
MISSING = {"", "0", "None", "nan", "NULL", "null", "N/A", "Unknown"}


def main():
    for label, base in LAYERS.items():
        rows = list(read_layer(str(base)))
        cols = list(rows[0].keys())
        print(f"\n=== {label}: {len(rows):,} rows, {len(cols)} columns ===")
        print(f"{'column':<12} {'% missing':>9}  examples")
        for c in cols:
            vals = [r[c] for r in rows]
            miss = sum(v in ("",) or (isinstance(v, str) and v.strip() in MISSING)
                       for v in vals)
            ex = [v for v in vals if v not in ("",)][:2]
            print(f"{c:<12} {100*miss/len(rows):>8.1f}%  {ex}")
        for c in cols:
            if c in SKIP_COUNTS:
                continue
            cnt = collections.Counter(r[c] for r in rows)
            if len(cnt) > 60:
                print(f"\n{c}: {len(cnt)} distinct values")
                continue
            print(f"\n{c}:")
            for v, n in cnt.most_common():
                print(f"  {v!r:<40} {n:>8,}")
        bad = sum(1 for r in rows if r["lon"] == "" or not (2.5 < r["lon"] < 15 and 4 < r["lat"] < 14.5))
        print(f"\ncoords missing or outside Nigeria bbox: {bad:,}")


if __name__ == "__main__":
    main()
