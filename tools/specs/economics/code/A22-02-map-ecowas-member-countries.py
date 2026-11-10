from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, FancyArrowPatch, Rectangle

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    
    # 15 ECOWAS members
    # Include multiple alias variants for robust matching in country_polys
    ecowas_names = [
        "Benin", "Burkina Faso", "Cape Verde", "Cabo Verde",
        "Ivory Coast", "Côte d'Ivoire", "Cote d'Ivoire",
        "Gambia", "The Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali",
        "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"
    ]
    
    # Background African continent for context
    try:
        africa = continent_polys('Africa')
        for poly in africa:
            ax.fill(*zip(*poly), color='#F5F6F8', edgecolor=GREY, lw=0.8, zorder=1)
    except Exception:
        pass
        
    # Draw ECOWAS countries highlighted in unified GREEN
    try:
        members = country_polys(*ecowas_names)
        for poly in members:
            ax.fill(*zip(*poly), color=GREEN, edgecolor=DEEP['green'], lw=1.2, zorder=2)
    except Exception:
        pass

    # Approximate centroids for regional trade / free movement flow arrows from Nigeria
    # Nigeria central hub
    nig_center = (8.0, 9.5)
    
    destinations = [
        ("Niger", (8.0, 16.0)),
        ("Mali", (-3.5, 17.0)),
        ("Burkina Faso", (-1.5, 12.5)),
        ("Benin / Togo", (1.8, 8.5)),
        ("Ghana / Côte d'Ivoire", (-3.5, 7.5)),
        ("Senegal / Guinea", (-11.5, 12.0)),
        ("Cape Verde", (-23.5, 16.0)),
    ]
    
    # Outward trade and movement arrows
    for name, dest in destinations:
        arrow = FancyArrowPatch(
            nig_center, dest,
            connectionstyle="arc3,rad=-0.15",
            arrowstyle="Simple,tail_width=2.5,head_width=7,head_length=8",
            color=DEEP["blue"],
            alpha=0.85,
            zorder=4
        )
        ax.add_patch(arrow)

    # Nigeria marker / center point
    ax.plot(nig_center[0], nig_center[1], marker='o', color=DEEP['blue'], markersize=7, zorder=5)
    ax.text(nig_center[0] + 0.3, nig_center[1] - 1.5, "NIGERIA", color=INK, fontsize=15, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["green"], lw=1.2), zorder=6)

    # Map extent encompassing West Africa and Cape Verde
    ax.set_xlim(-26.0, 16.0)
    ax.set_ylim(3.0, 25.0)
    ax.axis('off')

    # Title & Subtitle
    ax.text(-25.0, 24.0, "ECOWAS: Regional Trade & Free Movement", fontsize=18, fontweight='bold', color=INK, ha='left')
    ax.text(-25.0, 22.8, "Economic Community of West African States (15 Members)", fontsize=14, color=GREY, ha='left')

    # Legend / Annotation Box
    legend_box = Rectangle((-25.0, 4.0), 10.0, 4.2, facecolor="white", edgecolor=GREY, lw=1, zorder=5)
    ax.add_patch(legend_box)
    
    # Legend items
    patch_ecowas = Rectangle((-24.5, 6.7), 1.2, 0.8, facecolor=GREEN, edgecolor=DEEP['green'], lw=1, zorder=6)
    ax.add_patch(patch_ecowas)
    ax.text(-22.9, 7.0, "ECOWAS Member State", fontsize=14, va='center', color=INK, zorder=6)

    leg_arrow = FancyArrowPatch((-24.5, 5.2), (-23.3, 5.2),
                                arrowstyle="Simple,tail_width=2.5,head_width=6,head_length=7",
                                color=DEEP["blue"], zorder=6)
    ax.add_patch(leg_arrow)
    ax.text(-22.9, 5.2, "Regional trade & free\nmovement from Nigeria", fontsize=14, va='center', color=INK, zorder=6)

    # Simplified ECOWAS Logo Inset
    logo_x, logo_y = 12.0, 5.5
    outer_ring = Circle((logo_x, logo_y), 2.2, facecolor='white', edgecolor=DEEP['green'], lw=2.5, zorder=5)
    inner_ring = Circle((logo_x, logo_y), 1.8, facecolor=CREAM, edgecolor=DEEP['orange'], lw=1.5, zorder=6)
    ax.add_patch(outer_ring)
    ax.add_patch(inner_ring)
    ax.text(logo_x, logo_y + 0.3, "CEDEAO", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', zorder=7)
    ax.text(logo_x, logo_y - 0.4, "ECOWAS", fontsize=14, fontweight='bold', color=DEEP['green'], ha='center', va='center', zorder=7)
    ax.text(logo_x, logo_y - 2.8, "ECOWAS Logo", fontsize=14, ha='center', va='center', color=INK, zorder=7,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Caption
    ax.text(0.5, 0.02, "Sketch map: zones are approximate",
            transform=fig.transFigure, ha="center", fontsize=14, color=GREY)

    save(fig, out)
