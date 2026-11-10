from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Get Nigeria boundary from style helper (returns a numpy array or list of arrays)
    nigeria_geom = nigeria_poly()
    
    if isinstance(nigeria_geom, np.ndarray):
        poly_list = [nigeria_geom]
    else:
        poly_list = list(nigeria_geom)

    # Construct the clipping paths for the three regions based on the
    # Niger and Benue rivers converging at Lokoja (approx 6.75, 7.8)
    # 1. Northern Region Mask
    north_pts = np.array([
        [-1.0, 16.0], [16.0, 16.0], [16.0, 9.5],
        [12.0, 9.3], [10.0, 8.9], [8.5, 8.3],
        [6.75, 7.8],
        [5.5, 8.8], [4.5, 10.2], [3.6, 11.6],
        [-1.0, 12.0]
    ])

    # 2. Western Region Mask
    west_pts = np.array([
        [-1.0, 12.0], [3.6, 11.6], [4.5, 10.2], [5.5, 8.8],
        [6.75, 7.8],
        [6.75, 6.5], [6.5, 5.4], [6.2, 4.2], [6.2, 2.0],
        [-1.0, 2.0]
    ])

    # 3. Eastern Region Mask
    east_pts = np.array([
        [16.0, 9.5], [12.0, 9.3], [10.0, 8.9], [8.5, 8.3],
        [6.75, 7.8],
        [6.75, 6.5], [6.5, 5.4], [6.2, 4.2], [6.2, 2.0],
        [16.0, 2.0]
    ])

    # Draw the regions with clipping to the Nigeria boundary
    for coords in poly_list:
        nigeria_path = Path(coords)
        nigeria_clip = patches.PathPatch(nigeria_path, transform=ax.transData, facecolor="none", edgecolor="none")
        ax.add_patch(nigeria_clip)

        # Northern patch
        p_north = patches.Polygon(north_pts, facecolor=CREAM, edgecolor="none", zorder=2)
        p_north.set_clip_path(nigeria_clip)
        ax.add_patch(p_north)

        # Western patch
        p_west = patches.Polygon(west_pts, facecolor=GREEN, edgecolor="none", zorder=2)
        p_west.set_clip_path(nigeria_clip)
        ax.add_patch(p_west)

        # Eastern patch
        p_east = patches.Polygon(east_pts, facecolor=BLUE, edgecolor="none", zorder=2)
        p_east.set_clip_path(nigeria_clip)
        ax.add_patch(p_east)

        # Outer border
        ax.plot(coords[:, 0], coords[:, 1], color=INK, lw=2.5, zorder=5)

    # Dividing river boundaries (bold lines)
    river_nw = np.array([[3.65, 11.6], [4.5, 10.2], [5.5, 8.8], [6.75, 7.8]])
    river_e = np.array([[6.75, 7.8], [8.5, 8.3], [10.0, 8.9], [11.9, 9.25]])
    river_s = np.array([[6.75, 7.8], [6.75, 6.5], [6.5, 5.4], [6.2, 4.35]])

    for r_pts in [river_nw, river_e, river_s]:
        ax.plot(r_pts[:, 0], r_pts[:, 1], color=INK, lw=3.0, zorder=6)

    # Labels
    bbox_style = dict(facecolor="white", edgecolor=GREY, boxstyle="round,pad=0.4", alpha=0.95)

    ax.text(8.3, 10.5, "Northern Region", fontsize=16, weight="bold", ha="center", va="center",
            color=INK, bbox=bbox_style, zorder=7)
    ax.text(4.8, 6.8, "Western\nRegion", fontsize=15, weight="bold", ha="center", va="center",
            color=INK, bbox=bbox_style, zorder=7)
    ax.text(8.8, 6.0, "Eastern\nRegion", fontsize=15, weight="bold", ha="center", va="center",
            color=INK, bbox=bbox_style, zorder=7)

    # River labels
    ax.text(4.2, 9.6, "R. Niger", fontsize=14, fontstyle="italic", color=DEEP["blue"],
            rotation=-55, ha="center", va="center", zorder=7)
    ax.text(10.2, 8.4, "R. Benue", fontsize=14, fontstyle="italic", color=DEEP["blue"],
            rotation=16, ha="center", va="center", zorder=7)

    # Title & Caption
    ax.set_title("Foundation of Regionalism (1946)", fontsize=18, weight="bold", color=INK, pad=20)
    ax.text(8.5, 3.2, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic",
            color=GREY, ha="center", va="center")

    # Limits based on Nigeria extent
    minx = min(np.min(c[:, 0]) for c in poly_list)
    maxx = max(np.max(c[:, 0]) for c in poly_list)
    miny = min(np.min(c[:, 1]) for c in poly_list)
    maxy = max(np.max(c[:, 1]) for c in poly_list)

    ax.set_xlim(minx - 0.6, maxx + 0.6)
    ax.set_ylim(miny - 0.8, maxy + 1.2)

    save(fig, out)
