from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)

    # Bars setup
    x_pos = [1.2, 3.2]
    width = 0.9

    # Exports: Crude Oil ~85%, Non-oil ~15%
    # Imports: Machinery ~32%, Manufactured Goods ~28%, Refined Petroleum ~22%, Food ~18%
    
    # Left Bar: Exports
    # Crude oil
    ax.bar(x_pos[0], 85, width=width, color=DEEP["blue"], edgecolor=INK, lw=1.5)
    # Non-oil
    ax.bar(x_pos[0], 15, bottom=85, width=width, color=GREEN, edgecolor=INK, lw=1.5)

    # Right Bar: Imports
    imp_vals = [32, 28, 22, 18]
    imp_colors = [ORANGE, PINK, LAV, CREAM]
    bottom = 0
    for val, col in zip(imp_vals, imp_colors):
        ax.bar(x_pos[1], val, bottom=bottom, width=width, color=col, edgecolor=INK, lw=1.5)
        bottom += val

    # Labels inside / beside bars
    # Export annotations
    ax.text(x_pos[0], 42.5, "Crude Oil\n(over 80%)", ha="center", va="center", color="white", fontsize=15, weight="bold")
    ax.text(x_pos[0], 92.5, "Non-oil\n(Cocoa, Sesame)", ha="center", va="center", color=INK, fontsize=14, weight="bold")

    # Import annotations
    ax.text(x_pos[1], 16, "Machinery", ha="center", va="center", color=INK, fontsize=14, weight="bold")
    ax.text(x_pos[1], 46, "Manufactured\nGoods", ha="center", va="center", color=INK, fontsize=14, weight="bold")
    ax.text(x_pos[1], 71, "Refined\nPetroleum", ha="center", va="center", color=INK, fontsize=14, weight="bold")
    ax.text(x_pos[1], 91, "Food", ha="center", va="center", color=INK, fontsize=14, weight="bold")

    # Axes configuration
    ax.set_xlim(0.2, 4.2)
    ax.set_ylim(0, 115)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(["Exports", "Imports"], fontsize=16, weight="bold", color=INK)
    ax.set_yticks(np.arange(0, 101, 20))
    ax.set_yticklabels([f"{y}%" for y in np.arange(0, 101, 20)], fontsize=14, color=INK)
    ax.set_ylabel("Share of Total Trade (%)", fontsize=15, color=INK, labelpad=10)

    # Styling spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)
    ax.tick_params(axis="both", colors=INK, width=1.5, length=6)
    ax.grid(axis="y", linestyle="--", alpha=0.4, color=GREY)

    # Title and Subtitle / Notes
    ax.text(2.2, 110, "Nigeria's Foreign Trade Composition", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    
    # Explanatory note showing high dependence
    note = "High dependence on a single primary product for exports"
    ax.text(2.2, -14, note, ha="center", va="center", fontsize=14, style="italic", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.5", lw=1.2))

    plt.subplots_adjust(bottom=0.18, top=0.92, left=0.12, right=0.95)
    save(fig, out)
