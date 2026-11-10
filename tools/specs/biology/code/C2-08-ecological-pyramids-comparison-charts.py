import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(18, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Levels from bottom to top
    # y positions for 4 tiers:
    # tier 0 (producers): y = 1.3 to 2.5 (h=1.2)
    # tier 1 (primary consumers): y = 2.7 to 3.9
    # tier 2 (secondary consumers): y = 4.1 to 5.3
    # tier 3 (tertiary consumers): y = 5.5 to 6.7
    tier_y = [1.3, 2.7, 4.1, 5.5]
    h = 1.15

    # Colors for tiers: soft greens, yellows, oranges
    colors = [GREEN, CREAM, ORANGE, PINK]
    edge_colors = [DEEP["green"], DEEP["orange"], DEEP["orange"], DEEP["pink"]]

    # Common trophic level titles on the far left or shared
    # 3 Pyramids centered at x = 3.0, x = 8.8, x = 14.5
    centers = [3.3, 8.8, 14.4]

    # --- Titles ---
    ax.text(centers[0], 7.8, "pyramid of numbers (upright)", ha="center", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(centers[1], 7.8, "pyramid of numbers (inverted: one tree)", ha="center", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(centers[2], 7.8, "pyramid of energy (always upright)", ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # --- Pyramid 1: Upright numbers ---
    # Widths: Hawk, Lizards, Grasshoppers, Grass
    p1_widths = [4.8, 3.6, 2.4, 1.2] # bottom to top
    p1_labels = [
        "grass\n(producers)",
        "grasshoppers\n(primary consumers)",
        "lizards\n(secondary consumers)",
        "hawk\n(tertiary consumers)"
    ]

    for i in range(4):
        w = p1_widths[i]
        x = centers[0] - w / 2
        y = tier_y[i]
        rect = patches.Rectangle((x, y), w, h, facecolor=colors[i], edgecolor=edge_colors[i], linewidth=2, zorder=2)
        ax.add_patch(rect)
        ax.text(centers[0], y + h / 2, p1_labels[i], ha="center", va="center", fontsize=14, color=INK, zorder=3)

    # --- Pyramid 2: Inverted numbers (one tree) ---
    # Widths: Tree (narrow), Caterpillars (very wide), Birds (narrower), Hawks (very narrow)
    p2_widths = [1.0, 4.6, 2.8, 1.4]
    p2_labels = [
        "one tree\n(producers)",
        "many caterpillars\n(primary consumers)",
        "fewer birds\n(secondary consumers)",
        "fewer hawks\n(tertiary consumers)"
    ]

    for i in range(4):
        w = p2_widths[i]
        x = centers[1] - w / 2
        y = tier_y[i]
        rect = patches.Rectangle((x, y), w, h, facecolor=colors[i], edgecolor=edge_colors[i], linewidth=2, zorder=2)
        ax.add_patch(rect)
        
        # In tier 0, draw a little tree icon next to text
        if i == 0:
            ax.text(centers[1] + 0.1, y + h / 2, p2_labels[i], ha="center", va="center", fontsize=14, color=INK, zorder=3)
            # Tree trunk & foliage icon to the left inside/beside box
            tx = centers[1] - 1.1
            ty = y + 0.2
            # trunk
            ax.add_patch(patches.Rectangle((tx - 0.05, ty), 0.1, 0.35, facecolor="#8B5A2B", zorder=4))
            # leaves
            ax.add_patch(patches.Circle((tx, ty + 0.5), 0.25, facecolor=DEEP["green"], zorder=5))
        else:
            ax.text(centers[1], y + h / 2, p2_labels[i], ha="center", va="center", fontsize=14, color=INK, zorder=3)

    # --- Pyramid 3: Upright energy (ten times narrower per level) ---
    # Widths: 10,000 kJ (widest), 1,000 kJ, 100 kJ, 10 kJ
    p3_widths = [4.8, 3.4, 2.0, 0.8]
    p3_energy_text = ["10,000 kJ", "1,000 kJ", "100 kJ", "10 kJ"]
    p3_role_text = ["producers", "primary consumers", "secondary consumers", "tertiary consumers"]

    for i in range(4):
        w = p3_widths[i]
        x = centers[2] - w / 2
        y = tier_y[i]
        rect = patches.Rectangle((x, y), w, h, facecolor=colors[i], edgecolor=edge_colors[i], linewidth=2, zorder=2)
        ax.add_patch(rect)
        
        if i == 3: # 10 kJ tier
            ax.text(centers[2], y + h / 2, "10 kJ", ha="center", va="center", fontsize=14, color=INK, zorder=3)
            ax.text(centers[2] - 0.7, y + h / 2, "tertiary consumers", ha="right", va="center", fontsize=14, color=INK,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8))
        else:
            ax.text(centers[2], y + h / 2, f"{p3_energy_text[i]}\n({p3_role_text[i]})", ha="center", va="center", fontsize=14, color=INK, zorder=3)

        # Curved arrow showing heat lost at each level
        # Arrow starts from right edge of rect, curves up-right
        rx = x + w
        ry = y + h / 2
        arrow_end_x = rx + 0.75
        arrow_end_y = ry + 0.3
        
        ax.annotate(
            "",
            xy=(arrow_end_x, arrow_end_y),
            xytext=(rx, ry),
            arrowprops=dict(
                arrowstyle="-|>",
                color=DEEP["orange"],
                connectionstyle="arc3,rad=-0.3",
                lw=2,
                mutation_scale=12
            ),
            zorder=4
        )
        # Heat lost text
        ax.text(arrow_end_x + 0.1, arrow_end_y, "heat lost", ha="left", va="center", fontsize=14, color=DEEP["orange"], style="italic", zorder=4)

    save(fig, out)
