from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.1, "Rural–Urban Interdependence", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # -------------------------------------------------------------
    # Left Side: Rural Village (Green theme)
    # -------------------------------------------------------------
    # Main bounding rounded card/circle for Rural
    rural_box = patches.FancyBboxPatch((0.6, 1.8), 3.2, 3.8,
                                       boxstyle="round,pad=0.2,rounding_size=0.4",
                                       facecolor=CREAM, edgecolor=GREEN, linewidth=2.5)
    ax.add_patch(rural_box)

    # Rural title
    ax.text(2.2, 5.2, "Rural Area", ha="center", va="center",
            fontsize=16, fontweight="bold", color=DEEP["green"])

    # Landscape: gentle hills
    hill1 = patches.Polygon([[0.8, 2.0], [0.8, 2.8], [1.8, 3.4], [2.8, 2.7], [2.8, 2.0]],
                            closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, alpha=0.6)
    hill2 = patches.Polygon([[1.6, 2.0], [1.6, 2.6], [2.6, 3.3], [3.6, 2.7], [3.6, 2.0]],
                            closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, alpha=0.9)
    ax.add_patch(hill1)
    ax.add_patch(hill2)

    # Simple House / Barn
    house_wall = patches.Rectangle((1.3, 2.5), 0.7, 0.6, facecolor="white", edgecolor=INK, lw=1.5)
    house_roof = patches.Polygon([[1.2, 3.1], [1.65, 3.6], [2.1, 3.1]], closed=True,
                                 facecolor=DEEP["orange"], edgecolor=INK, lw=1.5)
    house_door = patches.Rectangle((1.55, 2.5), 0.2, 0.35, facecolor=INK)
    ax.add_patch(house_wall)
    ax.add_patch(house_roof)
    ax.add_patch(house_door)

    # Simple Tree
    trunk = patches.Rectangle((2.7, 2.6), 0.12, 0.5, facecolor="#8B5A2B")
    foliage = patches.Circle((2.76, 3.3), 0.35, facecolor=DEEP["green"], edgecolor=INK, lw=1.2)
    ax.add_patch(trunk)
    ax.add_patch(foliage)

    # Subtitle / keywords for Rural
    ax.text(2.2, 2.2, "Villages & Agriculture", ha="center", va="center",
            fontsize=14, color=INK, fontstyle="italic")

    # -------------------------------------------------------------
    # Right Side: Urban Skyline (Grey theme)
    # -------------------------------------------------------------
    # Main bounding card
    urban_box = patches.FancyBboxPatch((8.2, 1.8), 3.2, 3.8,
                                       boxstyle="round,pad=0.2,rounding_size=0.4",
                                       facecolor=CREAM, edgecolor=GREY, linewidth=2.5)
    ax.add_patch(urban_box)

    # Urban title
    ax.text(9.8, 5.2, "Urban Area", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # City Skyline Buildings
    b1 = patches.Rectangle((8.6, 2.4), 0.5, 1.4, facecolor=GREY, edgecolor=INK, lw=1.5, alpha=0.7)
    b2 = patches.Rectangle((9.2, 2.4), 0.65, 2.0, facecolor=LAV, edgecolor=INK, lw=1.5, alpha=0.8)
    b3 = patches.Rectangle((9.95, 2.4), 0.55, 1.6, facecolor=GREY, edgecolor=INK, lw=1.5, alpha=0.7)
    b4 = patches.Rectangle((10.6, 2.4), 0.5, 1.1, facecolor=BLUE, edgecolor=INK, lw=1.5, alpha=0.4)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.add_patch(b3)
    ax.add_patch(b4)

    # Windows on central high-rise (b2)
    for wy in [2.7, 3.1, 3.5, 3.9]:
        for wx in [9.35, 9.6]:
            win = patches.Rectangle((wx, wy), 0.1, 0.15, facecolor="white", edgecolor=INK, lw=0.8)
            ax.add_patch(win)

    # Ground line under city
    ax.plot([8.4, 11.2], [2.4, 2.4], color=INK, lw=2)

    # Subtitle / keywords for Urban
    ax.text(9.8, 2.1, "Cities & Towns", ha="center", va="center",
            fontsize=14, color=INK, fontstyle="italic")

    # -------------------------------------------------------------
    # Circular Flow Arrows
    # -------------------------------------------------------------
    # Top Arrow: Rural -> Urban (curving over the top)
    top_arrow = patches.FancyArrowPatch((3.7, 4.8), (8.3, 4.8),
                                        connectionstyle="arc3,rad=-0.35",
                                        color=DEEP["green"], lw=3,
                                        arrowstyle="-|>,head_length=10,head_width=7")
    ax.add_patch(top_arrow)

    # Top Arrow Label
    ax.text(6.0, 6.1, "Food, Raw Materials, Labour, Market",
            ha="center", va="center", fontsize=14.5, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["green"], lw=1.8))

    # Bottom Arrow: Urban -> Rural (curving along the bottom)
    bot_arrow = patches.FancyArrowPatch((8.3, 2.6), (3.7, 2.6),
                                        connectionstyle="arc3,rad=-0.35",
                                        color=DEEP["blue"], lw=3,
                                        arrowstyle="-|>,head_length=10,head_width=7")
    ax.add_patch(bot_arrow)

    # Bottom Arrow Label
    ax.text(6.0, 1.25, "Manufactured Goods, Remittances (Money),\nHigher Services, Technology",
            ha="center", va="center", fontsize=14, fontweight="bold", color=INK,
            multialignment="center",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["blue"], lw=1.8))

    save(fig, out)
