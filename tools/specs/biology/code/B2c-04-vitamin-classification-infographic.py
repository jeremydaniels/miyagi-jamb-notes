from style import *
import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path

def draw_drop(ax, cx, cy, r, color, border_color):
    # Teardrop shape using two cubic Bezier curves
    verts = [
        (cx, cy + 1.35 * r),           # tip
        (cx - 1.2 * r, cy + 0.3 * r),  # left shoulder control
        (cx - 1.2 * r, cy - 1.0 * r),  # left bottom control
        (cx, cy - 1.0 * r),            # bottom center
        (cx + 1.2 * r, cy - 1.0 * r),  # right bottom control
        (cx + 1.2 * r, cy + 0.3 * r),  # right shoulder control
        (cx, cy + 1.35 * r),           # back to tip
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
    ]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=color, edgecolor=border_color, lw=2, zorder=3)
    ax.add_patch(patch)

def draw_food_A(ax, x, y):
    # Carrot: orange wedge + green top
    c_pts = np.array([[x - 0.5, y + 0.25], [x - 0.3, y + 0.35], [x - 0.8, y - 0.35]])
    poly = patches.Polygon(c_pts, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=4)
    ax.add_patch(poly)
    ax.plot([x - 0.4, x - 0.35], [y + 0.3, y + 0.48], color=DEEP["green"], lw=2, zorder=5)
    ax.plot([x - 0.45, x - 0.5], [y + 0.28, y + 0.45], color=DEEP["green"], lw=2, zorder=5)

    # Red palm oil flask/bottle
    b_pts = np.array([
        [x + 0.3, y - 0.35], [x + 0.7, y - 0.35],
        [x + 0.65, y + 0.05], [x + 0.55, y + 0.2],
        [x + 0.55, y + 0.38], [x + 0.45, y + 0.38],
        [x + 0.45, y + 0.2], [x + 0.35, y + 0.05]
    ])
    flask = patches.Polygon(b_pts, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5, zorder=4)
    ax.add_patch(flask)
    cap = patches.Rectangle((x + 0.42, y + 0.38), 0.16, 0.07, facecolor=DEEP["pink"], edgecolor=DEEP["pink"], zorder=5)
    ax.add_patch(cap)

def draw_food_D(ax, x, y):
    # Sun
    sx, sy = x - 0.55, y
    ax.add_patch(patches.Circle((sx, sy), 0.2, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5, zorder=4))
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        dx, dy = np.cos(angle), np.sin(angle)
        ax.plot([sx + 0.26 * dx, sx + 0.38 * dx], [sy + 0.26 * dy, sy + 0.38 * dy], color=DEEP["orange"], lw=1.5, zorder=4)

    # Egg (boiled egg half)
    ex, ey = x + 0.5, y
    ax.add_patch(patches.Ellipse((ex, ey), 0.55, 0.7, facecolor="#F8F9FA", edgecolor=GREY, lw=1.5, zorder=4))
    ax.add_patch(patches.Circle((ex, ey - 0.05), 0.2, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=5))

def draw_food_E(ax, x, y):
    # Vegetable oil bottle
    bx, by = x, y - 0.05
    b_pts = np.array([
        [bx - 0.25, by - 0.3], [bx + 0.25, by - 0.3],
        [bx + 0.25, by + 0.15], [bx + 0.12, by + 0.28],
        [bx + 0.12, by + 0.42], [bx - 0.12, by + 0.42],
        [bx - 0.12, by + 0.28], [bx - 0.25, by + 0.15]
    ])
    bot = patches.Polygon(b_pts, closed=True, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5, zorder=4)
    ax.add_patch(bot)
    cap = patches.Rectangle((bx - 0.14, by + 0.42), 0.28, 0.08, facecolor=DEEP["green"], edgecolor=DEEP["green"], zorder=5)
    ax.add_patch(cap)
    label_rect = patches.Rectangle((bx - 0.2, by - 0.15), 0.4, 0.2, facecolor="white", edgecolor=GREY, lw=1, zorder=5)
    ax.add_patch(label_rect)
    ax.plot([bx - 0.1, bx + 0.1], [by - 0.05, by - 0.05], color=DEEP["green"], lw=2, zorder=6)

