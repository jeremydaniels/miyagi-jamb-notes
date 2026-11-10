from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Universal set rectangle
    rect = patches.Rectangle((0.6, 0.6), 8.8, 5.8, facecolor="white", edgecolor=INK, linewidth=2.5)
    ax.add_patch(rect)

    # Circle positions and size
    r = 2.1
    c_a = (3.8, 3.4)
    c_b = (6.2, 3.4)

    # Filled circles with soft tones
    circ_a = patches.Circle(c_a, r, facecolor=BLUE, alpha=0.35, edgecolor=DEEP["blue"], linewidth=2.5)
    circ_b = patches.Circle(c_b, r, facecolor=ORANGE, alpha=0.35, edgecolor=DEEP["orange"], linewidth=2.5)
    ax.add_patch(circ_a)
    ax.add_patch(circ_b)

    # Universal set label U
    ax.text(9.0, 6.0, "U", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    # Labels for Set A and Set B above the circles
    ax.text(c_a[0] - 0.7, c_a[1] + r + 0.3, "Set A", fontsize=16, fontweight="bold", color=DEEP["blue"], ha="center", va="center")
    ax.text(c_b[0] + 0.7, c_b[1] + r + 0.3, "Set B", fontsize=16, fontweight="bold", color=DEEP["orange"], ha="center", va="center")

    # Region: Only A / A ∩ B'
    ax.text(2.6, 3.55, "Only A", fontsize=15, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(2.6, 3.1, "A ∩ B'", fontsize=14, color=INK, ha="center", va="center")

    # Region: A ∩ B (intersection)
    ax.text(5.0, 3.55, "A ∩ B", fontsize=15, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(5.0, 3.1, "(both A and B)", fontsize=13, color=INK, ha="center", va="center")

    # Region: Only B / A' ∩ B
    ax.text(7.4, 3.55, "Only B", fontsize=15, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(7.4, 3.1, "A' ∩ B", fontsize=14, color=INK, ha="center", va="center")

    # Region: Outside both circles / (A ∪ B)'
    ax.text(5.0, 1.2, "(A ∪ B)'", fontsize=15, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2))

    save(fig, out)
