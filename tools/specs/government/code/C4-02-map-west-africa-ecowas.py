from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(11, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Base map: Africa outline / background
    africa = continent_polys('Africa')
    for poly in africa:
        ax.fill(poly[:, 0], poly[:, 1], facecolor='#F3F4F6', edgecolor=GREY, linewidth=0.8, zorder=1)

    # ECOWAS members (excluding Nigeria for separate highlight)
    # Include variant names for Ivory Coast to ensure it's picked up by the helper
    ecowas_others = [
        'Benin', 'Burkina Faso', 'Cabo Verde', "Côte d'Ivoire", "Cote d'Ivoire", "Ivory Coast", 'Gambia',
        'Ghana', 'Guinea', 'Guinea-Bissau', 'Liberia', 'Mali',
        'Niger', 'Senegal', 'Sierra Leone', 'Togo'
    ]

    # Draw other ECOWAS members in soft GREEN
    other_polys = country_polys(*ecowas_others)
    for poly in other_polys:
        ax.fill(poly[:, 0], poly[:, 1], facecolor=GREEN, edgecolor=DEEP['green'], linewidth=1.2, zorder=2)

    # Draw Nigeria in dark green (DEEP['green'])
    nig_polys = country_polys('Nigeria')
    if not nig_polys:
        nig_polys = [nigeria_poly()]
    for poly in nig_polys:
        ax.fill(poly[:, 0], poly[:, 1], facecolor=DEEP['green'], edgecolor='#0f3922', linewidth=1.5, zorder=3)

    # Set map extent with ample margins to avoid overlap
    ax.set_xlim(-19.0, 18.0)
    ax.set_ylim(2.5, 26.0)

    # Mark Abuja (ECOWAS headquarters: 7.49° E, 9.06° N)
    abuja_lon, abuja_lat = 7.49, 9.06
    ax.plot(abuja_lon, abuja_lat, marker='*', markersize=16, color=ORANGE, markeredgecolor=INK, markeredgewidth=1.2, zorder=5)

    # Label for Abuja / ECOWAS Headquarters pointing towards Gulf of Guinea / south-west of Abuja
    ax.annotate(
        "Abuja\n(ECOWAS HQ)",
        xy=(abuja_lon, abuja_lat),
        xytext=(abuja_lon + 1.0, abuja_lat - 3.2),
        fontsize=14,
        color=INK,
        fontweight='bold',
        ha='left',
        va='top',
        zorder=6,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.0),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3, shrinkB=4)
    )

    # Title
    ax.text(
        -18.0, 24.8,
        "ECOWAS Member States",
        fontsize=18,
        fontweight='bold',
        color=INK,
        ha='left',
        va='top',
        bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="none")
    )

    # Inset box listing the benefits (bottom-left)
    benefits_text = (
        "Key Benefits:\n"
        "• Free Movement\n"
        "• Regional Trade\n"
        "• Security (ECOMOG)"
    )
    ax.text(
        -18.0, 3.8,
        benefits_text,
        fontsize=14,
        color=INK,
        ha='left',
        va='bottom',
        linespacing=1.5,
        bbox=dict(boxstyle="round,pad=0.5", fc=CREAM, ec=GREY, lw=1.2),
        zorder=6
    )

    # Legend / Key (upper right, spaced appropriately to avoid label overlaps)
    legend_elements = [
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=GREEN, markeredgecolor=DEEP['green'], markersize=14, label='ECOWAS Member'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=DEEP['green'], markeredgecolor='#0f3922', markersize=14, label='Nigeria'),
        plt.Line2D([0], [0], marker='*', color='w', markerfacecolor=ORANGE, markeredgecolor=INK, markersize=16, label='ECOWAS Headquarters')
    ]
    ax.legend(
        handles=legend_elements,
        loc='upper right',
        fontsize=14,
        labelspacing=1.1,
        borderpad=0.8,
        handletextpad=0.7,
        frameon=True,
        facecolor='white',
        edgecolor=GREY,
        framealpha=0.95
    )

    # Footnote / sketch map note at the far bottom right
    ax.text(
        17.0, 3.0,
        "Sketch map: zones are approximate",
        fontsize=14,
        color=GREY,
        ha='right',
        va='bottom',
        bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none")
    )

    save(fig, out)
