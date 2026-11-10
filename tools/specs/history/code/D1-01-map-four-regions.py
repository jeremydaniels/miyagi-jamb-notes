from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(11, 9)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Coordinates roughly defining the 1964 regions of Nigeria
    # Northern Region (spanning the vast majority of the north and middle belt)
    poly_north = [
        (3.5, 11.5), (4.0, 13.0), (5.5, 13.8), (8.0, 13.0), (10.0, 13.5), 
        (13.0, 13.8), (14.2, 12.5), (14.5, 11.0), (12.5, 9.5), (11.5, 7.0),
        (10.0, 6.8), (9.0, 7.5), (7.0, 7.8), (6.7, 7.8), (5.8, 7.7),
        (5.0, 9.0), (3.6, 9.0), (2.7, 10.0), (3.5, 11.5)
    ]

    # Western Region (Southwest, excluding Lagos and Mid-West)
    poly_west = [
        (2.7, 10.0), (3.6, 9.0), (5.0, 9.0), (5.5, 7.7), (5.0, 7.0),
        (4.8, 6.0), (4.5, 6.2), (3.0, 6.3), (2.7, 6.5), (2.7, 10.0)
    ]

    # Mid-Western Region (created 1963, carved out of Western Region)
    poly_midwest = [
        (5.5, 7.7), (6.7, 7.8), (6.7, 5.3), (5.2, 5.3), (4.8, 6.0),
        (5.0, 7.0), (5.5, 7.7)
    ]

    # Eastern Region (Southeast, bounded by Niger River to the west)
    poly_east = [
        (6.7, 7.8), (7.0, 7.8), (9.0, 7.5), (10.0, 6.8), (9.5, 5.0),
        (8.5, 4.5), (6.7, 4.5), (6.7, 5.3), (6.7, 7.8)
    ]

    # Draw regions with contrasting pastel colours
    patch_n = Polygon(poly_north, closed=True, facecolor=CREAM, edgecolor=GREY, lw=2, zorder=2)
    patch_w = Polygon(poly_west, closed=True, facecolor=BLUE, edgecolor=GREY, lw=2, zorder=2)
    patch_mw = Polygon(poly_midwest, closed=True, facecolor=ORANGE, edgecolor=GREY, lw=2, zorder=2)
    patch_e = Polygon(poly_east, closed=True, facecolor=GREEN, edgecolor=GREY, lw=2, zorder=2)

    ax.add_patch(patch_n)
    ax.add_patch(patch_w)
    ax.add_patch(patch_mw)
    ax.add_patch(patch_e)

    # Rivers (Niger & Benue meeting at Lokoja)
    rn_x = [3.6, 4.5, 5.5, 6.7, 6.7, 6.2]
    rn_y = [11.0, 9.5, 8.5, 7.8, 5.3, 4.5]
    ax.plot(rn_x, rn_y, color=DEEP["blue"], lw=2.5, alpha=0.6, zorder=3)

    rb_x = [6.7, 8.0, 9.5, 11.5, 12.5]
    rb_y = [7.8, 8.0, 8.8, 9.2, 9.5]
    ax.plot(rb_x, rb_y, color=DEEP["blue"], lw=2.5, alpha=0.6, zorder=3)

    # River annotations
    ax.text(4.3, 9.8, "R. Niger", fontsize=14, color=DEEP["blue"], style='italic', rotation=-55)
    ax.text(9.2, 8.9, "R. Benue", fontsize=14, color=DEEP["blue"], style='italic', rotation=20)

    # Major Cities
    cities = [
        ("Kaduna", 7.4, 10.5, (12, 5)),
        ("Ibadan", 3.9, 7.4, (-15, -18)),
        ("Lagos", 3.4, 6.4, (-15, -18)),
        ("Benin City", 5.6, 6.3, (-55, -22)),
        ("Enugu", 7.5, 6.4, (12, 10))
    ]

    for name, cx, cy, (ox, oy) in cities:
        ax.scatter(cx, cy, s=55, color=INK, zorder=5)
        ax.annotate(
            name, xy=(cx, cy), xytext=(ox, oy), textcoords="offset points",
            fontsize=14, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
            zorder=6
        )

    # Region Labels - positioned carefully so no overlaps occur
    bbox_n = dict(fc="white", ec="none", pad=0.3, alpha=0.85)
    ax.text(8.5, 11.5, "Northern Region", fontsize=17, fontweight="bold", color=INK, ha="center", bbox=bbox_n, zorder=4)

    # Western Region label
    ax.text(3.7, 8.4, "Western Region", fontsize=14, fontweight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9), zorder=7)

    # Mid-Western Region (created 1963)
    ax.annotate(
        "Mid-Western Region\n(created 1963)",
        xy=(5.9, 6.0), xytext=(3.5, 4.5),
        fontsize=14, fontweight="bold", color=INK, ha="center",
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.95),
        zorder=7
    )

    # Eastern Region label: securely inside the green region
    ax.text(8.2, 6.0, "Eastern Region", fontsize=14, fontweight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9), zorder=7)

    # Title & Caption
    ax.text(8.5, 14.5, "Federal Republic of Nigeria (1964)", fontsize=18, fontweight="bold", color=INK, ha="center")
    ax.text(8.5, 3.6, "Sketch map: zones are approximate", fontsize=14, style='italic', color=GREY, ha="center")

    ax.set_xlim(1.5, 15.5)
    ax.set_ylim(3.2, 15.0)

    save(fig, out)
