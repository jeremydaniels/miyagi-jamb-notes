import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_subplot(111)
    
    # Map Extents for West Africa
    ax.set_xlim(-18, 16)
    ax.set_ylim(3, 21)
    ax.axis('off')
    
    # Outline map of West Africa (using Africa polygon without internal borders)
    # By setting edgecolor='none' and facecolor=CREAM on a white background,
    # it forms a simple outline map with no internal borders.
    africa_polys = continent_polys('Africa')
    for poly in africa_polys:
        ax.add_patch(patches.Polygon(poly, facecolor=CREAM, edgecolor='none', zorder=1))
    
    # Background ocean (for bounds)
    fig.patch.set_facecolor('white')
    
    # Points of interest
    pts = {
        "Bussa": (4.5, 10.0),
        "Niger Delta": (6.0, 5.0),
        "Lake Chad": (14.0, 13.0),
        "Sokoto": (5.2, 13.0)
    }
    
    # River Niger (Thick blue line)
    # Rises in Guinea, flows NE to Mali, then SE through Niger and Nigeria
    river_x = np.array([-10.5, -9.0, -7.0, -4.0, -1.0, 1.5, 3.5, pts["Bussa"][0], 5.2, pts["Niger Delta"][0]])
    river_y = np.array([9.0, 10.5, 12.5, 15.0, 16.5, 15.0, 12.0, pts["Bussa"][1], 8.0, pts["Niger Delta"][1]])
    
    # Smooth river interpolation
    t = np.linspace(0, 1, len(river_x))
    t_smooth = np.linspace(0, 1, 100)
    rx = np.interp(t_smooth, t, river_x)
    ry = np.interp(t_smooth, t, river_y)
    ax.plot(rx, ry, color=BLUE, linewidth=6, zorder=2)
    
    # Mungo Park's route (Dotted red line: West coast to Bussa)
    park_x = [-16.0, -13.0, -9.0, -6.0, -3.0, 1.0, pts["Bussa"][0]]
    park_y = [13.5, 14.5, 13.5, 14.0, 13.0, 11.5, pts["Bussa"][1]]
    ax.plot(park_x, park_y, color=DEEP['pink'], linewidth=3, linestyle='dotted', zorder=3)
    
    # Lander brothers' route (Solid blue line: Bussa to Niger Delta along the river)
    lander_idx = (rx >= pts["Bussa"][0]) & (ry <= pts["Bussa"][1])
    ax.plot(rx[lander_idx], ry[lander_idx], color=DEEP['blue'], linewidth=3, zorder=4)
    
    # Barth's route (Dashed green loop: Across the north through Sokoto toward Lake Chad)
    barth_x = [3.0, pts["Sokoto"][0], 9.0, pts["Lake Chad"][0], 11.0, 8.0, 4.0, 3.0]
    barth_y = [15.0, pts["Sokoto"][1], 12.0, pts["Lake Chad"][1], 15.5, 14.5, 15.5, 15.0]
    t_barth = np.linspace(0, 1, len(barth_x))
    bx = np.interp(t_smooth, t_barth, barth_x)
    by = np.interp(t_smooth, t_barth, barth_y)
    ax.plot(bx, by, color=DEEP['green'], linewidth=3, linestyle='dashed', zorder=3)
    
    # Lake Chad water body representation
    ax.add_patch(patches.Ellipse((pts["Lake Chad"][0], pts["Lake Chad"][1]), 1.5, 1.0, color=BLUE, zorder=2))
    
    # Plot dots for specific locations
    for name, (px, py) in pts.items():
        ax.plot(px, py, 'o', color='black', markersize=8, zorder=5)
        
    # Labels
    bbox_props = dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8)
    
    ax.text(pts["Bussa"][0] - 0.5, pts["Bussa"][1] + 0.5, "Bussa", 
            fontsize=16, color=INK, ha='right', va='bottom', bbox=bbox_props, zorder=6)
            
    ax.text(pts["Niger Delta"][0] + 0.5, pts["Niger Delta"][1], "Niger Delta", 
            fontsize=16, color=INK, ha='left', va='center', bbox=bbox_props, zorder=6)
            
    ax.text(pts["Lake Chad"][0], pts["Lake Chad"][1] - 1.0, "Lake Chad", 
            fontsize=16, color=INK, ha='center', va='top', bbox=bbox_props, zorder=6)
            
    ax.text(pts["Sokoto"][0], pts["Sokoto"][1] + 0.5, "Sokoto", 
            fontsize=16, color=INK, ha='center', va='bottom', bbox=bbox_props, zorder=6)
            
    # River Niger label
    ax.text(-2.0, 15.5, "River Niger", fontsize=16, color=DEEP['blue'], 
            ha='center', va='center', rotation=15, bbox=bbox_props, zorder=6)
    
    # Sketch map disclaimer
    ax.text(-17.5, 3.5, "Sketch map: zones are approximate", fontsize=14, color=GREY, style='italic', zorder=6)

    save(fig, out)
