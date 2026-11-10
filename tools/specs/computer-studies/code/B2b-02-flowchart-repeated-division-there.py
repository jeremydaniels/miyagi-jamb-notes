import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)

    # Title
    ax.text(5, 7.9, "Repeated Division of 45 by 2 (Decimal to Binary)", 
            fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Column Headers
    headers = ["Division", "Quotient", "Remainder"]
    col_x = [2.2, 4.6, 6.8]
    header_y = 6.9

    # Header backgrounds
    header_box_w = [2.6, 1.8, 2.0]
    for i, (x, w) in enumerate(zip(col_x, header_box_w)):
        rect = plt.Rectangle((x - w/2, header_y - 0.35), w, 0.7, 
                             facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
        ax.add_patch(rect)
        ax.text(x, header_y, headers[i], fontsize=16, fontweight='bold', 
                ha='center', va='center', color=INK, zorder=2)

    # Division steps for 45 / 2
    # 45 / 2 = 22 R 1
    # 22 / 2 = 11 R 0
    # 11 / 2 = 5  R 1
    #  5 / 2 = 2  R 1
    #  2 / 2 = 1  R 0
    #  1 / 2 = 0  R 1
    steps = [
        ("45 ÷ 2", "22", "1"),
        ("22 ÷ 2", "11", "0"),
        ("11 ÷ 2", "5",  "1"),
        ("5 ÷ 2",  "2",  "1"),
        ("2 ÷ 2",  "1",  "0"),
        ("1 ÷ 2",  "0",  "1")
    ]

    start_y = 5.9
    dy = 0.75

    for row_idx, (div, quot, rem) in enumerate(steps):
        y = start_y - row_idx * dy
        # Alternating subtle row shading
        bg_col = "white" if row_idx % 2 == 0 else "#F7F8F9"
        row_rect = plt.Rectangle((0.8, y - 0.32), 7.2, 0.64, 
                                 facecolor=bg_col, edgecolor="none", zorder=0)
        ax.add_patch(row_rect)

        # Values
        ax.text(col_x[0], y, div, fontsize=15, ha='center', va='center', color=INK)
        ax.text(col_x[1], y, quot, fontsize=15, ha='center', va='center', color=INK)
        
        # Highlight remainder
        rem_circle = plt.Circle((col_x[2], y), 0.28, facecolor=LAV, edgecolor=DEEP["blue"], lw=1.5, zorder=2)
        ax.add_patch(rem_circle)
        ax.text(col_x[2], y, rem, fontsize=16, fontweight='bold', ha='center', va='center', 
                color=DEEP["blue"], zorder=3)

    # Upward bold arrow alongside remainder column
    arrow_x = 8.1
    bottom_y = start_y - 5 * dy
    top_y = start_y

    ax.annotate(
        "",
        xy=(arrow_x, top_y + 0.15),
        xytext=(arrow_x, bottom_y - 0.15),
        arrowprops=dict(
            arrowstyle="->,head_width=0.5,head_length=0.7",
            color=DEEP["pink"],
            lw=4.0
        )
    )

    # Label along arrow
    mid_y = (top_y + bottom_y) / 2
    ax.text(arrow_x + 0.3, mid_y, "Read bottom to top",
            fontsize=15, fontweight='bold', color=DEEP["pink"],
            rotation=90, va='center', ha='left')

    # Result annotation at bottom
    result_box = plt.Rectangle((1.5, 0.4), 6.5, 0.9, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    ax.add_patch(result_box)
    ax.text(4.75, 0.85, "Binary Result:  45₁₀ = 101101₂", fontsize=16, 
            fontweight='bold', ha='center', va='center', color=INK)

    save(fig, out)
