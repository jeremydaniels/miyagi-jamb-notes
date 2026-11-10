from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(-100, 25)
    ax.set_ylim(-15, 65)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw continents/land masses using helper
    polys = continent_polys('World')
    for poly in polys:
        ax.add_patch(plt.Polygon(poly, facecolor=CREAM, edgecolor=GREY, linewidth=1.2, zorder=1))

    # Regional labels
    regions = [
        ("NORTH\nAMERICA", (-82, 38)),
        ("EUROPE", (-5, 52)),
        ("WEST\nAFRICA", (-5, 12)),
        ("CARIBBEAN", (-75, 18)),
        ("SOUTH\nAMERICA", (-55, -2)),
    ]
    for name, pos in regions:
        ax.text(pos[0], pos[1], name, fontsize=14, fontweight='bold', color=INK,
                ha='center', va='center', zorder=2,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.7))

    # Water label
    ax.text(-40, 28, "ATLANTIC\nOCEAN", fontsize=16, fontstyle='italic', color=GREY,
            ha='center', va='center', zorder=1)

    # Arrow 1: Europe to West Africa (Blue)
    # Manufactured goods, guns, rum
    ax.annotate(
        "",
        xy=(-10, 15), xycoords='data',
        xytext=(-5, 47), textcoords='data',
        arrowprops=dict(
            arrowstyle="-|>,head_length=0.9,head_width=0.6",
            color=DEEP["blue"],
            lw=3.5,
            connectionstyle="arc3,rad=-0.2"
        ),
        zorder=3
    )
    ax.text(3, 31, "Manufactured goods,\nguns, rum",
            fontsize=14, fontweight='bold', color=DEEP["blue"],
            ha='center', va='center', zorder=4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=DEEP["blue"], lw=1.5))

    # Arrow 2: West Africa to Americas (Red/Pink deep)
    # The Middle Passage: Enslaved Africans
    ax.annotate(
        "",
        xy=(-65, 18), xycoords='data',
        xytext=(-12, 8), textcoords='data',
        arrowprops=dict(
            arrowstyle="-|>,head_length=0.9,head_width=0.6",
            color=DEEP["pink"],
            lw=3.5,
            connectionstyle="arc3,rad=0.1"
        ),
        zorder=3
    )
    ax.text(-38, 7, "The Middle Passage:\nEnslaved Africans",
            fontsize=14, fontweight='bold', color=DEEP["pink"],
            ha='center', va='center', zorder=4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=DEEP["pink"], lw=1.5))

    # Arrow 3: Americas back to Europe (Green)
    # Raw materials: Sugar, Cotton, Tobacco
    ax.annotate(
        "",
        xy=(-10, 50), xycoords='data',
        xytext=(-68, 26), textcoords='data',
        arrowprops=dict(
            arrowstyle="-|>,head_length=0.9,head_width=0.6",
            color=DEEP["green"],
            lw=3.5,
            connectionstyle="arc3,rad=-0.22"
        ),
        zorder=3
    )
    ax.text(-47, 44, "Raw materials:\nSugar, Cotton, Tobacco",
            fontsize=14, fontweight='bold', color=DEEP["green"],
            ha='center', va='center', zorder=4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=DEEP["green"], lw=1.5))

    # Title & Caption
    ax.text(-40, 62, "The Triangular Trade", fontsize=18, fontweight='bold', color=INK,
            ha='center', va='center', zorder=5)
    ax.text(-40, -12, "Sketch map: zones are approximate", fontsize=14, fontstyle='italic',
            color=GREY, ha='center', va='center', zorder=5)

    save(fig, out)
