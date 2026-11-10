from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-18, 16)
    ax.set_ylim(3.5, 25)

    # Base map of Africa / West African region
    try:
        africa_polys = continent_polys("Africa")
        for p in africa_polys:
            poly_patch = patches.Polygon(p, closed=True, facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=1)
            ax.add_patch(poly_patch)
    except Exception:
        pass

    # Regional highlight for West Africa / Sahel zone (schematic polygon)
    sahel_coords = [(-16, 12), (-10, 10.5), (0, 11), (10, 10), (15, 11), (15, 17), (5, 19), (-5, 20), (-16, 17)]
    sahel_poly = patches.Polygon(sahel_coords, closed=True, facecolor=ORANGE, alpha=0.15, zorder=2)
    ax.add_patch(sahel_poly)

    # Country boundaries
    try:
        countries = country_polys("Mali", "Nigeria", "Niger", "Senegal", "Ghana")
        for p in countries:
            ax.add_patch(patches.Polygon(p, closed=True, facecolor="none", edgecolor=GREY, lw=0.8, ls=":", zorder=3))
    except Exception:
        pass

    # Title & Caption
    ax.text(-1, 23.8, "Islamic Scholarship & Heritage in West Africa", 
            fontsize=18, fontweight="bold", color=INK, ha="center")
    ax.text(-17, 4.2, "Sketch map: zones and architectural representations are approximate", 
            fontsize=14, color=GREY, style="italic")

    # Schematic Sankore Mosque drawing at Timbuktu coordinates (~ -3.0, 16.7)
    timbuktu_x, timbuktu_y = -3.0, 16.7
    
    # Draw Mosque Pyramid/Tower
    tower_pts = [
        (timbuktu_x - 1.2, timbuktu_y),
        (timbuktu_x - 0.4, timbuktu_y + 3.2),
        (timbuktu_x + 0.4, timbuktu_y + 3.2),
        (timbuktu_x + 1.2, timbuktu_y)
    ]
    tower = patches.Polygon(tower_pts, closed=True, facecolor="#D9A066", edgecolor=INK, lw=1.8, zorder=5)
    ax.add_patch(tower)

    # Base complex of Mosque
    base_pts = [
        (timbuktu_x - 2.2, timbuktu_y - 0.8),
        (timbuktu_x - 2.0, timbuktu_y + 0.3),
        (timbuktu_x + 2.0, timbuktu_y + 0.3),
        (timbuktu_x + 2.2, timbuktu_y - 0.8)
    ]
    base = patches.Polygon(base_pts, closed=True, facecolor="#C68953", edgecolor=INK, lw=1.8, zorder=4)
    ax.add_patch(base)

    # Iconic projecting timber beams (toron) on Sankore Mosque
    beam_color = INK
    beam_rows = [0.8, 1.4, 2.0, 2.6]
    for dy in beam_rows:
        y_beam = timbuktu_y + dy
        hw = 0.4 + (3.2 - dy) * 0.25
        for bx in np.linspace(timbuktu_x - hw, timbuktu_x + hw, 5):
            ax.plot([bx - 0.15, bx + 0.15], [y_beam, y_beam], color=beam_color, lw=1.8, zorder=6)

    # Top pinnacle / finial
    ax.plot([timbuktu_x, timbuktu_x], [timbuktu_y + 3.2, timbuktu_y + 3.6], color=INK, lw=2, zorder=6)
    ax.scatter([timbuktu_x], [timbuktu_y + 3.7], color=DEEP["orange"], s=40, zorder=7)

    # Label for Timbuktu / Sankore
    ax.text(timbuktu_x, timbuktu_y + 4.2, "Timbuktu\n(Sankore Mosque)", 
            fontsize=15, fontweight="bold", color=INK, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["orange"], lw=1.5, zorder=10))

    # Cities: Sokoto (~ 5.2, 13.0) and Kano (~ 8.5, 12.0)
    sokoto_x, sokoto_y = 5.2, 13.0
    kano_x, kano_y = 8.5, 12.0

    # Draw city points
    ax.scatter([sokoto_x], [sokoto_y], color=DEEP["green"], s=100, zorder=8, edgecolors=INK, lw=1.5)
    ax.scatter([kano_x], [kano_y], color=DEEP["blue"], s=100, zorder=8, edgecolors=INK, lw=1.5)

    # Annotations / Icons
    # Sokoto: Usman Danfodio (placed higher/northeast of Gulf to avoid water text)
    ax.annotate(
        "Sokoto\n• Usman Danfodio\n  (Sokoto Caliphate)",
        xy=(sokoto_x, sokoto_y),
        xytext=(sokoto_x - 3.2, sokoto_y - 2.8),
        fontsize=14,
        fontweight="bold",
        color=INK,
        ha="center",
        va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["green"], lw=1.5, zorder=10),
        arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.2, shrinkA=3, shrinkB=6)
    )

    # Kano: Al-Maghili (placed to the right/east)
    ax.annotate(
        "Kano\n• Muhammad Al-Maghili\n  (Scholar & Reformer)",
        xy=(kano_x, kano_y),
        xytext=(kano_x + 3.6, kano_y - 2.2),
        fontsize=14,
        fontweight="bold",
        color=INK,
        ha="center",
        va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["blue"], lw=1.5, zorder=10),
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.2, shrinkA=3, shrinkB=6)
    )

    # Geographic reference labels
    ax.text(-12, 14, "WEST AFRICA", fontsize=16, color=GREY, fontweight="bold", alpha=0.6, rotation=15)
    # Placed safely in the open Atlantic/Gulf of Guinea below latitude 5.5, clear of callouts
    ax.text(-7.0, 5.0, "Atlantic Ocean / Gulf of Guinea", fontsize=14, color=DEEP["blue"], style="italic", ha="center")

    save(fig, out)
