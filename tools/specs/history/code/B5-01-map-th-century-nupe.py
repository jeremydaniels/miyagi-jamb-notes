import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from style import *

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    
    # Coordinate bounds for Central Nigeria (around Nupe / Niger-Benue confluence)
    # Longitude: approx 4.5°E to 8.5°E
    # Latitude: approx 7.2°N to 10.2°N
    lon_min, lon_max = 4.5, 8.5
    lat_min, lat_max = 7.0, 10.2
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background / Title
    ax.text(6.5, 10.0, "The Nupe Emirate in the 19th Century", 
            fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(6.5, 9.68, "Expansion from Bida across the Niger River", 
            fontsize=14, fontstyle='italic', ha='center', va='center', color=INK)

    # Approximate territory of the Nupe Emirate in the 19th century
    nupe_poly_coords = [
        (5.0, 9.2), (5.5, 9.6), (6.1, 9.6), (6.8, 9.4), 
        (7.2, 9.0), (7.0, 8.4), (6.8, 8.0), (6.4, 7.8), 
        (5.8, 8.1), (5.2, 8.5), (4.9, 8.8)
    ]
    nupe_poly = Polygon(nupe_poly_coords, closed=True, facecolor=CREAM, 
                        edgecolor=DEEP["orange"], linestyle='--', linewidth=2.0, alpha=0.85, zorder=1)
    ax.add_patch(nupe_poly)

    # Region label
    ax.text(5.5, 9.0, "NUPE\nEMIRATE", fontsize=16, fontweight='bold', 
            color=DEEP["orange"], ha='center', va='center', zorder=2,
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.6))

    # Niger River path: flows from NW (Kwara/Jebba area) through Bida region, turning south to Lokoja
    # Jebba ~ (4.8, 9.1), Rabba ~ (5.0, 9.2), Pategi ~ (5.7, 8.7), Baro ~ (6.4, 8.6), Lokoja ~ (6.74, 7.8)
    # Beyond Lokoja flows south towards Niger Delta
    niger_river = [
        (4.5, 9.4), (4.8, 9.15), (5.1, 8.95), (5.5, 8.75), 
        (5.8, 8.65), (6.2, 8.6), (6.5, 8.4), (6.74, 7.8), 
        (6.75, 7.4), (6.7, 7.0)
    ]
    nr_x, nr_y = zip(*niger_river)
    
    # Benue River: joins Niger at Lokoja from East
    benue_river = [
        (8.5, 8.0), (8.0, 7.95), (7.5, 7.9), (7.1, 7.85), (6.74, 7.8)
    ]
    br_x, br_y = zip(*benue_river)

    # Kaduna River: tributary passing near Bida into Niger
    kaduna_river = [
        (6.8, 9.8), (6.3, 9.4), (6.0, 8.9), (5.8, 8.65)
    ]
    kr_x, kr_y = zip(*kaduna_river)

    # Plot Rivers
    ax.plot(nr_x, nr_y, color=DEEP["blue"], lw=4.5, zorder=3, solid_capstyle='round')
    ax.plot(br_x, br_y, color=DEEP["blue"], lw=3.8, zorder=3, solid_capstyle='round')
    ax.plot(kr_x, kr_y, color=DEEP["blue"], lw=2.2, zorder=3, linestyle='-', alpha=0.8)

    # River labels
    ax.text(4.8, 9.35, "Niger R.", color=DEEP["blue"], fontsize=14, fontstyle='italic', rotation=-30)
    ax.text(7.6, 8.1, "Benue R.", color=DEEP["blue"], fontsize=14, fontstyle='italic', rotation=5)
    ax.text(6.4, 9.3, "Kaduna R.", color=DEEP["blue"], fontsize=13, fontstyle='italic', rotation=-45)

    # Key Locations
    # Bida: Capital (6.01°E, 9.08°N)
    bida = (6.01, 9.08)
    ax.plot(bida[0], bida[1], marker='*', color=DEEP["pink"], markersize=18, 
            markeredgecolor=INK, markeredgewidth=1.2, zorder=6)
    ax.text(bida[0] + 0.1, bida[1] + 0.15, "Bida\n(Capital)", fontsize=15, fontweight='bold', 
            color=INK, zorder=7, bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', alpha=0.9))

    # Other towns: Kabba (~6.07°E, 7.83°N), Lokoja (~6.74°E, 7.80°N)
    towns = {
        "Lokoja": (6.74, 7.80),
        "Kabba": (6.07, 7.83),
        "Rabba": (5.03, 9.15)
    }

    for name, (tx, ty) in towns.items():
        ax.plot(tx, ty, marker='o', color=INK, markersize=6, zorder=6)
        offset_y = -0.22 if name != "Rabba" else 0.15
        offset_x = 0.0 if name != "Lokoja" else 0.25
        ha = 'center' if name != "Lokoja" else 'left'
        ax.text(tx + offset_x, ty + offset_y, name, fontsize=14, color=INK, 
                fontweight='semibold', ha=ha, va='center', zorder=7,
                bbox=dict(fc='white', ec='none', pad=1, alpha=0.85))

    # Annotation for Niger-Benue confluence
    ax.annotate("Niger–Benue\nconfluence", xy=(6.74, 7.80), xytext=(7.4, 7.35),
                fontsize=14, color=INK, ha='center', va='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2, shrinkB=6),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', alpha=0.9), zorder=7)

    # Expansion Arrows from Bida:
    # 1. Towards Kabba (South)
    ax.annotate("", xy=(6.05, 8.05), xytext=(6.01, 8.9),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7", 
                                color=DEEP["pink"], lw=3.0, shrinkA=8, shrinkB=8), zorder=5)

    # 2. Towards Lokoja / Confluence (Southeast)
    ax.annotate("", xy=(6.6, 7.95), xytext=(6.1, 8.95),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7", 
                                color=DEEP["pink"], lw=3.0, shrinkA=8, shrinkB=8), zorder=5)

    # 3. Southwest across the Niger
    ax.annotate("", xy=(5.5, 8.2), xytext=(5.9, 8.95),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7", 
                                color=DEEP["pink"], lw=3.0, shrinkA=8, shrinkB=8), zorder=5)

    # Expansion Legend / Label
    ax.text(5.05, 7.5, "Nupe expansion / raids\ninto Northeast Yoruba\nand confluence regions", 
            fontsize=14, fontstyle='italic', color=DEEP["pink"], 
            bbox=dict(fc='white', ec=DEEP["pink"], boxstyle='round,pad=0.4', lw=1.2), zorder=7)

    # North arrow
    ax.annotate('N', xy=(4.8, 9.85), xytext=(4.8, 9.6),
                ha='center', va='center', fontsize=14, fontweight='bold', color=INK,
                arrowprops=dict(arrowstyle='<|-', color=INK, lw=1.5), zorder=7)

    # Map border & schematic caption
    rect = plt.Rectangle((lon_min + 0.05, lat_min + 0.05), lon_max - lon_min - 0.1, lat_max - lat_min - 0.1,
                         fill=False, edgecolor=GREY, lw=1.2, zorder=10)
    ax.add_patch(rect)
    ax.text(6.5, 7.15, "Sketch map: zones are approximate", fontsize=14, 
            ha='center', va='center', color=GREY, fontstyle='italic', zorder=10)

    save(fig, out)
