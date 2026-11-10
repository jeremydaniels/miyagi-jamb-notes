from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Document shape at the top representing "Supreme Constitution"
    # Document dimensions
    doc_w, doc_h = 3.6, 1.4
    doc_x, doc_y = 5.0 - doc_w / 2.0, 6.6

    # Draw document base
    doc_bg = patches.FancyBboxPatch(
        (doc_x, doc_y), doc_w, doc_h,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor=CREAM, edgecolor=DEEP["orange"], linewidth=2.5, zorder=2
    )
    ax.add_patch(doc_bg)

    # Document folded corner / accent lines to look like a constitution document
    ax.plot([doc_x + 0.4, doc_x + doc_w - 0.4], [doc_y + doc_h - 0.3, doc_y + doc_h - 0.3],
            color=DEEP["orange"], lw=2.5, zorder=3)

    ax.text(5.0, doc_y + 0.45, "Supreme Constitution",
            ha="center", va="center", fontsize=16, fontweight="bold", color=INK, zorder=4)

    # Venn Diagram circles
    r = 2.4
    c1_x, c1_y = 3.3, 2.7
    c2_x, c2_y = 6.7, 2.7

    circle_fed = patches.Circle((c1_x, c1_y), r, facecolor=BLUE, alpha=0.35, edgecolor=DEEP["blue"], lw=2.5, zorder=1)
    circle_state = patches.Circle((c2_x, c2_y), r, facecolor=GREEN, alpha=0.35, edgecolor=DEEP["green"], lw=2.5, zorder=1)
    ax.add_patch(circle_fed)
    ax.add_patch(circle_state)

    # Arrows pointing down from Constitution
    ax.annotate("", xy=(3.0, 4.9), xytext=(4.1, doc_y),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["blue"]), zorder=3)
    ax.annotate("", xy=(7.0, 4.9), xytext=(5.9, doc_y),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"]), zorder=3)

    # Text / Labels inside Venn sections
    # Left: Federal Government (Exclusive Powers)
    ax.text(2.3, 2.7, "Federal Government\n(Exclusive Powers)",
            ha="center", va="center", fontsize=14, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none", alpha=0.85), zorder=4)

    # Overlapping center: Concurrent Powers
    ax.text(5.0, 2.7, "Concurrent\nPowers",
            ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=GREY, lw=1.5, alpha=0.92), zorder=5)

    # Right: State Governments (Residual Powers)
    ax.text(7.7, 2.7, "State Governments\n(Residual Powers)",
            ha="center", va="center", fontsize=14, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none", alpha=0.85), zorder=4)

    save(fig, out)
