from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 5.5)
    
    axes = [fig.add_subplot(1, 3, i + 1) for i in range(3)]
    
    r = 1.0
    circle_color = GREY
    
    # Helper to draw an interior angle arc between two vectors from a vertex
    def draw_angle_arc(ax, vertex, p_start, p_end, radius, color, lw=1.8):
        v1 = p_start - vertex
        v2 = p_end - vertex
        ang1 = np.degrees(np.arctan2(v1[1], v1[0])) % 360
        ang2 = np.degrees(np.arctan2(v2[1], v2[0])) % 360
        # Counterclockwise sweep from ang1 to ang2
        sweep = (ang2 - ang1) % 360
        if sweep > 180:
            # Swap so we draw the interior (smaller) arc
            ang1, ang2 = ang2, (ang2 + (360 - sweep)) % 360
        else:
            ang2 = ang1 + sweep
        arc = patches.Arc(vertex, 2 * radius, 2 * radius, angle=0,
                          theta1=ang1, theta2=ang2, color=color, lw=lw)
        ax.add_patch(arc)
        # Return angle bisector direction (radians)
        mid_ang = np.radians((ang1 + ang2) / 2.0)
        return np.array([np.cos(mid_ang), np.sin(mid_ang)])

    # ------------------ Circle 1: Angle at Centre = 2x ------------------
    ax1 = axes[0]
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_xlim(-1.45, 1.45)
    ax1.set_ylim(-1.4, 1.45)
    
    circle1 = plt.Circle((0, 0), r, fill=False, color=circle_color, lw=2.5)
    ax1.add_patch(circle1)
    
    ang_A = np.radians(210)
    ang_B = np.radians(330)
    ang_P = np.radians(95)
    
    A1 = np.array([r * np.cos(ang_A), r * np.sin(ang_A)])
    B1 = np.array([r * np.cos(ang_B), r * np.sin(ang_B)])
    P1 = np.array([r * np.cos(ang_P), r * np.sin(ang_P)])
    O1 = np.array([0.0, 0.0])
    
    # Radii lines A-O and B-O
    ax1.plot([A1[0], O1[0], B1[0]], [A1[1], O1[1], B1[1]], color=DEEP["blue"], lw=2)
    # Inscribed angle lines A-P and B-P
    ax1.plot([A1[0], P1[0], B1[0]], [A1[1], P1[1], B1[1]], color=DEEP["pink"], lw=2)
    
    # Highlight arc AB at the bottom
    arc_t = np.linspace(ang_A, ang_B, 100)
    ax1.plot(r * np.cos(arc_t), r * np.sin(arc_t), color=DEEP["green"], lw=3.5)
    
    # Angle at O (facing bottom arc AB)
    wedge_O = patches.Arc((0, 0), 0.5, 0.5, angle=0, theta1=210, theta2=330, color=DEEP["blue"], lw=1.8)
    ax1.add_patch(wedge_O)
    ax1.text(0, -0.42, "2x", fontsize=15, ha="center", va="center", color=DEEP["blue"], fontweight="bold",
             bbox=dict(fc="white", ec="none", pad=1))
    
    # Angle at P (interior)
    bis_P = draw_angle_arc(ax1, P1, A1, B1, 0.32, DEEP["pink"], lw=1.8)
    label_P_pos = P1 + 0.5 * bis_P
    ax1.text(label_P_pos[0], label_P_pos[1], "x", fontsize=15, ha="center", va="center",
             color=DEEP["pink"], fontweight="bold")
    
    # Center dot O
    ax1.plot(0, 0, 'o', color=INK, markersize=4.5)
    ax1.text(0.12, 0.1, "O", fontsize=15, color=INK)
    
    # Labels A, B, P
    ax1.text(A1[0] - 0.12, A1[1] - 0.12, "A", fontsize=15, ha="right", va="top", color=INK)
    ax1.text(B1[0] + 0.12, B1[1] - 0.12, "B", fontsize=15, ha="left", va="top", color=INK)
    ax1.text(P1[0], P1[1] + 0.12, "P", fontsize=15, ha="center", va="bottom", color=INK)
    
    ax1.set_title("Angle at Centre Theorem", fontsize=15, pad=16, color=INK, fontweight="bold")

    # ------------------ Circle 2: Angles in the Same Segment ------------------
    ax2 = axes[1]
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_xlim(-1.45, 1.45)
    ax2.set_ylim(-1.4, 1.45)
    
    circle2 = plt.Circle((0, 0), r, fill=False, color=circle_color, lw=2.5)
    ax2.add_patch(circle2)
    
    ang_C = np.radians(215)
    ang_D = np.radians(325)
    ang_P2 = np.radians(130)
    ang_Q2 = np.radians(50)
    
    C = np.array([r * np.cos(ang_C), r * np.sin(ang_C)])
    D = np.array([r * np.cos(ang_D), r * np.sin(ang_D)])
    P2 = np.array([r * np.cos(ang_P2), r * np.sin(ang_P2)])
    Q2 = np.array([r * np.cos(ang_Q2), r * np.sin(ang_Q2)])
    
    # Chord CD
    ax2.plot([C[0], D[0]], [C[1], D[1]], color=DEEP["green"], lw=2.5, ls="--")
    
    # Lines C-P2-D
    ax2.plot([C[0], P2[0], D[0]], [C[1], P2[1], D[1]], color=DEEP["blue"], lw=2)
    # Lines C-Q2-D
    ax2.plot([C[0], Q2[0], D[0]], [C[1], Q2[1], D[1]], color=DEEP["orange"], lw=2)
    
    # Interior angle arc at P
    bis_P2 = draw_angle_arc(ax2, P2, C, D, 0.3, DEEP["blue"], lw=1.8)
    pos_theta_P = P2 + 0.48 * bis_P2
    ax2.text(pos_theta_P[0], pos_theta_P[1], r"$\theta$", fontsize=15, ha="center", va="center",
             color=DEEP["blue"], fontweight="bold")
    
    # Interior angle arc at Q
    bis_Q2 = draw_angle_arc(ax2, Q2, C, D, 0.3, DEEP["orange"], lw=1.8)
    pos_theta_Q = Q2 + 0.48 * bis_Q2
    ax2.text(pos_theta_Q[0], pos_theta_Q[1], r"$\theta$", fontsize=15, ha="center", va="center",
             color=DEEP["orange"], fontweight="bold")
    
    # Labels C, D, P, Q placed clearly outside the circle
    ax2.text(C[0] - 0.12, C[1] - 0.12, "C", fontsize=15, ha="right", va="top", color=INK)
    ax2.text(D[0] + 0.12, D[1] - 0.12, "D", fontsize=15, ha="left", va="top", color=INK)
    ax2.text(P2[0] - 0.12, P2[1] + 0.12, "P", fontsize=15, ha="right", va="bottom", color=INK)
    ax2.text(Q2[0] + 0.12, Q2[1] + 0.12, "Q", fontsize=15, ha="left", va="bottom", color=INK)
    
    ax2.set_title("Angles in Same Segment", fontsize=15, pad=16, color=INK, fontweight="bold")

    # ------------------ Circle 3: Angle in a Semicircle ------------------
    ax3 = axes[2]
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_xlim(-1.45, 1.45)
    ax3.set_ylim(-1.4, 1.45)
    
    circle3 = plt.Circle((0, 0), r, fill=False, color=circle_color, lw=2.5)
    ax3.add_patch(circle3)
    
    X = np.array([-1.0, 0.0])
    Y = np.array([1.0, 0.0])
    
    ang_Z = np.radians(65)
    Z = np.array([r * np.cos(ang_Z), r * np.sin(ang_Z)])
    
    # Diameter XY
    ax3.plot([X[0], Y[0]], [X[1], Y[1]], color=INK, lw=2)
    # Center dot O
    ax3.plot(0, 0, 'o', color=INK, markersize=4.5)
    ax3.text(0, -0.18, "O", fontsize=15, ha="center", va="top", color=INK)
    
    # Lines X-Z and Y-Z
    ax3.plot([X[0], Z[0]], [X[1], Z[1]], color=DEEP["blue"], lw=2)
    ax3.plot([Y[0], Z[0]], [Y[1], Z[1]], color=DEEP["blue"], lw=2)
    
    # Square right-angle symbol at Z
    uZX = (X - Z) / np.linalg.norm(X - Z)
    uZY = (Y - Z) / np.linalg.norm(Y - Z)
    s = 0.16
    p1 = Z + s * uZX
    p2 = Z + s * uZX + s * uZY
    p3 = Z + s * uZY
    ax3.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color=DEEP["pink"], lw=2)
    
    # Labels X, Y, Z
    ax3.text(X[0] - 0.15, X[1], "X", fontsize=15, ha="right", va="center", color=INK)
    ax3.text(Y[0] + 0.15, Y[1], "Y", fontsize=15, ha="left", va="center", color=INK)
    ax3.text(Z[0] + 0.08, Z[1] + 0.12, "Z", fontsize=15, ha="left", va="bottom", color=INK)
    
    ax3.set_title("Angle in a Semicircle", fontsize=15, pad=16, color=INK, fontweight="bold")
    
    plt.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.06, wspace=0.15)
    save(fig, out)
