from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Title
    ax.text(5, 8.1, "Electroplating a Spoon with Silver", fontsize=18, fontweight="bold", ha="center", color=INK)

    # Beaker dimensions
    bx0, bx1 = 2.2, 7.8
    by0, by1 = 1.0, 5.5
    liq_y = 4.6

    # Solution fill
    solution_poly = plt.Polygon(
        [[bx0 + 0.08, by0 + 0.08], [bx1 - 0.08, by0 + 0.08], [bx1 - 0.08, liq_y], [bx0 + 0.08, liq_y]],
        facecolor=BLUE, alpha=0.35, edgecolor="none", zorder=1
    )
    ax.add_patch(solution_poly)

    # Beaker outline
    beaker_x = [bx0 - 0.2, bx0, bx0, bx1, bx1, bx1 + 0.2]
    beaker_y = [by1, by1, by0, by0, by1, by1]
    ax.plot(beaker_x, beaker_y, color=INK, lw=3, zorder=2)
    # Liquid surface line
    ax.plot([bx0, bx1], [liq_y, liq_y], color=DEEP["blue"], lw=1.8, linestyle="--", zorder=2)

    # Anode: Silver bar
    anode_x, anode_w = 3.2, 0.7
    anode_y, anode_h = 2.0, 3.4
    silver_bar = patches.Rectangle((anode_x, anode_y), anode_w, anode_h, facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(silver_bar)
    ax.text(anode_x + anode_w/2, anode_y + anode_h/2, "Pure\nSilver\n(Ag)", fontsize=14, ha="center", va="center", color=INK, zorder=4)

    # Cathode: Metal Spoon outline/shape
    # Spoon handle: 6.3, 5.4 down to 6.3, 3.0. Spoon bowl: oval centered at (6.35, 2.3)
    spoon_handle = patches.Rectangle((6.25, 3.2), 0.2, 2.2, facecolor=CREAM, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(spoon_handle)
    spoon_bowl = patches.Ellipse((6.35, 2.4), 0.9, 1.6, facecolor=CREAM, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(spoon_bowl)
    # Plating layer indication (thin edge on spoon)
    ax.text(6.35, 2.4, "Metal\nSpoon", fontsize=14, ha="center", va="center", color=INK, zorder=4)

    # Battery & Circuit at the top
    # Anode wire goes from (anode_x + anode_w/2, 5.4) -> (3.55, 6.8) -> (4.4, 6.8)
    wire_anode = [[anode_x + anode_w/2, 5.4], [anode_x + anode_w/2, 6.8], [4.4, 6.8]]
    ax.plot([p[0] for p in wire_anode], [p[1] for p in wire_anode], color=INK, lw=2.5, zorder=2)

    # Cathode wire goes from (spoon_handle top = 6.35, 5.4) -> (6.35, 6.8) -> (5.6, 6.8)
    wire_cathode = [[6.35, 5.4], [6.35, 6.8], [5.6, 6.8]]
    ax.plot([p[0] for p in wire_cathode], [p[1] for p in wire_cathode], color=INK, lw=2.5, zorder=2)

    # Battery symbol: long bar (+), short thick bar (-)
    # Long bar at 4.6 (anode side = +)
    ax.plot([4.6, 4.6], [6.3, 7.3], color=INK, lw=3, zorder=5)
    # Short thick bar at 4.9
    ax.plot([4.9, 4.9], [6.5, 7.1], color=INK, lw=6, zorder=5)
    # Long bar at 5.1
    ax.plot([5.1, 5.1], [6.3, 7.3], color=INK, lw=3, zorder=5)
    # Short thick bar at 5.4
    ax.plot([5.4, 5.4], [6.5, 7.1], color=INK, lw=6, zorder=5)
    # Connection between wire and battery
    ax.plot([4.4, 4.6], [6.8, 6.8], color=INK, lw=2.5, zorder=5)
    ax.plot([5.4, 5.6], [6.8, 6.8], color=INK, lw=2.5, zorder=5)

    # Battery labels
    ax.text(4.4, 7.45, "+", fontsize=18, fontweight="bold", ha="center", color=DEEP["pink"])
    ax.text(5.6, 7.45, "–", fontsize=18, fontweight="bold", ha="center", color=DEEP["blue"])
    ax.text(5.0, 7.6, "DC Power Supply", fontsize=14, ha="center", color=INK)

    # Electron flow indicators
    ax.annotate("", xy=(3.8, 6.8), xytext=(3.55, 6.8),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5))
    ax.text(3.7, 7.1, "e⁻", fontsize=15, color=DEEP["pink"], fontweight="bold", ha="center")

    ax.annotate("", xy=(6.35, 6.2), xytext=(6.35, 6.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5))
    ax.text(6.65, 6.35, "e⁻", fontsize=15, color=DEEP["blue"], fontweight="bold", ha="center")

    # Ion migration arrows (Ag+ moving to spoon)
    ions_y = [2.5, 3.3, 4.0]
    for y_pos in ions_y:
        ax.annotate("", xy=(5.8, y_pos), xytext=(4.1, y_pos),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, linestyle="-"))
        ax.text(4.9, y_pos + 0.12, "Ag⁺", fontsize=14, fontweight="bold", color=DEEP["orange"],
                ha="center", bbox=dict(fc="white", ec="none", pad=1.5))

    # Anode / Cathode explanatory labels
    ax.annotate("Anode (+)\n(Oxidation: Ag → Ag⁺ + e⁻)", xy=(anode_x, 3.8), xytext=(0.4, 4.2),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Cathode (–)\n(Reduction: Ag⁺ + e⁻ → Ag)\nSilver coats the spoon", xy=(6.8, 2.5), xytext=(7.4, 2.5),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Electrolyte solution label
    ax.annotate("Electrolyte solution\n(Silver nitrate, AgNO₃)", xy=(4.5, 1.4), xytext=(4.5, 0.4),
                fontsize=14, color=INK, ha="center", arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    save(fig, out)
