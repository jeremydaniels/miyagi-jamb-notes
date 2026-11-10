from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7.2)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    # Dimensions and coordinates
    # Bottom pipe: y from 1.0 to 2.2
    # Left cylinder: x from 1.2 to 2.8 (width 1.6), top at 5.5
    # Right cylinder: x from 5.8 to 8.8 (width 3.0), top at 5.5
    # Horizontal connecting pipe: y from 1.0 to 2.2, x from 2.8 to 5.8

    # Liquid polygon (cross section)
    liquid_pts = [
        (1.2, 3.6),  # left piston bottom-left
        (2.8, 3.6),  # left piston bottom-right
        (2.8, 2.2),  # inner corner left
        (5.8, 2.2),  # inner corner right
        (5.8, 3.6),  # right piston bottom-left
        (8.8, 3.6),  # right piston bottom-right
        (8.8, 1.0),  # bottom right
        (1.2, 1.0),  # bottom left
    ]
    liquid_poly = patches.Polygon(liquid_pts, closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5, zorder=1)
    ax.add_patch(liquid_poly)

    # Dotted horizontal lines in the fluid representing pressure equal throughout
    for y_iso in [1.6, 2.6, 3.1]:
        if y_iso <= 2.2:
            ax.plot([1.3, 8.7], [y_iso, y_iso], color=DEEP['blue'], linestyle=':', lw=2, zorder=2)
        else:
            ax.plot([1.3, 2.7], [y_iso, y_iso], color=DEEP['blue'], linestyle=':', lw=2, zorder=2)
            ax.plot([5.9, 8.7], [y_iso, y_iso], color=DEEP['blue'], linestyle=':', lw=2, zorder=2)

    # Label for equal pressure along dotted lines
    ax.text(5.0, 1.6, "Pressure is equal throughout", color=DEEP['blue'], fontsize=14,
            ha='center', va='center', fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=2.0), zorder=3)

    # Outer wall outline of the container (thick lines)
    ax.plot([1.2, 1.2, 8.8, 8.8], [5.5, 1.0, 1.0, 5.5], color=INK, lw=4, solid_capstyle='round', zorder=4)

    # Inner walls
    ax.plot([2.8, 2.8, 5.8, 5.8], [5.5, 2.2, 2.2, 5.5], color=INK, lw=4, solid_capstyle='round', zorder=4)

    # Pistons
    # Left piston: width 1.6 (from 1.2 to 2.8), thickness 0.6, from y=3.6 to 4.2
    left_piston = patches.Rectangle((1.22, 3.6), 1.56, 0.6, facecolor=GREY, edgecolor=INK, lw=2.5, zorder=3)
    ax.add_patch(left_piston)

    # Right piston: width 3.0 (from 5.8 to 8.8), thickness 0.6, from y=3.6 to 4.2
    right_piston = patches.Rectangle((5.82, 3.6), 2.96, 0.6, facecolor=GREY, edgecolor=INK, lw=2.5, zorder=3)
    ax.add_patch(right_piston)

    # Force F1 arrow (pointing down onto left piston)
    ax.annotate('', xy=(2.0, 4.3), xytext=(2.0, 6.1),
                arrowprops=dict(facecolor=DEEP['pink'], edgecolor=DEEP['pink'], width=3.5, headwidth=11, shrink=0.02),
                zorder=5)

    # Label for Left Piston
    ax.text(2.0, 6.4, "Area A1, Force F1 pointing down", color=INK, fontsize=14, ha='center', va='bottom',
            fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))
    ax.text(2.0, 3.9, "A1", color=INK, fontsize=15, ha='center', va='center', fontweight='bold', zorder=6)

    # Force F2 arrow (pointing up from right piston)
    ax.annotate('', xy=(7.3, 6.1), xytext=(7.3, 4.3),
                arrowprops=dict(facecolor=DEEP['green'], edgecolor=DEEP['green'], width=3.5, headwidth=11, shrink=0.02),
                zorder=5)

    # Label for Right Piston
    ax.text(7.3, 6.4, "Area A2, Force F2 pointing up", color=INK, fontsize=14, ha='center', va='bottom',
            fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))
    ax.text(7.3, 3.9, "A2", color=INK, fontsize=15, ha='center', va='center', fontweight='bold', zorder=6)

    # Formula / principle at the bottom (standard mathtext compatible)
    ax.text(5.0, 0.45, r"$P = \frac{F_1}{A_1} = \frac{F_2}{A_2} \quad \rightarrow \quad F_2 = F_1 \times \frac{A_2}{A_1}$",
            fontsize=15, color=INK, ha='center', va='center',
            bbox=dict(fc=CREAM, ec=GREY, boxstyle='round,pad=0.4'))

    save(fig, out)
