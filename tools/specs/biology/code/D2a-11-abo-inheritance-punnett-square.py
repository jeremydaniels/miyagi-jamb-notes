from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Main Title
    ax.text(5.0, 8.0, "ABO Blood Group Inheritance", fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # Grid parameters
    gx, gy = 3.2, 2.2
    cw, ch = 2.4, 2.2

    # Draw grid cells
    for r in range(2):
        for c in range(2):
            rect = patches.Rectangle((gx + c * cw, gy + (1 - r) * ch), cw, ch,
                                     linewidth=2.0, edgecolor=INK, facecolor='white', zorder=1)
            ax.add_patch(rect)

    # Labels for Parents
    # Mother on top
    ax.text(gx + cw, gy + 2 * ch + 1.1, "Mother: group B ($I^B i$)", fontsize=13.5, fontweight='bold', ha='center', va='center', color=INK)
    # Mother gametes across the top
    ax.text(gx + 0.5 * cw, gy + 2 * ch + 0.4, "$I^B$", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP['blue'])
    ax.text(gx + 1.5 * cw, gy + 2 * ch + 0.4, "$i$", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP['blue'])

    # Father on the left
    ax.text(gx - 1.6, gy + ch, "Father: group A ($I^A i$)", fontsize=13.5, fontweight='bold', ha='center', va='center', color=INK, rotation=90)
    # Father gametes down the side
    ax.text(gx - 0.5, gy + 1.5 * ch, "$I^A$", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP['orange'])
    ax.text(gx - 0.5, gy + 0.5 * ch, "$i$", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP['orange'])

    # Helper function to draw blood-drop icon using polygon coordinates
    def draw_drop(center_x, center_y, scale, facecol, edgecol, edgewidth=2.0):
        # Semicircular bottom lobe and sharp teardrop top
        t = np.linspace(-np.pi, 0, 40)
        r_bottom = 0.45
        y_center_bottom = -0.15
        xb = r_bottom * np.cos(t)
        yb = y_center_bottom + r_bottom * np.sin(t)
        # Left side goes from top peak (0, 0.75) to (-r_bottom, y_center_bottom)
        # Right side goes from (r_bottom, y_center_bottom) to top peak (0, 0.75)
        top_x, top_y = 0.0, 0.75
        drop_x = np.concatenate([[top_x], [-r_bottom], xb, [r_bottom], [top_x]])
        drop_y = np.concatenate([[top_y], [y_center_bottom], yb, [y_center_bottom], [top_y]])
        
        poly_verts = np.column_stack([center_x + drop_x * scale, center_y + drop_y * scale])
        poly = patches.Polygon(poly_verts, closed=True, facecolor=facecol, edgecolor=edgecol,
                               linewidth=edgewidth, zorder=3)
        ax.add_patch(poly)

    # Square contents: (row, col)
    # r=0, c=0: I^A I^B -> AB (Purple drop)
    # r=0, c=1: I^A i   -> A  (Blue drop)
    # r=1, c=0: I^B i   -> B  (Green drop)
    # r=1, c=1: ii      -> O  (White with red outline)

    cells_data = [
        # (row, col, genotype_text, phenotype_text, drop_face, drop_edge)
        (0, 0, "$I^A I^B$", "$I^A I^B = AB$", LAV, DEEP['lav']),
        (0, 1, "$I^A i$", "$I^A i = A$", BLUE, DEEP['blue']),
        (1, 0, "$I^B i$", "$I^B i = B$", GREEN, DEEP['green']),
        (1, 1, "$i i$", "$ii = O$", "white", DEEP['pink'])
    ]

    for r, c, geno, pheno, drop_face, drop_edge in cells_data:
        cx = gx + (c + 0.5) * cw
        cy = gy + (1 - r + 0.5) * ch
        
        # Drop icon
        draw_drop(cx, cy + 0.35, scale=0.55, facecol=drop_face, edgecol=drop_edge, edgewidth=2.0)
        
        # Genotype inside box
        ax.text(cx, cy - 0.22, geno, fontsize=13.5, fontweight='bold', ha='center', va='center', color=INK, zorder=4)
        
        # Explicit phenotype formula label inside the box
        ax.text(cx, cy - 0.65, pheno, fontsize=11.5, ha='center', va='center', color=INK, zorder=4,
                bbox=dict(fc='white', ec='none', pad=1))

    # Phenotypic Ratio at the bottom
    ax.text(5.0, 1.0, "1 AB : 1 A : 1 B : 1 O", fontsize=14, fontweight='bold', ha='center', va='center',
            color=INK, bbox=dict(boxstyle='round,pad=0.5', facecolor=CREAM, edgecolor=GREY, lw=1.2))

    save(fig, out)
