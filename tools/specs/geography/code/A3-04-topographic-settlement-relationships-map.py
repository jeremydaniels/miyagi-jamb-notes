from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Border for the map extract
    map_border = patches.Rectangle((0, 0), 100, 100, fill=False, edgecolor=INK, linewidth=2)
    ax.add_patch(map_border)

    # 1. Contours
    contour_color = '#C29A6B'  # Topographic contour brown
    contour_lw = 1.3

    # Generate synthetic elevation grid
    nx, ny = 200, 200
    x = np.linspace(0, 100, nx)
    y = np.linspace(0, 100, ny)
    X, Y = np.meshgrid(x, y)

    # Steep north ridge, steep south ridge, gentle valley floor
    Z_north = 180 * (np.clip((Y - 55) / 35, 0, 1) ** 1.6)
    Z_south = 160 * (np.clip((35 - Y + (X - 40) * 0.4) / 40, 0, 1) ** 1.5)
    Z_gentle = 15 * np.sin(X / 25) + 10 * np.cos(Y / 25)
    Z = Z_north + Z_south + Z_gentle + 20

    levels = np.arange(20, 180, 15)
    ax.contour(X, Y, Z, levels=levels, colors=contour_color, linewidths=contour_lw, alpha=0.85)
    ax.contour(X, Y, Z, levels=levels[::3], colors=contour_color, linewidths=2.0, alpha=0.9)

    # 2. Forest on steep hills (North area)
    np.random.seed(42)
    tree_xs = np.random.uniform(5, 70, 32)
    tree_ys = np.random.uniform(70, 93, 32)
    for tx, ty in zip(tree_xs, tree_ys):
        if ty > 68:
            ax.plot([tx, tx], [ty - 1.2, ty], color='#3E6B48', lw=1.5, zorder=3)
            foliage = patches.Circle((tx, ty + 0.6), radius=1.3, facecolor=GREEN, edgecolor='#3E6B48', lw=1.2, zorder=4)
            ax.add_patch(foliage)

    # Forest label
    ax.text(38, 92, "Coniferous Forest\n(Steep slopes, no settlements)", fontsize=14, 
            ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1), zorder=6)

    # 3. Meandering River
    t = np.linspace(0, 100, 300)
    def river_func(val):
        return 28 + 0.45 * val + 9 * np.sin(val * 0.12) - 4 * np.cos(val * 0.05)

    rx = t
    ry = river_func(rx)
    ax.plot(rx, ry, color=DEEP["blue"], linewidth=5.5, zorder=5, solid_capstyle='round')

    # River flow arrow
    ax.annotate("", xy=(85, river_func(85)), xytext=(75, river_func(75)),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5), zorder=6)

    # 4. Road network
    # Polynomial interpolation using only numpy (degree 3)
    road_sample_x = np.array([5, 20, 35, 48, 62, 78, 95], dtype=float)
    bridge_y = float(river_func(48))
    road_sample_y = np.array([20, 27, 33, bridge_y, 49, 56, 62], dtype=float)
    road_poly = np.poly1d(np.polyfit(road_sample_x, road_sample_y, deg=3))

    r_dense_x = np.linspace(5, 95, 200)
    r_dense_y = road_poly(r_dense_x)

    # Road line
    ax.plot(r_dense_x, r_dense_y, color=INK, linewidth=4.0, zorder=6)
    ax.plot(r_dense_x, r_dense_y, color=ORANGE, linewidth=2.4, zorder=7)

    # Bridge symbol at crossing (x=48, bridge_y)
    bx, by = 48.0, bridge_y
    road_deriv = road_poly.deriv()
    b_angle = np.arctan(road_deriv(bx))
    perp = b_angle + np.pi / 2
    dx, dy = 2.5 * np.cos(perp), 2.5 * np.sin(perp)
    ax.plot([bx - dx, bx + dx], [by - dy, by + dy], color=INK, lw=4, zorder=8)
    p_dx, p_dy = 1.8 * np.cos(b_angle), 1.8 * np.sin(b_angle)
    ax.plot([bx - p_dx - dx, bx + p_dx - dx], [by - p_dy - dy, by + p_dy - dy], color=INK, lw=2.5, zorder=9)
    ax.plot([bx - p_dx + dx, bx + p_dx + dx], [by - p_dy + dy, by + p_dy + dy], color=INK, lw=2.5, zorder=9)

    # 5. Linear Settlement along the road (northeast of bridge, ~ x=62 to 82)
    for lx in np.linspace(62, 82, 10):
        ly = float(road_poly(lx))
        normal_angle = np.arctan(road_deriv(lx)) + np.pi / 2
        for side in [-1, 1]:
            hx = lx + side * 1.8 * np.cos(normal_angle)
            hy = ly + side * 1.8 * np.sin(normal_angle)
            rect = patches.Rectangle((hx - 0.7, hy - 0.7), 1.4, 1.4, facecolor=INK, edgecolor=None, zorder=8)
            ax.add_patch(rect)

    # 6. Nucleated Settlement on gently sloping ground (dry point) away from flood plain
    nuc_center_x, nuc_center_y = 22, 54
    np.random.seed(101)
    for _ in range(16):
        ox = np.random.normal(0, 3.0)
        oy = np.random.normal(0, 2.8)
        sq = patches.Rectangle((nuc_center_x + ox - 0.8, nuc_center_y + oy - 0.8), 1.6, 1.6, 
                               facecolor=INK, edgecolor=None, zorder=8)
        ax.add_patch(sq)

    # Secondary track connecting nucleated settlement to main road
    track_x = [nuc_center_x, 26, 32, 35]
    track_y = [nuc_center_y - 2, 45, 38, float(road_poly(35))]
    ax.plot(track_x, track_y, color=INK, linewidth=1.5, linestyle='--', zorder=6)

    # 7. Text Annotations & Callouts
    ax.annotate("Nucleated Settlement\n• Clustered on gentle slope\n• Dry-point site (above flood risk)",
                xy=(nuc_center_x + 3, nuc_center_y + 2), xytext=(28, 72),
                fontsize=14, color=INK, ha='left', va='center',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=10)

    ax.annotate("Linear Settlement\n• Houses align along main road\n• Valley-floor communication route",
                xy=(74, float(road_poly(74)) + 2.5), xytext=(65, 36),
                fontsize=14, color=INK, ha='center', va='top',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=10)

    ax.annotate("Bridge\n(River crossing point)",
                xy=(bx, by), xytext=(38, 14),
                fontsize=14, color=INK, ha='center', va='top',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=10)

    ax.annotate("Wide Valley Floor\n(Widely spaced contours,\nmeandering river floodplain)",
                xy=(18, 30), xytext=(6, 10),
                fontsize=14, color=INK, ha='left', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=10)

    ax.annotate("Steep Hills\n(Closely spaced contours)",
                xy=(88, 15), xytext=(68, 8),
                fontsize=14, color=INK, ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=10)

    # Title block
    ax.text(50, 96.5, "Topographical Relationships: Physical Landscape & Settlement Patterns",
            fontsize=16, fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(boxstyle="square,pad=0.4", fc="white", ec=INK, lw=1.5), zorder=10)

    # Legend / Key in upper right corner
    legend_bg = patches.Rectangle((73, 76), 25, 18, facecolor="white", edgecolor=GREY, lw=1.2, zorder=9)
    ax.add_patch(legend_bg)
    ax.text(85.5, 91.5, "Key", fontsize=15, fontweight='bold', ha='center', color=INK, zorder=10)
    
    # Legend items
    ax.plot([75, 80], [88, 88], color=contour_color, lw=2, zorder=10)
    ax.text(82, 88, "Contour (15 m)", fontsize=14, va='center', color=INK, zorder=10)

    ax.plot([75, 80], [84.5, 84.5], color=DEEP["blue"], lw=3.5, zorder=10)
    ax.text(82, 84.5, "River", fontsize=14, va='center', color=INK, zorder=10)

    ax.plot([75, 80], [81, 81], color=INK, lw=3.8, zorder=9)
    ax.plot([75, 80], [81, 81], color=ORANGE, lw=2.5, zorder=10)
    ax.text(82, 81, "Main road", fontsize=14, va='center', color=INK, zorder=10)

    sq_leg = patches.Rectangle((76.5, 77.2), 2, 2, facecolor=INK, edgecolor=None, zorder=10)
    ax.add_patch(sq_leg)
    ax.text(82, 78.2, "Building", fontsize=14, va='center', color=INK, zorder=10)

    save(fig, out)
