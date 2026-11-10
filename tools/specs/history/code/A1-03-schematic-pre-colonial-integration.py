from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(6.0, 9.5, "Forces of Integration in the Nigeria Area prior to 1800",
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Simplified Nigeria sketch polygon
    # Real Nigeria lat/long ~ 3-15 E, 4-14 N, mapped roughly to schematic box x in [3.2, 8.8], y in [1.8, 7.8]
    poly_pts = [
        [3.8, 4.0], [3.5, 5.5], [4.0, 7.2], [5.5, 7.6],
        [8.0, 7.8], [8.6, 7.2], [8.2, 5.8], [8.6, 4.5],
        [7.5, 2.5], [6.0, 2.2], [4.5, 2.4]
    ]
    nigeria_shape = Polygon(poly_pts, closed=True, fc=CREAM, ec=DEEP["blue"], lw=2.5, zorder=1)
    ax.add_patch(nigeria_shape)

    # Region Labels on Map
    ax.text(6.0, 7.1, "NORTHERN SAVANNA", ha="center", va="center", fontsize=14, color=GREY, weight="bold", zorder=2)
    ax.text(6.0, 2.8, "SOUTHERN FOREST & COAST", ha="center", va="center", fontsize=14, color=GREY, weight="bold", zorder=2)

    # North to South trade arrow (left side)
    ax.annotate("", xy=(4.6, 3.2), xytext=(4.6, 6.7),
                arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["orange"], lw=4.5), zorder=3)
    ax.text(4.4, 5.0, "Cattle, Leather, Natron, Horses\n(North to South Trade)",
            ha="right", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["orange"], lw=1.5), zorder=4)

    # South to North trade arrow (right side)
    ax.annotate("", xy=(7.4, 6.7), xytext=(7.4, 3.2),
                arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["green"], lw=4.5), zorder=3)
    ax.text(7.6, 5.0, "Kola nut, Palm oil, Ivory\n(South to North Trade)",
            ha="left", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["green"], lw=1.5), zorder=4)

    # Integration Force 1: Islam / Crescent Moon (Upper/North-East)
    cx, cy = 6.8, 8.2
    # Crescent moon icon
    ax.scatter(cx, cy, s=450, color=DEEP["blue"], zorder=5)
    ax.scatter(cx + 0.1, cy + 0.1, s=400, color="white", zorder=6)
    ax.text(cx + 0.45, cy, "Spread of Islam via trade routes",
            ha="left", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc=BLUE, ec=DEEP["blue"], lw=1.2), zorder=7)

    # Integration Force 2: Intermarriage / Handshake icon (Central Transition Zone / Borderlands)
    bx, by = 6.0, 5.0
    # Two stylized hands clasping
    ax.plot([bx - 0.25, bx - 0.05], [by - 0.08, by + 0.08], lw=4, color=DEEP["pink"], zorder=5)
    ax.plot([bx + 0.25, bx + 0.05], [by + 0.08, by - 0.08], lw=4, color=DEEP["pink"], zorder=5)
    ax.plot([bx - 0.1, bx + 0.1], [by, by], lw=5, color=DEEP["pink"], zorder=5)
    ax.text(bx, by - 0.45, "Intermarriage at borderlands",
            ha="center", va="top", fontsize=14, color=INK, weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc=PINK, ec=DEEP["pink"], lw=1.2), zorder=7)

    # Integration Force 3: Imperial Expansion / Crossed Swords (South-West: Oyo, Benin)
    sx, sy = 5.0, 1.8
    # Crossed swords icon
    ax.plot([sx - 0.2, sx + 0.2], [sy - 0.2, sy + 0.2], color=DEEP["lav"], lw=3.5, zorder=5)
    ax.plot([sx - 0.2, sx + 0.2], [sy + 0.2, sy - 0.2], color=DEEP["lav"], lw=3.5, zorder=5)
    ax.plot([sx - 0.15, sx - 0.05], [sy - 0.05, sy - 0.15], color=INK, lw=2, zorder=6)
    ax.plot([sx - 0.15, sx - 0.05], [sy + 0.05, sy + 0.15], color=INK, lw=2, zorder=6)
    ax.text(sx + 0.4, sy, "Imperial Expansion (e.g., Oyo, Benin)",
            ha="left", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc=LAV, ec=DEEP["lav"], lw=1.2), zorder=7)

    # Schematic caption
    ax.text(6.0, 0.6, "Sketch map: zones are approximate",
            ha="center", va="center", fontsize=14, color=GREY, style="italic")

    save(fig, out)
