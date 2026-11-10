from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 13)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 13)
    ax.axis("off")

    # Title
    ax.text(6, 12.4, "Inheritance of Haemophilia (Sex-Linked)", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK)

    # Helper to draw chromosome X or Y
    def draw_chrom(x, y, kind="X", has_allele=False, scale=1.0):
        # kind: 'X' (pink) or 'Y' (blue, shorter)
        if kind == "X":
            w, h = 0.22 * scale, 0.9 * scale
            rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                         boxstyle="round,pad=0.04,rounding_size=0.1",
                                         facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5)
            ax.add_patch(rect)
            if has_allele:
                # Red dot marking haemophilia allele
                ax.plot(x, y + 0.15 * scale, marker='o', markersize=7 * scale,
                        color="red", markeredgecolor=INK, markeredgewidth=1)
        elif kind == "Y":
            w, h = 0.22 * scale, 0.55 * scale
            rect = patches.FancyBboxPatch((x - w/2, y - h/2 - 0.15 * scale), w, h,
                                         boxstyle="round,pad=0.04,rounding_size=0.1",
                                         facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5)
            ax.add_patch(rect)

    # Helper to draw pedigree icon (Circle = female, Square = male)
    def draw_person_icon(x, y, sex="F", status="normal", r=0.35):
        # status: 'normal', 'carrier' (half-shaded), 'affected' (fully shaded)
        if sex == "F":
            # Circle
            if status == "normal":
                c = patches.Circle((x, y), r, facecolor=CREAM, edgecolor=INK, lw=1.8)
                ax.add_patch(c)
            elif status == "carrier":
                # Left half CREAM/white, right half RED
                c_bg = patches.Circle((x, y), r, facecolor=CREAM, edgecolor=INK, lw=1.8)
                ax.add_patch(c_bg)
                wedge = patches.Wedge((x, y), r, 270, 90, facecolor="#E66161", edgecolor=INK, lw=1.5)
                ax.add_patch(wedge)
            elif status == "affected":
                c = patches.Circle((x, y), r, facecolor="#E66161", edgecolor=INK, lw=1.8)
                ax.add_patch(c)
        else:
            # Square
            side = 2 * r
            if status == "normal":
                sq = patches.Rectangle((x - r, y - r), side, side, facecolor=CREAM, edgecolor=INK, lw=1.8)
                ax.add_patch(sq)
            elif status == "carrier":
                sq = patches.Rectangle((x - r, y - r), side, side, facecolor=CREAM, edgecolor=INK, lw=1.8)
                ax.add_patch(sq)
                half = patches.Rectangle((x, y - r), r, side, facecolor="#E66161", edgecolor=INK, lw=1.5)
                ax.add_patch(half)
            elif status == "affected":
                sq = patches.Rectangle((x - r, y - r), side, side, facecolor="#E66161", edgecolor=INK, lw=1.8)
                ax.add_patch(sq)

    # 1. Parents section
    # Mother (Left)
    mx, my = 3.2, 10.7
    draw_person_icon(mx, my + 0.4, sex="F", status="carrier", r=0.38)
    draw_chrom(mx - 0.25, my - 0.45, "X", has_allele=False)
    draw_chrom(mx + 0.25, my - 0.45, "X", has_allele=True)
    ax.text(mx, my + 0.95, "carrier mother (X^H X^h)", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(mx - 0.25, my - 1.1, "$X^H$", ha="center", va="center", fontsize=14, color=INK)
    ax.text(mx + 0.25, my - 1.1, "$X^h$", ha="center", va="center", fontsize=14, color=INK)

    # Father (Right)
    fx, fy = 8.8, 10.7
    draw_person_icon(fx, fy + 0.4, sex="M", status="normal", r=0.38)
    draw_chrom(fx - 0.25, my - 0.45, "X", has_allele=False)
    draw_chrom(fx + 0.25, my - 0.45, "Y", has_allele=False)
    ax.text(fx, fy + 0.95, "normal father (X^H Y)", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(fx - 0.25, my - 1.1, "$X^H$", ha="center", va="center", fontsize=14, color=INK)
    ax.text(fx + 0.25, my - 1.1, "$Y$", ha="center", va="center", fontsize=14, color=INK)

    # Annotations for parent chromosomes
    ax.annotate("allele for haemophilia on X chromosome",
                xy=(mx + 0.35, my - 0.3), xytext=(mx - 2.8, 9.4),
                fontsize=14, color=INK, ha="left",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Y has no matching allele",
                xy=(fx + 0.25, my - 0.55), xytext=(fx + 0.6, 9.4),
                fontsize=14, color=INK, ha="left",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Gametes Row
    ax.text(0.6, 8.4, "Gametes:", fontsize=15, fontweight="bold", color=INK, va="center")
    
    # Mother gametes
    g_m1_x, g_m2_x = 2.4, 4.0
    gy = 8.4
    for gx, sym, allele in [(g_m1_x, "$X^H$", False), (g_m2_x, "$X^h$", True)]:
        circ = patches.Circle((gx, gy), 0.5, facecolor="white", edgecolor=DEEP["pink"], lw=1.8, linestyle="--")
        ax.add_patch(circ)
        draw_chrom(gx, gy, "X", has_allele=allele, scale=0.7)
        ax.text(gx, gy - 0.72, sym, ha="center", va="center", fontsize=14, fontweight="bold", color=INK)

    # Father gametes
    g_f1_x, g_f2_x = 8.0, 9.6
    for gx, sym, kind in [(g_f1_x, "$X^H$", "X"), (g_f2_x, "$Y$", "Y")]:
        circ = patches.Circle((gx, gy), 0.5, facecolor="white", edgecolor=DEEP["blue"], lw=1.8, linestyle="--")
        ax.add_patch(circ)
        draw_chrom(gx, gy, kind, has_allele=False, scale=0.7)
        ax.text(gx, gy - 0.72, sym, ha="center", va="center", fontsize=14, fontweight="bold", color=INK)

    # 2. Punnett Square
    # Grid coordinates
    px0, py0 = 3.6, 1.0
    cw, ch = 3.6, 2.7  # cell width, height

    # Grid labels: Father's gametes on Top, Mother's gametes on Left
    ax.text(px0 + cw, py0 + 2 * ch + 0.9, "Father's Gametes", ha="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(px0 - 1.2, py0 + ch, "Mother's\nGametes", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Column headers
    col_x = [px0 + 0.5 * cw, px0 + 1.5 * cw]
    ax.text(col_x[0], py0 + 2 * ch + 0.35, "X^H", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(col_x[1], py0 + 2 * ch + 0.35, "Y", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Row headers
    row_y = [py0 + 1.5 * ch, py0 + 0.5 * ch]
    ax.text(px0 - 0.35, row_y[0], "X^H", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(px0 - 0.35, row_y[1], "X^h", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Punnett grid outer box & dividers
    grid_rect = patches.Rectangle((px0, py0), 2 * cw, 2 * ch, facecolor="white", edgecolor=INK, lw=2)
    ax.add_patch(grid_rect)
    ax.plot([px0 + cw, px0 + cw], [py0, py0 + 2 * ch], color=INK, lw=1.8)
    ax.plot([px0, px0 + 2 * cw], [py0 + ch, py0 + ch], color=INK, lw=1.8)

    # Children cells:
    # Top-Left: Normal daughter (X^H X^H)
    c1_x, c1_y = col_x[0], row_y[0]
    draw_person_icon(c1_x - 0.8, c1_y + 0.3, sex="F", status="normal", r=0.38)
    draw_chrom(c1_x + 0.6, c1_y + 0.3, "X", scale=0.7)
    draw_chrom(c1_x + 0.95, c1_y + 0.3, "X", scale=0.7)
    ax.text(c1_x, c1_y - 0.45, "normal daughter", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(c1_x, c1_y - 0.85, "$X^H X^H$", ha="center", va="center", fontsize=14, color=INK)

    # Top-Right: Normal son (X^H Y)
    c2_x, c2_y = col_x[1], row_y[0]
    draw_person_icon(c2_x - 0.8, c2_y + 0.3, sex="M", status="normal", r=0.38)
    draw_chrom(c2_x + 0.6, c2_y + 0.3, "X", scale=0.7)
    draw_chrom(c2_x + 0.95, c2_y + 0.3, "Y", scale=0.7)
    ax.text(c2_x, c2_y - 0.45, "normal son", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(c2_x, c2_y - 0.85, "$X^H Y$", ha="center", va="center", fontsize=14, color=INK)

    # Bottom-Left: Carrier daughter (X^H X^h, half-shaded)
    c3_x, c3_y = col_x[0], row_y[1]
    draw_person_icon(c3_x - 0.8, c3_y + 0.3, sex="F", status="carrier", r=0.38)
    draw_chrom(c3_x + 0.6, c3_y + 0.3, "X", has_allele=False, scale=0.7)
    draw_chrom(c3_x + 0.95, c3_y + 0.3, "X", has_allele=True, scale=0.7)
    ax.text(c3_x, c3_y - 0.45, "carrier daughter", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(c3_x, c3_y - 0.85, "$X^H X^h$", ha="center", va="center", fontsize=14, color=INK)

    # Bottom-Right: Haemophiliac son (X^h Y, fully shaded red)
    c4_x, c4_y = col_x[1], row_y[1]
    draw_person_icon(c4_x - 0.8, c4_y + 0.3, sex="M", status="affected", r=0.38)
    draw_chrom(c4_x + 0.6, c4_y + 0.3, "X", has_allele=True, scale=0.7)
    draw_chrom(c4_x + 0.95, c4_y + 0.3, "Y", scale=0.7)
    ax.text(c4_x, c4_y - 0.45, "haemophiliac son", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
    ax.text(c4_x, c4_y - 0.85, "$X^h Y$", ha="center", va="center", fontsize=14, color=INK)

    save(fig, out)
