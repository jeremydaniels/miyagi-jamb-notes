from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)

    # Set map coordinate bounds (longitude, latitude for West Africa)
    lon_min, lon_max = -18.5, 15.5
    lat_min, lat_max = 2.5, 20.5
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Africa continent base / coastal outline
    africa_polys = continent_polys('Africa')
    for p in africa_polys:
        coords = np.array(p)
        ax.plot(coords[:, 0], coords[:, 1], color=GREY, lw=1.2, zorder=2)

    # Major river course (Niger River)
    niger_river = np.array([
        [-10.5, 9.5], [-8.0, 11.5], [-6.26, 13.44], [-4.2, 14.5], [-3.0, 16.5],
        [-0.5, 17.0], [1.5, 15.5], [3.0, 13.5], [4.5, 11.0], [6.0, 8.0],
        [6.8, 5.5], [6.0, 4.3]
    ])
    ax.plot(niger_river[:, 0], niger_river[:, 1], color=DEEP["blue"], lw=2.0, ls="-", alpha=0.55, zorder=3)
    ax.text(0.5, 16.8, "Niger R.", fontsize=14, color=DEEP["blue"], style='italic',
            bbox=dict(fc="white", ec="none", pad=1, alpha=0.7), zorder=5)

    # 1. Sokoto Caliphate (Green shaded region)
    sokoto_coords = np.array([
        [3.5, 10.5], [3.8, 12.5], [4.5, 14.0], [7.0, 14.5], [9.5, 14.0],
        [12.5, 13.0], [13.5, 11.5], [12.0, 8.5], [9.5, 7.5], [7.0, 8.0],
        [5.0, 9.0], [3.5, 10.5]
    ])
    poly_sokoto = Polygon(sokoto_coords, facecolor=GREEN, edgecolor=DEEP["green"],
                          linewidth=2.2, alpha=0.65, zorder=3)
    ax.add_patch(poly_sokoto)

    # 2. Macina Empire / Hamdallahi (Yellow/Cream shaded region)
    macina_coords = np.array([
        [-5.5, 13.0], [-5.0, 15.0], [-3.8, 16.2], [-2.0, 16.5],
        [-1.0, 15.0], [-2.5, 13.5], [-4.0, 12.8], [-5.5, 13.0]
    ])
    poly_macina = Polygon(macina_coords, facecolor=CREAM, edgecolor=DEEP["orange"],
                          linewidth=2.0, alpha=0.85, zorder=3)
    ax.add_patch(poly_macina)

    # 3. Tukolor Empire (Purple / Lav shaded region)
    tukolor_coords = np.array([
        [-16.0, 16.0], [-13.0, 15.8], [-9.5, 15.5], [-6.0, 14.8],
        [-4.5, 13.5], [-6.0, 12.5], [-9.0, 11.8], [-12.5, 12.0],
        [-15.0, 13.5], [-16.0, 16.0]
    ])
    poly_tukolor = Polygon(tukolor_coords, facecolor=LAV, edgecolor=DEEP["lav"],
                           linewidth=2.2, alpha=0.6, zorder=3)
    ax.add_patch(poly_tukolor)

    # 4. Mandinka / Wassoulou Empire (Red-outlined / Pink region)
    wassoulou_coords = np.array([
        [-10.8, 11.5], [-7.5, 12.0], [-6.0, 11.0], [-5.5, 9.0],
        [-7.0, 7.5], [-9.0, 8.0], [-10.5, 9.0], [-10.8, 11.5]
    ])
    poly_wassoulou = Polygon(wassoulou_coords, facecolor=PINK, edgecolor=DEEP["pink"],
                             linewidth=2.5, alpha=0.6, zorder=3)
    ax.add_patch(poly_wassoulou)

    # Empire Labels
    ax.text(8.5, 11.0, "Sokoto Caliphate\n(Usman dan Fodio)",
            fontsize=14, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3", lw=1.5), zorder=6)

    ax.text(-2.2, 17.8, "Macina Empire / Hamdallahi\n(Seku Ahmadu)",
            fontsize=14, fontweight="bold", color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.3", lw=1.5), zorder=6)
    ax.plot([-2.5, -3.2], [17.7, 15.5], color=INK, lw=1.2, zorder=5)

    ax.text(-12.8, 14.2, "Tukolor Empire\n(Al-Hajj Umar Tall)",
            fontsize=14, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["lav"], boxstyle="round,pad=0.3", lw=1.5), zorder=6)

    # Place Wassoulou label safely above bottom caption area
    ax.text(-8.0, 7.0, "Mandinka / Wassoulou Empire\n(Samori Toure)",
            fontsize=14, fontweight="bold", color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.5), zorder=6)
    ax.plot([-8.0, -8.0], [7.1, 9.0], color=INK, lw=1.2, zorder=5)

    # Important Cities (marker dots explicitly added with zorder above all fills)
    cities = [
        ("Sokoto", 5.23, 13.06, 0.4, 0.35),
        ("Hamdallahi", -4.08, 14.35, -0.4, 0.45),
        ("Segou", -6.26, 13.44, 0.4, 0.35),
        ("Dinguiraye", -10.71, 11.30, -0.5, 0.45),
        ("Kankan", -9.18, 10.38, 0.4, -0.45)
    ]

    for name, cx, cy, ox, oy in cities:
        ax.plot(cx, cy, marker='o', markersize=8, color=INK, markeredgecolor='white',
                markeredgewidth=1.2, zorder=10)
        ax.text(cx + ox, cy + oy, name, fontsize=14, fontweight="bold", color=INK,
                zorder=11, bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", alpha=0.92))

    # Title & Caption
    ax.text(0.5, 0.96, "Islamic Empires of 19th-Century West Africa",
            transform=ax.transAxes, ha="center", va="top", fontsize=18, fontweight="bold", color=INK)
    ax.text(0.5, 0.03, "Sketch map: zones are approximate",
            transform=ax.transAxes, ha="center", va="bottom", fontsize=14, color=GREY, style='italic')

    save(fig, out)
