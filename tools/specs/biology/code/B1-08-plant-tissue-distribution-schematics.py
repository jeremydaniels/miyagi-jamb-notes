from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_axes([0.02, 0.08, 0.96, 0.88])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.set_aspect("equal")
    ax.axis("off")

    # Palette
    RED_XYLEM = "#E05344"
    RED_XYLEM_LINE = "#B0281A"
    GREEN_COLL = GREEN
    GREEN_COLL_LINE = DEEP["green"]
    PINK_SCLER = PINK
    PINK_SCLER_LINE = DEEP["pink"]
    BROWN_ENDO = "#8D5B4C"
    PALE_PITH = CREAM
    OUTLINE_GREY = "#4A5568"

    # -------------------------------------------------------------
    # 1. ROOT
    # -------------------------------------------------------------
    r_cx, r_cy, r_rad = 2.4, 4.4, 1.8

    # Cortex / Outer circle
    root_bg = plt.Circle((r_cx, r_cy), r_rad, facecolor="white", edgecolor=OUTLINE_GREY, lw=1.8, zorder=1)
    ax.add_patch(root_bg)

    # Endodermis ring
    endo_rad = 0.65
    endo_circle = plt.Circle((r_cx, r_cy), endo_rad, facecolor="#F7FAFC", edgecolor=BROWN_ENDO, lw=2.2, ls="-", zorder=2)
    ax.add_patch(endo_circle)

    # Star-shaped xylem core (4-point star / cross)
    star_angles = np.linspace(0, 2*np.pi, 9)[:-1]
    star_radii = [0.48, 0.16, 0.48, 0.16, 0.48, 0.16, 0.48, 0.16]
    star_x = r_cx + star_radii * np.cos(star_angles)
    star_y = r_cy + star_radii * np.sin(star_angles)
    star_poly = plt.Polygon(np.column_stack([star_x, star_y]), closed=True,
                            facecolor=RED_XYLEM, edgecolor=RED_XYLEM_LINE, lw=1.5, zorder=3)
    ax.add_patch(star_poly)

    # -------------------------------------------------------------
    # 2. STEM
    # -------------------------------------------------------------
    s_cx, s_cy, s_rad = 6.8, 4.4, 1.8

    # Epidermis
    stem_bg = plt.Circle((s_cx, s_cy), s_rad, facecolor="white", edgecolor=OUTLINE_GREY, lw=1.8, zorder=1)
    ax.add_patch(stem_bg)

    # Collenchyma hypodermis ring (thin ring just under edge)
    coll_ring = plt.Circle((s_cx, s_cy), s_rad - 0.05, facecolor="none", edgecolor=GREEN_COLL_LINE,
                           lw=3.5, zorder=2)
    ax.add_patch(coll_ring)

    # Pith
    pith_circle = plt.Circle((s_cx, s_cy), 0.95, facecolor=PALE_PITH, edgecolor="none", zorder=2)
    ax.add_patch(pith_circle)

    # Vascular bundles (ring of bundles)
    num_bundles = 8
    bundle_r = 1.25
    b_angles = np.linspace(0, 2*np.pi, num_bundles, endpoint=False) + np.pi/8

    for angle in b_angles:
        bx = s_cx + bundle_r * np.cos(angle)
        by = s_cy + bundle_r * np.sin(angle)
        
        # Sclerenchyma cap (outer part of bundle)
        cap_x = s_cx + (bundle_r + 0.18) * np.cos(angle)
        cap_y = s_cy + (bundle_r + 0.18) * np.sin(angle)
        cap = plt.Circle((cap_x, cap_y), 0.16, facecolor=PINK_SCLER, edgecolor=PINK_SCLER_LINE, lw=1.2, zorder=4)
        ax.add_patch(cap)

        # Xylem (inner part of bundle, wedge/oval)
        xyl_x = s_cx + (bundle_r - 0.14) * np.cos(angle)
        xyl_y = s_cy + (bundle_r - 0.14) * np.sin(angle)
        xyl = plt.Circle((xyl_x, xyl_y), 0.16, facecolor=RED_XYLEM, edgecolor=RED_XYLEM_LINE, lw=1.2, zorder=3)
        ax.add_patch(xyl)

    # -------------------------------------------------------------
    # 3. LEAF
    # -------------------------------------------------------------
    l_cx, l_cy = 11.2, 4.4

    # Leaf blade and midrib outline
    verts = [
        (9.2, 4.5),      # left blade tip
        (10.5, 4.5),     # left blade to midrib top
        (10.8, 4.6),
        (11.2, 4.6),     # top slight ridge
        (11.6, 4.6),
        (11.9, 4.5),     # right blade from midrib top
        (13.2, 4.5),     # right blade tip
        (13.2, 4.3),     # right blade lower tip
        (12.0, 4.3),     # right blade lower to midrib
        (11.8, 3.8),     # midrib bottom curve right
        (11.2, 3.2),     # midrib bottom lowest point
        (10.6, 3.8),     # midrib bottom curve left
        (10.4, 4.3),     # midrib left to lower blade
        (9.2, 4.3),      # left blade lower tip
        (9.2, 4.5),      # close
    ]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.CURVE3, Path.CURVE3,
        Path.CURVE3, Path.CURVE3,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CURVE3, Path.CURVE3,
        Path.CURVE3, Path.CURVE3,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    leaf_path = Path(verts, codes)
    leaf_patch = patches.PathPatch(leaf_path, facecolor="#FCFDFD", edgecolor=OUTLINE_GREY, lw=1.8, zorder=2)
    ax.add_patch(leaf_patch)

    # Collenchyma patches in midrib (upper and lower)
    top_coll = patches.Ellipse((11.2, 4.45), 0.5, 0.22, facecolor=GREEN_COLL, edgecolor=GREEN_COLL_LINE, lw=1.2, zorder=3)
    bot_coll = patches.Ellipse((11.2, 3.5), 0.65, 0.35, facecolor=GREEN_COLL, edgecolor=GREEN_COLL_LINE, lw=1.2, zorder=3)
    ax.add_patch(top_coll)
    ax.add_patch(bot_coll)

    # Midrib bundle: xylem patch
    mid_xyl = patches.Ellipse((11.2, 4.08), 0.45, 0.22, facecolor=RED_XYLEM, edgecolor=RED_XYLEM_LINE, lw=1.2, zorder=4)
    ax.add_patch(mid_xyl)

    # Small veins along the blade
    vein_xs = [9.5, 9.9, 10.3, 12.1, 12.5, 12.9]
    for vx in vein_xs:
        v = patches.Ellipse((vx, 4.4), 0.09, 0.14, facecolor=RED_XYLEM, edgecolor=RED_XYLEM_LINE, lw=1.0, zorder=4)
        ax.add_patch(v)

    # -------------------------------------------------------------
    # HEADINGS (root, stem, leaf)
    # -------------------------------------------------------------
    ax.text(r_cx, 6.7, "Root", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)
    ax.text(s_cx, 6.7, "Stem", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)
    ax.text(l_cx, 6.7, "Leaf", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)

    # -------------------------------------------------------------
    # ANNOTATIONS / LABELS
    # -------------------------------------------------------------
    # Root labels
    # Central xylem core
    ax.annotate("central xylem core", xy=(r_cx - 0.15, r_cy + 0.15), xytext=(r_cx - 1.2, 5.8),
                fontsize=12, color=INK, ha="right", va="bottom",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))
    
    # Endodermis
    ax.annotate("endodermis", xy=(r_cx + endo_rad * np.cos(-np.pi/4), r_cy + endo_rad * np.sin(-np.pi/4)),
                xytext=(r_cx + 1.1, 3.3),
                fontsize=12, color=INK, ha="left", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Stem labels
    # Collenchyma
    ax.annotate("collenchyma", xy=(s_cx - s_rad + 0.05, s_cy + 0.6), xytext=(s_cx - 1.9, 5.8),
                fontsize=12, color=INK, ha="right", va="bottom",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Sclerenchyma (fibre cap)
    cap_target_x = s_cx + (bundle_r + 0.18) * np.cos(np.pi/8)
    cap_target_y = s_cy + (bundle_r + 0.18) * np.sin(np.pi/8)
    ax.annotate("sclerenchyma\n(fibre cap)", xy=(cap_target_x, cap_target_y), xytext=(s_cx + 1.6, 5.6),
                fontsize=12, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Xylem
    xyl_target_x = s_cx + (bundle_r - 0.14) * np.cos(-np.pi/8)
    xyl_target_y = s_cy + (bundle_r - 0.14) * np.sin(-np.pi/8)
    ax.annotate("xylem", xy=(xyl_target_x, xyl_target_y), xytext=(s_cx + 1.6, 3.8),
                fontsize=12, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Pith
    ax.annotate("pith", xy=(s_cx, s_cy), xytext=(s_cx - 1.1, 2.6),
                fontsize=12, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Leaf labels
    # Midrib
    ax.annotate("midrib", xy=(11.2, 3.3), xytext=(11.2, 2.3),
                fontsize=12, color=INK, ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Vein
    ax.annotate("vein", xy=(12.5, 4.45), xytext=(12.7, 5.5),
                fontsize=12, color=INK, ha="left", va="bottom",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # Collenchyma in leaf
    ax.annotate("collenchyma", xy=(11.0, 3.55), xytext=(9.7, 2.7),
                fontsize=12, color=INK, ha="right", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec="none", pad=1))

    # -------------------------------------------------------------
    # COLOUR KEY (Bottom)
    # -------------------------------------------------------------
    legend_y = 1.0
    box_w, box_h = 0.45, 0.28
    
    # Item 1: Collenchyma
    ax.add_patch(patches.Rectangle((2.4, legend_y - box_h/2), box_w, box_h,
                                   facecolor=GREEN_COLL, edgecolor=GREEN_COLL_LINE, lw=1.2))
    ax.text(3.05, legend_y, "collenchyma", fontsize=12.5, va="center", ha="left", color=INK)

    # Item 2: Sclerenchyma / fibres
    ax.add_patch(patches.Rectangle((5.8, legend_y - box_h/2), box_w, box_h,
                                   facecolor=PINK_SCLER, edgecolor=PINK_SCLER_LINE, lw=1.2))
    ax.text(6.45, legend_y, "sclerenchyma / fibres", fontsize=12.5, va="center", ha="left", color=INK)

    # Item 3: Xylem
    ax.add_patch(patches.Rectangle((9.9, legend_y - box_h/2), box_w, box_h,
                                   facecolor=RED_XYLEM, edgecolor=RED_XYLEM_LINE, lw=1.2))
    ax.text(10.55, legend_y, "xylem", fontsize=12.5, va="center", ha="left", color=INK)

    save(fig, out)
