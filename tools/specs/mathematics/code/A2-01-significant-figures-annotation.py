from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(6.0, 7.3, "Significant Figures in Decimal Numbers", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Characters in 0.040580
    chars = ['0', '.', '0', '4', '0', '5', '8', '0']
    xs = [2.2, 2.8, 3.4, 4.6, 5.8, 7.0, 8.2, 9.4]
    y_num = 4.0

    # Draw characters
    for char, x in zip(chars, xs):
        color = GREY if char in ['0', '.'] and x < 4.0 else INK
        ax.text(x, y_num, char, fontsize=48, ha='center', va='center',
                fontfamily='monospace', fontweight='bold', color=color)

    # Label 1: First two zeros (0.0) -> "Leading zeros (Not significant)"
    # Bracket or arrow spanning x=2.2 and x=3.4
    ax.annotate("Leading zeros\n(Not significant)",
                xy=(2.8, 4.7), xytext=(2.8, 6.2),
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.0))
    # Bracket line under the arrow pointing to both 0 and .0
    ax.plot([2.2, 3.4], [4.65, 4.65], color=DEEP["pink"], lw=2)

    # Label 2: Digit 4 -> "1st significant figure"
    ax.annotate("1st significant figure",
                xy=(4.6, 3.3), xytext=(3.5, 1.8),
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["blue"], lw=1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0,
                                connectionstyle="arc3,rad=-0.1"))

    # Label 3: Zero between 4 and 5 -> "Zero between non-zero digits (Significant)"
    ax.annotate("Zero between non-zero digits\n(Significant)",
                xy=(5.8, 4.7), xytext=(5.8, 6.2),
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["green"], lw=1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0))

    # Label 4: Digit 8 -> "4th significant figure"
    ax.annotate("4th significant figure",
                xy=(8.2, 3.3), xytext=(7.5, 1.8),
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["orange"], lw=1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0,
                                connectionstyle="arc3,rad=0.1"))

    # Label 5: Final zero -> "Trailing zero after decimal point (Significant)"
    ax.annotate("Trailing zero after decimal point\n(Significant)",
                xy=(9.4, 4.7), xytext=(9.7, 6.2),
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["lav"], lw=1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=2.0))

    save(fig, out)
