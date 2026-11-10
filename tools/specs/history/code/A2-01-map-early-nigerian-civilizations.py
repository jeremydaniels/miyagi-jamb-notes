from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)

    # Base styling
    ax.set_xlim(2.0, 15.0)
    ax.set_ylim(3.6, 14.6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw Nigeria polygon
    # nigeria_poly() returns a polygon (or list/structure of coordinates)
    polys = nigeria_poly()
    if not isinstance(polys, (list, tuple)):
        polys = [polys]

    for poly in polys:
        arr = np.asarray(poly)
        if arr.ndim == 1:
            arr = arr.reshape(-1, 2)
        ax.fill(arr[:, 0], arr[:, 1], color=CREAM, ec=DEEP["blue"], lw=2.0, zorder=1)

    # Simplified schematic courses of the Niger and Benue rivers
    # Niger: enters NW ~ (3.6, 11.7), flows SE to Lokoja confluence ~(6.7, 7.8), then south to delta ~(6.1, 4.3)
    niger_x = [3.6, 4.4, 5.2, 6.0, 6.7, 6.7, 6.4, 6.1]
    niger_y = [11.7, 10.2, 9.0, 8.4, 7.8, 7.0, 5.5, 4.3]
    ax.plot(niger_x, niger_y, color=DEEP["blue"], lw=2.4, alpha=0.7, zorder=2, ls='-')
    ax.text(4.2, 9.9, "River Niger", fontsize=14, color=DEEP["blue"], style='italic', rotation=-52,
            bbox=dict(fc='white', ec='none', pad=1, alpha=0.8), zorder=3)

    # Benue: enters E ~ (12.0, 9.3) flows SW to confluence ~(6.7, 7.8)
    benue_x = [12.0, 10.5, 9.2, 7.8, 6.7]
    benue_y = [9.3, 8.9, 8.5, 8.0, 7.8]
    ax.plot(benue_x, benue_y, color=DEEP["blue"], lw=2.4, alpha=0.7, zorder=2, ls='-')
    ax.text(9.1, 8.8, "River Benue", fontsize=14, color=DEEP["blue"], style='italic', rotation=-14,
            bbox=dict(fc='white', ec='none', pad=1, alpha=0.8), zorder=3)

    # Early centres of civilization
    # Coordinates:
    # Daima: ~ (14.2, 12.2) (far north-east, south of Lake Chad)
    # Nok: ~ (8.0, 9.5) (central, north of Niger-Benue confluence)
    # Iwo Eleru: ~ (5.3, 7.3) (south-west, near Akure)
    # Ife: ~ (4.55, 7.5) (south-west)
    # Benin: ~ (5.6, 6.3) (mid-west)
    # Igbo-Ukwu: ~ (7.0, 6.0) (south-east, near Awka)
    sites = [
        {"name": "Daima", "xy": (14.2, 12.2), "text_xy": (12.1, 13.0)},
        {"name": "Nok", "xy": (8.0, 9.5), "text_xy": (8.6, 10.4)},
        {"name": "Ife", "xy": (4.55, 7.5), "text_xy": (3.0, 8.1)},
        {"name": "Iwo Eleru", "xy": (5.3, 7.3), "text_xy": (3.2, 6.7)},
        {"name": "Benin", "xy": (5.6, 6.3), "text_xy": (3.5, 5.7)},
        {"name": "Igbo-Ukwu", "xy": (7.0, 6.0), "text_xy": (8.3, 5.5)},
    ]

    for site in sites:
        sx, sy = site["xy"]
        tx, ty = site["text_xy"]
        ax.plot(sx, sy, marker='o', markersize=9, color=DEEP["orange"],
                markeredgecolor=INK, markeredgewidth=1.8, zorder=4)
        ax.annotate(site["name"], xy=(sx, sy), xytext=(tx, ty),
                    fontsize=15, fontweight='bold', color=INK, zorder=5,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', lw=1.0))

    # Title and sketch caption
    ax.text(8.5, 14.1, "Early Centres of Civilization in Nigeria",
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    ax.text(8.5, 3.8, "Sketch map: zones are approximate",
            ha='center', va='center', fontsize=14, fontstyle='italic', color=GREY)

    save(fig, out)
