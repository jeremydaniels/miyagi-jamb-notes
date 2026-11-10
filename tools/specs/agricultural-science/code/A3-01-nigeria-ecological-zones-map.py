from style import *
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0.05, 0.08, 0.62, 0.84])
    
    # Get Nigeria polygon
    poly_coords = nigeria_poly()
    # Close polygon if not closed
    if not np.allclose(poly_coords[0], poly_coords[-1]):
        poly_coords = np.vstack([poly_coords, poly_coords[0]])
        
    nig_path = Path(poly_coords)
    
    # Custom soft palette colours for vegetation zones
    c_mangrove = "#2d6a4f"      # Dark green (Mangrove Swamp)
    c_rainforest = GREEN        # Green (Rainforest)
    c_derived = "#b7e4c7"       # Light green (Derived Savanna)
    c_guinea = "#e9d8a6"        # Yellow-green (Guinea Savanna)
    c_sudan = ORANGE            # Orange-yellow (Sudan Savanna)
    c_sahel = "#fef08a"         # Pale yellow (Sahel Savanna)
    c_montane = LAV             # Purple patch for Jos Plateau
    
    # Shading the bands using horizontal strips across the country
    # Base bands (Sudan Savanna covers the northern section)
    bands = [
        (4.0, 5.4, c_mangrove),
        (5.4, 6.9, c_rainforest),
        (6.9, 8.2, c_derived),
        (8.2, 11.0, c_guinea),
        (11.0, 14.5, c_sudan),  # Covers north up to border
    ]
    
    for lat_min, lat_max, col in bands:
        rect = mpatches.Rectangle((2.0, lat_min), 13.5, lat_max - lat_min,
                                  facecolor=col, edgecolor="none", lw=0)
        rect.set_clip_path(nig_path, transform=ax.transData)
        ax.add_patch(rect)
        
    # Sahel Savanna restricted to the extreme northeast corner (around Lake Chad / Borno)
    # A polygon covering the extreme northeast section of Nigeria (long > 11.5°E, lat > 12.0°N)
    sahel_coords = np.array([
        [11.2, 14.2],
        [15.0, 14.2],
        [15.0, 11.8],
        [12.8, 12.4],
        [11.2, 13.5],
        [11.2, 14.2]
    ])
    sahel_poly = mpatches.Polygon(sahel_coords, facecolor=c_sahel, edgecolor="none", zorder=2)
    sahel_poly.set_clip_path(nig_path, transform=ax.transData)
    ax.add_patch(sahel_poly)

    # Jos Plateau (Montane) - approx 8.5°E to 9.5°E, 9.0°N to 10.0°N
    montane_patch = mpatches.Ellipse((9.0, 9.5), 1.3, 0.9, angle=25,
                                     facecolor=c_montane, edgecolor=DEEP["lav"], lw=1.5, zorder=3)
    montane_patch.set_clip_path(nig_path, transform=ax.transData)
    ax.add_patch(montane_patch)
    
    # Boundary of Nigeria
    border = mpatches.Polygon(poly_coords, facecolor="none", edgecolor=INK, lw=2.0, zorder=4)
    ax.add_patch(border)
    
    # Label Jos Plateau on map
    ax.annotate("Jos Plateau\n(Montane)", xy=(9.1, 9.5), xytext=(11.5, 9.2),
                fontsize=14, color=INK, weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                ha="left", va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9),
                zorder=6)
    
    # Map extent and styling
    ax.set_xlim(2.3, 15.0)
    ax.set_ylim(4.0, 14.2)
    ax.set_aspect("equal")
    ax.axis("off")
    
    # Compass Rose at top left
    cx, cy = 3.8, 12.8
    ax.annotate("", xy=(cx, cy + 0.9), xytext=(cx, cy),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20),
                zorder=7)
    ax.text(cx, cy + 1.05, "N", ha="center", va="bottom", fontsize=16, weight="bold", color=INK)
    ax.plot([cx - 0.4, cx + 0.4], [cy + 0.35, cy + 0.35], color=INK, lw=1.5, zorder=7)
    
    # Caption
    ax.text(8.5, 3.8, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", color=INK, ha="center")
    
    # Title
    fig.text(0.5, 0.94, "Ecological Zones of Nigeria",
             fontsize=20, weight="bold", color=INK, ha="center")
    
    # Legend panel on the right side
    legend_items = [
        ("Sahel Savanna", c_sahel),
        ("Sudan Savanna", c_sudan),
        ("Guinea Savanna", c_guinea),
        ("Derived Savanna", c_derived),
        ("Rainforest", c_rainforest),
        ("Mangrove Swamp", c_mangrove),
        ("Montane (Jos Plateau)", c_montane)
    ]
    
    leg_ax = fig.add_axes([0.68, 0.22, 0.28, 0.58])
    leg_ax.axis("off")
    
    leg_ax.text(0.05, 0.95, "Ecological Zones", fontsize=16, weight="bold", color=INK, va="top")
    
    y_step = 0.12
    y_start = 0.82
    for i, (name, col) in enumerate(legend_items):
        y = y_start - i * y_step
        rect = mpatches.Rectangle((0.05, y - 0.04), 0.14, 0.07,
                                  facecolor=col, edgecolor=INK, lw=1.2)
        leg_ax.add_patch(rect)
        leg_ax.text(0.24, y - 0.005, name, fontsize=14, color=INK, va="center")
        
    save(fig, out)
