from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 8)

    # Coordinates
    A = np.array([1.5, 2.0])
    B = np.array([6.5, 2.0])
    M = (A + B) / 2.0  # (4.0, 2.0)
    P = np.array([4.0, 6.2])

    # Perpendicular bisector (dotted straight line)
    line_y_low = 0.5
    line_y_high = 7.2
    ax.plot([M[0], M[0]], [line_y_low, line_y_high], linestyle=":", color=DEEP["blue"], lw=2.5, zorder=2)

    # Segment AB
    ax.plot([A[0], B[0]], [A[1], B[1]], color=INK, lw=3, zorder=3)

    # Dashed lines PA and PB
    ax.plot([P[0], A[0]], [P[1], A[1]], linestyle="--", color=DEEP["orange"], lw=2.5, zorder=2)
    ax.plot([P[0], B[0]], [P[1], B[1]], linestyle="--", color=DEEP["orange"], lw=2.5, zorder=2)

    # Points A, B, P
    ax.plot(A[0], A[1], marker='o', markersize=9, color=INK, zorder=5)
    ax.plot(B[0], B[1], marker='o', markersize=9, color=INK, zorder=5)
    ax.plot(P[0], P[1], marker='o', markersize=9, color=DEEP["orange"], zorder=5)

    # Labels for vertices
    ax.text(A[0] - 0.4, A[1] - 0.1, "A", fontsize=16, fontweight="bold", color=INK, ha="right", va="center")
    ax.text(B[0] + 0.4, B[1] - 0.1, "B", fontsize=16, fontweight="bold", color=INK, ha="left", va="center")
    ax.text(P[0] + 0.35, P[1] + 0.3, "P", fontsize=16, fontweight="bold", color=DEEP["orange"], ha="left", va="bottom")

    # Right-angle mark at M
    sq_size = 0.4
    ax.plot([M[0], M[0] + sq_size, M[0] + sq_size, M[0]], 
            [M[1] + sq_size, M[1] + sq_size, M[1], M[1]], 
            color=INK, lw=1.5, zorder=2)

    # Congruence tick marks on AM and MB (single tick each)
    tick_len = 0.25
    m_AM = (A + M) / 2.0
    m_MB = (M + B) / 2.0
    ax.plot([m_AM[0], m_AM[0]], [m_AM[1] - tick_len, m_AM[1] + tick_len], color=INK, lw=2, zorder=4)
    ax.plot([m_MB[0], m_MB[0]], [m_MB[1] - tick_len, m_MB[1] + tick_len], color=INK, lw=2, zorder=4)

    # Congruence double-tick marks on PA and PB to show PA = PB
    # Midpoints of PA and PB
    m_PA = (P + A) / 2.0
    m_PB = (P + B) / 2.0

    # Direction vectors perpendicular to PA and PB
    v_PA = P - A
    v_PA_perp = np.array([-v_PA[1], v_PA[0]])
    v_PA_perp = v_PA_perp / np.linalg.norm(v_PA_perp) * 0.25
    u_PA = v_PA / np.linalg.norm(v_PA) * 0.12

    v_PB = P - B
    v_PB_perp = np.array([v_PB[1], -v_PB[0]])
    v_PB_perp = v_PB_perp / np.linalg.norm(v_PB_perp) * 0.25
    u_PB = v_PB / np.linalg.norm(v_PB) * 0.12

    # Draw double ticks on PA
    for offset in [-u_PA, u_PA]:
        pt = m_PA + offset
        ax.plot([pt[0] - v_PA_perp[0], pt[0] + v_PA_perp[0]], 
                [pt[1] - v_PA_perp[1], pt[1] + v_PA_perp[1]], 
                color=DEEP["orange"], lw=2, zorder=4)

    # Draw double ticks on PB
    for offset in [-u_PB, u_PB]:
        pt = m_PB + offset
        ax.plot([pt[0] - v_PB_perp[0], pt[0] + v_PB_perp[0]], 
                [pt[1] - v_PB_perp[1], pt[1] + v_PB_perp[1]], 
                color=DEEP["orange"], lw=2, zorder=4)

    # Informative annotation/label for perpendicular bisector
    ax.text(M[0], line_y_low - 0.4, "Perpendicular bisector", fontsize=14, color=DEEP["blue"],
            ha="center", va="top", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Annotation clarifying PA = PB
    ax.text(P[0], line_y_high + 0.3, "Locus of points: PA = PB", fontsize=15, color=INK,
            ha="center", va="bottom", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY))

    save(fig, out)
