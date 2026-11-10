from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9.5, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Colors for the 4 tiers (from bottom to top)
    colors = [GREEN, BLUE, LAV, ORANGE]
    edge_colors = [DEEP["green"], DEEP["blue"], DEEP["lav"], DEEP["orange"]]

    # Labels for the 4 tiers (bottom to top)
    labels = [
        "Ward Level (Grassroots)",
        "Local Government Level",
        "State Level",
        "National\nLevel"
    ]

    # Geometry of the pyramid
    # Center x = 4.5, height from y = 1.0 to y = 6.8 (total height 5.8)
    # 4 tiers of equal vertical height: h = 1.45 each
    cx = 4.5
    y_bottoms = [1.0, 2.45, 3.9, 5.35]
    y_tops = [2.45, 3.9, 5.35, 6.8]

    # Half-width at y=1.0 is 3.6, at y=6.8 is 0.0 (apex)
    # w(y) = 3.6 * (6.8 - y) / 5.8
    def half_width(y):
        return 3.6 * (6.8 - y) / 5.8

    for i in range(4):
        yb = y_bottoms[i]
        yt = y_tops[i]
        wb = half_width(yb)
        wt = half_width(yt)

        if i == 3:  # Top triangle
            pts = [[cx - wb, yb], [cx, yt], [cx + wb, yb]]
        else:  # Trapezoids
            pts = [
                [cx - wb, yb],
                [cx - wt, yt],
                [cx + wt, yt],
                [cx + wb, yb]
            ]

        poly = patches.Polygon(
            pts,
            closed=True,
            facecolor=colors[i],
            edgecolor=edge_colors[i],
            linewidth=2.5,
            zorder=2
        )
        ax.add_patch(poly)

        # Tier label placement
        y_center = (yb + yt) / 2
        # Slight adjustment for top triangle to visually center text
        if i == 3:
            y_center = yb + (yt - yb) / 3.5

        ax.text(
            cx, y_center, labels[i],
            ha="center", va="center",
            fontsize=15, fontweight="bold",
            color=INK, zorder=3
        )

    # Arrow indicating flow of power and representation
    arrow_x = 8.6
    ax.annotate(
        "",
        xy=(arrow_x, 6.6),
        xytext=(arrow_x, 1.2),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["blue"],
            lw=3.5,
            mutation_scale=24
        ),
        zorder=4
    )

    # Arrow text label
    ax.text(
        arrow_x + 0.25, 3.9,
        "Flow of Power\n& Representation",
        ha="left", va="center",
        fontsize=14, fontweight="bold",
        color=INK,
        bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none"),
        zorder=5
    )

    # Title
    ax.text(
        cx, 7.5,
        "Structure of a Political Party in Nigeria",
        ha="center", va="center",
        fontsize=17, fontweight="bold",
        color=INK
    )

    save(fig, out)
