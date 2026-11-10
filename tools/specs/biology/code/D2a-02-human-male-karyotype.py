from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    # Canvas setup - wider layout to comfortably fit 23 chromosome pairs and annotations
    fig = canvas(13, 9.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9.5)
    ax.axis("off")

    # Title
    ax.text(6.5, 8.9, "male karyotype: 46, XY", ha="center", va="center", 
            fontsize=18, fontweight="bold", color=INK)

    # Function to draw an X-shaped chromosome
    def draw_chromosome(cx, cy, h, w, color, lw=3.0):
        y_pts = np.linspace(-h/2, h/2, 25)
        # Pinch in the middle (centromere)
        x_offset = (w/2) * (2.2 * (y_pts / h)**2 + 0.12)
        ax.plot(cx - x_offset, cy + y_pts, color=color, lw=lw, solid_capstyle='round')
        ax.plot(cx + x_offset, cy + y_pts, color=color, lw=lw, solid_capstyle='round')
        # Centromere dot
        ax.plot(cx, cy, marker='o', markersize=lw*0.7, color=color)

    # Base sizes decreasing from pair 1 to 22
    sizes = np.linspace(0.82, 0.30, 22)

    autosome_color = DEEP["lav"]
    sex_color = DEEP["blue"]

    # Vertical rows with generous spacing:
    # Row 0: Pairs 1 - 6
    # Row 1: Pairs 7 - 12
    # Row 2: Pairs 13 - 18
    # Row 3: Pairs 19 - 22 (cols 0, 1, 2, 3), Pair 23 (Sex) at col 5
    row_y = [7.4, 5.5, 3.6, 1.7]
    col_x = [1.7 + i * 1.8 for i in range(6)]  # [1.7, 3.5, 5.3, 7.1, 8.9, 10.7]

    pair1_pos = None

    for i in range(22):
        pair_num = i + 1
        h = sizes[i]
        w = h * 0.36

        if pair_num <= 6:
            r = 0
            c = pair_num - 1
        elif pair_num <= 12:
            r = 1
            c = pair_num - 7
        elif pair_num <= 18:
            r = 2
            c = pair_num - 13
        else:
            r = 3
            c = pair_num - 19

        cx = col_x[c]
        cy = row_y[r]

        # Two sister homologues side by side
        dx = w * 0.85 + 0.08
        draw_chromosome(cx - dx, cy, h, w, autosome_color, lw=3.0)
        draw_chromosome(cx + dx, cy, h, w, autosome_color, lw=3.0)

        # Label pair number below
        ax.text(cx, cy - 0.62, str(pair_num), ha="center", va="top", fontsize=14, color=INK)

        if pair_num == 1:
            pair1_pos = (cx, cy, h)

    # Pair 23 (Sex chromosomes: X and Y) placed at Row 3, col 5 (10.7, 1.7)
    # Chromosome 18 is at Row 2, col 5 (10.7, 3.6), so vertical gap is 1.9 units.
    c23_x = col_x[5]
    c23_y = row_y[3]

    # X chromosome: medium size (~0.62)
    h_x = 0.62
    w_x = h_x * 0.36
    x_pos = c23_x - 0.28
    draw_chromosome(x_pos, c23_y, h_x, w_x, sex_color, lw=3.2)

    # Y chromosome: much smaller (~0.28)
    h_y = 0.28
    w_y = h_y * 0.36
    y_pos = c23_x + 0.28
    draw_chromosome(y_pos, c23_y - 0.14, h_y, w_y, sex_color, lw=3.0)

    # Labels for X and Y directly above chromosomes
    ax.text(x_pos, c23_y + h_x/2 + 0.12, "X", ha="center", va="bottom", 
            fontsize=15, fontweight="bold", color=DEEP["blue"])
    ax.text(y_pos, c23_y - 0.14 + h_y/2 + 0.12, "Y", ha="center", va="bottom", 
            fontsize=15, fontweight="bold", color=DEEP["blue"])

    # Highlighting box for sex chromosomes (compact, tightly enclosing Pair 23)
    # Box spans y: [0.75, 2.65] (height 1.90), well clear of pair 18 at y=3.6 (whose label is at y=2.98)
    sex_box = plt.Rectangle((c23_x - 0.72, c23_y - 0.95), 1.44, 1.90, 
                            fill=True, facecolor=BLUE, edgecolor=DEEP["blue"], 
                            alpha=0.18, lw=1.5, ls="--", zorder=0)
    ax.add_patch(sex_box)

    # "sex chromosomes" label placed neatly BELOW pair 23 box
    ax.text(c23_x, c23_y - 1.15, "sex chromosomes", ha="center", va="top", 
            fontsize=14, fontweight="bold", color=DEEP["blue"],
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1.2))

    # Autosomes side label and vertical bracket on the left
    ax.text(0.35, 4.6, "autosomes (pairs 1 to 22)", 
            fontsize=15, fontweight="bold", color=DEEP["lav"], rotation=90,
            ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["lav"], boxstyle="round,pad=0.3", lw=1.2))

    ax.plot([0.65, 0.65], [1.1, 8.0], color=DEEP["lav"], lw=1.5)
    ax.plot([0.65, 0.78], [8.0, 8.0], color=DEEP["lav"], lw=1.5)
    ax.plot([0.65, 0.78], [1.1, 1.1], color=DEEP["lav"], lw=1.5)

    # Homologous pair label pointing to Pair 1
    p1_x, p1_y, p1_h = pair1_pos
    ax.annotate("homologous pair", 
                xy=(p1_x, p1_y + p1_h/2 + 0.05), 
                xytext=(p1_x + 0.9, p1_y + 0.95),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                ha="center", va="bottom",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
