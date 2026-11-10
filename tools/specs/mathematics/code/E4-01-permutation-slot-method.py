from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(10, 5.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    # Title / Context
    ax.text(
        5, 4.8, "Arranging 5 Students in a Line (Permutations)",
        ha="center", va="center", fontsize=17, fontweight="bold", color=INK
    )

    box_labels = ["1st", "2nd", "3rd", "4th", "5th"]
    choices = ["5", "4", "3", "2", "1"]
    colors = [BLUE, GREEN, ORANGE, PINK, LAV]
    edge_colors = [DEEP["blue"], DEEP["green"], DEEP["orange"], DEEP["pink"], DEEP["lav"]]

    box_w = 1.3
    box_h = 1.3
    spacing = 0.5
    total_w = 5 * box_w + 4 * spacing
    start_x = (10 - total_w) / 2
    box_y = 2.2

    for i in range(5):
        x = start_x + i * (box_w + spacing)

        # Slot label above box
        ax.text(
            x + box_w / 2, box_y + box_h + 0.35,
            f"{box_labels[i]} slot",
            ha="center", va="center", fontsize=15, fontweight="bold", color=INK
        )

        # Box
        rect = patches.FancyBboxPatch(
            (x, box_y), box_w, box_h,
            boxstyle="round,pad=0.04,rounding_size=0.15",
            facecolor=colors[i],
            edgecolor=edge_colors[i],
            linewidth=2.5
        )
        ax.add_patch(rect)

        # Number of choices inside box
        ax.text(
            x + box_w / 2, box_y + box_h / 2,
            choices[i],
            ha="center", va="center", fontsize=24, fontweight="bold", color=INK
        )

        # Multiplication sign between boxes
        if i < 4:
            ax.text(
                x + box_w + spacing / 2, box_y + box_h / 2,
                "×",
                ha="center", va="center", fontsize=22, fontweight="bold", color=GREY
            )

    # Subtitle / description below
    ax.text(
        5, 1.4,
        "Number of choices available for each slot (without repetition)",
        ha="center", va="center", fontsize=14, color=INK, style="italic"
    )

    # Total calculation summary
    ax.text(
        5, 0.7,
        "Total arrangements = 5 × 4 × 3 × 2 × 1 = 5! = 120",
        ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
        bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=GREY, lw=1.2)
    )

    save(fig, out)
