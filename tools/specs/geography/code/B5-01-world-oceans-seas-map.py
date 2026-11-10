from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0.05, 0.08, 0.9, 0.85])
    
    # Map projection / coordinate bounds (Equirectangular -180 to 180, -80 to 85)
    ax.set_xlim(-180, 180)
    ax.set_ylim(-70, 85)
    ax.set_facecolor(BLUE)
    
    # Draw continents
    world = continent_polys('World')
    for poly in world:
        pts = np.asarray(poly)
        ax.add_patch(Polygon(pts, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], linewidth=0.8, zorder=2))
        
    # Ocean labels (Bold dark blue)
    # Pacific Ocean (split into West and East or labelled across)
    ax.text(-140, 0, "PACIFIC\nOCEAN", color=DEEP["blue"], fontsize=16, fontweight="bold", 
            ha="center", va="center", zorder=3)
    ax.text(160, 0, "PACIFIC\nOCEAN", color=DEEP["blue"], fontsize=15, fontweight="bold", 
            ha="center", va="center", zorder=3)
    ax.text(-35, 0, "ATLANTIC\nOCEAN", color=DEEP["blue"], fontsize=16, fontweight="bold", 
            ha="center", va="center", zorder=3)
    ax.text(80, -15, "INDIAN\nOCEAN", color=DEEP["blue"], fontsize=16, fontweight="bold", 
            ha="center", va="center", zorder=3)
    ax.text(0, -60, "SOUTHERN OCEAN", color=DEEP["blue"], fontsize=15, fontweight="bold", 
            ha="center", va="center", zorder=3, bbox=dict(fc="white", ec="none", alpha=0.5, pad=2))
    ax.text(0, 78, "ARCTIC OCEAN", color=DEEP["blue"], fontsize=15, fontweight="bold", 
            ha="center", va="center", zorder=3, bbox=dict(fc="white", ec="none", alpha=0.5, pad=2))

    # Regional seas annotations
    # Mediterranean Sea (~18°E, 35°N)
    ax.annotate("Mediterranean\nSea", xy=(18, 35), xytext=(20, 52),
                fontsize=14, color=INK, ha="center", va="bottom", zorder=4,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Red Sea (~38°E, 22°N)
    ax.annotate("Red Sea", xy=(38, 22), xytext=(55, 12),
                fontsize=14, color=INK, ha="left", va="center", zorder=4,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Caribbean Sea (~ -75°W, 15°N)
    ax.annotate("Caribbean\nSea", xy=(-75, 15), xytext=(-105, 15),
                fontsize=14, color=INK, ha="right", va="center", zorder=4,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Gulf of Guinea (~ 2°E, 2°N)
    ax.annotate("Gulf of\nGuinea", xy=(2, 2), xytext=(-18, -18),
                fontsize=14, color=INK, ha="right", va="top", zorder=4,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Remove axis ticks and frame styling
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color(GREY)
        spine.set_linewidth(1.0)
        
    ax.set_title("World Oceans and Major Seas", fontsize=18, color=INK, pad=12, fontweight="bold")
    
    save(fig, out)
