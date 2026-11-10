from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Outer circle: The State
    outer_center = (0, 0)
    outer_radius = 4.0
    outer_circle = patches.Circle(
        outer_center, outer_radius,
        facecolor=BLUE, edgecolor=DEEP["blue"],
        linewidth=2.5, zorder=1
    )
    ax.add_patch(outer_circle)

    # Inner circle: The Government
    inner_center = (0, -0.9)
    inner_radius = 2.0
    inner_circle = patches.Circle(
        inner_center, inner_radius,
        facecolor=CREAM, edgecolor=DEEP["orange"],
        linewidth=2.5, zorder=2
    )
    ax.add_patch(inner_circle)

    # Label for The State (at the top inside the outer circle)
    state_title = "The State"
    state_desc = "(Permanent, Includes all citizens)"
    ax.text(
        0, 2.5, f"{state_title}\n{state_desc}",
        ha="center", va="center",
        fontsize=16, color=INK, weight="bold",
        linespacing=1.4, zorder=3
    )

    # Label for The Government (inside the inner circle)
    govt_title = "The Government"
    govt_desc = "(Temporary,\nAgency of the State,\nMade up of officials)"
    ax.text(
        inner_center[0], inner_center[1], f"{govt_title}\n{govt_desc}",
        ha="center", va="center",
        fontsize=14, color=INK, weight="bold",
        linespacing=1.3, zorder=3
    )

    save(fig, out)
