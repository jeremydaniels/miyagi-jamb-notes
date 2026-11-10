from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    # Canvas sized cleanly to accommodate the map and distinct legend panels
    fig = canvas(14, 10.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Define approximate polygons for the 12 states of Nigeria created in May 1967
    # Longitude approx 2.7 to 14.2, Latitude approx 4.2 to 13.9
    states = {
        # Northern Region (6 States)
        "North-Western": {
            "coords": [
                (3.5, 11.5), (3.6, 11.8), (4.0, 12.5), (4.8, 13.8), (5.5, 13.9),
                (7.0, 13.3), (7.0, 11.5), (6.5, 10.5), (5.8, 9.8), (5.0, 9.0),
                (4.5, 9.8), (3.7, 10.2), (3.5, 11.5)
            ],
            "color": GREEN,
            "label_pos": (5.2, 11.8),
            "label": "North-Western"
        },
        "North-Central": {
            "coords": [
                (7.0, 13.3), (8.2, 13.1), (8.0, 11.8), (8.8, 10.8), (8.6, 9.2),
                (7.0, 9.0), (6.5, 10.5), (7.0, 11.5), (7.0, 13.3)
            ],
            "color": LAV,
            "label_pos": (7.6, 11.0),
            "label": "North-Central"
        },
        "Kano": {
            "coords": [
                (8.2, 13.1), (10.0, 13.0), (10.2, 11.8), (9.5, 11.0),
                (8.8, 10.8), (8.0, 11.8), (8.2, 13.1)
            ],
            "color": ORANGE,
            "label_pos": (9.1, 12.1),
            "label": "Kano"
        },
        "North-Eastern": {
            "coords": [
                (10.0, 13.0), (13.5, 13.8), (14.2, 12.5), (13.5, 10.8),
                (12.0, 9.0), (11.8, 7.0), (11.0, 6.8), (9.8, 8.0),
                (9.5, 9.5), (9.5, 11.0), (10.2, 11.8), (10.0, 13.0)
            ],
            "color": BLUE,
            "label_pos": (11.7, 11.1),
            "label": "North-Eastern"
        },
        "Benue-Plateau": {
            "coords": [
                (8.6, 9.2), (8.8, 10.8), (9.5, 11.0), (9.5, 9.5), (9.8, 8.0),
                (11.0, 6.8), (10.0, 6.6), (8.5, 7.0), (7.2, 7.6), (7.5, 8.5),
                (8.6, 9.2)
            ],
            "color": CREAM,
            "label_pos": (8.8, 8.3),
            "label": "Benue-Plateau"
        },
        "Kwara": {
            "coords": [
                (3.5, 10.2), (4.5, 9.8), (5.0, 9.0), (5.8, 9.8), (7.0, 9.0),
                (7.5, 8.5), (7.2, 7.6), (6.0, 7.8), (5.2, 8.2), (4.2, 8.5),
                (3.2, 8.8), (3.0, 9.5), (3.5, 10.2)
            ],
            "color": PINK,
            "label_pos": (4.9, 9.0),
            "label": "Kwara"
        },
        # Southern Region (6 States)
        "Western": {
            "coords": [
                (2.8, 7.5), (3.2, 8.8), (4.2, 8.5), (5.2, 8.2), (6.0, 7.8),
                (5.8, 6.8), (5.2, 6.0), (4.5, 6.2), (3.8, 6.5), (2.8, 6.6),
                (2.8, 7.5)
            ],
            "color": BLUE,
            "label_pos": (4.1, 7.3),
            "label": "Western"
        },
        "Lagos": {
            "coords": [
                (2.8, 6.6), (3.8, 6.5), (4.2, 6.3), (4.2, 6.0), (2.8, 6.1),
                (2.8, 6.6)
            ],
            "color": GREEN,
            "label_pos": (3.5, 6.2),
            "label": "Lagos"
        },
        "Mid-Western": {
            "coords": [
                (5.2, 6.0), (5.8, 6.8), (6.0, 7.8), (6.8, 7.4), (6.7, 6.2),
                (6.2, 5.2), (5.2, 5.5), (5.2, 6.0)
            ],
            "color": LAV,
            "label_pos": (5.9, 6.4),
            "label": "Mid-Western"
        },
        "East-Central": {
            "coords": [
                (6.8, 7.4), (7.2, 7.6), (8.0, 7.0), (8.0, 5.8), (7.2, 5.4),
                (6.7, 5.8), (6.7, 6.2), (6.8, 7.4)
            ],
            "color": ORANGE,
            "label_pos": (7.4, 6.5),
            "label": "East-Central"
        },
        "South-Eastern": {
            "coords": [
                (8.0, 7.0), (8.5, 7.0), (10.0, 6.6), (9.4, 5.2), (8.5, 4.8),
                (8.2, 5.2), (8.0, 5.8), (8.0, 7.0)
            ],
            "color": CREAM,
            "label_pos": (8.8, 5.8),
            "label": "South-Eastern"
        },
        "Rivers": {
            "coords": [
                (6.2, 5.2), (6.7, 6.2), (6.7, 5.8), (7.2, 5.4), (8.0, 5.8),
                (8.2, 5.2), (8.5, 4.8), (7.5, 4.2), (6.5, 4.3), (6.2, 5.2)
            ],
            "color": PINK,
            "label_pos": (7.1, 4.9),
            "label": "Rivers"
        }
    }

    # Draw state polygons
    for name, data in states.items():
        poly = Polygon(
            data["coords"], closed=True,
            facecolor=data["color"], edgecolor=INK,
            linewidth=1.8, zorder=2
        )
        ax.add_patch(poly)

    # State Labels inside/around map
    for name, data in states.items():
        x, y = data["label_pos"]
        if name == "Lagos":
            # Lagos is small coastal strip; label placed outside with arrow pointer
            ax.annotate(
                "Lagos", xy=(3.5, 6.3), xytext=(2.6, 5.3),
                fontsize=14, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=GREY, alpha=0.95),
                zorder=5, ha="center"
            )
        else:
            label_text = data["label"].replace("-", "-\n")
            ax.text(
                x, y, label_text, fontsize=14, fontweight="bold", color=INK,
                ha="center", va="center", zorder=4,
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="none", alpha=0.88)
            )

    # Surrounding geographic context
    ax.text(3.8, 4.2, "Gulf of Guinea", fontsize=15, fontstyle="italic", color=DEEP["blue"], zorder=3,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.7))
    ax.text(13.0, 12.7, "Lake\nChad", fontsize=14, fontstyle="italic", color=DEEP["blue"], ha="center", zorder=3)

    # Header Titles
    ax.text(8.0, 14.8, "Nigeria: The 12 States Created in 1967", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)
    ax.text(8.0, 14.25, "Reorganization of the Federation under General Yakubu Gowon (May 1967)",
            fontsize=14, fontstyle="italic", ha="center", va="center", color=INK)

    # Side panels for regions
    north_text = (
        "Northern Region (6 States)\n"
        " • North-Western\n"
        " • North-Central\n"
        " • Kano\n"
        " • North-Eastern\n"
        " • Benue-Plateau\n"
        " • Kwara"
    )
    south_text = (
        "Southern Region (6 States)\n"
        " • Western\n"
        " • Lagos\n"
        " • Mid-Western\n"
        " • East-Central\n"
        " • South-Eastern\n"
        " • Rivers"
    )

    ax.text(-1.8, 13.5, north_text, fontsize=14, va="top", ha="left", color=INK, linespacing=1.45,
            bbox=dict(boxstyle="round,pad=0.55", facecolor=CREAM, edgecolor=GREY, alpha=0.95),
            zorder=6)
    ax.text(-1.8, 9.7, south_text, fontsize=14, va="top", ha="left", color=INK, linespacing=1.45,
            bbox=dict(boxstyle="round,pad=0.55", facecolor=CREAM, edgecolor=GREY, alpha=0.95),
            zorder=6)

    # Sketch map disclaimer caption
    ax.text(8.0, 3.7, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic",
            ha="center", va="center", color=INK)

    # Extents
    ax.set_xlim(-2.2, 14.8)
    ax.set_ylim(3.3, 15.3)

    save(fig, out)
