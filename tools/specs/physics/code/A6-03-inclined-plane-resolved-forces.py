from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    theta_deg = 30.0
    theta = np.radians(theta_deg)

    # Incline wedge geometry: right-angled triangle with slope rising from bottom-left to top-right
    # Vertex at (x0, y0) has angle theta between horizontal base and hypotenuse slope
    x0, y0 = 1.0, 1.0
    L = 9.0  # length along slope
    x_top = x0 + L * np.cos(theta)
    y_top = y0 + L * np.sin(theta)

    # Wedge vertices: (x0, y0) [bottom-left corner with angle theta],
    #                 (x_top, y0) [bottom-right corner with 90° right angle],
    #                 (x_top, y_top) [top-right corner]
    wedge_poly = np.array([
        [x0, y0],
        [x_top, y0],
        [x_top, y_top]
    ])

    wedge = patches.Polygon(wedge_poly, closed=True,
                            facecolor=CREAM, edgecolor=GREY, lw=2.0, zorder=1)
    ax.add_patch(wedge)

    # Ground line extending slightly past the wedge
    ax.plot([x0 - 0.6, x_top + 0.6], [y0, y0], color=GREY, lw=2.0, zorder=1)

    # Angle arc at the base-slope junction (x0, y0)
    arc_r = 1.8
    arc = patches.Arc((x0, y0), 2 * arc_r, 2 * arc_r, angle=0,
                      theta1=0, theta2=theta_deg, color=INK, lw=1.8, zorder=2)
    ax.add_patch(arc)
    ax.text(x0 + 2.2 * np.cos(theta / 2.0), y0 + 2.2 * np.sin(theta / 2.0),
            r"$\theta$", fontsize=16, color=INK, va="center", ha="center", zorder=3)

    # Right-angle indicator at bottom-right corner of wedge (x_top, y0)
    sq_size = 0.4
    ax.plot([x_top - sq_size, x_top - sq_size, x_top],
            [y0, y0 + sq_size, y0 + sq_size], color=GREY, lw=1.5, zorder=2)

    # Unit vectors: along the slope (upwards) and normal to slope (up-left)
    u_par = np.array([np.cos(theta), np.sin(theta)])
    u_perp = np.array([-np.sin(theta), np.cos(theta)])

    # Block on the incline
    d_block = 5.2
    bw, bh = 2.4, 1.4

    base_center = np.array([x0, y0]) + d_block * u_par
    cm = base_center + (bh / 2.0) * u_perp

    # Block corners
    c1 = base_center - (bw / 2.0) * u_par
    c2 = base_center + (bw / 2.0) * u_par
    c3 = c2 + bh * u_perp
    c4 = c1 + bh * u_perp

    block = patches.Polygon([c1, c2, c3, c4], closed=True,
                            facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(block)

    # Label 'm' positioned clearly near the top-corner inside the block with white circular backing
    m_pos = cm + 0.28 * bh * u_perp + 0.18 * bw * u_par
    ax.text(m_pos[0], m_pos[1], "$m$", fontsize=16, color=INK,
            ha="center", va="center", zorder=7, weight="bold",
            bbox=dict(fc="white", ec=DEEP["blue"], lw=1.2, boxstyle="circle,pad=0.25"))

    # Helper function for force arrows
    def draw_force(start, vec, color, label, ha="center", va="center", offset=(0, 0)):
        end = start + vec
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", lw=2.5, color=color, mutation_scale=20),
                    zorder=5)
        ax.text(end[0] + offset[0], end[1] + offset[1], label,
                fontsize=15, color=color, ha=ha, va=va, zorder=6,
                bbox=dict(fc="white", ec="none", pad=2.0, alpha=0.95))

    # Dot at center of mass
    ax.plot(cm[0], cm[1], 'o', color=INK, markersize=4.5, zorder=6)

    # Forces:
    # 1. Weight (mg) straight down from CM
    mg_len = 2.6
    draw_force(cm, np.array([0, -mg_len]), DEEP["orange"], r"Weight ($mg$)",
               ha="center", va="top", offset=(0, -0.2))

    # 2. Normal Reaction (R) perpendicular to surface upwards from CM
    R_len = 2.4
    draw_force(cm, R_len * u_perp, DEEP["green"], r"Normal Reaction ($R$)",
               ha="center", va="bottom", offset=(-0.25, 0.2))

    # 3. Component down the slope: mg sin theta from CM
    down_slope_len = 2.2
    draw_force(cm, -down_slope_len * u_par, DEEP["pink"], r"$mg \sin\theta$",
               ha="right", va="top", offset=(-0.2, -0.15))

    # 4. Friction (F) acting up the slope (originating at the contact surface)
    f_len = 2.3
    draw_force(base_center, f_len * u_par, DEEP["lav"], r"Friction ($F$)",
               ha="left", va="bottom", offset=(0.2, 0.15))

    # Dashed line showing normal axis into the slope for reference
    dash_norm_end = cm - 1.8 * u_perp
    ax.plot([cm[0], dash_norm_end[0]], [cm[1], dash_norm_end[1]],
            "--", color=GREY, lw=1.5, zorder=2)

    # Angle theta between mg and the inward perpendicular to plane
    inward_norm = -u_perp
    ang_inward = np.degrees(np.arctan2(inward_norm[1], inward_norm[0]))
    ang_mg = -90.0  # straight down
    theta_comp_arc = patches.Arc(cm, 1.8, 1.8, angle=0,
                                 theta1=ang_mg, theta2=ang_inward,
                                 color=INK, lw=1.3, zorder=2)
    ax.add_patch(theta_comp_arc)
    mid_ang = np.radians((ang_mg + ang_inward) / 2.0)
    ax.text(cm[0] + 1.25 * np.cos(mid_ang), cm[1] + 1.25 * np.sin(mid_ang),
            r"$\theta$", fontsize=14, color=INK, ha="center", va="center", zorder=4)

    save(fig, out)
