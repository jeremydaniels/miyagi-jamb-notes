from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    
    # Left subplot: Raster, Right subplot: Vector
    ax_raster = fig.add_axes([0.06, 0.12, 0.42, 0.74])
    ax_vector = fig.add_axes([0.54, 0.12, 0.42, 0.74])

    for ax in [ax_raster, ax_vector]:
        ax.set_xlim(-0.5, 15.5)
        ax.set_ylim(-0.5, 15.5)
        ax.set_aspect('equal')
        ax.axis('off')

    # Grid dimensions for raster: 16x16
    grid_size = 16

    # Draw grid background for Raster
    for x in range(grid_size + 1):
        ax_raster.axvline(x - 0.5, color=GREY, lw=0.8, alpha=0.7)
    for y in range(grid_size + 1):
        ax_raster.axhline(y - 0.5, color=GREY, lw=0.8, alpha=0.7)

    # 1. Raster River
    river_cells = [
        (0, 14), (1, 14), (2, 13), (3, 13), (4, 12), (5, 11), (5, 10),
        (6, 9), (7, 8), (8, 7), (8, 6), (9, 5), (10, 4), (11, 4),
        (12, 3), (13, 2), (14, 1), (15, 0)
    ]
    for r, c in river_cells:
        rect = patches.Rectangle((r - 0.5, c - 0.5), 1, 1, facecolor=BLUE, edgecolor=DEEP["blue"], lw=0.5)
        ax_raster.add_patch(rect)

    # 2. Raster Tree
    tree_cells = [
        (3, 3), (4, 3), (2, 4), (3, 4), (4, 4), (5, 4),
        (2, 5), (3, 5), (4, 5), (5, 5), (3, 6), (4, 6)
    ]
    for r, c in tree_cells:
        rect = patches.Rectangle((r - 0.5, c - 0.5), 1, 1, facecolor=GREEN, edgecolor=DEEP["green"], lw=0.5)
        ax_raster.add_patch(rect)
    # Tree trunk
    rect = patches.Rectangle((3.5 - 0.5, 2 - 0.5), 1, 1, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=0.5)
    ax_raster.add_patch(rect)

    # 3. Raster House
    for r in range(10, 14):
        for c in range(8, 12):
            rect = patches.Rectangle((r - 0.5, c - 0.5), 1, 1, facecolor=CREAM, edgecolor=GREY, lw=0.5)
            ax_raster.add_patch(rect)
    roof_cells = [
        (10, 12), (11, 12), (12, 12), (13, 12),
        (11, 13), (12, 13),
        (11, 14), (12, 14)
    ]
    for r, c in roof_cells:
        rect = patches.Rectangle((r - 0.5, c - 0.5), 1, 1, facecolor=PINK, edgecolor=DEEP["pink"], lw=0.5)
        ax_raster.add_patch(rect)

    # Raster outer boundary box
    rect_box = patches.Rectangle((-0.5, -0.5), 16, 16, fill=False, edgecolor=INK, lw=2)
    ax_raster.add_patch(rect_box)

    # Raster Titles & Captions
    ax_raster.text(7.5, 16.5, "Raster Data Model\n(Grid of pixels)", 
                   ha='center', va='bottom', fontsize=16, weight='bold', color=INK)

    # ---------------- Vector Plot ----------------
    # Outer frame
    rect_box_vec = patches.Rectangle((-0.5, -0.5), 16, 16, fill=False, edgecolor=INK, lw=2)
    ax_vector.add_patch(rect_box_vec)

    # 1. Vector River: Parametric curve for exact smooth line through points
    t_eval = np.linspace(0, 1, 200)
    x_smooth = 15 * t_eval
    y_smooth = 14 * (1 - t_eval) + 1.8 * np.sin(t_eval * np.pi * 2.0)
    ax_vector.plot(x_smooth, y_smooth, color=DEEP["blue"], lw=4, zorder=3)

    t_nodes = np.linspace(0, 1, 8)
    x_nodes = 15 * t_nodes
    y_nodes = 14 * (1 - t_nodes) + 1.8 * np.sin(t_nodes * np.pi * 2.0)
    ax_vector.plot(x_nodes, y_nodes, 'o', color=DEEP["blue"], 
                   markeredgecolor='white', markeredgewidth=1.5, markersize=7, zorder=4)

    # 2. Vector Tree: Point feature
    ax_vector.plot(3.5, 4.5, marker='o', markersize=10, color=DEEP["green"], markeredgecolor=INK, markeredgewidth=1.5, zorder=5)
    circle = patches.Circle((3.5, 4.5), radius=1.2, fill=False, edgecolor=DEEP["green"], lw=1.8, linestyle='--', zorder=4)
    ax_vector.add_patch(circle)

    # 3. Vector House: Geometric Polygons
    # Body
    body_pts = np.array([[9.5, 7.5], [13.5, 7.5], [13.5, 11.5], [9.5, 11.5]])
    poly_body = patches.Polygon(body_pts, closed=True, facecolor=CREAM, edgecolor=INK, lw=2, zorder=3)
    ax_vector.add_patch(poly_body)
    
    # Roof
    roof_pts = np.array([[9.5, 11.5], [13.5, 11.5], [11.5, 14.5]])
    poly_roof = patches.Polygon(roof_pts, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    ax_vector.add_patch(poly_roof)

    # Explicit polygon vertices
    all_house_pts = np.vstack([body_pts, [[11.5, 14.5]]])
    ax_vector.plot(all_house_pts[:, 0], all_house_pts[:, 1], 's', color=INK, markersize=6, zorder=4)

    # Annotations on Vector side
    ax_vector.annotate("Line", xy=(6.0, 9.2), xytext=(2.0, 11.8),
                       fontsize=14, color=INK,
                       arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                       bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"),
                       zorder=6)

    ax_vector.annotate("Point", xy=(3.5, 4.5), xytext=(1.2, 1.8),
                       fontsize=14, color=INK,
                       arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                       bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"),
                       zorder=6)

    ax_vector.annotate("Polygon", xy=(13.5, 10.0), xytext=(10.5, 5.6),
                       fontsize=14, color=INK,
                       arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                       bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"),
                       zorder=6)

    # Vector Titles & Captions
    ax_vector.text(7.5, 16.5, "Vector Data Model\n(Points, lines, polygons)", 
                   ha='center', va='bottom', fontsize=16, weight='bold', color=INK)

    save(fig, out)
