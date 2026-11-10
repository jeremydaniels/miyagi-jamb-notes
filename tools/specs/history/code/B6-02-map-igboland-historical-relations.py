from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Surrounding region patches
    # Igala (North)
    igala_box = patches.FancyBboxPatch((3.5, 7.8), 5.0, 1.4, boxstyle="round,pad=0.2",
                                       fc=CREAM, ec=DEEP["orange"], lw=2, alpha=0.9)
    ax.add_patch(igala_box)
    ax.text(6.0, 8.5, "IGALA", fontsize=18, fontweight='bold', color=INK, ha='center', va='center')

    # Benin Empire (West)
    benin_box = patches.FancyBboxPatch((0.4, 4.0), 2.5, 2.5, boxstyle="round,pad=0.2",
                                       fc=LAV, ec=DEEP["lav"], lw=2, alpha=0.9)
    ax.add_patch(benin_box)
    ax.text(1.65, 5.25, "BENIN EMPIRE", fontsize=16, fontweight='bold', color=INK, ha='center', va='center')

    # Efik / Ibibio (East)
    efik_box = patches.FancyBboxPatch((9.1, 4.0), 2.5, 2.5, boxstyle="round,pad=0.2",
                                      fc=PINK, ec=DEEP["pink"], lw=2, alpha=0.9)
    ax.add_patch(efik_box)
    ax.text(10.35, 5.25, "EFIK/IBIBIO", fontsize=16, fontweight='bold', color=INK, ha='center', va='center')

    # Ijo / Niger Delta (South)
    ijo_box = patches.FancyBboxPatch((3.5, 0.6), 5.0, 1.3, boxstyle="round,pad=0.2",
                                     fc=BLUE, ec=DEEP["blue"], lw=2, alpha=0.9)
    ax.add_patch(ijo_box)
    ax.text(6.0, 1.25, "IJO (Niger Delta)", fontsize=17, fontweight='bold', color=INK, ha='center', va='center')

    # Central Region: IGBOLAND
    igbo_poly = patches.Polygon([[3.6, 3.6], [4.0, 6.7], [8.0, 6.7], [8.4, 3.6], [6.0, 3.4]],
                                closed=True, fc=GREEN, ec=DEEP["green"], lw=3, zorder=2)
    ax.add_patch(igbo_poly)
    ax.text(5.6, 5.3, "IGBOLAND", fontsize=20, fontweight='bold', color=INK, ha='center', va='center', zorder=4)

    # Arochukwu location
    aro_x, aro_y = 7.7, 4.2
    ax.plot(aro_x, aro_y, marker='*', markersize=19, color=DEEP["orange"], markeredgecolor=INK, markeredgewidth=1.2, zorder=6)
    ax.annotate("Arochukwu", xy=(aro_x, aro_y), xytext=(aro_x, aro_y + 0.45),
                fontsize=14, fontweight='bold', color=INK, ha='center', va='bottom', zorder=7,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1))

    # Radiating trade routes from Arochukwu (dashed lines)
    routes = [
        [(aro_x, aro_y), (5.5, 6.3)],
        [(aro_x, aro_y), (4.5, 4.6)],
        [(aro_x, aro_y), (5.5, 3.8)],
        [(aro_x, aro_y), (9.1, 4.6)],
        [(aro_x, aro_y), (6.8, 1.9)]
    ]
    for r in routes:
        xs, ys = zip(*r)
        ax.plot(xs, ys, color=DEEP["orange"], lw=2.0, ls='--', alpha=0.85, zorder=3)

    # Directional Interaction Arrows & Labels

    # 1. North to IGALA: arrow pointing North from Igboland to Igala
    ax.annotate("", xy=(6.0, 7.8), xytext=(6.0, 6.7),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=22), zorder=5)
    ax.text(6.0, 7.25, "Trade & Atama titles", fontsize=14, fontweight='bold', color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    # 2. West to BENIN EMPIRE: arrow pointing West from Igboland to Benin Empire
    ax.annotate("", xy=(2.9, 5.2), xytext=(3.6, 5.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=22), zorder=5)
    ax.text(3.25, 5.8, "Obi Kingship &\nCoral Beads", fontsize=14, fontweight='bold', color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    # 3. South to IJO (Niger Delta): clearly visible arrow pointing South from Igboland to Ijo
    ax.annotate("", xy=(5.2, 1.9), xytext=(5.2, 3.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=22), zorder=5)
    ax.text(5.2, 2.65, "Palm Oil Trade", fontsize=14, fontweight='bold', color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    # 4. East to EFIK/IBIBIO: arrow pointing East from Igboland to Efik/Ibibio
    ax.annotate("", xy=(9.1, 5.6), xytext=(8.4, 5.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=22), zorder=5)
    ax.text(8.75, 6.25, "Ekpe Society\n& Trade", fontsize=14, fontweight='bold', color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2), zorder=6)

    # Title & Caption
    ax.text(6.0, 9.55, "19th-Century South-Eastern Nigeria & Regional Interactions",
            fontsize=18, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(6.0, 0.25, "Sketch map: zones are approximate",
            fontsize=14, color=GREY, ha='center', va='center', style='italic')

    save(fig, out)
