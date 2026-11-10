from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Earth dimensions (flattened cross-section)
    a = 3.8  # semi-major axis (equatorial radius)
    b = 2.7  # semi-minor axis (polar radius)

    # Shaded cross-section of Earth
    earth = Ellipse((0, 0), width=2 * a, height=2 * b, facecolor=CREAM, edgecolor=DEEP["blue"], lw=3, zorder=2)
    ax.add_patch(earth)

    # Dashed reference lines only through the interior/opposite quadrants (kept away from outer labels)
    ax.plot([-a, 0], [0, 0], color=GREY, linestyle="--", lw=1.5, zorder=3)
    ax.plot([0, 0], [-b, 0], color=GREY, linestyle="--", lw=1.5, zorder=3)

    # Polar radius arrow: from centre to North Pole
    ax.annotate("", xy=(0, b), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.5, mutation_scale=22),
                zorder=4)

    # Equatorial radius arrow: from centre to Equator (pointing right)
    ax.annotate("", xy=(a, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3.5, mutation_scale=22),
                zorder=4)

    # Centre dot and label
    ax.plot(0, 0, marker="o", markersize=7, color=INK, zorder=5)
    ax.text(-0.25, -0.3, "Centre", ha="right", va="top", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5), zorder=5)

    # Geographic reference labels outside the ellipse
    ax.text(0, b + 0.25, "North Pole", ha="center", va="bottom", fontsize=15, color=INK, weight="bold")
    ax.text(0, -b - 0.25, "South Pole", ha="center", va="top", fontsize=14, color=GREY)
    ax.text(-a - 0.2, 0, "Equator", ha="right", va="center", fontsize=14, color=GREY)

    # Pointer annotation for Polar radius placed clearly in top-left space outside the earth
    ax.annotate("Polar radius (shorter) -> higher g",
                xy=(0, b * 0.55),
                xytext=(-1.5, b + 0.8),
                fontsize=14, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0),
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.4", lw=1.5),
                zorder=6)

    # Pointer annotation for Equatorial radius placed below the axis, completely clear of vertical arrow
    ax.annotate("Equatorial radius (longer) -> lower g",
                xy=(a * 0.55, 0),
                xytext=(a * 0.55, -1.3),
                fontsize=14, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0),
                bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.4", lw=1.5),
                zorder=6)

    # Set appropriate limits to leave generous margin around all annotations
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-3.9, 4.2)

    save(fig, out)
