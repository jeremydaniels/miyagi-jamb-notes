from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0.05, 0.08, 0.9, 0.84])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(5, 6.5, "Battle of Tel el-Kebir (1882)", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    # Desert background zone
    desert_patch = plt.Rectangle((0.5, 0.6), 9.0, 5.2, facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=1)
    ax.add_patch(desert_patch)
    ax.text(5.0, 0.95, "Flat desert terrain", ha="center", va="center",
            fontsize=14, style="italic", color=INK,
            bbox=dict(boxstyle="round,pad=0.2", facecolor=CREAM, edgecolor="none"))

    # Canal / Railway feature schematic (historical Sweet Water Canal / railway along south)
    ax.plot([0.5, 9.5], [1.4, 1.4], color=DEEP["blue"], lw=3, zorder=2)
    ax.text(8.5, 1.65, "Sweet Water Canal", ha="right", va="bottom",
            fontsize=14, color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["blue"], lw=0.8))

    # Egyptian Entrenchments / Lines (Zig-zag defensive works on the left)
    egypt_x = [2.6, 2.8, 2.5, 2.7, 2.5, 2.7, 2.6]
    egypt_y = [1.8, 2.3, 3.0, 3.7, 4.4, 5.1, 5.5]
    ax.plot(egypt_x, egypt_y, color=DEEP["orange"], lw=5, zorder=3)

    # Secondary redoubt / ditch marks
    for y in np.linspace(1.9, 5.4, 8):
        ax.plot([2.1, 2.6], [y, y], color=DEEP["orange"], lw=2, zorder=2)

    # Label for Urabi's forces
    ax.text(2.0, 3.65, "Urabi's forces\n(Egyptians)", ha="center", va="center",
            fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=DEEP["orange"], lw=2),
            zorder=4)

    # British advance arrows (night march / dawn assault pointing left)
    arrow_starts = [(7.5, 4.8), (7.5, 3.7), (7.5, 2.5)]
    arrow_ends   = [(3.5, 4.8), (3.5, 3.7), (3.5, 2.5)]
    
    for (sx, sy), (ex, ey) in zip(arrow_starts, arrow_ends):
        ax.annotate("", xy=(ex, ey), xytext=(sx, sy),
                    arrowprops=dict(facecolor=DEEP["pink"], edgecolor=DEEP["pink"],
                                    width=4, headwidth=12, headlength=14),
                    zorder=3)

    # Label for British forces
    ax.text(7.6, 3.7, "British forces\n(Dawn assault)", ha="center", va="center",
            fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=DEEP["pink"], lw=2),
            zorder=4)

    # Prominent label: "1882: British occupation begins"
    ax.text(5.0, 5.3, "1882: British occupation begins", ha="center", va="center",
            fontsize=16, weight="bold", color=INK,
            bbox=dict(boxstyle="square,pad=0.5", facecolor=LAV, edgecolor=INK, lw=1.5),
            zorder=5)

    save(fig, out)
