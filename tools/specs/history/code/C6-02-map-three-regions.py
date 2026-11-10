from style import *
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.path as mpath

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Get Nigeria polygon coordinates from style helper
    # nigeria_poly() returns shapely polygon or coordinates depending on helper implementation
    # Let's extract polygon outline safely
    raw_poly = nigeria_poly()
    
    # Extract coordinate array(s) without importing shapely
    poly_coords = []
    if hasattr(raw_poly, 'exterior'):
        poly_coords.append(np.array(raw_poly.exterior.coords))
    elif isinstance(raw_poly, list):
        for p in raw_poly:
            if hasattr(p, 'exterior'):
                poly_coords.append(np.array(p.exterior.coords))
            elif isinstance(p, (np.ndarray, list)):
                poly_coords.append(np.array(p))
    else:
        # Fallback approximation of Nigeria boundary if coordinates structure is different
        poly_coords = [np.array([
            (2.7, 6.3), (2.7, 9.0), (3.6, 10.5), (3.6, 11.7), (4.5, 12.0),
            (5.5, 13.8), (7.0, 13.0), (8.5, 13.0), (10.0, 13.8), (13.5, 13.5),
            (14.6, 12.5), (14.2, 11.5), (13.5, 10.0), (12.0, 9.0), (11.5, 7.0),
            (9.5, 6.5), (8.5, 4.8), (7.0, 4.3), (5.5, 5.0), (4.0, 6.2), (2.7, 6.3)
        ])]

    # Prepare clip path from the main Nigeria polygon
    main_ring = poly_coords[0]
    clip_patch = mpatches.Polygon(main_ring, transform=ax.transData, facecolor='none', edgecolor='none')
    ax.add_patch(clip_patch)

    # Dividing boundaries:
    # 1. Richards Constitution bold North-South boundary:
    # Starts west border at ~lat 8.0, passes north of Oyo/Kwara, near confluence (Lokoja, ~6.7E, 7.8N),
    # then heads east towards Cameroon border at ~lat 7.0.
    ns_line_pts = np.array([
        (2.0, 8.0),
        (3.5, 8.0),
        (5.0, 7.9),
        (6.7, 7.8),
        (8.5, 7.3),
        (10.0, 7.1),
        (12.0, 6.8),
        (15.5, 6.8)
    ])

    # 2. West-East dividing line along the Niger River south of confluence to Niger Delta:
    we_line_pts = np.array([
        (6.7, 7.8),
        (6.65, 7.0),
        (6.6, 6.0),
        (6.7, 5.0),
        (6.7, 3.5)
    ])

    # Define bounding polygons for the three regions that cover beyond Nigeria's borders,
    # so they can be clipped neatly by the Nigeria polygon.
    # Northern Region: north of ns_line_pts
    poly_north = np.vstack([
        ns_line_pts,
        [[16.0, 6.8], [16.0, 15.0], [1.5, 15.0], [1.5, 8.0]]
    ])

    # Western Region: south of ns_line_pts, west of we_line_pts
    poly_west = np.vstack([
        [(1.5, 3.5)],
        ns_line_pts[ns_line_pts[:, 0] <= 6.7],
        we_line_pts,
        [(1.5, 3.5)]
    ])

    # Eastern Region: south of ns_line_pts, east of we_line_pts
    poly_east = np.vstack([
        we_line_pts,
        ns_line_pts[ns_line_pts[:, 0] >= 6.7],
        [[16.0, 6.8], [16.0, 3.5], [6.7, 3.5]]
    ])

    # Distinct textbook colours:
    # Northern Region: green
    # Western Region: yellow
    # Eastern Region: blue
    YELLOW = "#FFF08A"

    patch_north = mpatches.Polygon(poly_north, facecolor=GREEN, edgecolor='none', zorder=2)
    patch_north.set_clip_path(clip_patch)
    ax.add_patch(patch_north)

    patch_west = mpatches.Polygon(poly_west, facecolor=YELLOW, edgecolor='none', zorder=2)
    patch_west.set_clip_path(clip_patch)
    ax.add_patch(patch_west)

    patch_east = mpatches.Polygon(poly_east, facecolor=BLUE, edgecolor='none', zorder=2)
    patch_east.set_clip_path(clip_patch)
    ax.add_patch(patch_east)

    # Draw Nigeria external outline
    for coords in poly_coords:
        ax.plot(coords[:, 0], coords[:, 1], color=INK, lw=2.2, zorder=5)

    # Draw bold boundary separating North from South (clipped)
    line_ns = ax.plot(ns_line_pts[:, 0], ns_line_pts[:, 1], color=INK, lw=3.8, zorder=6)[0]
    line_ns.set_clip_path(clip_patch)

    # Draw West-East boundary line (clipped)
    line_we = ax.plot(we_line_pts[:, 0], we_line_pts[:, 1], color=INK, lw=2.0, ls='--', zorder=6)[0]
    line_we.set_clip_path(clip_patch)

    # Lagos dot and label in the southwest
    lagos_x, lagos_y = 3.4, 6.45
    ax.scatter([lagos_x], [lagos_y], color=INK, s=55, zorder=8)
    ax.annotate("Lagos", xy=(lagos_x, lagos_y), xytext=(lagos_x - 0.7, lagos_y - 1.0),
                fontsize=15, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=9)

    # Region Labels
    ax.text(8.2, 10.3, "NORTHERN REGION", fontsize=16, fontweight="bold",
            color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=8)

    ax.text(4.4, 6.5, "WESTERN\nREGION", fontsize=15, fontweight="bold",
            color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=8)

    ax.text(9.0, 5.8, "EASTERN\nREGION", fontsize=15, fontweight="bold",
            color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=8)

    # Title & Subtitle
    ax.text(8.2, 14.6, "Nigeria in 1946: Richards Constitution",
            fontsize=18, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(8.2, 14.0, "The Three Regions and Bold North–South Boundary",
            fontsize=15, color=INK, ha="center", va="center")

    # Sea label
    ax.text(4.2, 4.3, "Gulf of Guinea", fontsize=14, fontstyle="italic",
            color=DEEP["blue"], ha="center", va="center")

    # Legend / Annotation for boundary
    ax.plot([10.5, 12.0], [4.4, 4.4], color=INK, lw=3.8, zorder=7)
    ax.text(12.2, 4.4, "North–South boundary", fontsize=14, color=INK, va="center")
    ax.plot([10.5, 12.0], [3.9, 3.9], color=INK, lw=2.0, ls='--', zorder=7)
    ax.text(12.2, 3.9, "Western–Eastern boundary", fontsize=14, color=INK, va="center")

    # Mandatory caption note
    ax.text(8.2, 3.3, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", color=INK, ha="center", va="center")

    ax.set_xlim(1.8, 15.2)
    ax.set_ylim(3.0, 15.2)

    save(fig, out)
