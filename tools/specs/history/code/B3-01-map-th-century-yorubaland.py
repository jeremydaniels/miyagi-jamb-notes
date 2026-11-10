from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Background ecological zones (Savanna in the north, Forest in the south)
    # Map area from y=1.0 to y=7.8
    savanna = plt.Rectangle((0.5, 4.4), 9, 3.4, color=CREAM, alpha=0.5, zorder=0)
    forest = plt.Rectangle((0.5, 1.0), 9, 3.4, color=GREEN, alpha=0.25, zorder=0)
    ax.add_patch(savanna)
    ax.add_patch(forest)

    # Dividing zone line
    ax.plot([0.5, 9.5], [4.4, 4.4], color=GREY, linestyle='--', lw=1.5, zorder=1)
    ax.text(0.8, 7.3, "SAVANNA REGION", fontsize=14, color=GREY, fontweight='bold', zorder=2)
    ax.text(0.8, 1.35, "FOREST REGION", fontsize=14, color=DEEP['green'], fontweight='bold', zorder=2)

    # Title
    ax.text(5.0, 8.1, "Yorubaland in the Early 19th Century", fontsize=17, fontweight='bold', ha='center', va='center', color=INK)

    # Old Oyo (Oyo-Ile) - ruined site in savanna
    old_oyo_pos = (4.0, 6.4)
    ax.scatter(*old_oyo_pos, marker='x', s=160, color=DEEP['orange'], lw=3, zorder=4)
    ax.text(old_oyo_pos[0], old_oyo_pos[1] + 0.38, "Old Oyo (Oyo-Ile)\n(Abandoned c. 1835)", 
            fontsize=14, ha='center', va='bottom', color=INK, fontweight='bold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'), zorder=5)

    # Ilorin Emirate (Northeast)
    ilorin_pos = (7.8, 6.0)
    ax.scatter(ilorin_pos[0], ilorin_pos[1], marker='o', s=120, color=DEEP['lav'], zorder=4)
    # Crescent symbol near Ilorin to denote the Emirate
    ax.text(ilorin_pos[0] + 0.35, ilorin_pos[1], "☪", fontsize=18, ha='center', va='center', color=DEEP['lav'], zorder=5)
    ax.text(ilorin_pos[0], ilorin_pos[1] + 0.42, "Ilorin\n(Emirate)", 
            fontsize=14, ha='center', va='bottom', color=INK, fontweight='bold',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'), zorder=5)

    # Pressure arrow from Ilorin pushing southwest
    ax.annotate("", xy=(5.4, 5.5), xytext=(7.3, 5.9),
                arrowprops=dict(arrowstyle="->", color=DEEP['lav'], lw=2.5, mutation_scale=18))

    # Migration routes (Arrows pointing downwards to the south)
    routes = [
        ((3.8, 5.9), (3.6, 4.6)),
        ((4.2, 5.9), (5.0, 4.6)),
        ((4.0, 5.7), (4.3, 3.8))
    ]
    for start, end in routes:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=3, mutation_scale=20))
    ax.text(2.5, 5.1, "Southward\nMigration Routes", fontsize=14, ha='center', va='center',
            color=DEEP['orange'], fontweight='bold',
            bbox=dict(fc='white', ec='none', boxstyle='round,pad=0.2'), zorder=5)

    # New Settlements in the Forest Region
    settlements = {
        "New Oyo": (3.6, 3.5),
        "Ijaye": (4.6, 2.9),
        "Ibadan": (6.2, 2.3),
        "Abeokuta": (3.2, 2.0)
    }

    # Connecting/path arrows continuing from boundary towards settlements
    ax.annotate("", xy=(3.6, 3.8), xytext=(3.6, 4.5),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2, linestyle=':'))
    ax.annotate("", xy=(4.6, 3.2), xytext=(4.3, 4.4),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2, linestyle=':'))
    ax.annotate("", xy=(6.0, 2.6), xytext=(5.1, 4.4),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2, linestyle=':'))
    ax.annotate("", xy=(3.3, 2.3), xytext=(3.5, 3.2),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2, linestyle=':'))

    # Plot circled settlements
    for name, pos in settlements.items():
        circ = plt.Circle(pos, 0.22, edgecolor=DEEP['blue'], facecolor=BLUE, lw=2.5, zorder=4)
        ax.add_patch(circ)
        ax.scatter(*pos, s=25, color=INK, zorder=5)

        if name == "Ibadan":
            offset_x, offset_y = 0.72, 0.0
            ha_align = 'left'
            va_align = 'center'
        elif name == "Abeokuta":
            offset_x, offset_y = 0.0, -0.45
            ha_align = 'center'
            va_align = 'top'
        elif name == "Ijaye":
            offset_x, offset_y = 0.65, 0.0
            ha_align = 'left'
            va_align = 'center'
        else:  # New Oyo
            offset_x, offset_y = -0.7, 0.0
            ha_align = 'right'
            va_align = 'center'

        ax.text(pos[0] + offset_x, pos[1] + offset_y, name, fontsize=15, 
                ha=ha_align, va=va_align, fontweight='bold', color=INK,
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', lw=1), zorder=6)

    # Neat outer frame around the map
    border = plt.Rectangle((0.5, 1.0), 9, 6.8, fill=False, edgecolor=GREY, lw=1.5, zorder=3)
    ax.add_patch(border)

    # Schematic note placed safely below the border line with ample clearance
    ax.text(5.0, 0.45, "Sketch map: zones are approximate", 
            fontsize=14, ha='center', va='center', style='italic', color=GREY)

    save(fig, out)
