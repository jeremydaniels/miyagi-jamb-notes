from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    
    # Draw Nigeria boundary
    nigeria = nigeria_poly()
    ax.add_patch(Polygon(nigeria, fc=CREAM, ec=INK, lw=2, zorder=1))
    
    # Set map limits
    ax.set_xlim(2.5, 15)
    ax.set_ylim(4, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Horizontal dashed line for regions
    # Approximate middle division roughly at latitude 9.0
    ax.plot([2.5, 14.5], [9.0, 9.0], color=GREY, linestyle='--', lw=2.5, zorder=2)
    
    # Zone Labels
    ax.text(12.5, 12.0, "Northern Provinces", fontsize=16, ha='center', va='center', 
            color=INK, fontweight='bold', bbox=dict(fc='white', ec='none', pad=3))
    
    # Place Southern Provinces label to the left of the Lagos-Kano line
    ax.text(4.2, 7.8, "Southern Provinces", fontsize=16, ha='right', va='center', 
            color=INK, fontweight='bold', bbox=dict(fc='white', ec='none', pad=3))
    
    # City coordinates
    cities = {
        "Lagos": (3.4, 6.5),
        "Kano": (8.5, 12.0),
        "Port Harcourt": (7.0, 4.8),
        "Enugu": (7.5, 6.4)
    }
    
    # Draw Railways
    # Lagos to Kano
    ax.plot([cities["Lagos"][0], cities["Kano"][0]], 
            [cities["Lagos"][1], cities["Kano"][1]], 
            color=DEEP['orange'], lw=3.5, zorder=3)
    
    # Port Harcourt to Enugu
    ax.plot([cities["Port Harcourt"][0], cities["Enugu"][0]], 
            [cities["Port Harcourt"][1], cities["Enugu"][1]], 
            color=DEEP['orange'], lw=3.5, zorder=3)
    
    # Draw Dots and City Labels
    # Offsets for text to avoid overlapping lines
    offsets = {
        "Lagos": (0, -0.4),
        "Kano": (0, 0.4),
        "Port Harcourt": (0, -0.4),
        "Enugu": (0.2, 0.2)
    }
    
    for city, (cx, cy) in cities.items():
        # Black dot
        ax.plot(cx, cy, marker='o', color=INK, markersize=8, zorder=4)
        
        # City label
        ox, oy = offsets[city]
        ha = 'left' if ox > 0 else ('right' if ox < 0 else 'center')
        va = 'bottom' if oy > 0 else ('top' if oy < 0 else 'center')
        
        ax.text(cx + ox, cy + oy, city, fontsize=15, ha=ha, va=va, color=INK,
                bbox=dict(fc='white', ec='none', pad=1.5), zorder=5)
    
    save(fig, out)
