from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_facecolor('white')

    # Curved atmosphere band across top/middle
    x_curve = np.linspace(0, 12, 100)
    y_outer = 6.9 - 0.075 * (x_curve - 6)**2
    y_inner = 5.3 - 0.075 * (x_curve - 6)**2

    ax.fill_between(x_curve, y_inner, y_outer, color=LAV, alpha=0.35, zorder=1)
    ax.plot(x_curve, y_outer, color=DEEP['blue'], lw=1.5, ls='--', alpha=0.6, zorder=2)
    ax.plot(x_curve, y_inner, color=DEEP['blue'], lw=1.5, ls='--', alpha=0.6, zorder=2)

    # Atmosphere gas molecules (dots/clusters in the atmosphere band)
    np.random.seed(42)
    for _ in range(50):
        gx = np.random.uniform(0.5, 11.5)
        gy_base = 5.3 - 0.075 * (gx - 6)**2
        gy = gy_base + np.random.uniform(0.2, 1.4)
        ax.plot(gx, gy, 'o', color=DEEP['blue'], markersize=3.5, alpha=0.45, zorder=2)

    # Ground landscape (green gentle rolling hills at bottom)
    ground_x = np.linspace(0, 12, 200)
    ground_y = 1.6 + 0.12 * np.sin(ground_x * 1.1) + 0.06 * np.cos(ground_x * 2.3)
    ax.fill_between(ground_x, 0, ground_y, color=GREEN, alpha=0.3, zorder=3)
    ax.plot(ground_x, ground_y, color=DEEP['green'], lw=2, zorder=4)

    # Sun at top left
    sun_center = (1.2, 7.0)
    sun_circle = patches.Circle(sun_center, 0.65, color=ORANGE, alpha=0.4, zorder=5)
    sun_core = patches.Circle(sun_center, 0.45, color=ORANGE, alpha=0.85, zorder=6)
    ax.add_patch(sun_circle)
    ax.add_patch(sun_core)

    # Sun rays
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        dx, dy = np.cos(angle), np.sin(angle)
        ax.plot([sun_center[0] + 0.75 * dx, sun_center[0] + 1.05 * dx],
                [sun_center[1] + 0.75 * dy, sun_center[1] + 1.05 * dy],
                color=DEEP['orange'], lw=2, zorder=5)

    # Yellow incoming solar radiation arrows (straight, thick short-wave)
    # Arrow 1: downwards towards open ground near x=3.5
    ax.annotate("", xy=(3.5, 2.0), xytext=(1.8, 6.4),
                arrowprops=dict(arrowstyle="-|>", color="#E69F00", lw=3.5, mutation_scale=20),
                zorder=7)
    # Arrow 2: downwards towards open ground / fields near x=7.8
    ax.annotate("", xy=(7.6, 2.1), xytext=(2.2, 6.3),
                arrowprops=dict(arrowstyle="-|>", color="#E69F00", lw=3.5, mutation_scale=20),
                zorder=7)

    # Helper function for wavy infrared arrows
    def draw_wavy_arrow(x_start, y_start, x_end, y_end, n_waves=4, amp=0.12, color=DEEP['pink'], lw=2.5):
        t = np.linspace(0, 1, 90)
        xs = (1 - t) * x_start + t * x_end
        ys = (1 - t) * y_start + t * y_end
        dx = x_end - x_start
        dy = y_end - y_start
        length = np.hypot(dx, dy)
        px, py = -dy / length, dx / length
        wave = np.sin(2 * np.pi * n_waves * t) * amp
        xs_w = xs + wave * px
        ys_w = ys + wave * py
        ax.plot(xs_w[:-5], ys_w[:-5], color=color, lw=lw, zorder=8)
        ax.annotate("", xy=(x_end, y_end), xytext=(xs_w[-6], ys_w[-6]),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=15),
                    zorder=8)

    # 1. Escaping heat radiation: originates cleanly from natural surface between cattle and car (x=3.6, y=1.72)
    draw_wavy_arrow(3.6, 1.72, 4.3, 7.3, n_waves=5, amp=0.15, color=DEEP['pink'])

    # 2. Radiation absorbed and trapped / reradiated downwards: originates from surface near x=8.0
    draw_wavy_arrow(8.0, 1.85, 8.4, 4.9, n_waves=3.5, amp=0.12, color=DEEP['pink'])
    draw_wavy_arrow(8.4, 4.9, 9.4, 2.1, n_waves=3.5, amp=0.12, color=DEEP['pink'])

    # Ground Features:
    # 1. Burning forest (far left, x: 0.6 - 1.5)
    ax.fill([0.7, 0.9, 1.1], [1.7, 2.3, 1.7], color=DEEP['green'], alpha=0.8, zorder=5)
    ax.plot([0.9, 0.9], [1.5, 1.7], color=INK, lw=2, zorder=5)
    ax.fill([1.2, 1.4, 1.6], [1.6, 2.2, 1.6], color=DEEP['green'], alpha=0.8, zorder=5)
    ax.plot([1.4, 1.4], [1.4, 1.6], color=INK, lw=2, zorder=5)
    flame_poly = patches.Polygon([[0.8, 1.7], [0.95, 2.2], [1.05, 1.9], [1.2, 2.35], [1.35, 1.6]],
                                 closed=True, color=ORANGE, alpha=0.9, zorder=6)
    ax.add_patch(flame_poly)

    # 2. Cattle / cow (around x: 2.3)
    cow_body = patches.Rectangle((2.1, 1.65), 0.52, 0.32, facecolor="white", edgecolor=INK, lw=1.2, zorder=5)
    cow_head = patches.Circle((2.02, 1.9), 0.13, facecolor="white", edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(cow_body)
    ax.add_patch(cow_head)
    ax.plot([2.18, 2.18], [1.42, 1.65], color=INK, lw=1.5, zorder=5)
    ax.plot([2.52, 2.52], [1.42, 1.65], color=INK, lw=1.5, zorder=5)

    # 3. Car with exhaust (around x: 4.8)
    car_body = patches.Rectangle((4.6, 1.75), 0.72, 0.24, facecolor=BLUE, edgecolor=INK, lw=1.2, zorder=5)
    car_top = patches.Polygon([[4.75, 1.99], [4.9, 2.22], [5.15, 2.22], [5.25, 1.99]],
                              closed=True, facecolor=BLUE, edgecolor=INK, lw=1.2, zorder=5)
    wheel1 = patches.Circle((4.75, 1.7), 0.1, facecolor=GREY, edgecolor=INK, lw=1.2, zorder=6)
    wheel2 = patches.Circle((5.18, 1.7), 0.1, facecolor=GREY, edgecolor=INK, lw=1.2, zorder=6)
    ax.add_patch(car_body)
    ax.add_patch(car_top)
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)
    # Exhaust pipe & puffs
    ax.plot([4.6, 4.45], [1.8, 1.83], color=INK, lw=1.5, zorder=5)
    ax.plot([4.35, 4.2], [1.9, 2.0], color=GREY, lw=2.2, ls=':', zorder=5)

    # 4. Factory chimney (around x: 6.4)
    factory_building = patches.Rectangle((6.1, 1.6), 0.75, 0.55, facecolor=CREAM, edgecolor=INK, lw=1.2, zorder=5)
    chimney = patches.Rectangle((6.55, 2.15), 0.22, 0.65, facecolor=GREY, edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(factory_building)
    ax.add_patch(chimney)
    # Chimney smoke puffs
    ax.plot([6.66, 6.6, 6.5], [2.85, 3.1, 3.3], color=GREY, lw=3, ls='--', alpha=0.7, zorder=5)

    # 5. City skyline backdrop (between factory and gas flare)
    for b_x, b_w, b_h in [(7.1, 0.35, 0.7), (7.5, 0.4, 0.95), (7.95, 0.35, 0.6)]:
        bldg = patches.Rectangle((b_x, 1.6), b_w, b_h, facecolor=LAV, edgecolor=INK, lw=1, alpha=0.7, zorder=4)
        ax.add_patch(bldg)

    # 6. Gas flare (around x: 10.4)
    pipe = patches.Rectangle((10.35, 1.6), 0.12, 0.9, facecolor=GREY, edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(pipe)
    flare_flame = patches.Polygon([[10.25, 2.5], [10.41, 3.05], [10.57, 2.5]], closed=True, color=ORANGE, zorder=6)
    ax.add_patch(flare_flame)

    # Labels and annotations
    bbox_white = dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, alpha=0.92, lw=0.8)

    # Atmosphere band label
    ax.text(6.0, 5.95, "atmosphere", fontsize=15, fontweight='bold', color=DEEP['blue'],
            ha='center', va='center', bbox=bbox_white, zorder=10)

    # Sunlight label
    ax.annotate("sunlight (short-wave radiation)", xy=(2.7, 4.5), xytext=(0.5, 4.9),
                fontsize=11.5, color=INK, ha='left', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # Earth absorbs heat (adjusted text position slightly to the right to avoid overlap)
    ax.annotate("Earth's surface absorbs heat", xy=(3.5, 1.95), xytext=(3.5, 0.8),
                fontsize=11.5, color=INK, ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # Infra-red heat radiation
    ax.annotate("infra-red (heat) radiation", xy=(8.1, 3.2), xytext=(6.5, 3.9),
                fontsize=11.5, color=INK, ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # Heat escapes to space
    ax.annotate("some heat escapes to space", xy=(4.3, 7.3), xytext=(3.7, 7.6),
                fontsize=11.5, color=INK, ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # Greenhouse gases trap heat
    ax.annotate("greenhouse gases trap heat", xy=(8.9, 4.1), xytext=(9.8, 5.5),
                fontsize=12, fontweight='bold', color=DEEP['pink'], ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.3),
                zorder=10)

    # Specific emission source labels
    # Deforestation and burning (moved x slightly left to separate from Earth absorbs heat)
    ax.annotate("deforestation and burning", xy=(1.1, 2.0), xytext=(1.0, 0.7),
                fontsize=11, color=INK, ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # Methane from cattle
    ax.annotate("methane from cattle", xy=(2.3, 1.95), xytext=(2.3, 2.8),
                fontsize=11, color=INK, ha='center', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    # CO2 from burning fuels: branch to both car exhaust and factory chimney
    ax.text(5.5, 0.7, "CO2 from burning fuels", fontsize=11, color=INK, ha='center', va='center',
            bbox=bbox_white, zorder=10)
    ax.annotate("", xy=(4.4, 1.85), xytext=(5.1, 0.85),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.1), zorder=10)
    ax.annotate("", xy=(6.66, 2.7), xytext=(5.9, 0.85),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.1), zorder=10)

    # Gas flaring
    ax.annotate("gas flaring", xy=(10.41, 2.75), xytext=(10.8, 3.4),
                fontsize=11, color=INK, ha='left', va='center',
                bbox=bbox_white, arrowprops=dict(arrowstyle="->", color=INK, lw=1.1),
                zorder=10)

    save(fig, out)
