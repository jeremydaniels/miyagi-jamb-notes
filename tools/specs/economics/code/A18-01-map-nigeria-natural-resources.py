from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

def draw_derrick(ax, x, y, size=0.35, color=INK):
    # Oil derrick frame
    h = size * 1.6
    w = size
    pts = [[x - w/2, y], [x - w/4, y + h], [x + w/4, y + h], [x + w/2, y]]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=2)
    # Crossbars
    ax.plot([x - w*0.4, x + w*0.4], [y + h*0.35, y + h*0.35], color=color, lw=1.5)
    ax.plot([x - w*0.3, x + w*0.3], [y + h*0.7, y + h*0.7], color=color, lw=1.5)
    # Crosses
    ax.plot([x - w*0.45, x + w*0.4], [y + h*0.05, y + h*0.35], color=color, lw=1.2)
    ax.plot([x + w*0.45, x - w*0.4], [y + h*0.05, y + h*0.35], color=color, lw=1.2)
    ax.plot([x - w*0.4, x + w*0.3], [y + h*0.35, y + h*0.7], color=color, lw=1.2)
    ax.plot([x + w*0.4, x - w*0.3], [y + h*0.35, y + h*0.7], color=color, lw=1.2)
    # Crown block
    ax.plot([x, x], [y + h, y + h*1.2], color=color, lw=2)

def draw_coal(ax, x, y, size=0.35, color=INK):
    # Lump of coal: irregular dark polygon
    pts = np.array([
        [x - size*0.5, y - size*0.2],
        [x - size*0.6, y + size*0.1],
        [x - size*0.3, y + size*0.45],
        [x + size*0.1, y + size*0.5],
        [x + size*0.5, y + size*0.25],
        [x + size*0.6, y - size*0.1],
        [x + size*0.3, y - size*0.35],
        [x - size*0.2, y - size*0.4]
    ])
    poly = Polygon(pts, closed=True, fc=color, ec=color, lw=1.5, zorder=4)
    ax.add_patch(poly)
    # Highlight facet lines
    ax.plot([x - size*0.3, x, x + size*0.3], [y + size*0.45, y, y - size*0.35], color="white", lw=1.2, zorder=5)

def draw_ingot(ax, x, y, size=0.45, color=DEEP["orange"]):
    # Trapezoidal metal ingot
    w_top = size * 0.7
    w_bot = size * 1.1
    h = size * 0.45
    pts = [
        [x - w_top/2, y + h/2],
        [x + w_top/2, y + h/2],
        [x + w_bot/2, y - h/2],
        [x - w_bot/2, y - h/2]
    ]
    poly = Polygon(pts, closed=True, fc=color, ec=INK, lw=1.8, zorder=4)
    ax.add_patch(poly)
    # Shading line
    ax.plot([x - w_top/2 + 0.05, x + w_top/2 - 0.05], [y + h/2 - 0.05, y + h/2 - 0.05], color="white", lw=1.5, zorder=5)

