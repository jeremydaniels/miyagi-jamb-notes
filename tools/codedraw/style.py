"""Shared look for code-drawn images (matplotlib): same fonts and soft palette as the AI images."""
import os
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


def save(fig, path):
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
