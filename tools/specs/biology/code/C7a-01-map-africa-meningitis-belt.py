from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9.5, 9.2)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_facecolor("white")
    ax.axis("off")

    # Map bounds around Africa with generous margins
    # Longitude: -22 to 54, Latitude: -38 to 40
    ax.set_xlim(-22, 54)
    ax.set_ylim(-38, 40)

    # 1. Continent outline
    africa_polys = continent_polys("Africa")
    for poly in africa_polys:
        patch = patches.Polygon(poly, closed=True, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=2)
        ax.add_patch(patch)

    # 2. Meningitis belt polygon
    # Stretches from Senegal in the west across to Ethiopia in the east (8°N to 16°N Sahel band)
    belt_coords = [
        (-17.5, 14.5),
        (-15.0, 16.5),
        (-5.0, 16.5),
        (5.0, 15.5),
        (15.0, 15.0),
        (25.0, 15.5),
        (34.0, 15.0),
        (40.0, 12.0),
        (42.0, 9.0),
        (40.0, 7.5),
        (35.0, 7.5),
        (25.0, 9.5),
        (15.0, 9.5),
        (8.0, 9.0),
        (0.0, 8.5),
        (-10.0, 9.0),
        (-16.5, 11.0),
        (-17.5, 14.5)
    ]
    belt_poly = patches.Polygon(belt_coords, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"],
                                lw=2.0, alpha=0.6, zorder=3)
    ax.add_patch(belt_poly)

    # 3. Nigeria outline
    nig_poly = nigeria_poly()
    nig_patch = patches.Polygon(nig_poly, closed=True, facecolor="none", edgecolor=DEEP["blue"],
                                lw=2.5, zorder=4)
    ax.add_patch(nig_patch)

    # 4. Labels & Titles
    # Main Title
    ax.text(15, 36.5, "African Meningitis Belt", fontsize=18, fontweight="bold",
            color=INK, ha="center", va="center")

    # Sahara Desert label
    ax.text(12, 23.5, "Sahara Desert", fontsize=15, fontstyle="italic",
            color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85), zorder=5)

    # Meningitis belt label with arrow
    ax.annotate("Meningitis belt",
                xy=(18, 12.5), xytext=(22, 19),
                fontsize=15, fontweight="bold", color=DEEP["orange"],
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2),
                ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["orange"], lw=1.2),
                zorder=6)

    # Nigeria label
    ax.annotate("Nigeria",
                xy=(8.0, 6.0), xytext=(0.0, -1.0),
                fontsize=15, fontweight="bold", color=DEEP["blue"],
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.8),
                ha="center", va="top",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.2),
                zorder=6)

    # Northern Nigeria inside the belt
    ax.annotate("Northern Nigeria\n(inside the belt)",
                xy=(8.5, 11.5), xytext=(-8.0, 4.0),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.0),
                zorder=6)

    # 5. Inset Box: Harmattan dry season symbol (Sun and dust cloud)
    # Box located in Atlantic Ocean off southwest coast (-21 to 7, -35 to -19)
    box_x, box_y, box_w, box_h = -21, -35, 27.5, 15
    box = patches.FancyBboxPatch((box_x, box_y), box_w, box_h,
                                 boxstyle="round,pad=0.5",
                                 fc="white", ec=GREY, lw=1.5, zorder=5)
    ax.add_patch(box)

    # Inside Inset:
    # Dry season title label
    ax.text(box_x + box_w / 2, box_y + box_h - 1.8, "Dry season: about December to June",
            fontsize=14, fontweight="bold", color=INK, ha="center", va="top", zorder=6)

    # Sun symbol
    sun_cx, sun_cy = box_x + 5.5, box_y + 6.2
    sun_r = 1.8
    sun_circle = plt.Circle((sun_cx, sun_cy), sun_r, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=6)
    ax.add_patch(sun_circle)
    # Sun rays
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        rx1 = sun_cx + 2.3 * np.cos(angle)
        ry1 = sun_cy + 2.3 * np.sin(angle)
        rx2 = sun_cx + 3.2 * np.cos(angle)
        ry2 = sun_cy + 3.2 * np.sin(angle)
        ax.plot([rx1, rx2], [ry1, ry2], color=DEEP["orange"], lw=1.8, zorder=6)

    # Dust cloud symbol next to sun
    cloud_cx, cloud_cy = box_x + 16.5, box_y + 6.2
    c1 = plt.Circle((cloud_cx - 2.5, cloud_cy - 0.8), 1.6, fc=CREAM, ec=GREY, lw=1.3, zorder=6)
    c2 = plt.Circle((cloud_cx + 2.2, cloud_cy - 0.6), 1.7, fc=CREAM, ec=GREY, lw=1.3, zorder=6)
    c3 = plt.Circle((cloud_cx, cloud_cy + 0.8), 2.2, fc=CREAM, ec=GREY, lw=1.3, zorder=7)
    c4 = plt.Circle((cloud_cx - 1.2, cloud_cy - 0.2), 2.0, fc=CREAM, ec="none", zorder=8)
    c5 = plt.Circle((cloud_cx + 1.2, cloud_cy - 0.2), 1.9, fc=CREAM, ec="none", zorder=8)
    for c in [c1, c2, c3, c4, c5]:
        ax.add_patch(c)
    # Dust lines / wind strokes
    ax.plot([cloud_cx - 4.5, cloud_cx + 4.5], [cloud_cy - 2.8, cloud_cy - 2.8], color=GREY, lw=1.8, ls="--", zorder=9)
    ax.plot([cloud_cx - 3.0, cloud_cx + 3.5], [cloud_cy - 3.7, cloud_cy - 3.7], color=GREY, lw=1.5, ls="--", zorder=9)

    ax.text(cloud_cx, box_y + 1.1, "Dust-laden Harmattan winds",
            fontsize=14, fontstyle="italic", color=INK, ha="center", va="center", zorder=9)

    # Caption schematic note - placed clearly in the Indian Ocean area (open ocean, no land overlap)
    ax.text(37, -32, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", color=GREY, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.9), zorder=5)

    save(fig, out)
