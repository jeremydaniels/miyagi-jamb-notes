from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(5.0, 6.4, "Levels of Changing Evil (Hadith 34)", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(5.0, 5.95, '"Whoever among you sees an evil, let him change it..."', 
            ha="center", va="center", fontsize=14, style="italic", color=INK)

    # 3-step staircase / pyramid tiers (from bottom to top)
    # Step 3 (Bottom): Widest base
    rect3 = patches.Rectangle((1.0, 1.0), 8.0, 1.3, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5, zorder=2)
    ax.add_patch(rect3)
    ax.text(5.0, 1.65, "3. With the Heart (Hating it - Weakest of Faith)", 
            ha="center", va="center", fontsize=14.5, weight="bold", color=INK, zorder=3)

    # Step 2 (Middle): Medium width
    rect2 = patches.Rectangle((1.5, 2.3), 7.0, 1.3, facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5, zorder=2)
    ax.add_patch(rect2)
    ax.text(5.0, 2.95, "2. With the Tongue (Speaking out)", 
            ha="center", va="center", fontsize=14.5, weight="bold", color=INK, zorder=3)

    # Step 1 (Top): Narrowest, highest level
    rect1 = patches.Rectangle((2.0, 3.6), 6.0, 1.3, facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5, zorder=2)
    ax.add_patch(rect1)
    ax.text(5.0, 4.25, "1. With the Hand (Action/Authority)", 
            ha="center", va="center", fontsize=14.5, weight="bold", color=INK, zorder=3)

    # Side indicator arrow showing progression / level of faith & capability
    arrow = patches.FancyArrow(0.7, 1.0, 0, 3.8, width=0.08, head_width=0.3, head_length=0.35, 
                               length_includes_head=True, facecolor=DEEP["blue"], edgecolor=DEEP["blue"], zorder=4)
    ax.add_patch(arrow)

    ax.text(0.3, 2.9, "Degree of Ability & Direct Impact", 
            ha="center", va="center", fontsize=14, color=DEEP["blue"], weight="bold", rotation=90)

    save(fig, out)
