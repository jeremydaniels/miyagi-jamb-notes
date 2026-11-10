from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Grid lines to mimic an OS topographical map extract
    for x in range(1, 12):
        ax.axvline(x, color=GREY, lw=0.6, alpha=0.35, zorder=1)
    for y in range(1, 10):
        ax.axhline(y, color=GREY, lw=0.6, alpha=0.35, zorder=1)

    # 1. Forested steep hills background tint (north area)
    hill_poly = np.array([
        [0, 10], [12, 10], [12, 6.2],
        [10, 6.4], [8, 6.6], [6, 6.7], [4, 6.5], [2, 6.3], [0, 6.2]
    ])
    ax.fill(hill_poly[:, 0], hill_poly[:, 1], color=GREEN, alpha=0.22, zorder=2)

    # 2. Contour lines
    x_c = np.linspace(0, 12, 300)

    # 300m
    x_300 = np.linspace(5.0, 12, 200)
    y_300 = 8.8 + 0.25 * np.sin(x_300 * 0.8)
    ax.plot(x_300, y_300, color='#b07230', lw=1.5, zorder=3)
    ax.text(x_300[150], y_300[150], "300m", fontsize=14, color='#7a4413',
            ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=1.5), zorder=4)

    # Other steep contours running across
    steep_contours = [
        (250, 8.2, 0.3, 0.8, 250),
        (200, 7.5, 0.25, 0.9, 100),
        (150, 6.8, 0.2, 1.0, 220),
        (100, 6.1, 0.2, 0.7, 15)
    ]
    for elev, base_y, amp, freq, idx in steep_contours:
        y_vals = base_y + amp * np.sin(x_c * freq + elev * 0.05)
        ax.plot(x_c, y_vals, color='#b07230', lw=1.5, zorder=3)
        ax.text(x_c[idx], y_vals[idx], f"{elev}m", fontsize=14, color='#7a4413',
                ha='center', va='center',
                bbox=dict(fc='white', ec='none', pad=1.5), zorder=4)

    # Gentle valley contours (widely spaced: 50m, 40m)
    y_50 = 4.8 + 0.2 * np.sin(x_c * 0.5)
    ax.plot(x_c, y_50, color='#c28242', lw=1.2, ls='--', zorder=3)
    ax.text(x_c[260], y_50[260], "50m", fontsize=14, color='#8c531b',
            ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=1.5), zorder=4)

    y_40 = 1.9 + 0.2 * np.cos(x_c * 0.4)
    ax.plot(x_c, y_40, color='#c28242', lw=1.2, ls='--', zorder=3)
    ax.text(x_c[180], y_40[180], "40m", fontsize=14, color='#8c531b',
            ha='center', va='center',
            bbox=dict(fc='white', ec='none', pad=1.5), zorder=4)

    # 3. Forest Tree Symbols on Steep Hill
    tree_locs = [
        (5.5, 8.6), (7.0, 8.9), (8.5, 8.8), (10.5, 8.7),
        (1.2, 7.7), (2.8, 7.8), (4.5, 7.5), (6.2, 7.8), (7.8, 7.6), (9.3, 7.9), (10.8, 7.7),
        (1.5, 6.7), (3.8, 6.6), (5.2, 6.7), (7.0, 6.7), (9.6, 6.6), (10.4, 6.7)
    ]
    for tx, ty in tree_locs:
        ax.plot([tx, tx], [ty - 0.18, ty], color='#2d5a27', lw=1.8, zorder=4)
        ax.scatter([tx], [ty + 0.06], s=75, color='#2d5a27', marker='^', zorder=5)

    # 4. Main Road
    road_x = np.linspace(0, 12, 300)
    def road_func(x):
        return 4.2 - 0.12 * x
    road_y = road_func(road_x)

    # 5. Meandering River
    bx = 8.5
    by = road_func(bx)
    t = np.linspace(0, 12, 400)
    def river_func(x):
        return (by + (x - bx) * 0.4
                + 0.7 * np.sin((x - bx) * 1.1)
                - 0.3 * np.sin((x - bx) * 2.3))

    river_y = river_func(t)
    ax.plot(t, river_y, color=DEEP["blue"], lw=5.5, zorder=6)

    # River flow arrow
    ax.annotate("", xy=(5.2, river_func(5.2)), xytext=(4.4, river_func(4.4)),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.8), zorder=7)

    # Draw Road
    ax.plot(road_x, road_y, color='#d95f02', lw=3.8, zorder=7)

    # 6. Bridge
    road_angle = np.arctan(-0.12)
    perp_angle = road_angle + np.pi / 2
    parapet_len = 0.45
    dx = parapet_len * np.cos(perp_angle)
    dy = parapet_len * np.sin(perp_angle)
    spacing = 0.22
    sx = spacing * np.cos(road_angle)
    sy = spacing * np.sin(road_angle)

    ax.plot([bx - sx - dx, bx - sx + dx], [by - sy - dy, by - sy + dy], color=INK, lw=3.5, zorder=11)
    ax.plot([bx + sx - dx, bx + sx + dx], [by + sy - dy, by + sy + dy], color=INK, lw=3.5, zorder=11)

    # 7. Linear Settlement
    for lx in np.linspace(1.0, 5.4, 15):
        ly = road_func(lx)
        side = 0.25 if int(lx * 3.5) % 2 == 0 else -0.25
        sq = patches.Rectangle((lx - 0.1, ly + side - 0.1), 0.2, 0.2,
                               facecolor=INK, edgecolor='none', zorder=9)
        ax.add_patch(sq)

    # 8. Nucleated Settlement
    np.random.seed(42)
    nuc_center_x, nuc_center_y = 10.0, 1.6
    for _ in range(25):
        ox = np.random.normal(0, 0.45)
        oy = np.random.normal(0, 0.38)
        sq = patches.Rectangle((nuc_center_x + ox - 0.1, nuc_center_y + oy - 0.1), 0.2, 0.2,
                               facecolor=INK, edgecolor='none', zorder=9)
        ax.add_patch(sq)
    ax.text(nuc_center_x, nuc_center_y, "+", fontsize=20, fontweight='bold',
            color=INK, ha='center', va='center', zorder=10)

    ax.plot([bx + 0.3, 9.4, nuc_center_x], [by - 0.05, 2.3, nuc_center_y + 0.4],
            color='#d95f02', lw=2.2, ls='--', zorder=6)

    # 9. Annotations
    bbox_style = dict(boxstyle='round,pad=0.3', fc='white', ec=GREY, lw=1)

    ax.annotate("Steep hills (forested,\nno settlements)",
                xy=(7.2, 7.8), xytext=(7.5, 9.1),
                fontsize=14, fontweight='bold', color=INK, ha='center',
                bbox=bbox_style, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                zorder=14)

    ax.annotate("Meandering river in wide valley\n(widely spaced contours)",
                xy=(2.8, river_func(2.8)), xytext=(2.8, 1.2),
                fontsize=14, color=INK, ha='center',
                bbox=bbox_style, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                zorder=14)

    ax.annotate("Linear settlement along\nmain road through valley",
                xy=(3.2, road_func(3.2) + 0.3), xytext=(3.2, 5.5),
                fontsize=14, color=INK, ha='center',
                bbox=bbox_style, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                zorder=14)

    ax.annotate("Bridge crossing river",
                xy=(bx, by), xytext=(7.2, 4.4),
                fontsize=14, fontweight='bold', color=INK, ha='center',
                bbox=bbox_style, arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                zorder=14)

    ax.annotate("Nucleated settlement (dry point:\ncluster away from flood plain)",
                xy=(nuc_center_x, nuc_center_y + 0.2), xytext=(7.5, 1.0),
                fontsize=14, color=INK, ha='center',
                bbox=bbox_style, arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                zorder=14)

    # 10. Map Title & North Arrow
    ax.text(0.5, 9.35, "Topographical Settlement & Relief Relationships",
            fontsize=16, fontweight='bold', color=INK, va='center',
            bbox=dict(boxstyle='square,pad=0.45', fc='white', ec=INK, lw=1.3),
            zorder=15)

    ax.annotate("", xy=(11.3, 9.3), xytext=(11.3, 8.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2), zorder=15)
    ax.text(11.3, 9.55, "N", fontsize=15, fontweight='bold', color=INK, 
            ha='center', va='center', bbox=dict(boxstyle='circle,pad=0.2', fc='white', ec=GREY, lw=1), zorder=15)

    # Map Border
    rect = patches.Rectangle((0, 0), 12, 10, linewidth=2, edgecolor=INK, facecolor='none', zorder=20)
    ax.add_patch(rect)

    save(fig, out)
    plt.close(fig)
