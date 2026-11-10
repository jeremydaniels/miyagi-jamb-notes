from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Overall Title
    ax.text(6.0, 7.05, "Treasury Single Account (TSA) vs. Old Banking System",
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # Dividing line
    ax.plot([6.0, 6.0], [0.8, 6.6], color=GREY, lw=1.5, linestyle='--')

    # Subtitles
    ax.text(3.0, 6.4, "Old System: Scattered Funds", ha='center', va='center',
            fontsize=16, weight='bold', color=DEEP['pink'])
    ax.text(9.0, 6.4, "TSA System: Consolidated Funds", ha='center', va='center',
            fontsize=16, weight='bold', color=DEEP['green'])

    ministries = ["Ministry of\nEducation", "Ministry of\nHealth", "Ministry of\nWorks"]
    y_min = [5.2, 3.6, 2.0]

    # --- LEFT SIDE: OLD SYSTEM ---
    # Draw Ministries (Left)
    for i, (m_text, y) in enumerate(zip(ministries, y_min)):
        box = patches.FancyBboxPatch((0.6, y - 0.5), 2.0, 1.0,
                                     boxstyle="round,pad=0.1",
                                     fc=CREAM, ec=INK, lw=1.5)
        ax.add_patch(box)
        ax.text(1.6, y, m_text, ha='center', va='center', fontsize=14, color=INK)

    # Commercial Banks (Scattered)
    banks = ["Commercial\nBank A", "Commercial\nBank B", "Commercial\nBank C"]
    y_banks = [5.2, 3.6, 2.0]
    for i, (b_text, y) in enumerate(zip(banks, y_banks)):
        box = patches.FancyBboxPatch((3.8, y - 0.5), 1.8, 1.0,
                                     boxstyle="round,pad=0.1",
                                     fc=PINK, ec=DEEP['pink'], lw=2.0)
        ax.add_patch(box)
        ax.text(4.7, y, b_text, ha='center', va='center', fontsize=14, weight='bold', color=INK)

        # Arrows connecting Ministry to specific Commercial Bank
        ax.annotate("", xy=(3.8, y), xytext=(2.6, y),
                    arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=2.5,
                                    mutation_scale=18))

    # Caption Left
    ax.text(3.0, 0.9, "Multiple autonomous accounts in\ndifferent commercial banks (revenue leakages)",
            ha='center', va='center', fontsize=14, color=INK, style='italic',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # --- RIGHT SIDE: TSA SYSTEM ---
    # Draw Ministries (Right)
    for i, (m_text, y) in enumerate(zip(ministries, y_min)):
        box = patches.FancyBboxPatch((6.6, y - 0.5), 2.0, 1.0,
                                     boxstyle="round,pad=0.1",
                                     fc=CREAM, ec=INK, lw=1.5)
        ax.add_patch(box)
        ax.text(7.6, y, m_text, ha='center', va='center', fontsize=14, color=INK)

    # Unified Central Bank (CBN) Vault
    cbn_box = patches.FancyBboxPatch((9.7, 1.8), 1.9, 3.6,
                                     boxstyle="round,pad=0.2",
                                     fc=GREEN, ec=DEEP['green'], lw=2.5)
    ax.add_patch(cbn_box)
    ax.text(10.65, 3.6, "Central Bank\nof Nigeria\n(CBN)\n\nTreasury Single\nAccount (TSA)",
            ha='center', va='center', fontsize=14, weight='bold', color=INK)

    # Arrows from each Ministry to Central Vault
    for y in y_min:
        ax.annotate("", xy=(9.7, 3.6), xytext=(8.6, y),
                    arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=2.5,
                                    mutation_scale=18))

    # Caption Right
    ax.text(9.0, 0.9, "All government revenue unified\nin a single CBN-managed account (transparency)",
            ha='center', va='center', fontsize=14, color=INK, style='italic',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    save(fig, out)
