from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 13.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    x_sun, y_sun, r_sun = 0.8, 0.0, 2.0
    x_moon, y_moon, r_moon = 7.0, 0.0, 0.735
    x_earth, y_earth, r_earth = 11.6, 0.0, 1.15

    x_vertex = 10.65
    m_top = - r_sun / (x_vertex - x_sun)
    r_moon = r_sun + m_top * (x_moon - x_sun) 

    x_end = 12.5
    
    y_umb_top_end = r_sun + m_top * (x_end - x_sun)
    y_umb_bot_end = -y_umb_top_end

    m_cross_top = (r_moon - (-r_sun)) / (x_moon - x_sun)
    y_pen_top_end = -r_sun + m_cross_top * (x_end - x_sun)

    m_cross_bot = (-r_moon - r_sun) / (x_moon - x_sun)
    y_pen_bot_end = r_sun + m_cross_bot * (x_end - x_sun)

    pen_upper_poly = [
        (x_moon, r_moon),
        (x_end, y_pen_top_end),
        (x_end, y_umb_top_end),
    ]
    poly_pen_up = patches.Polygon(pen_upper_poly, closed=True, facecolor=GREY, alpha=0.3, edgecolor=None, zorder=2)
    ax.add_patch(poly_pen_up)

    pen_lower_poly = [
        (x_moon, -r_moon),
        (x_end, y_pen_bot_end),
        (x_end, y_umb_bot_end),
    ]
    poly_pen_down = patches.Polygon(pen_lower_poly, closed=True, facecolor=GREY, alpha=0.3, edgecolor=None, zorder=2)
    ax.add_patch(poly_pen_down)

    umbra_poly = [
        (x_moon, r_moon),
        (x_end, y_umb_top_end),
        (x_end, y_umb_bot_end),
        (x_moon, -r_moon)
    ]
    poly_umbra = patches.Polygon(umbra_poly, closed=True, facecolor=INK, alpha=0.8, edgecolor=None, zorder=3)
    ax.add_patch(poly_umbra)

    ray_kw = dict(color=DEEP["orange"], lw=1.5, ls="--", alpha=0.9, zorder=4)
    ax.plot([x_sun, x_end], [r_sun, y_umb_top_end], **ray_kw)
    ax.plot([x_sun, x_end], [-r_sun, y_umb_bot_end], **ray_kw)
    ax.plot([x_sun, x_end], [-r_sun, y_pen_top_end], **ray_kw)
    ax.plot([x_sun, x_end], [r_sun, y_pen_bot_end], **ray_kw)

    sun = patches.Circle((x_sun, y_sun), r_sun, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5, zorder=6)
    ax.add_patch(sun)

    moon = patches.Circle((x_moon, y_moon), r_moon, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=6)
    ax.add_patch(moon)

    earth = patches.Circle((x_earth, y_earth), r_earth, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=6)
    ax.add_patch(earth)

    x_earth_front = x_earth - r_earth
    spot_h = max(0.08, abs(r_sun + m_top * (x_earth_front - x_sun)))
    umbra_spot = patches.Ellipse((x_earth_front + 0.02, 0.0), width=0.08, height=2 * spot_h, facecolor=INK, edgecolor=None, zorder=7)
    ax.add_patch(umbra_spot)

    ax.text(x_sun, -r_sun - 0.45, "Sun", ha="center", va="top", fontsize=16, color=INK, fontweight="bold")
    ax.text(x_moon, -r_moon - 0.55, "Moon", ha="center", va="top", fontsize=15, color=INK, fontweight="bold")
    ax.text(x_earth, -r_earth - 0.45, "Earth", ha="center", va="top", fontsize=16, color=INK, fontweight="bold")

    ax.annotate(
        "Penumbra (Partial eclipse)",
        xy=(9.3, 0.55),
        xytext=(8.0, 2.5),
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        zorder=8,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35")
    )

    ax.annotate(
        "Umbra (Total eclipse)",
        xy=(9.3, 0.0),
        xytext=(7.5, -2.5),
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        zorder=8,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35")
    )

    save(fig, out)
