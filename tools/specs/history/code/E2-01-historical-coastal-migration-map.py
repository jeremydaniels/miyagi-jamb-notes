from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)

    # Coordinates approx for West Africa regional view
    # Longitude: -17.5 to 0.5, Latitude: 3.5 to 15.0
    ax.set_xlim(-17.5, 0.5)
    ax.set_ylim(3.5, 15.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Africa continent base
    africa = continent_polys('Africa')
    for p in africa:
        poly = Polygon(p, facecolor=CREAM, edgecolor=GREY, linewidth=1.2, zorder=1)
        ax.add_patch(poly)

    # Highlight Sierra Leone and Liberia
    sl_polys = country_polys('Sierra Leone')
    for p in sl_polys:
        poly = Polygon(p, facecolor=ORANGE, edgecolor=DEEP['orange'], linewidth=2.0, zorder=2)
        ax.add_patch(poly)

    lib_polys = country_polys('Liberia')
    for p in lib_polys:
        poly = Polygon(p, facecolor=GREEN, edgecolor=DEEP['green'], linewidth=2.0, zorder=2)
        ax.add_patch(poly)

    # Other regional neighbors for context
    neighbors = country_polys('Guinea', "Côte d'Ivoire", 'Guinea-Bissau', 'Senegal', 'Mali', 'Ghana')
    for p in neighbors:
        poly = Polygon(p, facecolor='none', edgecolor=GREY, linewidth=0.8, linestyle=':', zorder=1.5)
        ax.add_patch(poly)

    # Coordinates for key cities
    freetown_xy = (-13.23, 8.48)
    monrovia_xy = (-10.80, 6.31)

    # Plot city markers
    ax.plot(*freetown_xy, marker='o', markersize=7, color=INK, zorder=5)
    ax.text(freetown_xy[0] - 0.3, freetown_xy[1] + 0.4, "Freetown", fontsize=14, fontweight='bold', color=INK,
            ha='right', va='bottom', bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.85), zorder=5)

    ax.plot(*monrovia_xy, marker='o', markersize=7, color=INK, zorder=5)
    ax.text(monrovia_xy[0] + 0.3, monrovia_xy[1] - 0.6, "Monrovia", fontsize=14, fontweight='bold', color=INK,
            ha='left', va='top', bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.85), zorder=5)

    # Labels for Countries
    ax.text(-11.8, 8.6, "SIERRA\nLEONE", fontsize=14, fontweight='bold', color=DEEP['orange'],
            ha='center', va='center', zorder=4)
    ax.text(-9.3, 6.8, "LIBERIA", fontsize=14, fontweight='bold', color=DEEP['green'],
            ha='center', va='center', zorder=4)

    # Label surrounding ocean & region
    ax.text(-14.0, 6.5, "ATLANTIC OCEAN", fontsize=16, fontstyle='italic', color=DEEP['blue'], ha='center', va='center')
    ax.text(-10.0, 11.0, "W E S T   A F R I C A", fontsize=15, color=GREY, ha='center', va='center')

    # Historical migration arrows and annotations
    # Arrow 1: toward Freetown (Recaptives)
    ax.annotate(
        "Liberated Africans (Recaptives)\nbrought by British Navy",
        xy=freetown_xy,
        xytext=(-17.0, 10.5),
        arrowprops=dict(
            arrowstyle="->,head_width=0.4,head_length=0.6",
            lw=2.5,
            color=DEEP['blue'],
            connectionstyle="arc3,rad=-0.15"
        ),
        fontsize=14,
        color=INK,
        fontweight='medium',
        ha='left',
        va='center',
        bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.5', lw=1.5),
        zorder=6
    )

    # Arrow 2: toward Monrovia (African Americans from USA)
    ax.annotate(
        "Free African Americans\nfrom the USA",
        xy=monrovia_xy,
        xytext=(-16.5, 4.0),
        arrowprops=dict(
            arrowstyle="->,head_width=0.4,head_length=0.6",
            lw=2.5,
            color=DEEP['pink'],
            connectionstyle="arc3,rad=0.15"
        ),
        fontsize=14,
        color=INK,
        fontweight='medium',
        ha='left',
        va='top',
        bbox=dict(fc='white', ec=DEEP['pink'], boxstyle='round,pad=0.5', lw=1.5),
        zorder=6
    )

    # Title & notes
    ax.text(-8.5, 14.2, "19th-Century Resettlement Settlements in West Africa",
            fontsize=17, fontweight='bold', color=INK, ha='center', va='top')
    ax.text(0.2, 3.8, "Sketch map: zones are approximate",
            fontsize=14, fontstyle='italic', color=GREY, ha='right', va='bottom')

    save(fig, out)
