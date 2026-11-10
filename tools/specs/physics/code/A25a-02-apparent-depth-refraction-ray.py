from style import *
import numpy as np
from matplotlib.patches import Ellipse

def draw(out):
    fig = canvas(9.5, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1.2, 9.6)
    ax.set_ylim(-0.8, 8.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Water bucket coordinates
    b_left = 3.2
    b_right = 7.6
    b_bottom = 0.8
    water_level = 4.8

    # Water fill
    ax.fill_between([b_left, b_right], b_bottom, water_level, color=BLUE, alpha=0.35, zorder=1)

    # Bucket walls
    ax.plot([b_left, b_left, b_right, b_right], [water_level + 0.8, b_bottom, b_bottom, water_level + 0.8],
            color=INK, lw=2.5, zorder=2)
    # Water surface line
    ax.plot([b_left, b_right], [water_level, water_level], color=DEEP["blue"], lw=2.0, zorder=2)
    ax.text(b_left + 0.3, water_level - 0.35, "Water surface", fontsize=14, color=DEEP["blue"], ha="left", va="top")

    # Positions of Real Coin and Apparent Image
    x_coin = 5.2
    y_real = b_bottom
    y_app = 2.4

    # Surface refraction points for two rays
    x_surf1 = 5.8
    x_surf2 = 6.6

    # Eye position
    eye_x = 7.7
    eye_y = 7.0

    # Draw normals at refraction points
    for xs in [x_surf1, x_surf2]:
        ax.plot([xs, xs], [water_level - 1.0, water_level + 1.2], color=GREY, lw=1.5, ls="--", zorder=2)
    
    # Label "Normal" placed cleanly above the left normal line to avoid ray clutter
    ax.text(x_surf1, water_level + 1.35, "Normal", fontsize=14, color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=1))

    # Real rays (from coin to surface)
    ax.plot([x_coin, x_surf1], [y_real, water_level], color=DEEP["orange"], lw=2.2, zorder=3)
    ax.plot([x_coin, x_surf2], [y_real, water_level], color=DEEP["orange"], lw=2.2, zorder=3)

    # Arrows on rays in water
    def draw_arrow(x0, y0, x1, y1, frac=0.55):
        xm = x0 + (x1 - x0) * frac
        ym = y0 + (y1 - y0) * frac
        dx = (x1 - x0) * 0.05
        dy = (y1 - y0) * 0.05
        ax.annotate("", xy=(xm + dx, ym + dy), xytext=(xm, ym),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0, mutation_scale=16),
                    zorder=4)

    draw_arrow(x_coin, y_real, x_surf1, water_level, 0.5)
    draw_arrow(x_coin, y_real, x_surf2, water_level, 0.5)

    # Refracted rays (from surface to eye)
    target1_x = eye_x - 0.25
    target1_y = eye_y - 0.2
    ax.plot([x_surf1, target1_x], [water_level, target1_y], color=DEEP["orange"], lw=2.2, zorder=3)
    ax.plot([x_surf2, eye_x], [water_level, eye_y], color=DEEP["orange"], lw=2.2, zorder=3)

    draw_arrow(x_surf1, water_level, target1_x, target1_y, 0.45)
    draw_arrow(x_surf2, water_level, eye_x, eye_y, 0.45)

    # Virtual rays (dashed backwards to apparent image)
    ax.plot([x_surf1, x_coin], [water_level, y_app], color=DEEP["pink"], lw=2.0, ls="--", zorder=3)
    ax.plot([x_surf2, x_coin], [water_level, y_app], color=DEEP["pink"], lw=2.0, ls="--", zorder=3)

    # Draw coins (real and ghost)
    coin_w, coin_h = 0.75, 0.24
    real_coin = Ellipse((x_coin, y_real + coin_h/2), coin_w, coin_h, fc=ORANGE, ec=INK, lw=1.8, zorder=5)
    ax.add_patch(real_coin)
    ax.text(x_coin, y_real - 0.25, "Real coin (object)", fontsize=14, color=INK, ha="center", va="top")

    app_coin = Ellipse((x_coin, y_app + coin_h/2), coin_w, coin_h, fc=CREAM, ec=DEEP["pink"], lw=1.8, ls="--", zorder=5)
    ax.add_patch(app_coin)
    ax.text(x_coin - 0.55, y_app + 0.35, 'Apparent image\n("ghost" coin)', fontsize=14, color=DEEP["pink"], ha="right", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5))

    # Draw observer's eye
    ex, ey = eye_x + 0.1, eye_y + 0.1
    t = np.linspace(-0.6, 0.6, 50)
    top_lid_x = ex + 0.6 * np.cos(t + 0.5) - 0.5
    top_lid_y = ey + 0.4 * np.sin(t + 0.5)
    bot_lid_x = ex + 0.6 * np.cos(t - 0.5) - 0.5
    bot_lid_y = ey + 0.4 * np.sin(t - 0.5)
    ax.plot(top_lid_x, top_lid_y, color=INK, lw=2.0, zorder=6)
    ax.plot(bot_lid_x, bot_lid_y, color=INK, lw=2.0, zorder=6)
    iris = Ellipse((ex - 0.1, ey + 0.05), 0.2, 0.28, angle=35, fc=INK, ec=INK, zorder=6)
    ax.add_patch(iris)
    ax.text(ex + 0.45, ey + 0.25, "Observer's\neye", fontsize=15, color=INK, ha="left", va="center")

    # Depth dimension lines on left (well separated to prevent any overlap)
    dim_x_app = 2.1
    dim_x_real = 0.6

    # Extension reference lines
    ax.plot([dim_x_real - 0.2, b_left], [water_level, water_level], color=GREY, lw=1.2, ls=":")
    ax.plot([dim_x_app - 0.2, x_coin - coin_w/2], [y_app + coin_h/2, y_app + coin_h/2], color=GREY, lw=1.2, ls=":")
    ax.plot([dim_x_real - 0.2, x_coin - coin_w/2], [y_real, y_real], color=GREY, lw=1.2, ls=":")

    # Apparent depth arrow & text (text placed to the left of its arrow, strictly right of dim_x_real)
    ax.annotate("", xy=(dim_x_app, water_level), xytext=(dim_x_app, y_app + coin_h/2),
                arrowprops=dict(arrowstyle="<->", color=DEEP["lav"], lw=2.2))
    ax.text(dim_x_app - 0.15, (water_level + y_app) / 2, "Apparent\ndepth", fontsize=14, color=DEEP["lav"],
            ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1))

    # Real depth arrow & text (text placed to the left of dim_x_real)
    ax.annotate("", xy=(dim_x_real, water_level), xytext=(dim_x_real, y_real),
                arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=2.2))
    ax.text(dim_x_real - 0.15, (water_level + y_real) / 2, "Real\ndepth", fontsize=14, color=DEEP["blue"],
            ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1))

    # Medium labels
    ax.text(3.5, 5.5, "Air", fontsize=16, color=INK, fontweight="bold")
    ax.text(3.5, 4.2, "Water", fontsize=16, color=DEEP["blue"], fontweight="bold")

    save(fig, out)
