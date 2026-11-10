from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge, Arc, FancyArrowPatch

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.5, 6.0)

    # Left: Net of cone (Sector of circle)
    # Vertex at (2.5, 4.8), radius R = 3.6
    # Angles: from 215 deg to 325 deg (span = 110 deg)
    v_x, v_y = 2.5, 4.8
    R = 3.6
    th1, th2 = 215, 325
    rad1, rad2 = np.deg2rad(th1), np.deg2rad(th2)

    # Draw sector fill
    arc_thetas = np.linspace(rad1, rad2, 100)
    arc_x = v_x + R * np.cos(arc_thetas)
    arc_y = v_y + R * np.sin(arc_thetas)
    sector_pts = np.vstack([[v_x, v_y], np.column_stack([arc_x, arc_y]), [v_x, v_y]])
    poly_sector = Polygon(sector_pts, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=2)
    ax.add_patch(poly_sector)

    # Apex vertex dot
    ax.plot(v_x, v_y, 'o', color=INK, markersize=5, zorder=5)

    # Sector angle arc at vertex
    ang_rad = 0.6
    ang_thetas = np.linspace(rad1, rad2, 40)
    ax.plot(v_x + ang_rad * np.cos(ang_thetas), v_y + ang_rad * np.sin(ang_thetas), color=INK, lw=1.5, zorder=3)
    ax.text(v_x, v_y - 0.9, r"$\theta$", fontsize=15, ha="center", va="center", color=INK)

    # Radius labels
    # Along left edge
    mid_left_x = v_x + 0.5 * R * np.cos(rad1) - 0.25
    mid_left_y = v_y + 0.5 * R * np.sin(rad1) + 0.15
    ax.text(mid_left_x, mid_left_y, "radius $R$", fontsize=15, color=INK, ha="right", va="center", rotation=35)

    # Along right edge
    mid_right_x = v_x + 0.5 * R * np.cos(rad2) + 0.25
    mid_right_y = v_y + 0.5 * R * np.sin(rad2) + 0.15
    ax.text(mid_right_x, mid_right_y, "radius $R$", fontsize=15, color=INK, ha="left", va="center", rotation=-35)

    # Arc length label along base of sector
    bottom_arc_x = v_x
    bottom_arc_y = v_y - R
    ax.annotate(r"Arc length $s = 2\pi r$", xy=(bottom_arc_x, bottom_arc_y), xytext=(bottom_arc_x, bottom_arc_y - 0.7),
                fontsize=15, ha="center", va="top", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # Rolling arrows showing folding along sector edges
    fold_arr_left = FancyArrowPatch((v_x + 2.2 * np.cos(rad1) - 0.1, v_y + 2.2 * np.sin(rad1) - 0.2),
                                    (v_x + 1.8 * np.cos(rad1) + 0.5, v_y + 1.8 * np.sin(rad1) + 0.4),
                                    connectionstyle="arc3,rad=-0.4",
                                    arrowstyle="-|>", mutation_scale=16, color=DEEP["orange"], lw=2.2, zorder=6)
    fold_arr_right = FancyArrowPatch((v_x + 2.2 * np.cos(rad2) + 0.1, v_y + 2.2 * np.sin(rad2) - 0.2),
                                     (v_x + 1.8 * np.cos(rad2) - 0.5, v_y + 1.8 * np.sin(rad2) + 0.4),
                                     connectionstyle="arc3,rad=0.4",
                                     arrowstyle="-|>", mutation_scale=16, color=DEEP["orange"], lw=2.2, zorder=6)
    ax.add_patch(fold_arr_left)
    ax.add_patch(fold_arr_right)

    # Big transition arrow between 2D net and 3D cone
    trans_arr = FancyArrowPatch((4.7, 2.6), (6.3, 2.6),
                                arrowstyle="-|>", mutation_scale=22, color=DEEP["blue"], lw=3.0)
    ax.add_patch(trans_arr)
    ax.text(5.5, 3.0, "fold & join\nedges", fontsize=15, ha="center", va="bottom", color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    # Right: 3D Cone
    # Base center at (8.8, 1.2), apex at (8.8, 4.8)
    cone_cx, cone_cy = 8.8, 1.2
    cone_apex_y = 4.8
    r_val = 1.6
    b_val = 0.45  # ellipse minor radius for 3D perspective

    # Cone body polygon: apex -> tangent on left -> bottom arc -> tangent on right -> apex
    # For ellipse x = r cos t, y = b sin t, tangent from apex (0, H):
    # Tangents touch slightly above bottom, near t = np.pi and 0
    t_vals = np.linspace(np.pi, 2 * np.pi, 100)
    base_front_x = cone_cx + r_val * np.cos(t_vals)
    base_front_y = cone_cy + b_val * np.sin(t_vals)

    cone_poly_pts = np.vstack([[cone_cx, cone_apex_y], np.column_stack([base_front_x, base_front_y]), [cone_cx, cone_apex_y]])
    poly_cone = Polygon(cone_poly_pts, closed=True, facecolor=BLUE, edgecolor="none", zorder=2)
    ax.add_patch(poly_cone)

    # Cone outline
    # Left edge: (cone_cx, cone_apex_y) to (cone_cx - r_val, cone_cy)
    ax.plot([cone_cx, cone_cx - r_val], [cone_apex_y, cone_cy], color=DEEP["blue"], lw=2.5, zorder=4)
    # Right edge: (cone_cx, cone_apex_y) to (cone_cx + r_val, cone_cy)
    ax.plot([cone_cx, cone_cx + r_val], [cone_apex_y, cone_cy], color=DEEP["blue"], lw=2.5, zorder=4)

    # Base: front visible solid, back hidden dashed
    t_back = np.linspace(0, np.pi, 100)
    base_back_x = cone_cx + r_val * np.cos(t_back)
    base_back_y = cone_cy + b_val * np.sin(t_back)
    ax.plot(base_front_x, base_front_y, color=DEEP["blue"], lw=2.5, zorder=4)
    ax.plot(base_back_x, base_back_y, color=DEEP["blue"], lw=2.0, linestyle="--", dashes=(4, 4), zorder=3)

    # Apex dot
    ax.plot(cone_cx, cone_apex_y, 'o', color=INK, markersize=5, zorder=5)

    # Slant height l annotation (on left edge)
    mid_slant_x = (cone_cx + (cone_cx - r_val)) / 2 - 0.2
    mid_slant_y = (cone_apex_y + cone_cy) / 2
    ax.text(mid_slant_x, mid_slant_y, "slant height\n$l = R$", fontsize=15, color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec="none", pad=0.2))

    # Base radius r: center to right edge
    ax.plot(cone_cx, cone_cy, 'o', color=INK, markersize=4, zorder=5)
    ax.plot([cone_cx, cone_cx + r_val], [cone_cy, cone_cy], color=INK, lw=1.8, linestyle="--", dashes=(3, 3), zorder=5)
    ax.text(cone_cx + 0.5 * r_val, cone_cy - 0.28, "radius $r$", fontsize=15, color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=0.1))

    # Titles / Subtitles
    ax.text(2.5, 5.5, "2D Sector (Net)", fontsize=17, weight="bold", ha="center", va="center", color=INK)
    ax.text(8.8, 5.5, "3D Cone", fontsize=17, weight="bold", ha="center", va="center", color=INK)

    save(fig, out)
