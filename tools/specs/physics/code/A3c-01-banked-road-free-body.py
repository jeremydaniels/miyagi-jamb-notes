from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 7.5)

    # Angle of banked road
    theta_deg = 26
    theta = np.radians(theta_deg)

    # Road wedge coordinates
    road_origin = np.array([2.2, 1.0])
    road_length = 6.8
    road_end = road_origin + road_length * np.array([np.cos(theta), np.sin(theta)])
    ground_end = np.array([road_origin[0] + road_length * np.cos(theta), road_origin[1]])

    # Horizontal ground line
    ax.plot([0.5, ground_end[0] + 0.3], [road_origin[1], road_origin[1]],
            color=GREY, lw=2, linestyle="--")

    # Wedge under the road
    wedge_poly = np.array([
        road_origin,
        road_end,
        ground_end
    ])
    ax.add_patch(patches.Polygon(wedge_poly, closed=True, facecolor=CREAM, edgecolor="none", alpha=0.55))

    # Banked road surface line
    ax.plot([road_origin[0], road_end[0]], [road_origin[1], road_end[1]],
            color=INK, lw=3.5)

    # Theta arc at base of incline
    arc_rad = 1.6
    arc_angles = np.linspace(0, theta, 40)
    ax.plot(road_origin[0] + arc_rad * np.cos(arc_angles),
            road_origin[1] + arc_rad * np.sin(arc_angles), color=INK, lw=2)
    ax.text(road_origin[0] + 1.95 * np.cos(theta / 2),
            road_origin[1] + 1.95 * np.sin(theta / 2),
            r"$\theta$", fontsize=18, color=INK, va="center", ha="center")

    # Car position on slope
    s_car = 3.6
    p_road = road_origin + s_car * np.array([np.cos(theta), np.sin(theta)])

    # Unit vectors
    u_tangent = np.array([np.cos(theta), np.sin(theta)])
    u_normal = np.array([-np.sin(theta), np.cos(theta)])

    # Center of mass of the car
    h_com = 0.65
    com = p_road + h_com * u_normal

    # Car geometry (rear cross-section view)
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    # Wheels
    wheel_w, wheel_h = 0.26, 0.36
    for offset in [-0.7, 0.7]:
        wheel_c = com + offset * u_tangent - 0.45 * u_normal
        w_corners = np.array([
            [-wheel_w / 2, -wheel_h / 2],
            [wheel_w / 2, -wheel_h / 2],
            [wheel_w / 2, wheel_h / 2],
            [-wheel_w / 2, wheel_h / 2]
        ])
        w_rot = (R @ w_corners.T).T + wheel_c
        ax.add_patch(patches.Polygon(w_rot, closed=True, facecolor=INK, edgecolor=INK, lw=1.5, zorder=3))

    # Car lower body
    body_w, body_h = 1.9, 0.65
    b_corners = np.array([
        [-body_w / 2, -body_h / 2],
        [body_w / 2, -body_h / 2],
        [body_w / 2, body_h / 2],
        [-body_w / 2, body_h / 2]
    ])
    b_rot = (R @ b_corners.T).T + com
    ax.add_patch(patches.Polygon(b_rot, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2, zorder=4))

    # Car cabin / roof
    roof_w_bot, roof_w_top, roof_h = 1.4, 1.0, 0.45
    roof_corners = np.array([
        [-roof_w_bot / 2, body_h / 2],
        [roof_w_bot / 2, body_h / 2],
        [roof_w_top / 2, body_h / 2 + roof_h],
        [-roof_w_top / 2, body_h / 2 + roof_h]
    ])
    roof_rot = (R @ roof_corners.T).T + com
    ax.add_patch(patches.Polygon(roof_rot, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2, zorder=4))

    # Rear window
    win_w_bot, win_w_top, win_h = 1.15, 0.85, 0.32
    win_corners = np.array([
        [-win_w_bot / 2, body_h / 2 + 0.05],
        [win_w_bot / 2, body_h / 2 + 0.05],
        [win_w_top / 2, body_h / 2 + 0.05 + win_h],
        [-win_w_top / 2, body_h / 2 + 0.05 + win_h]
    ])
    win_rot = (R @ win_corners.T).T + com
    ax.add_patch(patches.Polygon(win_rot, closed=True, facecolor="white", edgecolor=DEEP["blue"], lw=1.5, zorder=5))

    # Tail lights
    for offset in [-0.7, 0.7]:
        tl_c = com + offset * u_tangent + 0.02 * u_normal
        tl_corners = np.array([
            [-0.14, -0.07], [0.14, -0.07], [0.14, 0.07], [-0.14, 0.07]
        ])
        tl_rot = (R @ tl_corners.T).T + tl_c
        ax.add_patch(patches.Polygon(tl_rot, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5, zorder=5))

    # Centre of mass dot
    ax.plot(com[0], com[1], "o", color=INK, markersize=6.5, zorder=6)

    # --- FORCES ---
    N_mag = 3.3
    Ny = N_mag * np.cos(theta)
    Nx = N_mag * np.sin(theta)
    mg_mag = Ny  # Equilibrium in vertical direction

    # 1. Weight mg downwards
    p_mg_end = np.array([com[0], com[1] - mg_mag])
    ax.annotate("", xy=p_mg_end, xytext=com,
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.2, mutation_scale=22), zorder=6)
    ax.text(com[0] + 0.25, com[1] - mg_mag * 0.65, r"$mg$ (weight)", fontsize=16, color=INK,
            va="center", bbox=dict(fc="white", ec="none", pad=2), zorder=10)

    # 2. Normal reaction N (perpendicular to road)
    N_vec = com + N_mag * u_normal
    ax.annotate("", xy=(N_vec[0], N_vec[1]), xytext=(com[0], com[1]),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3.2, mutation_scale=22), zorder=6)
    
    # Label correctly attached to the Normal reaction vector
    ax.annotate(r"$N$ (Normal reaction)",
                xy=(N_vec[0], N_vec[1]),
                xytext=(N_vec[0] - 0.2, N_vec[1] + 0.5),
                fontsize=16, color=INK, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=2), zorder=10)

    # 3. Components of N
    # Vertical upward component: N cos(theta)
    p_vert_end = np.array([com[0], com[1] + Ny])
    ax.annotate("", xy=p_vert_end, xytext=com,
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, ls="--", mutation_scale=18), zorder=6)
    ax.text(com[0] + 0.25, com[1] + Ny * 0.8, r"$N \cos\theta$", fontsize=16, color=INK,
            va="center", bbox=dict(fc="white", ec="none", pad=2), zorder=10)

    # Horizontal inward component: N sin(theta) pointing towards curve centre
    p_horiz_end = np.array([com[0] - Nx, com[1]])
    ax.annotate("", xy=p_horiz_end, xytext=com,
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3.2, mutation_scale=22), zorder=6)
    
    # Label for N sin theta: placed with a high zorder below the horizontal line so it is perfectly readable
    ax.text(com[0] - Nx / 2, com[1] - 0.25, r"$N \sin\theta$", fontsize=16, color=INK,
            ha="center", va="top", bbox=dict(fc="white", ec="none", pad=2), zorder=10)

    # Label for Centripetal Force: positioned clearly at the arrow tip pointing inwards
    ax.annotate("Centripetal Force\n(towards centre of curve)",
                xy=(p_horiz_end[0], p_horiz_end[1]),
                xytext=(p_horiz_end[0] - 0.7, p_horiz_end[1] - 1.1),
                fontsize=14, color=INK, ha="right", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"), zorder=10)

    # Dashed rectangle completing resolution triangle/box
    ax.plot([p_horiz_end[0], N_vec[0]], [p_horiz_end[1], N_vec[1]], color=GREY, linestyle=":", lw=1.8, zorder=2)
    ax.plot([p_vert_end[0], N_vec[0]], [p_vert_end[1], N_vec[1]], color=GREY, linestyle=":", lw=1.8, zorder=2)

    # Angle theta between vertical and Normal reaction
    phi_rad = 1.35
    phi_angles = np.linspace(np.pi / 2, np.pi / 2 + theta, 30)
    ax.plot(com[0] + phi_rad * np.cos(phi_angles),
            com[1] + phi_rad * np.sin(phi_angles), color=INK, lw=1.8, zorder=6)
    ax.text(com[0] - 0.35, com[1] + 1.6, r"$\theta$", fontsize=16, color=INK, ha="center", va="center", zorder=10)

    save(fig, out)
