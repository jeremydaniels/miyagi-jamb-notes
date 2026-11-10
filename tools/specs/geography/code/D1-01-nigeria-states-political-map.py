import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
from style import *

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    
    # Clean axes, set limits for Nigeria approximately
    # Nigeria bounding box is roughly 3°E to 15°E, 4°N to 14°N
    ax.set_xlim(2.5, 15.5)
    ax.set_ylim(3.5, 14.5)
    ax.axis('off')
    
    # Draw Nigeria boundary
    poly = nigeria_poly()
    ax.add_patch(patches.Polygon(poly, facecolor=CREAM, edgecolor=INK, linewidth=2.5, zorder=1))
    
    # Label "Nigeria"
    ax.text(8.5, 11, "Nigeria", fontsize=24, fontweight='bold', color=INK, ha='center', va='center', zorder=2)
    
    # Mark Abuja (approx 7.49E, 9.07N)
    abuja_x, abuja_y = 7.49, 9.07
    ax.plot(abuja_x, abuja_y, marker='o', markersize=10, color=DEEP['orange'], zorder=3)
    ax.text(abuja_x + 0.3, abuja_y, "Abuja (FCT)", fontsize=16, color=INK, ha='left', va='center', 
            path_effects=[pe.withStroke(linewidth=3, foreground="white")], zorder=4)
    
    # Geographic grid lines and labels at the edges
    ax.axhline(4, color=GREY, linestyle='--', linewidth=1, zorder=0)
    ax.text(9, 3.8, "4°N", fontsize=16, color=INK, ha='center', va='top')
    
    ax.axhline(14, color=GREY, linestyle='--', linewidth=1, zorder=0)
    ax.text(9, 14.2, "14°N", fontsize=16, color=INK, ha='center', va='bottom')
    
    ax.axvline(3, color=GREY, linestyle='--', linewidth=1, zorder=0)
    ax.text(2.8, 9, "3°E", fontsize=16, color=INK, ha='right', va='center', rotation=90)
    
    ax.axvline(15, color=GREY, linestyle='--', linewidth=1, zorder=0)
    ax.text(15.2, 9, "15°E", fontsize=16, color=INK, ha='left', va='center', rotation=-90)
    
    # Simple four-point compass rose in top-right
    compass_x, compass_y = 13.5, 12.5
    size = 0.8
    # N-S line
    ax.plot([compass_x, compass_x], [compass_y - size, compass_y + size], color=INK, linewidth=2)
    # E-W line
    ax.plot([compass_x - size, compass_x + size], [compass_y, compass_y], color=INK, linewidth=2)
    # Triangles for N
    ax.fill([compass_x - 0.2, compass_x, compass_x + 0.2], [compass_y, compass_y + size, compass_y], color=INK, zorder=5)
    
    # Labels for compass
    ax.text(compass_x, compass_y + size + 0.2, "N", fontsize=14, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(compass_x, compass_y - size - 0.2, "S", fontsize=14, fontweight='bold', ha='center', va='top', color=INK)
    ax.text(compass_x + size + 0.2, compass_y, "E", fontsize=14, fontweight='bold', ha='left', va='center', color=INK)
    ax.text(compass_x - size - 0.2, compass_y, "W", fontsize=14, fontweight='bold', ha='right', va='center', color=INK)
    
    save(fig, out)
