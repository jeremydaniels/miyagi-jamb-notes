from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_xlim(-17, 17)
    ax.set_ylim(-16, 16)
    ax.axis('off')

    # Title
    ax.text(0, 14.5, "Monthly Wind Rose Diagram", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # Concentric reference grid circles (days: 4, 8, 12)
    r_calm = 2.4
    scale = 0.85  # length per day beyond calm octagon

    for days in [4, 8, 12]:
        r = r_calm + days * scale
        circle = plt.Circle((0, 0), r, fill=False, edgecolor=GREY, linestyle='--', linewidth=1.2, zorder=1)
        ax.add_patch(circle)
        ax.text(r * np.cos(np.radians(22.5)), r * np.sin(np.radians(22.5)), f"{days} d",
                ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none'))

    # Directions, angles (0 = East, math convention), and days for each
    directions = [
        ('N', 90, 4),
        ('NE', 45, 2),
        ('E', 0, 1),
        ('SE', 315, 2),
        ('S', 270, 3),
        ('SW', 225, 12),  # Longest bar: 12 days
        ('W', 180, 5),
        ('NW', 135, 2),
    ]

    bar_width_deg = 18

    # Draw bars radiating from octagon boundary
    for label, angle_deg, days in directions:
        rad = np.radians(angle_deg)
        length = days * scale
        r_outer = r_calm + length

        # Rectangular/sector bar patch
        theta1 = angle_deg - bar_width_deg / 2
        theta2 = angle_deg + bar_width_deg / 2
        t = np.linspace(np.radians(theta1), np.radians(theta2), 20)

        # Polygon coordinates for bar
        x_inner = r_calm * np.cos(t)
        y_inner = r_calm * np.sin(t)
        x_outer = r_outer * np.cos(t[::-1])
        y_outer = r_outer * np.sin(t[::-1])

        x_bar = np.concatenate([x_inner, x_outer])
        y_bar = np.concatenate([y_inner, y_outer])

        # Distinct highlight for SW (longest bar, 12 days)
        if label == 'SW':
            col = BLUE
            edge_col = DEEP['blue']
        else:
            col = LAV
            edge_col = DEEP['lav']

        ax.fill(x_bar, y_bar, color=col, ec=edge_col, lw=1.8, zorder=2)

        # Labels for directions
        lbl_r = 14.5 if label == 'SW' else 13.5
        lx = lbl_r * np.cos(rad)
        ly = lbl_r * np.sin(rad)
        ax.text(lx, ly, label, ha='center', va='center', fontsize=16,
                fontweight='bold', color=INK)

    # Central regular octagon for calm days
    # 8 vertices offset by 22.5 deg to align flat sides with the 8 directions
    angles = np.radians(np.linspace(22.5, 360 + 22.5, 8, endpoint=False))
    oct_x = r_calm * np.cos(angles)
    oct_y = r_calm * np.sin(angles)
    ax.fill(oct_x, oct_y, color=CREAM, ec=INK, lw=2.5, zorder=3)

    # Number 3 in center
    ax.text(0, 0, "3", ha='center', va='center', fontsize=18, fontweight='bold',
            color=INK, zorder=4)

    # Annotation for SW bar and calm center
    ax.annotate("South-West: 12 days\n(Prevailing wind)",
                xy=(-(r_calm + 12 * scale) * np.cos(np.radians(45)),
                    -(r_calm + 12 * scale) * np.sin(np.radians(45))),
                xytext=(-15, -11),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.3"),
                zorder=5)

    ax.annotate("Central octagon: 3 calm days\n(Total days = 31)",
                xy=(0, -r_calm),
                xytext=(3, -13),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.3"),
                zorder=5)

    save(fig, out)
