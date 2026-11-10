from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 6)
    ax = fig.add_subplot(111)
    
    # Hide standard spines
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # Limits
    xmin, xmax = 0.5, 4.5
    ymin, ymax = -1.0, 3.5
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Draw horizontal x-axis line with arrow
    ax.annotate(
        "", xy=(4.3, 0), xytext=(0.7, 0),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, mutation_scale=15)
    )
    # Axis label "x"
    ax.text(4.4, 0, "x", color=INK, fontsize=16, va="center", ha="left", style="italic")

    # Parabola functions: y = x^2 - 5x + 6
    # Left branch: x <= 2
    x_left = np.linspace(0.8, 2.0, 100)
    y_left = x_left**2 - 5*x_left + 6

    # Bottom portion (between roots): 2 <= x <= 3
    x_mid = np.linspace(2.0, 3.0, 100)
    y_mid = x_mid**2 - 5*x_mid + 6

    # Right branch: x >= 3
    x_right = np.linspace(3.0, 4.2, 100)
    y_right = x_right**2 - 5*x_right + 6

    # The sections rising above the x-axis are drawn with a thick solid line
    ax.plot(x_left, y_left, color=DEEP["blue"], lw=3.8)
    ax.plot(x_right, y_right, color=DEEP["blue"], lw=3.8)

    # The section below the x-axis (standard/thinner solid line to complete the U-shape parabola)
    ax.plot(x_mid, y_mid, color=DEEP["blue"], lw=2.0, linestyle="--")

    # Intersection points (roots at 2 and 3)
    ax.plot([2, 3], [0, 0], 'o', color=INK, markersize=5.5)

    # Labels for roots "2" and "3"
    ax.text(2.0, -0.25, "2", fontsize=16, ha="center", va="top", color=INK)
    ax.text(3.0, -0.25, "3", fontsize=16, ha="center", va="top", color=INK)

    # Plus signs indicating positive regions above the x-axis
    ax.text(1.4, 0.45, "+", fontsize=18, fontweight="bold", ha="center", va="center", color=DEEP["green"])
    ax.text(3.6, 0.45, "+", fontsize=18, fontweight="bold", ha="center", va="center", color=DEEP["green"])

    # Label: "y = x^2 - 5x + 6"
    ax.text(
        3.7, 2.6, r"$y = x^2 - 5x + 6$",
        fontsize=16, color=INK, ha="center", va="bottom",
        bbox=dict(fc="white", ec="none", pad=2)
    )

    save(fig, out)
