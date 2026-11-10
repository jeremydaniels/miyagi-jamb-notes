from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Cliffs positions
    # Left cliff: x from 0.5 to 1.8
    # Right cliff: x from 8.2 to 9.5
    cliff_l_inner = 1.8
    cliff_r_inner = 8.2
    ground_y = 1.5
    cliff_top = 6.2

    # Draw Cliffs
    # Left cliff block
    ax.fill_between([0.5, cliff_l_inner], ground_y, cliff_top, color=LAV, alpha=0.5)
    ax.plot([0.5, cliff_l_inner, cliff_l_inner, 0.5], [cliff_top, cliff_top, ground_y, ground_y], color=DEEP["lav"], lw=2.5)
    # Right cliff block
    ax.fill_between([cliff_r_inner, 9.5], ground_y, cliff_top, color=LAV, alpha=0.5)
    ax.plot([cliff_r_inner, 9.5, 9.5, cliff_r_inner], [ground_y, ground_y, cliff_top, cliff_top], color=DEEP["lav"], lw=2.5)

    # Labels for cliffs
    ax.text((0.5 + cliff_l_inner)/2, 5.0, "Cliff A\n(Left Cliff)", ha="center", va="center", fontsize=15, color=INK, fontweight="bold")
    ax.text((cliff_r_inner + 9.5)/2, 5.0, "Cliff B\n(Right Cliff)", ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

    # Ground between cliffs
    ax.plot([cliff_l_inner, cliff_r_inner], [ground_y, ground_y], color=INK, lw=2.5)

    # Man position: standing between cliffs, closer to left cliff (d1 < d2)
    # Total span = 8.2 - 1.8 = 6.4. Let d1 = 2.2, d2 = 4.2 -> man_x = 1.8 + 2.2 = 4.0
    man_x = 4.0
    man_base_y = ground_y

    # Draw stylized stick figure of a man
    # Head
    head_center = (man_x, man_base_y + 1.25)
    head = plt.Circle(head_center, 0.18, color=INK, fill=True)
    ax.add_patch(head)
    # Body
    ax.plot([man_x, man_x], [man_base_y + 0.55, man_base_y + 1.1], color=INK, lw=2.5)
    # Legs
    ax.plot([man_x, man_x - 0.2], [man_base_y + 0.55, man_base_y], color=INK, lw=2.5)
    ax.plot([man_x, man_x + 0.2], [man_base_y + 0.55, man_base_y], color=INK, lw=2.5)
    # Arms
    ax.plot([man_x - 0.25, man_x, man_x + 0.25], [man_base_y + 0.8, man_base_y + 0.95, man_base_y + 0.8], color=INK, lw=2.5)

    # Label for person/man
    ax.text(man_x, man_base_y - 0.35, "Observer / Man", ha="center", va="top", fontsize=14, color=INK)

    # Horizontal dashed lines representing distances d1 and d2
    dim_y = ground_y + 0.85

    # Distance d1 (left cliff to man)
    ax.annotate(
        "", xy=(cliff_l_inner, dim_y), xytext=(man_x, dim_y),
        arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=2, linestyle="--")
    )
    ax.text((cliff_l_inner + man_x)/2, dim_y + 0.2, "$d_1$", ha="center", va="bottom", fontsize=16, color=DEEP["blue"],
            bbox=dict(fc="white", ec="none", pad=2))

    # Distance d2 (man to right cliff)
    ax.annotate(
        "", xy=(man_x, dim_y), xytext=(cliff_r_inner, dim_y),
        arrowprops=dict(arrowstyle="<->", color=DEEP["pink"], lw=2, linestyle="--")
    )
    ax.text((man_x + cliff_r_inner)/2, dim_y + 0.2, "$d_2$", ha="center", va="bottom", fontsize=16, color=DEEP["pink"],
            bbox=dict(fc="white", ec="none", pad=2))

    # Total distance D = d1 + d2 (higher up)
    total_y = 3.6
    # Vertical guides for total distance
    ax.plot([cliff_l_inner, cliff_l_inner], [ground_y, total_y + 0.3], color=GREY, lw=1.2, linestyle=":")
    ax.plot([cliff_r_inner, cliff_r_inner], [ground_y, total_y + 0.3], color=GREY, lw=1.2, linestyle=":")
    # Dimension arrow for D
    ax.annotate(
        "", xy=(cliff_l_inner, total_y), xytext=(cliff_r_inner, total_y),
        arrowprops=dict(arrowstyle="<->", color=DEEP["orange"], lw=2.2)
    )
    ax.text((cliff_l_inner + cliff_r_inner)/2, total_y + 0.25, "$D = d_1 + d_2$", ha="center", va="bottom", fontsize=16,
            color=DEEP["orange"], fontweight="bold", bbox=dict(fc="white", ec="none", pad=3))

    save(fig, out)
