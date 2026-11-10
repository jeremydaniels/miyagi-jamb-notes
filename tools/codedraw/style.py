"""Shared look for code-drawn images (matplotlib): same fonts and soft palette as the AI images."""
import os
import sys
import logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

for _f in ("Inter-Medium.otf", "Inter-SemiBold.otf", "Inter-Regular.otf"):
    _p = os.path.join("/usr/share/fonts/opentype/inter", _f)
    if os.path.exists(_p):
        font_manager.fontManager.addfont(_p)
plt.rcParams["font.family"] = ["Inter", "DejaVu Sans"]
plt.rcParams["font.weight"] = "medium"
plt.rcParams["axes.unicode_minus"] = False

INK = "#282c34"
GREEN, BLUE, PINK, LAV, CREAM, ORANGE, GREY = "#9bc5a0", "#8fb8de", "#e8a5a5", "#c8b6e2", "#f6e7c1", "#f0b27a", "#c9ced6"
DEEP = {"green": "#4f9a62", "blue": "#3b7fc0", "pink": "#d0605f", "orange": "#e08a35", "lav": "#8466b8"}


def canvas(w=10, h=7):
    fig = plt.figure(figsize=(w, h), dpi=150)
    fig.patch.set_facecolor("white")
    return fig


MIN_PT = 14


def save(fig, path):
    """Save with a text lint: every text is raised to at least MIN_PT and overlapping texts are nudged apart."""
    from matplotlib.text import Text
    texts = [t for t in fig.findobj(Text) if t.get_text().strip() and t.get_visible()]
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
        from textfmt import fmt
    except Exception:
        fmt = lambda s: s
    for t in texts:
        new = fmt(t.get_text())
        if new != t.get_text():
            if os.environ.get("FMT_REPORT"):
                open(os.environ["FMT_REPORT"], "a").write(repr(t.get_text()) + " -> " + repr(new) + "\n")
            t.set_text(new)
        if t.get_fontsize() < MIN_PT:
            t.set_fontsize(MIN_PT)
    try:
        from templates import declutter
        declutter(fig, [t for t in texts if t.axes is not None], None)
    except Exception:
        pass
    w, h = fig.get_size_inches()
    if max(w, h) > 18:                       # a runaway canvas would exceed the image size limit
        k = 18 / max(w, h); fig.set_size_inches(w * k, h * k)
    fig.savefig(path, facecolor="white", bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


# ---- helpers shared by generated drawings ----
import json as _json
import numpy as _np
_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def _polys(geom):
    if geom["type"] == "Polygon":
        return [_np.array(geom["coordinates"][0])]
    return [_np.array(p[0]) for p in geom["coordinates"]]


def country_polys(*names):
    """Outline polygons (lon, lat arrays) of the named countries, Natural Earth 110m (public domain)."""
    d = _json.load(open(os.path.join(_DATA, "ne_110m_countries.geojson")))
    out = []
    for f in d["features"]:
        if f["properties"].get("ADMIN") in names:
            out += _polys(f["geometry"])
    return out


def continent_polys(continent):
    """All country outlines of a continent name ('Africa', 'Europe', ...) or of the whole world ('World')."""
    d = _json.load(open(os.path.join(_DATA, "ne_110m_countries.geojson")))
    out = []
    for f in d["features"]:
        if continent == "World" or f["properties"].get("CONTINENT") == continent:
            out += _polys(f["geometry"])
    return out


def nigeria_poly():
    """Detailed outline of Nigeria (lon, lat array), Natural Earth 50m (public domain)."""
    g = _json.load(open(os.path.join(_DATA, "ne_50m_nigeria.geojson")))
    return max(_polys(g), key=len)


def axes_clean(ax, xl, yl, xmax, ymax):
    """Clean textbook axes with arrowheads, no ticks. Origin at (0, 0)."""
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(2); ax.spines[s].set_color(INK)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(xl, fontsize=15, color=INK, loc="right"); ax.set_ylabel(yl, fontsize=15, color=INK, loc="top", rotation=0, labelpad=14)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=8); ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=8)


# ---------------------------------------------------------------- logic gate symbols (distinctive-shape, as in most textbooks)

def _bez(pts_codes):
    from matplotlib.path import Path
    verts = [p for p, _ in pts_codes]; codes = [c for _, c in pts_codes]
    return Path(verts, codes)


