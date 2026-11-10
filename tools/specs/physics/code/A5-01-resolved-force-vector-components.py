from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Set limits
    ax.set_xlim(-1.5, 9.5)
    ax.set_ylim(-1.5, 7.0)

    # Floor ground
    floor_y = 1.0
    ax.plot([-1.0, 9.0], [floor_y, floor_y], color=GREY, lw=2)
    # Hatching under floor
    for hx in np.linspace(-0.8, 8.8, 25):
        ax.plot([hx, hx - 0.3], [floor_y, floor_y - 0.3], color=GREY, lw=1.2)

    # Rectangular box
    box_w, box_h = 2.4, 1.8
    box_x = 0.5
    box = patches.Rectangle(
        (box_x, floor_y), box_w, box_h,
        facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3
    )
    ax.add_patch(box)

    # Center of front/side or attachment point (e.g. center of the box)
    origin_x = box_x + box_w
    origin_y = floor_y + box_h / 2.0

    # Axes: dotted lines
    axis_len = 5.8
    ax.plot([origin_x, origin_x + axis_len], [origin_y, origin_y],
            ls=":", color=INK, lw=1.8, zorder=2)
    ax.text(origin_x + axis_len + 0.2, origin_y, "x", color=INK,
            fontsize=16, va="center", ha="left")

    ax.plot([origin_x, origin_x], [origin_y, origin_y + axis_len * 0.75],
            ls=":", color=INK, lw=1.8, zorder=2)
    ax.text(origin_x, origin_y + axis_len * 0.75 + 0.3, "y", color=INK,
            fontsize=16, va="bottom", ha="center")

    # Force vector F = 50 N at 30 degrees
    theta_deg = 30
    theta_rad = np.radians(theta_deg)
    F_mag = 4.8
    Fx_mag = F_mag * np.cos(theta_rad)
    Fy_mag = F_mag * np.sin(theta_rad)

    vec_end_x = origin_x + Fx_mag
    vec_end_y = origin_y + Fy_mag

    # Angle arc and label (30°)
    arc_rad = 1.4
    arc_theta = np.linspace(0, theta_rad, 40)
    ax.plot(origin_x + arc_rad * np.cos(arc_theta),
            origin_y + arc_rad * np.sin(arc_theta),
            color=INK, lw=1.5)
    ax.text(origin_x + 1.7 * np.cos(theta_rad / 2),
            origin_y + 1.7 * np.sin(theta_rad / 2),
            "30°", color=INK, fontsize=15, va="center", ha="left")

    # Projection helper dotted lines to form rectangle of components
    ax.plot([vec_end_x, vec_end_x], [origin_y, vec_end_y],
            ls="--", color=GREY, lw=1.2, zorder=2)
    ax.plot([origin_x, vec_end_x], [vec_end_y, vec_end_y],
            ls="--", color=GREY, lw=1.2, zorder=2)

    # Component arrow: F_x along x-axis (red dashed arrow)
    ax.annotate(
        "", xy=(origin_x + Fx_mag, origin_y), xytext=(origin_x, origin_y),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                        color=DEEP["pink"], ls="--", lw=2.5),
        zorder=4
    )
    ax.text(
        origin_x + Fx_mag / 2, origin_y - 0.5,
        r"$F_x = F \cos 30^\circ$",
        color=DEEP["pink"], fontsize=15, ha="center", va="top",
        bbox=dict(fc="white", ec="none", pad=2)
    )

    # Component arrow: F_y along y-axis (red dashed arrow)
    ax.annotate(
        "", xy=(origin_x, origin_y + Fy_mag), xytext=(origin_x, origin_y),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                        color=DEEP["pink"], ls="--", lw=2.5),
        zorder=4
    )
    ax.text(
        origin_x - 0.35, origin_y + Fy_mag / 2,
        r"$F_y = F \sin 30^\circ$",
        color=DEEP["pink"], fontsize=15, ha="right", va="center",
        bbox=dict(fc="white", ec="none", pad=2)
    )

    # Main Force Arrow: solid arrow F = 50 N
    ax.annotate(
        "", xy=(vec_end_x, vec_end_y), xytext=(origin_x, origin_y),
        arrowprops=dict(arrowstyle="->,head_width=0.5,head_length=0.7",
                        color=DEEP["blue"], lw=3.2),
        zorder=5
    )
    ax.text(
        vec_end_x + 0.25, vec_end_y + 0.25,
        r"$F = 50\ \mathrm{N}$",
        color=DEEP["blue"], fontsize=16, weight="bold",
        va="bottom", ha="left",
        bbox=dict(fc="white", ec="none", pad=2)
    )

    # Label for Box
    ax.text(
        box_x + box_w / 2, floor_y + box_h / 2,
        "Box", color=INK, fontsize=15, ha="center", va="center", zorder=4
    )

    save(fig, out)
