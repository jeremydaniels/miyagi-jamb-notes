from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(5, 6.5, "Redemption Road — Character Map", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Coordinates
    bendu_pos = np.array([3.8, 3.5])
    cobra_pos = np.array([8.2, 3.5])
    
    # Branches for characters to be confirmed (dashed circles)
    branches = [
        np.array([1.5, 5.3]),
        np.array([1.2, 3.5]),
        np.array([1.8, 1.7]),
        np.array([4.2, 1.4]),
        np.array([3.8, 5.6])
    ]

    r_main = 1.05
    r_branch = 0.65

    # Connectors to dashed circles
    for pos in branches:
        ax.plot([bendu_pos[0], pos[0]], [bendu_pos[1], pos[1]], 
                color=GREY, lw=2, linestyle="--", zorder=1)

    # Arrow from Bendu to Commander Cobra
    arrow_start = bendu_pos + np.array([r_main, 0])
    arrow_end = cobra_pos - np.array([r_main, 0])
    ax.annotate("", xy=arrow_end, xytext=arrow_start,
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3, mutation_scale=20),
                zorder=2)
    
    # Label on arrow
    ax.text((arrow_start[0] + arrow_end[0]) / 2, 3.8, "conflict / pursuit",
            ha="center", va="bottom", fontsize=14, color=DEEP["pink"],
            bbox=dict(fc="white", ec="none", pad=2))

    # Bendu Lewis (protagonist) - Central solid circle
    bendu_circle = patches.Circle(bendu_pos, r_main, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(bendu_circle)
    ax.text(bendu_pos[0], bendu_pos[1] + 0.15, "Bendu Lewis",
            ha="center", va="center", fontsize=15, weight="bold", color=INK, zorder=4)
    ax.text(bendu_pos[0], bendu_pos[1] - 0.25, "(protagonist)",
            ha="center", va="center", fontsize=14, style="italic", color=INK, zorder=4)

    # Commander Cobra (antagonist) - Dark circle
    cobra_circle = patches.Circle(cobra_pos, r_main, facecolor=GREY, edgecolor=INK, lw=2.5, zorder=3)
    ax.add_patch(cobra_circle)
    ax.text(cobra_pos[0], cobra_pos[1] + 0.15, "Commander\nCobra",
            ha="center", va="center", fontsize=15, weight="bold", color="white", zorder=4)
    ax.text(cobra_pos[0], cobra_pos[1] - 0.45, "(antagonist)",
            ha="center", va="center", fontsize=14, style="italic", color="white", zorder=4)

    # Dashed circles for unconfirmed characters
    for i, pos in enumerate(branches):
        c = patches.Circle(pos, r_branch, facecolor="white", edgecolor=DEEP["lav"], 
                           lw=2, linestyle="--", zorder=3)
        ax.add_patch(c)
        ax.text(pos[0], pos[1], "?", ha="center", va="center", 
                fontsize=16, color=DEEP["lav"], weight="bold", zorder=4)

    # Note / Legend
    ax.text(1.2, 0.4, "* Dashed circles represent characters still to be confirmed", 
            ha="left", va="center", fontsize=14, style="italic", color=INK)

    save(fig, out)