def draw_food_K(ax, x, y):
    # Green leaves
    lx, ly = x - 0.2, y - 0.1
    ax.add_patch(patches.Ellipse((lx, ly + 0.15), 0.35, 0.65, angle=25, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, zorder=4))
    ax.plot([lx - 0.1, lx + 0.1], [ly - 0.15, ly + 0.4], color=DEEP["green"], lw=1.2, zorder=5)

    lx2, ly2 = x + 0.3, y - 0.05
    ax.add_patch(patches.Ellipse((lx2, ly2 + 0.1), 0.35, 0.6, angle=-30, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, zorder=4))
    ax.plot([lx2 + 0.08, lx2 - 0.08], [ly2 - 0.15, ly2 + 0.35], color=DEEP["green"], lw=1.2, zorder=5)

def draw_food_B1(ax, x, y):
    # Rice bowl + beans
    rx, ry = x - 0.4, y
    bowl_arc = patches.Arc((rx, ry), 0.65, 0.5, theta1=180, theta2=360, edgecolor=GREY, facecolor=CREAM, lw=2, zorder=4)
    ax.add_patch(bowl_arc)
    ax.add_patch(patches.Ellipse((rx, ry), 0.65, 0.2, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=5))
    ax.plot([rx - 0.2, rx + 0.2], [ry + 0.05, ry + 0.05], color=DEEP["orange"], lw=1.5, zorder=6)

    # Beans
    bx, by = x + 0.45, y
    ax.add_patch(patches.Ellipse((bx - 0.12, by - 0.1), 0.28, 0.16, angle=20, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.3, zorder=4))
    ax.add_patch(patches.Ellipse((bx + 0.15, by + 0.08), 0.28, 0.16, angle=-25, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.3, zorder=4))
    ax.add_patch(patches.Ellipse((bx - 0.05, by + 0.2), 0.25, 0.15, angle=40, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.3, zorder=4))

