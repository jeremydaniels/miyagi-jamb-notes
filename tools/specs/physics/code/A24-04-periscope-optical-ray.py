from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 9.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(5.0, 9.0, "Simple Periscope (Cross-Section)", fontsize=18, fontweight="bold", ha="center", color=INK)

    # Tube geometry parameters
    # Top horizontal tube: x from 2 to 5, y from 6 to 8
    # Vertical shaft: x from 3.5 to 5, y from 2 to 6
    # Bottom horizontal tube: x from 3.5 to 6.5, y from 0.5 to 2.5
    # Let's define clear periscope wall coordinates:
    # Outer wall contour:
    # Top opening: (2.0, 8.0) to (5.5, 8.0) -> corner down to (5.5, 2.5) -> right to (7.0, 2.5)
    # Bottom opening at x=7.0, y between 0.5 and 2.5
    # Inner wall contour:
    # (2.0, 6.5) -> (4.0, 6.5) -> down to (4.0, 0.5) -> right to (7.0, 0.5)

    tube_outer = [
        (1.8, 8.0), (5.5, 8.0), (5.5, 2.2), (7.2, 2.2)
    ]
    tube_inner = [
        (1.8, 6.2), (3.7, 6.2), (3.7, 0.4), (7.2, 0.4)
    ]

    # Draw tube body using filled polygon with a light grey/cream tone
    casing_polygon = [
        (1.8, 8.0), (5.5, 8.0), (5.5, 2.2), (7.2, 2.2),
        (7.2, 0.4), (3.7, 0.4), (3.7, 6.2), (1.8, 6.2)
    ]
    poly = patches.Polygon(casing_polygon, closed=True, facecolor=CREAM, edgecolor="none", zorder=1)
    ax.add_patch(poly)

    # Draw walls with thick lines
    # Top outer wall
    ax.plot([1.8, 5.5], [8.0, 8.0], color=INK, lw=3.5, zorder=2)
    # Right outer wall (top down to bottom corner)
    ax.plot([5.5, 5.5], [8.0, 2.2], color=INK, lw=3.5, zorder=2)
    # Bottom-right extension outer wall
    ax.plot([5.5, 7.2], [2.2, 2.2], color=INK, lw=3.5, zorder=2)

    # Top inner wall
    ax.plot([1.8, 3.7], [6.2, 6.2], color=INK, lw=3.5, zorder=2)
    # Left inner wall
    ax.plot([3.7, 3.7], [6.2, 0.4], color=INK, lw=3.5, zorder=2)
    # Bottom inner wall
    ax.plot([3.7, 7.2], [0.4, 0.4], color=INK, lw=3.5, zorder=2)

    # Plane Mirror 1 (Top corner, 45 degrees)
    # Centered at (4.6, 7.1)
    # Connecting roughly (3.7, 8.0) to (5.5, 6.2)
    m1_x = [3.7, 5.5]
    m1_y = [8.0, 6.2]
    ax.plot(m1_x, m1_y, color=DEEP["blue"], lw=5, solid_capstyle="round", zorder=4)
    # Hatching / backing for mirror 1
    for t in np.linspace(0.1, 0.9, 6):
        x0 = 3.7 + t * (5.5 - 3.7)
        y0 = 8.0 + t * (6.2 - 8.0)
        ax.plot([x0, x0 + 0.25], [y0, y0 + 0.25], color=GREY, lw=1.5, zorder=3)

    # Plane Mirror 2 (Bottom corner, 45 degrees)
    # Centered at (4.6, 1.3)
    # Connecting roughly (3.7, 2.2) to (5.5, 0.4)
    m2_x = [3.7, 5.5]
    m2_y = [2.2, 0.4]
    ax.plot(m2_x, m2_y, color=DEEP["blue"], lw=5, solid_capstyle="round", zorder=4)
    # Hatching / backing for mirror 2
    for t in np.linspace(0.1, 0.9, 6):
        x0 = 3.7 + t * (5.5 - 3.7)
        y0 = 2.2 + t * (0.4 - 2.2)
        ax.plot([x0, x0 - 0.25], [y0, y0 - 0.25], color=GREY, lw=1.5, zorder=3)

    # Light Ray path:
    # Object ray: enters horizontally at y = 7.1
    # Hits top mirror at x = 4.6, y = 7.1
    # Reflects down along x = 4.6
    # Hits bottom mirror at x = 4.6, y = 1.3
    # Reflects horizontally out at y = 1.3 to x = 8.8
    ray_color = DEEP["pink"]
    ray_lw = 2.8

    # Ray segments
    ax.plot([0.5, 4.6], [7.1, 7.1], color=ray_color, lw=ray_lw, zorder=5)
    ax.plot([4.6, 4.6], [7.1, 1.3], color=ray_color, lw=ray_lw, zorder=5)
    ax.plot([4.6, 8.4], [1.3, 1.3], color=ray_color, lw=ray_lw, zorder=5)

    # Direction arrows along ray
    # Top horizontal segment arrow
    ax.annotate("", xy=(2.9, 7.1), xytext=(2.5, 7.1),
                arrowprops=dict(arrowstyle="-|>", color=ray_color, lw=2.5, mutation_scale=16), zorder=6)
    # Vertical segment arrow
    ax.annotate("", xy=(4.6, 4.0), xytext=(4.6, 4.4),
                arrowprops=dict(arrowstyle="-|>", color=ray_color, lw=2.5, mutation_scale=16), zorder=6)
    # Bottom horizontal segment arrow
    ax.annotate("", xy=(6.5, 1.3), xytext=(6.1, 1.3),
                arrowprops=dict(arrowstyle="-|>", color=ray_color, lw=2.5, mutation_scale=16), zorder=6)

    # Normal lines and 45° angle indications on Top Mirror
    # Mirror normal is along vector (-1, -1) / sqrt(2) or (1, 1) / sqrt(2)
    norm_len = 0.7
    ax.plot([4.6, 4.6 - norm_len * np.cos(np.pi/4)], [7.1, 7.1 - norm_len * np.sin(np.pi/4)],
            color=GREY, lw=1.5, ls="--", zorder=4)

    # Normal line on Bottom Mirror
    ax.plot([4.6, 4.6 + norm_len * np.cos(np.pi/4)], [1.3, 1.3 + norm_len * np.sin(np.pi/4)],
            color=GREY, lw=1.5, ls="--", zorder=4)

    # Annotate 45° angles
    ax.text(4.9, 7.6, "45°", fontsize=14, color=INK, weight="bold")
    ax.text(3.4, 1.7, "45°", fontsize=14, color=INK, weight="bold")

    # Object indicator (e.g. tree or simple object arrow)
    ax.annotate("", xy=(0.5, 8.0), xytext=(0.5, 6.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3.5))
    ax.text(0.5, 8.3, "Object", fontsize=15, ha="center", color=INK, weight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # Drawn Eye observing the light ray at (8.8, 1.3)
    eye_x = 8.8
    eye_y = 1.3
    # Upper lid
    t_lid = np.linspace(-0.6, 0.6, 50)
    y_upper = eye_y + 0.45 * (1 - (t_lid / 0.6)**2)
    y_lower = eye_y - 0.45 * (1 - (t_lid / 0.6)**2)
    x_lid = eye_x + t_lid
    ax.plot(x_lid, y_upper, color=INK, lw=2, zorder=5)
    ax.plot(x_lid, y_lower, color=INK, lw=2, zorder=5)

    # Iris & Pupil
    iris = patches.Circle((eye_x - 0.15, eye_y), 0.28, facecolor=BLUE, edgecolor=INK, lw=1.5, zorder=6)
    pupil = patches.Circle((eye_x - 0.18, eye_y), 0.14, facecolor=INK, edgecolor=INK, zorder=7)
    highlight = patches.Circle((eye_x - 0.22, eye_y + 0.08), 0.04, facecolor="white", zorder=8)
    ax.add_patch(iris)
    ax.add_patch(pupil)
    ax.add_patch(highlight)
    # Eyelashes
    ax.plot([eye_x - 0.3, eye_x - 0.45], [eye_y + 0.35, eye_y + 0.55], color=INK, lw=1.8)
    ax.plot([eye_x, eye_x], [eye_y + 0.45, eye_y + 0.7], color=INK, lw=1.8)
    ax.plot([eye_x + 0.3, eye_x + 0.45], [eye_y + 0.35, eye_y + 0.55], color=INK, lw=1.8)

    ax.text(eye_x, eye_y - 0.8, "Eye", fontsize=15, ha="center", color=INK, weight="bold")

    # Labels and Annotations with white background boxes
    # Top mirror label
    ax.annotate("Top mirror (45°)\nplane mirror",
                xy=(4.8, 6.9), xytext=(7.4, 7.8),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Bottom mirror label
    ax.annotate("Bottom mirror (45°)\nparallel to top mirror",
                xy=(4.4, 1.1), xytext=(1.8, 2.8),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Light ray label
    ax.text(2.6, 7.35, "Light ray", fontsize=14, color=DEEP["pink"], ha="center", weight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # 90° Reflection annotations
    ax.annotate("90° reflection", xy=(4.65, 7.0), xytext=(2.7, 5.3),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("90° reflection", xy=(4.65, 1.35), xytext=(6.5, 3.2),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    save(fig, out)
