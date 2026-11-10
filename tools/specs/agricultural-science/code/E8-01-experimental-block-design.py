from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(5.5, 7.0, "Randomized Complete Block Design (RCBD)", fontsize=18,
            fontweight="bold", ha="center", va="center", color=INK)

    # Gradient Arrow at top (Soil fertility gradient)
    ax.annotate("", xy=(9.7, 6.35), xytext=(1.3, 6.35),
                arrowprops=dict(arrowstyle="->", lw=3.0, color=DEEP["orange"]))
    ax.text(5.5, 6.55, "Soil fertility gradient (increases right)", fontsize=14,
            ha="center", va="center", color=INK, fontweight="semibold")

    # Block columns specifications
    blocks_data = [
        {"x": 1.0, "title": "Block 1 (Low fertility)", "plots": ["T1", "C", "T2"]},
        {"x": 4.1, "title": "Block 2 (Medium fertility)", "plots": ["C", "T2", "T1"]},
        {"x": 7.2, "title": "Block 3 (High fertility)", "plots": ["T2", "T1", "C"]},
    ]

    block_w = 2.8
    block_h = 4.4
    plot_w = 2.4
    plot_h = 1.15

    # Treatment colors & styling
    treat_colors = {
        "T1": (GREEN, DEEP["green"]),
        "T2": (BLUE, DEEP["blue"]),
        "C":  (CREAM, GREY)
    }

    y_start = 1.4

    for b in blocks_data:
        bx = b["x"]
        # Outer block container
        block_rect = patches.FancyBboxPatch(
            (bx, y_start), block_w, block_h,
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor="#FBFBFA", edgecolor=GREY, lw=1.5, linestyle="--"
        )
        ax.add_patch(block_rect)

        # Block header label
        ax.text(bx + block_w / 2, y_start + block_h - 0.32, b["title"],
                fontsize=14, ha="center", va="center", color=INK, fontweight="bold")

        # 3 Plot rows inside block (from top to bottom)
        py_positions = [y_start + 2.65, y_start + 1.45, y_start + 0.25]
        for plot_name, py in zip(b["plots"], py_positions):
            px = bx + (block_w - plot_w) / 2
            fc, ec = treat_colors[plot_name]
            plot_rect = patches.FancyBboxPatch(
                (px, py), plot_w, plot_h,
                boxstyle="round,pad=0.04,rounding_size=0.1",
                facecolor=fc, edgecolor=ec, lw=2.0
            )
            ax.add_patch(plot_rect)

            # Label text inside plot
            if plot_name == "T1":
                label = "Treatment 1 (T1)"
            elif plot_name == "T2":
                label = "Treatment 2 (T2)"
            else:
                label = "Control (C)"

            ax.text(px + plot_w / 2, py + plot_h / 2, label,
                    fontsize=14, ha="center", va="center", color=INK, fontweight="semibold")

    # Bottom notes / legend
    ax.text(5.5, 1.05, "Randomized plot assignment within each block",
            fontsize=14, ha="center", va="center", style="italic", color=INK)

    # Legend elements at bottom
    leg_y = 0.5
    # T1 indicator
    ax.add_patch(patches.Rectangle((1.5, leg_y - 0.15), 0.45, 0.3, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5))
    ax.text(2.1, leg_y, "Treatment (T1)", fontsize=14, va="center", color=INK)

    # T2 indicator
    ax.add_patch(patches.Rectangle((4.4, leg_y - 0.15), 0.45, 0.3, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5))
    ax.text(5.0, leg_y, "Treatment (T2)", fontsize=14, va="center", color=INK)

    # Control indicator
    ax.add_patch(patches.Rectangle((7.4, leg_y - 0.15), 0.45, 0.3, facecolor=CREAM, edgecolor=GREY, lw=1.5))
    ax.text(8.0, leg_y, "Control (C)", fontsize=14, va="center", color=INK)

    save(fig, out)
