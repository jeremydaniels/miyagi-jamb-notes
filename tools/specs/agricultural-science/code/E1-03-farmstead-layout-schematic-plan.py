from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Top Crop fields zone (background / fertile flat land)
    crop_bg = patches.Rectangle((5, 68), 90, 24, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, alpha=0.35, zorder=1)
    ax.add_patch(crop_bg)

    # Crop rows (horizontal lines indicating neat crop planting)
    for y_crop in np.linspace(71, 89, 7):
        ax.plot([7, 93], [y_crop, y_crop], color=DEEP["green"], lw=1.5, linestyle="--", alpha=0.7, zorder=2)

    # Road network: "Access road" coming from bottom-center, branching to farm areas
    road_poly = patches.Polygon([
        [46, 0], [54, 0], [54, 38], [80, 38], [80, 44], [54, 44],
        [54, 60], [20, 60], [20, 54], [46, 54]
    ], facecolor=CREAM, edgecolor=GREY, lw=2, zorder=2)
    ax.add_patch(road_poly)

    # Center dash line along access road
    ax.plot([50, 50], [0, 57], color=GREY, linestyle=":", lw=1.5, zorder=3)
    ax.plot([50, 78], [41, 41], color=GREY, linestyle=":", lw=1.5, zorder=3)
    ax.plot([22, 50], [57, 57], color=GREY, linestyle=":", lw=1.5, zorder=3)

    # Contour lines indicating "uphill" on the Eastern side
    for x_c, r in zip([88, 80, 72], [14, 18, 22]):
        contour = patches.Arc((85, 38), r*2, 45, angle=0, theta1=90, theta2=270, 
                              color=DEEP["orange"], lw=1.2, linestyle="-.", alpha=0.5, zorder=2)
        ax.add_patch(contour)

    # Farmhouse area (Eastern / upwind / slightly uphill)
    farmhouse_garden = patches.Rectangle((70, 25), 24, 28, facecolor=LAV, edgecolor=DEEP["lav"], lw=1.5, alpha=0.3, zorder=2)
    ax.add_patch(farmhouse_garden)
    farmhouse = patches.Rectangle((75, 32), 14, 14, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5, zorder=4)
    ax.add_patch(farmhouse)
    ax.text(82, 39, "Farmhouse", ha="center", va="center", fontsize=15, fontweight="bold", color=INK, zorder=5)

    # Centre: "Machinery Shed" and "Store"
    machinery = patches.Rectangle((37, 43), 11, 8, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=4)
    store = patches.Rectangle((37, 31), 11, 8, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2, zorder=4)
    ax.add_patch(machinery)
    ax.add_patch(store)
    ax.text(42.5, 47, "Machinery\nShed", ha="center", va="center", fontsize=14, color=INK, zorder=5)
    ax.text(42.5, 35, "Store", ha="center", va="center", fontsize=14, color=INK, zorder=5)

    # Western (downwind) side: "Poultry and Pig Houses", rectangular aligned East-West
    pig_house = patches.Rectangle((10, 42), 22, 7, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2, zorder=4)
    poultry_house = patches.Rectangle((10, 30), 22, 7, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2, zorder=4)
    ax.add_patch(pig_house)
    ax.add_patch(poultry_house)
    ax.text(21, 45.5, "Pig House (E-W)", ha="center", va="center", fontsize=14, color=INK, zorder=5)
    ax.text(21, 33.5, "Poultry House (E-W)", ha="center", va="center", fontsize=14, color=INK, zorder=5)

    # Compass rose in top-left
    cx, cy = 12, 85
    ax.annotate("", xy=(cx, cy + 9), xytext=(cx, cy - 3),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=18), zorder=6)
    ax.annotate("", xy=(cx + 6, cy + 3), xytext=(cx - 6, cy + 3),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.5), zorder=6)
    ax.text(cx, cy + 10.5, "N", ha="center", va="bottom", fontsize=16, fontweight="bold", color=INK, zorder=6)
    ax.text(cx + 7.5, cy + 3, "E", ha="left", va="center", fontsize=14, color=INK, zorder=6)
    ax.text(cx - 7.5, cy + 3, "W", ha="right", va="center", fontsize=14, color=INK, zorder=6)

    # Wind arrow: blowing from East to West
    ax.annotate("", xy=(60, 96), xytext=(85, 96),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3, mutation_scale=22), zorder=6)
    ax.text(72.5, 98, "Wind direction", ha="center", va="bottom", fontsize=15, fontweight="bold", color=DEEP["blue"],
            bbox=dict(fc="white", ec="none", pad=1))

    # Required Labels as specified
    # 1. "Crop fields (fertile soil)"
    ax.text(50, 80, "Crop fields (fertile soil)", ha="center", va="center", fontsize=16, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.35", lw=1.5), zorder=5)

    # 2. "Farmhouse (upwind and uphill)"
    ax.annotate("Farmhouse (upwind and uphill)", xy=(82, 46.5), xytext=(82, 58),
                ha="center", va="bottom", fontsize=14.5, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.35", lw=1.5), zorder=6)

    # 3. "Livestock houses (downwind, aligned East-West)"
    ax.annotate("Livestock houses (downwind, aligned East-West)", xy=(21, 29), xytext=(21, 16),
                ha="center", va="top", fontsize=14, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.5), zorder=6)

    # 4. "Access road"
    ax.text(50, 10, "Access road", ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1.2), zorder=5)

    save(fig, out)
