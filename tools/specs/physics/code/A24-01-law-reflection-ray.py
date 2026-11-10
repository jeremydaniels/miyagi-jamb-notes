from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-1.8, 5.2)
    ax.axis("off")

    # Mirror surface line (horizontal at y = 0)
    x_min, x_max = -4.5, 4.5
    ax.plot([x_min, x_max], [0, 0], color=INK, lw=3)

    # Diagonal hash marks on bottom side of the mirror
    hash_spacing = 0.4
    hash_len = 0.35
    for x in np.arange(x_min + 0.2, x_max, hash_spacing):
        ax.plot([x, x - hash_len * 0.7], [0, -hash_len], color=GREY, lw=1.5)

    # Mirror label
    ax.text(x_max + 0.2, 0, "Plane mirror", va="center", ha="left", fontsize=14, color=INK)

    # Normal line (dashed vertical line at x = 0)
    ax.plot([0, 0], [0, 4.5], color=DEEP["blue"], lw=2.2, linestyle="--")
    ax.text(0, 4.7, "Normal", ha="center", va="bottom", fontsize=15, color=DEEP["blue"], fontweight="bold")

    # Reflection angle: 50 degrees to normal
    theta_deg = 50.0
    theta_rad = np.radians(theta_deg)
    ray_len = 5.0

    # Point of incidence is O = (0, 0)
    # Incident ray comes from top-left: (-ray_len * sin(theta), ray_len * cos(theta))
    ix, iy = -ray_len * np.sin(theta_rad), ray_len * np.cos(theta_rad)
    # Reflected ray goes toward top-right: (ray_len * sin(theta), ray_len * cos(theta))
    rx, ry = ray_len * np.sin(theta_rad), ray_len * np.cos(theta_rad)

    # Draw incident and reflected rays
    ax.plot([ix, 0], [iy, 0], color=DEEP["pink"], lw=3)
    ax.plot([0, rx], [0, ry], color=DEEP["pink"], lw=3)

    # Inward arrow on incident ray: pointing toward (0, 0)
    # Vector along incident ray direction is (0 - ix, 0 - iy) = (-ix, -iy)
    # At t = 0.55 along the path from (ix, iy) to (0, 0):
    t_in = 0.55
    px_in = ix * (1 - t_in)
    py_in = iy * (1 - t_in)
    step_in = 0.25
    u_in_x = -ix / ray_len
    u_in_y = -iy / ray_len
    ax.annotate(
        "",
        xy=(px_in + step_in * u_in_x, py_in + step_in * u_in_y),
        xytext=(px_in - step_in * u_in_x, py_in - step_in * u_in_y),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=22),
    )

    # Outward arrow on reflected ray: pointing away from (0, 0) toward (rx, ry)
    # Vector along reflected ray direction is (rx, ry)
    t_out = 0.55
    px_out = rx * t_out
    py_out = ry * t_out
    step_out = 0.25
    u_out_x = rx / ray_len
    u_out_y = ry / ray_len
    ax.annotate(
        "",
        xy=(px_out + step_out * u_out_x, py_out + step_out * u_out_y),
        xytext=(px_out - step_out * u_out_x, py_out - step_out * u_out_y),
        arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=22),
    )

    # Ray Labels
    ax.text(ix * 0.75 - 0.25, iy * 0.75, "Incident ray", ha="right", va="center", fontsize=15, color=INK)
    ax.text(rx * 0.75 + 0.25, ry * 0.75, "Reflected ray", ha="left", va="center", fontsize=15, color=INK)

    # Arcs for angles
    # Angle 'i': between normal (90 deg) and incident ray (90 + theta_deg = 140 deg)
    arc_i = patches.Arc((0, 0), 2.8, 2.8, angle=0, theta1=90, theta2=90 + theta_deg, color=DEEP["lav"], lw=2.2)
    ax.add_patch(arc_i)
    # Position for label 'i'
    ang_i_mid = np.radians(90 + theta_deg / 2)
    ax.text(
        1.75 * np.cos(ang_i_mid),
        1.75 * np.sin(ang_i_mid),
        "i",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=INK,
        bbox=dict(fc="white", ec="none", pad=1.5),
    )

    # Angle 'r': between reflected ray (90 - theta_deg = 40 deg) and normal (90 deg)
    arc_r = patches.Arc((0, 0), 2.8, 2.8, angle=0, theta1=90 - theta_deg, theta2=90, color=DEEP["lav"], lw=2.2)
    ax.add_patch(arc_r)
    # Position for label 'r'
    ang_r_mid = np.radians(90 - theta_deg / 2)
    ax.text(
        1.75 * np.cos(ang_r_mid),
        1.75 * np.sin(ang_r_mid),
        "r",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=INK,
        bbox=dict(fc="white", ec="none", pad=1.5),
    )

    # Angle 'g' (glancing angle): between mirror (180 deg) and incident ray (140 deg)
    arc_g = patches.Arc((0, 0), 2.4, 2.4, angle=0, theta1=90 + theta_deg, theta2=180, color=DEEP["green"], lw=2.2)
    ax.add_patch(arc_g)
    # Position for label 'g'
    ang_g_mid = np.radians(180 - (90 - theta_deg) / 2)
    ax.text(
        1.55 * np.cos(ang_g_mid),
        1.55 * np.sin(ang_g_mid),
        "g",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=INK,
        bbox=dict(fc="white", ec="none", pad=1.5),
    )

    # Point of incidence label
    ax.plot(0, 0, marker="o", markersize=5, color=INK)
    ax.text(0, -0.7, "Point of incidence", ha="center", va="top", fontsize=14, color=INK)

    # Title / Caption
    ax.set_title("Laws of Reflection", fontsize=18, color=INK, pad=14, fontweight="bold")

    save(fig, out)
