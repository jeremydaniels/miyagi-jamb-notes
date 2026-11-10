from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(6, 6.5, "Parallel Lines Cut by a Transversal", fontsize=18, weight="bold", ha="center", color=INK)

    # Parallel horizontal lines
    y1 = 4.3  # top line
    y2 = 2.1  # bottom line
    x_start, x_end = 0.8, 6.8

    # Transversal line: y = m*x + c
    # Let intersection 1 be at (3.8, 4.3) and intersection 2 be at (2.4, 2.1)
    p1 = np.array([3.8, y1])
    p2 = np.array([2.4, y2])
    
    # Direction vector of transversal
    v = p1 - p2
    angle_trans_deg = np.degrees(np.arctan2(v[1], v[0])) # ~ 57.5 degrees

    # Draw parallel lines
    ax.plot([x_start, x_end], [y1, y1], color=INK, lw=2.5, zorder=2)
    ax.plot([x_start, x_end], [y2, y2], color=INK, lw=2.5, zorder=2)

    # Draw arrows on parallel lines to indicate they are parallel
    arrow_kw = dict(length_includes_head=True, head_width=0.18, head_length=0.25, color=INK)
    ax.arrow(5.5, y1, 0.05, 0, **arrow_kw)
    ax.arrow(5.5, y2, 0.05, 0, **arrow_kw)

    # Line labels
    ax.text(x_end + 0.15, y1, "$L_1$", fontsize=15, va="center", color=INK, weight="bold")
    ax.text(x_end + 0.15, y2, "$L_2$", fontsize=15, va="center", color=INK, weight="bold")

    # Draw transversal extending past intersections
    t_start = p2 - 0.55 * v
    t_end = p1 + 0.6 * v
    ax.plot([t_start[0], t_end[0]], [t_start[1], t_end[1]], color=INK, lw=2.5, zorder=2)
    ax.text(t_end[0] + 0.1, t_end[1] + 0.1, "$T$", fontsize=15, va="bottom", color=INK, weight="bold")

    # Color fills for angles
    # Group A: 1, 4, 5, 8 -> BLUE (obtuse)
    # Group B: 2, 3, 6, 7 -> ORANGE (acute)
    col_A = BLUE
    col_B = ORANGE
    r = 0.7  # wedge radius

    # Wedges at top intersection p1:
    # Angles relative to positive x-axis:
    # 0 to theta: Acute (Angle 2) -> Group B
    # theta to 180: Obtuse (Angle 1) -> Group A
    # 180 to 180+theta: Acute (Angle 3) -> Group B
    # 180+theta to 360: Obtuse (Angle 4) -> Group A
    theta = angle_trans_deg

    wedge_defs = [
        # Center, theta1, theta2, color, label, label_dist, label_angle_mid
        # Intersection 1 (top, p1)
        (p1, theta, 180, col_A, "1", 0.42, (theta + 180) / 2),
        (p1, 0, theta, col_B, "2", 0.42, theta / 2),
        (p1, 180, 180 + theta, col_B, "3", 0.42, 180 + theta / 2),
        (p1, 180 + theta, 360, col_A, "4", 0.42, (180 + theta + 360) / 2),
        # Intersection 2 (bottom, p2)
        (p2, theta, 180, col_A, "5", 0.42, (theta + 180) / 2),
        (p2, 0, theta, col_B, "6", 0.42, theta / 2),
        (p2, 180, 180 + theta, col_B, "7", 0.42, 180 + theta / 2),
        (p2, 180 + theta, 360, col_A, "8", 0.42, (180 + theta + 360) / 2),
    ]

    for center, t1, t2, col, num, dist, mid_ang in wedge_defs:
        w = patches.Wedge(center, r, t1, t2, facecolor=col, edgecolor=INK, lw=1.2, alpha=0.85, zorder=3)
        ax.add_patch(w)
        # Position label
        rad = np.radians(mid_ang)
        lx = center[0] + dist * np.cos(rad)
        ly = center[1] + dist * np.sin(rad)
        ax.text(lx, ly, num, fontsize=15, weight="bold", color=INK, ha="center", va="center", zorder=4)

    # Right side: Explanatory card / panel
    panel_bg = patches.FancyBboxPatch((7.6, 0.6), 4.1, 5.5,
                                      boxstyle="round,pad=0.3",
                                      fc=CREAM, ec=GREY, lw=1.5, zorder=1)
    ax.add_patch(panel_bg)

    # Legend / Angle relationships text
    ax.text(7.9, 5.7, "Angle Relationships", fontsize=16, weight="bold", color=INK)

    # Key / Equal groups
    p_box1 = patches.Rectangle((7.9, 5.1), 0.35, 0.3, facecolor=BLUE, edgecolor=INK, lw=1)
    p_box2 = patches.Rectangle((7.9, 4.6), 0.35, 0.3, facecolor=ORANGE, edgecolor=INK, lw=1)
    ax.add_patch(p_box1)
    ax.add_patch(p_box2)
    ax.text(8.4, 5.25, r"$\angle 1 = \angle 4 = \angle 5 = \angle 8$ (obtuse)", fontsize=14, va="center", color=INK)
    ax.text(8.4, 4.75, r"$\angle 2 = \angle 3 = \angle 6 = \angle 7$ (acute)", fontsize=14, va="center", color=INK)

    ax.plot([7.9, 11.4], [4.35, 4.35], color=GREY, lw=1)

    # Corresponding
    ax.text(7.9, 4.0, "Corresponding Pairs", fontsize=14.5, weight="bold", color=DEEP["blue"])
    ax.text(7.9, 3.65, "• Equal: (1, 5), (2, 6), (3, 7), (4, 8)", fontsize=14, color=INK)

    # Alternate Interior & Exterior
    ax.text(7.9, 3.1, "Alternate Pairs", fontsize=14.5, weight="bold", color=DEEP["blue"])
    ax.text(7.9, 2.75, "• Alternate Interior: (4, 5), (3, 6)", fontsize=14, color=INK)
    ax.text(7.9, 2.4, "• Alternate Exterior: (1, 8), (2, 7)", fontsize=14, color=INK)

    # Co-interior
    ax.text(7.9, 1.85, "Co-interior Pairs", fontsize=14.5, weight="bold", color=DEEP["orange"])
    ax.text(7.9, 1.5, "• Sum to 180° (Supplementary):", fontsize=14, color=INK)
    ax.text(8.1, 1.15, r"$\angle 4 + \angle 6 = 180^\circ$", fontsize=14, color=INK)
    ax.text(8.1, 0.8, r"$\angle 3 + \angle 5 = 180^\circ$", fontsize=14, color=INK)

    save(fig, out)
