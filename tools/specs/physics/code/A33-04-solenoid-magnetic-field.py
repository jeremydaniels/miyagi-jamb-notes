from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Polygon

def draw(out):
    fig = canvas(14, 9.5)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    ax.set_xlim(-7.0, 7.0)
    ax.set_ylim(-5.5, 4.2)
    ax.axis("off")

    # Title
    ax.text(0, 3.8, "Magnetic Field of a Current-Carrying Solenoid", 
            fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    field_color = DEEP["blue"]

    # 1. Centre field lines (through solenoid, S -> N, pointing left)
    for y_val in [-0.4, 0.0, 0.4]:
        ax.plot([-5.8, 5.8], [y_val, y_val], color=field_color, lw=1.8, linestyle="--", alpha=0.85, zorder=1)
        ax.annotate("", xy=(-1.2, y_val), xytext=(-0.5, y_val),
                    arrowprops=dict(arrowstyle="->", color=field_color, lw=2.0))
        ax.annotate("", xy=(-5.0, y_val), xytext=(-4.3, y_val),
                    arrowprops=dict(arrowstyle="->", color=field_color, lw=2.0))
        ax.annotate("", xy=(3.6, y_val), xytext=(4.3, y_val),
                    arrowprops=dict(arrowstyle="->", color=field_color, lw=2.0))

    # 2. Outer curved field lines (N -> S, curving around outside)
    # Top loops (full curves)
    for scale_x, peak_y in [(4.8, 1.8), (5.5, 2.5), (6.2, 3.2)]:
        t = np.linspace(0, np.pi, 100)
        xs = -scale_x * np.cos(t)
        ys = 0.9 + (peak_y - 0.9) * np.sin(t)
        ax.plot(xs, ys, color=field_color, lw=1.8, alpha=0.85, zorder=1)
        # Arrow pointing right outside (from N to S)
        ax.annotate("", xy=(0.6, peak_y), xytext=(-0.6, peak_y),
                    arrowprops=dict(arrowstyle="->", color=field_color, lw=2.0))

    # Bottom loops: scaled so they stay well clear of the inset box (inset top is y = -2.1)
    # Solenoid bottom is y = -0.9, keep loops above y = -1.95
    for scale_x, valley_y in [(4.6, -1.45), (5.3, -1.85)]:
        t = np.linspace(0, np.pi, 100)
        xs = -scale_x * np.cos(t)
        ys = -0.9 + (valley_y - (-0.9)) * np.sin(t)
        ax.plot(xs, ys, color=field_color, lw=1.8, alpha=0.85, zorder=1)
        # Arrow pointing right outside
        ax.annotate("", xy=(0.6, valley_y), xytext=(-0.6, valley_y),
                    arrowprops=dict(arrowstyle="->", color=field_color, lw=2.0))

    # 3. Solenoid core interior shading
    ax.fill_between([-3.2, 3.2], -0.85, 0.85, color=CREAM, alpha=0.45, zorder=2)

    # 4. Solenoid Coils (Helical winding)
    turns_total = 8.5
    coil_color = DEEP["orange"]
    coil_lw = 4.0
    t_helix = np.linspace(0, turns_total * 2 * np.pi, 1200)
    x_helix = -3.2 + (6.4 / (turns_total * 2 * np.pi)) * t_helix
    y_helix = 0.9 * np.sin(t_helix)
    z_depth = np.cos(t_helix)  # z > 0 is front face, z <= 0 is rear

    # Back arcs
    for i in range(len(t_helix) - 1):
        if z_depth[i] <= 0:
            ax.plot(x_helix[i:i+2], y_helix[i:i+2], color=GREY, lw=2.5, alpha=0.55, zorder=3)

    # Front arcs
    for i in range(len(t_helix) - 1):
        if z_depth[i] > 0:
            ax.plot(x_helix[i:i+2], y_helix[i:i+2], color=coil_color, lw=coil_lw, zorder=4)

    # Current flow arrows on front coil turns (flowing downward at front)
    for turn_idx in range(1, 8):
        t_mid = (turn_idx + 0.25) * 2 * np.pi
        xm = -3.2 + (6.4 / (turns_total * 2 * np.pi)) * t_mid
        ax.annotate("", xy=(xm + 0.08, -0.2), xytext=(xm - 0.08, 0.2),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=2.5), zorder=5)

    # 5. External leads
    # Left entering: current I entering at top-left
    ax.plot([-4.2, -3.2], [1.3, 0.9], color=coil_color, lw=coil_lw, zorder=4)
    ax.annotate("", xy=(-3.5, 1.02), xytext=(-4.1, 1.26),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5), zorder=5)
    ax.text(-4.4, 1.4, "Current 'I'\n(entering)", fontsize=15, color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Right exiting: current I exiting at bottom-right
    ax.plot([3.2, 4.2], [-0.9, -1.3], color=coil_color, lw=coil_lw, zorder=4)
    ax.annotate("", xy=(4.0, -1.22), xytext=(3.4, -0.98),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5), zorder=5)
    ax.text(4.4, -1.4, "Current 'I'\n(exiting)", fontsize=15, color=INK, ha="left", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # 6. Pole N and Pole S labels
    ax.text(-3.6, 0.0, "N", fontsize=28, fontweight="bold", color=DEEP["pink"], ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="circle,pad=0.25", lw=2), zorder=6)
    ax.text(-4.8, -0.85, "North Pole (N)\n(anti-clockwise current)", fontsize=14, color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

    ax.text(3.6, 0.0, "S", fontsize=28, fontweight="bold", color=DEEP["blue"], ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="circle,pad=0.25", lw=2), zorder=6)
    ax.text(4.8, 0.85, "South Pole (S)\n(clockwise current)", fontsize=14, color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

    # 7. Inset: Right-hand grip rule
    # Generous box at bottom center with clear margins
    box_w, box_h = 7.6, 2.9
    box_x0, box_y0 = -3.8, -5.2
    inset_bg = Rectangle((box_x0, box_y0), box_w, box_h, fc=CREAM, ec=GREY, lw=1.5, zorder=7)
    ax.add_patch(inset_bg)

    ax.text(0.0, -2.45, "Right-hand grip rule", fontsize=16, fontweight="bold", ha="center", va="center", color=INK, zorder=8)

    # Core cylinder representing the solenoid held inside hand
    core_rect = Rectangle((-1.8, -3.95), 4.2, 0.7, fc="white", ec=GREY, lw=1.5, zorder=8)
    ax.add_patch(core_rect)
    ax.text(2.1, -3.6, "coil core", fontsize=14, color=GREY, ha="left", va="center", zorder=8)

    # Realistic anatomical drawing of right hand gripping the cylinder
    # Palm & wrist entering from right
    wrist_pts = np.array([[1.8, -3.3], [1.8, -4.1], [1.0, -4.0], [0.8, -3.4]])
    wrist_patch = Polygon(wrist_pts, fc=PINK, ec=INK, lw=1.8, zorder=9)
    ax.add_patch(wrist_patch)

    # 4 curled fingers wrapping over cylinder from top to bottom
    finger_xs = [0.65, 0.3, -0.05, -0.4]
    for fx in finger_xs:
        # Finger arched over the front
        f_pts = np.array([
            [fx + 0.12, -3.25],
            [fx + 0.12, -3.95],
            [fx - 0.12, -3.95],
            [fx - 0.12, -3.25]
        ])
        finger_patch = Polygon(f_pts, fc=PINK, ec=INK, lw=1.8, zorder=10)
        ax.add_patch(finger_patch)

    # Current arrows showing downward curl along fingers
    for fx in [0.48, -0.22]:
        ax.annotate("", xy=(fx, -3.85), xytext=(fx, -3.35),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5), zorder=11)

    # Extended thumb pointing left towards 'N'
    thumb_pts = np.array([
        [-0.45, -3.45],
        [-1.3, -3.45],
        [-1.5, -3.6],
        [-1.3, -3.75],
        [-0.45, -3.75]
    ])
    thumb_patch = Polygon(thumb_pts, fc=PINK, ec=INK, lw=1.8, zorder=10)
    ax.add_patch(thumb_patch)

    # Bold magnetic field arrow from thumb pointing left to N
    ax.annotate("", xy=(-2.5, -3.6), xytext=(-1.5, -3.6),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3.2), zorder=11)

    # Annotations inside inset with dedicated comfortable spacing
    ax.text(-2.5, -4.3, "Thumb points left\ntowards 'N'", fontsize=14, fontweight="bold",
            color=DEEP["pink"], ha="center", va="top", zorder=12,
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.2", lw=1.2))

    ax.text(0.8, -4.5, "Fingers curl in\ndirection of current 'I'", fontsize=14, fontweight="bold",
            color=INK, ha="center", va="top", zorder=12,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=1.2))

    save(fig, out)
