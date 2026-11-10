from style import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as mpath
from matplotlib.patches import FancyBboxPatch, Circle, PathPatch

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Branches config: 6 nodes at 60 degree increments starting from 90 (top)
    # Order: Visual, Auditory, Olfactory, Gustatory, Tactile, Kinesthetic
    nodes = [
        {"name": "Visual", "desc": "Eye", "angle": 90, "color": BLUE, "deep": DEEP["blue"]},
        {"name": "Auditory", "desc": "Ear", "angle": 30, "color": GREEN, "deep": DEEP["green"]},
        {"name": "Olfactory", "desc": "Nose", "angle": 330, "color": ORANGE, "deep": DEEP["orange"]},
        {"name": "Gustatory", "desc": "Tongue / Mouth", "angle": 270, "color": PINK, "deep": DEEP["pink"]},
        {"name": "Tactile", "desc": "Hand", "angle": 210, "color": LAV, "deep": DEEP["lav"]},
        {"name": "Kinesthetic", "desc": "Movement", "angle": 150, "color": CREAM, "deep": DEEP["orange"]},
    ]

    r_branch = 3.3
    r_center = 1.35
    r_node = 0.95

    # Draw branch lines first
    for node in nodes:
        rad = np.radians(node["angle"])
        x_end = r_branch * np.cos(rad)
        y_end = r_branch * np.sin(rad)
        ax.plot([0, x_end], [0, y_end], color=GREY, lw=3, zorder=1, linestyle="-")

    # Center circle
    center_circle = Circle((0, 0), r_center, facecolor="white", edgecolor=INK, lw=3, zorder=3)
    ax.add_patch(center_circle)
    ax.text(0, 0, "IMAGERY", ha="center", va="center", fontsize=18, fontweight="bold", color=INK, zorder=4)

    # Helper functions to draw simple flat icons inside each node circle
    def draw_eye(cx, cy, col):
        # Eye outline using two arcs
        t = np.linspace(-np.pi/3, np.pi/3, 50)
        top_x = cx + 0.5 * np.sin(t) * 1.5
        top_y = cy + 0.35 * np.cos(t) - 0.1
        bot_y = cy - 0.35 * np.cos(t) + 0.1
        ax.plot(top_x, top_y, color=col, lw=2.2, zorder=5)
        ax.plot(top_x, bot_y, color=col, lw=2.2, zorder=5)
        # Pupil / iris
        iris = Circle((cx, cy), 0.18, facecolor=col, edgecolor=col, zorder=5)
        pupil = Circle((cx, cy), 0.08, facecolor="white", zorder=6)
        ax.add_patch(iris)
        ax.add_patch(pupil)

    def draw_ear(cx, cy, col):
        # Ear outline
        t = np.linspace(-0.2, np.pi * 1.2, 50)
        r = 0.35
        x = cx + r * np.cos(t) * 0.8
        y = cy + r * np.sin(t)
        # add lobe
        x_lobe = [x[-1], cx - 0.05, cx]
        y_lobe = [y[-1], cy - 0.45, cy - 0.35]
        ax.plot(np.append(x, x_lobe), np.append(y, y_lobe), color=col, lw=2.2, zorder=5, solid_capstyle='round')
        # inner ear ridge
        t_in = np.linspace(0.2, np.pi * 0.9, 30)
        ax.plot(cx + 0.2 * np.cos(t_in) * 0.8, cy + 0.05 + 0.2 * np.sin(t_in), color=col, lw=1.8, zorder=5)

    def draw_nose(cx, cy, col):
        # Profile nose curve
        x = [cx - 0.1, cx - 0.05, cx + 0.22, cx + 0.18, cx - 0.15]
        y = [cy + 0.4, cy + 0.1, cy - 0.2, cy - 0.32, cy - 0.3]
        # Smooth with spline or path
        Path = mpath.Path
        pp = [
            (Path.MOVETO, (cx - 0.08, cy + 0.4)),
            (Path.LINETO, (cx - 0.02, cy + 0.05)),
            (Path.CURVE3, (cx + 0.28, cy - 0.2)),
            (Path.CURVE3, (cx + 0.12, cy - 0.35)),
            (Path.CURVE3, (cx - 0.15, cy - 0.35)),
            (Path.CURVE3, (cx - 0.22, cy - 0.2))
        ]
        codes, verts = zip(*pp)
        patch = PathPatch(mpath.Path(verts, codes), facecolor="none", edgecolor=col, lw=2.2, zorder=5, capstyle='round')
        ax.add_patch(patch)

    def draw_mouth(cx, cy, col):
        # Mouth outline and sticking out tongue
        # Lips line
        x_lip = np.linspace(cx - 0.35, cx + 0.35, 30)
        y_lip = cy + 0.08 - 0.2 * ((x_lip - cx) / 0.35)**2
        ax.plot(x_lip, y_lip, color=col, lw=2.2, zorder=5)
        # Lower lip line
        y_lip_bot = cy + 0.08 - 0.45 * (1 - ((x_lip - cx)/0.35)**2)
        # Tongue hanging
        t = np.linspace(0, np.pi, 30)
        tx = cx + 0.18 * np.cos(t)
        ty = cy - 0.12 - 0.22 * np.sin(t)
        ax.plot(tx, ty, color=col, lw=2, zorder=5)
        ax.plot([cx, cx], [cy - 0.12, cy - 0.26], color=col, lw=1.5, zorder=5)
        ax.plot([cx - 0.35, cx - 0.18], [cy + 0.08, cy - 0.12], color=col, lw=2, zorder=5)
        ax.plot([cx + 0.35, cx + 0.18], [cy + 0.08, cy - 0.12], color=col, lw=2, zorder=5)

    def draw_hand(cx, cy, col):
        # Stylized palm + fingers
        # Palm base
        wrist_w = 0.18
        ax.plot([cx - wrist_w, cx + wrist_w], [cy - 0.4, cy - 0.4], color=col, lw=2.2, zorder=5)
        # Fingers: thumb, index, middle, ring, pinky
        pts = [
            (cx - wrist_w, cy - 0.4),
            (cx - 0.32, cy - 0.15),
            (cx - 0.38, cy + 0.02),
            (cx - 0.25, cy + 0.08),
            (cx - 0.18, cy - 0.05),
            (cx - 0.18, cy + 0.32),
            (cx - 0.08, cy + 0.32),
            (cx - 0.08, cy - 0.02),
            (cx - 0.06, cy + 0.38),
            (cx + 0.05, cy + 0.38),
            (cx + 0.05, cy - 0.02),
            (cx + 0.07, cy + 0.33),
            (cx + 0.17, cy + 0.33),
            (cx + 0.17, cy - 0.05),
            (cx + 0.19, cy + 0.2),
            (cx + 0.28, cy + 0.2),
            (cx + 0.28, cy - 0.2),
            (cx + wrist_w, cy - 0.4),
        ]
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=col, lw=2.0, zorder=5, solid_joinstyle='round')

    def draw_runner(cx, cy, col):
        # Person running stick-figure / flat graphic
        # Head
        head = Circle((cx - 0.05, cy + 0.28), 0.11, facecolor=col, edgecolor=col, zorder=5)
        ax.add_patch(head)
        # Torso (angled forward)
        ax.plot([cx - 0.05, cx + 0.08], [cy + 0.17, cy - 0.08], color=col, lw=2.5, zorder=5)
        # Back leg
        ax.plot([cx + 0.08, cx - 0.15, cx - 0.32], [cy - 0.08, cy - 0.18, cy - 0.15], color=col, lw=2.2, zorder=5)
        # Forward leg
        ax.plot([cx + 0.08, cx + 0.25, cx + 0.12], [cy - 0.08, cy - 0.22, cy - 0.38], color=col, lw=2.2, zorder=5)
        # Back arm
        ax.plot([cx + 0.0, cx - 0.2, cx - 0.18], [cy + 0.12, cy + 0.08, cy - 0.06], color=col, lw=2.2, zorder=5)
        # Forward arm
        ax.plot([cx + 0.0, cx + 0.18, cx + 0.32], [cy + 0.12, cy + 0.18, cy + 0.08], color=col, lw=2.2, zorder=5)

    icon_drawers = [draw_eye, draw_ear, draw_nose, draw_mouth, draw_hand, draw_runner]

    for node, drawer in zip(nodes, icon_drawers):
        rad = np.radians(node["angle"])
        nx = r_branch * np.cos(rad)
        ny = r_branch * np.sin(rad)

        # Draw outer circle node
        circle = Circle((nx, ny), r_node, facecolor=node["color"], edgecolor=node["deep"], lw=2.5, zorder=3)
        ax.add_patch(circle)

        # Draw icon
        drawer(nx, ny, INK)

        # Place label outside circle
        label_dist = r_branch + r_node + 0.45
        lx = label_dist * np.cos(rad)
        ly = label_dist * np.sin(rad)

        ha = "center"
        if np.cos(rad) > 0.3:
            ha = "left"
        elif np.cos(rad) < -0.3:
            ha = "right"

        va = "center"
        if np.sin(rad) > 0.8:
            va = "bottom"
        elif np.sin(rad) < -0.8:
            va = "top"

        full_label = f"{node['name']}\n({node['desc']})"
        ax.text(lx, ly, full_label, ha=ha, va=va, fontsize=15, fontweight="bold", color=INK,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85), zorder=6)

    # Main Title
    ax.text(0, 5.1, "Types of Imagery in Literature", ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    save(fig, out)
