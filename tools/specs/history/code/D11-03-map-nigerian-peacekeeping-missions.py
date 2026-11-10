from style import *
import numpy as np
import matplotlib.pyplot as plt

def _draw_polys(ax, polys, **kwargs):
    """Safely plot polygons returned by style helpers (handles Nx2 arrays or lists of arrays)."""
    if isinstance(polys, np.ndarray):
        if polys.ndim == 2:
            ax.fill(polys[:, 0], polys[:, 1], **kwargs)
        elif polys.ndim == 3:
            for p in polys:
                ax.fill(p[:, 0], p[:, 1], **kwargs)
    elif isinstance(polys, (list, tuple)):
        for item in polys:
            p = np.asarray(item)
            if p.ndim == 2:
                ax.fill(p[:, 0], p[:, 1], **kwargs)
            elif p.ndim == 1 and len(p) == 2:
                continue

def draw(out):
    fig = canvas(11, 10)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Africa continent outline / polygons
    africa = continent_polys('Africa')
    _draw_polys(ax, africa, color=CREAM, ec=GREY, lw=1.2, zorder=1)
        
    # Nigeria polygon highlight
    nig = nigeria_poly()
    _draw_polys(ax, nig, color=GREEN, ec=DEEP['green'], lw=2.0, zorder=3)
        
    # Nigeria origin coordinates (approx center of Nigeria: lon 8.0, lat 9.5)
    nig_coord = (8.0, 9.5)
    ax.plot(nig_coord[0], nig_coord[1], marker='o', color=DEEP['green'], markersize=8, zorder=5)
    ax.text(nig_coord[0], nig_coord[1] - 2.5, "NIGERIA\n(Origin)", color=INK, fontsize=15, 
            fontweight='bold', ha='center', va='top', zorder=6,
            bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.2', lw=1.5))

    # Destinations: name, (lon, lat), label_offset, curve_rad, text_align
    interventions = [
        ("Sierra Leone", (-11.7, 8.5), (-13.5, 10.5), -0.15, "right"),
        ("Liberia", (-9.5, 6.4), (-11.0, 4.0), -0.15, "right"),
        ("Guinea-Bissau", (-15.2, 11.9), (-16.5, 13.8), -0.15, "right"),
        ("Chad", (18.5, 15.4), (20.0, 17.5), 0.1, "left"),
        ("Sudan / Darfur", (26.0, 14.5), (28.5, 15.0), 0.15, "left"),
        ("Congo (DRC)", (23.5, -2.5), (25.5, -4.0), -0.15, "left"),
    ]

    for name, target, label_pos, rad, align in interventions:
        # Draw curved bold arrow from Nigeria to target
        ax.annotate(
            "",
            xy=target,
            xytext=nig_coord,
            arrowprops=dict(
                arrowstyle="-|>",
                color=DEEP["blue"],
                lw=2.5,
                mutation_scale=18,
                connectionstyle=f"arc3,rad={rad}"
            ),
            zorder=4
        )
        # Star marker at target
        ax.plot(target[0], target[1], marker='*', markersize=16, 
                color=DEEP["orange"], markeredgecolor=INK, markeredgewidth=1.0, zorder=5)
        # Label text
        ax.text(label_pos[0], label_pos[1], name, fontsize=14, color=INK,
                fontweight='semibold', ha=align, va='center', zorder=6,
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', lw=1.0))

    # Title
    ax.text(15, 36, "Nigeria's Major Peacekeeping Interventions in Africa", 
            fontsize=17, fontweight='bold', color=INK, ha='center', va='top')
    
    # Legend panel
    leg_x, leg_y = -17, -25
    ax.plot([leg_x], [leg_y + 4], marker='*', markersize=14, color=DEEP["orange"], markeredgecolor=INK)
    ax.text(leg_x + 2, leg_y + 4, "Peacekeeping mission zone", fontsize=14, va='center', color=INK)
    
    ax.annotate("", xy=(leg_x + 1.2, leg_y), xytext=(leg_x - 1.2, leg_y),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.5, mutation_scale=14))
    ax.text(leg_x + 2, leg_y, "Intervention deployment path", fontsize=14, va='center', color=INK)
    
    ax.fill([leg_x - 1.2, leg_x + 1.2, leg_x + 1.2, leg_x - 1.2], 
            [leg_y - 4.8, leg_y - 4.8, leg_y - 3.2, leg_y - 3.2], 
            color=GREEN, ec=DEEP['green'], lw=1.5)
    ax.text(leg_x + 2, leg_y - 4, "Nigeria", fontsize=14, va='center', color=INK)
    
    ax.text(15, -36, "Sketch map: zones are approximate", fontsize=14, 
            style='italic', color=GREY, ha='center', va='bottom')

    ax.set_xlim(-22, 52)
    ax.set_ylim(-38, 38)
    
    save(fig, out)
