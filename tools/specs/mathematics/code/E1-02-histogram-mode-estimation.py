from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Bin edges and frequencies
    bins = [149.5, 159.5, 169.5, 179.5, 189.5]
    freqs = [5, 15, 20, 10]

    # Draw histogram bars touching each other
    for i in range(len(freqs)):
        left = bins[i]
        width = bins[i+1] - bins[i]
        height = freqs[i]
        ax.bar(left, height, width=width, align='edge',
               facecolor=BLUE, edgecolor=DEEP["blue"], linewidth=2.0)

    # Intersection calculation for mode estimation:
    # Line 1: from top-left of tallest bar (169.5, 20) to top-left of next bar (179.5, 10)
    # Line 2: from top-right of tallest bar (179.5, 20) to top-right of previous bar (169.5, 15)
    # Line 1: y - 20 = (10 - 20)/(179.5 - 169.5) * (x - 169.5) => y - 20 = -1 * (x - 169.5)
    # Line 2: y - 20 = (15 - 20)/(169.5 - 179.5) * (x - 179.5) => y - 20 = 0.5 * (x - 179.5)
    # - (x - 169.5) = 0.5 (x - 179.5) => -1.5 x = -169.5 - 89.75 = -259.25 => x = 172.833... ≈ 172.8
    # y = 20 - (172.833 - 169.5) = 16.667

    p_tl_tall = (169.5, 20)
    p_tl_next = (179.5, 10)
    p_tr_tall = (179.5, 20)
    p_tr_prev = (169.5, 15)

    x_intersect = 172.833
    y_intersect = 16.667

    # Draw diagonal dashed lines
    ax.plot([p_tl_tall[0], p_tl_next[0]], [p_tl_tall[1], p_tl_next[1]],
            color=DEEP["pink"], linestyle="--", linewidth=2.2, zorder=5)
    ax.plot([p_tr_tall[0], p_tr_prev[0]], [p_tr_tall[1], p_tr_prev[1]],
            color=DEEP["pink"], linestyle="--", linewidth=2.2, zorder=5)

    # Vertical dashed line to the x-axis
    ax.plot([x_intersect, x_intersect], [0, y_intersect],
            color=DEEP["pink"], linestyle="--", linewidth=2.2, zorder=5)

    # Dot at intersection
    ax.plot(x_intersect, y_intersect, marker='o', markersize=6,
            color=DEEP["pink"], zorder=6)

    # Label for estimated mode
    ax.annotate("Mode ≈ 172.8 cm",
                xy=(x_intersect, 0), xytext=(x_intersect, 3),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5),
                fontsize=14, color=INK, ha="center", va="bottom",
                bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.2),
                zorder=7)

    # Formatting axes and limits
    ax.set_xlim(144.5, 194.5)
    ax.set_ylim(0, 24)

    ax.set_xticks(bins)
    ax.set_xticklabels([f"{b:.1f}" for b in bins], fontsize=14, color=INK)

    y_ticks = [0, 5, 10, 15, 20]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([str(y) for y in y_ticks], fontsize=14, color=INK)

    # Grid, spines, and labels
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":", color=GREY, alpha=0.6)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)

    ax.set_xlabel("Height (cm)", fontsize=16, color=INK, labelpad=10)
    ax.set_ylabel("Frequency", fontsize=16, color=INK, labelpad=10)
    ax.set_title("Heights of students", fontsize=18, color=INK, pad=15, weight="bold")

    fig.tight_layout()
    save(fig, out)
