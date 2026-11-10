from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 7.5)
    ax.axis("off")

    # Perspective vectors: X is rightwards, Y is upwards, Z along perspective vector
    dx_p, dy_p = 1.6, 1.2

    def proj(x, y, z):
        return x + z * dx_p, y + z * dy_p

    def polygon_coords(pts):
        return [proj(*p) for p in pts]

    # Plate dimensions
    y_bot = 1.0
    y_top = 3.8
    x0, x1 = 1.2, 6.2
    z0, z1 = 0.0, 2.2
    t = 0.15  # plate thickness

    # 1. Bottom Plate
    bot_top_face = polygon_coords([(x0, y_bot, z0), (x1, y_bot, z0), (x1, y_bot, z1), (x0, y_bot, z1)])
    bot_front_face = polygon_coords([(x0, y_bot - t, z0), (x1, y_bot - t, z0), (x1, y_bot, z0), (x0, y_bot, z0)])
    bot_right_face = polygon_coords([(x1, y_bot - t, z0), (x1, y_bot - t, z1), (x1, y_bot, z1), (x1, y_bot, z0)])

    ax.add_patch(patches.Polygon(bot_top_face, facecolor=CREAM, edgecolor=DEEP["blue"], lw=2, zorder=2))
    ax.add_patch(patches.Polygon(bot_front_face, facecolor=GREY, edgecolor=DEEP["blue"], lw=1.5, zorder=2))
    ax.add_patch(patches.Polygon(bot_right_face, facecolor=GREY, edgecolor=DEEP["blue"], lw=1.5, zorder=2))

    # Overlapping Area A shading on bottom plate
    area_face = polygon_coords([(x0, y_bot + 0.01, z0), (x1, y_bot + 0.01, z0), (x1, y_bot + 0.01, z1), (x0, y_bot + 0.01, z1)])
    ax.add_patch(patches.Polygon(area_face, facecolor=BLUE, alpha=0.35, edgecolor=DEEP["blue"], lw=1.8, linestyle="--", zorder=3))

    # 2. Dielectric slab partially inserted
    xd0, xd1 = 3.2, 7.8
    yd0, yd1 = y_bot + 0.05, y_top - 0.05
    zd0, zd1 = 0.3, 2.1

    d_front = polygon_coords([(xd0, yd0, zd0), (xd1, yd0, zd0), (xd1, yd1, zd0), (xd0, yd1, zd0)])
    d_top = polygon_coords([(xd0, yd1, zd0), (xd1, yd1, zd0), (xd1, yd1, zd1), (xd0, yd1, zd1)])
    d_left = polygon_coords([(xd0, yd0, zd0), (xd0, yd0, zd1), (xd0, yd1, zd1), (xd0, yd1, zd0)])
    d_right = polygon_coords([(xd1, yd0, zd0), (xd1, yd0, zd1), (xd1, yd1, zd1), (xd1, yd1, zd0)])

    ax.add_patch(patches.Polygon(d_left, facecolor=ORANGE, alpha=0.8, edgecolor=DEEP["orange"], lw=1.5, zorder=4))
    ax.add_patch(patches.Polygon(d_front, facecolor=ORANGE, alpha=0.6, edgecolor=DEEP["orange"], lw=2, zorder=4))
    ax.add_patch(patches.Polygon(d_top, facecolor=CREAM, alpha=0.9, edgecolor=DEEP["orange"], lw=1.8, zorder=4))
    ax.add_patch(patches.Polygon(d_right, facecolor=ORANGE, alpha=0.85, edgecolor=DEEP["orange"], lw=1.5, zorder=4))

    # 3. Top Plate (semi-transparent to see dielectric and area beneath)
    top_face = polygon_coords([(x0, y_top, z0), (x1, y_top, z0), (x1, y_top, z1), (x0, y_top, z1)])
    top_front = polygon_coords([(x0, y_top - t, z0), (x1, y_top - t, z0), (x1, y_top, z0), (x0, y_top, z0)])
    top_right = polygon_coords([(x1, y_top - t, z0), (x1, y_top - t, z1), (x1, y_top, z1), (x1, y_top, z0)])

    ax.add_patch(patches.Polygon(top_face, facecolor=BLUE, alpha=0.45, edgecolor=DEEP["blue"], lw=2.2, zorder=5))
    ax.add_patch(patches.Polygon(top_front, facecolor=GREY, alpha=0.7, edgecolor=DEEP["blue"], lw=1.5, zorder=5))
    ax.add_patch(patches.Polygon(top_right, facecolor=GREY, alpha=0.7, edgecolor=DEEP["blue"], lw=1.5, zorder=5))

    # 4. Connecting terminals / wires
    # Shift terminals slightly to avoid formula box
    p_top_center = proj(x0 + 0.4, y_top, (z0 + z1) / 2)
    p_bot_center = proj(x0 + 0.4, y_bot - t, (z0 + z1) / 2)
    ax.plot([p_top_center[0], p_top_center[0]], [p_top_center[1], p_top_center[1] + 1.2], color=INK, lw=2, zorder=6)
    ax.plot([p_top_center[0]], [p_top_center[1] + 1.2], marker="o", markersize=6, color=INK, zorder=7)

    ax.plot([p_bot_center[0], p_bot_center[0]], [p_bot_center[1], p_bot_center[1] - 1.2], color=INK, lw=2, zorder=6)
    ax.plot([p_bot_center[0]], [p_bot_center[1] - 1.2], marker="o", markersize=6, color=INK, zorder=7)

    # 5. Annotations and Labels
    # Label: Distance (d)
    x_gap = x0 - 0.3
    p_gap_top = proj(x_gap, y_top, z0)
    p_gap_bot = proj(x_gap, y_bot, z0)

    # Extension tick marks for d
    ax.plot([proj(x0, y_top, z0)[0], p_gap_top[0] - 0.2], [proj(x0, y_top, z0)[1], p_gap_top[1]], color=GREY, lw=1.2, ls=":")
    ax.plot([proj(x0, y_bot, z0)[0], p_gap_bot[0] - 0.2], [proj(x0, y_bot, z0)[1], p_gap_bot[1]], color=GREY, lw=1.2, ls=":")

    # Double-headed arrow for distance d
    ax.annotate("", xy=p_gap_top, xytext=p_gap_bot,
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8, shrinkA=0, shrinkB=0))
    ax.text(p_gap_top[0] - 0.4, (p_gap_top[1] + p_gap_bot[1]) / 2, "Distance (d)",
            ha="right", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Label: Area (A)
    p_area_pt = proj(2.2, y_bot, 0.7)
    ax.annotate("Area (A)", xy=p_area_pt, xytext=(0.5, 0.2),
                fontsize=15, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, connectionstyle="arc3,rad=-0.1"),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Label: Dielectric (permittivity ε)
    p_diel_pt = proj(xd1 - 0.3, yd1, 0.9)
    ax.annotate("Dielectric (permittivity ε)", xy=p_diel_pt, xytext=(8.0, 5.7),
                fontsize=15, color=INK, weight="bold", ha="center", zorder=10,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, connectionstyle="arc3,rad=-0.15"),
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.3"))

    # Insertion arrow for dielectric block
    arrow_start = proj(xd1 + 0.8, (yd0 + yd1) / 2, (zd0 + zd1) / 2)
    arrow_end = proj(xd1 + 0.1, (yd0 + yd1) / 2, (zd0 + zd1) / 2)
    ax.annotate("", xy=arrow_end, xytext=arrow_start,
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5))

    # Title & Capacitance formula
    ax.text(5.0, 6.8, "Parallel Plate Capacitor: Factors Affecting Capacitance",
            ha="center", va="center", fontsize=16, weight="bold", color=INK)
    ax.text(5.0, 6.1, r"$C = \frac{\varepsilon A}{d}$",
            ha="center", va="center", fontsize=18, color=INK, zorder=10,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"))

    save(fig, out)
