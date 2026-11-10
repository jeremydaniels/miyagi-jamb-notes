from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.3, "Converting Mark-up to Margin", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Box 1: Mark-up
    box_markup = patches.FancyBboxPatch((0.8, 3.2), 3.0, 1.3,
                                        boxstyle="round,pad=0.15",
                                        facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(box_markup)
    ax.text(2.3, 4.05, "MARK-UP", ha='center', va='center', fontsize=15, fontweight='bold', color=INK)
    ax.text(2.3, 3.6, "(Fraction of Cost)", ha='center', va='center', fontsize=14, color=INK)

    # Box 2: Margin
    box_margin = patches.FancyBboxPatch((6.2, 3.2), 3.0, 1.3,
                                        boxstyle="round,pad=0.15",
                                        facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(box_margin)
    ax.text(7.7, 4.05, "MARGIN", ha='center', va='center', fontsize=15, fontweight='bold', color=INK)
    ax.text(7.7, 3.6, "(Fraction of Sales)", ha='center', va='center', fontsize=14, color=INK)

    # Arrow between top boxes
    arrow_top = patches.FancyArrowPatch((4.0, 3.85), (6.0, 3.85),
                                       arrowstyle='->,head_width=0.4,head_length=0.6',
                                       color=DEEP["blue"], lw=2.5)
    ax.add_patch(arrow_top)
    
    # Label on arrow
    ax.text(5.0, 4.25, "Add numerator\nto denominator", 
            ha='center', va='bottom', fontsize=14, fontweight='bold', color=DEEP["blue"],
            bbox=dict(fc='white', ec='none', pad=2))

    # General formula below the arrow
    ax.text(2.3, 2.3, r"$\frac{a}{b}$", ha='center', va='center', fontsize=18, color=INK)
    arrow_mid = patches.FancyArrowPatch((3.5, 2.3), (6.5, 2.3),
                                       arrowstyle='->,head_width=0.3,head_length=0.5',
                                       color=GREY, lw=2)
    ax.add_patch(arrow_mid)
    ax.text(5.0, 2.3, r"$\frac{a}{b + a}$", ha='center', va='center', fontsize=18, color=DEEP["blue"],
            bbox=dict(fc='white', ec='none', pad=3))
    ax.text(7.7, 2.3, r"$\frac{a}{c}$", ha='center', va='center', fontsize=18, color=INK)

    # Example section box / panel
    ex_bg = patches.FancyBboxPatch((1.2, 0.4), 7.6, 1.3,
                                   boxstyle="round,pad=0.1",
                                   facecolor=LAV, edgecolor=DEEP["lav"], lw=1.5)
    ax.add_patch(ex_bg)

    ax.text(1.6, 1.05, "Example:", ha='left', va='center', fontsize=15, fontweight='bold', color=INK)

    # 1/4 -> 1/(4+1) -> 1/5
    ax.text(3.7, 1.05, r"$\frac{1}{4}$", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    
    arrow_ex1 = patches.FancyArrowPatch((4.3, 1.05), (5.1, 1.05),
                                        arrowstyle='->,head_width=0.3,head_length=0.4',
                                        color=INK, lw=2)
    ax.add_patch(arrow_ex1)

    ax.text(5.9, 1.05, r"$\frac{1}{4 + 1}$", ha='center', va='center', fontsize=18, fontweight='bold', color=DEEP["orange"])

    arrow_ex2 = patches.FancyArrowPatch((6.7, 1.05), (7.5, 1.05),
                                        arrowstyle='->,head_width=0.3,head_length=0.4',
                                        color=INK, lw=2)
    ax.add_patch(arrow_ex2)

    ax.text(8.1, 1.05, r"$\frac{1}{5}$", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    save(fig, out)
