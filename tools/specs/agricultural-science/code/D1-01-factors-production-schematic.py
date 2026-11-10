from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Center circle for "Agricultural Production"
    r_center = 1.6
    center_circle = plt.Circle((0, 0), r_center, facecolor=CREAM, edgecolor=INK, lw=2.5, zorder=5)
    ax.add_patch(center_circle)

    # 4 Quadrant puzzle blocks (rounded square sector tiles)
    # Positions of quadrants:
    # Top-Left: (-2.6, 2.6) -> Green
    # Top-Right: (2.6, 2.6) -> Orange
    # Bottom-Left: (-2.6, -2.6) -> Blue
    # Bottom-Right: (2.6, -2.6) -> Lavender / Purple

    gap = 0.15
    box_w = 4.8
    box_h = 4.8

    # Draw 4 curved/rounded cards meeting near the center circle
    pieces_data = [
        # Top-Left
        {
            "rect": [-box_w, gap, box_w - gap, box_h - gap],
            "face": GREEN,
            "edge": DEEP["green"],
            "title": "Land",
            "desc": "(Nature's gifts,\nsoil, water)",
            "text_pos": (-2.5, 2.7)
        },
        # Top-Right
        {
            "rect": [gap, gap, box_w - gap, box_h - gap],
            "face": ORANGE,
            "edge": DEEP["orange"],
            "title": "Labour",
            "desc": "(Human effort,\nworkers)",
            "text_pos": (2.5, 2.7)
        },
        # Bottom-Left
        {
            "rect": [-box_w, -box_h, box_w - gap, box_h - gap],
            "face": BLUE,
            "edge": DEEP["blue"],
            "title": "Capital",
            "desc": "(Money, machines,\ntools)",
            "text_pos": (-2.5, -2.7)
        },
        # Bottom-Right
        {
            "rect": [gap, -box_h, box_w - gap, box_h - gap],
            "face": LAV,
            "edge": DEEP["lav"],
            "title": "Management",
            "desc": "(The Farm Manager,\nplanning, control)",
            "text_pos": (2.5, -2.7)
        }
    ]

    for p in pieces_data:
        x, y, w, h = p["rect"]
        # FancyBboxPatch draws a rounded rectangle
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                             facecolor=p["face"], edgecolor=p["edge"], lw=3, zorder=2)
        ax.add_patch(box)

        # Labels
        ax.text(p["text_pos"][0], p["text_pos"][1] + 0.35, p["title"],
                ha="center", va="center", fontsize=17, fontweight="bold", color=INK, zorder=6)
        ax.text(p["text_pos"][0], p["text_pos"][1] - 0.45, p["desc"],
                ha="center", va="center", fontsize=14, color=INK, zorder=6, linespacing=1.3)

    # Inward arrows from pieces pointing towards the central circle
    arrow_props = dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20)
    coords = [
        ((-1.5, 1.5), (-1.15, 1.15)),
        ((1.5, 1.5), (1.15, 1.15)),
        ((-1.5, -1.5), (-1.15, -1.15)),
        ((1.5, -1.5), (1.15, -1.15))
    ]
    for start, end in coords:
        ax.annotate("", xy=end, xytext=start, arrowprops=arrow_props, zorder=6)

    # Re-draw center circle outline on top for crisp boundary
    ax.add_patch(plt.Circle((0, 0), r_center, facecolor=CREAM, edgecolor=INK, lw=3, zorder=7))

    # Center circle text
    ax.text(0, 0.25, "Agricultural", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK, zorder=8)
    ax.text(0, -0.3, "Production", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK, zorder=8)

    save(fig, out)