def draw_food_B2(ax, x, y):
    # Milk carton / bottle + egg
    mx, my = x - 0.45, y
    m_pts = np.array([
        [mx - 0.22, my - 0.35], [mx + 0.22, my - 0.35],
        [mx + 0.22, my + 0.2], [mx + 0.15, my + 0.38],
        [mx - 0.15, my + 0.38], [mx - 0.22, my + 0.2]
    ])
    carton = patches.Polygon(m_pts, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    ax.add_patch(carton)
    ax.text(mx, my - 0.05, "M", ha="center", va="center", fontsize=9, color=DEEP["blue"], weight="bold", zorder=5)

    # Egg
    ex, ey = x + 0.45, y - 0.05
    ax.add_patch(patches.Ellipse((ex, ey), 0.4, 0.55, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5, zorder=4))

def draw_food_B3(ax, x, y):
    # Groundnuts (peanuts) + meat steak
    gx, gy = x - 0.5, y
    ax.add_patch(patches.Ellipse((gx - 0.08, gy + 0.1), 0.2, 0.26, angle=15, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.3, zorder=4))
    ax.add_patch(patches.Ellipse((gx + 0.05, gy - 0.1), 0.2, 0.26, angle=-20, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.3, zorder=4))

    # Meat
    mx, my = x + 0.4, y
    ax.add_patch(patches.Ellipse((mx, my), 0.65, 0.42, angle=-10, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5, zorder=4))
    ax.add_patch(patches.Circle((mx - 0.08, my + 0.02), 0.09, facecolor="white", edgecolor=GREY, lw=1.2, zorder=5))

def draw_food_B12(ax, x, y):
    # Liver + fish
    lx, ly = x - 0.45, y
    ax.add_patch(patches.Ellipse((lx, ly), 0.6, 0.35, angle=20, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5, zorder=4))

    # Fish
    fx, fy = x + 0.4, y
    f_body = patches.Ellipse((fx, fy), 0.6, 0.3, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    ax.add_patch(f_body)
    f_tail = patches.Polygon([[fx + 0.25, fy], [fx + 0.48, fy + 0.18], [fx + 0.48, fy - 0.18]],
                             closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    ax.add_patch(f_tail)
    ax.plot([fx - 0.18], [fy + 0.04], marker='o', markersize=3, color=INK, zorder=5)

def draw_food_C(ax, x, y):
    # Orange + guava
    ox, oy = x - 0.45, y
    ax.add_patch(patches.Circle((ox, oy), 0.28, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=4))
    ax.plot([ox, ox + 0.06], [oy + 0.28, oy + 0.38], color=DEEP["green"], lw=2, zorder=5)

    # Guava
    gx, gy = x + 0.45, y
    ax.add_patch(patches.Ellipse((gx, gy), 0.52, 0.6, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, zorder=4))
    ax.plot([gx, gx - 0.05], [gy + 0.3, gy + 0.4], color=DEEP["green"], lw=2, zorder=5)

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Column background cards
    card_l = patches.FancyBboxPatch((0.5, 0.5), 5.2, 9.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                    facecolor="#FCFBF7", edgecolor=GREY, lw=1.5, zorder=1)
    card_r = patches.FancyBboxPatch((6.3, 0.5), 5.2, 9.0, boxstyle="round,pad=0.2,rounding_size=0.4",
                                    facecolor="#F7FAFC", edgecolor=GREY, lw=1.5, zorder=1)
    ax.add_patch(card_l)
    ax.add_patch(card_r)

    # Column Headers
    header_l = patches.FancyBboxPatch((0.8, 8.5), 4.6, 0.75, boxstyle="round,pad=0.1,rounding_size=0.2",
                                      facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5, zorder=2)
    header_r = patches.FancyBboxPatch((6.6, 8.5), 4.6, 0.75, boxstyle="round,pad=0.1,rounding_size=0.2",
                                      facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=2)
    ax.add_patch(header_l)
    ax.add_patch(header_r)

    ax.text(3.1, 8.87, "fat-soluble", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, zorder=3)
    ax.text(8.9, 8.87, "water-soluble", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, zorder=3)

    # Left Column: Fat-soluble (A, D, E, K) - 4 items
    fat_y = [7.2, 5.3, 3.4, 1.5]
    fat_items = [
        ("A", "carrot and red palm oil", draw_food_A),
        ("D", "sun and egg", draw_food_D),
        ("E", "vegetable oil bottle", draw_food_E),
        ("K", "green leaves", draw_food_K),
    ]

    for y, (vit, desc, draw_func) in zip(fat_y, fat_items):
        # Divider line
        if y < 7.0:
            ax.plot([0.8, 5.4], [y + 0.95, y + 0.95], color=GREY, lw=0.8, linestyle="--", zorder=2)
        
        # Yellow oil drop icon
        drop_x = 1.3
        draw_drop(ax, drop_x, y + 0.1, 0.42, CREAM, DEEP["orange"])
        ax.text(drop_x, y - 0.05, vit, ha="center", va="center", fontsize=14, fontweight="bold", color=INK, zorder=4)

        # Food picture
        food_x = 3.6
        draw_func(ax, food_x, y + 0.18)

        # Text label
        ax.text(food_x, y - 0.4, desc, ha="center", va="center", fontsize=11, color=INK, zorder=4)

    # Right Column: Water-soluble (B1, B2, B3, B12, C) - 5 items
    water_y = [7.5, 6.0, 4.5, 3.0, 1.5]
    water_items = [
        ("B1", "unpolished rice and beans", draw_food_B1),
        ("B2", "milk and egg", draw_food_B2),
        ("B3", "groundnuts and meat", draw_food_B3),
        ("B12", "liver and fish", draw_food_B12),
        ("C", "orange and guava", draw_food_C),
    ]

    for y, (vit, desc, draw_func) in zip(water_y, water_items):
        # Divider line
        if y < 7.0:
            ax.plot([6.6, 11.2], [y + 0.75, y + 0.75], color=GREY, lw=0.8, linestyle="--", zorder=2)

        # Blue water drop icon
        drop_x = 7.1
        draw_drop(ax, drop_x, y + 0.08, 0.38, BLUE, DEEP["blue"])
        font_sz = 12 if len(vit) > 2 else 13
        ax.text(drop_x, y - 0.05, vit, ha="center", va="center", fontsize=font_sz, fontweight="bold", color=INK, zorder=4)

        # Food picture
        food_x = 9.4
        draw_func(ax, food_x, y + 0.16)

        # Text label
        ax.text(food_x, y - 0.38, desc, ha="center", va="center", fontsize=11, color=INK, zorder=4)

    save(fig, out)
