import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(10, 5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 105)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Metre rule bar
    bar_y = 5.0
    bar_h = 0.4
    ax.add_patch(patches.Rectangle((0, bar_y - bar_h/2), 100, bar_h, fc=CREAM, ec=INK, lw=2, zorder=3))

    # Pivot at 50 cm
    pivot_x = 50
    pivot_y = bar_y - bar_h/2
    ax.add_patch(patches.Polygon([[pivot_x, pivot_y], [pivot_x - 3, pivot_y - 1.5], [pivot_x + 3, pivot_y - 1.5]], 
                                 fc=GREY, ec=INK, lw=2, zorder=2))

    # 50 cm mark
    ax.plot([50, 50], [bar_y - bar_h/2, bar_y + bar_h/2], color=INK, lw=2, zorder=4)
    ax.text(50, bar_y + 0.6, "50 cm", ha='center', va='bottom', fontsize=16, color=INK, fontweight='bold')

    for x_pos, label_cm, weight, color, w_width in [ (30, "30 cm", "60 g", BLUE, 10), (80, "80 cm", "40 g", PINK, 8) ]:
        # Mark on bar
        ax.plot([x_pos, x_pos], [bar_y - bar_h/2, bar_y + bar_h/2], color=INK, lw=2, zorder=4)
        # Position label
        ax.text(x_pos, bar_y + 0.6, label_cm, ha='center', va='bottom', fontsize=16, color=INK, fontweight='bold')
        
        # String
        ax.plot([x_pos, x_pos], [bar_y - bar_h/2, 2.5], color=INK, lw=2, zorder=2)
        
        # Weight
        w_h = 1.5
        ax.add_patch(patches.Rectangle((x_pos - w_width/2, 2.5 - w_h), w_width, w_h, fc=color, ec=INK, lw=2, zorder=3))
        ax.text(x_pos, 2.5 - w_h/2, weight, ha='center', va='center', fontsize=15, color=INK, fontweight='bold', zorder=4)

    # Curved arrows for moments, pointing downward
    # Left downward curving arrow
    arrow_left = patches.FancyArrowPatch(
        (40, 6.0), (25, 3.5),
        connectionstyle="arc3,rad=-0.3",
        color=DEEP['blue'], lw=2.5,
        arrowstyle="simple,head_width=8,head_length=8",
        zorder=5
    )
    ax.add_patch(arrow_left)

    # Right downward curving arrow
    arrow_right = patches.FancyArrowPatch(
        (60, 6.0), (85, 3.5),
        connectionstyle="arc3,rad=0.3",
        color=DEEP['pink'], lw=2.5,
        arrowstyle="simple,head_width=8,head_length=8",
        zorder=5
    )
    ax.add_patch(arrow_right)

    save(fig, out)
