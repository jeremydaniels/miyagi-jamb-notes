from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 9.5)
    ax.set_ylim(-0.5, 8.5)
    ax.axis("off")

    # Base / Nut body of the jack
    # Ground hatching
    ax.plot([1.0, 5.0], [0.5, 0.5], color=INK, lw=2.5)
    for gx in np.linspace(1.2, 4.8, 10):
        ax.plot([gx, gx - 0.25], [0.5, 0.2], color=GREY, lw=1.5)

    # Jack frame/base
    base_x = [1.2, 2.0, 2.0, 4.0, 4.0, 4.8]
    base_y = [0.5, 1.2, 3.2, 3.2, 1.2, 0.5]
    ax.fill(base_x, base_y, color=CREAM, ec=INK, lw=2, zorder=2)
    # Inner threaded collar of base
    ax.fill_between([2.0, 4.0], 1.2, 3.2, color=GREY, alpha=0.15, zorder=2)

    # Threaded screw spindle (center at x = 3.0, width = 1.2, extends from y = 1.8 to 5.2)
    screw_left = 2.4
    screw_right = 3.6
    pitch = 0.4
    y_starts = np.arange(2.0, 5.0, pitch)

    # Draw screw cylinder background
    ax.fill_between([screw_left, screw_right], 2.0, 5.2, color=LAV, alpha=0.3, zorder=3)
    ax.plot([screw_left, screw_left], [2.0, 5.2], color=INK, lw=2, zorder=4)
    ax.plot([screw_right, screw_right], [2.0, 5.2], color=INK, lw=2, zorder=4)

    # Threads
    for ys in y_starts:
        ax.plot([screw_left, screw_right], [ys, ys + pitch * 0.5], color=DEEP["lav"], lw=2.5, zorder=5)

    # Pitch annotation between two adjacent threads
    p_y1 = 3.8
    p_y2 = p_y1 + pitch
    ax.annotate("", xy=(screw_left - 0.2, p_y1), xytext=(screw_left - 0.2, p_y2),
                arrowprops=dict(arrowstyle="<->", color=DEEP["pink"], lw=1.8), zorder=6)
    ax.plot([screw_left - 0.35, screw_left], [p_y1, p_y1], color=GREY, lw=1, ls="--", zorder=6)
    ax.plot([screw_left - 0.35, screw_left], [p_y2, p_y2], color=GREY, lw=1, ls="--", zorder=6)
    ax.text(screw_left - 0.45, (p_y1 + p_y2) / 2, "Pitch (p)",
            ha="right", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=1), zorder=7)

    # Top collar / turntable on screw
    collar = plt.Rectangle((2.1, 5.0), 1.8, 0.4, facecolor=CREAM, edgecolor=INK, lw=2, zorder=6)
    ax.add_patch(collar)

    # Horizontal handle (tommy bar) of length 'r'
    bar_y = 5.2
    ax.plot([3.0, 8.0], [bar_y, bar_y], color=DEEP["blue"], lw=6, solid_capstyle="round", zorder=7)

    # Dimension 'r' below the tommy bar
    dim_y = bar_y - 0.5
    ax.annotate("", xy=(3.0, dim_y), xytext=(8.0, dim_y),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8), zorder=8)
    ax.plot([3.0, 3.0], [dim_y - 0.2, bar_y - 0.1], color=GREY, lw=1, ls="--", zorder=8)
    ax.plot([8.0, 8.0], [dim_y - 0.2, bar_y - 0.1], color=GREY, lw=1, ls="--", zorder=8)
    ax.text(5.5, dim_y - 0.15, "r", ha="center", va="top", fontsize=16, color=INK,
            bbox=dict(fc="white", ec="none", pad=1), zorder=9)

    # Effort (E) downward arrow at the end of the handle
    ax.annotate("", xy=(8.0, bar_y - 2.0), xytext=(8.0, bar_y),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["orange"], lw=3.5, mutation_scale=22), zorder=8)
    ax.text(8.0, bar_y - 2.2, "Effort (E)", ha="center", va="top", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=1), zorder=9)

    # Load (L) - large weight resting on top of the jack
    load_rect = plt.Rectangle((1.2, 5.6), 3.6, 2.0, facecolor=BLUE, edgecolor=INK, lw=2.5, zorder=6)
    ax.add_patch(load_rect)
    ax.text(3.0, 6.6, "Load (L)", ha="center", va="center", fontsize=18, weight="bold", color=INK, zorder=10)

    save(fig, out)
