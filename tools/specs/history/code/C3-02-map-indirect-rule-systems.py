from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(13, 10.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(1.5, 15.5)
    ax.set_ylim(2.5, 14.8)

    # Simplified representation of Nigeria outline circa 1920
    # Outer coordinates (approximate boundary of colonial Nigeria)
    poly_north = [
        (3.6, 11.7), (4.5, 12.0), (5.2, 13.8), (7.0, 13.0), (8.5, 13.0),
        (10.0, 13.5), (12.0, 13.5), (13.5, 13.7), (14.2, 12.8), (14.6, 12.2),
        (13.5, 11.0), (12.5, 10.0), (11.5, 8.8), (10.0, 7.8), (9.0, 7.8),
        (6.7, 7.8), (5.5, 9.0), (4.0, 9.0), (3.6, 10.5), (3.6, 11.7)
    ]

    poly_west = [
        (2.7, 6.4), (3.6, 9.0), (4.0, 9.0), (5.5, 9.0), (6.7, 7.8),
        (6.7, 5.8), (5.5, 6.0), (4.5, 6.2), (3.5, 6.4), (2.7, 6.4)
    ]

    poly_east = [
        (6.7, 5.8), (6.7, 7.8), (9.0, 7.8), (10.0, 7.8), (9.8, 6.6),
        (9.2, 5.5), (8.5, 5.0), (7.5, 5.0), (6.7, 5.8)
    ]

    # Draw shaded regions: North = green, West = yellow, East = red (pink/red tone)
    p_n = Polygon(poly_north, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], linewidth=2.5)
    p_w = Polygon(poly_west, closed=True, facecolor="#FFF3CD", edgecolor="#D39E00", linewidth=2.5)
    p_e = Polygon(poly_east, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], linewidth=2.5)

    ax.add_patch(p_n)
    ax.add_patch(p_w)
    ax.add_patch(p_e)

    # Rivers (Niger & Benue confluence roughly schematic)
    niger_river = np.array([(3.8, 11.7), (4.8, 9.8), (6.0, 8.8), (6.7, 7.8), (6.7, 5.8), (6.0, 4.8)])
    benue_river = np.array([(12.0, 9.3), (10.5, 8.5), (8.5, 7.9), (6.7, 7.8)])
    ax.plot(niger_river[:, 0], niger_river[:, 1], color=DEEP["blue"], lw=2, ls="--", alpha=0.6)
    ax.plot(benue_river[:, 0], benue_river[:, 1], color=DEEP["blue"], lw=2, ls="--", alpha=0.6)

    # Title
    ax.text(8.5, 14.3, "Nigeria: Regional Administrative Systems under Indirect Rule (c. 1920)",
            fontsize=17, fontweight="bold", ha="center", color=INK)

    # Northern Region annotation
    label_north = (
        "NORTHERN REGION\n"
        "Highly Centralized Emirates:\n"
        "Indirect Rule Highly Successful\n"
        "(Emirs)"
    )
    ax.text(9.0, 10.8, label_north, fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.5", lw=1.5))

    # Western Region callout / label
    label_west = (
        "WESTERN REGION\n"
        "Constitutional Monarchies:\n"
        "Indirect Rule Partially Successful\n"
        "(Obas made Sole Authorities)"
    )
    ax.annotate(
        label_west,
        xy=(4.7, 7.2),
        xytext=(3.5, 7.2),
        fontsize=14,
        ha="right",
        va="center",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec="#D39E00", boxstyle="round,pad=0.5", lw=1.5)
    )

    # Eastern Region callout / label
    label_east = (
        "EASTERN REGION\n"
        "Non-centralized Societies:\n"
        "Indirect Rule Failed\n"
        "(Artificial Warrant Chiefs)"
    )
    ax.annotate(
        label_east,
        xy=(8.2, 6.4),
        xytext=(11.5, 6.0),
        fontsize=14,
        ha="left",
        va="center",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.5", lw=1.5)
    )

    # Water label clearly positioned below the landmass with plenty of clearance
    ax.text(5.5, 3.8, "Gulf of Guinea / Atlantic Ocean", fontsize=15, style="italic", color=DEEP["blue"], ha="center")

    # Schematic note
    ax.text(8.5, 3.0, "Sketch map: zones are approximate", fontsize=14, ha="center", color=GREY, style="italic")

    save(fig, out)
