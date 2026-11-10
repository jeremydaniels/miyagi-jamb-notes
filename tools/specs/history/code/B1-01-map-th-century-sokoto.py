from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    
    # Range of Nigeria region: Longitude 2.5 to 14.5 E, Latitude 3.8 to 14.4 N
    ax.set_xlim(2.5, 14.5)
    ax.set_ylim(3.8, 14.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw modern Nigeria outline faintly as reference
    try:
        n_polys = nigeria_poly()
        for poly in n_polys:
            xs, ys = poly.exterior.xy
            ax.plot(xs, ys, color=GREY, lw=1.2, ls="--", alpha=0.7, zorder=1)
    except Exception:
        pass

    # Rivers (Niger and Benue sketch)
    niger_x = [3.6, 4.4, 5.0, 6.0, 6.7, 6.7, 6.1]
    niger_y = [11.6, 10.0, 9.0, 8.5, 7.8, 6.0, 4.4]
    ax.plot(niger_x, niger_y, color=DEEP["blue"], lw=2.0, alpha=0.6, zorder=2)
    
    benue_x = [6.7, 7.8, 9.3, 11.0, 12.5]
    benue_y = [7.8, 7.9, 8.8, 9.3, 9.5]
    ax.plot(benue_x, benue_y, color=DEEP["blue"], lw=2.0, alpha=0.6, zorder=2)

    # 1. Sokoto Caliphate territory polygon
    # Covers most of northern Nigeria, extending down to Nupe and Ilorin, and east to Adamawa
    sokoto_coords = [
        (3.5, 11.5), (4.2, 12.8), (5.2, 13.8), (7.5, 13.5), (8.8, 13.0),
        (10.0, 12.5), (10.8, 11.2), (11.0, 10.0), (12.8, 10.2), (13.5, 9.0),
        (13.2, 7.5), (11.8, 7.0), (10.2, 7.5), (8.5, 7.8), (7.5, 7.6),
        (4.5, 8.0), (4.0, 9.0), (3.8, 10.2)
    ]
    sokoto_poly = Polygon(sokoto_coords, closed=True, fc=GREEN, ec=DEEP["green"], lw=2.5, alpha=0.35, zorder=2)
    ax.add_patch(sokoto_poly)

    # 2. Borno Empire polygon (Northeast)
    borno_coords = [
        (10.8, 11.2), (10.0, 12.5), (11.2, 13.6), (13.8, 13.8), 
        (14.2, 12.2), (13.5, 11.0), (12.2, 10.8)
    ]
    borno_poly = Polygon(borno_coords, closed=True, fc=LAV, ec=DEEP["lav"], lw=2.0, ls="-", alpha=0.4, zorder=2)
    ax.add_patch(borno_poly)

    # 3. Oyo Empire polygon (Southwest)
    oyo_coords = [
        (2.8, 7.2), (4.3, 8.3), (4.8, 7.8), (4.8, 6.8), (3.5, 6.5)
    ]
    oyo_poly = Polygon(oyo_coords, closed=True, fc=PINK, ec=DEEP["pink"], lw=2.0, ls="-", alpha=0.4, zorder=2)
    ax.add_patch(oyo_poly)

    # Region Labels
    ax.text(8.0, 11.8, "SOKOTO CALIPHATE", fontsize=17, fontweight="bold", color=DEEP["green"], ha="center", va="center", zorder=5)
    ax.text(12.5, 12.4, "BORNO\nEMPIRE", fontsize=15, fontweight="bold", color=DEEP["lav"], ha="center", va="center", multialignment="center", zorder=5)
    ax.text(3.7, 7.2, "OYO\nEMPIRE", fontsize=14, fontweight="bold", color=DEEP["pink"], ha="center", va="center", multialignment="center", zorder=5)

    # Twin Capitals (Stars)
    # Sokoto: lat ~13.06, lon ~5.24; Gwandu: lat ~12.45, lon ~4.64
    capitals = [
        ("Gwandu (West)", 4.64, 12.45, -0.3, -0.45),
        ("Sokoto (East)", 5.24, 13.06, 0.2, 0.35)
    ]
    for name, lon, lat, ox, oy in capitals:
        ax.plot(lon, lat, marker="*", markersize=18, color=DEEP["orange"], markeredgecolor=INK, markeredgewidth=1.2, zorder=10)
        ax.annotate(name, xy=(lon, lat), xytext=(lon + ox, lat + oy),
                    fontsize=14, fontweight="bold", color=INK, zorder=11,
                    bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85))

    # Key Emirate Cities (Dots)
    emirates = [
        ("Katsina", 7.60, 12.99, 0.25, 0.2),
        ("Kano", 8.52, 12.00, 0.25, 0.1),
        ("Zaria", 7.71, 11.08, 0.25, -0.1),
        ("Bauchi", 9.84, 10.31, 0.25, -0.1),
        ("Nupe (Bida)", 6.01, 9.08, 0.25, 0.1),
        ("Ilorin", 4.55, 8.49, 0.25, -0.2),
        ("Adamawa", 12.45, 9.32, 0.25, 0.0)
    ]

    for city, lon, lat, ox, oy in emirates:
        ax.plot(lon, lat, marker="o", markersize=8, color=INK, zorder=10)
        ax.text(lon + ox, lat + oy, city, fontsize=14, color=INK, va="center",
                bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.85), zorder=11)

    # Title & Subtitle
    ax.text(8.5, 14.1, "The Sokoto Caliphate (Mid-19th Century)", fontsize=18, fontweight="bold", ha="center", color=INK)
    ax.text(8.5, 13.7, "Twin capitals, major emirates, and neighbouring states", fontsize=14, ha="center", color=INK)

    # Legend / Key Box
    legend_x, legend_y = 9.8, 4.6
    ax.plot(legend_x, legend_y + 0.9, marker="*", markersize=16, color=DEEP["orange"], markeredgecolor=INK, markeredgewidth=1.2, zorder=10)
    ax.text(legend_x + 0.4, legend_y + 0.9, "Twin Capitals", fontsize=14, va="center", color=INK)

    ax.plot(legend_x, legend_y + 0.3, marker="o", markersize=8, color=INK, zorder=10)
    ax.text(legend_x + 0.4, legend_y + 0.3, "Major Emirate City", fontsize=14, va="center", color=INK)

    # Caption
    ax.text(8.5, 4.0, "Sketch map: zones are approximate", fontsize=14, style="italic", ha="center", color=INK)

    save(fig, out)