def draw_tree(ax, x, y, size=0.35, color=DEEP["green"]):
    # Trunk
    tw = size * 0.15
    th = size * 0.35
    trunk = Rectangle((x - tw/2, y), tw, th, fc="#8B5A2B", ec=INK, lw=1.2, zorder=3)
    ax.add_patch(trunk)
    # Foliage (cloud of circles or triangle layers)
    c1 = Circle((x, y + th + size*0.3), size*0.38, fc=color, ec=INK, lw=1.5, zorder=4)
    c2 = Circle((x - size*0.2, y + th + size*0.18), size*0.28, fc=color, ec=INK, lw=1.5, zorder=4)
    c3 = Circle((x + size*0.2, y + th + size*0.18), size*0.28, fc=color, ec=INK, lw=1.5, zorder=4)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.add_patch(c3)

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)

    # Base Nigeria outline from natural earth helpers
    try:
        polys = nigeria_poly()
        for poly in polys:
            x_pts, y_pts = zip(*poly)
            ax.fill(x_pts, y_pts, color=CREAM, zorder=1)
            ax.plot(x_pts, y_pts, color=INK, lw=2.5, zorder=2)
    except Exception:
        # Fallback approximate polygon if helper differs
        nig_pts = [
            (2.7, 6.5), (3.6, 6.4), (4.3, 6.3), (5.5, 5.5), (6.5, 4.3),
            (7.5, 4.4), (8.5, 4.7), (9.0, 5.0), (10.0, 6.0), (11.5, 6.8),
            (12.0, 7.3), (13.5, 8.5), (14.5, 10.0), (14.6, 12.0), (14.0, 13.0),
            (13.0, 13.5), (10.0, 13.8), (8.0, 13.5), (6.0, 13.8), (4.0, 13.5),
            (3.6, 11.5), (3.0, 10.5), (2.7, 9.0), (2.7, 6.5)
        ]
        poly_shape = Polygon(nig_pts, closed=True, fc=CREAM, ec=INK, lw=2.5, zorder=1)
        ax.add_patch(poly_shape)

    # River Niger and Benue (Y-shaped river system for context)
    r_niger_x = [3.6, 4.5, 5.0, 6.0, 6.7, 6.7]
    r_niger_y = [11.5, 10.0, 9.0, 8.0, 7.8, 5.5]
    r_benue_x = [6.7, 8.0, 9.5, 11.5, 12.5]
    r_benue_y = [7.8, 8.0, 8.8, 9.3, 9.5]
    ax.plot(r_niger_x, r_niger_y, color=DEEP["blue"], lw=2.2, alpha=0.7, zorder=2)
    ax.plot(r_benue_x, r_benue_y, color=DEEP["blue"], lw=2.2, alpha=0.7, zorder=2)

    # Simplified internal regional boundaries
    borders = [
        # SW boundary
        [(4.5, 6.4), (5.0, 7.0), (6.7, 7.2)],
        # Niger Delta separation
        [(5.0, 6.0), (6.0, 5.8), (7.5, 5.6), (8.5, 5.0)],
        # SE boundary
        [(6.7, 7.2), (7.5, 6.8), (8.5, 6.5), (9.0, 6.0)],
        # Central / North
        [(3.6, 10.0), (6.7, 9.0), (10.0, 9.5), (13.0, 10.5)],
        [(6.7, 9.0), (6.7, 7.8)]
    ]
    for b in borders:
        bx, by = zip(*b)
        ax.plot(bx, by, color=GREY, lw=1.2, ls="--", zorder=2)

    # Draw Resource Icons & Labels

    # 1. Crude Oil (Niger Delta: Bayelsa, Rivers, Delta) ~ (6.0, 4.8) & (6.8, 4.7)
    draw_derrick(ax, 5.8, 4.75, size=0.35)
    draw_derrick(ax, 6.6, 4.6, size=0.35)
    ax.text(6.2, 3.8, "Crude Oil", fontsize=15, weight="bold", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1), zorder=6)
    ax.annotate("", xy=(6.2, 4.5), xytext=(6.2, 4.15),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=5)

    # 2. Coal (Enugu) ~ (7.5, 6.4)
    draw_coal(ax, 7.5, 6.45, size=0.45)
    ax.text(8.7, 6.4, "Coal", fontsize=15, weight="bold", color=INK, ha="left", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1), zorder=6)
    ax.annotate("", xy=(7.8, 6.45), xytext=(8.6, 6.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=5)

    # 3. Tin/Columbite (Jos) ~ (8.9, 9.9)
    draw_ingot(ax, 8.9, 9.9, size=0.5)
    ax.text(9.7, 10.2, "Tin/Columbite", fontsize=15, weight="bold", color=INK, ha="left", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1), zorder=6)
    ax.annotate("", xy=(9.2, 9.95), xytext=(9.6, 10.15),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=5)

    # 4. Timber (Edo / Ondo) ~ (5.2, 6.8)
    draw_tree(ax, 5.0, 6.7, size=0.38)
    draw_tree(ax, 5.5, 6.6, size=0.32)
    ax.text(3.9, 7.2, "Timber", fontsize=15, weight="bold", color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1), zorder=6)
    ax.annotate("", xy=(4.9, 6.9), xytext=(4.0, 7.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=5)

    # Surrounding context labels
    ax.text(5.5, 3.2, "Gulf of Guinea", fontsize=14, fontstyle="italic", color=DEEP["blue"], ha="center")
    ax.text(6.8, 8.2, "R. Niger", fontsize=14, fontstyle="italic", color=DEEP["blue"], ha="right")
    ax.text(9.0, 8.5, "R. Benue", fontsize=14, fontstyle="italic", color=DEEP["blue"], ha="left")

    # Title & Legend Box
    ax.text(8.5, 14.5, "Major Natural Resources of Nigeria", fontsize=18, weight="bold", color=INK, ha="center")
    ax.text(8.5, 2.5, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic", color=GREY, ha="center")

    # Limits and formatting
    ax.set_xlim(1.5, 15.5)
    ax.set_ylim(2.2, 15.2)
    ax.set_aspect("equal")
    ax.axis("off")

    save(fig, out)
