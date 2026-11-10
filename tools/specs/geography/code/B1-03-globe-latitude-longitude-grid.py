from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")

    R = 1.0

    # Background shaded globe circle
    globe_bg = Circle((0, 0), R, facecolor=CREAM, edgecolor="none", zorder=1)
    ax.add_patch(globe_bg)

    # Draw parallels (Lines of Latitude)
    latitudes = [-60, -45, -30, -15, 0, 15, 30, 45, 60]
    for lat in latitudes:
        phi = np.radians(lat)
        y = R * np.sin(phi)
        r_slice = R * np.cos(phi)
        x_vals = np.linspace(-r_slice, r_slice, 200)
        y_vals = np.full_like(x_vals, y)

        if lat == 0:
            # Equator
            ax.plot(x_vals, y_vals, color=DEEP["orange"], lw=3.0, zorder=3)
        else:
            ax.plot(x_vals, y_vals, color=GREY, lw=1.5, linestyle="--", zorder=2)

    # Draw meridians (Lines of Longitude)
    # Visible front meridians as half-ellipses from (0, -R) to (0, R)
    longitudes = [-75, -50, -25, 0, 25, 50, 75]
    theta = np.linspace(-np.pi/2, np.pi/2, 200)
    y_merid = R * np.sin(theta)

    for lon in longitudes:
        # projected semi-minor axis
        a = R * np.sin(np.radians(lon))
        x_merid = a * np.cos(theta)
        if lon == 0:
            # Prime Meridian
            ax.plot(x_merid, y_merid, color=DEEP["blue"], lw=3.0, zorder=4)
        else:
            ax.plot(x_merid, y_merid, color=DEEP["lav"], lw=1.6, zorder=2)

    # Globe outer boundary circle
    globe_border = Circle((0, 0), R, fill=False, edgecolor=INK, lw=2.5, zorder=5)
    ax.add_patch(globe_border)

    # Mark Poles
    ax.plot(0, R, marker="o", markersize=6, color=INK, zorder=6)
    ax.plot(0, -R, marker="o", markersize=6, color=INK, zorder=6)

    # Annotations & Labels placed well outside globe boundary (R=1.0)
    # 1. North Pole
    ax.annotate(
        "North Pole",
        xy=(0, R),
        xytext=(0, R + 0.35),
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY),
        zorder=10
    )

    # 2. South Pole
    ax.annotate(
        "South Pole",
        xy=(0, -R),
        xytext=(0, -R - 0.35),
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY),
        zorder=10
    )

    # 3. Equator (0°)
    ax.annotate(
        "Equator (0°)",
        xy=(-0.5, 0),
        xytext=(-1.65, -0.35),
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=DEEP["orange"],
        arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["orange"]),
        zorder=10
    )

    # 4. Lines of Latitude (parallel)
    ax.annotate(
        "Lines of Latitude (parallel)",
        xy=(-0.4, 0.5),
        xytext=(-1.65, 0.65),
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY),
        zorder=10
    )

    # 5. Prime Meridian (0°)
    ax.annotate(
        "Prime Meridian (0°)",
        xy=(0, 0.1),
        xytext=(1.65, -0.2),
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=DEEP["blue"],
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"]),
        zorder=10
    )

    # 6. Lines of Longitude (Meridians) meeting at the poles
    ax.annotate(
        "Lines of Longitude (Meridians)\nmeeting at the poles",
        xy=(0.35, 0.55),
        xytext=(1.65, 0.65),
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY),
        zorder=10
    )

    save(fig, out)
