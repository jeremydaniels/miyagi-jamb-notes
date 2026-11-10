from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 5.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # Center coordinates and radii
    c1 = (2.0, 2.4)
    r1 = 1.0
    c2 = (8.0, 2.4)
    r2 = 1.3

    # Dashed line connecting centres
    ax.plot([c1[0], c2[0]], [c1[1], c2[1]], linestyle="--", color=GREY, lw=2, zorder=1)

    # Spheres (bodies)
    sphere1 = patches.Circle(c1, r1, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=2)
    sphere2 = patches.Circle(c2, r2, facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5, zorder=2)
    ax.add_patch(sphere1)
    ax.add_patch(sphere2)

    # Center points
    ax.scatter([c1[0], c2[0]], [c1[1], c2[1]], color=INK, s=25, zorder=4)

    # Labels m1 and m2 inside or above spheres
    ax.text(c1[0], c1[1] + r1 + 0.35, "$m_1$", fontsize=18, color=INK, ha="center", va="bottom")
    ax.text(c2[0], c2[1] + r2 + 0.35, "$m_2$", fontsize=18, color=INK, ha="center", va="bottom")

    # Force arrows pointing towards each other from center
    # Distance between centers is 6.0 units.
    arrow_len = 1.8
    ax.annotate(
        "", xy=(c1[0] + arrow_len, c1[1]), xytext=(c1[0], c1[1]),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3, mutation_scale=20),
        zorder=5
    )
    ax.annotate(
        "", xy=(c2[0] - arrow_len, c2[1]), xytext=(c2[0], c2[1]),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3, mutation_scale=20),
        zorder=5
    )

    # Force labels F placed well outside the sphere circles with clean white bounding boxes
    ax.text(
        c1[0] + arrow_len - 0.3, c1[1] + 0.45, "$F$",
        fontsize=16, color=DEEP["pink"], ha="center", va="bottom",
        bbox=dict(fc="white", ec="none", pad=2), zorder=6
    )
    ax.text(
        c2[0] - arrow_len + 0.3, c2[1] + 0.45, "$F$",
        fontsize=16, color=DEEP["pink"], ha="center", va="bottom",
        bbox=dict(fc="white", ec="none", pad=2), zorder=6
    )

    # Dimension line / annotation for r below
    y_dim = 0.5
    ax.annotate(
        "", xy=(c1[0], y_dim), xytext=(c2[0], y_dim),
        arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8),
        zorder=3
    )
    # Extension lines from centers down to dimension line
    ax.plot([c1[0], c1[0]], [c1[1] - r1 - 0.15, y_dim - 0.2], color=GREY, lw=1.2, linestyle=":")
    ax.plot([c2[0], c2[0]], [c2[1] - r2 - 0.15, y_dim - 0.2], color=GREY, lw=1.2, linestyle=":")

    # Label r with clear background
    ax.text(
        (c1[0] + c2[0]) / 2, y_dim, "$r$",
        fontsize=16, color=INK, ha="center", va="center",
        bbox=dict(fc="white", ec="none", pad=4), zorder=4
    )

    save(fig, out)
