from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)

    # Circle parameters
    r = 1.0
    theta_deg = 80
    theta = np.radians(theta_deg)

    # Angles for chord endpoints (oriented symmetrically at top)
    alpha1 = np.pi / 2 - theta / 2
    alpha2 = np.pi / 2 + theta / 2

    # Coordinates
    O = np.array([0.0, 0.0])
    A = np.array([r * np.cos(alpha2), r * np.sin(alpha2)])  # Left endpoint
    B = np.array([r * np.cos(alpha1), r * np.sin(alpha1)])  # Right endpoint
    M = (A + B) / 2  # Midpoint of chord

    # Draw full circle
    circle_theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r * np.cos(circle_theta), r * np.sin(circle_theta), color=GREY, lw=2.5)

    # Draw shaded sector / triangle subtly to give textbook feel
    tri_poly = plt.Polygon([O, A, B], facecolor=CREAM, edgecolor="none", alpha=0.5)
    ax.add_patch(tri_poly)

    # Radii
    ax.plot([O[0], A[0]], [O[1], A[1]], color=DEEP["blue"], lw=2.5)
    ax.plot([O[0], B[0]], [O[1], B[1]], color=DEEP["blue"], lw=2.5)

    # Chord
    ax.plot([A[0], B[0]], [A[1], B[1]], color=DEEP["pink"], lw=3.0)

    # Perpendicular bisector from centre to chord (O to M)
    ax.plot([O[0], M[0]], [O[1], M[1]], color=DEEP["green"], lw=2.5, linestyle="--")

    # Centre point
    ax.plot(0, 0, marker="o", color=INK, markersize=5)
    ax.text(0, -0.08, "O", fontsize=15, ha="center", va="top", color=INK)

    # Right-angle symbols at M
    sq_size = 0.06
    # Left right-angle square
    sq1 = plt.Polygon(
        [
            [M[0], M[1]],
            [M[0] - sq_size, M[1]],
            [M[0] - sq_size, M[1] - sq_size],
            [M[0], M[1] - sq_size],
        ],
        fill=False,
        edgecolor=INK,
        lw=1.5,
    )
    ax.add_patch(sq1)

    # Arc for theta
    arc_rad = 0.25
    arc_angles = np.linspace(alpha1, alpha2, 100)
    ax.plot(arc_rad * np.cos(arc_angles), arc_rad * np.sin(arc_angles), color=INK, lw=1.5)

    # Label: "theta"
    ax.text(
        0,
        arc_rad + 0.08,
        r"$\theta$",
        fontsize=16,
        ha="center",
        va="bottom",
        color=INK,
        bbox=dict(fc="white", ec="none", pad=1),
    )

    # Label: "r" on both radii
    pos_r_left = (O + A) / 2
    pos_r_right = (O + B) / 2
    ax.text(
        pos_r_left[0] - 0.07,
        pos_r_left[1],
        "r",
        fontsize=16,
        ha="right",
        va="center",
        color=DEEP["blue"],
        bbox=dict(fc="white", ec="none", pad=1),
    )
    ax.text(
        pos_r_right[0] + 0.07,
        pos_r_right[1],
        "r",
        fontsize=16,
        ha="left",
        va="center",
        color=DEEP["blue"],
        bbox=dict(fc="white", ec="none", pad=1),
    )

    # Label: "chord"
    ax.text(
        0,
        A[1] + 0.08,
        "chord",
        fontsize=16,
        ha="center",
        va="bottom",
        color=DEEP["pink"],
        fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=1),
    )

    save(fig, out)
