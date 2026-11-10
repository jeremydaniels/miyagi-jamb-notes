import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from style import *

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title / Headers
    ax.text(7, 8.4, "Antony's Divided Loyalties", fontsize=20, weight="bold", color=INK, ha="center")
    
    # Left Zone (Rome) background panel
    rect_rome = patches.FancyBboxPatch((0.6, 0.8), 4.2, 7.0, boxstyle="round,pad=0.2",
                                       fc=CREAM, ec=DEEP["blue"], lw=2.0)
    ax.add_patch(rect_rome)

    # Right Zone (Egypt) background panel
    rect_egypt = patches.FancyBboxPatch((9.2, 0.8), 4.2, 7.0, boxstyle="round,pad=0.2",
                                        fc=CREAM, ec=DEEP["orange"], lw=2.0)
    ax.add_patch(rect_egypt)

    # Central Sea Area background
    sea_poly = patches.FancyBboxPatch((5.1, 2.5), 3.8, 3.8, boxstyle="round,pad=0.2",
                                      fc="#EBF4F6", ec="none")
    ax.add_patch(sea_poly)

    # Label Sea
    ax.text(7, 4.4, "Mediterranean Sea", fontsize=16, weight="bold", color=DEEP["blue"], ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.2))

    # Bidirectional Dotted Connection representing divided loyalties
    # Rome to Egypt curve (upper)
    arrow_east = patches.FancyArrowPatch((4.8, 5.2), (9.2, 5.2),
                                         connectionstyle="arc3,rad=-0.25",
                                         linestyle=":", linewidth=2.5,
                                         arrowstyle="->", mutation_scale=22,
                                         color=DEEP["pink"])
    ax.add_patch(arrow_east)

    # Egypt to Rome curve (lower)
    arrow_west = patches.FancyArrowPatch((9.2, 3.6), (4.8, 3.6),
                                         connectionstyle="arc3,rad=-0.25",
                                         linestyle=":", linewidth=2.5,
                                         arrowstyle="->", mutation_scale=22,
                                         color=DEEP["pink"])
    ax.add_patch(arrow_west)

    ax.text(7, 5.85, "Divided Loyalties", fontsize=14, style="italic", color=DEEP["pink"], ha="center",
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # ------------------ ROME (West) ------------------
    ax.text(2.7, 7.3, "Rome: Duty, Power, Reason", fontsize=15, weight="bold", color=DEEP["blue"], ha="center")

    # Marble Columns
    # Base and pediment
    col_x = 1.3
    for cx in [col_x, col_x + 0.8]:
        # capital & base
        ax.add_patch(patches.Rectangle((cx - 0.2, 4.3), 0.4, 0.1, fc=GREY, ec=INK, lw=1.2))
        ax.add_patch(patches.Rectangle((cx - 0.15, 3.2), 0.3, 1.1, fc="white", ec=INK, lw=1.2))
        ax.add_patch(patches.Rectangle((cx - 0.2, 3.1), 0.4, 0.1, fc=GREY, ec=INK, lw=1.2))
        # fluting lines
        ax.plot([cx - 0.05, cx - 0.05], [3.2, 4.3], color=GREY, lw=1)
        ax.plot([cx + 0.05, cx + 0.05], [3.2, 4.3], color=GREY, lw=1)
    # Pediment beam across
    ax.add_patch(patches.Rectangle((col_x - 0.3, 4.4), 1.4, 0.2, fc=GREY, ec=INK, lw=1.2))
    ax.text(1.7, 2.7, "Marble Columns", fontsize=14, color=INK, ha="center")

    # Roman Eagle (Aquila)
    # Simplified heraldic eagle shape
    eagle_cx, eagle_cy = 3.6, 5.6
    # Body & head
    ax.plot([eagle_cx, eagle_cx], [eagle_cy - 0.3, eagle_cy + 0.3], color=DEEP["blue"], lw=4, solid_capstyle='round')
    ax.plot([eagle_cx, eagle_cx + 0.15], [eagle_cy + 0.3, eagle_cy + 0.25], color=DEEP["blue"], lw=2.5) # beak
    # Wings
    wing_left = np.array([[eagle_cx, eagle_cy + 0.1], [eagle_cx - 0.5, eagle_cy + 0.4], [eagle_cx - 0.6, eagle_cy]])
    wing_right = np.array([[eagle_cx, eagle_cy + 0.1], [eagle_cx + 0.5, eagle_cy + 0.4], [eagle_cx + 0.6, eagle_cy]])
    ax.plot(wing_left[:, 0], wing_left[:, 1], color=DEEP["blue"], lw=3)
    ax.plot(wing_right[:, 0], wing_right[:, 1], color=DEEP["blue"], lw=3)
    ax.text(eagle_cx, eagle_cy - 0.65, "Roman Eagle", fontsize=14, color=INK, ha="center")

    # Crossed Swords
    sw_cx, sw_cy = 3.6, 3.8
    ax.plot([sw_cx - 0.4, sw_cx + 0.4], [sw_cy - 0.4, sw_cy + 0.4], color=INK, lw=2.5)
    ax.plot([sw_cx - 0.4, sw_cx + 0.4], [sw_cy + 0.4, sw_cy - 0.4], color=INK, lw=2.5)
    # Guards
    ax.plot([sw_cx - 0.3, sw_cx - 0.2], [sw_cy - 0.2, sw_cy - 0.3], color=DEEP["blue"], lw=3)
    ax.plot([sw_cx - 0.3, sw_cx - 0.2], [sw_cy + 0.2, sw_cy + 0.3], color=DEEP["blue"], lw=3)
    ax.text(sw_cx, 3.0, "Swords", fontsize=14, color=INK, ha="center")

    # Rome sub-text
    ax.text(2.7, 1.2, "West: Roman Empire", fontsize=14, color=GREY, ha="center")

    # ------------------ EGYPT (East) ------------------
    ax.text(11.3, 7.3, "Egypt: Passion, Pleasure, Fertility", fontsize=15, weight="bold", color=DEEP["orange"], ha="center")

    # Pyramids
    pyr1 = patches.Polygon([[9.8, 5.0], [10.5, 6.2], [11.2, 5.0]], closed=True, fc=CREAM, ec=DEEP["orange"], lw=2)
    pyr2 = patches.Polygon([[10.7, 5.0], [11.3, 6.0], [11.9, 5.0]], closed=True, fc=CREAM, ec=DEEP["orange"], lw=2)
    ax.add_patch(pyr1)
    ax.add_patch(pyr2)
    ax.text(10.8, 4.6, "Pyramids", fontsize=14, color=INK, ha="center")

    # Winding River Nile
    nile_t = np.linspace(0, 1, 100)
    nile_x = 12.8 + 0.2 * np.sin(nile_t * 3 * np.pi)
    nile_y = 3.6 + (1 - nile_t) * 2.8
    ax.plot(nile_x, nile_y, color=DEEP["blue"], lw=3.5, label="River Nile")
    ax.text(12.8, 3.2, "River Nile", fontsize=14, color=INK, ha="center")

    # Lotus Flower
    lotus_x, lotus_y = 10.3, 3.3
    # Petals
    ax.plot([lotus_x, lotus_x], [lotus_y - 0.2, lotus_y + 0.3], color=DEEP["green"], lw=2.5) # stem
    # Center & side petals
    petal_l = patches.Arc((lotus_x - 0.1, lotus_y + 0.15), 0.25, 0.35, angle=25, theta1=0, theta2=180, ec=DEEP["pink"], lw=2)
    petal_r = patches.Arc((lotus_x + 0.1, lotus_y + 0.15), 0.25, 0.35, angle=-25, theta1=0, theta2=180, ec=DEEP["pink"], lw=2)
    petal_c = patches.Arc((lotus_x, lotus_y + 0.2), 0.2, 0.4, theta1=0, theta2=180, ec=DEEP["pink"], lw=2)
    ax.add_patch(petal_l)
    ax.add_patch(petal_r)
    ax.add_patch(petal_c)
    ax.text(10.3, 2.7, "Lotus flower", fontsize=14, color=INK, ha="center")

    # Snake (Asp)
    snake_t = np.linspace(0, 1, 100)
    snake_x = 11.6 + 0.15 * np.sin(snake_t * 4 * np.pi)
    snake_y = 2.4 + snake_t * 1.0
    ax.plot(snake_x, snake_y, color=DEEP["green"], lw=2.5)
    ax.plot(snake_x[-1], snake_y[-1], marker="o", color=DEEP["green"], markersize=4) # head
    ax.text(11.6, 2.0, "Snake", fontsize=14, color=INK, ha="center")

    # Egypt sub-text
    ax.text(11.3, 1.2, "East: Alexandria & The Nile", fontsize=14, color=GREY, ha="center")

    save(fig, out)
