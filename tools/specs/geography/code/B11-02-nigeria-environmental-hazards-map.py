import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, PathPatch
from matplotlib.path import Path
from style import *

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Get Nigeria polygon
    # nigeria_poly() returns a list of polygons or a polygon structure from Natural Earth
    # In style.py, nigeria_poly() returns a shapely polygon or coordinates, or country_polys('Nigeria')
    # Standard helper usage:
    n_polys = nigeria_poly()
    if not isinstance(n_polys, list):
        n_polys = [n_polys]

    # Plot base Nigeria outline
    for poly in n_polys:
        if hasattr(poly, 'exterior'):
            x, y = poly.exterior.xy
            ax.plot(x, y, color=INK, lw=2.0)
            ax.fill(x, y, color='#FBFBF8', zorder=1)
            # Create a path for clipping zones
            ng_path = Path(np.column_stack((x, y)))
        else:
            # Assumed list of (x, y) coords or similar
            coords = np.array(poly)
            ax.plot(coords[:, 0], coords[:, 1], color=INK, lw=2.0)
            ax.fill(coords[:, 0], coords[:, 1], color='#FBFBF8', zorder=1)
            ng_path = Path(coords)

    # Coordinates roughly: Lon 2.6 to 14.7 E, Lat 4.2 to 13.9 N
    # Zone 1: Northern strip (Desertification and Drought) - roughly Lat > 11.5 N
    # Zone 2: South-eastern area (Severe Gully Erosion) - roughly Lon 6.8 to 9.2, Lat 5.2 to 7.2
    # Zone 3: Southern coastal strip / Niger Delta (Coastal Flooding and Oil Pollution) - roughly Lat < 6.0, coastal belt

    # 1. Northern Strip (Yellow / Orange tint)
    # Define a polygon across the north that covers latitude 11.2 to 14.5
    north_pts = np.array([
        [2.0, 11.2],
        [15.0, 11.2],
        [15.0, 14.5],
        [2.0, 14.5]
    ])
    patch_north = Polygon(north_pts, facecolor='#FFE57F', edgecolor='none', alpha=0.85, zorder=2)
    ax.add_patch(patch_north)
    patch_north.set_clip_path(PathPatch(ng_path, transform=ax.transData))

    # 2. South-eastern area (Brown with hatch marks)
    # Centered around Anambra, Imo, Abia, Enugu (approx Lon 6.5 to 8.6, Lat 5.2 to 6.8)
    se_pts = np.array([
        [6.6, 5.2],
        [7.0, 6.6],
        [8.3, 6.7],
        [8.6, 5.6],
        [7.8, 5.1],
        [6.8, 5.0]
    ])
    patch_se = Polygon(se_pts, facecolor='#D7CCC8', edgecolor='#5D4037', hatch='//', lw=1.2, alpha=0.9, zorder=3)
    ax.add_patch(patch_se)
    patch_se.set_clip_path(PathPatch(ng_path, transform=ax.transData))

    # 3. Southern coastal strip & Niger Delta (Blue)
    # Coast from west to east, up to lat ~5.5-6.0 around delta
    coast_pts = np.array([
        [2.0, 3.8],
        [10.0, 3.8],
        [9.5, 5.0],
        [7.5, 5.5],
        [5.0, 6.2],
        [2.5, 6.6],
        [2.0, 6.6]
    ])
    patch_coast = Polygon(coast_pts, facecolor=BLUE, edgecolor='none', alpha=0.75, zorder=2)
    ax.add_patch(patch_coast)
    patch_coast.set_clip_path(PathPatch(ng_path, transform=ax.transData))

    # Re-draw the boundary line on top so clipping doesn't obscure the border
    for poly in n_polys:
        if hasattr(poly, 'exterior'):
            x, y = poly.exterior.xy
            ax.plot(x, y, color=INK, lw=1.8, zorder=4)
        else:
            coords = np.array(poly)
            ax.plot(coords[:, 0], coords[:, 1], color=INK, lw=1.8, zorder=4)

    # Labels and Annotations with clean boxes and arrows
    # Title
    ax.text(8.5, 14.5, "Nigeria: Environmental Hazard Zones", fontsize=17,
            fontweight='bold', color=INK, ha='center', va='bottom')

    # Northern Label
    ax.annotate(
        "Prone to Desertification\nand Drought",
        xy=(8.5, 12.3), xytext=(8.5, 13.5),
        fontsize=14, color=INK, ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.0),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        zorder=5
    )

    # South-East Gully Erosion Label
    ax.annotate(
        "Severe Gully Erosion",
        xy=(7.6, 5.8), xytext=(11.5, 7.0),
        fontsize=14, color=INK, ha='left', va='center',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.0),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        zorder=5
    )

    # Coastal & Delta Label
    ax.annotate(
        "Prone to Coastal Flooding\nand Oil Pollution",
        xy=(5.5, 4.8), xytext=(4.0, 3.0),
        fontsize=14, color=INK, ha='center', va='top',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.0),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        zorder=5
    )

    # Caption note
    ax.text(8.5, 2.5, "Sketch map: zones are approximate", fontsize=14,
            style='italic', color=INK, ha='center', va='top')

    # Adjust view boundaries around Nigeria coordinates
    ax.set_xlim(1.5, 15.5)
    ax.set_ylim(2.2, 15.2)

    save(fig, out)
