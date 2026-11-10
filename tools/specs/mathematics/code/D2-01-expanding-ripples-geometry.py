from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")

    # Center of ripples
    cx, cy = 0.0, 0.0
    r1, r2, r3 = 1.3, 2.3, 3.3

    # Draw circular ripples
    theta = np.linspace(0, 2 * np.pi, 300)
    
    # Outer shaded water disc (subtle wash)
    ax.fill(r3 * np.cos(theta), r3 * np.sin(theta), color=BLUE, alpha=0.15, zorder=1)

    # Ripple lines with varying dash/weight
    ax.plot(r1 * np.cos(theta), r1 * np.sin(theta), color=DEEP["blue"], lw=2.0, ls=(0, (6, 4)), alpha=0.6, zorder=2)
    ax.plot(r2 * np.cos(theta), r2 * np.sin(theta), color=DEEP["blue"], lw=2.5, ls=(0, (8, 4)), alpha=0.8, zorder=2)
    ax.plot(r3 * np.cos(theta), r3 * np.sin(theta), color=DEEP["blue"], lw=3.0, zorder=2)

    # Center point
    ax.plot(cx, cy, "o", color=INK, markersize=5, zorder=5)

    # Radius line from center to outermost edge
    # Choose an angle of 35 degrees for 'r'
    ang_r = np.deg2rad(35)
    rx, ry = r3 * np.cos(ang_r), r3 * np.sin(ang_r)
    ax.plot([cx, rx], [cy, ry], color=INK, lw=2.2, zorder=4)

    # Label 'r' along the line with white bbox
    mid_rx, mid_ry = 0.52 * rx, 0.52 * ry
    ax.text(mid_rx - 0.12, mid_ry + 0.15, r"$r$", fontsize=16, color=INK,
            ha="center", va="center",
            bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec="none"), zorder=6)

    # Outward-pointing arrow on the outer circle labelled 'dr/dt'
    # Place arrow along angle 145 degrees
    ang_arrow = np.deg2rad(140)
    ax_start = r3 * np.cos(ang_arrow)
    ay_start = r3 * np.sin(ang_arrow)
    dr_len = 0.85
    ax_end = (r3 + dr_len) * np.cos(ang_arrow)
    ay_end = (r3 + dr_len) * np.sin(ang_arrow)

    ax.annotate(
        "", xy=(ax_end, ay_end), xytext=(ax_start, ay_start),
        arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.8, mutation_scale=20),
        zorder=5
    )

    # Label 'dr/dt' near the tip of the expansion arrow
    label_x = (r3 + dr_len + 0.45) * np.cos(ang_arrow)
    label_y = (r3 + dr_len + 0.45) * np.sin(ang_arrow)
    ax.text(label_x, label_y, r"$\frac{dr}{dt}$", fontsize=18, color=INK,
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8), zorder=6)

    # Limits
    lim = 4.6
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    save(fig, out)
