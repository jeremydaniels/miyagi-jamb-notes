from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Color definitions for this diagram
    red_nucleus = "#D32F2F"
    electron_blue = DEEP["blue"]

    # --- 1. Thomson Model (Plum Pudding) ---
    c1 = (2.4, 3.0)
    r1 = 1.6
    # Pink positive sphere
    sphere = patches.Circle(c1, r1, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5, zorder=1)
    ax.add_patch(sphere)
    
    # Positive soup background label / plus signs
    plus_positions = [(-0.8, 0.7), (0.7, 0.8), (-0.7, -0.7), (0.8, -0.6), (0.0, 1.1), (0.0, -1.1)]
    for dx, dy in plus_positions:
        ax.text(c1[0] + dx, c1[1] + dy, "+", color=DEEP["pink"], fontsize=18, fontweight='bold', ha='center', va='center', zorder=2)

    # Scattered electrons (blue dots with minus signs)
    e_coords_1 = [
        (-0.6, 0.2), (0.5, 0.3), (-0.1, -0.4), (0.2, 0.8), 
        (-0.3, 0.6), (0.7, -0.2), (-0.2, -1.0), (0.6, -0.8)
    ]
    for dx, dy in e_coords_1:
        ep = patches.Circle((c1[0] + dx, c1[1] + dy), 0.2, facecolor=electron_blue, edgecolor="white", lw=1.5, zorder=3)
        ax.add_patch(ep)
        ax.text(c1[0] + dx, c1[1] + dy, "–", color="white", fontsize=14, fontweight='bold', ha='center', va='center', zorder=4)

    ax.text(c1[0], 0.6, "Thomson Model\n(Plum Pudding)", ha="center", va="top", fontsize=15, color=INK, fontweight="bold")

    # --- 2. Rutherford Model (Planetary) ---
    c2 = (7.0, 3.0)
    # Elliptical orbits
    angles = [0, 60, 120]
    for ang in angles:
        ellipse = patches.Ellipse(c2, width=3.4, height=1.1, angle=ang, fill=False, edgecolor=GREY, lw=2, linestyle='-', zorder=1)
        ax.add_patch(ellipse)

    # Central nucleus (+)
    nuc2 = patches.Circle(c2, 0.35, facecolor=red_nucleus, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(nuc2)
    ax.text(c2[0], c2[1], "+", color="white", fontsize=16, fontweight='bold', ha='center', va='center', zorder=4)

    # Electrons on orbits
    # Calculate points on rotated ellipses
    e_thetas = [
        (angles[0], 0, 1.7, 0.55),
        (angles[0], np.pi, 1.7, 0.55),
        (angles[1], np.pi/3, 1.7, 0.55),
        (angles[1], 4*np.pi/3, 1.7, 0.55),
        (angles[2], 2*np.pi/3, 1.7, 0.55),
        (angles[2], 5*np.pi/3, 1.7, 0.55)
    ]
    for rot, theta, a, b in e_thetas:
        rad = np.radians(rot)
        x_e = a * np.cos(theta)
        y_e = b * np.sin(theta)
        xr = c2[0] + x_e * np.cos(rad) - y_e * np.sin(rad)
        yr = c2[1] + x_e * np.sin(rad) + y_e * np.cos(rad)
        ep = patches.Circle((xr, yr), 0.16, facecolor=electron_blue, edgecolor="white", lw=1.2, zorder=5)
        ax.add_patch(ep)
        ax.text(xr, yr, "–", color="white", fontsize=12, fontweight='bold', ha='center', va='center', zorder=6)

    ax.text(c2[0], 0.6, "Rutherford Model\n(Planetary)", ha="center", va="top", fontsize=15, color=INK, fontweight="bold")

    # --- 3. Bohr Model ---
    c3 = (11.6, 3.0)
    radii = [0.9, 1.5]
    # Concentric rings (shells)
    for r in radii:
        shell = patches.Circle(c3, r, fill=False, edgecolor=GREY, lw=2, linestyle='--', zorder=1)
        ax.add_patch(shell)

    # Nucleus (+)
    nuc3 = patches.Circle(c3, 0.35, facecolor=red_nucleus, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(nuc3)
    ax.text(c3[0], c3[1], "+", color="white", fontsize=16, fontweight='bold', ha='center', va='center', zorder=4)

    # Ground-state-like electron on inner shell
    ep_inner = patches.Circle((c3[0] - radii[0], c3[1]), 0.16, facecolor=electron_blue, edgecolor="white", lw=1.2, zorder=4)
    ax.add_patch(ep_inner)
    ax.text(c3[0] - radii[0], c3[1], "–", color="white", fontsize=12, fontweight='bold', ha='center', va='center', zorder=5)

    # Transitioning electron from outer to inner shell (jumping between rings)
    # Position: outer shell at 45 deg, jumping towards inner shell
    angle_jump = np.pi / 4
    p_outer = np.array([c3[0] + radii[1] * np.cos(angle_jump), c3[1] + radii[1] * np.sin(angle_jump)])
    p_inner = np.array([c3[0] + radii[0] * np.cos(angle_jump), c3[1] + radii[0] * np.sin(angle_jump)])

    # Ghost start on outer ring
    ghost = patches.Circle(p_outer, 0.16, facecolor="none", edgecolor=electron_blue, lw=1.5, linestyle=":", zorder=3)
    ax.add_patch(ghost)

    # Arrow indicating transition inwards
    ax.annotate("", xy=p_inner, xytext=p_outer,
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=15),
                zorder=4)

    # Arriving / jumping electron shown near inner ring
    ep_jump = patches.Circle(p_inner, 0.16, facecolor=electron_blue, edgecolor="white", lw=1.2, zorder=5)
    ax.add_patch(ep_jump)
    ax.text(p_inner[0], p_inner[1], "–", color="white", fontsize=12, fontweight='bold', ha='center', va='center', zorder=6)

    # Photon emission (wavy arrow leaving the jump site)
    # Wavy path going outward towards top-right
    s = np.linspace(0, 1.4, 100)
    w_amp = 0.08
    w_freq = 25
    photon_x = p_outer[0] + 0.15 + s * np.cos(np.radians(20)) - w_amp * np.sin(w_freq * s) * np.sin(np.radians(20))
    photon_y = p_outer[1] + 0.15 + s * np.sin(np.radians(20)) + w_amp * np.sin(w_freq * s) * np.cos(np.radians(20))
    ax.plot(photon_x, photon_y, color=DEEP["orange"], lw=2.2, zorder=5)
    # Arrow head for photon
    ax.annotate("", xy=(photon_x[-1], photon_y[-1]), xytext=(photon_x[-8], photon_y[-8]),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=14),
                zorder=5)
    ax.text(photon_x[-1] + 0.15, photon_y[-1] + 0.05, "photon", color=DEEP["orange"], fontsize=14, fontweight="bold", ha="left", va="center")

    ax.text(c3[0], 0.6, "Bohr Model\n(Shells / Energy Levels)", ha="center", va="top", fontsize=15, color=INK, fontweight="bold")

    save(fig, out)
