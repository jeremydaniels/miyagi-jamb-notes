from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.2, 6.4)
    ax.axis('off')

    # Dimensions of the optical fibre
    x_start = 1.0
    x_end = 9.8
    y_bottom_clad = 1.0
    y_bottom_core = 2.0
    y_top_core = 4.0
    y_top_clad = 5.0

    # Shading layers
    # Cladding (lighter tint)
    clad_top = patches.Rectangle((x_start, y_top_core), x_end - x_start, y_top_clad - y_top_core, 
                                 facecolor=CREAM, edgecolor='none', zorder=1)
    clad_bottom = patches.Rectangle((x_start, y_bottom_clad), x_end - x_start, y_bottom_core - y_bottom_clad, 
                                    facecolor=CREAM, edgecolor='none', zorder=1)
    # Core (darker tint than cladding)
    core = patches.Rectangle((x_start, y_bottom_core), x_end - x_start, y_top_core - y_bottom_core, 
                             facecolor=LAV, edgecolor='none', zorder=1)

    ax.add_patch(clad_top)
    ax.add_patch(clad_bottom)
    ax.add_patch(core)

    # Boundaries
    ax.plot([x_start, x_end], [y_top_clad, y_top_clad], color=INK, lw=2, zorder=2)
    ax.plot([x_start, x_end], [y_top_core, y_top_core], color=INK, lw=2.5, zorder=2)
    ax.plot([x_start, x_end], [y_bottom_core, y_bottom_core], color=INK, lw=2.5, zorder=2)
    ax.plot([x_start, x_end], [y_bottom_clad, y_bottom_clad], color=INK, lw=2, zorder=2)
    # End caps
    ax.plot([x_start, x_start], [y_bottom_clad, y_top_clad], color=INK, lw=2, zorder=2)
    ax.plot([x_end, x_end], [y_bottom_clad, y_top_clad], color=INK, lw=2, linestyle='--', zorder=2)

    # Ray path (zigzag inside core)
    # Enters at left (0.0, 2.3) -> boundary at (1.0, 3.0)
    # bounces at (2.5, 4.0) -> (4.5, 2.0) -> (6.5, 4.0) -> (8.5, 2.0) -> continues towards (9.8, 3.3)
    ray_x = [0.0, 1.0, 2.5, 4.5, 6.5, 8.5, 9.8]
    ray_y = [2.3, 3.0, 4.0, 2.0, 4.0, 2.0, 3.3]

    for i in range(len(ray_x) - 1):
        x1, y1 = ray_x[i], ray_y[i]
        x2, y2 = ray_x[i+1], ray_y[i+1]
        ax.plot([x1, x2], [y1, y2], color=DEEP["orange"], lw=3.5, zorder=5)
        # Midpoint directional arrows
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = (x2 - x1) * 0.05, (y2 - y1) * 0.05
        ax.annotate('', xy=(xm + dx, ym + dy), xytext=(xm - dx, ym - dy),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18),
                    zorder=6)

    # Normal line at first reflection point (2.5, 4.0)
    ax.plot([2.5, 2.5], [3.1, 4.6], color=GREY, lw=1.6, linestyle=":", zorder=4)
    # Normal line at second reflection point (4.5, 2.0)
    ax.plot([4.5, 4.5], [1.4, 2.9], color=GREY, lw=1.6, linestyle=":", zorder=4)

    # Angle arc at first bounce: between normal (downwards, 270 deg) and incoming ray
    # Incoming ray from (1.0, 3.0) to (2.5, 4.0): direction is (1.5, 1.0), vector backward is (-1.5, -1.0)
    # which corresponds to 180 + arctan(1/1.5) = 213.7 deg.
    arc = patches.Arc((2.5, 4.0), 1.1, 1.1, angle=0, theta1=214, theta2=270, color=INK, lw=1.6, zorder=7)
    ax.add_patch(arc)
    ax.text(2.35, 3.35, r"$\theta > c$", fontsize=15, color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5), zorder=8)

    # Angle arc at bottom bounce (4.5, 2.0)
    # Incoming ray from (2.5, 4.0) to (4.5, 2.0): vector backward is (-2.0, 2.0) -> 135 deg; normal upwards is 90 deg
    arc_bot = patches.Arc((4.5, 2.0), 1.1, 1.1, angle=0, theta1=90, theta2=135, color=INK, lw=1.6, zorder=7)
    ax.add_patch(arc_bot)
    ax.text(4.35, 2.65, r"$\theta$", fontsize=15, color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5), zorder=8)

    # Labels placed in clear regions with white background pads to guarantee zero overlap
    # Cladding label (top layer)
    ax.text(8.2, 4.5, r"Cladding ($n_2$)", fontsize=16, color=INK, ha="center", va="center",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"), zorder=8)
    
    # Core label placed at an open pocket between bounces (e.g. x = 5.5, y = 3.0)
    # At x = 5.5, the ray passes at (4.5, 2.0) -> (6.5, 4.0), so at x=5.5, y_ray = 3.0!
    # To completely avoid ray, place Core label with an indicator pointer above/below or at a clear space
    # Notice at x = 3.5, y_ray is 4.0 - (1.0/2.0)*(3.5-2.5) = 3.0. The ray crosses 3.0 at x=3.5, 5.5, 7.5.
    # Safe zones inside core are near the top/bottom away from vertices:
    # At x = 3.5: top is near 4.0, bottom is near 2.0.
    # Best: place label clearly with a pointer or clean white card inside the core:
    ax.text(5.5, 3.45, r"Core ($n_1$)", fontsize=16, color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=8)

    # Cladding label (bottom layer)
    ax.text(8.2, 1.5, r"Cladding ($n_2$)", fontsize=16, color=INK, ha="center", va="center",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"), zorder=8)

    # Condition label n1 > n2 above the fibre
    ax.text(5.5, 5.7, r"$n_1 > n_2$", fontsize=16, color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2))

    # Annotation for Total internal reflection
    ax.annotate("Total internal reflection", xy=(4.5, 2.0), xytext=(4.5, 0.4),
                fontsize=15, color=INK, ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2))

    save(fig, out)
