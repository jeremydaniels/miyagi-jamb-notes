from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    # Canvas setup
    fig = canvas(10, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 12.5)
    ax.axis('off')

    # Isometric/oblique projection parameters for square layers
    # Base square coordinates in 2D plane: (u, v) in [0, 1] x [0, 1]
    # Projection to canvas: x = u_vec * u + v_vec * v + x0
    #                       y = u_y * u + v_y * v + y0
    ux, uy = 4.2, -1.2
    vx, vy = 3.0, 1.5

    def to_iso(u, v, y_level):
        x = 1.0 + ux * u + vx * v
        y = y_level + uy * u + vy * v
        return x, y

    def layer_corners(y_level):
        c = [to_iso(0, 0, y_level),
             to_iso(1, 0, y_level),
             to_iso(1, 1, y_level),
             to_iso(0, 1, y_level)]
        return np.array(c)

    # Elevation levels for the 5 tiers (bottom real-world to top transportation)
    levels = [0.8, 3.2, 5.4, 7.6, 9.8]
    
    # Feature coordinates in UV space (0 to 1) so they align across all layers:
    # A reference vertical alignment point
    ref_u, ref_v = 0.55, 0.45

    # Features:
    # 1. Lake polygon
    lake_u = np.array([0.45, 0.65, 0.75, 0.65, 0.4, 0.35])
    lake_v = np.array([0.35, 0.3, 0.5, 0.65, 0.6, 0.45])

    # River path
    river_u = np.array([0.0, 0.2, 0.35, 0.65, 0.85, 1.0])
    river_v = np.array([0.2, 0.3, 0.45, 0.65, 0.75, 0.9])

    # 2. Forest polygons
    forest1_u = np.array([0.1, 0.3, 0.25, 0.05])
    forest1_v = np.array([0.55, 0.6, 0.85, 0.8])
    forest2_u = np.array([0.7, 0.9, 0.95, 0.8])
    forest2_v = np.array([0.15, 0.1, 0.35, 0.4])

    # 3. Roads
    road1_u = np.array([0.0, 0.4, 0.7, 1.0])
    road1_v = np.array([0.5, 0.4, 0.3, 0.2])
    road2_u = np.array([0.5, 0.52, 0.55, 0.6])
    road2_v = np.array([0.0, 0.35, 0.7, 1.0])

    # 4. Buildings (u, v, width, height)
    buildings = [
        (0.58, 0.42, 0.06, 0.06, PINK),
        (0.48, 0.48, 0.05, 0.07, GREY),
        (0.62, 0.52, 0.07, 0.05, PINK),
        (0.42, 0.32, 0.06, 0.05, GREY),
        (0.52, 0.25, 0.05, 0.05, PINK),
        (0.68, 0.38, 0.05, 0.06, GREY)
    ]

    # --- Draw Layers bottom to top ---

    # Level 0: Real World / Satellite Image
    y0 = levels[0]
    poly0 = layer_corners(y0)
    # Background terrain base
    patch0 = Polygon(poly0, facecolor='#dcedc8', edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(patch0)

    # Real world features on satellite layer
    # Forest patches (realistic satellite shading)
    for fu, fv in [(forest1_u, forest1_v), (forest2_u, forest2_v)]:
        pts = np.column_stack(to_iso(fu, fv, y0))
        ax.add_patch(Polygon(pts, facecolor=GREEN, edgecolor=DEEP['green'], lw=1, alpha=0.9, zorder=3))

    # Water on satellite layer
    pts_lake = np.column_stack(to_iso(lake_u, lake_v, y0))
    ax.add_patch(Polygon(pts_lake, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1, zorder=3))
    rx, ry = to_iso(river_u, river_v, y0)
    ax.plot(rx, ry, color=DEEP['blue'], lw=3, zorder=3)

    # Roads on satellite layer
    r1x, r1y = to_iso(road1_u, road1_v, y0)
    r2x, r2y = to_iso(road2_u, road2_v, y0)
    ax.plot(r1x, r1y, color='#757575', lw=2, zorder=4)
    ax.plot(r2x, r2y, color='#757575', lw=2, zorder=4)

    # Buildings on satellite layer
    for bu, bv, bw, bh, col in buildings:
        b_pts = np.column_stack(to_iso(np.array([bu, bu+bw, bu+bw, bu]), np.array([bv, bv, bv+bh, bv+bh]), y0))
        ax.add_patch(Polygon(b_pts, facecolor=col, edgecolor=INK, lw=0.8, zorder=5))

    # Level 1: Water Layer
    y1 = levels[1]
    patch1 = Polygon(layer_corners(y1), facecolor='white', edgecolor=DEEP['blue'], lw=1.8, alpha=0.75, zorder=2)
    ax.add_patch(patch1)
    pts_lake1 = np.column_stack(to_iso(lake_u, lake_v, y1))
    ax.add_patch(Polygon(pts_lake1, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5, zorder=3))
    rx1, ry1 = to_iso(river_u, river_v, y1)
    ax.plot(rx1, ry1, color=DEEP['blue'], lw=3.5, zorder=3)

    # Level 2: Vegetation Layer
    y2 = levels[2]
    patch2 = Polygon(layer_corners(y2), facecolor='white', edgecolor=DEEP['green'], lw=1.8, alpha=0.75, zorder=2)
    ax.add_patch(patch2)
    for fu, fv in [(forest1_u, forest1_v), (forest2_u, forest2_v)]:
        pts = np.column_stack(to_iso(fu, fv, y2))
        ax.add_patch(Polygon(pts, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=3))

    # Level 3: Structures Layer
    y3 = levels[3]
    patch3 = Polygon(layer_corners(y3), facecolor='white', edgecolor=DEEP['pink'], lw=1.8, alpha=0.75, zorder=2)
    ax.add_patch(patch3)
    for bu, bv, bw, bh, col in buildings:
        b_pts = np.column_stack(to_iso(np.array([bu, bu+bw, bu+bw, bu]), np.array([bv, bv, bv+bh, bv+bh]), y3))
        ax.add_patch(Polygon(b_pts, facecolor=col, edgecolor=INK, lw=1.2, zorder=3))

    # Level 4: Transportation Layer
    y4 = levels[4]
    patch4 = Polygon(layer_corners(y4), facecolor='white', edgecolor='#555555', lw=1.8, alpha=0.75, zorder=2)
    ax.add_patch(patch4)
    r1x4, r1y4 = to_iso(road1_u, road1_v, y4)
    r2x4, r2y4 = to_iso(road2_u, road2_v, y4)
    ax.plot(r1x4, r1y4, color='#424242', lw=3, zorder=3)
    ax.plot(r2x4, r2y4, color='#424242', lw=3, zorder=3)

    # Vertical dashed line passing through all layers to show alignment
    ref_x_vals = [to_iso(ref_u, ref_v, lvl)[0] for lvl in levels]
    ref_y_vals = [to_iso(ref_u, ref_v, lvl)[1] for lvl in levels]
    
    # Extend slightly above and below
    line_x = ref_x_vals[0]
    ax.plot([line_x, line_x], [ref_y_vals[0] - 0.3, ref_y_vals[-1] + 0.8],
            color=DEEP['orange'], linestyle='--', lw=2.2, dashes=(4, 3), zorder=10)
    
    for rx_pt, ry_pt in zip(ref_x_vals, ref_y_vals):
        ax.plot(rx_pt, ry_pt, marker='o', markersize=6, color=DEEP['orange'], zorder=11)

    # Alignment annotation
    ax.annotate("Geographic alignment\nacross layers",
                xy=(line_x, ref_y_vals[-1] + 0.8),
                xytext=(line_x + 1.2, ref_y_vals[-1] + 1.1),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=12)

    # Layer Labels with descriptions on the right
    labels_info = [
        (y4, "Transportation", "Roads and transport networks (lines)", DEEP['orange']),
        (y3, "Structures", "Houses, buildings and parcels (polygons)", DEEP['pink']),
        (y2, "Vegetation", "Forests, crops and ground cover (polygons)", DEEP['green']),
        (y1, "Water", "Rivers, lakes and water bodies (polygons/lines)", DEEP['blue']),
        (y0, "Real World", "Integrated landscape / satellite base", INK)
    ]

    for y_lvl, title, desc, col in labels_info:
        # Get right corner of layer
        right_corner = to_iso(1, 0.5, y_lvl)
        ax.plot([right_corner[0], right_corner[0] + 0.5], [right_corner[1], right_corner[1]],
                color=GREY, lw=1.2, zorder=1)
        ax.text(right_corner[0] + 0.6, right_corner[1] + 0.1, title,
                fontsize=16, fontweight='bold', color=INK, va='bottom', zorder=12)
        ax.text(right_corner[0] + 0.6, right_corner[1] - 0.25, desc,
                fontsize=14, color='#555555', va='top', zorder=12)

    save(fig, out)
