from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 6)
    ax = fig.add_subplot(111)

    # Coordinate ranges
    x_min, x_max = -4.5, 4.5
    y_min, y_max = -1.5, 11.0

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Draw coordinate axes with arrows
    arrow_props = dict(arrowstyle="-|>", color=INK, lw=1.8, mutation_scale=15)
    ax.annotate("", xy=(x_max, 0), xytext=(x_min, 0), arrowprops=arrow_props)
    ax.annotate("", xy=(0, y_max), xytext=(0, y_min), arrowprops=arrow_props)

    # Axis labels
    ax.text(x_max - 0.2, -0.7, "x", fontsize=16, color=INK, ha='center', va='center')
    ax.text(-0.4, y_max - 0.4, "y", fontsize=16, color=INK, ha='center', va='center')

    # Parabola data
    x_arch = np.linspace(-3, 3, 200)
    y_arch = 9 - x_arch**2

    # Shaded region between curve and x-axis
    ax.fill_between(x_arch, 0, y_arch, color=BLUE, alpha=0.55, zorder=2)

    # Parabola curve extending slightly beyond intercepts for context
    x_full = np.linspace(-3.25, 3.25, 300)
    y_full = 9 - x_full**2
    ax.plot(x_full, y_full, color=DEEP["blue"], lw=3.0, zorder=3)

    # Tick marks and labels for -3 and 3
    tick_len = 0.25
    ax.plot([-3, -3], [-tick_len, tick_len], color=INK, lw=1.8, zorder=4)
    ax.plot([3, 3], [-tick_len, tick_len], color=INK, lw=1.8, zorder=4)

    ax.text(-3, -0.7, "-3", fontsize=16, color=INK, ha='center', va='center')
    ax.text(3, -0.7, "3", fontsize=16, color=INK, ha='center', va='center')

    # Origin label
    ax.text(-0.35, -0.6, "0", fontsize=15, color=GREY, ha='center', va='center')

    # Peak value tick/label (optional but helpful context for y = 9)
    ax.plot([-tick_len, tick_len], [9, 9], color=INK, lw=1.5, zorder=4)
    ax.text(-0.45, 9, "9", fontsize=15, color=INK, ha='right', va='center')

    # "Area" label inside the shaded region
    ax.text(0, 4.0, "Area", fontsize=18, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.85), zorder=5)

    # Curve equation label
    ax.text(1.7, 8.0, "y = 9 - x²", fontsize=16, color=DEEP["blue"], ha='left', va='center',
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1.0), zorder=5)

    save(fig, out)
