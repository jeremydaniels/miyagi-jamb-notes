from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Base and central pillar
    base = patches.Rectangle((4.0, 0.8), 2.0, 0.4, facecolor=GREY, edgecolor=INK, lw=2, zorder=2)
    pillar = patches.Rectangle((4.75, 1.2), 0.5, 3.8, facecolor=CREAM, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(base)
    ax.add_patch(pillar)

    # Central fulcrum / pivot triangle
    fulcrum = patches.Polygon([[4.6, 5.0], [5.4, 5.0], [5.0, 5.4]], closed=True, facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(fulcrum)
    pivot_circle = patches.Circle((5.0, 5.35), 0.15, facecolor=INK, edgecolor=INK, zorder=5)
    ax.add_patch(pivot_circle)

    # Balance Beam (horizontal, perfectly balanced)
    beam_y = 5.35
    ax.plot([1.5, 8.5], [beam_y, beam_y], color=INK, lw=5, solid_capstyle='round', zorder=4)

    # Left Pan Suspension and Pan
    left_x = 2.0
    pan_y = 3.0
    ax.plot([left_x, left_x - 1.2], [beam_y, pan_y + 0.4], color=INK, lw=1.5, zorder=2)
    ax.plot([left_x, left_x + 1.2], [beam_y, pan_y + 0.4], color=INK, lw=1.5, zorder=2)
    
    # Left Pan Arc/Plate
    left_pan_arc = patches.Arc((left_x, pan_y + 0.4), 2.4, 0.8, angle=0, theta1=180, theta2=360, color=INK, lw=2.5, zorder=3)
    ax.add_patch(left_pan_arc)
    left_pan_plate = patches.Rectangle((left_x - 1.2, pan_y + 0.35), 2.4, 0.08, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(left_pan_plate)

    # Right Pan Suspension and Pan
    right_x = 8.0
    ax.plot([right_x, right_x - 1.2], [beam_y, pan_y + 0.4], color=INK, lw=1.5, zorder=2)
    ax.plot([right_x, right_x + 1.2], [beam_y, pan_y + 0.4], color=INK, lw=1.5, zorder=2)

    # Right Pan Arc/Plate
    right_pan_arc = patches.Arc((right_x, pan_y + 0.4), 2.4, 0.8, angle=0, theta1=180, theta2=360, color=INK, lw=2.5, zorder=3)
    ax.add_patch(right_pan_arc)
    right_pan_plate = patches.Rectangle((right_x - 1.2, pan_y + 0.35), 2.4, 0.08, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(right_pan_plate)

    # Left side items: 24g Mg and 16g O2
    # Mg weight / block
    mg_block = patches.Rectangle((left_x - 1.0, pan_y + 0.45), 0.9, 0.9, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=4)
    ax.add_patch(mg_block)
    ax.text(left_x - 0.55, pan_y + 0.9, "24 g\nMg", color=INK, fontsize=14, ha="center", va="center", weight="bold")

    # O2 gas flask / block
    o2_block = patches.Rectangle((left_x + 0.1, pan_y + 0.45), 0.9, 0.7, facecolor=LAV, edgecolor=DEEP["lav"], lw=2, zorder=4)
    ax.add_patch(o2_block)
    ax.text(left_x + 0.55, pan_y + 0.8, "16 g\nO₂", color=INK, fontsize=14, ha="center", va="center", weight="bold")

    # Right side item: 40g MgO
    mgo_block = patches.Rectangle((right_x - 0.75, pan_y + 0.45), 1.5, 1.2, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=4)
    ax.add_patch(mgo_block)
    ax.text(right_x, pan_y + 1.05, "40 g\nMgO", color=INK, fontsize=15, ha="center", va="center", weight="bold")

    # Pointer / indicator in center
    ax.plot([5.0, 5.0], [5.35, 4.3], color=DEEP["pink"], lw=2.5, zorder=4)
    ax.plot([4.8, 5.2], [4.3, 4.3], color=INK, lw=1.5)

    # Labels below pans
    ax.text(left_x, 1.8, "Reactants: 24g Mg + 16g O2 = 40g", fontsize=14.5, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))
    
    ax.text(right_x, 1.8, "Products: 40g MgO", fontsize=14.5, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))

    # Title / Conservation of Mass header
    ax.text(5.0, 6.8, "Conservation of Mass", fontsize=18, color=INK, ha="center", va="center", weight="bold")

    save(fig, out)
