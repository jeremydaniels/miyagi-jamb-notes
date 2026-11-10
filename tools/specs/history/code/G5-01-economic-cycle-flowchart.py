from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "The Cycle of Neo-Colonialism", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # Box 1: African Nation
    box_left = patches.FancyBboxPatch((0.8, 2.5), 3.0, 2.0,
                                      boxstyle="round,pad=0.2,rounding_size=0.15",
                                      facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(box_left)
    ax.text(2.3, 3.5, "African Nation", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # Box 2: Foreign Powers / Corporations
    box_right = patches.FancyBboxPatch((8.2, 2.5), 3.0, 2.0,
                                       boxstyle="round,pad=0.2,rounding_size=0.15",
                                       facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(box_right)
    ax.text(9.7, 3.5, "Foreign Powers /\nCorporations", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # Top Arrow: African Nation -> Foreign Powers
    # "Cheap Raw Materials (Cocoa, Oil, Minerals)"
    arrow_top = patches.FancyArrowPatch((3.8, 4.0), (8.2, 4.0),
                                        arrowstyle="->,head_length=8,head_width=5",
                                        connectionstyle="arc3,rad=-0.12",
                                        color=DEEP["green"], lw=2.5)
    ax.add_patch(arrow_top)
    ax.text(6.0, 4.85, "Cheap Raw Materials\n(Cocoa, Oil, Minerals)",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.0))

    # Bottom Arrow: Foreign Powers -> African Nation
    # "Expensive Manufactured Goods & High-Interest Loans"
    arrow_bottom = patches.FancyArrowPatch((8.2, 3.0), (3.8, 3.0),
                                           arrowstyle="->,head_length=8,head_width=5",
                                           connectionstyle="arc3,rad=-0.12",
                                           color=DEEP["blue"], lw=2.5)
    ax.add_patch(arrow_bottom)
    ax.text(6.0, 2.15, "Expensive Manufactured Goods\n& High-Interest Loans",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.0))

    # Third Arrow: Out of African Nation
    # "Debt Repayment & Profits leaving the country"
    arrow_out = patches.FancyArrowPatch((2.3, 2.5), (2.3, 0.8),
                                        arrowstyle="->,head_length=8,head_width=5",
                                        color=DEEP["pink"], lw=2.5)
    ax.add_patch(arrow_out)
    ax.text(2.3, 0.45, "Debt Repayment & Profits\nleaving the country",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.0))

    save(fig, out)
