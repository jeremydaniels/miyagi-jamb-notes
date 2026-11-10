from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 8.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Equilateral triangular prism vertices
    A = np.array([5.0, 7.2])
    B = np.array([1.5, 1.5])
    C = np.array([8.5, 1.5])

    # Draw prism body
    prism = patches.Polygon([A, B, C], closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, alpha=0.35)
    ax.add_patch(prism)
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], color=DEEP["blue"], lw=2.5)

    # Intersection points on faces
    # Left face AB: goes from B to A
    P = B + 0.45 * (A - B)  # (3.075, 4.065)
    # Right face AC: symmetric point on AC
    Q = np.array([10.0 - P[0], P[1]])  # (6.925, 4.065)

    # Face outward normals
    v_AB = A - B
    n1 = np.array([-v_AB[1], v_AB[0]])
    n1 = n1 / np.linalg.norm(n1)  # outward normal to left face

    v_AC = C - A
    n2 = np.array([-v_AC[1], v_AC[0]])
    n2 = n2 / np.linalg.norm(n2)  # outward normal to right face

    # Light rays geometry:
    # Let ray inside prism be horizontal from P to Q: dir_internal = (1, 0)
    # Incident ray strikes P from the air:
    # Choose realistic angle: n1 has angle ~ 148.28 degrees.
    # We want incident ray direction to be at angle ~ 25 degrees (coming from bottom-left).
    # Then incident vector into P is dir_inc:
    dir_inc = np.array([np.cos(np.radians(24)), np.sin(np.radians(24))])
    S = P - dir_inc * 3.4

    # Emergent ray leaves Q, bends symmetrically downwards:
    dir_eme = np.array([np.cos(np.radians(-24)), np.sin(np.radians(-24))])
    T = Q + dir_eme * 3.4

    # Normals: draw dashed lines
    norm_len = 2.0
    ax.plot([P[0] + n1[0]*norm_len, P[0] - n1[0]*norm_len],
            [P[1] + n1[1]*norm_len, P[1] - n1[1]*norm_len],
            color=GREY, ls="--", lw=1.8)
    ax.plot([Q[0] + n2[0]*norm_len, Q[0] - n2[0]*norm_len],
            [Q[1] + n2[1]*norm_len, Q[1] - n2[1]*norm_len],
            color=GREY, ls="--", lw=1.8)

    # Intersection of incident ray extended forward and emergent ray extended backward:
    # P + t * dir_inc = Q - u * dir_eme
    # By symmetry, intersection R_inter is at x = 5.0
    t_inter = (5.0 - P[0]) / dir_inc[0]
    R_inter = P + t_inter * dir_inc

    # Dotted extensions:
    # 1. Incident ray forward beyond R_inter
    ax.plot([P[0], R_inter[0] + dir_inc[0] * 1.5],
            [P[1], R_inter[1] + dir_inc[1] * 1.5],
            color=DEEP["pink"], ls=":", lw=2.2)
    # 2. Emergent ray straight backward from Q through R_inter
    # Emergent ray is along line Q + s * dir_eme. Backward extension is towards R_inter:
    ax.plot([Q[0], R_inter[0]], [Q[1], R_inter[1]],
            color=DEEP["pink"], ls=":", lw=2.2)

    # Draw solid light rays
    ax.plot([S[0], P[0]], [S[1], P[1]], color=DEEP["orange"], lw=2.8)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color=DEEP["orange"], lw=2.8)
    ax.plot([Q[0], T[0]], [Q[1], T[1]], color=DEEP["orange"], lw=2.8)

    # Ray arrowheads (centered on segments)
    def add_arrow(p1, p2):
        mid = 0.52 * p1 + 0.48 * p2
        d = (p2 - p1) / np.linalg.norm(p2 - p1)
        ax.annotate("", xy=mid + d * 0.15, xytext=mid - d * 0.15,
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18))

    add_arrow(S, P)
    add_arrow(P, Q)
    add_arrow(Q, T)

    # Robust arc drawer using explicit points to avoid matplotlib Arc angle/wrap bugs
    def draw_arc_explicit(center, r, theta_start, theta_end, color=INK, lw=1.6):
        # normalize so theta_end > theta_start and range is < 360
        t1 = theta_start % 360
        t2 = theta_end % 360
        if t2 < t1:
            t2 += 360
        thetas = np.linspace(np.radians(t1), np.radians(t2), 60)
        xs = center[0] + r * np.cos(thetas)
        ys = center[1] + r * np.sin(thetas)
        ax.plot(xs, ys, color=color, lw=lw)

    # 1. Apex Angle A
    # Edges from A point to B and C
    ang_AB = np.degrees(np.arctan2(B[1] - A[1], B[0] - A[0])) % 360  # ~ 238°
    ang_AC = np.degrees(np.arctan2(C[1] - A[1], C[0] - A[0])) % 360  # ~ 301°
    draw_arc_explicit(A, 0.9, ang_AB, ang_AC, color=INK, lw=1.6)
    ax.text(A[0], A[1] - 1.3, "$A$", fontsize=16, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # 2. Angle of Incidence i (outside prism, between incoming ray S->P and outward normal n1)
    # Direction pointing back along ray: P -> S
    ang_ray_in = np.degrees(np.arctan2(S[1] - P[1], S[0] - P[0])) % 360  # ~ 204°
    ang_n1 = np.degrees(np.arctan2(n1[1], n1[0])) % 360                   # ~ 148°
    # Sweep from ang_n1 to ang_ray_in
    draw_arc_explicit(P, 1.2, ang_n1, ang_ray_in, color=INK, lw=1.6)
    mid_i = np.radians((ang_n1 + ang_ray_in) / 2.0)
    ax.text(P[0] + 1.6 * np.cos(mid_i), P[1] + 1.6 * np.sin(mid_i), "$i$",
            fontsize=16, ha="center", va="center", color=INK)

    # 3. Angle of Emergence e (outside prism, between emergent ray Q->T and outward normal n2)
    ang_n2 = np.degrees(np.arctan2(n2[1], n2[0])) % 360                   # ~ 32°
    ang_ray_out = np.degrees(np.arctan2(T[1] - Q[1], T[0] - Q[0])) % 360 # ~ 336°
    # Sweep from ang_ray_out to ang_n2 + 360 (counter-clockwise)
    draw_arc_explicit(Q, 1.2, ang_ray_out, ang_n2, color=INK, lw=1.6)
    mid_e = np.radians((ang_ray_out + (ang_n2 + 360)) / 2.0)
    ax.text(Q[0] + 1.6 * np.cos(mid_e), Q[1] + 1.6 * np.sin(mid_e), "$e$",
            fontsize=16, ha="center", va="center", color=INK)

    # 4. Angle of Deviation D (at intersection point R_inter)
    # Between extended incident ray (angle ~ 24°) and emergent ray direction (angle ~ -24° = 336°)
    ang_fwd_inc = np.degrees(np.arctan2(dir_inc[1], dir_inc[0])) % 360
    ang_fwd_eme = np.degrees(np.arctan2(dir_eme[1], dir_eme[0])) % 360
    # From ang_fwd_eme (336°) to ang_fwd_inc (24° + 360° = 384°)
    draw_arc_explicit(R_inter, 1.1, ang_fwd_eme, ang_fwd_inc, color=DEEP["pink"], lw=2.0)
    mid_D = np.radians((ang_fwd_eme + (ang_fwd_inc + 360)) / 2.0)
    ax.text(R_inter[0] + 1.5 * np.cos(mid_D), R_inter[1] + 1.5 * np.sin(mid_D), "$D$",
            fontsize=16, ha="center", va="center", color=DEEP["pink"],
            bbox=dict(fc="white", ec="none", pad=1))

    # Descriptive annotations
    ax.text(S[0] - 0.2, S[1] - 0.45, "Incident ray", fontsize=14, color=INK, ha="right",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax.text(T[0] + 0.2, T[1] - 0.45, "Emergent ray", fontsize=14, color=INK, ha="left",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax.text(5.0, 2.2, "Glass prism", fontsize=15, color=DEEP["blue"], ha="center", style="italic")

    # Dotted lines label
    ax.text(R_inter[0], R_inter[1] + 0.8, "Angle of deviation ($D$)", fontsize=14,
            color=DEEP["pink"], ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
