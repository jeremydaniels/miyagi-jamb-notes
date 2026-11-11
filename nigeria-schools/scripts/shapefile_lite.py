"""Minimal standard-library reader for point shapefiles (.shp + .dbf).

Only what this project needs: point geometry (shape type 1) and dBASE III
attribute tables. No third-party dependencies.
"""
import struct


def read_dbf(path, encoding="utf-8"):
    """Yield one dict per record of a .dbf file (deleted records skipped)."""
    with open(path, "rb") as f:
        header = f.read(32)
        n_records, header_len, record_len = struct.unpack("<4xIHH20x", header)
        fields = []
        while True:
            desc = f.read(32)
            if desc[0] == 0x0D:
                break
            name = desc[:11].split(b"\0")[0].decode("ascii")
            fields.append((name, desc[16]))
        f.seek(header_len)
        for _ in range(n_records):
            rec = f.read(record_len)
            if rec[0:1] == b"*":
                yield None  # keep alignment with .shp
                continue
            pos, row = 1, {}
            for name, length in fields:
                row[name] = rec[pos:pos + length].decode(encoding, "replace").strip()
                pos += length
            yield row


def read_points(path):
    """Yield (x, y) for each record of a point .shp file; None for null shapes."""
    with open(path, "rb") as f:
        f.seek(100)
        while True:
            head = f.read(8)
            if len(head) < 8:
                break
            _, content_len = struct.unpack(">ii", head)
            content = f.read(content_len * 2)
            shape_type = struct.unpack("<i", content[:4])[0]
            if shape_type == 0:
                yield None
            elif shape_type in (1, 11, 21):
                yield struct.unpack("<dd", content[4:20])
            else:
                raise ValueError(f"unsupported shape type {shape_type}")


def read_layer(base):
    """Yield attribute dicts with 'lon'/'lat' added. base = path without extension."""
    for attrs, pt in zip(read_dbf(base + ".dbf"), read_points(base + ".shp")):
        if attrs is None:
            continue
        attrs["lon"], attrs["lat"] = (pt if pt else ("", ""))
        yield attrs
