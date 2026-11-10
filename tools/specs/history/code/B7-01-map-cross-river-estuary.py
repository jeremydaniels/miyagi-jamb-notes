from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # Water background (Bight of Biafra / Gulf of Guinea)
    water = patches.Rectangle((0, 0), 12, 9, facecolor='#E3F2FD', edgecolor='none', zorder=0)
    ax.add_patch(water)

    # Simplified landmass polygon for SE Nigeria / Cross River region
    land_verts = [
        (0, 9), (12, 9), (12, 4.0),
        # Cameroon border / Rio del Rey coast
        (10.5, 3.8), (9.8, 3.2), (9.2, 2.5),
        # East side of Cross River estuary
        (8.8, 2.8), (8.4, 3.8), (8.1, 4.5), (7.8, 5.2),
        # Head of estuary near Calabar
        (7.5, 5.4), (7.2, 5.2), (7.1, 4.2),
        # West side of estuary (Bakassi / Calabar mouth)
        (7.0, 3.0), (6.5, 2.2),
        # Coast heading west
        (5.5, 2.2), (4.5, 2.0), (3.0, 1.8), (1.5, 1.5), (0, 1.2)
    ]
    land = patches.Polygon(land_verts, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
    ax.add_patch(land)

    # Rivers: Cross River main stem and branches
    cross_river_x = [9.8, 8.8, 8.2, 7.8, 7.4, 7.5, 7.8, 8.0, 7.6, 7.2]
    cross_river_y = [8.5, 7.8, 7.0, 6.2, 5.6, 4.8, 4.0, 3.2, 2.5, 1.5]
    ax.plot(cross_river_x, cross_river_y, color='#90CAF9', lw=6, solid_capstyle='round', zorder=2)
    ax.plot(cross_river_x, cross_river_y, color=DEEP['blue'], lw=1.5, zorder=3)

    # River labels
    ax.text(8.8, 7.6, "Cross River", fontsize=14, fontstyle='italic', color=DEEP['blue'],
            ha='left', va='center', bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.85), zorder=5)

    # Label Bight of Biafra
    ax.text(3.0, 0.9, "Bight of Biafra\n(Gulf of Guinea)", fontsize=15, fontstyle='italic',
            ha='center', va='center', color=DEEP['blue'], zorder=4)

    # Estuary label
    ax.text(9.0, 2.0, "Cross River\nEstuary", fontsize=14, fontstyle='italic',
            ha='center', va='center', color=DEEP['blue'],
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.85), zorder=5)

    # Territory soft background patches
    igbo_patch = patches.FancyBboxPatch((0.8, 6.6), 2.8, 1.5, boxstyle="round,pad=0.3",
                                        fc=LAV, ec=DEEP['lav'], ls='--', lw=1.5, alpha=0.5, zorder=2)
    annang_patch = patches.FancyBboxPatch((1.6, 4.7), 2.3, 1.2, boxstyle="round,pad=0.3",
                                          fc=LAV, ec=DEEP['lav'], ls='--', lw=1.5, alpha=0.5, zorder=2)
    ibibio_patch = patches.FancyBboxPatch((3.4, 3.0), 2.3, 1.2, boxstyle="round,pad=0.3",
                                          fc=LAV, ec=DEEP['lav'], ls='--', lw=1.5, alpha=0.5, zorder=2)
    ekoi_patch = patches.FancyBboxPatch((9.2, 6.0), 2.3, 1.6, boxstyle="round,pad=0.3",
                                        fc=LAV, ec=DEEP['lav'], ls='--', lw=1.5, alpha=0.5, zorder=2)
    for p in [igbo_patch, annang_patch, ibibio_patch, ekoi_patch]:
        ax.add_patch(p)

    # Territories inland text
    ax.text(2.2, 7.5, "IGBO", fontsize=17, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.9), zorder=6)
    ax.text(2.2, 7.0, "Hinterland territory", fontsize=14, fontstyle='italic', color=GREY, ha='center',
            bbox=dict(fc='white', ec='none', pad=1, alpha=0.9), zorder=6)
    ax.text(2.7, 5.3, "ANNANG", fontsize=16, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.9), zorder=6)
    ax.text(4.5, 3.6, "IBIBIO", fontsize=16, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.9), zorder=6)
    ax.text(10.35, 6.8, "EKOI\n(EJAGHAM)", fontsize=16, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.9), zorder=6)

    # Old Calabar Towns cluster
    towns = [
        ("Creek Town", 6.7, 5.9, -0.15, 'right'),
        ("Obutong", 7.4, 5.9, 0.15, 'left'),
        ("Duke Town", 7.4, 5.3, 0.15, 'left'),
        ("Henshaw Town", 6.8, 4.9, -0.15, 'right')
    ]

    calabar_box = patches.FancyBboxPatch((6.4, 4.6), 1.8, 1.6, boxstyle="round,pad=0.25",
                                         fc=PINK, ec=DEEP['pink'], lw=2, alpha=0.4, zorder=3)
    ax.add_patch(calabar_box)

    for name, tx, ty, off_x, ha_align in towns:
        ax.plot(tx, ty, marker='o', markersize=7, color=DEEP['pink'], zorder=6)
        ax.text(tx + off_x, ty, name, fontsize=14, fontweight='semibold', color=INK,
                ha=ha_align, va='center', zorder=7,
                bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.85))

    ax.annotate("OLD CALABAR",
                xy=(7.3, 4.5), xytext=(7.3, 3.5),
                fontsize=16, fontweight='bold', color=DEEP['pink'], ha='center', va='center',
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=2, mutation_scale=20),
                bbox=dict(fc='white', ec=DEEP['pink'], boxstyle="round,pad=0.4", lw=1.5),
                zorder=7)

    # Trade Route Arrows
    # Hinterland to Old Calabar
    ax.annotate("", xy=(6.3, 5.4), xytext=(3.7, 6.7),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['orange'], lw=3, mutation_scale=25),
                zorder=4)
    ax.text(4.8, 6.4, "Palm oil and slaves", fontsize=14, fontweight='bold', color=DEEP['orange'],
            ha='center', va='center', rotation=-22,
            bbox=dict(fc='white', ec=DEEP['orange'], boxstyle="round,pad=0.3", lw=1.2), zorder=6)

    # Coast to Inland (with clear robust arrowhead)
    ax.annotate("", xy=(3.0, 4.7), xytext=(1.5, 1.8),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['green'], lw=3, mutation_scale=25),
                zorder=4)
    ax.text(2.0, 2.9, "European manufactured goods",
            fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', rotation=62,
            bbox=dict(fc='white', ec=DEEP['green'], boxstyle="round,pad=0.3", lw=1.2), zorder=6)

    # Title and Subtitle
    ax.text(6.0, 8.55, "19th-Century Cross River Estuary & Trade Networks",
            fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(6.0, 8.18, "Old Calabar and Hinterland Peoples (SE Nigeria)",
            fontsize=15, fontstyle='italic', ha='center', va='center', color=INK)

    # Caption required for schematic maps
    ax.text(0.3, 0.4, "Sketch map: zones are approximate",
            fontsize=14, color=GREY, ha='left', va='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.8), zorder=5)

    # Outer neatline border
    border = patches.Rectangle((0.05, 0.05), 11.9, 8.9, fill=False, edgecolor=INK, lw=1.5, zorder=10)
    ax.add_patch(border)

    save(fig, out)
