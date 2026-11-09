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
