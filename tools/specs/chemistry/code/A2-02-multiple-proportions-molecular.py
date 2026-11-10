from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(11, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(5.5, 6.3, "Law of Multiple Proportions", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)

    # Style definitions
    C_COLOR = "#2B2D42"      # Black/Charcoal for Carbon
    O_COLOR = DEEP["pink"]    # Red/Deep Pink for Oxygen
    BOND_COLOR = GREY
    
    # Radius of atoms
    r_c = 0.45
    r_o = 0.40

    # Layout coordinates (shifted right to avoid any overlap with labels on left)
    # --- TOP ROW: CO ---
    y_co = 4.6
    x_label = 0.8
    x_co_c = 2.7
    x_co_o = 3.8

    # Triple bond representation for CO
    for offset in [-0.1, 0.0, 0.1]:
        ax.plot([x_co_c, x_co_o], [y_co + offset, y_co + offset], color=BOND_COLOR, lw=2.5, zorder=1)

    # C atom
    c1 = patches.Circle((x_co_c, y_co), r_c, facecolor=C_COLOR, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(c1)
    ax.text(x_co_c, y_co, "C", fontsize=16, fontweight="bold", color="white", ha="center", va="center", zorder=3)

    # O atom
    o1 = patches.Circle((x_co_o, y_co), r_o, facecolor=O_COLOR, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(o1)
    ax.text(x_co_o, y_co, "O", fontsize=16, fontweight="bold", color="white", ha="center", va="center", zorder=3)

    # Label CO
    ax.text(x_label, y_co, "CO", fontsize=17, fontweight="bold", ha="center", va="center", color=INK)

    # CO Mass text
    ax.text(4.9, y_co, "In CO, 12g C combines with 16g O", fontsize=15, ha="left", va="center", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.45", lw=1.2))

    # --- BOTTOM ROW: CO2 ---
    y_co2 = 2.8
    x_co2_c = 3.1
    x_co2_o1 = 2.0
    x_co2_o2 = 4.2

    # Double bonds for CO2
    for offset in [-0.08, 0.08]:
        ax.plot([x_co2_o1, x_co2_c], [y_co2 + offset, y_co2 + offset], color=BOND_COLOR, lw=2.5, zorder=1)
        ax.plot([x_co2_c, x_co2_o2], [y_co2 + offset, y_co2 + offset], color=BOND_COLOR, lw=2.5, zorder=1)

    # Atoms for CO2
    o2_left = patches.Circle((x_co2_o1, y_co2), r_o, facecolor=O_COLOR, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(o2_left)
    ax.text(x_co2_o1, y_co2, "O", fontsize=16, fontweight="bold", color="white", ha="center", va="center", zorder=3)

    c2 = patches.Circle((x_co2_c, y_co2), r_c, facecolor=C_COLOR, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(c2)
    ax.text(x_co2_c, y_co2, "C", fontsize=16, fontweight="bold", color="white", ha="center", va="center", zorder=3)

    o2_right = patches.Circle((x_co2_o2, y_co2), r_o, facecolor=O_COLOR, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(o2_right)
    ax.text(x_co2_o2, y_co2, "O", fontsize=16, fontweight="bold", color="white", ha="center", va="center", zorder=3)

    # Label CO2 (now well separated: label at 0.8, atom edge at 1.6)
    ax.text(x_label, y_co2, "CO₂", fontsize=17, fontweight="bold", ha="center", va="center", color=INK)

    # CO2 Mass text
    ax.text(4.9, y_co2, "In CO2, 12g C combines with 32g O", fontsize=15, ha="left", va="center", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.45", lw=1.2))

    # --- RATIO SUMMARY BOX ---
    y_ratio = 1.15
    ax.text(5.5, y_ratio, "Ratio of oxygen masses = 16:32 = 1:2", fontsize=16, fontweight="bold",
            ha="center", va="center", color=INK,
            bbox=dict(fc=CREAM, ec=DEEP["blue"], boxstyle="round,pad=0.5", lw=1.5))

    save(fig, out)
