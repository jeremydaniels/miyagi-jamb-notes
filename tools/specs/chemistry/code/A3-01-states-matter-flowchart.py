from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 12)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    # Titles / Headings
    ax.text(5, 11.4, "Changes of State", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    box_w, box_h = 4.2, 2.2
    box_x = 2.9  # left edge of container boxes

    # 1. SOLID (Top row: center y = 9.8)
    y_solid = 9.8
    # Container
    rect_solid = patches.FancyBboxPatch((box_x, y_solid - box_h/2), box_w, box_h,
                                        boxstyle="round,pad=0.08,rounding_size=0.15",
                                        facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax.add_patch(rect_solid)
    ax.text(box_x - 0.4, y_solid, "SOLID", fontsize=16, fontweight="bold", ha="right", va="center", color=INK)

    # Solid particles: tightly packed square grid (4 rows, 7 cols)
    r_solid = 0.16
    grid_rows, grid_cols = 4, 7
    xs = np.linspace(box_x + 0.6, box_x + box_w - 0.6, grid_cols)
    ys = np.linspace(y_solid - 0.65, y_solid + 0.65, grid_rows)
    for x in xs:
        for y in ys:
            c = plt.Circle((x, y), r_solid, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.2, zorder=3)
            ax.add_patch(c)

    # 2. LIQUID (Middle row: center y = 6.0)
    y_liquid = 6.0
    rect_liquid = patches.FancyBboxPatch((box_x, y_liquid - box_h/2), box_w, box_h,
                                         boxstyle="round,pad=0.08,rounding_size=0.15",
                                         facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax.add_patch(rect_liquid)
    ax.text(box_x - 0.4, y_liquid, "LIQUID", fontsize=16, fontweight="bold", ha="right", va="center", color=INK)

    # Liquid particles: touching but jumbled / irregular, settled toward bottom
    r_liq = 0.16
    np.random.seed(42)
    # Generate structured jumbled positions
    liq_pts = []
    y_base = y_liquid - 0.75
    row_y = [y_base, y_base + 0.32, y_base + 0.64, y_base + 0.96]
    for r_idx, ry in enumerate(row_y):
        n_p = 7 if r_idx % 2 == 0 else 6
        x_start = box_x + 0.55 if r_idx % 2 == 0 else box_x + 0.8
        for i in range(n_p):
            px = x_start + i * 0.48 + np.random.uniform(-0.06, 0.06)
            py = ry + np.random.uniform(-0.04, 0.04)
            liq_pts.append((px, py))

    for px, py in liq_pts:
        c = plt.Circle((px, py), r_liq, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.2, zorder=3)
        ax.add_patch(c)

    # 3. GAS (Bottom row: center y = 2.2)
    y_gas = 2.2
    rect_gas = patches.FancyBboxPatch((box_x, y_gas - box_h/2), box_w, box_h,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax.add_patch(rect_gas)
    ax.text(box_x - 0.4, y_gas, "GAS", fontsize=16, fontweight="bold", ha="right", va="center", color=INK)

    # Gas particles: widely separated with motion lines
    gas_coords = [
        (box_x + 0.8, y_gas + 0.5, 0.2, 0.15),
        (box_x + 2.1, y_gas + 0.7, -0.22, 0.1),
        (box_x + 3.4, y_gas + 0.4, -0.15, -0.2),
        (box_x + 1.2, y_gas - 0.45, 0.25, -0.1),
        (box_x + 2.4, y_gas - 0.2, -0.2, 0.15),
        (box_x + 3.3, y_gas - 0.55, 0.18, 0.2),
        (box_x + 1.7, y_gas + 0.1, 0.2, -0.15),
        (box_x + 2.9, y_gas + 0.2, -0.15, -0.22)
    ]
    for gx, gy, dx, dy in gas_coords:
        c = plt.Circle((gx, gy), r_solid, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.2, zorder=3)
        ax.add_patch(c)
        # Motion trail / lines behind particle
        ax.plot([gx - dx * 0.7, gx - dx * 1.5], [gy - dy * 0.7, gy - dy * 1.5],
                color=GREY, lw=1.5, zorder=2)
        ax.plot([gx - dx * 0.6 - dy * 0.2, gx - dx * 1.2 - dy * 0.2],
                [gy - dy * 0.6 + dx * 0.2, gy - dy * 1.2 + dx * 0.2],
                color=GREY, lw=1.0, linestyle=":", zorder=2)

    # Process Arrows between Solid and Liquid
    top_solid_bottom = y_solid - box_h/2
    mid_liquid_top = y_liquid + box_h/2
    mid_liquid_bottom = y_liquid - box_h/2
    bot_gas_top = y_gas + box_h/2

    arrow_x_heat = 4.2
    arrow_x_cool = 5.8

    # Downward red arrow: Melting (Solid -> Liquid)
    ax.annotate("", xy=(arrow_x_heat, mid_liquid_top + 0.08),
                xytext=(arrow_x_heat, top_solid_bottom - 0.08),
                arrowprops=dict(facecolor=DEEP["pink"], edgecolor=DEEP["pink"], width=3, headwidth=9, shrink=0.05))
    ax.text(arrow_x_heat - 0.18, (top_solid_bottom + mid_liquid_top)/2, "Melting",
            fontsize=15, fontweight="bold", ha="right", va="center", color=DEEP["pink"])

    # Upward blue arrow: Freezing (Liquid -> Solid)
    ax.annotate("", xy=(arrow_x_cool, top_solid_bottom - 0.08),
                xytext=(arrow_x_cool, mid_liquid_top + 0.08),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=9, shrink=0.05))
    ax.text(arrow_x_cool + 0.18, (top_solid_bottom + mid_liquid_top)/2, "Freezing",
            fontsize=15, fontweight="bold", ha="left", va="center", color=DEEP["blue"])

    # Downward red arrow: Boiling/Vapourization (Liquid -> Gas)
    ax.annotate("", xy=(arrow_x_heat, bot_gas_top + 0.08),
                xytext=(arrow_x_heat, mid_liquid_bottom - 0.08),
                arrowprops=dict(facecolor=DEEP["pink"], edgecolor=DEEP["pink"], width=3, headwidth=9, shrink=0.05))
    ax.text(arrow_x_heat - 0.18, (mid_liquid_bottom + bot_gas_top)/2, "Boiling /\nVapourization",
            fontsize=15, fontweight="bold", ha="right", va="center", color=DEEP["pink"])

    # Upward blue arrow: Condensation (Gas -> Liquid)
    ax.annotate("", xy=(arrow_x_cool, mid_liquid_bottom - 0.08),
                xytext=(arrow_x_cool, bot_gas_top + 0.08),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=9, shrink=0.05))
    ax.text(arrow_x_cool + 0.18, (mid_liquid_bottom + bot_gas_top)/2, "Condensation",
            fontsize=15, fontweight="bold", ha="left", va="center", color=DEEP["blue"])

    # Legend / Key on the right margin
    legend_x = 8.5
    # Heating indicator
    ax.annotate("", xy=(legend_x, 6.7), xytext=(legend_x, 8.5),
                arrowprops=dict(facecolor=DEEP["pink"], edgecolor=DEEP["pink"], width=3, headwidth=8))
    ax.text(legend_x + 0.25, 7.6, "Heating\n(energy added)", fontsize=14, va="center", ha="left", color=DEEP["pink"], fontweight="bold")

    # Cooling indicator
    ax.annotate("", xy=(legend_x, 5.3), xytext=(legend_x, 3.5),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=8))
    ax.text(legend_x + 0.25, 4.4, "Cooling\n(energy removed)", fontsize=14, va="center", ha="left", color=DEEP["blue"], fontweight="bold")

    save(fig, out)
