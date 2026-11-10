from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # Main title
    ax.text(6.0, 8.4, "Text Alignment Types", fontsize=20, weight='bold', ha='center', va='center', color=INK)

    # Relative line lengths for visual text simulation
    line_ratios = [1.0, 0.85, 0.95, 0.72, 0.88, 0.55]
    max_w = 3.6
    line_h = 0.20

    # Configurations for the 4 boxes: (bx, by, title, desc, align, bg_col, line_col)
    configs = [
        (0.9, 4.6, "1. Left aligned", "Straight left edge, jagged right", "left", BLUE, DEEP["blue"]),
        (6.5, 4.6, "2. Center aligned", "Jagged on both sides, centered", "center", GREEN, DEEP["green"]),
        (0.9, 0.7, "3. Right aligned", "Jagged left edge, straight right", "right", ORANGE, DEEP["orange"]),
        (6.5, 0.7, "4. Justified", "Straight edges on both left and right", "justify", LAV, DEEP["lav"]),
    ]

    for (bx, by, title, desc, align, bg_col, line_col) in configs:
        # Card background
        rect = patches.FancyBboxPatch(
            (bx, by), 4.6, 3.3,
            boxstyle="round,pad=0.08,rounding_size=0.18",
            facecolor="white", edgecolor=GREY, linewidth=1.5
        )
        ax.add_patch(rect)

        # Header accent bar
        header_bar = patches.FancyBboxPatch(
            (bx + 0.15, by + 2.5), 4.3, 0.65,
            boxstyle="round,pad=0.03,rounding_size=0.1",
            facecolor=bg_col, edgecolor="none", alpha=0.35
        )
        ax.add_patch(header_bar)

        # Title and Description (ensure fontsize >= 14)
        ax.text(bx + 2.3, by + 2.82, title, fontsize=16, weight='bold', ha='center', va='center', color=INK)
        ax.text(bx + 2.3, by + 2.25, desc, fontsize=14, ha='center', va='center', color=INK)

        # Content area coordinates
        content_left = bx + 0.5
        content_right = bx + 4.1
        content_top = by + 1.85
        line_gap = 0.28

        # Margin alignment guides (dashed lines indicating edges)
        guide_y_bottom = content_top - (len(line_ratios) - 1) * line_gap - 0.15
        guide_y_top = content_top + 0.15

        if align in ["left", "justify"]:
            ax.plot([content_left, content_left], [guide_y_bottom, guide_y_top],
                    color=line_col, lw=1.8, ls="--", alpha=0.6)
        if align in ["right", "justify"]:
            ax.plot([content_right, content_right], [guide_y_bottom, guide_y_top],
                    color=line_col, lw=1.8, ls="--", alpha=0.6)
        if align == "center":
            center_x = (content_left + content_right) / 2
            ax.plot([center_x, center_x], [guide_y_bottom, guide_y_top],
                    color=line_col, lw=1.8, ls=":", alpha=0.6)

        # Draw lines of text
        for i, ratio in enumerate(line_ratios):
            ly = content_top - i * line_gap
            lw_len = max_w * ratio

            if align == "left":
                lx = content_left
                cur_len = lw_len if i < len(line_ratios) - 1 else max_w * 0.48
            elif align == "right":
                cur_len = lw_len if i < len(line_ratios) - 1 else max_w * 0.48
                lx = content_right - cur_len
            elif align == "center":
                cur_len = lw_len if i < len(line_ratios) - 1 else max_w * 0.45
                lx = (content_left + content_right) / 2 - cur_len / 2
            elif align == "justify":
                if i < len(line_ratios) - 1:
                    cur_len = max_w
                    lx = content_left
                else:
                    cur_len = max_w * 0.45
                    lx = content_left

            line_patch = patches.FancyBboxPatch(
                (lx, ly - line_h / 2), cur_len, line_h,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                facecolor=line_col, edgecolor="none", alpha=0.85
            )
            ax.add_patch(line_patch)

    save(fig, out)
