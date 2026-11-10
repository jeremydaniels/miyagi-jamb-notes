from style import *
import numpy as np
import matplotlib.patches as mpatches

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Get Nigeria polygon
    poly = nigeria_poly()
    poly_patch = mpatches.Polygon(poly, closed=True, fc='none', ec=INK, lw=2.0, zorder=10)

    # Rivers Niger and Benue coordinates (realistic courses within Nigeria)
    # Niger: enters NW (~3.6E, 11.7N) -> Jebba (~4.8E, 9.1N) -> Lokoja (~6.74E, 7.80N) -> Delta (~6.1E, 4.3N)
    niger_upper = np.array([
        [3.6, 11.7],
        [4.2, 10.5],
        [4.6, 9.7],
        [5.3, 8.9],
        [6.0, 8.4],
        [6.74, 7.80]
    ])
    
    # Benue: enters E (~12.8E, 9.0N) -> Makurdi (~8.5E, 7.7N) -> Lokoja (~6.74E, 7.80N)
    benue = np.array([
        [12.8, 9.0],
        [12.0, 9.3],
        [10.8, 8.9],
        [9.8, 8.0],
        [8.5, 7.7],
        [7.6, 7.8],
        [6.74, 7.80]
    ])

    niger_lower = np.array([
        [6.74, 7.80],
        [6.7, 7.0],
        [6.6, 6.2],
        [6.2, 5.4],
        [6.0, 4.4]
    ])

    # Territorial split boundary (~7.1°N approx historical boundary)
    div_y = 7.1
    
    north_rect = mpatches.Polygon(
        [[2.0, div_y], [15.5, div_y], [15.5, 15.0], [2.0, 15.0]],
        closed=True,
        fc='#FFF3B0',  # soft yellow
        ec='none',
        zorder=2
    )
    south_rect = mpatches.Polygon(
        [[2.0, 3.5], [15.5, 3.5], [15.5, div_y], [2.0, div_y]],
        closed=True,
        fc=GREEN,      # soft green
        ec='none',
        zorder=2
    )
    
    # Clip regions to Nigeria's outline
    clip_path = mpatches.Polygon(poly, closed=True, transform=ax.transData)
    north_rect.set_clip_path(clip_path)
    south_rect.set_clip_path(clip_path)
    
    ax.add_patch(north_rect)
    ax.add_patch(south_rect)
    ax.add_patch(poly_patch)

    # Dividing boundary line dashed across Nigeria
    ax.plot([2.7, 11.9], [div_y, div_y], ls='--', color=GREY, lw=1.5, zorder=4)

    # Plot Rivers
    ax.plot(niger_upper[:, 0], niger_upper[:, 1], color=DEEP['blue'], lw=3, zorder=6)
    ax.plot(benue[:, 0], benue[:, 1], color=DEEP['blue'], lw=3, zorder=6)
    ax.plot(niger_lower[:, 0], niger_lower[:, 1], color=DEEP['blue'], lw=3.5, zorder=6)

    # River labels
    ax.text(4.8, 9.3, 'River Niger', color=DEEP['blue'], fontsize=14, fontweight='bold',
            rotation=-45, ha='center', va='center', zorder=8,
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.85))
    ax.text(9.7, 8.4, 'River Benue', color=DEEP['blue'], fontsize=14, fontweight='bold',
            rotation=-10, ha='left', va='bottom', zorder=8,
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.85))

    # Territory labels
    ax.text(8.0, 10.8, 'Protectorate of\nNorthern Nigeria',
            fontsize=17, fontweight='bold', color=INK, ha='center', va='center', zorder=7,
            bbox=dict(fc='white', ec='none', pad=4, alpha=0.85))
    
    ax.text(8.7, 5.8, 'Colony and Protectorate\nof Southern Nigeria',
            fontsize=16, fontweight='bold', color=INK, ha='center', va='center', zorder=7,
            bbox=dict(fc='white', ec='none', pad=4, alpha=0.85))

    # Lagos marker (approx 3.4°E, 6.45°N)
    lagos_x, lagos_y = 3.4, 6.45
    ax.scatter([lagos_x], [lagos_y], color=DEEP['pink'], s=90, zorder=12, edgecolor=INK, lw=1.2)
    ax.annotate('Lagos', xy=(lagos_x, lagos_y), xytext=(lagos_x - 0.2, lagos_y - 0.75),
                fontsize=15, fontweight='bold', color=INK, ha='center',
                arrowprops=dict(arrowstyle='->', color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'), zorder=13)

    # Ocean label placed well clear of the Niger delta and lower river course (x=6.0 to 6.7)
    ax.text(5.5, 3.8, 'Gulf of Guinea', fontsize=14, style='italic', color=DEEP['blue'], ha='center',
            bbox=dict(fc='white', ec='none', pad=2, alpha=0.9), zorder=8)

    # Title & Caption
    ax.text(8.5, 14.1, 'Nigeria c. 1910', fontsize=18, fontweight='bold', color=INK, ha='center')
    ax.text(8.5, 3.1, 'Sketch map: zones are approximate', fontsize=14, style='italic', color=GREY, ha='center')

    ax.set_xlim(1.8, 15.2)
    ax.set_ylim(2.8, 14.5)

    save(fig, out)
