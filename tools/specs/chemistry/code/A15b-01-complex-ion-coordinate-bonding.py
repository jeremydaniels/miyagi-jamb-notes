from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)

    # Title
    ax.text(0, 4.7, "Tetraamminecopper(II) ion, [Cu(NH₃)₄]²⁺",
            fontsize=17, fontweight="bold", color=INK, ha="center", va="center")

    # Central metal ion: Cu2+
    circle_cu = plt.Circle((0, 0), 0.75, color=LAV, ec=DEEP["lav"], lw=2, zorder=2)
    ax.add_patch(circle_cu)
    ax.text(0, 0, "Cu²⁺", fontsize=18, fontweight="bold", color=INK, ha="center", va="center", zorder=3)

    # 4 NH3 ligands in a square planar arrangement: Top, Bottom, Left, Right
    # Arrow styles
    arrow_kw = dict(arrowstyle="-|>", mutation_scale=18, color=DEEP["blue"], lw=2.5)

    # Left Ligand: center at x = -2.8, text "H₃N"
    ax.text(-2.8, 0, "H₃N", fontsize=17, fontweight="bold", color=INK, ha="center", va="center")
    # Arrow from N (around x = -2.2) to Cu (around x = -0.85)
    ax.annotate("", xy=(-0.85, 0), xytext=(-2.2, 0), arrowprops=arrow_kw)

    # Right Ligand: center at x = 2.8, text "NH₃"
    ax.text(2.8, 0, "NH₃", fontsize=17, fontweight="bold", color=INK, ha="center", va="center")
    # Arrow from N (around x = 2.2) to Cu (around x = 0.85)
    ax.annotate("", xy=(0.85, 0), xytext=(2.2, 0), arrowprops=arrow_kw)

    # Top Ligand: center at y = 2.7, text "NH₃"
    ax.text(0, 2.7, "NH₃", fontsize=17, fontweight="bold", color=INK, ha="center", va="center")
    # Arrow from N (around y = 2.2) to Cu (around y = 0.85)
    ax.annotate("", xy=(0, 0.85), xytext=(0, 2.2), arrowprops=arrow_kw)

    # Bottom Ligand: center at y = -2.7, text "NH₃"
    ax.text(0, -2.7, "NH₃", fontsize=17, fontweight="bold", color=INK, ha="center", va="center")
    # Arrow from N (around y = -2.2) to Cu (around y = -0.85)
    ax.annotate("", xy=(0, -0.85), xytext=(0, -2.2), arrowprops=arrow_kw)

    # Large square brackets enclosing the structure
    bx_l = -3.7
    bx_r = 3.7
    by_top = 3.7
    by_bot = -3.7
    cap = 0.6

    # Left bracket lines: (bx_l + cap, by_top) -> (bx_l, by_top) -> (bx_l, by_bot) -> (bx_l + cap, by_bot)
    ax.plot([bx_l + cap, bx_l, bx_l, bx_l + cap],
            [by_top, by_top, by_bot, by_bot],
            color=INK, lw=2.5, solid_capstyle='butt')

    # Right bracket lines: (bx_r - cap, by_top) -> (bx_r, by_top) -> (bx_r, by_bot) -> (bx_r - cap, by_bot)
    ax.plot([bx_r - cap, bx_r, bx_r, bx_r - cap],
            [by_top, by_top, by_bot, by_bot],
            color=INK, lw=2.5, solid_capstyle='butt')

    # 2+ charge outside upper right corner of bracket
    ax.text(bx_r + 0.2, by_top + 0.1, "2+", fontsize=20, fontweight="bold", color=INK, ha="left", va="bottom")

    # Annotations explaining the parts
    # Label for coordinate bond
    ax.annotate("Coordinate bond\n(lone pair donation)",
                xy=(1.5, 0), xytext=(2.6, -1.8),
                fontsize=14, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Label for square planar geometry
    ax.text(0, -4.6, "Square planar geometry",
            fontsize=15, fontstyle="italic", color=INK, ha="center", va="center",
            bbox=dict(fc=CREAM, ec="none", boxstyle="round,pad=0.3"))

    save(fig, out)
