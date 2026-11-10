from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw(out):
    fig = canvas(8, 6.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Geometry setup
    # Origin O at (0, 0)
    # F1 along horizontal axis, F2 at angle theta = 50 degrees
    theta_deg = 50.0
    theta_rad = np.radians(theta_deg)
    len_F1 = 5.2
    len_F2 = 3.6

    pO = np.array([0.0, 0.0])
    pF1 = np.array([len_F1, 0.0])
    pF2 = np.array([len_F2 * np.cos(theta_rad), len_F2 * np.sin(theta_rad)])
    pR = pF1 + pF2

    # Draw dashed parallelogram sides
    ax.plot([pF1[0], pR[0]], [pF1[1], pR[1]], linestyle="--", color=GREY, lw=2.0, zorder=2)
    ax.plot([pF2[0], pR[0]], [pF2[1], pR[1]], linestyle="--", color=GREY, lw=2.0, zorder=2)

    # Helper function to draw clean vector arrows
    def draw_vector(p_start, p_end, color, lw=3.0):
        ax.annotate(
            "",
            xy=(p_end[0], p_end[1]),
            xytext=(p_start[0], p_start[1]),
            arrowprops=dict(
                arrowstyle="-|>",
                color=color,
                lw=lw,
                mutation_scale=22,
                shrinkA=0,
                shrinkB=0,
                capstyle="round"
            ),
            zorder=4
        )

    # Draw primary vectors
    draw_vector(pO, pF1, DEEP["blue"], lw=3.2)
    draw_vector(pO, pF2, DEEP["green"], lw=3.2)
    draw_vector(pO, pR, DEEP["orange"], lw=3.6)

    # Angle arc for theta between F1 and F2
    arc_radius = 1.4
    arc = Arc(
        (0, 0),
        2 * arc_radius,
        2 * arc_radius,
        angle=0,
        theta1=0,
        theta2=theta_deg,
        color=INK,
        lw=1.8,
        zorder=3
    )
    ax.add_patch(arc)

    # Theta label: placed with an arrow pointer pointing clearly to the arc,
    # positioned outside the angle sector so it never overlaps the resultant vector R
    theta_pt_angle = np.radians(theta_deg * 0.72)
    arc_target = np.array([arc_radius * np.cos(theta_pt_angle), arc_radius * np.sin(theta_pt_angle)])
    ax.annotate(
        r"$\theta$",
        xy=(arc_target[0], arc_target[1]),
        xytext=(arc_target[0] - 0.45, arc_target[1] + 0.65),
        fontsize=16,
        color=INK,
        ha="center",
        va="center",
        arrowprops=dict(
            arrowstyle="->",
            color=INK,
            lw=1.3,
            shrinkA=2,
            shrinkB=3
        ),
        bbox=dict(fc="white", ec="none", pad=1.5),
        zorder=6
    )

    # Origin point O
    ax.scatter([0], [0], color=INK, s=40, zorder=5)
    ax.text(-0.35, -0.2, "O", fontsize=16, fontweight="bold", color=INK, ha="right", va="top")

    # Labels for vectors
    # F1
    ax.text(
        len_F1 / 2, -0.45,
        r"$\mathbf{F}_1$",
        fontsize=16,
        color=DEEP["blue"],
        ha="center",
        va="top",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6
    )

    # F2
    ax.text(
        (pF2[0] / 2) - 0.45, (pF2[1] / 2) + 0.25,
        r"$\mathbf{F}_2$",
        fontsize=16,
        color=DEEP["green"],
        ha="right",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6
    )

    # Resultant R (positioned safely above the resultant line)
    mid_R = pR * 0.58
    ax.text(
        mid_R[0] - 0.25, mid_R[1] + 0.4,
        r"$\mathbf{R}$",
        fontsize=17,
        fontweight="bold",
        color=DEEP["orange"],
        ha="right",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6
    )

    # Dashed side annotations (F2 and F1 mirrored)
    mid_dashed_F2 = (pF1 + pR) / 2
    ax.text(
        mid_dashed_F2[0] + 0.35, mid_dashed_F2[1],
        r"$\mathbf{F}_2$",
        fontsize=15,
        color=GREY,
        ha="left",
        va="center",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6
    )

    mid_dashed_F1 = (pF2 + pR) / 2
    ax.text(
        mid_dashed_F1[0], mid_dashed_F1[1] + 0.35,
        r"$\mathbf{F}_1$",
        fontsize=15,
        color=GREY,
        ha="center",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6
    )

    # Title
    ax.set_title("Parallelogram Law of Vector Addition", fontsize=16, pad=18, color=INK)

    # Limits and padding
    ax.set_xlim(-1.2, pR[0] + 1.2)
    ax.set_ylim(-1.0, pR[1] + 1.0)

    save(fig, out)
