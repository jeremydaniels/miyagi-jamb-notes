from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 9.5)
    ax.axis("off")

    # Corner positions: Triangle
    # Top corner: Raw Material Source
    pt_raw = np.array([2.0, 7.2]) # Lowered slightly to avoid title
    # Bottom left: Power/Energy Source
    pt_power = np.array([1.5, 1.2]) # Lowered slightly
    # Right corner: Market (City)
    pt_market = np.array([8.5, 3.2])

    # Factory location (Weber's optimal least-cost point)
    pt_factory = np.array([4.2, 3.8]) # Adjusted slightly

    # Draw dashed Weber locational triangle
    tri_poly = plt.Polygon([pt_raw, pt_market, pt_power], closed=True, 
                           facecolor=CREAM, edgecolor=GREY, lw=1.8, linestyle="--", alpha=0.4, zorder=1)
    ax.add_patch(tri_poly)

    # Road from factory to market (under the arrow)
    ax.plot([pt_factory[0], pt_market[0]], [pt_factory[1], pt_market[1]], 
            color=GREY, lw=7.0, solid_capstyle='round', zorder=2)
    ax.plot([pt_factory[0], pt_market[0]], [pt_factory[1], pt_market[1]], 
            color='white', lw=1.2, linestyle='--', dashes=(4, 4), zorder=3)

    # Pull arrows towards factory
    def draw_pull_arrow(p_start, p_end, col, label, offset_text=(0, 0)):
        vec = p_end - p_start
        dist = np.linalg.norm(vec)
        uvec = vec / dist
        start = p_start + uvec * 0.9
        end = p_end - uvec * 0.8
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=3.2,
                                    mutation_scale=22), zorder=4)
        mid = (start + end) / 2 + np.array(offset_text)
        ax.text(mid[0], mid[1], label, color=col, fontsize=14, weight='bold',
                ha='center', va='center', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.85), zorder=5)

    draw_pull_arrow(pt_raw, pt_factory, DEEP["orange"], "Material Pull", (-0.8, 0.2))
    draw_pull_arrow(pt_power, pt_factory, DEEP["blue"], "Energy Pull", (-0.8, 0.1))
    draw_pull_arrow(pt_market, pt_factory, DEEP["green"], "Market Pull", (0.3, -0.6))

    # --- Corner nodes ---
    # 1. Raw Material Source
    ax.add_patch(patches.Circle(pt_raw, 0.75, fc=PINK, ec=DEEP["pink"], lw=2.0, zorder=6))
    # Ore/pickaxe icon hint (rocks)
    ax.scatter([pt_raw[0]-0.2, pt_raw[0]+0.2, pt_raw[0]], [pt_raw[1]-0.1, pt_raw[1]-0.15, pt_raw[1]+0.2], 
               s=[140, 160, 200], c=DEEP["pink"], marker='8', zorder=7)
    ax.text(pt_raw[0], pt_raw[1] + 1.1, "Raw Material Source", fontsize=15, weight='bold', 
            ha='center', va='center', color=INK, bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY))

    # 2. Power/Energy Source
    ax.add_patch(patches.Circle(pt_power, 0.75, fc=LAV, ec=DEEP["lav"], lw=2.0, zorder=6))
    # Lightning bolt symbol
    bolt_x = pt_power[0] + np.array([0.05, -0.2, 0.0, -0.15, 0.25, 0.0, 0.15])
    bolt_y = pt_power[1] + np.array([0.35, 0.05, 0.05, -0.35, -0.05, -0.05, 0.35])
    ax.fill(bolt_x, bolt_y, color=DEEP["lav"], zorder=7)
    ax.text(pt_power[0], pt_power[1] - 1.15, "Power/Energy Source", fontsize=15, weight='bold', 
            ha='center', va='center', color=INK, bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY))

    # 3. Market (City)
    ax.add_patch(patches.Circle(pt_market, 0.85, fc=GREEN, ec=DEEP["green"], lw=2.0, zorder=6))
    # Buildings sketch
    ax.add_patch(patches.Rectangle((pt_market[0]-0.45, pt_market[1]-0.35), 0.25, 0.7, fc=DEEP["green"], zorder=7))
    ax.add_patch(patches.Rectangle((pt_market[0]-0.15, pt_market[1]-0.45), 0.3, 0.9, fc=DEEP["green"], zorder=7))
    ax.add_patch(patches.Rectangle((pt_market[0]+0.2, pt_market[1]-0.25), 0.25, 0.55, fc=DEEP["green"], zorder=7))
    ax.text(pt_market[0], pt_market[1] + 1.25, "Market (City)", fontsize=15, weight='bold', 
            ha='center', va='center', color=INK, bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY))

    # --- Central Factory Node ---
    fx, fy = pt_factory[0], pt_factory[1]
    ax.add_patch(patches.Circle((fx, fy), 0.8, fc='white', ec=INK, lw=2.5, zorder=8))
    # Factory silhouette
    # Main building
    ax.add_patch(patches.Rectangle((fx - 0.45, fy - 0.35), 0.9, 0.45, fc=INK, ec=INK, zorder=9))
    # Sawtooth roof
    roof = np.array([
        [fx - 0.45, fy + 0.1],
        [fx - 0.45, fy + 0.3],
        [fx - 0.15, fy + 0.1],
        [fx - 0.15, fy + 0.3],
        [fx + 0.15, fy + 0.1],
        [fx + 0.15, fy + 0.3],
        [fx + 0.45, fy + 0.1]
    ])
    ax.add_patch(patches.Polygon(roof, closed=False, color=INK, lw=2.5, zorder=9))
    # Chimney smoke
    ax.plot([fx + 0.32, fx + 0.32], [fy + 0.1, fy + 0.45], color=INK, lw=3.0, zorder=9)
    ax.text(fx - 0.1, fy - 1.2, "Optimal Factory Location\n(Least-Cost Point)", fontsize=14, weight='bold',
            ha='center', va='top', color=INK, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=INK, lw=1.2))

    # --- Truck on the Road ---
    # Placed along the road between factory and market
    truck_t = 0.58
    truck_pos = (1 - truck_t) * pt_factory + truck_t * pt_market + np.array([0.0, 0.45])
    tx, ty = truck_pos[0], truck_pos[1]
    # Truck cargo box
    ax.add_patch(patches.Rectangle((tx - 0.32, ty - 0.05), 0.42, 0.28, fc=ORANGE, ec=INK, lw=1.2, zorder=8))
    # Truck cabin
    cab = patches.Rectangle((tx + 0.12, ty - 0.05), 0.18, 0.20, fc=DEEP["orange"], ec=INK, lw=1.2, zorder=8)
    ax.add_patch(cab)
    # Truck wheels
    ax.add_patch(patches.Circle((tx - 0.18, ty - 0.08), 0.06, fc=INK, zorder=9))
    ax.add_patch(patches.Circle((tx + 0.2, ty - 0.08), 0.06, fc=INK, zorder=9))
    ax.text(tx, ty + 0.42, "Finished Goods Delivery", fontsize=14, ha='center', va='bottom',
            color=INK, style='italic', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY, lw=0.8))

    # Title & Concept Banner
    ax.text(5.0, 9.1, "Weber's Location Triangle Model", fontsize=18, weight='bold',
            ha='center', va='center', color=INK)
    ax.text(5.0, 8.6, "The factory's location balances the pull of raw materials, power, and market",
            fontsize=14, ha='center', va='center', color=INK, style='italic',
            bbox=dict(boxstyle='square,pad=0.3', fc=CREAM, ec=GREY, lw=0.8))

    save(fig, out)
