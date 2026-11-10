from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)

    # Set limits
    xlim = (-3, 3)
    ylim = (-3, 5)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')

    # Grid
    ax.grid(True, which='both', color=GREY, linestyle='-', linewidth=0.7, alpha=0.4)

    # Axes lines with arrows through origin
    ax.axhline(0, color=INK, linewidth=1.5)
    ax.axvline(0, color=INK, linewidth=1.5)

    # Axis arrows
    ax.plot(xlim[1], 0, marker='>', markersize=8, color=INK, clip_on=False)
    ax.plot(0, ylim[1], marker='^', markersize=8, color=INK, clip_on=False)

    # Line definition: y = 2x + 1
    x_vals = np.linspace(-3, 3, 200)
    y_vals = 2 * x_vals + 1

    # Shaded region below the line: y <= 2x + 1 (Unwanted region)
    ax.fill_between(
        x_vals, ylim[0], y_vals,
        facecolor='none',
        hatch='//',
        edgecolor=GREY,
        linewidth=0.0
    )

    # Dashed boundary line
    ax.plot(x_vals, y_vals, linestyle='--', color=DEEP["blue"], linewidth=2.5)

    # Key points on the line: (0, 1) and (-0.5, 0)
    ax.plot([0, -0.5], [1, 0], 'o', color=DEEP["blue"], markersize=6, zorder=5)

    # Axis tick labels styling
    ax.set_xticks(range(-3, 4))
    ax.set_yticks(range(-3, 6))
    ax.tick_params(colors=INK, labelsize=14)

    # Axis name labels
    ax.text(xlim[1] - 0.15, -0.4, "x", fontsize=16, color=INK, fontweight='bold')
    ax.text(0.2, ylim[1] - 0.2, "y", fontsize=16, color=INK, fontweight='bold')

    # Line label: "y = 2x + 1"
    ax.text(
        1.1, 4.0, "y = 2x + 1",
        fontsize=15, color=DEEP["blue"],
        bbox=dict(facecolor='white', edgecolor='none', pad=2.0)
    )

    # Region labels
    # Required region: y > 2x + 1 (above line)
    ax.text(
        -2.2, 2.5, "Required region: y > 2x + 1",
        fontsize=14.5, color=INK,
        bbox=dict(facecolor='white', edgecolor=DEEP["blue"], boxstyle='round,pad=0.4', lw=1.2)
    )

    # Unwanted region (shaded) (below line, near origin)
    ax.text(
        0.5, -1.5, "Unwanted region (shaded)",
        fontsize=14.5, color=INK,
        bbox=dict(facecolor='white', edgecolor=GREY, boxstyle='round,pad=0.4', lw=1.2)
    )

    # Remove outer spines for clean textbook plane
    for spine in ax.spines.values():
        spine.set_visible(False)

    save(fig, out)
