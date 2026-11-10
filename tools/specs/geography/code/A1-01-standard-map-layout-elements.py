from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.set_aspect('equal')
    ax.axis('off')

    # Border coordinates (neat margin)
    x0, y0, w, h = 6, 6, 88, 68
    x1, y1 = x0 + w, y0 + h

    # Outer border (thick) & Inner border (thin neat line)
    border_outer = patches.Rectangle((x0 - 1.2, y0 - 1.2), w + 2.4, h + 2.4,
                                     linewidth=3.5, edgecolor=INK, facecolor='none', zorder=10)
    border_inner = patches.Rectangle((x0, y0), w, h,
                                     linewidth=1.2, edgecolor=INK, facecolor='white', zorder=0)
    ax.add_patch(border_outer)
    ax.add_patch(border_inner)

    # Faint grid lines across the map (strictly clipped within inner bounds)
    grid_xs = list(range(16, 90, 12))
    grid_ys = list(range(16, 70, 12))

    for gx in grid_xs:
        ax.plot([gx, gx], [y0, y1], color=GREY, lw=0.8, linestyle='--', alpha=0.5, zorder=1)
        # Margin grid ticks / coordinate labels strictly outside the outer margin line
        ax.text(gx, y0 - 2.0, f"{gx:02d}", fontsize=14, ha='center', va='top', color=INK)
        ax.text(gx, y1 + 2.0, f"{gx:02d}", fontsize=14, ha='center', va='bottom', color=INK)

    for gy in grid_ys:
        ax.plot([x0, x1], [gy, gy], color=GREY, lw=0.8, linestyle='--', alpha=0.5, zorder=1)
        # Margin grid ticks / coordinate labels strictly outside the outer margin line
        ax.text(x0 - 2.0, gy, f"{gy:02d}", fontsize=14, ha='right', va='center', color=INK)
        ax.text(x1 + 2.0, gy, f"{gy:02d}", fontsize=14, ha='left', va='center', color=INK)

    # Title: "MAP OF OLU TOWN" at the top
    ax.text(50, y1 - 4.2, "MAP OF OLU TOWN", fontsize=18, fontweight='bold', ha='center', va='center',
            color=INK, zorder=12,
            bbox=dict(boxstyle='square,pad=0.4', facecolor='white', edgecolor=INK, lw=1.5))

    # Winding River (Blue line)
    t = np.linspace(0, 1, 150)
    river_x = (x0 + 1) + (w - 2) * t
    river_y = 52 - 16 * t + 6 * np.sin(2.5 * np.pi * t)
    ax.plot(river_x, river_y, color=DEEP["blue"], lw=3.5, zorder=2)
    ax.text(38, 51, "River Olu", fontsize=14, fontstyle='italic', color=DEEP["blue"], rotation=-10,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.9), zorder=4)

    # Main Road (Red line)
    road_x = np.array([x0 + 10, 32, 50, 68, x1 - 5])
    road_y = np.array([32, 36, 42, 45, 54])
    road_t = np.linspace(0, 1, 100)
    poly_x = np.poly1d(np.polyfit([0, 0.25, 0.5, 0.75, 1.0], road_x, 3))
    poly_y = np.poly1d(np.polyfit([0, 0.25, 0.5, 0.75, 1.0], road_y, 3))
    rx = poly_x(road_t)
    ry = poly_y(road_t)
    ax.plot(rx, ry, color=DEEP["orange"], lw=3.5, zorder=3)
    ax.text(30, 38.5, "Olu - Ilesa Road", fontsize=14, color=DEEP["orange"], rotation=14,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.9), zorder=4)

    # Buildings (Black squares)
    building_locs = [
        (48, 45), (50, 46), (52, 44), (55, 45), (49, 42),
        (57, 48), (60, 47), (59, 51), (62, 50), (65, 52),
        (38, 33), (40, 35), (41, 32), (43, 34),
        (22, 34), (24, 33), (25, 36)
    ]
    for bx, by in building_locs:
        rect = patches.Rectangle((bx - 0.75, by - 0.75), 1.5, 1.5, facecolor=INK, edgecolor='none', zorder=4)
        ax.add_patch(rect)

    # Settlement label
    ax.text(55, 39, "Olu Settlement", fontsize=15, fontweight='bold', ha='center', va='center',
            color=INK, zorder=5,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=GREY, alpha=0.9))

    # North Arrow on the right side pointing up
    na_x, na_y = 86, 60
    arrow = patches.FancyArrow(na_x, na_y - 5.5, 0, 7.5, width=1.1, head_width=3.4, head_length=4.0,
                                length_includes_head=True, facecolor=INK, edgecolor=INK, zorder=12)
    ax.add_patch(arrow)
    ax.text(na_x, na_y + 4.2, "N", fontsize=16, fontweight='bold', ha='center', va='center', color=INK, zorder=12)

    # Key / Legend Box in the bottom left
    kl_w, kl_h = 28, 17
    kl_x, kl_y = x0 + 2, y0 + 2
    key_box = patches.Rectangle((kl_x, kl_y), kl_w, kl_h, facecolor='white', edgecolor=INK, lw=1.4, zorder=8)
    ax.add_patch(key_box)
    ax.text(kl_x + kl_w / 2, kl_y + kl_h - 2.5, "KEY / LEGEND", fontsize=14, fontweight='bold',
            ha='center', va='center', color=INK, zorder=9)

    # Legend item 1: Road (red line)
    ax.plot([kl_x + 2, kl_x + 8], [kl_y + 10.5, kl_y + 10.5], color=DEEP["orange"], lw=3.2, zorder=9)
    ax.text(kl_x + 10, kl_y + 10.5, "Road", fontsize=14, va='center', color=INK, zorder=9)

    # Legend item 2: River (blue line)
    ax.plot([kl_x + 2, kl_x + 8], [kl_y + 6.8, kl_y + 6.8], color=DEEP["blue"], lw=3.2, zorder=9)
    ax.text(kl_x + 10, kl_y + 6.8, "River", fontsize=14, va='center', color=INK, zorder=9)

    # Legend item 3: Buildings (black square)
    b_key = patches.Rectangle((kl_x + 4.2, kl_y + 2.4), 1.6, 1.6, facecolor=INK, edgecolor='none', zorder=9)
    ax.add_patch(b_key)
    ax.text(kl_x + 10, kl_y + 3.2, "Buildings", fontsize=14, va='center', color=INK, zorder=9)

    # Scale in the bottom right (linear scale 0 to 5 km)
    sc_w, sc_h = 32, 12
    sc_x, sc_y = x1 - sc_w - 2, y0 + 2
    scale_box = patches.Rectangle((sc_x, sc_y), sc_w, sc_h, facecolor='white', edgecolor=INK, lw=1.4, zorder=8)
    ax.add_patch(scale_box)
    ax.text(sc_x + sc_w / 2, sc_y + sc_h - 2.5, "SCALE", fontsize=14, fontweight='bold',
            ha='center', va='center', color=INK, zorder=9)

    # Alternating black and white blocks from 0 to 5 km
    sx_start = sc_x + 3.5
    sy = sc_y + 3.5
    block_w = 4.8
    block_h = 1.6
    for i in range(5):
        fc = INK if i % 2 == 0 else 'white'
        blk = patches.Rectangle((sx_start + i * block_w, sy), block_w, block_h,
                                facecolor=fc, edgecolor=INK, lw=1, zorder=9)
        ax.add_patch(blk)
        ax.text(sx_start + i * block_w, sy + 2.2, f"{i}", fontsize=14, ha='center', va='bottom', color=INK, zorder=9)
    ax.text(sx_start + 5 * block_w, sy + 2.2, "5 km", fontsize=14, ha='center', va='bottom', color=INK, zorder=9)

    save(fig, out)
    plt.close(fig)
