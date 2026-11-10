import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon, Wedge
import matplotlib.path as mpath
from style import *

def draw(out):
    fig = canvas(9, 6.8)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(0, 2.45, "Composition of a Good Loam Soil (by Volume)", 
            fontsize=15, fontweight="bold", ha="center", va="center", color=INK)

    # Pie chart setup (4 slices):
    # Mineral particles: 45% (sandy brown) -> 90 to 252 deg
    # Organic matter: 5% (dark brown) -> 252 to 270 deg
    # Water: 25% (soft blue) -> 270 to 360 deg
    # Air: 25% (very pale grey-blue) -> 0 to 90 deg

    c_mineral = "#D2B48C"        # sandy brown
    c_organic = "#5C4033"        # dark brown
    c_water = BLUE               # soft blue
    c_air = "#E2EAF0"            # very pale grey-blue

    colors = [c_mineral, c_organic, c_water, c_air]
    r = 1.6
    angles = [90, 252, 270, 360, 450]

    for i in range(4):
        wedge = Wedge((0, 0), r, angles[i], angles[i+1], facecolor=colors[i], edgecolor="white", lw=2.5)
        ax.add_patch(wedge)

    # Soil solids vs Pore space indicators
    ax.text(-1.9, -1.2, "50% Soil Solids", fontsize=11, fontstyle="italic", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8))
    ax.text(1.9, -0.1, "50% Pore Space", fontsize=11, fontstyle="italic", color=INK, ha="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8))

    # Icon Drawing Helpers
    def draw_grains(cx, cy):
        # Cluster of distinct tiny rock grains
        offsets = [
            (-0.16, 0.08), (-0.03, 0.12), (0.12, 0.07),
            (-0.12, -0.06), (0.04, -0.02), (0.15, -0.08),
            (-0.02, -0.12)
        ]
        radii = [(0.065, 0.05), (0.075, 0.06), (0.06, 0.05),
                 (0.07, 0.055), (0.08, 0.065), (0.065, 0.05),
                 (0.06, 0.045)]
        rots = [20, 60, -30, 45, -15, 75, -40]
        cols = ["#B08D57", "#C4A47C", "#9C7844", "#CBB08A", "#8F6B38", "#A48050", "#BDA073"]
        for (dx, dy), (rx, ry), ag, col in zip(offsets, radii, rots, cols):
            ax.add_patch(Ellipse((cx + dx, cy + dy), rx * 2, ry * 2, angle=ag,
                                 facecolor=col, edgecolor=INK, lw=1.1, zorder=5))

    def draw_leaf(cx, cy):
        # Simple decaying leaf
        pts = np.array([
            [-0.18, -0.1],
            [-0.08, 0.08],
            [0.16, 0.14],
            [0.2, 0.04],
            [0.08, -0.12],
            [-0.1, -0.14]
        ])
        ax.add_patch(Polygon(pts + np.array([cx, cy]), closed=True,
                             facecolor="#4A3525", edgecolor=INK, lw=1.1, zorder=5))
        ax.plot([cx - 0.14, cx + 0.15], [cy - 0.1, cy + 0.1], color="#2E1F14", lw=1.2, zorder=6)
        ax.add_patch(Circle((cx - 0.02, cy - 0.03), 0.028, facecolor="white", edgecolor=INK, lw=0.8, zorder=6))

    def draw_drop(cx, cy):
        # Water drop
        path_data = [
            (mpath.Path.MOVETO, [0, 0.18]),
            (mpath.Path.CURVE4, [0.08, 0.08]),
            (mpath.Path.CURVE4, [0.15, -0.02]),
            (mpath.Path.CURVE4, [0.15, -0.10]),
            (mpath.Path.CURVE4, [0.15, -0.20]),
            (mpath.Path.CURVE4, [-0.15, -0.20]),
            (mpath.Path.CURVE4, [-0.15, -0.10]),
            (mpath.Path.CURVE4, [-0.15, -0.02]),
            (mpath.Path.CURVE4, [-0.08, 0.08]),
            (mpath.Path.CURVE4, [0, 0.18]),
            (mpath.Path.CLOSEPOLY, [0, 0.18])
        ]
        codes, verts = zip(*path_data)
        verts = [(vx + cx, vy + cy + 0.03) for vx, vy in verts]
        path = mpath.Path(verts, codes)
        ax.add_patch(PathPatch(path, facecolor=DEEP["blue"], edgecolor=INK, lw=1.1, zorder=5))
        ax.add_patch(Ellipse((cx - 0.05, cy - 0.03), 0.04, 0.07, angle=30,
                             facecolor="white", edgecolor="none", alpha=0.7, zorder=6))

    def draw_bubble(cx, cy):
        # Bubble for air
        ax.add_patch(Circle((cx, cy), 0.14, facecolor="#CDE0EB", edgecolor=DEEP["blue"], lw=1.2, zorder=5))
        ax.add_patch(Ellipse((cx - 0.05, cy + 0.05), 0.04, 0.06, angle=-30,
                             facecolor="white", edgecolor="none", zorder=6))
        ax.add_patch(Circle((cx + 0.13, cy + 0.12), 0.055, facecolor="#CDE0EB", edgecolor=DEEP["blue"], lw=1, zorder=5))

    # Slice annotations and icons (placed cleanly beside slices and labels)

    # 1. Mineral particles 45% (mid ~171 deg)
    t_m = (-2.1, 0.35)
    ax.annotate("", xy=(-1.55, 0.25), xytext=(t_m[0] + 0.1, t_m[1]),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    ax.text(t_m[0] - 0.35, t_m[1], "Mineral particles 45%", 
            fontsize=12, fontweight="bold", color=INK, ha="right", va="center")
    draw_grains(t_m[0] - 0.1, t_m[1])

    # 2. Organic matter 5% (mid 261 deg)
    t_om = (-1.0, -2.0)
    ax.annotate("", xy=(-0.25, -1.58), xytext=(t_om[0] + 0.2, t_om[1] + 0.2),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    ax.text(t_om[0] - 0.35, t_om[1], "Organic matter 5%",
            fontsize=12, fontweight="bold", color=INK, ha="right", va="center")
    draw_leaf(t_om[0] - 0.1, t_om[1])

    # 3. Water 25% (mid 315 deg)
    t_w = (2.2, -1.15)
    ax.annotate("", xy=(1.15, -1.15), xytext=(t_w[0] - 0.1, t_w[1]),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    draw_drop(t_w[0] + 0.1, t_w[1])
    ax.text(t_w[0] + 0.35, t_w[1], "Water 25%", 
            fontsize=12, fontweight="bold", color=INK, ha="left", va="center")

    # 4. Air 25% (mid 45 deg)
    t_a = (2.2, 1.15)
    ax.annotate("", xy=(1.15, 1.15), xytext=(t_a[0] - 0.1, t_a[1]),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.2))
    draw_bubble(t_a[0] + 0.1, t_a[1])
    ax.text(t_a[0] + 0.35, t_a[1], "Air 25%", 
            fontsize=12, fontweight="bold", color=INK, ha="left", va="center")

    ax.set_xlim(-4.3, 4.3)
    ax.set_ylim(-2.5, 2.7)

    save(fig, out)
