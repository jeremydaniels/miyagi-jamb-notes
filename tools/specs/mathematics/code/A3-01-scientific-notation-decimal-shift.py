from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "Scientific Notation: Moving the Decimal Point", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # -------------------------------------------------------------
    # Top Section: Large number (4,500,000 -> 4.5 × 10^6)
    # Digits: 4  5  0  0  0  0  0 .
    # -------------------------------------------------------------
    top_y = 5.0
    digits_top = ['4', '5', '0', '0', '0', '0', '0']
    spacing = 0.55
    x_start_top = 1.2
    xs_top = [x_start_top + i * spacing for i in range(len(digits_top))]
    
    # Draw top digits
    for x, d in zip(xs_top, digits_top):
        ax.text(x, top_y, d, ha="center", va="center", fontsize=20, fontweight="bold", color=INK)

    # Decimal points: Original (right of last 0) and New (between 4 and 5)
    orig_dec_top_x = xs_top[-1] + spacing * 0.5
    new_dec_top_x = (xs_top[0] + xs_top[1]) / 2.0

    # Indicator dots
    ax.plot(orig_dec_top_x, top_y - 0.22, marker='o', markersize=6, color=GREY)
    ax.text(orig_dec_top_x, top_y - 0.55, "original\ndecimal", ha="center", va="top",
            fontsize=14, color=GREY,
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    ax.plot(new_dec_top_x, top_y - 0.22, marker='o', markersize=7, color=DEEP["blue"])
    ax.text(new_dec_top_x, top_y - 0.55, "new\ndecimal", ha="center", va="top",
            fontsize=14, fontweight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # 6 Arcs moving LEFT from original decimal to new decimal
    jump_points_top = [new_dec_top_x] + [(xs_top[i] + xs_top[i+1]) / 2.0 for i in range(1, 6)] + [orig_dec_top_x]
    
    for i in range(6, 0, -1):
        x_from = jump_points_top[i]
        x_to = jump_points_top[i-1]
        arc = patches.FancyArrowPatch(
            (x_from, top_y + 0.35), (x_to, top_y + 0.35),
            connectionstyle="arc3,rad=-0.5",
            arrowstyle="->,head_length=4,head_width=3",
            color=DEEP["blue"], lw=2.0
        )
        ax.add_patch(arc)
        jump_idx = 7 - i
        ax.text((x_from + x_to) / 2.0, top_y + 0.72, str(jump_idx), ha="center", va="bottom",
                fontsize=14, fontweight="bold", color=DEEP["blue"])

    # Result arrow & text for top
    ax.annotate("", xy=(6.5, top_y), xytext=(5.5, top_y),
                arrowprops=dict(arrowstyle="->,head_length=6,head_width=4", lw=2.5, color=INK))
    
    ax.text(6.8, top_y, r"$= 4.5 \times 10^6$", ha="left", va="center", fontsize=20, fontweight="bold", color=INK)
    ax.text(6.8, top_y + 0.65, "6 places left  "+r"$\rightarrow$  exponent $+6$", 
            ha="left", va="center", fontsize=15, color=DEEP["blue"], fontweight="bold")

    # Separator line with plenty of clearance from top and bottom annotations
    ax.plot([0.8, 11.2], [3.6, 3.6], color=GREY, lw=1.0, linestyle="--", alpha=0.5)

    # -------------------------------------------------------------
    # Bottom Section: Small decimal (0.00032 -> 3.2 × 10^-4)
    # Digits: 0 . 0 0 0 3 2
    # -------------------------------------------------------------
    bot_y = 1.9
    digits_bot = ['0', '0', '0', '0', '3', '2']
    x_start_bot = 1.2
    # Generous spacing so decimals and jump labels have ample room
    xs_bot = [x_start_bot] + [x_start_bot + 0.5 + i * spacing for i in range(1, len(digits_bot))]

    for i, d in enumerate(digits_bot):
        ax.text(xs_bot[i], bot_y, d, ha="center", va="center", fontsize=20, fontweight="bold", color=INK)

    orig_dec_bot_x = (xs_bot[0] + xs_bot[1]) / 2.0
    new_dec_bot_x = (xs_bot[4] + xs_bot[5]) / 2.0

    ax.plot(orig_dec_bot_x, bot_y - 0.22, marker='o', markersize=6, color=GREY)
    ax.text(orig_dec_bot_x, bot_y - 0.55, "original\ndecimal", ha="center", va="top",
            fontsize=14, color=GREY,
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    ax.plot(new_dec_bot_x, bot_y - 0.22, marker='o', markersize=7, color=DEEP["orange"])
    ax.text(new_dec_bot_x, bot_y - 0.55, "new\ndecimal", ha="center", va="top",
            fontsize=14, fontweight="bold", color=DEEP["orange"],
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # 4 Arcs moving RIGHT from orig_dec_bot_x to new_dec_bot_x
    jump_points_bot = [orig_dec_bot_x] + [(xs_bot[i] + xs_bot[i+1]) / 2.0 for i in range(1, 4)] + [new_dec_bot_x]

    for i in range(4):
        x_from = jump_points_bot[i]
        x_to = jump_points_bot[i+1]
        arc = patches.FancyArrowPatch(
            (x_from, bot_y + 0.35), (x_to, bot_y + 0.35),
            connectionstyle="arc3,rad=0.5",
            arrowstyle="->,head_length=4,head_width=3",
            color=DEEP["orange"], lw=2.0
        )
        ax.add_patch(arc)
        ax.text((x_from + x_to) / 2.0, bot_y + 0.72, str(i + 1), ha="center", va="bottom",
                fontsize=14, fontweight="bold", color=DEEP["orange"])

    # Result arrow & text for bottom
    ax.annotate("", xy=(6.5, bot_y), xytext=(5.5, bot_y),
                arrowprops=dict(arrowstyle="->,head_length=6,head_width=4", lw=2.5, color=INK))

    ax.text(6.8, bot_y, r"$= 3.2 \times 10^{-4}$", ha="left", va="center", fontsize=20, fontweight="bold", color=INK)
    ax.text(6.8, bot_y + 0.65, "4 places right  "+r"$\rightarrow$  exponent $-4$", 
            ha="left", va="center", fontsize=15, color=DEEP["orange"], fontweight="bold")

    save(fig, out)
