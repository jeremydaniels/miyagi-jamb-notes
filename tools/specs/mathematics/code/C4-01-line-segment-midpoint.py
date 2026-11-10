from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)

    # Set up coordinate ranges
    xmin, xmax = -5, 7
    ymin, ymax = -4, 8

    # Background grid
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('equal')
    
    # Grid lines
    ax.set_xticks(np.arange(xmin, xmax + 1, 1))
    ax.set_yticks(np.arange(ymin, ymax + 1, 1))
    ax.grid(True, which='both', color=GREY, linestyle='-', linewidth=0.8, alpha=0.6)

    # Hide default spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Draw centered x and y axes with arrows
    arrow_props = dict(arrowstyle="-|>", color=INK, lw=1.8, mutation_scale=12)
    ax.annotate("", xy=(xmax - 0.2, 0), xytext=(xmin + 0.2, 0), arrowprops=arrow_props)
    ax.annotate("", xy=(0, ymax - 0.2), xytext=(0, ymin + 0.2), arrowprops=arrow_props)

    # Axis labels
    ax.text(xmax - 0.2, -0.6, "$x$", fontsize=16, color=INK, ha='center', va='center', weight='bold')
    ax.text(-0.5, ymax - 0.2, "$y$", fontsize=16, color=INK, ha='center', va='center', weight='bold')

    # Selected tick labels on axes
    for x in range(xmin + 1, xmax):
        if x != 0 and x % 2 == 1:
            ax.text(x, -0.45, str(x), fontsize=14, color=INK, ha='center', va='top')
    for y in range(ymin + 1, ymax):
        if y != 0 and y % 2 == 0:
            ax.text(-0.35, y, str(y), fontsize=14, color=INK, ha='right', va='center')
    ax.text(-0.35, -0.45, "0", fontsize=14, color=INK, ha='right', va='top')

    # Points coordinates
    xA, yA = -3, 6
    xB, yB = 5, -2
    xM, yM = 1, 2

    # Draw line segment AB
    ax.plot([xA, xB], [yA, yB], color=DEEP["blue"], lw=3, zorder=3)

    # Draw point markers
    ax.scatter([xA, xB], [yA, yB], color=DEEP["blue"], s=80, zorder=4)
    ax.scatter([xM], [yM], color=DEEP["orange"], s=100, edgecolors=INK, linewidth=1.5, zorder=5)

    # Annotations / labels with clean white bounding boxes
    bbox_style = dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8)
    ax.text(xA - 0.3, yA + 0.4, "A(-3, 6)", fontsize=15, color=INK, weight='bold',
            ha='right', va='bottom', bbox=bbox_style, zorder=6)
    ax.text(xB + 0.3, yB - 0.4, "B(5, -2)", fontsize=15, color=INK, weight='bold',
            ha='left', va='top', bbox=bbox_style, zorder=6)
    ax.text(xM + 0.4, yM + 0.4, "M(1, 2)", fontsize=15, color=DEEP["orange"], weight='bold',
            ha='left', va='bottom', bbox=bbox_style, zorder=6)

    # Remove tick marks to keep standard textbook sketch appearance
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    save(fig, out)
