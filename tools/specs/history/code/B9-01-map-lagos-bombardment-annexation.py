from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background ocean (Bight of Benin)
    ocean = Rectangle((0, 0), 12, 8, facecolor=BLUE, alpha=0.35, zorder=0)
    ax.add_patch(ocean)

    # Mainland coordinates (North of lagoons and creeks)
    mainland_pts = [
        [0, 8],
        [12, 8],
        [12, 3.8],
        [10.5, 3.9],
        [9.5, 4.2],
        [8.5, 4.8],  # Epe area north shore
        [7.0, 4.3],
        [5.8, 4.5],  # North shore of Lagos Lagoon
        [4.8, 4.4],
        [3.5, 3.6],  # North of Badagry creek
        [1.5, 3.5],
        [0, 3.5]
    ]
    ax.add_patch(Polygon(mainland_pts, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1))

    # Barrier sandspits enclosing the lagoons
    # West spit (Badagry strip to Lagos harbour entrance)
    west_spit = [
        [0, 2.5],
        [4.8, 2.5],
        [4.8, 2.9],
        [0, 2.9]
    ]
    ax.add_patch(Polygon(west_spit, facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=2))

    # East spit (Lekki strip eastward)
    east_spit = [
        [5.5, 2.5],
        [12, 2.5],
        [12, 2.9],
        [5.5, 2.9]
    ]
    ax.add_patch(Polygon(east_spit, facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=2))

    # Lagos Island
    lagos_island = [
        [4.9, 3.1],
        [5.4, 3.1],
        [5.45, 3.5],
        [5.0, 3.6]
    ]
    ax.add_patch(Polygon(lagos_island, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.0, zorder=3))

    # Water labels
    ax.text(6.1, 5.2, "Lagos Lagoon", fontsize=16, color=DEEP["blue"], style="italic", ha="center", va="center")
    ax.text(2.5, 3.15, "Badagry Creek", fontsize=14, color=DEEP["blue"], style="italic", ha="center", va="center")
    ax.text(6.0, 0.9, "BIGHT OF BENIN\n(Gulf of Guinea)", fontsize=18, color=DEEP["blue"], ha="center", va="center", weight="bold")

    # Mainland label
    ax.text(2.0, 6.5, "YORUBALAND / MAINLAND", fontsize=15, color=INK, alpha=0.6, weight="bold")

    # Towns / Locations
    # Badagry
    ax.plot(1.8, 3.6, marker='o', markersize=7, color=INK, zorder=5)
    ax.text(1.8, 3.9, "Badagry", fontsize=15, fontweight="bold", color=INK, ha="center", bbox=dict(fc="white", ec="none", pad=1.5))

    # Epe
    ax.plot(8.8, 4.6, marker='o', markersize=7, color=INK, zorder=5)
    ax.text(8.8, 5.0, "Epe", fontsize=15, fontweight="bold", color=INK, ha="center", bbox=dict(fc="white", ec="none", pad=1.5))

    # Lagos Island label
    ax.text(5.2, 3.9, "Lagos Island", fontsize=14, fontweight="bold", color=INK, ha="center", bbox=dict(fc="white", ec="none", pad=1))

    # Historical Events Annotations: Two distinct points marked exactly as required
    # Point 1: 1851: Bombardment (Kosoko ousted)
    ax.annotate(
        "1851: Bombardment (Kosoko ousted)",
        xy=(5.0, 3.35),
        xytext=(2.6, 5.4),
        fontsize=14,
        fontweight="bold",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.2),
        ha="center",
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.4", lw=1.5),
        zorder=6
    )

    # Point 2: 1861: Annexation (Dosunmu cedes Lagos)
    ax.annotate(
        "1861: Annexation (Dosunmu cedes Lagos)",
        xy=(5.4, 3.3),
        xytext=(8.2, 2.2),
        fontsize=14,
        fontweight="bold",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2),
        ha="center",
        bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.4", lw=1.5),
        zorder=6
    )

    # Helper function to draw a stylized 19th-century British naval ship
    def draw_ship(x, y, scale=0.8):
        hull_pts = [
            [x - 0.45 * scale, y],
            [x + 0.45 * scale, y],
            [x + 0.35 * scale, y - 0.15 * scale],
            [x - 0.35 * scale, y - 0.15 * scale]
        ]
        ax.add_patch(Polygon(hull_pts, facecolor=INK, edgecolor=INK, zorder=4))
        # Masts
        ax.plot([x - 0.2 * scale, x - 0.2 * scale], [y, y + 0.4 * scale], color=INK, lw=1.5, zorder=4)
        ax.plot([x + 0.1 * scale, x + 0.1 * scale], [y, y + 0.45 * scale], color=INK, lw=1.5, zorder=4)
        # Sails
        ax.add_patch(Rectangle((x - 0.28 * scale, y + 0.12 * scale), 0.16 * scale, 0.22 * scale, facecolor="white", edgecolor=INK, lw=1, zorder=4))
        ax.add_patch(Rectangle((x + 0.02 * scale, y + 0.15 * scale), 0.16 * scale, 0.24 * scale, facecolor="white", edgecolor=INK, lw=1, zorder=4))

    # Offshore British naval ships
    draw_ship(4.3, 1.8, 0.85)
    draw_ship(5.1, 1.9, 0.95)
    draw_ship(3.7, 1.5, 0.70)
    ax.text(4.4, 1.25, "British naval ships", fontsize=14, color=INK, ha="center", style="italic", bbox=dict(fc="white", ec="none", pad=1.5))

    # Title & map caption
    ax.text(6.0, 7.5, "19th-Century Lagos & The Bight of Benin", fontsize=18, fontweight="bold", color=INK, ha="center")
    ax.text(0.3, 0.3, "Sketch map: zones are approximate", fontsize=14, color=GREY, style="italic")

    # North arrow
    nx, ny = 11.0, 6.8
    ax.annotate("N", xy=(nx, ny + 0.4), fontsize=15, fontweight="bold", ha="center", va="center", color=INK)
    ax.arrow(nx, ny - 0.3, 0, 0.5, head_width=0.25, head_length=0.25, fc=INK, ec=INK, lw=1.5)

    save(fig, out)
