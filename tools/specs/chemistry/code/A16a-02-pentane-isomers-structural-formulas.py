from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    # Title
    ax.text(6, 4.9, r"Isomers of Pentane ($\mathrm{C_5H_{12}}$)", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Box styling
    def draw_bond(p1, p2, color=INK, lw=2.5):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, solid_capstyle="round", zorder=1)

    def draw_atom(p, text, color=INK, bg="white"):
        ax.text(p[0], p[1], text, ha="center", va="center", fontsize=15, 
                fontweight="bold", color=color, zorder=2,
                bbox=dict(boxstyle="square,pad=0.15", fc=bg, ec="none"))

    # Panel 1: Pentane (straight zigzag chain)
    # Centers around x = 2.0, y = 2.4
    x1, y1 = 2.0, 2.5
    p1_pts = [
        (x1 - 1.4, y1 - 0.5),
        (x1 - 0.7, y1 + 0.3),
        (x1,       y1 - 0.5),
        (x1 + 0.7, y1 + 0.3),
        (x1 + 1.4, y1 - 0.5)
    ]
    for i in range(len(p1_pts) - 1):
        draw_bond(p1_pts[i], p1_pts[i+1], color=DEEP["blue"])

    draw_atom(p1_pts[0], r"$\mathrm{H_3C}$", color=DEEP["blue"])
    draw_atom(p1_pts[1], r"$\mathrm{CH_2}$", color=INK)
    draw_atom(p1_pts[2], r"$\mathrm{CH_2}$", color=INK)
    draw_atom(p1_pts[3], r"$\mathrm{CH_2}$", color=INK)
    draw_atom(p1_pts[4], r"$\mathrm{CH_3}$", color=DEEP["blue"])

    ax.text(x1, 1.0, "pentane", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(x1, 0.5, "(n-pentane)", ha="center", va="center", fontsize=14, color=GREY)

    # Panel 2: 2-Methylbutane (isopentane)
    # Centers around x = 6.0, y = 2.5
    x2, y2 = 6.0, 2.5
    # Main 4-carbon chain
    p2_pts = [
        (x2 - 1.2, y2 - 0.4),
        (x2 - 0.4, y2 + 0.3),
        (x2 + 0.4, y2 - 0.4),
        (x2 + 1.2, y2 + 0.3)
    ]
    for i in range(len(p2_pts) - 1):
        draw_bond(p2_pts[i], p2_pts[i+1], color=DEEP["green"])

    # Branch on second carbon (x2 - 0.4, y2 + 0.3)
    p2_branch = (x2 - 0.4, y2 + 1.3)
    draw_bond(p2_pts[1], p2_branch, color=DEEP["green"])

    draw_atom(p2_pts[0], r"$\mathrm{H_3C}$", color=DEEP["green"])
    draw_atom(p2_pts[1], r"$\mathrm{CH}$", color=INK)
    draw_atom(p2_pts[2], r"$\mathrm{CH_2}$", color=INK)
    draw_atom(p2_pts[3], r"$\mathrm{CH_3}$", color=DEEP["green"])
    draw_atom(p2_branch, r"$\mathrm{CH_3}$", color=DEEP["green"])

    ax.text(x2, 1.0, "2-methylbutane", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(x2, 0.5, "(isopentane)", ha="center", va="center", fontsize=14, color=GREY)

    # Panel 3: 2,2-Dimethylpropane (neopentane)
    # Central carbon bonded to four methyl groups in a cross
    x3, y3 = 10.0, 2.5
    d = 1.05
    c_center = (x3, y3)
    c_left   = (x3 - d, y3)
    c_right  = (x3 + d, y3)
    c_up     = (x3, y3 + d)
    c_down   = (x3, y3 - d)

    draw_bond(c_center, c_left, color=DEEP["orange"])
    draw_bond(c_center, c_right, color=DEEP["orange"])
    draw_bond(c_center, c_up, color=DEEP["orange"])
    draw_bond(c_center, c_down, color=DEEP["orange"])

    draw_atom(c_center, r"$\mathrm{C}$", color=INK)
    draw_atom(c_left,   r"$\mathrm{H_3C}$", color=DEEP["orange"])
    draw_atom(c_right,  r"$\mathrm{CH_3}$", color=DEEP["orange"])
    draw_atom(c_up,     r"$\mathrm{CH_3}$", color=DEEP["orange"])
    draw_atom(c_down,   r"$\mathrm{CH_3}$", color=DEEP["orange"])

    ax.text(x3, 1.0, "2,2-dimethylpropane", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(x3, 0.5, "(neopentane)", ha="center", va="center", fontsize=14, color=GREY)

    # Divider lines
    ax.plot([3.9, 3.9], [0.8, 4.4], color=GREY, lw=1, ls="--", alpha=0.5)
    ax.plot([8.1, 8.1], [0.8, 4.4], color=GREY, lw=1, ls="--", alpha=0.5)

    save(fig, out)
