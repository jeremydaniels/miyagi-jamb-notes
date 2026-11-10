from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-1.5, 4.5)
    ax.axis("off")

    # Title
    ax.text(5.5, 4.0, "Progression of Nigerian Constitutions", fontsize=18, weight="bold", color=INK, ha="center")

    # Main timeline axis
    y_line = 2.0
    ax.annotate(
        "",
        xy=(11.0, y_line),
        xytext=(0.0, y_line),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=3, mutation_scale=20)
    )

    milestones = [
        {"year": "1914", "name": "Lugard's\nCouncil", "x": 0.8},
        {"year": "1922", "name": "Clifford", "x": 2.7},
        {"year": "1946", "name": "Richards", "x": 4.8},
        {"year": "1951", "name": "Macpherson", "x": 6.8},
        {"year": "1954", "name": "Lyttelton", "x": 8.7},
        {"year": "1960", "name": "Independence", "x": 10.4},
    ]

    for m in milestones:
        x = m["x"]
        # Node circle
        ax.plot(x, y_line, marker="o", markersize=10, color=DEEP["blue"], zorder=4)
        ax.plot(x, y_line, marker="o", markersize=6, color="white", zorder=5)

        # Year label (above line)
        ax.text(
            x, y_line + 0.35, m["year"],
            fontsize=15, weight="bold", color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=1)
        )

        # Name label (further above)
        ax.text(
            x, y_line + 0.9, m["name"],
            fontsize=14, color=INK, ha="center", va="bottom"
        )

    # Annotation for 1922: Elective Principle & Ballot box
    x_1922 = 2.7
    y_box_top = y_line - 1.2

    # Stem connecting timeline to ballot box
    ax.plot([x_1922, x_1922], [y_line - 0.15, y_box_top + 0.55], color=GREY, lw=1.5, linestyle=":")

    # Ballot Box Drawing
    bw = 0.8
    bh = 0.6
    bx = x_1922 - bw / 2
    by = y_box_top - 0.2

    # Box body
    box = patches.Rectangle((bx, by), bw, bh, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2, zorder=3)
    ax.add_patch(box)

    # Box slot
    slot_w = 0.36
    slot_h = 0.05
    slot = patches.Rectangle((x_1922 - slot_w/2, by + bh - slot_h - 0.04), slot_w, slot_h, facecolor=DEEP["orange"], edgecolor="none", zorder=4)
    ax.add_patch(slot)

    # Ballot paper dropping into slot
    paper = patches.Rectangle((x_1922 - 0.12, by + bh - 0.02), 0.24, 0.28, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.2, zorder=3)
    ax.add_patch(paper)

    # Text below ballot box
    ax.text(
        x_1922, by - 0.35, "Elective Principle\n(Lagos & Calabar)",
        fontsize=14, color=INK, ha="center", va="top",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1)
    )

    save(fig, out)
