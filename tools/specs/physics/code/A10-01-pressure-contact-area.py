from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    # Height slightly enlarged to 7.6 to give comfortable clearance
    fig = canvas(12, 7.6)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.6)
    ax.axis('off')

    # Draw tabletop / ground line
    ground_y = 1.6
    ax.plot([0.8, 11.2], [ground_y, ground_y], color=GREY, lw=2, zorder=1)

    # Oblique projection vector
    theta = np.radians(35)
    scale = 0.55
    def proj(x, y, z):
        return x + z * scale * np.cos(theta), y + z * scale * np.sin(theta)

    def draw_cuboid(ox, oy, w, h, d, face_col, edge_col):
        v000 = proj(ox, oy, 0)
        v100 = proj(ox + w, oy, 0)
        v110 = proj(ox + w, oy + h, 0)
        v010 = proj(ox, oy + h, 0)

        v001 = proj(ox, oy, d)
        v101 = proj(ox + w, oy, d)
        v111 = proj(ox + w, oy + h, d)
        v011 = proj(ox, oy + h, d)

        # Front face
        front = Polygon([v000, v100, v110, v010], closed=True,
                        facecolor=face_col, edgecolor=edge_col, lw=2.2, zorder=4)
        # Top face
        top = Polygon([v010, v110, v111, v011], closed=True,
                      facecolor=CREAM, edgecolor=edge_col, lw=2.2, zorder=3)
        # Right face
        side = Polygon([v100, v101, v111, v110], closed=True,
                       facecolor=LAV, edgecolor=edge_col, lw=2.2, zorder=3)

        ax.add_patch(top)
        ax.add_patch(side)
        ax.add_patch(front)

        # Base contact area (dashed lines showing contact footprint)
        base = Polygon([v000, v100, v101, v001], closed=True,
                       facecolor='none', edgecolor=edge_col, lw=1.5, ls='--', zorder=2)
        ax.add_patch(base)

    # Block 1: resting on largest flat face
    # Dimensions: 4.0 (width) x 1.0 (height) x 2.2 (depth)
    b1_x = 1.3
    b1_w = 4.0
    b1_h = 1.0
    b1_d = 2.2
    draw_cuboid(b1_x, ground_y, b1_w, b1_h, b1_d, BLUE, DEEP["blue"])

    # Block 2: standing upright on smallest face
    # Dimensions: 1.0 (width) x 3.6 (height) x 2.2 (depth)
    b2_x = 8.4
    b2_w = 1.0
    b2_h = 3.6
    b2_d = 2.2
    draw_cuboid(b2_x, ground_y, b2_w, b2_h, b2_d, ORANGE, DEEP["orange"])

    # Downward force arrows (Weight W)
    # For Block 1
    c1_x = b1_x + b1_w / 2 + (b1_d / 2) * scale * np.cos(theta)
    top1_y = ground_y + b1_h + (b1_d / 2) * scale * np.sin(theta)
    ax.annotate("", xy=(c1_x, top1_y - 0.05), xytext=(c1_x, top1_y + 0.85),
                arrowprops=dict(arrowstyle="->", lw=2.4, color=DEEP["blue"]))
    ax.text(c1_x + 0.25, top1_y + 0.45, "Weight ($W$)", fontsize=14, color=INK, va="center")

    # For Block 2: upright top surface is at ground_y + 3.6 + depth_offset ≈ 5.55
    c2_x = b2_x + b2_w / 2 + (b2_d / 2) * scale * np.cos(theta)
    top2_y = ground_y + b2_h + (b2_d / 2) * scale * np.sin(theta)
    arrow_top_y = min(top2_y + 0.85, 6.45)
    ax.annotate("", xy=(c2_x, top2_y - 0.05), xytext=(c2_x, arrow_top_y),
                arrowprops=dict(arrowstyle="->", lw=2.4, color=DEEP["orange"]))
    ax.text(c2_x + 0.25, (top2_y + arrow_top_y) / 2, "Weight ($W$)",
            fontsize=14, color=INK, va="center")

    # Labels under each block
    label_y = 0.7
    ax.text(3.3, label_y, "Minimum pressure, largest area",
            fontsize=14.5, color=INK, ha="center", weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    ax.text(9.2, label_y, "Maximum pressure, smallest area",
            fontsize=14.5, color=INK, ha="center", weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Title positioned clearly above all block elements
    ax.text(6.0, 7.15, "Effect of Surface Area on Pressure ($P = \\frac{F}{A}$)",
            fontsize=17, color=INK, ha="center", weight="bold")

    save(fig, out)
