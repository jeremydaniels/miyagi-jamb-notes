from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(6, 10.4, "The Accounting Equation & Statement of Financial Position",
            fontsize=17, fontweight='bold', color=INK, ha='center', va='center')

    # --- BALANCED SCALE ---
    # Central base & pillar
    base = patches.Polygon([[5.2, 7.3], [6.8, 7.3], [6.5, 7.6], [5.5, 7.6]],
                           closed=True, facecolor=GREY, edgecolor=INK, lw=1.8)
    ax.add_patch(base)
    ax.plot([6, 6], [7.6, 9.4], color=INK, lw=3)
    ax.scatter([6], [9.4], s=100, color=INK, zorder=5)

    # Balance beam (horizontal = balanced)
    ax.plot([3.0, 9.0], [9.4, 9.4], color=INK, lw=3.5)

    # Left plate strings and pan (Assets)
    ax.plot([3.0, 2.0], [9.4, 8.2], color=INK, lw=1.5)
    ax.plot([3.0, 4.0], [9.4, 8.2], color=INK, lw=1.5)
    pan_left = patches.Arc((3.0, 8.2), 2.0, 0.6, angle=0, theta1=180, theta2=360, color=INK, lw=2.5)
    ax.add_patch(pan_left)
    ax.plot([2.0, 4.0], [8.2, 8.2], color=INK, lw=2)

    # Left weight box: Assets
    box_assets = patches.FancyBboxPatch((2.0, 8.25), 2.0, 0.75,
                                        boxstyle="round,pad=0.08",
                                        facecolor=BLUE, edgecolor=DEEP['blue'], lw=2)
    ax.add_patch(box_assets)
    ax.text(3.0, 8.62, "Assets", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')

    # Equals symbol between plates
    ax.text(6, 8.6, "=", fontsize=26, fontweight='bold', color=DEEP['orange'], ha='center', va='center')

    # Right plate strings and pan (Capital + Liabilities)
    ax.plot([9.0, 7.7], [9.4, 8.2], color=INK, lw=1.5)
    ax.plot([9.0, 10.3], [9.4, 8.2], color=INK, lw=1.5)
    pan_right = patches.Arc((9.0, 8.2), 2.6, 0.6, angle=0, theta1=180, theta2=360, color=INK, lw=2.5)
    ax.add_patch(pan_right)
    ax.plot([7.7, 10.3], [8.2, 8.2], color=INK, lw=2)

    # Right weight box: Capital + Liabilities
    box_cap_liab = patches.FancyBboxPatch((7.6, 8.25), 2.8, 0.75,
                                          boxstyle="round,pad=0.08",
                                          facecolor=PINK, edgecolor=DEEP['pink'], lw=2)
    ax.add_patch(box_cap_liab)
    ax.text(9.0, 8.62, "Capital + Liabilities", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')

    # --- DOWNWARD FLOW ARROWS ---
    ax.annotate('', xy=(3.0, 6.7), xytext=(3.0, 7.5),
                arrowprops=dict(arrowstyle="-|>", lw=2, color=INK, mutation_scale=16))
    ax.annotate('', xy=(9.0, 6.7), xytext=(9.0, 7.5),
                arrowprops=dict(arrowstyle="-|>", lw=2, color=INK, mutation_scale=16))

    # Central statement title banner
    stmt_box = patches.FancyBboxPatch((3.5, 6.5), 5.0, 0.65,
                                      boxstyle="round,pad=0.1",
                                      facecolor=CREAM, edgecolor=DEEP['orange'], lw=2)
    ax.add_patch(stmt_box)
    ax.text(6.0, 6.82, "Statement of Financial Position",
            fontsize=15, fontweight='bold', color=INK, ha='center', va='center')

    # Flow lines from central statement down to columns
    ax.annotate('', xy=(3.0, 5.7), xytext=(4.5, 6.4),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color=INK, mutation_scale=14))
    ax.annotate('', xy=(9.0, 5.7), xytext=(7.5, 6.4),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color=INK, mutation_scale=14))

    # --- LEFT COLUMN: ASSETS CATEGORIES ---
    # Column Header: Total Assets
    header_assets = patches.FancyBboxPatch((1.0, 5.0), 4.0, 0.65,
                                           boxstyle="round,pad=0.08",
                                           facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.8)
    ax.add_patch(header_assets)
    ax.text(3.0, 5.32, "Assets", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')

    # Sub-category 1: Non-Current Assets
    box_nc_assets = patches.FancyBboxPatch((1.2, 3.4), 3.6, 1.1,
                                           boxstyle="round,pad=0.08",
                                           facecolor=LAV, edgecolor=DEEP['lav'], lw=1.5)
    ax.add_patch(box_nc_assets)
    ax.text(3.0, 4.15, "Non-Current Assets", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(3.0, 3.7, "(e.g., Property, Plant,\nEquipment)", fontsize=14, color=INK, ha='center', va='center')

    # Sub-category 2: Current Assets
    box_c_assets = patches.FancyBboxPatch((1.2, 1.5), 3.6, 1.1,
                                          boxstyle="round,pad=0.08",
                                          facecolor=LAV, edgecolor=DEEP['lav'], lw=1.5)
    ax.add_patch(box_c_assets)
    ax.text(3.0, 2.25, "Current Assets", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(3.0, 1.8, "(e.g., Inventory, Trade\nReceivables, Cash)", fontsize=14, color=INK, ha='center', va='center')

    # Arrows for Left Column
    ax.plot([3.0, 3.0], [5.0, 4.5], color=INK, lw=1.5)
    ax.plot([3.0, 3.0], [3.4, 2.6], color=INK, lw=1.5)

    # --- RIGHT COLUMN: CAPITAL & LIABILITIES CATEGORIES ---
    # Column Header: Total Capital + Liabilities
    header_right = patches.FancyBboxPatch((7.0, 5.0), 4.0, 0.65,
                                          boxstyle="round,pad=0.08",
                                          facecolor=PINK, edgecolor=DEEP['pink'], lw=1.8)
    ax.add_patch(header_right)
    ax.text(9.0, 5.32, "Capital + Liabilities", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')

    # Sub-category 1: Capital (Equity)
    box_capital = patches.FancyBboxPatch((7.2, 3.6), 3.6, 1.05,
                                         boxstyle="round,pad=0.08",
                                         facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5)
    ax.add_patch(box_capital)
    ax.text(9.0, 4.3, "Capital", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(9.0, 3.85, "(Owner's Equity /\nReserves)", fontsize=14, color=INK, ha='center', va='center')

    # Sub-category 2: Long-term Liabilities
    box_lt_liab = patches.FancyBboxPatch((7.2, 2.2), 3.6, 1.05,
                                         boxstyle="round,pad=0.08",
                                         facecolor=ORANGE, edgecolor=DEEP['orange'], lw=1.5)
    ax.add_patch(box_lt_liab)
    ax.text(9.0, 2.9, "Long-term Liabilities", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(9.0, 2.45, "(e.g., Bank Loans,\nMortgages)", fontsize=14, color=INK, ha='center', va='center')

    # Sub-category 3: Current Liabilities
    box_c_liab = patches.FancyBboxPatch((7.2, 0.8), 3.6, 1.05,
                                        boxstyle="round,pad=0.08",
                                        facecolor=ORANGE, edgecolor=DEEP['orange'], lw=1.5)
    ax.add_patch(box_c_liab)
    ax.text(9.0, 1.5, "Current Liabilities", fontsize=14, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(9.0, 1.05, "(e.g., Trade Payables,\nOverdraft)", fontsize=14, color=INK, ha='center', va='center')

    # Arrows for Right Column
    ax.plot([9.0, 9.0], [5.0, 4.65], color=INK, lw=1.5)
    ax.plot([9.0, 9.0], [3.6, 3.25], color=INK, lw=1.5)
    ax.plot([9.0, 9.0], [2.2, 1.85], color=INK, lw=1.5)

    save(fig, out)
