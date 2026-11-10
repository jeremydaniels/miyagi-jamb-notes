from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Draw sea/ocean background
    ocean = plt.Rectangle((0.5, 0.5), 9, 6, fc='#EAF2F8', ec=GREY, lw=1.5, zorder=1)
    ax.add_patch(ocean)

    # Simplified landmass polygon (schematic continent/peninsula)
    land_pts = np.array([
        [1.8, 0.5],
        [1.8, 1.8],
        [2.3, 3.2],
        [2.0, 4.5],
        [2.8, 5.8],
        [4.2, 6.5],
        [6.0, 6.5],
        [7.5, 6.0],
        [8.2, 5.0],
        [8.0, 3.8],
        [7.4, 2.5],
        [8.2, 1.2],
        [7.8, 0.5]
    ])
    land = Polygon(land_pts, closed=True, fc='#FCF9EE', ec=DEEP['green'], lw=2, zorder=2)
    ax.add_patch(land)

    # Annotate Land and Sea
    ax.text(5.0, 5.5, "LANDMASS", fontsize=15, fontweight='bold', color=INK, ha='center', zorder=3, alpha=0.7)
    ax.text(1.1, 5.5, "SEA", fontsize=14, fontweight='bold', color=DEEP['blue'], ha='center', zorder=3, alpha=0.8)
    ax.text(8.8, 5.5, "SEA", fontsize=14, fontweight='bold', color=DEEP['blue'], ha='center', zorder=3, alpha=0.8)

    # Map frame / border lines clip
    x = np.linspace(0.5, 9.5, 200)

    # 4 Isotherms with typical thermal contrast (bending poleward/equatorward over land)
    # Curves: 24°C, 26°C, 28°C, 30°C from north to south
    isotherms = [
        ("24°C", 4.8, 0.45, DEEP['blue']),
        ("26°C", 3.7, 0.60, DEEP['green']),
        ("28°C", 2.6, 0.70, DEEP['orange']),
        ("30°C", 1.4, 0.65, DEEP['pink'])
    ]

    for label, base_y, amp, col in isotherms:
        # Wavy isotherm curving over landmass
        # Land warms up more than sea in summer, displacing isotherms poleward (upward)
        y = base_y + amp * np.exp(-((x - 5.0) / 1.8)**2) + 0.15 * np.sin(x * 1.5)
        ax.plot(x, y, color=col, lw=2.5, zorder=4)

        # Place label with clean white background bbox
        label_x = 4.8
        label_y = base_y + amp * np.exp(-((label_x - 5.0) / 1.8)**2) + 0.15 * np.sin(label_x * 1.5)
        ax.text(label_x, label_y, f" {label} ", fontsize=14, fontweight='bold', color=col,
                ha='center', va='center', zorder=5,
                bbox=dict(fc='white', ec=col, boxstyle='round,pad=0.25', lw=1.2))

    # Title & Caption
    ax.text(5.0, 6.75, "Isotherm Map (Lines of Equal Temperature)", fontsize=16, fontweight='bold', color=INK, ha='center')
    ax.text(5.0, 0.2, "Sketch map: isotherms bend due to differential heating of land and sea",
            fontsize=14, color=INK, ha='center', style='italic')

    save(fig, out)
