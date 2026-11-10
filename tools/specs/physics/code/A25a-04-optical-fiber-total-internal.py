from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.2, 13)
    ax.set_ylim(-4.0, 4.2)

    # Geometry coordinates
    x_start = 1.0
    x_end = 11.5
    y_core = 1.3
    y_clad = 2.6

    # Cladding regions (top and bottom)
    clad_top = plt.Rectangle((x_start, y_core), x_end - x_start, y_clad - y_core,
                             facecolor=LAV, edgecolor="none", zorder=1)
    clad_bot = plt.Rectangle((x_start, -y_clad), x_end - x_start, y_clad - y_core,
                             facecolor=LAV, edgecolor="none", zorder=1)
    ax.add_patch(clad_top)
    ax.add_patch(clad_bot)

    # Core region
    core = plt.Rectangle((x_start, -y_core), x_end - x_start, 2 * y_core,
                         facecolor=CREAM, edgecolor="none", zorder=1)
    ax.add_patch(core)

    # Boundary lines
    # Core-cladding boundaries
    ax.plot([x_start, x_end], [y_core, y_core], color=INK, lw=2.2, zorder=3)
    ax.plot([x_start, x_end], [-y_core, -y_core], color=INK, lw=2.2, zorder=3)
    # Outer cladding boundaries
    ax.plot([x_start, x_end], [y_clad, y_clad], color=DEEP["lav"], lw=2.2, zorder=3)
    ax.plot([x_start, x_end], [-y_clad, -y_clad], color=DEEP["lav"], lw=2.2, zorder=3)
    # Entrance boundary (left end)
    ax.plot([x_start, x_start], [-y_clad, y_clad], color=INK, lw=2.5, zorder=3)

    # Zigzag ray path
    # Ray enters at (1.0, -0.3), goes up to (3.2, 1.3), down to (6.0, -1.3), up to (8.8, 1.3), down to (11.5, -1.1)
    ray_x = [-0.6, 1.0, 3.2, 6.0, 8.8, 11.5, 12.3]
    ray_y = [-0.9, -0.3, 1.3, -1.3, 1.3, -1.1, -1.4]

    ax.plot(ray_x, ray_y, color=DEEP["pink"], lw=3.2, zorder=5)

    # Direction arrows along ray segments
    def add_arrow(p1, p2):
        mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        dx = (p2[0] - p1[0]) * 0.001
        dy = (p2[1] - p1[1]) * 0.001
        ax.annotate("", xy=(mid[0] + dx, mid[1] + dy), xytext=mid,
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.2, mutation_scale=16),
                    zorder=6)

    for i in range(len(ray_x) - 1):
        add_arrow((ray_x[i], ray_y[i]), (ray_x[i+1], ray_y[i+1]))

    # Normal line at first internal reflection point
    pt_refl = (3.2, 1.3)
    ax.plot([pt_refl[0], pt_refl[0]], [0.3, 2.3], color=GREY, lw=1.6, linestyle=":", zorder=4)

    # Title
    ax.text(6.0, 3.7, "Cross-Section of an Optical Fibre",
            fontsize=17, fontweight="bold", ha="center", va="center", color=INK)

    # Incident light ray callout
    ax.annotate("Incident light ray", xy=(0.2, -0.6), xytext=(-0.4, 0.7),
                fontsize=14, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # TIR callout at top reflection point
    ax.annotate("Total internal reflection (TIR)\nat Core–Cladding boundary",
                xy=pt_refl, xytext=(4.3, 2.9),
                fontsize=14, color=INK, ha="left",
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # Cladding label (positioned completely outside the fibre with an arrow, preventing ray overlap)
    ax.annotate("Cladding (lower refractive index, $n_2$)",
                xy=(10.0, 2.0), xytext=(10.0, 3.2),
                fontsize=14, ha="center", va="center", color=INK,
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["lav"], lw=1.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                zorder=7)

    # Core label (placed below the fibre with an arrow into the core, avoiding any ray crossings)
    ax.annotate("Core (high refractive index, $n_1 > n_2$)",
                xy=(6.0, 0.0), xytext=(6.0, -3.4),
                fontsize=14, fontweight="semibold", ha="center", va="center", color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["orange"], lw=1.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                zorder=7)

    save(fig, out)
