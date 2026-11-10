from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(5, 6.4, "Financing of a Company: Balance Sheet Equation", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Main Dimensions
    left_x = 1.2
    right_x = 5.2
    w = 3.6
    base_y = 1.0
    total_h = 4.6

    # Column Titles
    ax.text(left_x + w/2, base_y + total_h + 0.35, "Total Assets",
            ha="center", va="bottom", fontsize=16, weight="bold", color=INK)
    ax.text(right_x + w/2, base_y + total_h + 0.35, "Total Equity & Liabilities",
            ha="center", va="bottom", fontsize=16, weight="bold", color=INK)

    # Left Column: Assets
    # Total Assets = Non-Current Assets (top) + Current Assets (bottom)
    # Heights
    h_ca = 1.8
    h_nca = total_h - h_ca  # 2.8

    # Left: Current Assets (bottom)
    rect_ca = patches.Rectangle((left_x, base_y), w, h_ca, 
                                facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=2)
    ax.add_patch(rect_ca)
    ax.text(left_x + w/2, base_y + h_ca/2, "Current Assets",
            ha="center", va="center", fontsize=15, weight="bold", color=INK, zorder=3)

    # Left: Non-Current Assets (top)
    rect_nca = patches.Rectangle((left_x, base_y + h_ca), w, h_nca,
                                 facecolor=LAV, edgecolor=DEEP["lav"], lw=2, zorder=2)
    ax.add_patch(rect_nca)
    ax.text(left_x + w/2, base_y + h_ca + h_nca/2, "Non-Current Assets",
            ha="center", va="center", fontsize=15, weight="bold", color=INK, zorder=3)

    # Right Column: Equity & Liabilities
    # Bottom: Current Liabilities (1.8)
    # Middle: Non-Current Liabilities (1.4)
    # Top: Equity (1.4)
    h_cl = 1.8
    h_ncl = 1.4
    h_eq = total_h - h_cl - h_ncl  # 1.4

    # Right: Current Liabilities (bottom)
    rect_cl = patches.Rectangle((right_x, base_y), w, h_cl,
                                facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2, zorder=2)
    ax.add_patch(rect_cl)
    ax.text(right_x + w/2, base_y + h_cl/2, "Current Liabilities",
            ha="center", va="center", fontsize=15, weight="bold", color=INK, zorder=3)

    # Right: Non-Current Liabilities (middle)
    rect_ncl = patches.Rectangle((right_x, base_y + h_cl), w, h_ncl,
                                 facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=2)
    ax.add_patch(rect_ncl)
    ax.text(right_x + w/2, base_y + h_cl + h_ncl/2, 
            "Non-Current Liabilities\n(Debentures)",
            ha="center", va="center", fontsize=14, weight="bold", color=INK, zorder=3)

    # Right: Equity (top)
    rect_eq = patches.Rectangle((right_x, base_y + h_cl + h_ncl), w, h_eq,
                                facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=2)
    ax.add_patch(rect_eq)
    ax.text(right_x + w/2, base_y + h_cl + h_ncl + h_eq/2, 
            "Equity\n(Share Capital + Reserves)",
            ha="center", va="center", fontsize=14, weight="bold", color=INK, zorder=3)

    # Center Equality / Relation Symbol & Double Arrow
    mid_x = (left_x + w + right_x) / 2
    ax.annotate("", xy=(right_x - 0.05, base_y + total_h/2), 
                xytext=(left_x + w + 0.05, base_y + total_h/2),
                arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=2.5, mutation_scale=18))

    ax.text(mid_x, base_y + total_h/2 + 0.4, "MUST\nEQUAL",
            ha="center", va="center", fontsize=14, weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Overall Total Value bracket/annotation at the bottom
    ax.annotate("", xy=(left_x, base_y - 0.25), xytext=(left_x + w, base_y - 0.25),
                arrowprops=dict(arrowstyle="|-|", color=GREY, lw=1.5))
    ax.text(left_x + w/2, base_y - 0.55, "Total Uses of Funds", 
            ha="center", va="center", fontsize=14, color=INK)

    ax.annotate("", xy=(right_x, base_y - 0.25), xytext=(right_x + w, base_y - 0.25),
                arrowprops=dict(arrowstyle="|-|", color=GREY, lw=1.5))
    ax.text(right_x + w/2, base_y - 0.55, "Total Sources of Funds", 
            ha="center", va="center", fontsize=14, color=INK)

    save(fig, out)
