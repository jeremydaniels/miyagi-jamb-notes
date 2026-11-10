from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw(out):
    # Generous vertical space to avoid overlaps between rows
    fig = canvas(14, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Color palette for chromosome bands
    band_colors = {
        'A': BLUE,
        'B': GREEN,
        'C': CREAM,
        'D': ORANGE,
        'E': PINK,
        'F': LAV,
        'G': GREY,
        'H': '#d0d7de'
    }

    # Band geometry
    w = 0.52
    bh = 0.48
    centromere_r = 0.15

    def draw_chromosome(x_center, y_top, bands, centromere_after='B'):
        """Draws a vertical chromosome with labeled bands and a centromere."""
        curr_y = y_top
        for b in bands:
            rect = plt.Rectangle((x_center - w/2, curr_y - bh), w, bh,
                                 facecolor=band_colors.get(b, GREY),
                                 edgecolor=INK, lw=1.5, zorder=2)
            ax.add_patch(rect)
            ax.text(x_center, curr_y - bh/2, b, ha='center', va='center',
                    fontsize=14, fontweight='bold', color=INK, zorder=3)
            
            if centromere_after and b == centromere_after:
                circle = plt.Circle((x_center, curr_y - bh), centromere_r,
                                    facecolor='white', edgecolor=INK, lw=1.5, zorder=4)
                ax.add_patch(circle)
            
            curr_y -= bh

    # Distinct layout coordinates
    # Row 0 (top): Deletion & Duplication
    # Row 1 (bottom): Inversion & Translocation
    row_y_tops = [9.8, 4.6]
    col_x_offsets = [1.2, 7.8]

    panels = [
        {"name": "deletion", "col": 0, "row": 0,
         "mut_bands": ['A', 'B', 'C', 'E', 'F']},
        {"name": "duplication", "col": 1, "row": 0,
         "mut_bands": ['A', 'B', 'C', 'D', 'D', 'E', 'F']},
        {"name": "inversion", "col": 0, "row": 1,
         "mut_bands": ['A', 'B', 'C', 'E', 'D', 'F']},
        {"name": "translocation", "col": 1, "row": 1,
         "mut_bands": ['A', 'B', 'C', 'D', 'G', 'H']}
    ]

    for p in panels:
        base_x = col_x_offsets[p["col"]]
        y_top = row_y_tops[p["row"]]
        
        # Panel Title strictly placed above the diagram
        ax.text(base_x + 2.4, y_top + 0.5, p["name"].capitalize(),
                fontsize=16, fontweight='bold', ha='center', va='bottom', color=INK)

        # Normal chromosome
        norm_x = base_x + 1.0
        draw_chromosome(norm_x, y_top, ['A', 'B', 'C', 'D', 'E', 'F'])
        ax.text(norm_x, y_top - 6 * bh - 0.25, "normal\nchromosome",
                ha='center', va='top', fontsize=14, color=INK)

        # Transition arrow
        arrow_x = base_x + 2.35
        ax.annotate("", xy=(arrow_x + 0.45, y_top - 3 * bh),
                    xytext=(arrow_x - 0.45, y_top - 3 * bh),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.8, mutation_scale=14))

        # Mutated chromosome(s)
        mut_x = base_x + 3.7
        mut_len = len(p["mut_bands"])
        
        if p["name"] == "translocation":
            # Chromosome 1 with translocated G H
            draw_chromosome(mut_x, y_top, p["mut_bands"])
            ax.text(mut_x, y_top - mut_len * bh - 0.25, p["name"],
                    ha='center', va='top', fontsize=14, fontweight='bold', color=INK)
            
            # Second chromosome shown shortened (originally G H, now just remainder/shortened)
            sec_x = mut_x + 1.05
            # Shown shortened with just one or two remaining bands (e.g. non-homologous partner)
            draw_chromosome(sec_x, y_top, ['E', 'F'], centromere_after=None)
            ax.text(sec_x, y_top - 2 * bh - 0.25, "shortened\npartner",
                    ha='center', va='top', fontsize=14, color=INK)
        else:
            draw_chromosome(mut_x, y_top, p["mut_bands"])
            ax.text(mut_x, y_top - mut_len * bh - 0.25, p["name"],
                    ha='center', va='top', fontsize=14, fontweight='bold', color=INK)

    # Label for centromere with arrow pointing to the centromere on the first normal chromosome
    cent_x = col_x_offsets[0] + 1.0
    cent_y = row_y_tops[0] - 2 * bh
    ax.annotate("centromere", xy=(cent_x, cent_y), xytext=(cent_x - 1.6, cent_y + 0.2),
                ha='right', va='center', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    save(fig, out)
