"""Download the GRID3 Nigeria Education Facilities dataset from HDX.

Uses the HDX CKAN API to list the resources, saves each one to
data/raw/grid3/ and unzips the shapefiles. Standard library only.

    python nigeria-schools/scripts/grid3_download.py
"""
import json
import pathlib
import urllib.request
import zipfile

DATASET = "nigeria-education-facilities"
API = f"https://data.humdata.org/api/3/action/package_show?id={DATASET}"
RAW = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw" / "grid3"


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(API) as r:
        pkg = json.load(r)["result"]
    (RAW / "package.json").write_text(json.dumps(pkg, indent=2))
    for res in pkg["resources"]:
        dest = RAW / res["url"].rsplit("/", 1)[-1]
        print(f"downloading {res['name']} -> {dest.name}")
        urllib.request.urlretrieve(res["url"], dest)
        if dest.suffix == ".zip":
            with zipfile.ZipFile(dest) as z:
                z.extractall(RAW / dest.stem)


if __name__ == "__main__":
    main()