def gate(ax, kind, x, y, w=1.6, h=1.0, color=None, lw=2.4):
    """Draw a standard logic gate symbol on `ax` (data coordinates, y up, aspect should be equal).
    kind: AND, OR, NOT, NAND, NOR, XOR, XNOR, BUFFER. (x, y) is the centre of the body. w and h are the body width and height.
    Returns {"in": [(x, y), ...], "out": (x, y)}: the pin positions (two inputs for the two-input gates, one for NOT and BUFFER).
    The short pin wires (a quarter of w) are drawn too; connect your own wires to the returned points."""
    from matplotlib.patches import PathPatch, Circle, Polygon
    from matplotlib.path import Path
    M, L, C, Z = Path.MOVETO, Path.LINETO, Path.CURVE4, Path.CLOSEPOLY
    col = color or CREAM
    ink = INK if "INK" in globals() else "#2b2f3a"
    kind = kind.upper()
    x0, x1 = x - w / 2, x + w / 2
    y0, y1 = y - h / 2, y + h / 2
    pin = w * 0.28
    bubble = 0.09 * h * 1.6
    end = x1
    ins = []
    if kind in ("NOT", "BUFFER"):
        tri_end = x1 - (bubble * 2 if kind == "NOT" else 0)
        ax.add_patch(Polygon([(x0, y1), (x0, y0), (tri_end, y)], closed=True, fc=col, ec=ink, lw=lw, joinstyle="round", zorder=3))
        end = tri_end
        ins = [(x0 - pin, y)]
        ax.plot([x0 - pin, x0], [y, y], color=ink, lw=lw, zorder=2)
    else:
        base = kind[1:] if kind in ("NAND", "NOR", "XNOR") else kind
        if base == "AND":
            flat = x0 + w * 0.5
            verts = [((x0, y0), M), ((flat, y0), L), ((flat + w * 0.30, y0), C), ((x1, y - h * 0.22), C), ((x1, y), C),
                     ((x1, y + h * 0.22), C), ((flat + w * 0.30, y1), C), ((flat, y1), C), ((x0, y1), L), ((x0, y0), Z)]
            back = x0
        else:   # OR / XOR family: curved back, pointed front
            cx = x0 + w * 0.22     # depth of the concave back
            verts = [((x0, y0), M), ((x0 + w * 0.40, y0), C), ((x0 + w * 0.80, y0 + h * 0.08), C), ((x1, y), C),
                     ((x0 + w * 0.80, y1 - h * 0.08), C), ((x0 + w * 0.40, y1), C), ((x0, y1), C),
                     ((cx, y + h * 0.28), C), ((cx, y - h * 0.28), C), ((x0, y0), C)]
            back = x0 + w * 0.12
        path = _bez([(p, c) for p, c in verts])
        ax.add_patch(PathPatch(path, fc=col, ec=ink, lw=lw, joinstyle="round", zorder=3))
        if base == "XOR" or kind == "XOR" or kind == "XNOR":
            off = w * 0.10
            # simple back curve: same bulge as the body back, shifted left
            p2 = _bez([((x0 - off, y1), M), ((x0 - off + w * 0.22, y + h * 0.28), C), ((x0 - off + w * 0.22, y - h * 0.28), C), ((x0 - off, y0), C)])
            ax.add_patch(PathPatch(p2, fc="none", ec=ink, lw=lw, zorder=3))
        yy = [y + h * 0.25, y - h * 0.25]
        for yi in yy:
            xb = (x0 + w * 0.10) if base != "AND" else x0     # where the input wire meets the body
            xs = x0 - pin - (w * 0.10 if kind in ("XOR", "XNOR") else 0)
            ax.plot([xs, xb], [yi, yi], color=ink, lw=lw, zorder=2)
            ins.append((xs, yi))
        if kind in ("NAND", "NOR", "XNOR"):
            r = bubble
            ax.add_patch(Circle((x1 + r, y), r, fc="white", ec=ink, lw=lw, zorder=4))
            end = x1 + 2 * r
    out_end = end + pin
    ax.plot([end, out_end], [y, y], color=ink, lw=lw, zorder=2)
    return {"in": ins, "out": (out_end, y)}
