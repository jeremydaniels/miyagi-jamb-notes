from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")

    # Center O
    ox, oy = 0.0, 0.0
    radius = 2.4

    # Position of moving point P on circular path (angle = 35 degrees)
    theta = np.deg2rad(35)
    px = ox + radius * np.cos(theta)
    py = oy + radius * np.sin(theta)

    # Dotted circular path around O
    circle_theta = np.linspace(0, 2 * np.pi, 400)
    cx = ox + radius * np.cos(circle_theta)
    cy = oy + radius * np.sin(circle_theta)
    ax.plot(cx, cy, linestyle=":", color=DEEP["blue"], lw=2.5, zorder=1)

    # Straight line segment connecting O to P
    ax.plot([ox, px], [oy, py], color=INK, lw=2.5, zorder=2)

    # Label 'r' along segment OP with white background to avoid overlapping line
    mid_x = (ox + px) / 2
    mid_y = (oy + py) / 2
    perp_dx = -np.sin(theta) * 0.25
    perp_dy = np.cos(theta) * 0.25
    ax.text(mid_x + perp_dx, mid_y + perp_dy, "r", fontsize=16, color=INK,
            ha="center", va="center", style="italic",
            bbox=dict(fc="white", ec="none", pad=2), zorder=4)

    # Direction of motion hint (small curved arrow along the path at P)
    arrow_arc = np.linspace(theta + 0.12, theta + 0.38, 30)
    ax.plot(radius * np.cos(arrow_arc), radius * np.sin(arrow_arc),
            color=DEEP["orange"], lw=2.0, zorder=2)
    ax.annotate("", xy=(radius * np.cos(theta + 0.40), radius * np.sin(theta + 0.40)),
                xytext=(radius * np.cos(theta + 0.35), radius * np.sin(theta + 0.35)),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["orange"], lw=2.0, mutation_scale=14),
                zorder=3)

    # Fixed central point O
    ax.plot(ox, oy, "o", color=INK, markersize=8, zorder=5)
    ax.text(ox - 0.22, oy - 0.22, "O", fontsize=16, color=INK,
            ha="right", va="top", weight="bold")

    # Moving point P
    ax.plot(px, py, "o", color=DEEP["orange"], markersize=9, zorder=5)
    ax.text(px + 0.22, py + 0.18, "P", fontsize=16, color=INK,
            ha="left", va="bottom", weight="bold")

    # Limits ensuring everything is comfortably inside the canvas
    limit = 3.2
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    save(fig, out)
