from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Helper function to draw human icon (female or male)
    def draw_person(x, y, is_female, scale=0.8, fill_color=CREAM):
        head_radius = 0.28 * scale
        head_cy = y + 0.35 * scale
        head = patches.Circle((x, head_cy), head_radius, fc=fill_color, ec=INK, lw=1.5, zorder=5)
        ax.add_patch(head)
        
        if is_female:
            # Triangular dress / body
            poly = patches.Polygon([
                [x, head_cy - head_radius],
                [x - 0.45 * scale, y - 0.5 * scale],
                [x + 0.45 * scale, y - 0.5 * scale]
            ], fc=fill_color, ec=INK, lw=1.5, zorder=5)
            ax.add_patch(poly)
            # Legs
            ax.plot([x - 0.18 * scale, x - 0.18 * scale], [y - 0.5 * scale, y - 0.8 * scale], color=INK, lw=1.5, zorder=4)
            ax.plot([x + 0.18 * scale, x + 0.18 * scale], [y - 0.5 * scale, y - 0.8 * scale], color=INK, lw=1.5, zorder=4)
        else:
            # Torso rectangle
            rect = patches.Rectangle(
                (x - 0.32 * scale, y - 0.45 * scale),
                0.64 * scale, 0.52 * scale,
                fc=fill_color, ec=INK, lw=1.5, zorder=5
            )
            ax.add_patch(rect)
            # Legs
            ax.plot([x - 0.18 * scale, x - 0.18 * scale], [y - 0.45 * scale, y - 0.8 * scale], color=INK, lw=1.5, zorder=4)
            ax.plot([x + 0.18 * scale, x + 0.18 * scale], [y - 0.45 * scale, y - 0.8 * scale], color=INK, lw=1.5, zorder=4)

    # Helper function to draw sperm
    def draw_sperm(x, y, chrom="X"):
        circle = patches.Circle((x, y), 0.34, fc="white", ec=DEEP["blue"], lw=2.0, zorder=5)
        ax.add_patch(circle)
        # Tail curving to the left
        tail_x = np.linspace(x - 0.34, x - 0.78, 30)
        tail_y = y - 0.15 * np.sin((tail_x - (x - 0.34)) * 12)
        ax.plot(tail_x, tail_y, color=DEEP["blue"], lw=1.8, zorder=4)
        # Chromosome label
        c_col = DEEP["pink"] if chrom == "X" else DEEP["blue"]
        ax.text(x, y, chrom, ha="center", va="center", fontsize=15, fontweight="bold", color=c_col, zorder=6)

    # Helper function to draw egg
    def draw_egg(x, y):
        circle = patches.Circle((x, y), 0.38, fc="white", ec=DEEP["pink"], lw=2.0, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y, "X", ha="center", va="center", fontsize=15, fontweight="bold", color=DEEP["pink"], zorder=6)

    # 1. Parents Level
    # Mother
    m_x, m_y = 3.2, 9.6
    draw_person(m_x, m_y, is_female=True, scale=0.9, fill_color=PINK)
    ax.text(m_x, m_y + 0.65, "Mother (XX)", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)
    ax.text(m_x - 0.22, m_y - 0.95, "X", ha="center", va="top", fontsize=15, fontweight="bold", color=DEEP["pink"])
    ax.text(m_x + 0.22, m_y - 0.95, "X", ha="center", va="top", fontsize=15, fontweight="bold", color=DEEP["pink"])

    # Father
    f_x, f_y = 8.8, 9.6
    draw_person(f_x, f_y, is_female=False, scale=0.9, fill_color=BLUE)
    ax.text(f_x, f_y + 0.65, "Father (XY)", ha="center", va="bottom", fontsize=14, fontweight="bold", color=INK)
    ax.text(f_x - 0.22, f_y - 0.95, "X", ha="center", va="top", fontsize=15, fontweight="bold", color=DEEP["pink"])
    ax.text(f_x + 0.22, f_y - 0.95, "Y", ha="center", va="top", fontsize=15, fontweight="bold", color=DEEP["blue"])

    # 2. Gametes Level
    e1_x, e1_y = 2.0, 6.7
    e2_x, e2_y = 4.4, 6.7
    s1_x, s1_y = 7.6, 6.7
    s2_x, s2_y = 10.0, 6.7

    # Arrows from parents to gametes
    arrow_props = dict(arrowstyle="->", lw=1.5, color=GREY, shrinkA=8, shrinkB=8)
    ax.annotate("", xy=(e1_x, e1_y), xytext=(m_x, m_y - 1.2), arrowprops=arrow_props)
    ax.annotate("", xy=(e2_x, e2_y), xytext=(m_x, m_y - 1.2), arrowprops=arrow_props)
    ax.annotate("", xy=(s1_x, s1_y), xytext=(f_x, f_y - 1.2), arrowprops=arrow_props)
    ax.annotate("", xy=(s2_x, s2_y), xytext=(f_x, f_y - 1.2), arrowprops=arrow_props)

    # Place labels clearly above the gametes to avoid intersecting any crossing fertilization arrows below
    ax.text(3.2, 7.55, "eggs: all X", ha="center", va="center", fontsize=13, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=7)
    ax.text(8.8, 7.55, "sperm: X or Y", ha="center", va="center", fontsize=13, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=7)

    # Draw eggs and sperm
    draw_egg(e1_x, e1_y)
    draw_egg(e2_x, e2_y)
    draw_sperm(s1_x, s1_y, "X")
    draw_sperm(s2_x, s2_y, "Y")

    # 3. Offspring Level
    c_xs = [2.0, 4.5, 7.5, 10.0]
    c_y = 2.4

    # Connect crossing arrows:
    # Child 1: Egg 1 + Sperm X -> Girl (XX)
    # Child 2: Egg 1 + Sperm Y -> Boy (XY)
    # Child 3: Egg 2 + Sperm X -> Girl (XX)
    # Child 4: Egg 2 + Sperm Y -> Boy (XY)
    cross_lines = [
        ((e1_x, e1_y - 0.45), (c_xs[0], c_y + 1.2), DEEP["pink"]),
        ((s1_x, s1_y - 0.45), (c_xs[0], c_y + 1.2), DEEP["pink"]),
        ((e1_x, e1_y - 0.45), (c_xs[1], c_y + 1.2), DEEP["pink"]),
        ((s2_x, s2_y - 0.45), (c_xs[1], c_y + 1.2), DEEP["blue"]),
        ((e2_x, e2_y - 0.45), (c_xs[2], c_y + 1.2), DEEP["pink"]),
        ((s1_x, s1_y - 0.45), (c_xs[2], c_y + 1.2), DEEP["pink"]),
        ((e2_x, e2_y - 0.45), (c_xs[3], c_y + 1.2), DEEP["pink"]),
        ((s2_x, s2_y - 0.45), (c_xs[3], c_y + 1.2), DEEP["blue"]),
    ]

    for start, end, col in cross_lines:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", lw=1.3, color=col, alpha=0.75, shrinkA=4, shrinkB=4))

    # Draw children
    is_females = [True, False, True, False]
    labels = ["XX girl", "XY boy", "XX girl", "XY boy"]
    fills = [PINK, BLUE, PINK, BLUE]

    for cx, is_f, lbl, fll in zip(c_xs, is_females, labels, fills):
        draw_person(cx, c_y, is_female=is_f, scale=0.75, fill_color=fll)
        
        # Chromosome label below person
        chrom_str = lbl.split()[0]
        c1, c2 = chrom_str[0], chrom_str[1]
        ax.text(cx - 0.2, c_y - 0.85, c1, ha="center", va="top", fontsize=14, fontweight="bold",
                color=DEEP["pink"])
        ax.text(cx + 0.2, c_y - 0.85, c2, ha="center", va="top", fontsize=14, fontweight="bold",
                color=DEEP["pink"] if c2 == "X" else DEEP["blue"])
        
        # Sex text
        ax.text(cx, c_y - 1.25, lbl, ha="center", va="top", fontsize=12.5, fontweight="bold", color=INK)

    # 4. Summary / Conclusion labels at the bottom
    ax.text(6.0, 0.7, "1 girl : 1 boy", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(6.0, 0.25, "the father's sperm decides the sex", ha="center", va="center", fontsize=13,
            color=INK, style="italic")

    save(fig, out)
