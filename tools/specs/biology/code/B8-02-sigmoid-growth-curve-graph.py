import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)

    # Sigmoid curve formulation
    x = np.linspace(0, 10, 300)
    # Standard logistic function scaled: L / (1 + exp(-k*(x-x0)))
    L = 8.5
    k = 1.0
    x0 = 4.5
    y = L / (1 + np.exp(-k * (x - x0)))

    # Boundaries dividing into 4 regions:
    # 1. Lag phase: 0 to ~2.5
    # 2. Log (exponential) phase: 2.5 to ~5.0
    # 3. Deceleration phase: 5.0 to ~7.5
    # 4. Stationary phase: 7.5 to 10
    b1, b2, b3 = 2.5, 5.0, 7.5

    # Clean axes
    axes_clean(ax, "time", "size (height or dry mass)", 10.2, 9.5)

    # Draw vertical dashed boundary lines
    for bx in [b1, b2, b3]:
        by = L / (1 + np.exp(-k * (bx - x0)))
        ax.plot([bx, bx], [0, by], linestyle="--", color=GREY, lw=1.5, zorder=2)

    # Plot the smooth S-shaped sigmoid curve
    ax.plot(x, y, color=DEEP["green"], lw=3.5, zorder=3)

    # Region label positions (centers of each interval)
    regions = [
        ("lag phase", (0 + b1) / 2),
        ("log (exponential)\nphase", (b1 + b2) / 2),
        ("deceleration\nphase", (b2 + b3) / 2),
        ("stationary\nphase", (b3 + 10) / 2),
    ]

    # Label regions below the axis / lower portion
    for label, cx in regions:
        ax.text(
            cx, -1.2, label,
            ha="center", va="top",
            fontsize=11.5, color=INK,
            clip_on=False
        )

    # Fastest growth annotation at the steepest part (x0, y(x0))
    # Steepest part of logistic curve is at inflection point x = x0
    inflection_y = L / 2.0
    ax.annotate(
        "fastest growth",
        xy=(x0, inflection_y),
        xytext=(x0 - 1.8, inflection_y + 1.8),
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3, connectionstyle="arc3,rad=-0.1"),
        ha="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    # Adjust plot limits and margins to accommodate labels below axis
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-0.2, 9.5)
    plt.subplots_adjust(bottom=0.22, left=0.12, right=0.92, top=0.92)

    save(fig, out)
