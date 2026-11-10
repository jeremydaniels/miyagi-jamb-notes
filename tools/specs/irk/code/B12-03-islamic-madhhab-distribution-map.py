from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-20, 145)
    ax.set_ylim(-35, 55)
    ax.axis('off')

    # Draw continental outlines (simplified, no country borders)
    try:
        continents = continent_polys('Africa') + continent_polys('Asia') + continent_polys('Europe')
        for poly in continents:
            ax.plot(poly[:, 0], poly[:, 1], color=GREY, lw=1.2, zorder=1)
    except:
        pass

    # Define simple zone polygons
    maliki_x = [-18, -10, 15, 32, 28, 15, 0, -18]
    maliki_y = [15, -5, -5, 18, 38, 38, 30, 25]
    
    hanafi_x = [26, 45, 75, 100, 95, 75, 65, 50, 26]
    hanafi_y = [36, 45, 50, 40, 20, 5, 20, 30, 40]
    
    shafii_ea_x = [30, 42, 52, 45, 30]
    shafii_ea_y = [15, -15, -15, 12, 18]
    
    shafii_se_x = [95, 120, 145, 145, 120, 95]
    shafii_se_y = [10, 20, 10, -10, -15, -5]
    
    hanbali_x = [35, 40, 60, 55, 35]
    hanbali_y = [28, 12, 13, 28, 32]

    # Draw colored zones
    ax.fill(maliki_x, maliki_y, color=GREEN, alpha=0.5, zorder=0)
    ax.fill(hanafi_x, hanafi_y, color=BLUE, alpha=0.5, zorder=0)
    ax.fill(shafii_ea_x, shafii_ea_y, color=ORANGE, alpha=0.5, zorder=0)
    ax.fill(shafii_se_x, shafii_se_y, color=ORANGE, alpha=0.5, zorder=0)
    ax.fill(hanbali_x, hanbali_y, color=LAV, alpha=0.5, zorder=0)

    # Zone labels (no bbox to put them directly in zones)
    ax.text(5, 23, "Maliki", fontsize=18, color=DEEP['green'], fontweight='bold', ha='center', va='center', zorder=2)
    ax.text(65, 35, "Hanafi", fontsize=18, color=DEEP['blue'], fontweight='bold', ha='center', va='center', zorder=2)
    ax.text(120, 0, "Shafi'i", fontsize=18, color=DEEP['orange'], fontweight='bold', ha='center', va='center', zorder=2)
    ax.text(42, 0, "Shafi'i", fontsize=16, color=DEEP['orange'], fontweight='bold', ha='center', va='center', zorder=2)
    ax.text(50, 18, "Hanbali", fontsize=18, color=DEEP['lav'], fontweight='bold', ha='center', va='center', zorder=2)

    # Reference dots and labels
    dots = [
        (8, 9, "Nigeria", "left", 2, -1),
        (30, 27, "Egypt", "right", -2, -1),
        (39.8, 21.4, "Mecca", "right", -2, 1),
        (114, -0.5, "Indonesia", "left", 2, -1)
    ]

    for x, y, label, align, dx, dy in dots:
        ax.plot(x, y, 'o', color=INK, markersize=6, zorder=3)
        ax.text(x + dx, y + dy, label, fontsize=14, color=INK, 
                ha=align, va='center', bbox=dict(fc="white", ec="none", pad=1, alpha=0.8), zorder=4)

    # Caption
    ax.text(-15, -30, "Sketch map: zones are approximate", fontsize=14, color=GREY, style='italic', zorder=4)

    save(fig, out)
