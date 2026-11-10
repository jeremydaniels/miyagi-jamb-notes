from style import *
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(13, 7.5)
    ax = fig.add_axes([0.04, 0.1, 0.92, 0.8])
    
    # World map limits
    ax.set_xlim(-170, 180)
    ax.set_ylim(-60, 85)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw world continents as base outline/fill
    world = continent_polys('World')
    for poly in world:
        pts = np.array(poly)
        ax.fill(pts[:, 0], pts[:, 1], color=CREAM, ec=GREY, lw=1.2, zorder=1)
        
    # Sparsely populated regions (Light shading)
    # 1. Northern Canada / Alaska
    sparse_canada = [
        (-165, 60), (-165, 72), (-130, 70), (-110, 75), (-80, 75), 
        (-60, 65), (-65, 55), (-95, 55), (-130, 58), (-165, 60)
    ]
    # 2. Sahara Desert
    sparse_sahara = [
        (-15, 18), (-15, 30), (0, 32), (25, 32), (35, 28), 
        (35, 18), (20, 15), (0, 16), (-15, 18)
    ]
    # 3. Amazon Basin
    sparse_amazon = [
        (-75, 2), (-60, 4), (-48, -2), (-50, -12), (-68, -10), (-75, -2), (-75, 2)
    ]
    # 4. Australian Outback
    sparse_outback = [
        (120, -20), (138, -20), (140, -30), (128, -32), (118, -28), (120, -20)
    ]
    # 5. Siberia / Central Asia
    sparse_siberia = [
        (60, 58), (90, 58), (130, 60), (150, 65), (140, 72), (90, 72), (60, 68), (60, 58)
    ]
    
    sparse_zones = [sparse_canada, sparse_sahara, sparse_amazon, sparse_outback, sparse_siberia]
    for sz in sparse_zones:
        poly = Polygon(sz, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], alpha=0.35, lw=1.5, zorder=2)
        ax.add_patch(poly)

    # Densely populated regions (Dark shading)
    # 1. North-Eastern USA
    dense_ne_usa = [
        (-88, 38), (-80, 44), (-71, 44), (-71, 40), (-76, 36), (-85, 36), (-88, 38)
    ]
    # 2. Western Europe
    dense_weur = [
        (-4, 43), (-5, 54), (2, 56), (14, 55), (15, 45), (5, 43), (-4, 43)
    ]
    # 3. India & Ganges Plain
    dense_india = [
        (70, 22), (76, 30), (88, 27), (90, 22), (82, 12), (76, 12), (70, 22)
    ]
    # 4. Eastern China
    dense_china = [
        (105, 23), (105, 38), (120, 38), (122, 30), (118, 22), (105, 23)
    ]
    
    dense_zones = [dense_ne_usa, dense_weur, dense_india, dense_china]
    for dz in dense_zones:
        poly = Polygon(dz, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], alpha=0.85, lw=2, zorder=3)
        ax.add_patch(poly)

    # Annotations for Densely Populated Areas
    ax.annotate("North-Eastern USA", xy=(-75, 41), xytext=(-110, 32),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                fontsize=14, fontweight="bold", color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("Western Europe", xy=(6, 48), xytext=(12, 65),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                fontsize=14, fontweight="bold", color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("India", xy=(79, 23), xytext=(52, 10),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                fontsize=14, fontweight="bold", color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("Eastern China", xy=(115, 32), xytext=(126, 48),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                fontsize=14, fontweight="bold", color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    # Annotations for Sparsely Populated Areas
    ax.annotate("Northern Canada", xy=(-105, 65), xytext=(-138, 78),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                fontsize=14, color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("Amazon Basin in\nSouth America", xy=(-62, -4), xytext=(-105, -20),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                fontsize=14, color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("Sahara Desert", xy=(12, 23), xytext=(-28, 6),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                fontsize=14, color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    ax.annotate("Australian Outback", xy=(130, -25), xytext=(108, -50),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                fontsize=14, color=INK,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=5)

    # Title & Caption
    fig.text(0.5, 0.94, "Global Population Distribution", ha="center", fontsize=18, fontweight="bold", color=INK)
    fig.text(0.5, 0.03, "Sketch map: zones are approximate", ha="center", fontsize=14, style="italic", color=INK)

    # Custom Key / Legend positioned cleanly in the South Pacific ocean without crowding
    legend_elements = [
        mpatches.Patch(facecolor=ORANGE, edgecolor=DEEP["orange"], alpha=0.85, label="Densely Populated"),
        mpatches.Patch(facecolor=BLUE, edgecolor=DEEP["blue"], alpha=0.35, label="Sparsely Populated")
    ]
    
    # Fixed: removed negative labelspacing and adjusted padding so text does not overlap
    ax.legend(handles=legend_elements, loc="lower left", bbox_to_anchor=(0.02, 0.05),
              fontsize=14, frameon=True, edgecolor=GREY, facecolor="white", framealpha=0.95,
              borderpad=1.0, labelspacing=1.2)

    save(fig, out)
