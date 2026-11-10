from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)

    R = 1.0
    tilt = 0.28  # ellipse flattening for equator viewed from slight angle

    # Outer circle of the Earth
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(R * np.cos(theta), R * np.sin(theta), color=INK, lw=2.2, zorder=2)

    # Shading/tint for Earth
    sphere_fill = plt.Circle((0, 0), R, color=BLUE, alpha=0.08, zorder=1)
    ax.add_patch(sphere_fill)

    # Equator (ellipse)
    phi_front = np.linspace(np.pi, 2 * np.pi, 200)
    phi_back = np.linspace(0, np.pi, 200)
    ax.plot(R * np.cos(phi_back), tilt * R * np.sin(phi_back), color=GREY, lw=1.5, ls="--", zorder=2)
    ax.plot(R * np.cos(phi_front), tilt * R * np.sin(phi_front), color=DEEP["blue"], lw=2.5, zorder=3)

    # Parallel of latitude (at angle alpha ~ 42 deg)
    alpha = np.radians(42)
    y_lat = R * np.sin(alpha)
    r = R * np.cos(alpha)

    # Parallel of latitude ellipse
    ax.plot(r * np.cos(phi_back), y_lat + tilt * r * np.sin(phi_back), color=GREY, lw=1.5, ls="--", zorder=2)
    ax.plot(r * np.cos(phi_front), y_lat + tilt * r * np.sin(phi_front), color=DEEP["orange"], lw=2.5, zorder=3)

    # Polar Axis (North - South)
    ax.plot([0, 0], [-1.15 * R, 1.15 * R], color=INK, lw=1.8, ls="-.", zorder=2)
    ax.text(0, 1.18 * R, "N", ha="center", va="bottom", fontsize=16, fontweight="bold", color=INK)
    ax.text(0, -1.18 * R, "S", ha="center", va="top", fontsize=16, fontweight="bold", color=INK)

    # Greenwich Meridian (prime meridian passing near central meridian)
    psi = np.linspace(-np.pi/2, np.pi/2, 200)
    ax.plot(0.25 * R * np.cos(psi), R * np.sin(psi), color=DEEP["green"], lw=2.2, zorder=3)

    # Meridian of longitude (further out to the right)
    meridian_x = 0.72 * R * np.cos(psi)
    ax.plot(meridian_x, R * np.sin(psi), color=DEEP["lav"], lw=2.2, zorder=3)

    # Centre O of Earth
    ax.scatter([0], [0], color=INK, s=40, zorder=5)
    ax.text(-0.04, -0.04, "O", fontsize=15, fontweight="bold", ha="right", va="top", color=INK)

    # Centre O' of the parallel of latitude
    ax.scatter([0], [y_lat], color=INK, s=35, zorder=5)
    ax.text(-0.04, y_lat + 0.04, "O′", fontsize=15, ha="right", va="bottom", color=INK)

    # Point P on the surface at latitude alpha
    P_x = r
    P_y = y_lat
    ax.scatter([P_x], [P_y], color=INK, s=45, zorder=6)
    ax.text(P_x + 0.04, P_y + 0.04, "P", fontsize=15, fontweight="bold", ha="left", va="bottom", color=INK)

    # Radii
    ax.plot([0, P_x], [0, P_y], color=DEEP["pink"], lw=2.3, zorder=4)  # Radius R to P
    ax.plot([0, P_x], [y_lat, P_y], color=DEEP["orange"], lw=2.3, zorder=4)  # Radius r to P
    ax.plot([0, R], [0, 0], color=DEEP["blue"], lw=2.3, zorder=4)  # Radius R to equator

    # Labels for radii R and r
    ax.text(P_x / 2 - 0.04, P_y / 2 + 0.04, "R", fontsize=16, fontweight="bold", color=DEEP["pink"],
            bbox=dict(fc="white", ec="none", pad=1.0))
    ax.text(P_x / 2, y_lat + 0.05, "r", fontsize=16, fontweight="bold", color=DEEP["orange"],
            bbox=dict(fc="white", ec="none", pad=1.0))
    ax.text(R / 2, -0.07, "R", fontsize=16, fontweight="bold", color=DEEP["blue"],
            bbox=dict(fc="white", ec="none", pad=1.0))

    # Angle alpha arc at centre O
    arc_angles = np.linspace(0, alpha, 40)
    arc_rad = 0.32
    ax.plot(arc_rad * np.cos(arc_angles), arc_rad * np.sin(arc_angles), color=INK, lw=1.6, zorder=5)
    ax.text(arc_rad * np.cos(alpha/2) + 0.04, arc_rad * np.sin(alpha/2) + 0.01, "α", fontsize=16,
            fontweight="bold", color=INK, ha="left", va="center")

    # Alternate angle alpha at P (between PO and PO')
    arc_rad_p = 0.22
    ax.plot(P_x - arc_rad_p * np.cos(arc_angles), P_y - arc_rad_p * np.sin(arc_angles), color=INK, lw=1.4, zorder=5)
    ax.text(P_x - 0.25, P_y - 0.05, "α", fontsize=15, color=INK, ha="right", va="top")

    # Annotations and Feature Labels
    ax.annotate("Parallel of latitude", xy=(-0.45 * r, y_lat), xytext=(-1.2, y_lat + 0.2),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), va="center", ha="center")

    ax.annotate("Equator", xy=(-0.65 * R, 0), xytext=(-1.15, -0.3),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), va="center", ha="center")

    ax.annotate("Greenwich\nMeridian", xy=(0, R), xytext=(0, 1.35),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), va="center", ha="center")

    ax.annotate("Meridian of\nlongitude", xy=(meridian_x[100], R), xytext=(0.8, 1.25),
                fontsize=14, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), va="center", ha="center")

    # Relationship formula in a neat box
    ax.text(0, -1.25, "r = R cos α", fontsize=16, ha="center", va="center",
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"))

    save(fig, out)
