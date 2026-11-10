from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-5.2, 5.2)

    # 16 Compass points definition: name, angle (deg from North, clockwise), type (0=cardinal, 1=intercardinal, 2=subdivision)
    points_info = [
        ("N", 0, 0),
        ("NNE", 22.5, 2),
        ("NE", 45, 1),
        ("ENE", 67.5, 2),
        ("E", 90, 0),
        ("ESE", 112.5, 2),
        ("SE", 135, 1),
        ("SSE", 157.5, 2),
        ("S", 180, 0),
        ("SSW", 202.5, 2),
        ("SW", 225, 1),
        ("WSW", 247.5, 2),
        ("W", 270, 0),
        ("WNW", 292.5, 2),
        ("NW", 315, 1),
        ("NNW", 337.5, 2),
    ]

    # Outer decorative rings
    ring_angles = np.linspace(0, 2 * np.pi, 360)
    ax.plot(3.7 * np.cos(ring_angles), 3.7 * np.sin(ring_angles), color=GREY, lw=1.2)
    ax.plot(4.15 * np.cos(ring_angles), 4.15 * np.sin(ring_angles), color=INK, lw=1.5)

    # Degree tick marks around the ring
    for deg in range(0, 360, 5):
        rad = np.radians(90 - deg)
        if deg % 90 == 0:
            r1, r2 = 3.6, 4.15
            lw = 1.8
        elif deg % 45 == 0:
            r1, r2 = 3.7, 4.15
            lw = 1.4
        elif deg % 10 == 0:
            r1, r2 = 3.85, 4.15
            lw = 1.0
        else:
            r1, r2 = 3.95, 4.15
            lw = 0.6
        ax.plot([r1 * np.cos(rad), r2 * np.cos(rad)],
                [r1 * np.sin(rad), r2 * np.sin(rad)],
                color=INK, lw=lw)

    # Helper function to draw shaded points (rhombus half-facets)
    def draw_spear(angle_deg, length, base_width, c_left, c_right):
        theta = np.radians(90 - angle_deg)
        left_theta = theta + np.pi / 2
        right_theta = theta - np.pi / 2

        tip = np.array([length * np.cos(theta), length * np.sin(theta)])
        p_left = np.array([base_width * np.cos(left_theta), base_width * np.sin(left_theta)])
        p_right = np.array([base_width * np.cos(right_theta), base_width * np.sin(right_theta)])
        origin = np.array([0, 0])

        poly_l = plt.Polygon([origin, tip, p_left], facecolor=c_left, edgecolor=INK, lw=0.8, zorder=2)
        poly_r = plt.Polygon([origin, tip, p_right], facecolor=c_right, edgecolor=INK, lw=0.8, zorder=2)
        ax.add_patch(poly_l)
        ax.add_patch(poly_r)

    # Draw 8 subdivisions (smallest)
    for name, deg, ptype in points_info:
        if ptype == 2:
            draw_spear(deg, 2.3, 0.22, LAV, "white")

    # Draw 4 intercardinals (medium)
    for name, deg, ptype in points_info:
        if ptype == 1:
            draw_spear(deg, 2.9, 0.38, BLUE, CREAM)

    # Draw 4 cardinals (largest)
    for name, deg, ptype in points_info:
        if ptype == 0:
            draw_spear(deg, 3.65, 0.55, DEEP["blue"], "white")

    # Central rings / cap
    c1 = plt.Circle((0, 0), 0.35, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=4)
    c2 = plt.Circle((0, 0), 0.12, facecolor=DEEP["blue"], edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # Labels for direction points and degrees
    deg_labels = {
        0: "0° / 360°",
        90: "90°",
        180: "180°",
        270: "270°"
    }

    for name, deg, ptype in points_info:
        rad = np.radians(90 - deg)
        cos_t = np.cos(rad)
        sin_t = np.sin(rad)

        if ptype == 0:
            # Cardinal point
            r_label = 4.5
            ax.text(r_label * cos_t, r_label * sin_t, name,
                    ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
            
            # Degree label outside
            r_deg = 4.88
            ax.text(r_deg * cos_t, r_deg * sin_t, deg_labels[deg],
                    ha="center", va="center", fontsize=14, color=INK,
                    bbox=dict(fc="white", ec="none", pad=1.5))
        elif ptype == 1:
            # Intercardinal point
            r_label = 3.3
            ax.text(r_label * cos_t, r_label * sin_t, name,
                    ha="center", va="center", fontsize=15, fontweight="semibold", color=INK,
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.0), zorder=3)
        else:
            # Subdivisions
            r_label = 2.6
            ax.text(r_label * cos_t, r_label * sin_t, name,
                    ha="center", va="center", fontsize=14, color=INK,
                    bbox=dict(fc="white", ec="none", alpha=0.8, pad=0.8), zorder=3)

    save(fig, out)
