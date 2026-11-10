from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 6)
    
    # Create 3 subplots side by side
    ax1 = fig.add_axes([0.05, 0.12, 0.27, 0.72])
    ax2 = fig.add_axes([0.37, 0.12, 0.27, 0.72])
    ax3 = fig.add_axes([0.69, 0.12, 0.27, 0.72])
    
    for ax in [ax1, ax2, ax3]:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(INK)
            spine.set_linewidth(1.5)
            
    # Helper to draw a building/house
    def draw_house(ax, x, y, size=0.55, color=DEEP['orange']):
        rect = patches.Rectangle((x - size/2, y - size/2), size, size, 
                                 facecolor=color, edgecolor=INK, linewidth=1.2, zorder=5)
        ax.add_patch(rect)

    # ---------------- panel 1: Dispersed ----------------
    ax1.set_facecolor(CREAM)
    ax1.set_title("Dispersed", fontsize=18, fontweight='bold', pad=15, color=INK)
    
    # Field boundaries (thin grey dashed lines)
    fields = [
        [(0, 3.5), (10, 3.5)],
        [(0, 7.0), (10, 7.0)],
        [(4.0, 0), (4.0, 10)],
        [(7.5, 0), (7.5, 10)]
    ]
    for p1, p2 in fields:
        ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color=GREY, lw=1.2, linestyle=':', zorder=1)
        
    # Minor winding track
    track_x = [0, 2.5, 5.0, 8.0, 10]
    track_y = [1.5, 3.0, 5.5, 6.5, 9.0]
    ax1.plot(track_x, track_y, color=GREY, lw=2, linestyle='--', zorder=2)
    
    # Scattered houses with small enclosures/farms
    dispersed_coords = [
        (2.0, 8.2), (8.5, 8.0), (1.5, 5.0), 
        (5.8, 6.2), (8.2, 3.8), (2.5, 1.8), (6.2, 1.5)
    ]
    for hx, hy in dispersed_coords:
        # small garden/field patch
        ax1.add_patch(patches.Rectangle((hx - 0.7, hy - 0.7), 1.4, 1.4, facecolor=GREEN, alpha=0.3, zorder=3, ec='none'))
        draw_house(ax1, hx, hy, size=0.6)
        
    ax1.text(5.0, -1.0, "Isolated farms scattered\nfar apart across fields", 
             ha='center', va='top', fontsize=14, color=INK)

    # ---------------- panel 2: Nucleated ----------------
    ax2.set_facecolor(CREAM)
    ax2.set_title("Nucleated", fontsize=18, fontweight='bold', pad=15, color=INK)
    
    # Crossroads
    road_w = 0.5
    # Road horizontal
    ax2.plot([0, 10], [5, 5], color=GREY, lw=10, zorder=2)
    ax2.plot([0, 10], [5, 5], color='white', lw=1.5, linestyle='--', zorder=3)
    # Road vertical
    ax2.plot([5, 5], [0, 10], color=GREY, lw=10, zorder=2)
    ax2.plot([5, 5], [0, 10], color='white', lw=1.5, linestyle='--', zorder=3)
    
    # Village centre / square
    ax2.add_patch(patches.Circle((5, 5), 1.6, facecolor='#E8E5DE', edgecolor=GREY, lw=1.5, zorder=4))
    
    # Church or central landmark
    church = patches.Rectangle((4.7, 4.7), 0.6, 0.6, facecolor=DEEP['pink'], edgecolor=INK, lw=1.2, zorder=6)
    ax2.add_patch(church)
    
    # Tightly clustered houses around crossroads
    nucleated_coords = [
        # NW cluster
        (3.8, 5.8), (4.3, 6.2), (3.6, 6.6), (4.3, 7.0), (3.7, 7.5),
        # NE cluster
        (5.7, 6.2), (6.3, 5.8), (5.7, 7.0), (6.4, 6.6), (6.3, 7.4),
        # SW cluster
        (3.8, 4.2), (4.3, 3.8), (3.5, 3.4), (4.2, 3.0), (3.6, 2.5),
        # SE cluster
        (5.7, 3.8), (6.2, 4.2), (5.7, 3.0), (6.4, 3.4), (6.3, 2.6)
    ]
    for hx, hy in nucleated_coords:
        draw_house(ax2, hx, hy, size=0.5)
        
    ax2.text(5.0, -1.0, "Dwellings clustered tightly\naround a central crossroads", 
             ha='center', va='top', fontsize=14, color=INK)

    # ---------------- panel 3: Linear ----------------
    ax3.set_facecolor(CREAM)
    ax3.set_title("Linear", fontsize=18, fontweight='bold', pad=15, color=INK)
    
    # Blue river winding slightly on left side
    river_x = np.array([2.5, 2.8, 2.6, 3.0, 2.7, 2.9])
    river_y = np.linspace(0, 10, len(river_x))
    # Interpolate for smooth curve
    y_fine = np.linspace(0, 10, 100)
    x_river_fine = np.interp(y_fine, river_y, river_x)
    ax3.plot(x_river_fine, y_fine, color=DEEP['blue'], lw=7, zorder=2, alpha=0.85)
    
    # Road running alongside
    road_x = 5.5
    ax3.plot([road_x, road_x], [0, 10], color=INK, lw=4, zorder=2)
    
    # Label river and road
    ax3.text(2.1, 8.8, "River", color=DEEP['blue'], fontsize=14, fontweight='bold', ha='right',
             bbox=dict(fc='white', ec='none', pad=1))
    ax3.text(5.5, 9.3, "Road", color=INK, fontsize=14, fontweight='bold', ha='center',
             bbox=dict(fc='white', ec='none', pad=1))
    
    # Houses aligned on both sides of road and river
    y_positions = np.linspace(0.8, 8.2, 8)
    for y in y_positions:
        # Houses between river and road
        draw_house(ax3, 4.5, y + np.random.uniform(-0.15, 0.15), size=0.55)
        # Houses to the right of road
        draw_house(ax3, 6.5, y + np.random.uniform(-0.15, 0.15), size=0.55)
        
    ax3.text(5.0, -1.0, "Houses lined up along\na river and transport route", 
             ha='center', va='top', fontsize=14, color=INK)

    save(fig, out)
