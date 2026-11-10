from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)

    # Set up centered origin coordinate plane
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Curve domain
    x = np.linspace(-1.3, 3.7, 400)
    y = x**3 - 3 * x**2

    # Plot curve
    ax.plot(x, y, color=DEEP["blue"], lw=3.5, zorder=3)

    # Range limits
    ax.set_xlim(-2.0, 4.5)
    ax.set_ylim(-6.0, 4.5)

    # Axis arrowheads
    ax.plot(4.5, 0, marker='>', color=INK, markersize=8, clip_on=False)
    ax.plot(0, 4.5, marker='^', color=INK, markersize=8, clip_on=False)

    # Axis labels
    ax.text(4.4, 0.4, r'$x$', fontsize=16, color=INK, ha='center', va='bottom')
    ax.text(0.25, 4.3, r'$y$', fontsize=16, color=INK, ha='left', va='center')

    # Key points: local max (0,0), local min (2,-4), x-intercept (3,0)
    points = [
        (0, 0, "local maximum\n(0, 0)", (-0.8, 1.2), 'right'),
        (2, -4, "local minimum\n(2, -4)", (2, -5.3), 'center'),
        (3, 0, "x-intercept\n(3, 0)", (3.4, -1.2), 'left')
    ]

    # Dashed drop lines for (2, -4)
    ax.plot([2, 2], [0, -4], color=GREY, linestyle='--', lw=1.5, zorder=2)
    ax.plot([0, 2], [-4, -4], color=GREY, linestyle='--', lw=1.5, zorder=2)

    # Tick-like annotations on the axes for (2, -4)
    ax.text(2, 0.3, "2", fontsize=14, color=INK, ha='center', va='bottom')
    ax.text(-0.25, -4, "-4", fontsize=14, color=INK, ha='right', va='center')

    for px, py, label, tpos, align in points:
        ax.scatter([px], [py], color=DEEP["pink"], s=70, zorder=5, edgecolor=INK, linewidth=1.2)
        ax.annotate(
            label,
            xy=(px, py),
            xytext=tpos,
            fontsize=14,
            color=INK,
            ha=align,
            va='center',
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2, shrinkA=4, shrinkB=4)
        )

    # Equation label
    ax.text(
        -1.5, -3.5,
        r'$y = x^3 - 3x^2$',
        fontsize=18,
        color=DEEP["blue"],
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4")
    )

    # Grid styling
    ax.grid(True, which='both', color=CREAM, linestyle='-', linewidth=1.0, zorder=1)
    ax.set_xticks([-1, 1, 2, 3, 4])
    ax.set_yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4])
    ax.tick_params(colors=GREY, labelsize=12)
    # Hide default ticks as we use custom positioning and clean styling
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(left=False, bottom=False)

    save(fig, out)
