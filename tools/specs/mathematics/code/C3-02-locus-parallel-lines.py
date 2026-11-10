from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Geometry parameters
    x_start = 1.5
    x_end = 7.5
    y_mid = 3.0
    d = 1.8

    y_top = y_mid + d
    y_bot = y_mid - d

    # Solid straight horizontal line AB
    ax.plot([x_start, x_end], [y_mid, y_mid], color=DEEP["blue"], lw=3.0, solid_capstyle="round")

    # Endpoints A and B
    ax.plot([x_start, x_end], [y_mid, y_mid], "o", color=DEEP["blue"], markersize=7)
    ax.text(x_start - 0.35, y_mid, "A", fontsize=18, fontweight="bold", color=INK, va="center", ha="right")
    ax.text(x_end + 0.35, y_mid, "B", fontsize=18, fontweight="bold", color=INK, va="center", ha="left")

    # Parallel dotted lines above and below
    ax.plot([x_start - 0.5, x_end + 0.5], [y_top, y_top], color=DEEP["lav"], lw=2.2, linestyle=":", dash_capstyle="round")
    ax.plot([x_start - 0.5, x_end + 0.5], [y_bot, y_bot], color=DEEP["lav"], lw=2.2, linestyle=":", dash_capstyle="round")

    # Vertical dashed lines indicating distance d
    # Left vertical indicator for top distance
    x_dim_top = 3.2
    ax.plot([x_dim_top, x_dim_top], [y_mid, y_top], color=GREY, lw=1.8, linestyle="--")

    # Double-headed arrows on the vertical line
    ax.annotate("", xy=(x_dim_top, y_top), xytext=(x_dim_top, y_mid),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5, shrinkA=0, shrinkB=0))

    # Label 'd' for top segment
    ax.text(x_dim_top - 0.3, y_mid + d / 2, "d", fontsize=16, fontstyle="italic", color=INK,
            va="center", ha="right", bbox=dict(fc="white", ec="none", pad=1))

    # Right-angle indicator at (x_dim_top, y_mid)
    sq_size = 0.28
    ax.plot([x_dim_top, x_dim_top + sq_size, x_dim_top + sq_size],
            [y_mid + sq_size, y_mid + sq_size, y_mid],
            color=INK, lw=1.4)

    # Right vertical indicator for bottom distance
    x_dim_bot = 5.8
    ax.plot([x_dim_bot, x_dim_bot], [y_bot, y_mid], color=GREY, lw=1.8, linestyle="--")

    # Double-headed arrows on the vertical line
    ax.annotate("", xy=(x_dim_bot, y_bot), xytext=(x_dim_bot, y_mid),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5, shrinkA=0, shrinkB=0))

    # Label 'd' for bottom segment
    ax.text(x_dim_bot + 0.3, y_mid - d / 2, "d", fontsize=16, fontstyle="italic", color=INK,
            va="center", ha="left", bbox=dict(fc="white", ec="none", pad=1))

    # Right-angle indicator at (x_dim_bot, y_mid)
    ax.plot([x_dim_bot, x_dim_bot - sq_size, x_dim_bot - sq_size],
            [y_mid - sq_size, y_mid - sq_size, y_mid],
            color=INK, lw=1.4)

    # Adjust view bounds
    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(0.5, 5.5)

    save(fig, out)
