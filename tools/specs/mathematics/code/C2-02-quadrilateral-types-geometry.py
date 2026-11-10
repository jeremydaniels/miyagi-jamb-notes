from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    # Canvas size 12x8 for a 2x3 grid of shapes
    fig = canvas(12, 8)
    
    # Grid: 2 rows, 3 columns
    # Row 1: Square, Rectangle, Parallelogram
    # Row 2: Rhombus, Trapezium, Kite
    
    titles = [
        "Square", "Rectangle", "Parallelogram",
        "Rhombus", "Trapezium", "Kite"
    ]
    
    # Setup 6 subplots
    axes = []
    for i in range(6):
        r = i // 3
        c = i % 3
        # Left, bottom, width, height in normalized figure coords
        ax = fig.add_axes([0.05 + c * 0.31, 0.52 - r * 0.46, 0.27, 0.40])
        ax.set_aspect("equal")
        ax.set_xlim(-0.2, 3.2)
        ax.set_ylim(-0.3, 3.1)
        ax.axis("off")
        ax.text(1.5, -0.15, titles[i], ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
        axes.append(ax)

    # 1. Square
    ax = axes[0]
    sq = patches.Polygon([[0.5, 0.5], [2.5, 0.5], [2.5, 2.5], [0.5, 2.5]], 
                         closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(sq)
    # Right angle marker in bottom-left
    ra = patches.Polygon([[0.5, 0.8], [0.8, 0.8], [0.8, 0.5]], closed=False, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(ra)

    # 2. Rectangle
    ax = axes[1]
    rect = patches.Polygon([[0.2, 0.7], [2.8, 0.7], [2.8, 2.3], [0.2, 2.3]], 
                           closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5)
    ax.add_patch(rect)
    # Right angle marker
    ra = patches.Polygon([[0.2, 1.0], [0.5, 1.0], [0.5, 0.7]], closed=False, edgecolor=DEEP["green"], lw=1.5)
    ax.add_patch(ra)

    # 3. Parallelogram (with vertical height h)
    ax = axes[2]
    pts_para = [[0.3, 0.6], [2.1, 0.6], [2.7, 2.4], [0.9, 2.4]]
    para = patches.Polygon(pts_para, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(para)
    # Height dashed line from (0.9, 2.4) down to (0.9, 0.6)
    ax.plot([0.9, 0.9], [0.6, 2.4], ls="--", color=INK, lw=1.8)
    # Right angle indicator at (0.9, 0.6)
    ra = patches.Polygon([[0.9, 0.85], [1.15, 0.85], [1.15, 0.6]], closed=False, edgecolor=INK, lw=1.5)
    ax.add_patch(ra)
    # Label h
    ax.text(0.75, 1.5, "h", fontsize=15, va="center", ha="right", color=INK, fontweight="bold")

    # 4. Rhombus (with intersecting diagonals shown)
    ax = axes[3]
    pts_rhomb = [[1.5, 0.4], [2.7, 1.5], [1.5, 2.6], [0.3, 1.5]]
    rhomb = patches.Polygon(pts_rhomb, closed=True, facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5)
    ax.add_patch(rhomb)
    # Diagonals
    ax.plot([1.5, 1.5], [0.4, 2.6], ls="--", color=DEEP["lav"], lw=1.8)
    ax.plot([0.3, 2.7], [1.5, 1.5], ls="--", color=DEEP["lav"], lw=1.8)
    # Right angle mark at center (1.5, 1.5)
    ra = patches.Polygon([[1.5, 1.75], [1.75, 1.75], [1.75, 1.5]], closed=False, edgecolor=DEEP["lav"], lw=1.5)
    ax.add_patch(ra)

    # 5. Trapezium
    ax = axes[4]
    pts_trap = [[0.3, 0.6], [2.7, 0.6], [2.1, 2.4], [0.9, 2.4]]
    trap = patches.Polygon(pts_trap, closed=True, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(trap)
    # Parallel arrows on top and bottom bases
    ax.annotate("", xy=(1.6, 0.6), xytext=(1.4, 0.6),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2, mutation_scale=15))
    ax.annotate("", xy=(1.6, 2.4), xytext=(1.4, 2.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2, mutation_scale=15))

    # 6. Kite
    ax = axes[5]
    pts_kite = [[1.5, 0.3], [2.6, 1.8], [1.5, 2.7], [0.4, 1.8]]
    kite = patches.Polygon(pts_kite, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5)
    ax.add_patch(kite)
    # Diagonals
    ax.plot([1.5, 1.5], [0.3, 2.7], ls=":", color=DEEP["pink"], lw=1.5)
    ax.plot([0.4, 2.6], [1.8, 1.8], ls=":", color=DEEP["pink"], lw=1.5)
    # Right angle mark at intersection (1.5, 1.8)
    ra = patches.Polygon([[1.5, 2.0], [1.7, 2.0], [1.7, 1.8]], closed=False, edgecolor=DEEP["pink"], lw=1.5)
    ax.add_patch(ra)

    save(fig, out)
