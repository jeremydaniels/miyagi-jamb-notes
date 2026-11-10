from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

def draw(out):
    # Canvas with plenty of vertical breathing room
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(2.5, 15.0)
    ax.set_ylim(8.2, 16.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Base map: Nigeria boundary
    try:
        n_polys = nigeria_poly()
        for poly in n_polys:
            ax.add_patch(Polygon(poly, closed=True, facecolor='#FAF8F5', edgecolor=GREY, lw=1.5, zorder=1))
    except Exception:
        pass

    # Titles placed clearly at the top (y = 15.65, 15.2) well above route arrows
    ax.text(8.75, 15.65, "Pre-Colonial Northern Nigeria", fontsize=18, weight='bold', ha='center', color=INK)
    ax.text(8.75, 15.2, "Hausawa States (Hausa Bakwai) & Kanem-Borno", fontsize=14, ha='center', color=INK, style='italic')

    # Trans-Saharan route destination banner below titles, above arrow tips
    ax.text(8.75, 14.55, "To the Sahara (Trans-Saharan Routes)", fontsize=14,
            ha='center', va='center', color=DEEP['pink'], weight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['pink'], lw=1.2), zorder=6)

    # Lake Chad representation (northeast)
    chad_x = [13.2, 14.3, 14.6, 14.1, 13.5]
    chad_y = [12.8, 13.4, 13.0, 12.3, 12.5]
    ax.fill(chad_x, chad_y, color=BLUE, alpha=0.5, zorder=2)
    ax.plot(chad_x + [chad_x[0]], chad_y + [chad_y[0]], color=DEEP['blue'], lw=1.5, zorder=2)
    ax.text(13.9, 12.85, "Lake\nChad", fontsize=14, ha='center', va='center', color=DEEP['blue'], weight='bold', zorder=4)

    # Kanem-Borno region highlight
    borno_patch = Circle((12.2, 12.0), 1.45, facecolor=CREAM, edgecolor=DEEP['orange'], lw=2, linestyle='--', zorder=2)
    ax.add_patch(borno_patch)
    ax.text(12.2, 11.4, "Kanem-Borno\n(Kanuri)", fontsize=15, ha='center', va='center', weight='bold', color=DEEP['orange'],
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['orange'], lw=1.2), zorder=4)

    # Hausaland zone highlight
    hausa_zone = Circle((7.8, 11.8), 2.2, facecolor='#F3F8F2', edgecolor=DEEP['green'], lw=1.5, linestyle=':', zorder=2)
    ax.add_patch(hausa_zone)
    ax.text(5.5, 13.7, "Hausa Bakwai States", fontsize=15, color=DEEP['green'], weight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=4)

    # Hausa Bakwai city coordinates
    cities = {
        "Gobir": (5.2, 13.1),
        "Katsina": (7.6, 12.95),
        "Daura": (8.4, 13.05),
        "Kano": (8.5, 12.0),
        "Rano": (8.6, 11.45),
        "Biram": (9.7, 12.25),
        "Zaria": (7.7, 11.0)
    }

    # Walled city icon helper (circle with bastions)
    def draw_walled_city(cx, cy):
        ax.add_patch(Circle((cx, cy), 0.16, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=5))
        for angle in np.linspace(0, 2 * np.pi, 5, endpoint=False):
            bx = cx + 0.16 * np.cos(angle)
            by = cy + 0.16 * np.sin(angle)
            ax.plot([cx, bx], [cy, by], color=INK, lw=1.8, zorder=5)

    label_offsets = {
        "Gobir": (-0.25, 0.22, 'right'),
        "Katsina": (-0.25, -0.22, 'right'),
        "Daura": (0.28, 0.22, 'left'),
        "Kano": (-0.3, 0.0, 'right'),
        "Rano": (0.3, -0.15, 'left'),
        "Biram": (0.3, 0.1, 'left'),
        "Zaria": (-0.3, -0.15, 'right')
    }

    for name, (cx, cy) in cities.items():
        draw_walled_city(cx, cy)
        ox, oy, align = label_offsets[name]
        ax.text(cx + ox, cy + oy, name, fontsize=14, weight='bold', ha=align, va='center', color=INK,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=6)

    # Trade routes heading north towards the Sahara
    # Arrow endpoints stop at y = 14.25, safely below the Sahara label and titles
    trade_arrows = [
        # From Gobir northwestwards
        ((5.2, 13.4), (4.5, 14.25)),
        # From Katsina northwards
        ((7.6, 13.25), (7.4, 14.25)),
        # From Daura / Kano northwards
        ((8.4, 13.35), (8.7, 14.25)),
        # From Kanem-Borno northwards
        ((12.4, 12.8), (12.6, 14.25))
    ]

    for (x1, y1), (x2, y2) in trade_arrows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                    color=DEEP['pink'], lw=2.5, ls="--"), zorder=3)

    # Legend / Key in bottom-left
    leg_x, leg_y = 3.2, 9.5
    ax.add_patch(Rectangle((leg_x, leg_y - 0.85), 4.0, 1.25, facecolor='white', edgecolor=GREY, lw=1.2, zorder=5))
    draw_walled_city(leg_x + 0.35, leg_y)
    ax.text(leg_x + 0.7, leg_y, "Hausa walled city (Birni)", fontsize=14, va='center', color=INK, zorder=6)
    ax.annotate("", xy=(leg_x + 0.55, leg_y - 0.45), xytext=(leg_x + 0.15, leg_y - 0.45),
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=2.2, ls="--"), zorder=6)
    ax.text(leg_x + 0.7, leg_y - 0.45, "Trade route to Sahara", fontsize=14, va='center', color=INK, zorder=6)

    # Caption
    ax.text(8.75, 8.4, "Sketch map: zones are approximate", fontsize=14, style='italic', ha='center', color=INK)

    save(fig, out)
