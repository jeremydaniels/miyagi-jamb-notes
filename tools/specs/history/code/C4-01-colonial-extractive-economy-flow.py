from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(7, 7.5, "The Colonial Extractive Economy", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # Nigeria Map Representation on the left
    n_polys = nigeria_poly()
    if isinstance(n_polys, np.ndarray):
        n_polys = [n_polys]
        
    all_pts = np.vstack(n_polys)
    min_x, max_x = np.min(all_pts[:, 0]), np.max(all_pts[:, 0])
    min_y, max_y = np.min(all_pts[:, 1]), np.max(all_pts[:, 1])

    target_x0, target_y0 = 0.8, 1.8
    target_w, target_h = 3.6, 3.8

    for p in n_polys:
        norm_x = (p[:, 0] - min_x) / (max_x - min_x) * target_w + target_x0
        norm_y = (p[:, 1] - min_y) / (max_y - min_y) * target_h + target_y0
        poly_patch = Polygon(np.column_stack([norm_x, norm_y]), closed=True,
                             facecolor=CREAM, edgecolor=DEEP['green'], linewidth=2.5, zorder=2)
        ax.add_patch(poly_patch)

    # Label for Colonial Nigeria
    ax.text(2.6, 1.2, "Colonial Nigeria\n(Source of raw materials and market)",
            ha='center', va='top', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=DEEP['green'], lw=1.5))

    # Great Britain Representation on the right (Factory Icon / Industrial center)
    gb_x0, gb_y0 = 10.0, 2.0
    gb_w, gb_h = 3.2, 3.4

    # Card background for Industrial Great Britain
    card = FancyBboxPatch((gb_x0, gb_y0), gb_w, gb_h, boxstyle="round,pad=0.2",
                          facecolor=LAV, edgecolor=DEEP['lav'], linewidth=2, zorder=2)
    ax.add_patch(card)

    # Factory Graphic inside card
    fact_base = Rectangle((10.4, 2.3), 2.4, 1.4, facecolor='white', edgecolor=INK, lw=1.8, zorder=3)
    ax.add_patch(fact_base)
    roof_pts = np.array([
        [10.4, 3.7], [10.4, 4.3], [11.2, 3.7],
        [11.2, 4.3], [12.0, 3.7],
        [12.0, 4.3], [12.8, 3.7]
    ])
    roof = Polygon(roof_pts, closed=False, edgecolor=INK, lw=1.8, zorder=3)
    ax.add_patch(roof)
    chimney = Rectangle((12.3, 4.2), 0.35, 0.9, facecolor='white', edgecolor=INK, lw=1.8, zorder=3)
    ax.add_patch(chimney)
    
    ax.plot([12.4, 12.35, 12.5], [5.2, 5.35, 5.5], color=GREY, lw=2, zorder=3)
    ax.plot([12.55, 12.6, 12.75], [5.2, 5.4, 5.55], color=GREY, lw=2, zorder=3)
    
    ax.add_patch(Rectangle((10.7, 2.5), 0.4, 0.5, facecolor=DEEP['blue'], edgecolor=INK, lw=1, zorder=4))
    ax.add_patch(Rectangle((11.4, 2.5), 0.4, 0.5, facecolor=DEEP['blue'], edgecolor=INK, lw=1, zorder=4))
    ax.add_patch(Rectangle((12.1, 2.3), 0.4, 0.7, facecolor=INK, edgecolor=INK, lw=1, zorder=4))

    # Label for Great Britain
    ax.text(11.6, 1.2, "Great Britain\n(Industrial center)",
            ha='center', va='top', fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=DEEP['lav'], lw=1.5))

    # Flow Arrow 1: Outward from Nigeria to Great Britain (Upper curved arrow)
    ax.annotate(
        "", xy=(10.0, 4.8), xytext=(4.3, 4.8),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP['orange'],
            lw=4,
            mutation_scale=25,
            connectionstyle="arc3,rad=0.15"
        ),
        zorder=5
    )

    text_export = (
        "Raw materials exported\n"
        "Raw Materials (Palm oil, Cocoa, Groundnut, Tin)"
    )
    ax.text(7.1, 5.7, text_export, ha='center', va='center',
            fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=DEEP['orange'], lw=2),
            zorder=6)

    # Flow Arrow 2: Back from Great Britain to Nigeria (Lower curved arrow)
    ax.annotate(
        "", xy=(4.3, 2.9), xytext=(10.0, 2.9),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP['blue'],
            lw=4,
            mutation_scale=25,
            connectionstyle="arc3,rad=0.15"
        ),
        zorder=5
    )

    text_import = (
        "Manufactured goods imported\n"
        "Manufactured Goods (Textiles, Soap, Machinery)"
    )
    ax.text(7.1, 2.2, text_import, ha='center', va='center',
            fontsize=14, fontweight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=DEEP['blue'], lw=2),
            zorder=6)

    # Sketch map note
    ax.text(0.5, 0.4, "Sketch map: zones are approximate", fontsize=14, fontstyle='italic', color=GREY)

    save(fig, out)
