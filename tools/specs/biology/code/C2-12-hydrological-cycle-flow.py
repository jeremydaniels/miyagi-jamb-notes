from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # 1. Terrain Profile (coast at x=3.5, rising inland across hills to high forest plateau)
    x_terrain = np.linspace(3.5, 15, 300)
    y_terrain = (
        2.0
        + 0.6 * (x_terrain - 3.5) / 11.5
        + 1.3 * np.exp(-((x_terrain - 7.2) / 1.7) ** 2)
        + 0.9 * np.exp(-((x_terrain - 12.8) / 2.3) ** 2)
    )

    # Soil background
    ground_poly = [(3.5, 2.0)] + list(zip(x_terrain, y_terrain)) + [(15, 0), (3.5, 0)]
    poly_ground = patches.Polygon(ground_poly, closed=True, fc="#e5dac5", ec="none", zorder=1)
    ax.add_patch(poly_ground)

    # Groundwater layer
    gw_poly = patches.Rectangle((3.5, 0), 11.5, 1.15, fc="#cfe6f8", ec="none", zorder=2)
    ax.add_patch(gw_poly)
    ax.plot([3.5, 15], [1.15, 1.15], color=DEEP["blue"], lw=1.5, linestyle="--", zorder=3)

    # Terrain surface line
    ax.plot(x_terrain, y_terrain, color="#50703a", lw=2.5, zorder=4)

    # 2. Sea (Left: x=0 to 3.5)
    sea_rect = patches.Rectangle((0, 0), 3.5, 2.0, fc="#bde2f7", ec=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(sea_rect)
    for wy in [0.45, 0.95, 1.45]:
        wx = np.linspace(0.2, 3.3, 50)
        ax.plot(wx, wy + 0.05 * np.sin(wx * 9), color=DEEP["blue"], lw=1.2, alpha=0.55, zorder=4)

    # 3. River flowing down to the sea
    river_x = np.linspace(3.5, 10.2, 120)
    river_y = np.interp(river_x, x_terrain, y_terrain)
    ax.plot(river_x, river_y + 0.04, color=DEEP["blue"], lw=4.5, solid_capstyle="round", zorder=5)

    # 4. Sun at top left
    sun_center = (1.5, 8.8)
    sun_circle = patches.Circle(sun_center, 0.65, fc=ORANGE, ec=DEEP["orange"], lw=2.2, zorder=5)
    ax.add_patch(sun_circle)
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        dx, dy = np.cos(angle), np.sin(angle)
        ax.plot(
            [sun_center[0] + 0.78 * dx, sun_center[0] + 1.12 * dx],
            [sun_center[1] + 0.78 * dy, sun_center[1] + 1.12 * dy],
            color=DEEP["orange"], lw=2, zorder=4
        )
    ax.text(sun_center[0], sun_center[1], "sun", fontsize=13, weight="bold", ha="center", va="center", color=INK, zorder=6)

    # 5. Clouds
    def draw_cloud(cx, cy, scale=1.0):
        offsets = [(0, 0, 0.48), (-0.4, -0.08, 0.35), (0.4, -0.08, 0.36), (-0.2, 0.22, 0.36), (0.22, 0.2, 0.34)]
        for ox, oy, r in offsets:
            c = patches.Circle((cx + ox * scale, cy + oy * scale), r * scale, fc="#f0f6fc", ec=DEEP["blue"], lw=1.5, zorder=6)
            ax.add_patch(c)

    draw_cloud(3.2, 7.8, scale=1.1)
    draw_cloud(6.8, 8.0, scale=1.4)
    draw_cloud(9.2, 7.7, scale=1.1)

    # Cloud inland movement arrow
    ax.annotate(
        "", xy=(5.4, 8.1), xytext=(4.3, 8.0),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=DEEP["blue"], lw=2.5),
        zorder=7
    )

    # Rain falling from centre cloud over hills
    for rx in np.linspace(5.9, 7.7, 10):
        ax.plot([rx, rx - 0.25], [7.1, 6.1], color=DEEP["blue"], lw=1.8, linestyle="--", zorder=5)

    # 6. Wavy Evaporation Arrows rising from the sea
    def draw_wavy_arrow(base_x, y_start, y_end, amp=0.12, freq=2.8):
        ys = np.linspace(y_start, y_end - 0.2, 60)
        xs = base_x + amp * np.sin(freq * 2 * np.pi * (ys - y_start) / (y_end - y_start))
        ax.plot(xs, ys, color=DEEP["blue"], lw=2.2, zorder=5)
        # Arrowhead at the top pointing up
        ax.annotate(
            "", xy=(xs[-1], y_end), xytext=(xs[-2], ys[-2]),
            arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", color=DEEP["blue"], lw=2.2),
            zorder=6
        )

    for ex in [1.0, 1.8, 2.6]:
        draw_wavy_arrow(ex, 2.2, 6.5, amp=0.1, freq=2.5)

    # 7. Forest on the right (x=11 to 14.5)
    def draw_tree(tx, ty, scale=1.0):
        ax.plot([tx, tx], [ty, ty + 0.6 * scale], color="#6b4c35", lw=3.2 * scale, zorder=5)
        foliage1 = patches.Polygon([
            (tx - 0.42 * scale, ty + 0.5 * scale),
            (tx + 0.42 * scale, ty + 0.5 * scale),
            (tx, ty + 1.45 * scale)
        ], closed=True, fc=GREEN, ec=DEEP["green"], lw=1.5, zorder=6)
        foliage2 = patches.Polygon([
            (tx - 0.32 * scale, ty + 0.9 * scale),
            (tx + 0.32 * scale, ty + 0.9 * scale),
            (tx, ty + 1.65 * scale)
        ], closed=True, fc="#a1d99b", ec=DEEP["green"], lw=1.2, zorder=6)
        ax.add_patch(foliage1)
        ax.add_patch(foliage2)

    for tx, sc in [(11.2, 0.9), (12.0, 1.1), (12.8, 1.05), (13.6, 1.15), (14.3, 0.95)]:
        ty = float(np.interp(tx, x_terrain, y_terrain))
        draw_tree(tx, ty, sc)

    # Plant root uptake illustration
    rx_root = 12.8
    ry_root = float(np.interp(rx_root, x_terrain, y_terrain))
    ax.plot([rx_root, rx_root - 0.25], [ry_root, ry_root - 0.75], color="#7a5430", lw=2, zorder=5)
    ax.plot([rx_root, rx_root + 0.25], [ry_root, ry_root - 0.9], color="#7a5430", lw=2, zorder=5)
    ax.annotate("", xy=(rx_root, ry_root - 0.1), xytext=(rx_root - 0.35, ry_root - 0.65),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2), zorder=6)
    ax.annotate("", xy=(rx_root + 0.05, ry_root - 0.1), xytext=(rx_root + 0.35, ry_root - 0.75),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2), zorder=6)

    # 8. Cow Drinking at the River (at x=8.7)
    # Clear animal anatomy: barrel body, neck angled down to water, head touching river, horns, tail, 4 legs
    cx_cow = 8.65
    cy_river = float(np.interp(cx_cow, x_terrain, y_terrain))
    # Body ellipse
    cow_body = patches.Ellipse((cx_cow + 0.35, cy_river + 0.42), width=0.75, height=0.42,
                               angle=5, fc="#e8d8c3", ec=INK, lw=1.5, zorder=7)
    ax.add_patch(cow_body)
    # Hump (Zebu cow characteristic in Nigeria)
    hump = patches.Ellipse((cx_cow + 0.2, cy_river + 0.65), width=0.25, height=0.18,
                           fc="#dcc4aa", ec=INK, lw=1.3, zorder=7)
    ax.add_patch(hump)
    # Neck dipping downwards towards river surface
    neck = patches.Polygon([
        (cx_cow + 0.05, cy_river + 0.52),
        (cx_cow - 0.25, cy_river + 0.18),
        (cx_cow - 0.18, cy_river + 0.10),
        (cx_cow + 0.15, cy_river + 0.32)
    ], closed=True, fc="#e8d8c3", ec=INK, lw=1.3, zorder=7)
    ax.add_patch(neck)
    # Head dipping into water
    head = patches.Polygon([
        (cx_cow - 0.22, cy_river + 0.24),
        (cx_cow - 0.42, cy_river + 0.04), # Muzzle at water
        (cx_cow - 0.32, cy_river + 0.01),
        (cx_cow - 0.14, cy_river + 0.14)
    ], closed=True, fc="#dcc4aa", ec=INK, lw=1.3, zorder=7)
    ax.add_patch(head)
    # Horn
    ax.plot([cx_cow - 0.18, cx_cow - 0.24], [cy_river + 0.24, cy_river + 0.38], color=INK, lw=1.8, zorder=8)
    # Legs (4 legs)
    for lx in [cx_cow + 0.15, cx_cow + 0.28, cx_cow + 0.55, cx_cow + 0.68]:
        ax.plot([lx, lx], [cy_river + 0.25, cy_river], color=INK, lw=1.8, zorder=6)
    # Tail
    ax.plot([cx_cow + 0.72, cx_cow + 0.82], [cy_river + 0.45, cy_river + 0.22], color=INK, lw=1.4, zorder=7)

    # 9. Person Sweating (at x=9.7)
    px = 9.7
    py = float(np.interp(px, x_terrain, y_terrain))
    # Head, body, arms, legs
    ax.add_patch(patches.Circle((px, py + 0.72), 0.11, fc="#d29062", ec=INK, lw=1.3, zorder=7))
    ax.plot([px, px], [py + 0.28, py + 0.61], color=DEEP["orange"], lw=2.6, zorder=7)
    ax.plot([px, px - 0.12], [py + 0.28, py], color=INK, lw=1.6, zorder=7)
    ax.plot([px, px + 0.12], [py + 0.28, py], color=INK, lw=1.6, zorder=7)
    # Arms bent wiping brow
    ax.plot([px, px - 0.18, px - 0.08], [py + 0.52, py + 0.60, py + 0.72], color=INK, lw=1.4, zorder=7)
    ax.plot([px, px + 0.16], [py + 0.52, py + 0.35], color=INK, lw=1.4, zorder=7)
    # Sweat droplets
    ax.plot([px - 0.16, px - 0.18], [py + 0.78, py + 0.73], color=DEEP["blue"], lw=1.6, zorder=8)

    # Water vapour arrows from cow & person
    ax.annotate("", xy=(cx_cow + 0.2, cy_river + 1.1), xytext=(cx_cow + 0.2, cy_river + 0.7),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.6, linestyle=":"), zorder=8)
    ax.annotate("", xy=(px + 0.12, py + 1.15), xytext=(px + 0.12, py + 0.78),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.6, linestyle=":"), zorder=8)

    # 10. Well / Borehole (shifted to x=10.55, label elevated and away to avoid overlaps)
    bx = 10.55
    by_surf = float(np.interp(bx, x_terrain, y_terrain))
    # Borehole pipe cutting down through soil into groundwater
    ax.plot([bx, bx], [by_surf + 0.45, 0.4], color="#4b5563", lw=3.2, zorder=4)
    # Concrete plinth / apron
    ax.add_patch(patches.Rectangle((bx - 0.25, by_surf), 0.5, 0.12, fc="#cbd5e1", ec=INK, lw=1.3, zorder=5))
    # Handpump handle & spout
    ax.plot([bx, bx + 0.35], [by_surf + 0.42, by_surf + 0.22], color=INK, lw=2.2, zorder=5) # handle
    ax.plot([bx, bx - 0.18], [by_surf + 0.28, by_surf + 0.22], color=INK, lw=2.0, zorder=5) # spout
    # Placed neatly above the borehole
    ax.text(bx, by_surf + 0.75, "well or borehole", fontsize=11, weight="bold", ha="center", va="bottom",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=8)

    # 11. All Required Labels and Annotations

    # Evaporation
    ax.text(1.8, 4.4, "evaporation", fontsize=13, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3"), zorder=7)

    # Transpiration
    for tx in [12.0, 13.5]:
        ax.annotate("", xy=(tx, 6.7), xytext=(tx, 4.8),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5",
                                    color=DEEP["green"], lw=2.2, linestyle="--"), zorder=6)
    ax.text(12.8, 6.0, "transpiration", fontsize=13, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3"), zorder=7)

    # Condensation (clouds)
    ax.text(6.8, 8.85, "condensation (clouds)", fontsize=13, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=8)

    # Precipitation (rain)
    ax.text(6.8, 5.5, "precipitation (rain)", fontsize=13, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3"), zorder=8)

    # Run-off along river
    ax.annotate("", xy=(4.2, 2.35), xytext=(5.6, 2.85),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                color=DEEP["blue"], lw=2.5), zorder=7)
    ax.text(4.9, 3.2, "run-off", fontsize=12, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25"), zorder=8)

    # Infiltration (soaking into ground)
    ax.annotate("", xy=(7.9, 2.2), xytext=(7.9, 2.95),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.5",
                                color=DEEP["blue"], lw=2), zorder=6)
    ax.text(7.9, 2.7, "infiltration", fontsize=12, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=8)

    # Percolation (moving downwards to groundwater)
    ax.annotate("", xy=(7.9, 1.25), xytext=(7.9, 1.95),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.5",
                                color=DEEP["blue"], lw=2), zorder=6)
    ax.text(7.9, 1.6, "percolation", fontsize=12, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=8)

    # Groundwater
    ax.text(5.5, 0.55, "groundwater", fontsize=13, weight="bold", color=DEEP["blue"], ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25"), zorder=7)

    # River & Sea
    ax.text(1.75, 1.0, "sea", fontsize=14, weight="bold", color=DEEP["blue"], ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25"), zorder=6)
    ax.text(4.4, 1.95, "river", fontsize=12, weight="bold", color=DEEP["blue"], ha="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.2"), zorder=7)

    # Uptake by plant roots
    ax.text(13.5, 2.3, "uptake by plant roots", fontsize=12, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.25"), zorder=8)

    # Water lost by animals (breathing, sweating, urine)
    ax.text(9.1, 4.4, "water lost by animals\n(breathing, sweating, urine)", fontsize=11, color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=9)

    # Main Diagram Title
    ax.text(7.5, 9.6, "The Water Cycle in a Nigerian Landscape", fontsize=16, weight="bold", ha="center", color=INK)

    save(fig, out)
