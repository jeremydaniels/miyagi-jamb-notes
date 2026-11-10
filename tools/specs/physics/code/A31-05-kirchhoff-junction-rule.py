from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Central node coordinates
    cx, cy = 0.0, 0.0
    r = 3.6  # wire length

    # 4 branches:
    # Top-left (inward): 5 A, angle = 145°
    # Bottom-left (inward): 4 A, angle = 215°
    # Top-right (outward): 3 A, angle = 35°
    # Bottom-right (outward): x, angle = 315° (-45°)

    branches = [
        {"angle": 145, "dir": "in", "label": "5 A", "col": DEEP["blue"]},
        {"angle": 215, "dir": "in", "label": "4 A", "col": DEEP["green"]},
        {"angle": 35,  "dir": "out", "label": "3 A", "col": DEEP["orange"]},
        {"angle": 315, "dir": "out", "label": "x",   "col": DEEP["pink"]},
    ]

    for b in branches:
        rad = np.radians(b["angle"])
        dx = np.cos(rad)
        dy = np.sin(rad)
        
        # Wire endpoints
        p_outer = (cx + r * dx, cy + r * dy)
        
        # Draw wire
        ax.plot([cx, p_outer[0]], [cy, p_outer[1]], color=GREY, lw=3.5, zorder=1)

        # Midpoint for arrow and label
        mid_r = 1.9
        mx = cx + mid_r * dx
        my = cy + mid_r * dy

        # Direction vector for arrow
        sign = -1.0 if b["dir"] == "in" else 1.0
        arrow_len = 0.45
        ax.annotate(
            "",
            xy=(mx + sign * dx * arrow_len, my + sign * dy * arrow_len),
            xytext=(mx - sign * dx * arrow_len, my - sign * dy * arrow_len),
            arrowprops=dict(
                arrowstyle="-|>",
                mutation_scale=22,
                color=b["col"],
                lw=3,
            ),
            zorder=3
        )

        # Text label offset perpendicularly or slightly along
        offset_dist = 0.65
        # Perpendicular unit vector
        perp_x = -dy
        perp_y = dx
        # Choose side to make label clear
        if b["angle"] in [145, 35]:
            side = 1.0
        else:
            side = -1.0

        lx = mx + side * perp_x * offset_dist
        ly = my + side * perp_y * offset_dist

        ax.text(
            lx, ly, b["label"],
            fontsize=17,
            fontweight="bold",
            color=INK,
            ha="center",
            va="center",
            bbox=dict(fc="white", ec="none", pad=3),
            zorder=4
        )

    # Central junction node dot
    node_circle = plt.Circle((cx, cy), 0.2, color=INK, zorder=5)
    ax.add_patch(node_circle)

    # Title / Header
    ax.text(0, 4.2, "Kirchhoff's Current Law (Junction Rule)", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    save(fig, out)
