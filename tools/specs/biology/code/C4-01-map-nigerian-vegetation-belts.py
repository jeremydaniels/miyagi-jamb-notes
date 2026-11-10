from style import *
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path

def draw(out):
    fig = canvas(15, 12)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(1.5, 16.5)
    ax.set_ylim(3.5, 15.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Get Nigeria polygon
    polys = nigeria_poly()
    ng_raw = polys[0] if isinstance(polys, (list, tuple)) else polys

    # Safely extract 2D coordinate array (N, 2)
    if hasattr(ng_raw, 'exterior'):
        coords = np.array(ng_raw.exterior.coords)
    elif isinstance(ng_raw, (list, tuple)):
        first_elem = ng_raw[0]
        if hasattr(first_elem, 'exterior'):
            coords = np.array(first_elem.exterior.coords)
        elif hasattr(first_elem, '__len__') and len(first_elem) == 2 and isinstance(first_elem[0], (int, float)):
            coords = np.array(ng_raw)
        elif hasattr(first_elem, '__len__') and len(first_elem) > 2:
            coords = np.array(first_elem)
        else:
            coords = np.array(ng_raw)
    else:
        coords = np.array(ng_raw)

    coords = np.atleast_2d(coords)
    if coords.ndim != 2 or coords.shape[1] != 2:
        coords = coords.reshape(-1, 2)

    ng_path = Path(coords)
    ng_patch = mpatches.PathPatch(ng_path, facecolor='none', edgecolor=INK, linewidth=2, zorder=10)
    ax.add_patch(ng_patch)

    # Colours for vegetation zones
    c_mangrove = "#2d5a3f"      # thin dark-green coastal strip
    c_rainforest = "#4e9b58"    # green band
    c_derived = "#8bc34a"       # pale green band
    c_s_guinea = "#c0ca33"      # yellow-green band
    c_n_guinea = "#ffd54f"      # yellow band (widest)
    c_sudan = "#ffb74d"         # pale orange band
    c_sahel = "#d7ccc8"         # light tan area (Sahel)
    c_highland = "#8d6e63"      # brown-purple for highlands

    # Create bands running roughly west to east across Nigeria
    def make_band(y_bot_w, y_bot_e, y_top_w, y_top_e):
        x = np.linspace(2, 15.5, 50)
        curve_bot = 0.3 * np.sin(np.pi * (x - 2) / 13.5)
        curve_top = 0.3 * np.sin(np.pi * (x - 2) / 13.5)
        y_bot = y_bot_w + (y_bot_e - y_bot_w) * (x - 2) / 13.5 - curve_bot
        y_top = y_top_w + (y_top_e - y_top_w) * (x - 2) / 13.5 - curve_top
        poly_pts = np.vstack([np.column_stack([x, y_bot]), np.column_stack([x[::-1], y_top[::-1]])])
        return poly_pts

    bands = [
        ("mangrove and swamp forest", make_band(3.5, 3.5, 5.3, 5.0), c_mangrove),
        ("tropical rainforest", make_band(5.3, 5.0, 6.8, 6.2), c_rainforest),
        ("derived savanna", make_band(6.8, 6.2, 7.8, 7.3), c_derived),
        ("southern Guinea savanna", make_band(7.8, 7.3, 9.2, 8.8), c_s_guinea),
        ("northern Guinea savanna", make_band(9.2, 8.8, 11.5, 11.2), c_n_guinea),
        ("Sudan savanna", make_band(11.5, 11.2, 13.2, 12.8), c_sudan),
        ("Sahel savanna", make_band(13.2, 12.8, 15.0, 15.0), c_sahel),
    ]

    for name, pts, col in bands:
        p = mpatches.Polygon(pts, facecolor=col, edgecolor=col, lw=0.5, zorder=2)
        p.set_clip_path(ng_patch)
        ax.add_patch(p)

    # Highlands: Jos Plateau, Mambilla Plateau, Obudu Plateau
    jos = mpatches.Ellipse((8.9, 9.5), 1.2, 1.0, angle=25, facecolor=c_highland, edgecolor="#5d4037", lw=1.5, zorder=5)
    jos.set_clip_path(ng_patch)
    ax.add_patch(jos)

    mambilla = mpatches.Ellipse((11.4, 6.9), 1.3, 0.7, angle=40, facecolor=c_highland, edgecolor="#5d4037", lw=1.5, zorder=5)
    mambilla.set_clip_path(ng_patch)
    ax.add_patch(mambilla)

    obudu = mpatches.Ellipse((9.3, 6.4), 0.6, 0.5, angle=-20, facecolor=c_highland, edgecolor="#5d4037", lw=1.5, zorder=5)
    obudu.set_clip_path(ng_patch)
    ax.add_patch(obudu)

    # Rivers Niger and Benue
    niger_x = [3.6, 4.3, 4.8, 5.1, 5.7, 6.4, 6.7, 6.8, 6.7, 6.4, 6.1]
    niger_y = [11.7, 10.5, 9.8, 8.9, 8.5, 8.0, 7.8, 6.5, 5.5, 4.8, 4.3]
    benue_x = [12.8, 12.2, 11.2, 9.8, 8.8, 7.8, 6.8]
    benue_y = [9.4, 9.1, 8.8, 8.2, 7.9, 7.8, 7.8]

    ax.plot(niger_x, niger_y, color=DEEP["blue"], lw=3, zorder=6)
    ax.plot(benue_x, benue_y, color=DEEP["blue"], lw=3, zorder=6)

    # Lake Chad patch in far NE
    lake_chad = mpatches.Polygon(np.array([[13.5, 13.0], [14.3, 12.8], [14.6, 13.6], [14.1, 14.2], [13.4, 13.8]]),
                                 facecolor="#90caf9", edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    lake_chad.set_clip_path(ng_patch)
    ax.add_patch(lake_chad)

    # Atlantic Ocean label
    ax.text(5.5, 3.8, "Atlantic Ocean", fontsize=16, fontstyle="italic", color=DEEP["blue"], ha="center")
    
    # Lake Chad label
    ax.text(13.9, 13.3, "Lake Chad", fontsize=14, color=DEEP["blue"], ha="center",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85), zorder=8)

    # Sahara Desert label beyond northern border
    ax.text(8.0, 14.3, "Sahara Desert (beyond Nigeria)", fontsize=16, fontstyle="italic", color="#795548", ha="center")

    # River labels
    ax.text(4.4, 9.9, "River Niger", fontsize=14, fontstyle="italic", color=DEEP["blue"], rotation=-45,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85), zorder=7)
    ax.text(9.9, 8.6, "River Benue", fontsize=14, fontstyle="italic", color=DEEP["blue"], rotation=15,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85), zorder=7)

    # Plateau labels
    ax.text(8.9, 9.0, "Jos Plateau", fontsize=14, fontweight="bold", color=INK, ha="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=8)
    ax.text(12.3, 6.7, "Mambilla Plateau", fontsize=14, fontweight="bold", color=INK, ha="left",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=8)
    ax.text(9.7, 6.1, "Obudu Plateau", fontsize=14, fontweight="bold", color=INK, ha="left",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=8)

    # Main towns
    towns = [
        ("Lagos", 3.4, 6.5, (-25, -12)),
        ("Port Harcourt", 7.0, 4.8, (15, 12)),  # Moved to avoid southern boundary overlap
        ("Calabar", 8.3, 5.0, (10, -8)),
        ("Benin City", 5.6, 6.3, (-15, -14)),
        ("Ibadan", 3.9, 7.4, (-30, 8)),
        ("Enugu", 7.5, 6.4, (10, -5)),
        ("Ilorin", 4.5, 8.5, (-30, -5)),
        ("Makurdi", 8.5, 7.7, (10, -5)),
        ("Abuja", 7.5, 9.1, (10, 5)),
        ("Jos", 8.9, 9.9, (10, 10)),
        ("Kaduna", 7.4, 10.5, (-35, 5)),
        ("Zaria", 7.7, 11.1, (-25, 8)),
        ("Kano", 8.5, 12.0, (10, 5)),
        ("Sokoto", 5.2, 13.0, (10, 5)),
        ("Maiduguri", 13.1, 11.8, (10, 5)),
    ]

    for name, tx, ty, (off_x, off_y) in towns:
        ax.plot(tx, ty, marker='o', markersize=6, color=INK, zorder=9)
        ax.annotate(name, xy=(tx, ty), xytext=(tx + off_x * 0.03, ty + off_y * 0.03),
                    fontsize=14, fontweight="medium", color=INK,
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8),
                    zorder=9)

    # Vegetation belt annotations
    ax.text(12.5, 13.0, "Sahel savanna", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_sahel, lw=2), zorder=8)
    ax.text(10.8, 12.3, "Sudan savanna", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_sudan, lw=2), zorder=8)
    ax.text(2.3, 10.5, "northern Guinea savanna", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_n_guinea, lw=2), zorder=8)
    ax.text(2.3, 8.6, "southern Guinea savanna", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_s_guinea, lw=2), zorder=8)
    ax.text(2.3, 7.1, "derived savanna", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_derived, lw=2), zorder=8)
    ax.text(2.3, 5.6, "tropical rainforest", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=c_rainforest, lw=2), zorder=8)
    ax.text(7.6, 4.3, "mangrove and swamp forest", fontsize=14, fontweight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.25", fc=c_mangrove, ec="none"), zorder=8)

    # Rainfall arrow on the right side
    ax.annotate("", xy=(15.8, 14.0), xytext=(15.8, 5.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3, mutation_scale=20),
                zorder=10)
    ax.text(16.0, 9.5, "rainfall decreases northwards", fontsize=15, rotation=-90,
            color=DEEP["blue"], ha="left", va="center", fontweight="bold")

    # Caption
    ax.text(2.2, 3.8, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic", color=GREY)

    save(fig, out)
