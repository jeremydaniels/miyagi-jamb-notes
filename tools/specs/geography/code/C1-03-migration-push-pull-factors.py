from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(14, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Title
    ax.text(7.0, 8.0, "Rural–Urban Migration: Push and Pull Factors",
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # ------------------ LEFT SIDE: RURAL VILLAGE (SOURCE) ------------------
    # Container box for Source Area
    source_box = patches.FancyBboxPatch((0.6, 1.0), 4.2, 6.5, boxstyle="round,pad=0.2",
                                        facecolor=CREAM, edgecolor=GREY, lw=1.5, alpha=0.5)
    ax.add_patch(source_box)

    ax.text(2.7, 7.15, "Source: Rural Area", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # Rural illustration: rolling hills & huts
    # Hill 1
    h1 = patches.Ellipse((2.0, 5.0), 3.2, 1.4, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    ax.add_patch(h1)
    # Hill 2
    h2 = patches.Ellipse((3.4, 4.9), 2.8, 1.2, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    ax.add_patch(h2)

    # Village Hut 1
    ax.add_patch(patches.Rectangle((1.5, 4.7), 0.8, 0.6, facecolor="white", edgecolor=INK, lw=1.5))
    ax.add_patch(patches.Polygon([[1.35, 5.3], [1.9, 5.8], [2.45, 5.3]], closed=True,
                                 facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5))
    # Hut 1 door
    ax.add_patch(patches.Rectangle((1.8, 4.7), 0.2, 0.35, facecolor=INK))

    # Village Hut 2
    ax.add_patch(patches.Rectangle((2.8, 4.6), 0.7, 0.55, facecolor="white", edgecolor=INK, lw=1.5))
    ax.add_patch(patches.Polygon([[2.65, 5.15], [3.15, 5.6], [3.65, 5.15]], closed=True,
                                 facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5))
    # Hut 2 door
    ax.add_patch(patches.Rectangle((3.05, 4.6), 0.2, 0.3, facecolor=INK))

    # Tree
    ax.add_patch(patches.Rectangle((3.8, 4.8), 0.12, 0.4, facecolor=INK))
    ax.add_patch(patches.Circle((3.86, 5.3), 0.35, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5))

    # Push Factors Header
    ax.text(2.7, 4.0, "PUSH FACTORS", ha="center", va="center",
            fontsize=15, fontweight="bold", color=DEEP["pink"])

    # Push Factors with outward arrows
    push_items = [
        "Poverty",
        "Lack of jobs",
        "Poor amenities",
        "Soil exhaustion"
    ]
    y_starts = [3.35, 2.65, 1.95, 1.25]
    for text, y in zip(push_items, y_starts):
        # Text box
        ax.text(2.1, y, text, ha="center", va="center", fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=GREY, lw=1.2))
        # Arrow pointing outward to the right
        ax.annotate("", xy=(4.5, y), xytext=(3.4, y),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=16))

    # ------------------ CENTER: MIGRATION FLOW ------------------
    # Large arrow representing migration
    mig_arrow = patches.FancyArrow(5.2, 4.25, 2.8, 0, width=0.45,
                                  head_width=0.9, head_length=0.7,
                                  length_includes_head=True,
                                  facecolor=BLUE, edgecolor=DEEP["blue"], lw=2)
    ax.add_patch(mig_arrow)
    ax.text(6.3, 4.25, "MIGRATION", ha="center", va="center",
            fontsize=15, fontweight="bold", color="white")

    # Flow label / explanation
    ax.text(6.6, 3.4, "Movement of\npeople", ha="center", va="center",
            fontsize=14, style="italic", color=INK)

    # ------------------ RIGHT SIDE: CITY SKYLINE (DESTINATION) ------------------
    # Container box for Destination Area
    dest_box = patches.FancyBboxPatch((9.2, 1.0), 4.2, 6.5, boxstyle="round,pad=0.2",
                                       facecolor=CREAM, edgecolor=GREY, lw=1.5, alpha=0.5)
    ax.add_patch(dest_box)

    ax.text(11.3, 7.15, "Destination: Urban Area", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # Modern city skyline illustration
    buildings = [
        (9.8, 4.6, 0.6, 1.1),
        (10.5, 4.6, 0.7, 1.5),
        (11.3, 4.6, 0.65, 1.8),
        (12.05, 4.6, 0.8, 1.3),
    ]
    for bx, by, bw, bh in buildings:
        ax.add_patch(patches.Rectangle((bx, by), bw, bh, facecolor=LAV, edgecolor=DEEP["lav"], lw=1.5))
        # Add windows
        for wx in np.linspace(bx + 0.12, bx + bw - 0.15, max(2, int(bw * 3))):
            for wy in np.linspace(by + 0.2, by + bh - 0.2, max(2, int(bh * 2))):
                ax.add_patch(patches.Rectangle((wx, wy), 0.08, 0.08, facecolor="white", edgecolor=DEEP["lav"], lw=0.6))

    # Pull Factors Header
    ax.text(11.3, 4.0, "PULL FACTORS", ha="center", va="center",
            fontsize=15, fontweight="bold", color=DEEP["blue"])

    # Pull Factors with inward arrows
    pull_items = [
        "Jobs & opportunities",
        "Electricity & water",
        "Hospitals & schools",
        "Higher wages"
    ]
    for text, y in zip(pull_items, y_starts):
        # Arrow pointing inward from left
        ax.annotate("", xy=(10.0, y), xytext=(8.9, y),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.5, mutation_scale=16))
        # Text box
        ax.text(11.6, y, text, ha="center", va="center", fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=GREY, lw=1.2))

    save(fig, out)
