from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 5.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.axis('off')

    # Common styling
    lw = 2.5
    lbl_font = dict(fontsize=15, color=INK, ha='center', va='center')
    title_font = dict(fontsize=16, color=INK, ha='center', va='bottom', weight='bold')

    # -------------------------------------------------------------
    # 1. Right-angled triangle
    # -------------------------------------------------------------
    # Vertices
    r_A = np.array([1.2, 1.2])
    r_B = np.array([4.0, 1.2])
    r_C = np.array([1.2, 4.2])

    poly1 = Polygon([r_A, r_B, r_C], closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=lw, zorder=2)
    ax.add_patch(poly1)

    # Right angle square indicator at r_A
    sq_size = 0.35
    ax.plot([r_A[0], r_A[0] + sq_size, r_A[0] + sq_size],
            [r_A[1] + sq_size, r_A[1] + sq_size, r_A[1]],
            color=DEEP["blue"], lw=1.8, zorder=3)

    # Labels for right-angled triangle
    ax.text(2.6, 0.75, "base $b$", **lbl_font)
    ax.text(0.65, 2.7, "height $h$", **lbl_font)
    ax.text(2.6, 4.7, "Right-angled", **title_font)

    # -------------------------------------------------------------
    # 2. Isosceles triangle
    # -------------------------------------------------------------
    # Vertices
    i_left = np.array([4.8, 1.2])
    i_right = np.array([7.6, 1.2])
    i_top = np.array([6.2, 4.2])
    i_mid = np.array([6.2, 1.2])

    poly2 = Polygon([i_left, i_right, i_top], closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=lw, zorder=2)
    ax.add_patch(poly2)

    # Dashed height line
    ax.plot([i_top[0], i_mid[0]], [i_top[1], i_mid[1]], color=DEEP["green"], lw=2.0, ls='--', zorder=3)

    # Right angle square at base of height line
    ax.plot([i_mid[0], i_mid[0] + sq_size, i_mid[0] + sq_size],
            [i_mid[1] + sq_size, i_mid[1] + sq_size, i_mid[1]],
            color=DEEP["green"], lw=1.5, zorder=3)

    # Equal side tick marks
    def draw_tick(p1, p2):
        mid = (p1 + p2) / 2
        vec = p2 - p1
        normal = np.array([-vec[1], vec[0]])
        normal = normal / np.linalg.norm(normal) * 0.15
        ax.plot([mid[0] - normal[0], mid[0] + normal[0]],
                [mid[1] - normal[1], mid[1] + normal[1]],
                color=DEEP["green"], lw=2.0, zorder=4)

    draw_tick(i_left, i_top)
    draw_tick(i_right, i_top)

    # Height label
    ax.text(6.5, 2.7, "$h$", bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none'), **lbl_font)
    ax.text(6.2, 0.75, "base", **lbl_font)
    ax.text(6.2, 4.7, "Isosceles", **title_font)

    # -------------------------------------------------------------
    # 3. Scalene triangle
    # -------------------------------------------------------------
    # Vertices
    s_A = np.array([8.4, 1.2])
    s_B = np.array([11.4, 1.2])
    s_C = np.array([9.4, 4.2])

    poly3 = Polygon([s_A, s_B, s_C], closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=lw, zorder=2)
    ax.add_patch(poly3)

    # Labels for sides a, b, c
    # Side c: base (A -> B)
    ax.text(9.9, 0.75, "$b$", **lbl_font)
    # Side b: left-ish (A -> C)
    ax.text(8.5, 2.9, "$a$", **lbl_font)
    # Side a: right (C -> B)
    ax.text(10.7, 2.9, "$c$", **lbl_font)

    ax.text(9.9, 4.7, "Scalene", **title_font)

    save(fig, out)
