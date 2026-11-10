from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyBboxPatch
from matplotlib.path import Path
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 25)
    ax.set_ylim(8, 36)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Africa continent base outline if available
    try:
        africa = continent_polys('Africa')
        for poly in africa:
            ax.add_patch(Polygon(poly, facecolor='#FAF8F5', edgecolor=GREY, lw=1.2, zorder=1))
    except Exception:
        pass

    # Ecological zones (schematic shaded bands)
    # Mediterranean coast / North: > 30N
    # Sahara: ~16N to 30N
    # Sahel / Savanna: ~10N to 16N
    sahara_rect = Rectangle((-5, 16), 30, 14, facecolor='#FFF8E7', edgecolor='none', zorder=0)
    savanna_rect = Rectangle((-5, 8), 30, 8, facecolor='#EDF5EB', edgecolor='none', zorder=0)
    ax.add_patch(sahara_rect)
    ax.add_patch(savanna_rect)

    # Zone annotations (subtle)
    ax.text(-3.5, 23.5, "SAHARA DESERT", fontsize=16, fontweight='bold', color='#D2B48C', rotation=20, alpha=0.6, zorder=1)
    ax.text(-3.5, 10.5, "SAVANNA / SUDAN ZONE", fontsize=15, fontweight='bold', color='#8EA885', alpha=0.7, zorder=1)
    ax.text(19.0, 34.0, "MEDITERRANEAN SEA", fontsize=14, fontstyle='italic', color=DEEP['blue'], alpha=0.5, zorder=1)

    # Coordinates of key hubs
    nodes = {
        "Tunis": (10.2, 36.8),
        "Tripoli": (13.2, 32.9),
        "Ghadames": (9.5, 30.1),
        "Fezzan": (14.4, 25.9),      # Murzuk / Fezzan region
        "Ghat": (10.2, 24.9),
        "Bilma": (12.9, 18.7),
        "Agadez": (7.98, 17.0),
        "Kano": (8.5, 12.0),
        "Ngazargamu": (12.3, 13.0)   # Kanem-Borno capital
    }

    # Trade route paths (thick lines)
    # 1. Tripoli -> Fezzan -> Bilma -> Ngazargamu (Borno route / Central Trans-Saharan)
    # 2. Fezzan -> Agadez -> Kano
    # 3. Tunis -> Ghadames -> Ghat -> Agadez -> Kano
    # 4. Bilma -> Kano branch

    routes = [
        # Tripoli - Fezzan - Bilma - Ngazargamu
        [(13.2, 32.9), (14.4, 25.9), (12.9, 18.7), (12.3, 13.0)],
        # Fezzan - Agadez - Kano
        [(14.4, 25.9), (7.98, 17.0), (8.5, 12.0)],
        # Tunis - Ghadames - Ghat - Agadez
        [(10.2, 36.8), (9.5, 30.1), (10.2, 24.9), (7.98, 17.0)],
        # Bilma to Kano
        [(12.9, 18.7), (8.5, 12.0)]
    ]

    for r in routes:
        rx, ry = zip(*r)
        # Background outline for routes
        ax.plot(rx, ry, color='white', lw=6.5, zorder=3, solid_capstyle='round')
        # Main thick trade line
        ax.plot(rx, ry, color=DEEP['orange'], lw=3.8, zorder=4, solid_capstyle='round', linestyle='-')

    # Draw small route dashes for caravan feel
    for r in routes:
        rx, ry = zip(*r)
        ax.plot(rx, ry, color='#8B3A00', lw=1.2, linestyle=(0, (3, 4)), zorder=5)

    # Helper to draw a clean minimalist Camel icon
    def draw_camel(x, y, scale=0.35):
        # Schematic silhouette of a dromedary camel
        verts = [
            (0.0, 0.0), (0.2, 0.8), (0.3, 1.3), (0.5, 1.4), (0.8, 1.4), # head & neck
            (0.7, 0.9), (1.1, 1.2), (1.6, 1.5), (2.1, 1.1),             # hump
            (2.5, 0.9), (2.7, 0.4),                                      # hindquarters
            (2.6, -0.6), (2.3, -0.6), (2.4, 0.3),                        # back leg 1
            (1.9, 0.4), (2.0, -0.6), (1.8, -0.6), (1.6, 0.3),           # back leg 2
            (1.0, 0.3), (0.9, -0.6), (0.7, -0.6), (0.8, 0.4),           # front leg
            (0.3, 0.4), (0.2, -0.6), (0.0, -0.6), (-0.1, 0.3),          # front leg 2
            (0.0, 0.0)
        ]
        verts = [(vx * scale + x, vy * scale + y) for vx, vy in verts]
        poly = Polygon(verts, closed=True, facecolor=INK, edgecolor='none', zorder=7)
        ax.add_patch(poly)

    # Camel icons along caravan tracks
    draw_camel(14.3, 22.0, scale=0.32)
    draw_camel(9.4, 21.0, scale=0.30)
    draw_camel(11.2, 15.2, scale=0.28)

    # Helper to draw Salt Bars (desert commodities)
    def draw_salt(x, y, label="Salt"):
        for dx, dy in [(0, 0), (0.25, 0.2), (-0.2, 0.15)]:
            rect = FancyBboxPatch((x + dx - 0.4, y + dy - 0.2), 0.8, 0.35,
                                  boxstyle="round,pad=0.04", fc="#FFFFFF", ec=DEEP["blue"], lw=1.5, zorder=6)
            ax.add_patch(rect)
        ax.text(x + 0.8, y, label, fontsize=14, fontweight='bold', color=DEEP["blue"],
                va='center', zorder=8, bbox=dict(fc='white', ec='none', pad=1))

    # Draw salt near Bilma and northern desert
    draw_salt(14.6, 18.7, "Salt bars")

    # Helper to draw Gold & Kola nuts (savanna commodities)
    def draw_savanna_goods(x, y):
        # Gold nuggets / circles
        c1 = Circle((x - 0.25, y), 0.28, fc='#F5B041', ec=INK, lw=1.3, zorder=6)
        c2 = Circle((x + 0.25, y + 0.15), 0.22, fc='#FAD7A0', ec=INK, lw=1.3, zorder=6)
        # Kola nuts (brown ovals)
        c3 = FancyBboxPatch((x + 0.5, y - 0.3), 0.55, 0.35,
                            boxstyle="round,pad=0.08", fc="#795548", ec=INK, lw=1.2, zorder=6)
        ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3)
        ax.text(x + 1.4, y - 0.1, "Gold & Kola nuts", fontsize=14, fontweight='bold', color=INK,
                va='center', zorder=8, bbox=dict(fc='white', ec='none', pad=1))

    draw_savanna_goods(6.2, 9.8)

    # Draw settlement points and labels exactly as requested
    label_specs = [
        ("Tunis", (10.2, 36.8), (-1.2, 0.4), "right"),
        ("Tripoli", (13.2, 32.9), (0.6, 0.3), "left"),
        ("Fezzan", (14.4, 25.9), (0.6, 0.2), "left"),
        ("Agadez", (7.98, 17.0), (-0.6, -0.1), "right"),
        ("Bilma (Salt)", (12.9, 18.7), (-0.6, 0.4), "right"),
        ("Kano", (8.5, 12.0), (-0.6, -0.4), "right"),
        ("Kanem-Borno", (12.3, 13.0), (0.6, -0.4), "left"),
    ]

    for name, (nx, ny), (dx, dy), align in label_specs:
        # Node dot
        ax.scatter([nx], [ny], s=70, color=INK, edgecolor='white', linewidth=2, zorder=7)
        # Text label with white protective backdrop
        ax.text(nx + dx, ny + dy, name, fontsize=15, fontweight='bold', color=INK,
                ha=align, va='center', zorder=8,
                bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.9))

    # Title & Legend Box
    title_box = dict(boxstyle='square,pad=0.5', facecolor='white', edgecolor=GREY, lw=1.2)
    ax.text(10.0, 38.3, "Trans-Saharan Trade Routes", fontsize=18, fontweight='bold',
            ha='center', va='top', color=INK)

    # Legend / Explanatory card
    leg_x, leg_y = -3.8, 33.5
    leg_patch = FancyBboxPatch((leg_x, leg_y - 4.2), 6.8, 4.4, boxstyle='round,pad=0.3',
                               fc='white', ec=GREY, lw=1.2, zorder=9)
    ax.add_patch(leg_patch)
    ax.text(leg_x + 0.3, leg_y - 0.2, "Trade Legend", fontsize=15, fontweight='bold', color=INK, zorder=10)

    # Legend line
    ax.plot([leg_x + 0.4, leg_x + 1.8], [leg_y - 1.2, leg_y - 1.2], color=DEEP['orange'], lw=3.5, zorder=10)
    ax.text(leg_x + 2.1, leg_y - 1.2, "Main Caravan Route", fontsize=14, va='center', color=INK, zorder=10)

    # Legend camel
    draw_camel(leg_x + 0.7, leg_y - 2.4, scale=0.25)
    ax.text(leg_x + 2.1, leg_y - 2.2, "Camel Caravan", fontsize=14, va='center', color=INK, zorder=10)

    # Legend commodities
    rect_salt = FancyBboxPatch((leg_x + 0.4, leg_y - 3.4), 0.6, 0.25, boxstyle="round,pad=0.02",
                               fc="#FFFFFF", ec=DEEP["blue"], lw=1.3, zorder=10)
    ax.add_patch(rect_salt)
    c_gold = Circle((leg_x + 1.5, leg_y - 3.25), 0.16, fc='#F5B041', ec=INK, lw=1.0, zorder=10)
    ax.add_patch(c_gold)
    ax.text(leg_x + 2.1, leg_y - 3.3, "Regional Trade Goods", fontsize=14, va='center', color=INK, zorder=10)

    # Sketch map disclaimer caption
    ax.text(10.0, 8.4, "Sketch map: zones are approximate", fontsize=14, fontstyle='italic',
            ha='center', va='bottom', color=GREY, zorder=10)

    save(fig, out)
