from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def draw(out):
    fig = canvas(12, 13)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')

    # Color definitions
    color_peaceful = BLUE
    color_peaceful_edge = DEEP["blue"]
    color_armed = DEEP["pink"]  # darker red tone
    color_armed_edge = "#5a101d"
    color_other = CREAM

    # Base continent outline
    africa_base = continent_polys('Africa')
    for p in africa_base:
        ax.add_patch(plt.Polygon(p, facecolor=color_other, edgecolor=GREY, linewidth=1.0, zorder=1))

    # Countries categorized (trying possible Natural Earth name variants)
    peaceful_countries = ['Nigeria', 'Ghana', 'Senegal', "Côte d'Ivoire", 'Ivory Coast']
    armed_countries = ['Algeria', 'Kenya', 'Angola', 'Mozambique', 'Zimbabwe']

    # Draw Constitutional / Peaceful Process countries
    for name in peaceful_countries:
        polys = country_polys(name)
        for p in polys:
            ax.add_patch(plt.Polygon(p, facecolor=color_peaceful, edgecolor=color_peaceful_edge, linewidth=1.5, zorder=2))

    # Draw Armed Struggle countries
    for name in armed_countries:
        polys = country_polys(name)
        for p in polys:
            ax.add_patch(plt.Polygon(p, facecolor=color_armed, edgecolor=color_armed_edge, linewidth=1.5, zorder=2))

    # Set map limits around Africa
    ax.set_xlim(-24, 56)
    ax.set_ylim(-38, 42)

    # Key labels on selected countries
    labels = [
        ('Algeria', (2.5, 28)),
        ('Senegal', (-14.5, 14.5)),
        ('Ivory Coast', (-5.5, 7.5)),
        ('Ghana', (-1.0, 7.8)),
        ('Nigeria', (8.0, 9.5)),
        ('Kenya', (38.0, 0.5)),
        ('Angola', (17.5, -12.5)),
        ('Mozambique', (35.5, -18.5)),
        ('Zimbabwe', (29.5, -19.0)),
    ]

    for text, (lon, lat) in labels:
        ax.text(lon, lat, text, fontsize=14, color=INK, ha='center', va='center',
                fontweight='semibold',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor=GREY, alpha=0.9),
                zorder=4)

    # Title
    ax.text(16.0, 40.5, "Decolonisation of Africa (1960s–1970s)",
            ha='center', va='bottom', fontsize=18, fontweight='bold', color=INK)

    # Legend with proper spacing and vertical label separation
    legend_elements = [
        Patch(facecolor=color_peaceful, edgecolor=color_peaceful_edge, linewidth=1.5,
              label='Constitutional/Peaceful Process'),
        Patch(facecolor=color_armed, edgecolor=color_armed_edge, linewidth=1.5,
              label='Armed Struggle / Guerrilla War'),
        Patch(facecolor=color_other, edgecolor=GREY, linewidth=1.0,
              label='Other / Pre-1960 Independence')
    ]

    leg = ax.legend(handles=legend_elements, loc='lower left',
                    bbox_to_anchor=(0.02, 0.05),
                    frameon=True, facecolor='white', edgecolor=GREY,
                    fontsize=14, labelspacing=1.2, handlelength=2.0, handleheight=1.2,
                    borderpad=1.0, framealpha=0.95,
                    title='Route to Independence', title_fontsize=15)
    leg.get_title().set_fontweight('bold')

    # Note
    ax.text(0.98, 0.02, "Sketch map: zones are approximate",
            transform=ax.transAxes, ha='right', va='bottom', fontsize=14, color=GREY, style='italic')

    save(fig, out)
