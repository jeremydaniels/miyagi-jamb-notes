from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

def draw(out):
    fig = canvas(10.0, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10.0)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Overall testing tile (clean white background tile with subtle grey border)
    tile = FancyBboxPatch((0.6, 0.5), 5.8, 6.5, boxstyle="round,pad=0.15,rounding_size=0.25"),
    # Add tile directly
    tile_patch = FancyBboxPatch((0.6, 0.5), 5.8, 6.5, boxstyle="round,pad=0.1,rounding_size=0.25",
                               fc="white", ec=GREY, lw=1.5, zorder=1)
    ax.add_patch(tile_patch)

    # Column centers for drops
    col_x = [2.8, 4.8]
    # Row y-centers (Row 1: Group A, Row 2: Group B, Row 3: Group AB, Row 4: Group O)
    row_y = [5.5, 4.1, 2.7, 1.3]
    row_labels = ["Group A", "Group B", "Group AB", "Group O"]
    drop_radius = 0.50

    # Column headings above the drops
    ax.text(col_x[0], 6.45, "anti-A serum", ha="center", va="center",
            fontsize=13, fontweight="bold", color=INK)
    ax.text(col_x[1], 6.45, "anti-B serum", ha="center", va="center",
            fontsize=13, fontweight="bold", color=INK)

    # Row labels (blood group) to the left
    for y, label in zip(row_y, row_labels):
        ax.text(0.9, y, label, ha="left", va="center",
                fontsize=13, fontweight="bold", color=INK)

    # Agglutination patterns (anti-A, anti-B)
    results = [
        (True, False),   # Group A
        (False, True),   # Group B
        (True, True),    # Group AB
        (False, False)   # Group O
    ]

    smooth_color = "#c0262d"       # Uniform rich red
    clump_bg = "#fbebeb"           # Pale cleared serum background
    clump_dot_color = "#7f1015"    # Dark red clotted specks

    np.random.seed(42)

    def draw_smooth_drop(cx, cy):
        c = Circle((cx, cy), drop_radius, fc=smooth_color, ec="#9b1b22", lw=1.2, zorder=2)
        ax.add_patch(c)
        hl = Circle((cx - 0.15, cy + 0.15), 0.13, fc="white", ec="none", alpha=0.3, zorder=3)
        ax.add_patch(hl)

    def draw_clumped_drop(cx, cy):
        bg = Circle((cx, cy), drop_radius, fc=clump_bg, ec="#d8a8aa", lw=1.2, zorder=2)
        ax.add_patch(bg)

        # Grainy dark red clusters
        n_clusters = 13
        cluster_angles = np.random.uniform(0, 2 * np.pi, n_clusters)
        cluster_dists = drop_radius * np.sqrt(np.random.uniform(0.04, 0.72, n_clusters))
        cl_x = cx + cluster_dists * np.cos(cluster_angles)
        cl_y = cy + cluster_dists * np.sin(cluster_angles)

        for kx, ky in zip(cl_x, cl_y):
            n_sub = np.random.randint(6, 12)
            dx = np.random.normal(0, 0.035, n_sub)
            dy = np.random.normal(0, 0.035, n_sub)
            sizes = np.random.uniform(5, 18, n_sub)
            ax.scatter(kx + dx, ky + dy, s=sizes, color=clump_dot_color, alpha=0.9, zorder=3, edgecolors='none')

        # Additional scattered individual specks
        n_specks = 40
        sp_angles = np.random.uniform(0, 2 * np.pi, n_specks)
        sp_dists = drop_radius * np.sqrt(np.random.uniform(0.02, 0.85, n_specks))
        ax.scatter(cx + sp_dists * np.cos(sp_angles),
                   cy + sp_dists * np.sin(sp_angles),
                   s=np.random.uniform(2, 6, n_specks),
                   color=clump_dot_color, alpha=0.75, zorder=3, edgecolors='none')

    # Draw all drops
    for r_idx, (clump_a, clump_b) in enumerate(results):
        y = row_y[r_idx]
        if clump_a:
            draw_clumped_drop(col_x[0], y)
        else:
            draw_smooth_drop(col_x[0], y)

        if clump_b:
            draw_clumped_drop(col_x[1], y)
        else:
            draw_smooth_drop(col_x[1], y)

    # Place annotations on the right side, completely clear of column headers
    # "agglutination (clumping)" pointing to Row 1 left drop (clumped)
    ax.annotate("agglutination (clumping)",
                xy=(col_x[0] + drop_radius * 0.7, row_y[0] - drop_radius * 0.7),
                xytext=(8.3, 5.0),
                fontsize=12, color=INK,
                ha="center", va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3,
                                connectionstyle="arc3,rad=-0.15", shrinkB=4),
                zorder=5)

    # "no agglutination" pointing to Row 1 right drop (smooth)
    ax.annotate("no agglutination",
                xy=(col_x[1] + drop_radius * 0.8, row_y[0] + drop_radius * 0.5),
                xytext=(8.3, 6.0),
                fontsize=12, color=INK,
                ha="center", va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3,
                                connectionstyle="arc3,rad=0.1", shrinkB=4),
                zorder=5)

    save(fig, out)
