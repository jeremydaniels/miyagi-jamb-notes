from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0.05, 0.08, 0.9, 0.84])
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.5, 6.5)
    ax.axis("off")

    # Title
    ax.text(5.0, 6.0, "Accounting Year-End Adjustments", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)

    # Financial Year Main Bar / Timeline
    y_tl = 3.2
    # Background bar for Current Financial Year
    ax.fill_between([1.0, 8.5], [y_tl - 0.22, y_tl - 0.22], [y_tl + 0.22, y_tl + 0.22],
                    color=BLUE, alpha=0.35, zorder=1)
    # Next year segment
    ax.fill_between([8.5, 10.5], [y_tl - 0.22, y_tl - 0.22], [y_tl + 0.22, y_tl + 0.22],
                    color=GREY, alpha=0.25, linestyle="--", zorder=1)

    # Timeline main axis line
    ax.plot([0.5, 10.8], [y_tl, y_tl], color=INK, lw=3, zorder=2)
    # Arrow tip for time flow
    ax.annotate("", xy=(11.0, y_tl), xytext=(10.7, y_tl),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=3, mutation_scale=18))

    # Ticks and Labels for Dates
    dates = [(1.0, "1 January\n(Start of Year)"), 
             (8.5, "31 December\n(Financial Year End)")]
    
    for x_pos, label in dates:
        ax.plot([x_pos, x_pos], [y_tl - 0.45, y_tl + 0.45], color=INK, lw=2.5, zorder=3)
        ax.text(x_pos, y_tl - 0.7, label, ha="center", va="top", fontsize=14,
                fontweight="bold", color=INK)

    # Middle label for Current Financial Year
    ax.text(4.75, y_tl + 0.35, "Current Financial Year", ha="center", va="bottom",
            fontsize=15, fontweight="bold", color=DEEP["blue"])

    # Next Financial Year label
    ax.text(9.6, y_tl + 0.35, "Next Year", ha="center", va="bottom",
            fontsize=14, fontstyle="italic", color=INK)

    # 1. Prepayment (Upper section)
    # Arrow extending past 31 December
    y_pre = 4.7
    ax.annotate("", xy=(10.2, y_pre), xytext=(6.5, y_pre),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3.5, mutation_scale=22))
    # Dashed line showing threshold of 31 Dec crossing
    ax.plot([8.5, 8.5], [y_tl + 0.45, y_pre + 0.4], color=DEEP["green"], ls=":", lw=2)

    pre_text = (
        "Prepayment (paid for next year, subtract from expense, Current Asset)"
    )
    ax.text(8.35, y_pre + 0.4, pre_text, ha="center", va="bottom", fontsize=14,
            fontweight="bold", color=DEEP["green"],
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["green"], lw=1.5))

    # 2. Accrual (Lower section)
    # Arrow pointing just before 31 December with a gap to the end
    y_acc = 1.6
    ax.annotate("", xy=(7.0, y_acc), xytext=(2.5, y_acc),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3.5, mutation_scale=22))

    # Gap bracket / indicator between 7.0 and 8.5
    ax.plot([7.0, 8.5], [y_acc, y_acc], color=DEEP["pink"], ls="--", lw=2.5)
    ax.plot([7.0, 7.0], [y_acc - 0.2, y_acc + 0.2], color=DEEP["pink"], lw=2)
    ax.plot([8.5, 8.5], [y_acc - 0.2, y_tl - 0.45], color=DEEP["pink"], ls=":", lw=2)
    ax.text(7.75, y_acc + 0.25, "Unpaid period\n(Gap)", ha="center", va="bottom",
            fontsize=14, color=DEEP["pink"], fontweight="bold")

    acc_text = (
        "Accrual (used this year but not paid, add to expense, Current Liability)"
    )
    ax.text(5.5, y_acc - 0.5, acc_text, ha="center", va="top", fontsize=14,
            fontweight="bold", color=DEEP["pink"],
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["pink"], lw=1.5))

    save(fig, out)
