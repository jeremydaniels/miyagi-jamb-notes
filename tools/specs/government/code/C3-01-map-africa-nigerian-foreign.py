from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 9)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Base Africa polygons
    africa = continent_polys("Africa")
    for poly in africa:
        pts = np.asarray(poly)
        if pts.ndim == 2 and len(pts) >= 3:
            ax.fill(pts[:, 0], pts[:, 1], facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=1)

    # Highlight Nigeria: handle potential nested lists/arrays
    nig = nigeria_poly()
    # Handle if nigeria_poly() returns a single polygon Nx2, or a list of polygons
    if isinstance(nig, (list, tuple)):
        # Check if it's a list of polygons or a list of points
        first_item = nig[0]
        if isinstance(first_item, (list, tuple, np.ndarray)) and np.ndim(first_item) == 1 and len(first_item) == 2:
            # Single polygon represented as list of [x, y]
            nig_list = [np.asarray(nig)]
        else:
            nig_list = [np.asarray(p) for p in nig]
    else:
        nig_list = [np.asarray(nig)]

    for pts in nig_list:
        if pts.ndim == 2 and len(pts) >= 3:
            ax.fill(pts[:, 0], pts[:, 1], facecolor=GREEN, edgecolor=DEEP["green"], lw=2.0, zorder=2)

    # Nigeria label
    ax.text(8.0, 9.5, "NIGERIA", color=DEEP["green"], fontsize=15, fontweight="bold",
            ha="center", va="center", zorder=5,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["green"], lw=1.5))

    # Arrow 1: To Liberia / Sierra Leone
    dest_west = (-11.5, 7.5)
    ax.annotate(
        "", xy=dest_west, xytext=(4.0, 9.0),
        arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["blue"], lw=3.0,
                        connectionstyle="arc3,rad=-0.15"),
        zorder=4
    )
    ax.text(-12.0, 4.0, "ECOMOG Peacekeeping",
            fontsize=14, color=INK, ha="center", va="top", zorder=5,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=DEEP["blue"], lw=1.2))

    # Arrow 2: To Angola
    dest_angola = (17.5, -12.5)
    ax.annotate(
        "", xy=dest_angola, xytext=(8.5, 7.0),
        arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["orange"], lw=3.0,
                        connectionstyle="arc3,rad=0.15"),
        zorder=4
    )
    ax.text(21.0, -12.5, "1975 MPLA Support",
            fontsize=14, color=INK, ha="left", va="center", zorder=5,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=DEEP["orange"], lw=1.2))

    # Arrow 3: To South Africa
    dest_sa = (25.0, -29.0)
    ax.annotate(
        "", xy=dest_sa, xytext=(8.0, 6.0),
        arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["pink"], lw=3.0,
                        connectionstyle="arc3,rad=-0.1"),
        zorder=4
    )
    ax.text(25.0, -32.5, "Anti-Apartheid Frontline State",
            fontsize=14, color=INK, ha="center", va="top", zorder=5,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=DEEP["pink"], lw=1.2))

    # Title & Caption
    ax.set_title("Nigeria's Key Foreign Interventions in Africa",
                 fontsize=17, fontweight="bold", pad=20, color=INK)
    ax.text(0.5, 0.02, "Sketch map: zones are approximate",
            transform=ax.transAxes, fontsize=14, color=GREY, ha="center")

    ax.set_xlim(-25, 55)
    ax.set_ylim(-38, 38)

    save(fig, out)
