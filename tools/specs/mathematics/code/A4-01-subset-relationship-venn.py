from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(8, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Universal set boundary (rectangle)
    rect = patches.Rectangle(
        (0.8, 0.8), 8.4, 5.9,
        facecolor="#FAFAFA",
        edgecolor=INK,
        linewidth=2,
        zorder=1
    )
    ax.add_patch(rect)

    # Label for Universal Set U
    ax.text(
        1.2, 6.2, "U",
        fontsize=18,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center",
        zorder=5
    )

    # Set B (larger circle)
    circle_b = patches.Circle(
        (5.0, 3.75), radius=2.3,
        facecolor=BLUE,
        edgecolor=DEEP["blue"],
        linewidth=2.5,
        alpha=0.6,
        zorder=2
    )
    ax.add_patch(circle_b)

    # Set A (smaller circle, completely inside B)
    circle_a = patches.Circle(
        (4.3, 3.5), radius=1.2,
        facecolor=PINK,
        edgecolor=DEEP["pink"],
        linewidth=2.5,
        alpha=0.85,
        zorder=3
    )
    ax.add_patch(circle_a)

    # Labels for Set A and Set B
    ax.text(
        4.3, 3.5, "A",
        fontsize=18,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center",
        zorder=5
    )

    ax.text(
        6.3, 4.4, "B",
        fontsize=18,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center",
        zorder=5
    )

    # Annotation explaining relationship A ⊂ B
    ax.text(
        5.0, 1.3, r"$A \subset B$  (A is a proper subset of B)",
        fontsize=16,
        color=INK,
        ha="center",
        va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4", lw=1.2),
        zorder=5
    )

    save(fig, out)
