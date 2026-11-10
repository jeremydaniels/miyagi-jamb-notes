from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(18, 6.5)
    
    # Subplots
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)
    
    # ----------------------------------------------------
    # Panel 1: Topographical Map
    # ----------------------------------------------------
    ax1.set_title("Topographical Map", fontsize=16, weight="bold", color=INK, pad=12)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')
    ax1.set_facecolor("#FCFCF9")
    
    # Grid lines to evoke an OS / topographic map
    for g in range(1, 10):
        ax1.axhline(g, color=GREY, lw=0.6, ls=":", alpha=0.7)
        ax1.axvline(g, color=GREY, lw=0.6, ls=":", alpha=0.7)
        
    # Brown contour lines (hills)
    brown = "#8B5A2B"
    x = np.linspace(0, 10, 150)
    y = np.linspace(0, 10, 150)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-((X - 3.2)**2 + (Y - 7.0)**2) / 6.0) * 180 + 50
    Z2 = np.exp(-((X - 7.5)**2 + (Y - 3.0)**2) / 8.0) * 140 + 40
    Z = Z1 + Z2
    
    contours = ax1.contour(X, Y, Z, levels=[70, 90, 110, 130, 150, 170, 190], colors=brown, linewidths=1.6)
    ax1.clabel(contours, inline=True, fontsize=10, fmt='%d m', colors=brown)
    
    # Blue river
    riv_x = np.linspace(0, 10, 100)
    riv_y = 4.2 + 1.2 * np.sin(riv_x * 0.7) - 0.2 * riv_x
    ax1.plot(riv_x, riv_y, color=DEEP["blue"], lw=3.2, zorder=3, label="River")
    ax1.text(0.8, 4.8, "River", color=DEEP["blue"], fontsize=14, weight="bold", rotation=25)
    
    # Red road
    road_x = [1.5, 3.0, 5.5, 7.5, 9.5]
    road_y = [0.0, 2.5, 5.0, 7.5, 10.0]
    ax1.plot(road_x, road_y, color=DEEP["pink"], lw=3.0, zorder=4, label="Road")
    
    # Black square buildings
    buildings = [(2.6, 3.2), (3.4, 2.8), (3.1, 1.8), (6.0, 6.2), (6.5, 5.8), (7.0, 6.4)]
    for bx, by in buildings:
        rect = patches.Rectangle((bx - 0.2, by - 0.2), 0.4, 0.4, facecolor=INK, edgecolor="none", zorder=5)
        ax1.add_patch(rect)
    ax1.text(3.3, 1.3, "Buildings", color=INK, fontsize=14, ha="center")
    
    # Border
    for spine in ax1.spines.values():
        spine.set_edgecolor(INK)
        spine.set_linewidth(1.2)
    ax1.set_xticks([])
    ax1.set_yticks([])

    # ----------------------------------------------------
    # Panel 2: Thematic Map (Nigeria Population Density)
    # ----------------------------------------------------
    ax2.set_title("Thematic Map", fontsize=16, weight="bold", color=INK, pad=12)
    ax2.set_xlim(2.0, 15.5)
    ax2.set_ylim(3.5, 14.5)
    ax2.set_aspect('equal')
    ax2.set_facecolor("#FCFCF9")
    
    # Nigeria Poly outline
    nig_poly = nigeria_poly()
    
    # Draw outline
    base_patch = patches.Polygon(nig_poly, closed=True, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=2)
    ax2.add_patch(base_patch)
    
    # Regions representing density zones (schematic bands/polygons clipped inside)
    # High: South/Lagos & Kano (Red/Pink/Orange)
    # Medium: Middle belt / transitions
    # Low: Semi-arid North / Northeast / East
    
    # High density regions
    high_poly1 = np.array([[2.5, 4.0], [7.5, 4.0], [7.5, 7.0], [4.5, 7.2], [2.5, 6.5]])
    med_poly1 = np.array([[2.5, 6.5], [14.5, 6.5], [14.0, 10.5], [3.0, 10.0]])
    high_poly2 = np.array([[7.0, 11.0], [9.5, 11.0], [9.5, 13.0], [7.0, 13.0]])
    
    patch_high1 = patches.Polygon(high_poly1, closed=True, facecolor=ORANGE, alpha=0.75, clip_path=base_patch, zorder=3)
    patch_med = patches.Polygon(med_poly1, closed=True, facecolor=LAV, alpha=0.7, clip_path=base_patch, zorder=3)
    patch_high2 = patches.Polygon(high_poly2, closed=True, facecolor=ORANGE, alpha=0.8, clip_path=base_patch, zorder=4)
    
    ax2.add_patch(patch_med)
    ax2.add_patch(patch_high1)
    ax2.add_patch(patch_high2)
    
    # Re-stroke boundary
    ax2.plot(nig_poly[:, 0], nig_poly[:, 1], color=INK, lw=1.6, zorder=5)
    
    ax2.text(8.5, 8.8, "Nigeria", fontsize=15, weight="bold", color=INK, ha="center", zorder=6)
    ax2.text(8.5, 4.0, "Sketch map: zones are approximate", fontsize=11, color=GREY, ha="center", style="italic")
    
    # Legend for Thematic Map
    leg_x = 2.6
    leg_y = 12.8
    # High
    ax2.add_patch(patches.Rectangle((leg_x, leg_y), 0.7, 0.7, facecolor=ORANGE, edgecolor=INK, lw=1, zorder=6))
    ax2.text(leg_x + 0.9, leg_y + 0.15, "High density", fontsize=14, color=INK, va="bottom", zorder=6)
    # Medium
    ax2.add_patch(patches.Rectangle((leg_x, leg_y - 1.0), 0.7, 0.7, facecolor=LAV, edgecolor=INK, lw=1, zorder=6))
    ax2.text(leg_x + 0.9, leg_y - 0.85, "Medium density", fontsize=14, color=INK, va="bottom", zorder=6)
    # Low
    ax2.add_patch(patches.Rectangle((leg_x, leg_y - 2.0), 0.7, 0.7, facecolor=CREAM, edgecolor=INK, lw=1, zorder=6))
    ax2.text(leg_x + 0.9, leg_y - 1.85, "Low density", fontsize=14, color=INK, va="bottom", zorder=6)
    
    for spine in ax2.spines.values():
        spine.set_edgecolor(INK)
        spine.set_linewidth(1.2)
    ax2.set_xticks([])
    ax2.set_yticks([])

    # ----------------------------------------------------
    # Panel 3: Sketch Map
    # ----------------------------------------------------
    ax3.set_title("Sketch Map", fontsize=16, weight="bold", color=INK, pad=12)
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.set_aspect('equal')
    ax3.set_facecolor("#FCFCF9")
    
    # Hand-drawn style simple main road and side road
    # Main Road
    road_main_x = [1.0, 3.5, 5.0, 7.5, 9.0]
    road_main_y = [1.5, 3.5, 5.0, 6.5, 8.5]
    ax3.plot(road_main_x, road_main_y, color=INK, lw=3.0, ls="-")
    ax3.text(7.2, 7.5, "Main Road", color=INK, fontsize=14, rotation=40,
             bbox=dict(fc="white", ec="none", pad=1))
    
    # Side track
    side_x = [5.0, 3.5, 2.0]
    side_y = [5.0, 6.5, 7.5]
    ax3.plot(side_x, side_y, color=INK, lw=2.5, ls="--")
    
    # Market (symbol / label)
    mkt_x, mkt_y = 6.2, 4.0
    ax3.plot(mkt_x, mkt_y, 'o', ms=10, color=DEEP["orange"])
    ax3.text(mkt_x + 0.4, mkt_y - 0.2, "Market", color=INK, fontsize=14, weight="bold",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    # Church (with cross icon)
    ch_x, ch_y = 2.5, 3.0
    ax3.plot(ch_x, ch_y, 's', ms=12, color=DEEP["blue"])
    ax3.text(ch_x - 0.3, ch_y + 0.6, "Church", color=INK, fontsize=14, weight="bold",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    # Destination House and Arrow pointing "To my house"
    house_x, house_y = 1.8, 8.0
    ax3.plot(house_x, house_y, '^', ms=14, color=DEEP["green"])
    
    ax3.annotate("To my house",
                 xy=(house_x + 0.1, house_y + 0.1),
                 xytext=(4.2, 8.8),
                 fontsize=14,
                 weight="bold",
                 color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=2.0),
                 ha="left",
                 va="center",
                 bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3"))
    
    # Note "No grid lines" aesthetic
    for spine in ax3.spines.values():
        spine.set_edgecolor(INK)
        spine.set_linewidth(1.2)
    ax3.set_xticks([])
    ax3.set_yticks([])

    plt.tight_layout()
    save(fig, out)
