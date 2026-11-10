from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 12)
    ax = fig.add_subplot(111)
    
    # Geographic bounds: West/Central Africa to Mediterranean
    lon_min, lon_max = -12, 22
    lat_min, lat_max = -1.5, 39.5
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Africa continent base
    africa = continent_polys('Africa')
    for poly in africa:
        pts = np.array(poly)
        ax.add_patch(Polygon(pts, closed=True, facecolor=CREAM, edgecolor=GREY, linewidth=1.2, zorder=1))

    # Highlight Nigeria
    try:
        n_poly = nigeria_poly()
        for poly in n_poly:
            pts = np.array(poly)
            ax.add_patch(Polygon(pts, closed=True, facecolor='#E8F5E9', edgecolor=DEEP['green'], linewidth=1.5, zorder=2))
    except Exception:
        pass

    # Sahara desert band representation
    ax.text(3, 22.5, "SAHARA   DESERT", fontsize=16, color=GREY, alpha=0.7,
            weight='bold', ha='center', va='center', rotation=-5, zorder=2)

    # Rivers: Niger and Benue
    niger_coords = np.array([
        (-9.5, 9.5), (-6.0, 12.0), (-3.0, 14.5), (-0.0, 16.5), 
        (2.5, 13.0), (3.5, 11.5), (4.5, 10.0), (6.5, 8.0), (6.0, 4.5)
    ])
    benue_coords = np.array([
        (13.5, 9.0), (11.0, 8.0), (8.5, 8.0), (6.5, 8.0)
    ])

    ax.plot(niger_coords[:, 0], niger_coords[:, 1], color=DEEP['green'], lw=3.5, zorder=3)
    ax.plot(benue_coords[:, 0], benue_coords[:, 1], color=DEEP['green'], lw=3.5, zorder=3)

    # River Labels
    ax.text(0.5, 11.5, "River Niger", color=DEEP['green'], fontsize=14, weight='bold',
            rotation=60, bbox=dict(fc='white', ec='none', pad=2), zorder=4)
    ax.text(10.0, 9.2, "River Benue", color=DEEP['green'], fontsize=14, weight='bold',
            rotation=-10, bbox=dict(fc='white', ec='none', pad=2), zorder=4)

    # Key Cities / Locations
    cities = {
        "Tunis": (10.2, 36.8),
        "Tripoli": (13.2, 32.9),
        "Kano": (8.5, 12.0),
        "Borno": (13.0, 11.8),
        "Lagos": (3.4, 6.4),
        "Calabar": (8.3, 5.0)
    }

    for name, (cx, cy) in cities.items():
        ax.plot(cx, cy, 'o', color=INK, markersize=5, zorder=5)
        if name in ["Tunis", "Tripoli"]:
            offset = (0, 1.4)
        elif name in ["Kano", "Borno"]:
            offset = (0, -1.5)
        else:
            offset = (0, 1.0)
        ax.text(cx + offset[0], cy + offset[1], name, fontsize=14, weight='bold',
                ha='center', va='center', color=INK,
                bbox=dict(fc='white', ec='none', pad=1), zorder=5)

    # Trans-Saharan Trade Routes (Red arrows pointing northwards)
    # Kano -> Tripoli
    ax.annotate("", xy=(13.0, 31.8), xytext=(8.8, 13.0),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['pink'], lw=3.5), zorder=4)
    # Kano -> Tunis
    ax.annotate("", xy=(10.5, 35.5), xytext=(8.0, 13.0),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['pink'], lw=3.5, linestyle="--"), zorder=4)
    # Borno -> Tripoli (Bilma route)
    ax.annotate("", xy=(13.5, 31.8), xytext=(13.2, 13.0),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['pink'], lw=3.5), zorder=4)

    # Trans-Atlantic Trade Routes (Blue arrows pointing southwards to Atlantic)
    # Lagos seaward
    ax.annotate("", xy=(2.5, 2.5), xytext=(3.4, 5.8),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['blue'], lw=3.5), zorder=4)
    # Niger Delta / Calabar seaward
    ax.annotate("", xy=(6.0, 2.2), xytext=(6.0, 4.3),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['blue'], lw=3.5), zorder=4)
    ax.annotate("", xy=(9.5, 2.4), xytext=(8.5, 4.6),
                arrowprops=dict(arrowstyle="->,head_length=1.0,head_width=0.6",
                                color=DEEP['blue'], lw=3.5), zorder=4)

    # Ocean labels
    ax.text(12.0, 36.2, "Mediterranean Sea", color=DEEP['blue'], fontsize=14,
            style='italic', bbox=dict(fc='white', ec='none', pad=2), zorder=4)
    ax.text(-2.5, 3.5, "Atlantic Ocean", color=DEEP['blue'], fontsize=16,
            style='italic', bbox=dict(fc='white', ec='none', pad=2), zorder=4)

    # Trans-Saharan Label
    ax.text(1.5, 26.5,
            "Trans-Saharan Trade\n(Slaves, Kola, Hides for Salt, Horses)",
            color=DEEP['pink'], fontsize=14, weight='bold', ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['pink'], boxstyle='round,pad=0.5', lw=1.5), zorder=6)

    # Inland Waterway Routes Label
    ax.text(-4.5, 17.5,
            "Inland Waterway Routes",
            color=DEEP['green'], fontsize=14, weight='bold', ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.5', lw=1.5), zorder=6)
    ax.annotate("", xy=(-1.5, 16.0), xytext=(-3.5, 16.8),
                arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=1.8), zorder=6)

    # Trans-Atlantic Label placed clearly separated from caption
    ax.text(3.5, 0.2,
            "Trans-Atlantic Trade\n(Slaves, Ivory for Guns, Spirits)",
            color=DEEP['blue'], fontsize=14, weight='bold', ha='center', va='center',
            bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.5', lw=1.5), zorder=6)

    # Main Title and Caption
    ax.text(5.0, 38.6, "Traditional Trade Routes of Nigeria and North Africa",
            fontsize=17, weight='bold', ha='center', color=INK)
    ax.text(21.0, -1.0, "Sketch map: zones are approximate",
            fontsize=14, style='italic', color=GREY, ha='right')

    save(fig, out)
