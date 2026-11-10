from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlim(-4.2, 4.2)
    ax.set_ylim(-4.2, 4.2)
    ax.axis("off")

    # Central Round Table
    table_radius = 1.8
    table = patches.Circle((0, 0), table_radius, facecolor=CREAM, edgecolor=INK, lw=2.5, zorder=2)
    ax.add_patch(table)

    # 6 Chairs arranged evenly in a circle around the table
    n_chairs = 6
    chair_dist = 2.6
    chair_w, chair_h = 0.8, 0.7

    for i in range(n_chairs):
        angle_deg = i * 60
        angle_rad = np.deg2rad(angle_deg)
        cx = chair_dist * np.cos(angle_rad)
        cy = chair_dist * np.sin(angle_rad)

        # Draw chair seat: a rounded rectangle facing the table
        # We rotate rectangle centered at (cx, cy)
        # Angle of rotation: angle_deg points radially outward; seat back is further out, seat front towards center.
        seat = patches.FancyBboxPatch(
            (-chair_w / 2, -chair_h / 2),
            chair_w, chair_h,
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor=BLUE, edgecolor=DEEP["blue"], lw=2,
            zorder=3
        )
        # Transform chair position and rotation
        t = plt.matplotlib.transforms.Affine2D().rotate_deg(angle_deg - 90).translate(cx, cy) + ax.transData
        seat.set_transform(t)
        ax.add_patch(seat)

        # Chair backrest (a curved thick arc or bar slightly further from the center)
        back_dist = chair_dist + 0.32
        bx = back_dist * np.cos(angle_rad)
        by = back_dist * np.sin(angle_rad)
        back = patches.FancyBboxPatch(
            (-chair_w * 0.45, -0.08),
            chair_w * 0.9, 0.16,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor=DEEP["blue"], edgecolor=INK, lw=1.5,
            zorder=4
        )
        tb = plt.matplotlib.transforms.Affine2D().rotate_deg(angle_deg - 90).translate(bx, by) + ax.transData
        back.set_transform(tb)
        ax.add_patch(back)

    # Curved arrow showing rotational symmetry / no fixed first or last position
    # An arc just inside the table perimeter or along the table edge
    arc_radius = 1.2
    arc_theta1 = 30
    arc_theta2 = 150
    arrow_arc = patches.Arc((0, 0), arc_radius * 2, arc_radius * 2, angle=0,
                            theta1=arc_theta1, theta2=arc_theta2,
                            color=DEEP["orange"], lw=3.5, zorder=5)
    ax.add_patch(arrow_arc)

    # Arrowhead at arc_theta2 (150 degrees)
    head_rad = np.deg2rad(arc_theta2)
    head_x = arc_radius * np.cos(head_rad)
    head_y = arc_radius * np.sin(head_rad)
    # Direction tangent along counter-clockwise circle: (-sin(theta), cos(theta))
    dx = -np.sin(head_rad) * 0.01
    dy = np.cos(head_rad) * 0.01

    arrow = patches.FancyArrow(head_x, head_y, dx, dy,
                               width=0.05, length_includes_head=True,
                               head_width=0.28, head_length=0.32,
                               facecolor=DEEP["orange"], edgecolor=DEEP["orange"],
                               zorder=6)
    ax.add_patch(arrow)

    # Table center label
    ax.text(0, -0.1, "Round\nTable", fontsize=16, ha="center", va="center",
            color=INK, weight="bold", zorder=7)

    # Explanation annotations
    ax.text(0, 3.7, "Circular Permutations: $(n - 1)!$", fontsize=18,
            ha="center", va="center", color=INK, weight="bold")

    ax.text(0, -3.7, "Rotational equivalence:\nno distinct first or last position",
            fontsize=15, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2))

    save(fig, out)
