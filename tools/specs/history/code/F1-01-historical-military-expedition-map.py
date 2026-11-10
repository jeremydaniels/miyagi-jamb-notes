from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    
    # Horn of Africa coordinates
    lon_min, lon_max = 34.0, 48.0
    lat_min, lat_max = 6.0, 18.0
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Background
    ax.set_facecolor('white')

    # Country polygons via helper if available
    try:
        countries = country_polys('Ethiopia', 'Eritrea', 'Djibouti', 'Somalia', 'Sudan', 'South Sudan', 'Yemen', 'Saudi Arabia')
        for poly in countries:
            ax.add_patch(plt.Polygon(poly, facecolor='#FAF8F5', edgecolor=GREY, lw=1.2, zorder=1))
    except Exception:
        pass

    # Simplified schematic water bodies (Red Sea & Gulf of Aden)
    red_sea_pts = np.array([
        [37.5, 18.0], [41.0, 16.0], [43.5, 12.5], [43.3, 11.5],
        [45.0, 11.5], [48.0, 12.0], [48.0, 14.5], [44.0, 14.0],
        [42.5, 16.5], [39.0, 18.0]
    ])
    ax.fill(red_sea_pts[:,0], red_sea_pts[:,1], color='#EAF2F8', zorder=2)
    ax.plot(red_sea_pts[:,0], red_sea_pts[:,1], color=DEEP["blue"], lw=1, alpha=0.5, zorder=2)

    # Lake Tana schematic
    t_angle = np.linspace(0, 2*np.pi, 50)
    tana_x = 37.3 + 0.45 * np.cos(t_angle) + 0.1 * np.sin(2*t_angle)
    tana_y = 12.0 + 0.45 * np.sin(t_angle)
    ax.fill(tana_x, tana_y, color='#D4E6F1', ec=DEEP["blue"], lw=1.2, zorder=3)
    ax.text(36.3, 12.0, "Lake\nTana", fontsize=14, color=INK, ha='center', va='center', zorder=5)

    # Ethiopian Empire approximate core territory boundary (late 19th c.)
    eth_poly = np.array([
        [36.5, 14.2], [39.5, 14.8], [40.5, 13.0], [42.0, 10.5],
        [42.5, 9.0], [40.5, 7.5], [38.0, 7.0], [35.5, 8.5],
        [35.0, 11.0], [36.0, 13.0], [36.5, 14.2]
    ])
    ax.fill(eth_poly[:,0], eth_poly[:,1], color=ORANGE, alpha=0.18, zorder=2)
    ax.plot(eth_poly[:,0], eth_poly[:,1], color=DEEP["orange"], lw=2, ls='--', zorder=3)

    # Empire label shifted to the southwest of Magdala/Lake Tana to avoid overlap
    ax.text(37.5, 10.0, "ETHIOPIAN\nEMPIRE", fontsize=16, fontweight='bold', color=INK, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8), zorder=4)

    # Water labels
    ax.text(39.8, 16.8, "RED  SEA", fontsize=15, fontstyle='italic', color=DEEP["blue"], rotation=-32, zorder=4)
    ax.text(45.5, 11.2, "Gulf of Aden", fontsize=14, fontstyle='italic', color=DEEP["blue"], rotation=5, zorder=4)

    # Coastal area of Eritrea
    ax.text(38.8, 15.5, "ERITREA\n(Coastal Region)", fontsize=14, fontweight='bold', color=INK, ha='center',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7), zorder=5)

    # Region of Shewa (Shoa) to the south
    ax.text(39.0, 8.4, "SHEWA (SHOA)", fontsize=15, fontweight='bold', color=DEEP["orange"], ha='center',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=5)

    # Locations
    # 1. Gondar (Old capital) ~ 37.47 E, 12.60 N
    gondar = (37.47, 12.60)
    ax.scatter([gondar[0]], [gondar[1]], color=DEEP["orange"], edgecolors=INK, s=90, zorder=6)
    ax.text(gondar[0] - 0.3, gondar[1] + 0.35, "Gondar\n(Old Capital)", fontsize=14, ha='right', va='bottom',
            fontweight='bold', color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8), zorder=6)

    # 2. Magdala (Fortress) ~ 39.31 E, 11.37 N
    magdala = (39.31, 11.37)
    ax.scatter([magdala[0]], [magdala[1]], color=DEEP["pink"], edgecolors=INK, s=110, marker='s', zorder=6)
    ax.text(magdala[0] + 0.35, magdala[1] - 0.15, "Magdala\n(Fortress)", fontsize=14, ha='left', va='center',
            fontweight='bold', color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8), zorder=6)

    # 3. Zula / Annesley Bay (Start of Napier Expedition) ~ 39.7 E, 15.2 N
    zula = (39.7, 15.25)
    ax.scatter([zula[0]], [zula[1]], color=DEEP["blue"], edgecolors=INK, s=70, zorder=6)
    ax.text(zula[0] + 0.35, zula[1] + 0.15, "Zula (Coast)", fontsize=14, ha='left', va='bottom', color=INK,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8), zorder=6)

    # Route of Napier Expedition (1868)
    route_lons = [39.7, 39.45, 39.55, 39.6, 39.4, 39.31]
    route_lats = [15.25, 14.7, 13.9, 13.3, 12.2, 11.37]
    ax.plot(route_lons, route_lats, color=DEEP["pink"], lw=3.0, ls='--', zorder=5)

    # Napier route label with arrow annotation
    ax.annotate("Napier Expedition (1868)\nBritish march inland", 
                xy=(39.55, 13.3), xytext=(42.2, 13.8),
                fontsize=14, color=DEEP["pink"], fontweight='bold',
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["pink"], lw=1.2),
                zorder=7)

    # Title
    ax.text(lon_min + 0.5, lat_max - 0.8, "The Ethiopian Empire & Napier Expedition (1868)",
            fontsize=17, fontweight='bold', color=INK, va='top', zorder=8)
    
    # Caption
    ax.text(lon_min + 0.5, lat_min + 0.5, "Sketch map: zones are approximate",
            fontsize=14, fontstyle='italic', color=GREY, va='bottom', zorder=8)

    save(fig, out)
