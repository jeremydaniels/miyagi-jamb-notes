from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 6.5)
    ax.axis("off")

    # Coordinates for A and B
    xA, yA = 1.0, 1.5
    xB, yB = 9.0, 1.5

    # Winding path points for Distance (bezier-like smooth spline)
    t = np.linspace(0, 1, 300)
    # Control points or sinusoidal winding path
    # Path goes up, loops down, goes up, then arrives at B
    x_path = np.linspace(xA, xB, 300)
    y_path = yA + 2.8 * np.sin(np.pi * (x_path - xA) / (xB - xA)) + \
             1.2 * np.sin(2 * np.pi * (x_path - xA) / (xB - xA))

    # Plot winding path (Distance)
    ax.plot(x_path, y_path, color=DEEP["blue"], lw=3.0, ls=(0, (4, 3)), zorder=2)

    # Plot straight-line arrow (Displacement)
    # Red/Pink deep accent for the displacement vector
    ax.annotate(
        "",
        xy=(xB, yB),
        xytext=(xA, yA),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["pink"],
            lw=4.0,
            mutation_scale=25,
        ),
        zorder=3
    )

    # Draw Points A and B
    ax.scatter([xA, xB], [yA, yB], color=INK, s=120, zorder=5)

    # Label Points A and B
    ax.text(xA - 0.2, yA - 0.7, "Point A\n(House)", fontsize=16, color=INK,
            ha="center", va="top", weight="bold")
    ax.text(xB + 0.2, yB - 0.7, "Point B\n(School)", fontsize=16, color=INK,
            ha="center", va="top", weight="bold")

    # Label for Distance
    # Peak of winding path is around x = 3.5, y = 4.8
    ax.text(
        4.5, 4.9,
        "Distance: actual path",
        fontsize=16,
        color=DEEP["blue"],
        weight="bold",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["blue"], lw=1.5)
    )

    # Label for Displacement
    ax.text(
        5.0, 0.7,
        "Displacement: straight-line vector",
        fontsize=16,
        color=DEEP["pink"],
        weight="bold",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["pink"], lw=1.5)
    )

    save(fig, out)
