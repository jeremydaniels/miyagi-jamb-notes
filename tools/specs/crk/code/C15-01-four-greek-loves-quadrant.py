from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

def draw_heart(ax, cx, cy, size, color=DEEP["pink"], fill_color=PINK):
    t = np.linspace(0, 2 * np.pi, 200)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    x = cx + (x / 18.0) * size
    y = cy + (y / 18.0) * size
    ax.fill(x, y, color=fill_color, zorder=2)
    ax.plot(x, y, color=color, lw=2.5, zorder=3)

def draw(out):
    fig = canvas(11, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    # Main Title
    ax.text(5.5, 9.9, "FOUR TYPES OF LOVE IN ANCIENT GREEK", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK)

    # Quadrant Boxes (Rounded background cards)
    # Top-Left: Agape
    # Top-Right: Phileo
    # Bottom-Left: Eros
    # Bottom-Right: Storge
    box_w, box_h = 4.8, 4.2
    tl_box = FancyBboxPatch((0.5, 5.2), box_w, box_h, boxstyle="round,pad=0.1,rounding_size=0.3",
                            fc="#FAF9F6", ec=GREY, lw=1.5, zorder=1)
    tr_box = FancyBboxPatch((5.7, 5.2), box_w, box_h, boxstyle="round,pad=0.1,rounding_size=0.3",
                            fc="#FAF9F6", ec=GREY, lw=1.5, zorder=1)
    bl_box = FancyBboxPatch((0.5, 0.6), box_w, box_h, boxstyle="round,pad=0.1,rounding_size=0.3",
                            fc="#FAF9F6", ec=GREY, lw=1.5, zorder=1)
    br_box = FancyBboxPatch((5.7, 0.6), box_w, box_h, boxstyle="round,pad=0.1,rounding_size=0.3",
                            fc="#FAF9F6", ec=GREY, lw=1.5, zorder=1)
    
    for b in [tl_box, tr_box, bl_box, br_box]:
        ax.add_patch(b)

    # ----------------- 1. TOP-LEFT: AGAPE -----------------
    ax.text(2.9, 9.0, "AGAPE (Unconditional/Divine)", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK)

    # Heart at center
    draw_heart(ax, 2.9, 7.3, 0.9, color=DEEP["pink"], fill_color=PINK)
    
    # Cross inside heart
    ax.plot([2.9, 2.9], [6.95, 7.7], color=DEEP["pink"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([2.65, 3.15], [7.45, 7.45], color=DEEP["pink"], lw=3, solid_capstyle="round", zorder=4)

    # Hands cupping / holding the heart from below
    # Left hand/arm curve
    ax.plot([1.9, 2.4, 2.8], [6.0, 6.1, 6.4], color=DEEP["orange"], lw=3.5, solid_capstyle="round", zorder=4)
    # Right hand/arm curve
    ax.plot([3.9, 3.4, 3.0], [6.0, 6.1, 6.4], color=DEEP["orange"], lw=3.5, solid_capstyle="round", zorder=4)
    # Gentle upward fingers
    ax.plot([2.55, 2.65], [6.25, 6.55], color=DEEP["orange"], lw=2.5, solid_capstyle="round", zorder=4)
    ax.plot([3.25, 3.15], [6.25, 6.55], color=DEEP["orange"], lw=2.5, solid_capstyle="round", zorder=4)

    # Rays / halo of divine love
    for ang in np.linspace(np.pi/4, 3*np.pi/4, 5):
        r1, r2 = 1.15, 1.45
        ax.plot([2.9 + r1*np.cos(ang), 2.9 + r2*np.cos(ang)],
                [7.3 + r1*np.sin(ang), 7.3 + r2*np.sin(ang)],
                color=DEEP["orange"], lw=2, zorder=3)

    # ----------------- 2. TOP-RIGHT: PHILEO -----------------
    ax.text(8.1, 9.0, "PHILEO (Brotherly/Friendship)", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK)

    # Two friends side-by-side with arms around shoulders
    # Friend 1 (Left): head, body
    ax.add_patch(Circle((7.6, 7.6), 0.32, fc=BLUE, ec=DEEP["blue"], lw=2.5, zorder=4))
    ax.plot([7.6, 7.6], [7.28, 6.1], color=DEEP["blue"], lw=3.5, solid_capstyle="round", zorder=4)
    # Friend 2 (Right): head, body
    ax.add_patch(Circle((8.6, 7.6), 0.32, fc=GREEN, ec=DEEP["green"], lw=2.5, zorder=4))
    ax.plot([8.6, 8.6], [7.28, 6.1], color=DEEP["green"], lw=3.5, solid_capstyle="round", zorder=4)

    # Outer arms resting downwards
    ax.plot([7.6, 7.15, 7.2], [7.0, 6.5, 5.9], color=DEEP["blue"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([8.6, 9.05, 9.0], [7.0, 6.5, 5.9], color=DEEP["green"], lw=3, solid_capstyle="round", zorder=4)

    # Arms around each other's shoulders (overlapping)
    ax.plot([7.6, 8.1, 8.6], [6.9, 7.05, 6.9], color=DEEP["blue"], lw=3, solid_capstyle="round", zorder=5)
    ax.plot([8.6, 8.1, 7.6], [6.75, 6.9, 6.75], color=DEEP["green"], lw=3, solid_capstyle="round", zorder=4)

    # Legs
    ax.plot([7.6, 7.4], [6.1, 5.4], color=DEEP["blue"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([7.6, 7.8], [6.1, 5.4], color=DEEP["blue"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([8.6, 8.4], [6.1, 5.4], color=DEEP["green"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([8.6, 8.8], [6.1, 5.4], color=DEEP["green"], lw=3, solid_capstyle="round", zorder=4)

    # ----------------- 3. BOTTOM-LEFT: EROS -----------------
    ax.text(2.9, 4.4, "EROS (Romantic/Spousal)", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK)

    # Couple holding hands
    # Partner 1 (Left)
    ax.add_patch(Circle((2.3, 3.1), 0.32, fc=LAV, ec=DEEP["lav"], lw=2.5, zorder=4))
    ax.plot([2.3, 2.3], [2.78, 1.6], color=DEEP["lav"], lw=3.5, solid_capstyle="round", zorder=4)
    # Legs Partner 1
    ax.plot([2.3, 2.1], [1.6, 0.9], color=DEEP["lav"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([2.3, 2.45], [1.6, 0.9], color=DEEP["lav"], lw=3, solid_capstyle="round", zorder=4)
    # Left outer arm
    ax.plot([2.3, 1.9, 2.0], [2.5, 2.1, 1.5], color=DEEP["lav"], lw=3, solid_capstyle="round", zorder=4)

    # Partner 2 (Right)
    ax.add_patch(Circle((3.5, 3.1), 0.32, fc=PINK, ec=DEEP["pink"], lw=2.5, zorder=4))
    # Dress shape / torso for Partner 2
    ax.plot([3.5, 3.5], [2.78, 1.6], color=DEEP["pink"], lw=3.5, solid_capstyle="round", zorder=4)
    # Legs Partner 2
    ax.plot([3.5, 3.35], [1.6, 0.9], color=DEEP["pink"], lw=3, solid_capstyle="round", zorder=4)
    ax.plot([3.5, 3.7], [1.6, 0.9], color=DEEP["pink"], lw=3, solid_capstyle="round", zorder=4)
    # Right outer arm
    ax.plot([3.5, 3.9, 3.8], [2.5, 2.1, 1.5], color=DEEP["pink"], lw=3, solid_capstyle="round", zorder=4)

    # Holding hands in the middle
    ax.plot([2.3, 2.9, 3.5], [2.5, 2.05, 2.5], color=INK, lw=2.5, solid_capstyle="round", zorder=5)
    ax.add_patch(Circle((2.9, 2.05), 0.08, color=INK, zorder=6))

    # Small romantic heart between them floating above hands
    draw_heart(ax, 2.9, 2.9, 0.45, color=DEEP["pink"], fill_color=PINK)

    # ----------------- 4. BOTTOM-RIGHT: STORGE -----------------
    ax.text(8.1, 4.4, "STORGE (Family/Affection)", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK)

    # Mother holding a child
    # Mother head
    ax.add_patch(Circle((7.8, 3.1), 0.34, fc=CREAM, ec=DEEP["orange"], lw=2.5, zorder=4))
    # Mother torso
    ax.plot([7.8, 7.8], [2.76, 1.5], color=DEEP["orange"], lw=4, solid_capstyle="round", zorder=4)
    # Mother legs / skirt base
    ax.plot([7.8, 7.5], [1.5, 0.9], color=DEEP["orange"], lw=3.5, solid_capstyle="round", zorder=4)
    ax.plot([7.8, 8.0], [1.5, 0.9], color=DEEP["orange"], lw=3.5, solid_capstyle="round", zorder=4)

    # Child head (smaller, resting close to mother's chest)
    ax.add_patch(Circle((8.4, 2.5), 0.22, fc=CREAM, ec=DEEP["orange"], lw=2.2, zorder=5))
    # Child body
    ax.plot([8.4, 8.3], [2.28, 1.7], color=DEEP["orange"], lw=3.2, solid_capstyle="round", zorder=5)

    # Mother's arms embracing child
    # Upper arm wrapping over and under child
    ax.plot([7.8, 8.2, 8.55, 8.3], [2.5, 2.2, 1.9, 1.7], color=DEEP["orange"], lw=3, solid_capstyle="round", zorder=6)
    # Supporting arm underneath
    ax.plot([7.8, 8.1, 8.4], [2.2, 1.6, 1.65], color=DEEP["orange"], lw=3, solid_capstyle="round", zorder=6)

    # Little tender heart above the mother and child
    draw_heart(ax, 8.35, 3.25, 0.35, color=DEEP["orange"], fill_color=CREAM)

    save(fig, out)
