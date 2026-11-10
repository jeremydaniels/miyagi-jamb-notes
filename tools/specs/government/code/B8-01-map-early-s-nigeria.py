from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Boundary definitions for early 1960s Nigeria regions (approximate schematic outlines)
    # Confluence at Lokoja roughly (6.7, 7.8)
    
    # Northern Region: covers majority of the north
    north_pts = np.array([
        [3.6, 11.7], [4.2, 13.0], [5.5, 13.8], [8.5, 13.8], [12.0, 13.5],
        [13.8, 13.0], [14.5, 12.5], [13.5, 10.5], [12.0, 9.3], [10.0, 8.5],
        [8.5, 8.0], [6.7, 7.8], [5.5, 8.3], [4.5, 8.8], [3.5, 9.5],
        [2.7, 10.5], [3.6, 11.7]
    ])
    
    # Western Region (including Mid-West): South-West
    west_pts = np.array([
        [2.7, 10.5], [3.5, 9.5], [4.5, 8.8], [5.5, 8.3], [6.7, 7.8],
        [6.7, 6.2], [6.5, 5.4], [6.0, 4.3], [4.8, 5.8], [3.5, 6.4],
        [2.7, 6.4], [2.7, 10.5]
    ])
    
    # Eastern Region: South-East
    east_pts = np.array([
        [6.7, 7.8], [8.5, 8.0], [10.0, 8.5], [9.5, 6.8], [9.0, 5.5],
        [8.5, 4.7], [7.2, 4.4], [6.0, 4.3], [6.5, 5.4], [6.7, 6.2], [6.7, 7.8]
    ])
    
    # Draw Regions with specified soft colors / palette
    poly_north = Polygon(north_pts, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], linewidth=2.5, zorder=2)
    poly_west = Polygon(west_pts, closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], linewidth=2.5, zorder=2)
    poly_east = Polygon(east_pts, closed=True, facecolor=PINK, edgecolor=DEEP['pink'], linewidth=2.5, zorder=2)
    
    ax.add_patch(poly_north)
    ax.add_patch(poly_west)
    ax.add_patch(poly_east)
    
    # Internal Rivers indicating the regional boundaries
    niger_river = np.array([[3.6, 11.7], [4.5, 9.8], [5.5, 8.5], [6.7, 7.8], [6.7, 6.0], [6.0, 4.3]])
    benue_river = np.array([[12.0, 9.3], [10.0, 8.5], [8.5, 8.0], [6.7, 7.8]])
    ax.plot(niger_river[:, 0], niger_river[:, 1], color='white', lw=3, zorder=3, linestyle='--')
    ax.plot(benue_river[:, 0], benue_river[:, 1], color='white', lw=3, zorder=3, linestyle='--')
    
    # Regional Labels
    ax.text(8.5, 11.2, "NORTHERN REGION", fontsize=16, fontweight='bold', color=INK, ha='center', va='center', zorder=4)
    ax.text(8.5, 10.3, "NPC Dominance", fontsize=15, color=DEEP['green'], ha='center', va='center', fontweight='semibold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['green'], lw=1.2), zorder=4)
    
    ax.text(4.4, 7.5, "WESTERN\nREGION", fontsize=15, fontweight='bold', color=INK, ha='center', va='center', zorder=4)
    ax.text(4.4, 6.2, "AG Dominance", fontsize=14, color=DEEP['blue'], ha='center', va='center', fontweight='semibold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['blue'], lw=1.2), zorder=4)
    
    ax.text(8.1, 6.6, "EASTERN\nREGION", fontsize=15, fontweight='bold', color=INK, ha='center', va='center', zorder=4)
    ax.text(8.1, 5.3, "NCNC Dominance", fontsize=14, color=DEEP['pink'], ha='center', va='center', fontweight='semibold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['pink'], lw=1.2), zorder=4)
    
    # Title
    ax.text(8.5, 14.8, "Nigeria in the Early 1960s: Regions & Political Dominance", 
            fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
    
    # Schematic note caption
    ax.text(8.5, 3.4, "Sketch map: zones are approximate", fontsize=14, color=GREY, ha='center', va='center', style='italic')

    # Legend / Key
    legend_elements = [
        Patch(facecolor=GREEN, edgecolor=DEEP['green'], label='Northern Region (NPC Dominance)'),
        Patch(facecolor=BLUE, edgecolor=DEEP['blue'], label='Western Region (AG Dominance)'),
        Patch(facecolor=PINK, edgecolor=DEEP['pink'], label='Eastern Region (NCNC Dominance)')
    ]
    ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.05),
              ncol=1, frameon=True, fontsize=14, edgecolor=GREY, facecolor='white')
    
    ax.set_xlim(1.5, 15.5)
    ax.set_ylim(0.0, 15.5)
    
    save(fig, out)
