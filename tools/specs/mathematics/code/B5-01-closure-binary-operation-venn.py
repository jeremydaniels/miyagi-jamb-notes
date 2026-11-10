from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Main circle for the Set of Natural Numbers (N)
    circle_center = (3.6, 3.4)
    circle_radius = 2.4
    circle = patches.Circle(
        circle_center,
        circle_radius,
        facecolor=BLUE,
        edgecolor=DEEP["blue"],
        linewidth=2.5,
        alpha=0.6,
        zorder=1
    )
    ax.add_patch(circle)

    # Set Label above / top-left of the circle
    ax.text(
        3.6, 5.2,
        'Set of Natural Numbers (N)',
        fontsize=16,
        fontweight='bold',
        color=INK,
        ha='center',
        va='center',
        zorder=3
    )

    # Numbers 3 and 5 inside the circle
    ax.text(
        2.6, 3.5,
        '3',
        fontsize=18,
        fontweight='bold',
        color=INK,
        ha='center',
        va='center',
        bbox=dict(boxstyle='circle,pad=0.3', fc='white', ec=DEEP["blue"], lw=1.5),
        zorder=4
    )
    ax.text(
        3.8, 2.7,
        '5',
        fontsize=18,
        fontweight='bold',
        color=INK,
        ha='center',
        va='center',
        bbox=dict(boxstyle='circle,pad=0.3', fc='white', ec=DEEP["blue"], lw=1.5),
        zorder=4
    )

    # Result -2 outside the set boundary
    result_x, result_y = 8.0, 3.1
    ax.text(
        result_x, result_y,
        '-2',
        fontsize=18,
        fontweight='bold',
        color=INK,
        ha='center',
        va='center',
        bbox=dict(boxstyle='circle,pad=0.35', fc=PINK, ec=DEEP["pink"], lw=2),
        zorder=4
    )

    # Explanatory tag next to -2
    ax.text(
        result_x, result_y - 0.9,
        '-2 ∉ N\n(Not a Natural Number)',
        fontsize=14,
        color=INK,
        ha='center',
        va='top',
        zorder=4
    )

    # Arrow from the operation inside to -2 outside
    ax.annotate(
        '',
        xy=(result_x - 0.55, result_y),
        xytext=(4.3, 3.1),
        arrowprops=dict(
            arrowstyle='->,head_width=0.45,head_length=0.65',
            color=DEEP["orange"],
            lw=2.5,
            shrinkA=0,
            shrinkB=0
        ),
        zorder=3
    )

    # Label for the arrow: 'Subtraction (3 - 5)'
    ax.text(
        5.85, 3.45,
        'Subtraction (3 - 5)',
        fontsize=14,
        fontweight='bold',
        color=INK,
        ha='center',
        va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=GREY, lw=1),
        zorder=5
    )

    # Caption / explanatory statement at the bottom
    ax.text(
        5.0, 0.7,
        'The set of natural numbers is not closed under subtraction.',
        fontsize=15,
        fontstyle='italic',
        color=INK,
        ha='center',
        va='center',
        bbox=dict(boxstyle='round,pad=0.4', fc=CREAM, ec=GREY, lw=1),
        zorder=3
    )

    save(fig, out)
