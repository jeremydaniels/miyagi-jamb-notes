from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Media backgrounds
    # Air (top, light blue tint)
    ax.axhspan(0, 4, facecolor='#EBF4FA', zorder=0)
    # Water (bottom, darker blue)
    ax.axhspan(-4, 0, facecolor='#D0E4F5', zorder=0)

    # Boundary interface line
    ax.axhline(0, color=INK, lw=2.5, zorder=2)

    # Normal line (vertical dashed)
    ax.axvline(0, ymin=0.08, ymax=0.92, color=INK, ls='--', lw=1.8, zorder=2)

    # Parameters for rays
    # Incident ray: comes from top left, angle to normal theta_i = 45 degrees
    # Refracted ray: bends towards normal in water, n_air=1, n_water=1.333
    # sin(r) = sin(45)/1.333 => r ~ 32.1 degrees (in bottom right quadrant)
    theta_i_deg = 45.0
    theta_r_deg = np.degrees(np.arcsin(np.sin(np.radians(theta_i_deg)) / 1.333))

    # Points
    L_in = 4.2
    x_in = -L_in * np.sin(np.radians(theta_i_deg))
    y_in = L_in * np.cos(np.radians(theta_i_deg))

    L_ref = 4.0
    x_ref = L_ref * np.sin(np.radians(theta_r_deg))
    y_ref = -L_ref * np.cos(np.radians(theta_r_deg))

    # Red ray (incident and refracted)
    RAY_COLOR = DEEP['pink']
    ax.plot([x_in, 0], [y_in, 0], color=RAY_COLOR, lw=3, zorder=3)
    ax.plot([0, x_ref], [0, y_ref], color=RAY_COLOR, lw=3, zorder=3)

    # Arrows indicating light direction
    # Arrow on incident ray (pointing towards (0,0))
    mid_in = (x_in * 0.45, y_in * 0.45)
    dx_in = -x_in * 0.1
    dy_in = -y_in * 0.1
    ax.annotate('', xy=(mid_in[0] + dx_in, mid_in[1] + dy_in), xytext=mid_in,
                arrowprops=dict(arrowstyle="-|>", color=RAY_COLOR, lw=2.5, mutation_scale=20),
                zorder=4)

    # Arrow on refracted ray (pointing away from (0,0))
    mid_ref = (x_ref * 0.55, y_ref * 0.55)
    dx_ref = x_ref * 0.1
    dy_ref = y_ref * 0.1
    ax.annotate('', xy=(mid_ref[0] + dx_ref, mid_ref[1] + dy_ref), xytext=mid_ref,
                arrowprops=dict(arrowstyle="-|>", color=RAY_COLOR, lw=2.5, mutation_scale=20),
                zorder=4)

    # Angle arcs
    # Angle of incidence i: from normal (90 deg) to incident ray (135 deg) on the top left
    arc_i = Arc((0, 0), 2.2, 2.2, angle=0, theta1=90, theta2=135,
                color=INK, lw=1.6, zorder=3)
    ax.add_patch(arc_i)

    # Angle of refraction r: between normal (270 deg) and refracted ray (270 + theta_r = ~302 deg) on bottom right
    arc_r = Arc((0, 0), 2.2, 2.2, angle=0, theta1=270, theta2=270 + theta_r_deg,
                color=INK, lw=1.6, zorder=3)
    ax.add_patch(arc_r)

    # Label angles
    ax.text(-0.55, 1.45, r"$i$", fontsize=18, color=INK, ha='center', va='center')
    ax.text(0.45, -1.45, r"$r$", fontsize=18, color=INK, ha='center', va='center')

    # Media labels
    ax.text(-4.6, 3.4, "Air (less dense)", fontsize=16, fontweight='bold', color=INK,
            ha='left', va='center', bbox=dict(fc='white', ec='none', pad=3, alpha=0.85))
    ax.text(-4.6, -3.4, "Water (optically denser)", fontsize=16, fontweight='bold', color=INK,
            ha='left', va='center', bbox=dict(fc='white', ec='none', pad=3, alpha=0.85))

    # Ray & Normal Labels
    ax.text(-2.4, 2.8, "Incident ray", fontsize=15, color=RAY_COLOR, fontweight='semibold',
            ha='center', va='bottom', bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.25"))
    ax.text(2.2, -2.5, "Refracted ray", fontsize=15, color=RAY_COLOR, fontweight='semibold',
            ha='center', va='top', bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.25"))
    ax.text(0.15, 3.65, "Normal", fontsize=15, color=INK, fontstyle='italic',
            ha='left', va='center', bbox=dict(fc='white', ec='none', pad=2, alpha=0.85))

    save(fig, out)
