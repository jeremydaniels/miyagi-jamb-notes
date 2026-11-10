from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Base map limits
    lon_min, lon_max = -26, 16
    lat_min, lat_max = 2.5, 26
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)

    # Categories
    # 1. Landlocked (light yellow / CREAM): Mali, Niger, Burkina Faso
    landlocked = ["Mali", "Niger", "Burkina Faso"]

    # 2. Coastal Francophone & Lusophone (GREEN):
    # Senegal, Guinea, Guinea-Bissau, Côte d'Ivoire, Togo, Benin, Cape Verde
    coastal_fr_pt = [
        "Senegal", "Guinea", "Guinea-Bissau", "Ivory Coast", 
        "Togo", "Benin", "Cape Verde"
    ]

    # 3. Anglophone (pale orange / ORANGE):
    # Nigeria, Ghana, Sierra Leone, Liberia, The Gambia
    anglophone = ["Nigeria", "Ghana", "Sierra Leone", "Liberia", "Gambia"]

    # Other neighbouring countries for context (GREY background)
    neighbours = [
        "Mauritania", "Algeria", "Libya", "Chad", "Cameroon"
    ]

    # Draw neighbouring countries
    for name in neighbours:
        polys = country_polys(name)
        for poly in polys:
            p = Polygon(poly, closed=True, facecolor="#F0F0F0", edgecolor="#D0D0D0", lw=0.8, zorder=1)
            ax.add_patch(p)

    # Helper to plot country group
    def plot_group(country_names, facecolor, edgecolor):
        for name in country_names:
            polys = country_polys(name)
            for poly in polys:
                p = Polygon(poly, closed=True, facecolor=facecolor, edgecolor=edgecolor, lw=1.2, zorder=2)
                ax.add_patch(p)

    plot_group(landlocked, CREAM, DEEP["orange"])
    plot_group(coastal_fr_pt, GREEN, DEEP["green"])
    plot_group(anglophone, ORANGE, DEEP["pink"])

    # Cabo Verde manual islands in case Natural Earth is sparse/small
    cv_islands = [
        [(-25.2, 17.0), (-24.9, 17.1), (-25.0, 16.8)],
        [(-24.3, 16.7), (-24.1, 16.8), (-24.2, 16.5)],
        [(-23.6, 15.1), (-23.4, 15.2), (-23.6, 14.8), (-23.8, 14.9)],
        [(-24.5, 14.9), (-24.3, 15.0), (-24.4, 14.8)]
    ]
    for isl in cv_islands:
        ax.add_patch(Polygon(isl, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2, zorder=3))

    # Country Labels
    labels = [
        ("Mali", (-3.5, 17.5)),
        ("Niger", (8.5, 17.5)),
        ("Burkina Faso", (-1.5, 12.3)),
        ("Senegal", (-14.3, 14.6)),
        ("The Gambia", (-15.3, 13.4)),
        ("Guinea-Bissau", (-15.1, 11.9)),
        ("Guinea", (-11.0, 10.5)),
        ("Sierra Leone", (-11.8, 8.5)),
        ("Liberia", (-9.3, 6.4)),
        ("Côte d'Ivoire", (-5.5, 7.5)),
        ("Ghana", (-1.2, 8.0)),
        ("Togo", (1.1, 8.6)),
        ("Benin", (2.3, 9.6)),
        ("Nigeria", (8.0, 9.5)),
        ("Cape Verde", (-24.0, 17.8))
    ]

    for text, pos in labels:
        if text == "The Gambia":
            ax.annotate(text, xy=(-15.3, 13.45), xytext=(-18.5, 13.45),
                        fontsize=14, fontweight="bold", color=INK,
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
                        ha="right", va="center",
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
        elif text == "Guinea-Bissau":
            ax.annotate(text, xy=(-15.0, 11.9), xytext=(-17.5, 11.5),
                        fontsize=14, fontweight="bold", color=INK,
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
                        ha="right", va="center",
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
        elif text == "Togo":
            ax.annotate(text, xy=(1.1, 8.2), xytext=(1.1, 5.5),
                        fontsize=14, fontweight="bold", color=INK,
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
                        ha="center", va="top",
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
        elif text == "Benin":
            ax.annotate(text, xy=(2.3, 9.0), xytext=(3.5, 6.2),
                        fontsize=14, fontweight="bold", color=INK,
                        arrowprops=dict(arrowstyle="->", color=INK, lw=1.0),
                        ha="left", va="top",
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
        else:
            ax.text(pos[0], pos[1], text, fontsize=14, fontweight="bold", color=INK,
                    ha="center", va="center", zorder=5,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.75))

    # Water labels
    ax.text(-5, 4.0, "Atlantic Ocean / Gulf of Guinea", fontsize=15, fontstyle="italic", color=DEEP["blue"], ha="center")

    # Title
    ax.text(-5, 24.5, "ECOWAS Member States (15 Countries)", fontsize=18, fontweight="bold", color=INK, ha="center")

    # Legend
    legend_items = [
        (CREAM, DEEP["orange"], "Landlocked states (3)"),
        (GREEN, DEEP["green"], "Coastal Francophone & Lusophone states (7)"),
        (ORANGE, DEEP["pink"], "Anglophone states (5)")
    ]
    leg_x, leg_y = -25.5, 7.5
    ax.text(leg_x, leg_y + 1.2, "Grouping:", fontsize=15, fontweight="bold", color=INK)
    for i, (fc, ec, label) in enumerate(legend_items):
        y = leg_y - i * 1.0
        rect = Rectangle((leg_x, y - 0.3), 1.5, 0.6, facecolor=fc, edgecolor=ec, lw=1.2)
        ax.add_patch(rect)
        ax.text(leg_x + 1.9, y, label, fontsize=14, color=INK, va="center")

    # Compass Rose
    cx, cy = -23.0, 22.5
    ax.annotate("", xy=(cx, cy + 1.4), xytext=(cx, cy - 1.0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2, mutation_scale=15))
    ax.plot([cx - 1.0, cx + 1.0], [cy, cy], color=INK, lw=1.5)
    ax.text(cx, cy + 1.6, "N", fontsize=15, fontweight="bold", ha="center", va="bottom", color=INK)
    ax.text(cx + 1.2, cy, "E", fontsize=14, ha="left", va="center", color=INK)
    ax.text(cx, cy - 1.2, "S", fontsize=14, ha="center", va="top", color=INK)
    ax.text(cx - 1.2, cy, "W", fontsize=14, ha="right", va="center", color=INK)

    # Scale Bar placed in clear ocean space south of Ghana/Liberia (lon -12 to -7, lat 3.5)
    # to avoid overlapping southern Nigeria (Nigeria goes down to ~4.3°N, lon 3°E to 14°E)
    sx, sy = -12.0, 3.4
    bar_len = 4.6
    ax.plot([sx, sx + bar_len], [sy, sy], color=INK, lw=3, zorder=6)
    ax.plot([sx, sx], [sy - 0.25, sy + 0.25], color=INK, lw=2, zorder=6)
    ax.plot([sx + bar_len, sx + bar_len], [sy - 0.25, sy + 0.25], color=INK, lw=2, zorder=6)
    ax.plot([sx + bar_len / 2, sx + bar_len / 2], [sy - 0.15, sy + 0.15], color=INK, lw=1.5, zorder=6)
    ax.text(sx, sy + 0.45, "0", fontsize=14, ha="center", color=INK, zorder=6)
    ax.text(sx + bar_len / 2, sy + 0.45, "250", fontsize=14, ha="center", color=INK, zorder=6)
    ax.text(sx + bar_len, sy + 0.45, "500 km", fontsize=14, ha="center", color=INK, zorder=6)

    # Caption
    ax.text(15.5, 2.8, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic", color=GREY, ha="right")

    save(fig, out)
