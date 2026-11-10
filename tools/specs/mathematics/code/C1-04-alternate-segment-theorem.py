from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.5, 1.7)

    # Circle centered at origin with radius R = 1
    r = 1.0
    circle = patches.Circle((0, 0), r, fill=False, edgecolor=INK, lw=2.2)
    ax.add_patch(circle)

    # Points on the circle
    # P is at the bottom: angle -90 degrees (-pi/2)
    p_angle = -np.pi / 2
    P = np.array([0.0, -1.0])

    # Q is in the lower-right/mid-right, R is in the upper-left
    q_angle = np.deg2rad(25)
    r_angle = np.deg2rad(140)

    Q = np.array([r * np.cos(q_angle), r * np.sin(q_angle)])
    R = np.array([r * np.cos(r_angle), r * np.sin(r_angle)])

    # Tangent line at P: P is (0, -1), tangent is horizontal line y = -1
    tangent_x = np.array([-1.5, 1.5])
    tangent_y = np.array([-1.0, -1.0])
    ax.plot(tangent_x, tangent_y, color=DEEP["blue"], lw=2.5, zorder=2)

    # Triangle PQR
    triangle_coords = np.array([P, Q, R, P])
    poly = patches.Polygon(np.array([P, Q, R]), closed=True, facecolor=CREAM, edgecolor="none", alpha=0.5, zorder=1)
    ax.add_patch(poly)
    ax.plot(triangle_coords[:, 0], triangle_coords[:, 1], color=INK, lw=2.2, zorder=3)

    # Angle arc at P between tangent (pointing right, (1, 0)) and chord PQ
    # Vector PQ:
    v_PQ = Q - P
    angle_PQ = np.arctan2(v_PQ[1], v_PQ[0])  # in radians, relative to positive x-axis
    # Tangent to the right has angle 0
    arc_P = patches.Arc(P, 0.5, 0.5, angle=0, theta1=0, theta2=np.rad2deg(angle_PQ),
                        color=DEEP["pink"], lw=2.5, zorder=4)
    ax.add_patch(arc_P)

    # Angle arc at R between RP and RQ
    v_RP = P - R
    v_RQ = Q - R
    angle_RP = np.rad2deg(np.arctan2(v_RP[1], v_RP[0]))
    angle_RQ = np.rad2deg(np.arctan2(v_RQ[1], v_RQ[0]))
    # Arc from RP to RQ (counterclockwise or properly oriented)
    theta1 = min(angle_RP, angle_RQ)
    theta2 = max(angle_RP, angle_RQ)
    # Ensure inner angle is < 180
    if theta2 - theta1 > 180:
        theta1, theta2 = theta2, theta1 + 360
    arc_R = patches.Arc(R, 0.45, 0.45, angle=0, theta1=theta1, theta2=theta2,
                        color=DEEP["pink"], lw=2.5, zorder=4)
    ax.add_patch(arc_R)

    # Angle labels "x"
    # Label for angle at P
    mid_angle_P = angle_PQ / 2.0
    label_P_pos = P + 0.38 * np.array([np.cos(mid_angle_P), np.sin(mid_angle_P)])
    ax.text(label_P_pos[0], label_P_pos[1], r"$x$", fontsize=16, color=DEEP["pink"],
            ha="center", va="center", weight="bold")

    # Label for angle at R
    mid_angle_R = np.deg2rad((theta1 + theta2) / 2.0)
    label_R_pos = R + 0.35 * np.array([np.cos(mid_angle_R), np.sin(mid_angle_R)])
    ax.text(label_R_pos[0], label_R_pos[1], r"$x$", fontsize=16, color=DEEP["pink"],
            ha="center", va="center", weight="bold")

    # Vertex points and labels
    ax.plot([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], 'o', color=INK, markersize=5, zorder=5)

    ax.text(P[0], P[1] - 0.22, "P", fontsize=16, color=INK, ha="center", va="top")
    ax.text(Q[0] + 0.12, Q[1] + 0.05, "Q", fontsize=16, color=INK, ha="left", va="center")
    ax.text(R[0] - 0.12, R[1] + 0.08, "R", fontsize=16, color=INK, ha="right", va="bottom")

    # Tangent line label
    ax.text(1.4, -1.18, "tangent", fontsize=14, color=DEEP["blue"], ha="right", va="top",
            bbox=dict(fc="white", ec="none", pad=1))

    # Theorem title
    ax.set_title("Alternate Segment Theorem", fontsize=16, color=INK, pad=18)

    save(fig, out)
