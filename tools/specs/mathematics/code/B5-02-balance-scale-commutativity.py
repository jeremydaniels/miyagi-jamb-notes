from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8.5, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 5)
    ax.axis('off')

    # Base stand (trapezoid body)
    base_poly = plt.Polygon([[-1.2, -1.0], [1.2, -1.0], [0.25, 2.5], [-0.25, 2.5]], 
                            facecolor=CREAM, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(base_poly)

    # Base foot
    foot = patches.FancyBboxPatch((-1.8, -1.25), 3.6, 0.35, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(foot)

    # Central pivot
    pivot = plt.Circle((0, 2.5), 0.22, facecolor=DEEP["orange"], edgecolor=INK, lw=2, zorder=6)
    ax.add_patch(pivot)

    # Balanced horizontal beam
    beam_y = 2.5
    ax.plot([-3.5, 3.5], [beam_y, beam_y], color=INK, lw=4, solid_capstyle='round', zorder=5)

    # Left and Right pan suspension points
    lx, rx = -3.2, 3.2
    pan_w = 2.4
    pan_y = 0.4
    pan_depth = 0.3

    # Suspension strings
    # Left strings
    ax.plot([lx, lx - pan_w/2], [beam_y, pan_y], color=INK, lw=1.5, zorder=2)
    ax.plot([lx, lx + pan_w/2], [beam_y, pan_y], color=INK, lw=1.5, zorder=2)
    # Right strings
    ax.plot([rx, rx - pan_w/2], [beam_y, pan_y], color=INK, lw=1.5, zorder=2)
    ax.plot([rx, rx + pan_w/2], [beam_y, pan_y], color=INK, lw=1.5, zorder=2)

    # Scale pan platforms: sleek flat tray with rounded rim
    for cx in (lx, rx):
        tray = patches.Polygon([
            [cx - pan_w/2, pan_y],
            [cx + pan_w/2, pan_y],
            [cx + pan_w/2 - 0.2, pan_y - pan_depth],
            [cx - pan_w/2 + 0.2, pan_y - pan_depth]
        ], closed=True, facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
        ax.add_patch(tray)

    # Blocks dimensions
    bw, bh = 1.3, 0.75

    # Left Stack: block 'a' stacked with block 'b'
    # Block 'b' at bottom
    rect_lb = patches.Rectangle((lx - bw/2, pan_y), bw, bh,
                                facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=4)
    ax.add_patch(rect_lb)
    ax.text(lx, pan_y + bh/2, 'b', ha='center', va='center', fontsize=18, fontweight='bold', color=INK, zorder=5)

    # Block 'a' on top
    rect_la = patches.Rectangle((lx - bw/2, pan_y + bh), bw, bh,
                                facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=4)
    ax.add_patch(rect_la)
    ax.text(lx, pan_y + 1.5 * bh, 'a', ha='center', va='center', fontsize=18, fontweight='bold', color=INK, zorder=5)

    # Right Stack: reversed order (block 'a' at bottom, block 'b' on top)
    # Block 'a' at bottom
    rect_ra = patches.Rectangle((rx - bw/2, pan_y), bw, bh,
                                facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=4)
    ax.add_patch(rect_ra)
    ax.text(rx, pan_y + bh/2, 'a', ha='center', va='center', fontsize=18, fontweight='bold', color=INK, zorder=5)

    # Block 'b' on top
    rect_rb = patches.Rectangle((rx - bw/2, pan_y + bh), bw, bh,
                                facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=4)
    ax.add_patch(rect_rb)
    ax.text(rx, pan_y + 1.5 * bh, 'b', ha='center', va='center', fontsize=18, fontweight='bold', color=INK, zorder=5)

    # Title / Label
    ax.text(0, 4.3, "Commutative Property", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Equation below
    eq_text = r"$a \cdot b = b \cdot a$"
    ax.text(0, -2.1, eq_text, ha='center', va='center', fontsize=22, color=INK,
            bbox=dict(boxstyle="round,pad=0.4", facecolor=CREAM, edgecolor=GREY, lw=1.5))

    save(fig, out)
