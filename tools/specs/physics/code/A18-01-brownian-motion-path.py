from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title
    ax.text(5, 7.5, "Brownian Motion of a Smoke Particle", fontsize=18, fontweight="bold", 
            ha="center", va="center", color=INK)

    # Zig-zag path of smoke particle history leading to the center
    # Center position: (5.2, 4.0)
    path_x = [1.5, 2.8, 2.2, 3.8, 3.2, 4.4, 5.2]
    path_y = [2.0, 2.6, 4.2, 4.8, 3.1, 2.5, 4.0]

    # Draw the path
    ax.plot(path_x, path_y, color=DEEP["lav"], lw=2.5, linestyle="--", zorder=2)
    # Small dots at previous positions
    ax.scatter(path_x[:-1], path_y[:-1], color=DEEP["lav"], s=30, zorder=3)

    # Label for path
    ax.annotate("Random zig-zag\npath of particle", xy=(2.8, 2.6), xytext=(1.8, 1.2),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=6)

    # Draw jagged smoke particle at (5.2, 4.0)
    # Create irregular polygon vertices
    cx, cy = 5.2, 4.0
    r_angles = np.linspace(0, 2 * np.pi, 14, endpoint=False)
    radii = [0.85, 0.65, 0.95, 0.70, 0.88, 0.60, 0.92, 0.75, 0.90, 0.68, 0.82, 0.62, 0.85, 0.70]
    poly_x = cx + np.array(radii) * np.cos(r_angles)
    poly_y = cy + np.array(radii) * np.sin(r_angles)
    
    ax.fill(poly_x, poly_y, color=GREY, ec=INK, lw=2.5, zorder=4)

    # Label for smoke particle
    ax.annotate("Large smoke particle\n(visible under microscope)", xy=(cx, cy + 0.9), xytext=(5.2, 6.5),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=6)

    # Surrounding fast-moving tiny air molecules bombarding the particle
    # (x, y, dx, dy)
    molecules = [
        (3.4, 5.6, 1.2, -1.0),
        (6.8, 5.8, -1.1, -1.2),
        (7.5, 4.2, -1.5, -0.1),
        (6.8, 2.3, -1.1, 1.1),
        (4.0, 2.2, 0.9, 1.2),
        (3.0, 3.8, 1.4, 0.1),
        (5.5, 2.0, -0.2, 1.3),
        (5.0, 6.0, 0.1, -1.3),
    ]

    for mx, my, dx, dy in molecules:
        # Air molecule circle
        ax.scatter([mx], [my], color=BLUE, edgecolors=DEEP["blue"], s=90, lw=1.5, zorder=5)
        # Velocity arrow pointing towards collision
        ax.annotate("", xy=(mx + dx * 0.8, my + dy * 0.8), xytext=(mx, my),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0), zorder=4)

    # Label for air molecules
    ax.annotate("Fast-moving, invisible\nair molecules bombarding\nfrom random directions", 
                xy=(6.8, 5.8), xytext=(8.0, 6.4),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=6)

    # Explanation note at bottom
    ax.text(5.0, 0.4, "Unequal bombardment from air molecules causes continuous, erratic motion",
            fontsize=14, ha="center", va="center", color=INK, style="italic",
            bbox=dict(fc=CREAM, ec="none", boxstyle="round,pad=0.4"))

    save(fig, out)
