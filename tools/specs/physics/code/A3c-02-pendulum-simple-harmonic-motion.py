from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-6.8, 2.0)

    # Pivot / Support parameters
    px, py = 0.0, 0.8
    L = 5.0
    theta_deg = 24.0
    theta_rad = np.radians(theta_deg)
    r_bob = 0.45

    # Rigid support beam
    ax.plot([-3.0, 3.0], [py, py], color=INK, lw=3)
    # Hatching above support
    for hx in np.linspace(-2.8, 2.8, 15):
        ax.plot([hx, hx + 0.3], [py, py + 0.35], color=GREY, lw=1.5)
    ax.text(0, py + 0.55, "Rigid horizontal support", ha="center", va="bottom", fontsize=15, color=INK)

    # Pivot point
    ax.plot(px, py, 'o', color=INK, markersize=6, zorder=5)

    # Positions
    # Center (equilibrium)
    x0, y0 = px, py - L
    # Left (-A)
    x_l, y_l = px - L * np.sin(theta_rad), py - L * np.cos(theta_rad)
    # Right (+A)
    x_r, y_r = px + L * np.sin(theta_rad), py - L * np.cos(theta_rad)

    # Arc path of oscillation
    angles_arc = np.linspace(-theta_rad * 1.15, theta_rad * 1.15, 100)
    arc_x = px + L * np.sin(angles_arc)
    arc_y = py - L * np.cos(angles_arc)
    ax.plot(arc_x, arc_y, color=GREY, linestyle=":", lw=1.5, zorder=1)

    # Angle arc and label theta at pivot
    arc_radius = 1.4
    theta_arc = patches.Arc((px, py), 2 * arc_radius, 2 * arc_radius,
                            angle=270 - theta_deg, theta1=0, theta2=2 * theta_deg,
                            color=INK, lw=1.5)
    ax.add_patch(theta_arc)
    ax.text(px - 0.28, py - arc_radius - 0.2, r"$\theta$", fontsize=16, color=INK, ha="center")
    ax.text(px + 0.28, py - arc_radius - 0.2, r"$\theta$", fontsize=16, color=INK, ha="center")

    # Strings
    # Left string (dashed)
    ax.plot([px, x_l], [py, y_l], color=DEEP["blue"], lw=2, linestyle="--", zorder=2)
    # Right string (dashed)
    ax.plot([px, x_r], [py, y_r], color=DEEP["blue"], lw=2, linestyle="--", zorder=2)
    # Center string (solid)
    ax.plot([px, x0], [py, y0], color=INK, lw=2.5, zorder=2)

    # String length label 'l'
    mid_x, mid_y = (px + x_l) / 2.0, (py + y_l) / 2.0
    ax.text(mid_x - 0.35, mid_y, "String of\nlength 'l'", fontsize=14, color=INK,
            ha="right", va="center", bbox=dict(fc="white", ec="none", pad=2))

    # Bobs
    # Left bob (dashed)
    bob_l = patches.Circle((x_l, y_l), r_bob, facecolor=CREAM, edgecolor=DEEP["blue"],
                           linestyle="--", lw=2, zorder=3)
    ax.add_patch(bob_l)

    # Right bob (dashed)
    bob_r = patches.Circle((x_r, y_r), r_bob, facecolor=CREAM, edgecolor=DEEP["blue"],
                           linestyle="--", lw=2, zorder=3)
    ax.add_patch(bob_r)

    # Center bob (solid)
    bob_c = patches.Circle((x0, y0), r_bob, facecolor=BLUE, edgecolor=INK,
                           lw=2.5, zorder=4)
    ax.add_patch(bob_c)

    # Restoring force arrows at extremes pointing tangentially along the arc back towards the central equilibrium
    arrow_len = 1.3
    tx_l, ty_l = np.cos(theta_rad), -np.sin(theta_rad)
    start_xl = x_l + (r_bob + 0.1) * tx_l
    start_yl = y_l + (r_bob + 0.1) * ty_l
    ax.annotate("", xy=(start_xl + arrow_len * tx_l, start_yl + arrow_len * ty_l),
                xytext=(start_xl, start_yl),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, mutation_scale=18))
    # Place text to the outside of the bob to avoid overlapping the central string
    ax.text(x_l - 0.1, y_l + 0.6, "Restoring force", fontsize=14, color=DEEP["orange"],
            ha="right", va="center", weight="bold", bbox=dict(fc="white", ec="none", pad=1))

    tx_r, ty_r = -np.cos(theta_rad), -np.sin(theta_rad)
    start_xr = x_r + (r_bob + 0.1) * tx_r
    start_yr = y_r + (r_bob + 0.1) * ty_r
    ax.annotate("", xy=(start_xr + arrow_len * tx_r, start_yr + arrow_len * ty_r),
                xytext=(start_xr, start_yr),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, mutation_scale=18))
    # Place text to the outside of the bob to avoid overlapping the central string
    ax.text(x_r + 0.1, y_r + 0.6, "Restoring force", fontsize=14, color=DEEP["orange"],
            ha="left", va="center", weight="bold", bbox=dict(fc="white", ec="none", pad=1))

    # Position labels along the bottom
    label_y = y0 - 1.25
    # Dashed guide lines down to labels
    for x_pos in [x_l, x0, x_r]:
        ax.plot([x_pos, x_pos], [y0 - r_bob, label_y + 0.35], color=GREY, linestyle=":", lw=1.2)

    ax.text(x_l, label_y, "x = -A\n(Maximum\ndisplacement)", ha="center", va="top",
            fontsize=14, color=INK)
    ax.text(x0, label_y, "x = 0\n(Central\nequilibrium)", ha="center", va="top",
            fontsize=14, color=INK, weight="bold")
    ax.text(x_r, label_y, "x = +A\n(Maximum\ndisplacement)", ha="center", va="top",
            fontsize=14, color=INK)

    # Title
    ax.text(0, 1.8, "Simple Pendulum undergoing S.H.M.", ha="center", va="center",
            fontsize=18, color=INK, weight="bold")

    save(fig, out)
