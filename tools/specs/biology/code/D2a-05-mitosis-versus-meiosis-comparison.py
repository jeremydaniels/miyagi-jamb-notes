from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Color palette
    RED = DEEP["pink"]
    BLU = DEEP["blue"]
    CELL_BG = "#FDFBF7"
    CELL_EDGE = GREY

    # Helper: draw cell circle/oval
    def draw_cell(x, y, r=1.05, rx=None, ry=None, label=None, label_pos="top"):
        if rx is None: rx = r
        if ry is None: ry = r
        cell = patches.Ellipse((x, y), 2*rx, 2*ry, facecolor=CELL_BG, edgecolor=CELL_EDGE, lw=1.5, zorder=1)
        ax.add_patch(cell)
        if label:
            ly = y + ry + 0.25 if label_pos == "top" else y - ry - 0.25
            va = "bottom" if label_pos == "top" else "top"
            ax.text(x, ly, label, ha="center", va=va, fontsize=11, color=INK, fontweight="bold")

    # Helper: draw single chromosome (vertical bar with rounded caps)
    def draw_chrom(x, y, h, w, color, tip_color=None, tip_frac=0.3, tip_pos="bottom"):
        # if tip_color is given, split the bar into main body and swapped tip
        r_corner = w / 2.0
        if tip_color is None:
            p = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                       boxstyle=f"round,pad=0,rounding_size={r_corner}",
                                       facecolor=color, edgecolor="none", zorder=3)
            ax.add_patch(p)
        else:
            # Main part and tip part
            tip_h = h * tip_frac
            body_h = h - tip_h
            if tip_pos == "bottom":
                # Body on top
                p1 = patches.FancyBboxPatch((x - w/2, y - h/2 + tip_h), w, body_h,
                                            boxstyle=f"round,pad=0,rounding_size={r_corner}",
                                            facecolor=color, edgecolor="none", zorder=3)
                p2 = patches.FancyBboxPatch((x - w/2, y - h/2), w, tip_h,
                                            boxstyle=f"round,pad=0,rounding_size={r_corner}",
                                            facecolor=tip_color, edgecolor="none", zorder=3)
            else:
                # Body on bottom
                p1 = patches.FancyBboxPatch((x - w/2, y - h/2), w, body_h,
                                            boxstyle=f"round,pad=0,rounding_size={r_corner}",
                                            facecolor=color, edgecolor="none", zorder=3)
                p2 = patches.FancyBboxPatch((x - w/2, y + h/2 - tip_h), w, tip_h,
                                            boxstyle=f"round,pad=0,rounding_size={r_corner}",
                                            facecolor=tip_color, edgecolor="none", zorder=3)
            ax.add_patch(p1)
            ax.add_patch(p2)

    # Helper: draw duplicated chromosome (X shape / sister chromatids)
    def draw_x_chrom(x, y, h, w, color, cross_arm=None, cross_color=None):
        # Two parallel chromatids pinched at center, or an X
        # Clean representation: two vertical chromatid rods touching at center
        gap = 0.08
        rod_w = 0.09
        # Left sister
        tip_c_left = cross_color if cross_arm == "left" else None
        draw_chrom(x - gap, y, h, rod_w, color, tip_color=tip_c_left, tip_frac=0.35, tip_pos="bottom")
        # Right sister
        tip_c_right = cross_color if cross_arm == "right" else None
        draw_chrom(x + gap, y, h, rod_w, color, tip_color=tip_c_right, tip_frac=0.35, tip_pos="bottom")
        # Centromere
        ax.plot([x - gap, x + gap], [y, y], color="white", lw=1.2, zorder=4)
        ax.plot(x, y, marker='o', markersize=3.5, color=INK, zorder=5)

    # Helper: Arrow
    def draw_arrow(x1, y1, x2, y2, text=None, text_offset=(0.2, 0)):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=1.8, mutation_scale=14))
        if text:
            ax.text((x1 + x2)/2 + text_offset[0], (y1 + y2)/2 + text_offset[1],
                    text, ha="left", va="center", fontsize=11, color=INK,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.9))

    # --- TOP HEADINGS ---
    ax.text(3.75, 11.4, "MITOSIS", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(11.25, 11.4, "MEIOSIS", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    # Divider line between columns
    ax.plot([7.5, 7.5], [0.5, 11.5], color=GREY, lw=1, linestyle="--", alpha=0.6)

    # Long and short chromosome dimensions
    H_L = 0.95
    H_S = 0.55
    W_C = 0.11

    # ==========================================
    # 1. PARENT CELLS (ROW 1, y = 9.8)
    # ==========================================
    # Mitosis Parent
    draw_cell(3.75, 9.8, r=1.05)
    # 4 single unduplicated chromosomes: 1 long red, 1 long blue, 1 short red, 1 short blue
    draw_chrom(3.25, 9.8, H_L, W_C, RED)
    draw_chrom(3.60, 9.8, H_L, W_C, BLU)
    draw_chrom(3.95, 9.8, H_S, W_C, RED)
    draw_chrom(4.25, 9.8, H_S, W_C, BLU)

    # Meiosis Parent
    draw_cell(11.25, 9.8, r=1.05)
    draw_chrom(10.75, 9.8, H_L, W_C, RED)
    draw_chrom(11.10, 9.8, H_L, W_C, BLU)
    draw_chrom(11.45, 9.8, H_S, W_C, RED)
    draw_chrom(11.75, 9.8, H_S, W_C, BLU)

    # Label for parent cell row
    ax.text(7.5, 9.8, "parent cell (2n = 4)", ha="center", va="center", fontsize=12,
            fontweight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY))

    # ==========================================
    # MITOSIS: ROW 2 (y = 6.6)
    # Chromosomes duplicated and lined up singly at equator
    # ==========================================
    draw_arrow(3.75, 8.7, 3.75, 7.7, text="chromosomes duplicate\n& align singly at equator", text_offset=(0.25, 0))
    draw_cell(3.75, 6.4, rx=1.4, ry=1.1)

    # Equator dash line
    ax.plot([3.75, 3.75], [5.5, 7.3], color=GREY, lw=0.9, linestyle=":")

    # 4 duplicated chromosomes lined up vertically along the equator
    xs = [2.8, 3.45, 4.05, 4.7]
    draw_x_chrom(2.8, 6.4, H_L, W_C, RED)
    draw_x_chrom(3.45, 6.4, H_L, W_C, BLU)
    draw_x_chrom(4.05, 6.4, H_S, W_C, RED)
    draw_x_chrom(4.7, 6.4, H_S, W_C, BLU)

    # ==========================================
    # MITOSIS: ROW 3 (y = 2.6)
    # Two daughter cells, identical diploid
    # ==========================================
    draw_arrow(3.75, 5.25, 3.75, 3.9, text="sister chromatids separate", text_offset=(0.25, 0))

    # Two daughter cells side by side
    c_m1 = 2.45
    c_m2 = 5.05
    y_m_d = 2.5
    draw_cell(c_m1, y_m_d, rx=1.05, ry=1.0)
    draw_cell(c_m2, y_m_d, rx=1.05, ry=1.0)

    for cx in [c_m1, c_m2]:
        draw_chrom(cx - 0.45, y_m_d, H_L, W_C, RED)
        draw_chrom(cx - 0.15, y_m_d, H_L, W_C, BLU)
        draw_chrom(cx + 0.15, y_m_d, H_S, W_C, RED)
        draw_chrom(cx + 0.45, y_m_d, H_S, W_C, BLU)

    ax.text(3.75, 0.9, "2 identical diploid cells\n(2n = 4)", ha="center", va="center",
            fontsize=12, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=GREY))

    # ==========================================
    # MEIOSIS: ROW 2 (y = 6.8)
    # Homologous chromosomes paired up with crossing over
    # ==========================================
    draw_arrow(11.25, 8.7, 11.25, 7.9, text="homologous chromosomes\npair up & cross over", text_offset=(0.25, 0))
    draw_cell(11.25, 6.7, rx=1.45, ry=1.1)

    # Pair 1: Long pair (Red & Blue with crossed tips)
    draw_x_chrom(10.6, 6.7, H_L, W_C, RED, cross_arm="right", cross_color=BLU)
    draw_x_chrom(10.9, 6.7, H_L, W_C, BLU, cross_arm="left", cross_color=RED)

    # Pair 2: Short pair (Red & Blue with crossed tips)
    draw_x_chrom(11.6, 6.7, H_S, W_C, RED, cross_arm="right", cross_color=BLU)
    draw_x_chrom(11.9, 6.7, H_S, W_C, BLU, cross_arm="left", cross_color=RED)

    # Annotations for pairing and crossing over
    ax.annotate("homologous pair", xy=(10.75, 7.3), xytext=(9.2, 7.7),
                fontsize=11, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2),
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, alpha=0.9))

    ax.annotate("crossing over", xy=(11.75, 6.35), xytext=(13.3, 6.35),
                fontsize=11, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2),
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, alpha=0.9))

    # ==========================================
    # MEIOSIS: ROW 3 (y = 4.4)
    # First division: pairs separate into 2 cells
    # ==========================================
    draw_arrow(11.25, 5.55, 11.25, 4.9)
    ax.text(11.25, 5.25, "first division: pairs separate", ha="center", va="center",
            fontsize=11, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    c_me_1 = 9.8
    c_me_2 = 12.7
    y_me_mid = 4.0
    draw_cell(c_me_1, y_me_mid, rx=1.05, ry=0.85)
    draw_cell(c_me_2, y_me_mid, rx=1.05, ry=0.85)

    # Cell 1 gets: Long RED (with blue recombinant tip) and Short RED (with blue recombinant tip)
    draw_x_chrom(c_me_1 - 0.25, y_me_mid, H_L, W_C, RED, cross_arm="right", cross_color=BLU)
    draw_x_chrom(c_me_1 + 0.25, y_me_mid, H_S, W_C, RED, cross_arm="right", cross_color=BLU)

    # Cell 2 gets: Long BLUE (with red recombinant tip) and Short BLUE (with red recombinant tip)
    draw_x_chrom(c_me_2 - 0.25, y_me_mid, H_L, W_C, BLU, cross_arm="left", cross_color=RED)
    draw_x_chrom(c_me_2 + 0.25, y_me_mid, H_S, W_C, BLU, cross_arm="left", cross_color=RED)

    # ==========================================
    # MEIOSIS: ROW 4 (y = 1.9)
    # Second division: chromatids separate into 4 cells
    # ==========================================
    draw_arrow(c_me_1, 3.1, 9.1, 2.4)
    draw_arrow(c_me_1, 3.1, 10.4, 2.4)
    draw_arrow(c_me_2, 3.1, 12.1, 2.4)
    draw_arrow(c_me_2, 3.1, 13.4, 2.4)

    ax.text(11.25, 2.9, "second division: chromatids separate", ha="center", va="center",
            fontsize=11, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    # Four daughter cells
    xs_hap = [8.8, 10.1, 12.1, 13.4]
    y_hap = 1.8
    r_hap = 0.62

    for x_h in xs_hap:
        draw_cell(x_h, y_hap, rx=r_hap, ry=r_hap)

    # Cell 1: Pure maternal (Long Red, Short Red)
    draw_chrom(xs_hap[0] - 0.16, y_hap, H_L, W_C, RED)
    draw_chrom(xs_hap[0] + 0.16, y_hap, H_S, W_C, RED)

    # Cell 2: Recombinant 1 (Long Red with Blue tip, Short Red with Blue tip)
    draw_chrom(xs_hap[1] - 0.16, y_hap, H_L, W_C, RED, tip_color=BLU, tip_frac=0.35, tip_pos="bottom")
    draw_chrom(xs_hap[1] + 0.16, y_hap, H_S, W_C, RED, tip_color=BLU, tip_frac=0.35, tip_pos="bottom")

    # Cell 3: Recombinant 2 (Long Blue with Red tip, Short Blue with Red tip)
    draw_chrom(xs_hap[2] - 0.16, y_hap, H_L, W_C, BLU, tip_color=RED, tip_frac=0.35, tip_pos="bottom")
    draw_chrom(xs_hap[2] + 0.16, y_hap, H_S, W_C, BLU, tip_color=RED, tip_frac=0.35, tip_pos="bottom")

    # Cell 4: Pure paternal (Long Blue, Short Blue)
    draw_chrom(xs_hap[3] - 0.16, y_hap, H_L, W_C, BLU)
    draw_chrom(xs_hap[3] + 0.16, y_hap, H_S, W_C, BLU)

    ax.text(11.25, 0.6, "4 different haploid cells (n = 2)", ha="center", va="center",
            fontsize=12, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=GREY))

    save(fig, out)
