from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8.5, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.8, 7.2)
    ax.set_ylim(-0.8, 8.2)

    # Title
    ax.text(3.5, 8.0, "Sample Space of Two Dice", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Headers for First Die and Second Die
    ax.text(3.5, 7.7, "First Die", fontsize=15, fontweight="bold", ha="center", va="center", color=DEEP["blue"])
    ax.text(-1.1, 3.5, "Second Die", fontsize=15, fontweight="bold", ha="center", va="center", rotation=90, color=DEEP["orange"])

    # Draw cells
    for r in range(1, 7):      # Second die (rows 1 to 6, mapped vertically: 1 at top, 6 at bottom)
        y = 7 - r              # row 1 -> y=6, row 6 -> y=1
        for c in range(1, 7):  # First die (cols 1 to 6, x = 1 to 6)
            x = c
            
            # Diagonal cells where first die == second die (c == r)
            if c == r:
                rect = patches.Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor=CREAM, edgecolor=GREY, linewidth=1.2)
                ax.add_patch(rect)
                text_color = DEEP["orange"]
                fontweight = "bold"
            else:
                rect = patches.Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor="white", edgecolor=GREY, linewidth=1.0)
                ax.add_patch(rect)
                text_color = INK
                fontweight = "normal"
            
            # Outcome label
            ax.text(x, y, f"({c},{r})", fontsize=14, ha="center", va="center", color=text_color, fontweight=fontweight)

    # Column headers (First die values 1 to 6)
    for c in range(1, 7):
        rect = patches.Rectangle((c - 0.5, 6.5), 1, 0.8, facecolor=BLUE, edgecolor=GREY, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(c, 6.9, str(c), fontsize=15, fontweight="bold", ha="center", va="center", color=INK)

    # Row headers (Second die values 1 to 6)
    for r in range(1, 7):
        y = 7 - r
        rect = patches.Rectangle((-0.3, y - 0.5), 0.8, 1, facecolor=ORANGE, edgecolor=GREY, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(0.1, y, str(r), fontsize=15, fontweight="bold", ha="center", va="center", color=INK)

    # Outer border around grid
    outer_border = patches.Rectangle((0.5, 0.5), 6, 6, fill=False, edgecolor=INK, linewidth=2.0)
    ax.add_patch(outer_border)

    save(fig, out)
