from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 6)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Triangle coordinates
    origin = np.array([1.5, 1.2])
    theta_deg = 32.0
    theta_rad = np.radians(theta_deg)
    length = 6.0
    
    fx = length * np.cos(theta_rad)
    fy = length * np.sin(theta_rad)
    
    pt_right = origin + np.array([fx, 0])
    pt_top = origin + np.array([fx, fy])

    # Fill triangle lightly
    tri_pts = np.array([origin, pt_right, pt_top])
    tri_poly = patches.Polygon(tri_pts, facecolor=CREAM, edgecolor="none", zorder=1)
    ax.add_patch(tri_poly)

    # Right angle symbol at (pt_right)
    sq_size = 0.4
    square = patches.Rectangle((pt_right[0] - sq_size, pt_right[1]), sq_size, sq_size,
                               fill=False, edgecolor=INK, lw=1.5, zorder=2)
    ax.add_patch(square)

    # Angle arc for theta
    arc_radius = 1.3
    arc = patches.Arc(origin, 2 * arc_radius, 2 * arc_radius, angle=0,
                      theta1=0, theta2=theta_deg, color=INK, lw=1.8, zorder=3)
    ax.add_patch(arc)
    
    # Theta label
    theta_label_angle = np.radians(theta_deg / 2)
    t_pos = origin + (arc_radius + 0.35) * np.array([np.cos(theta_label_angle), np.sin(theta_label_angle)])
    ax.text(t_pos[0], t_pos[1], r"$\theta$", fontsize=16, color=INK, ha="center", va="center")

    # Horizontal component arrow (Fx)
    ax.annotate("", xy=pt_right, xytext=origin,
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45",
                                color=DEEP["blue"], lw=2.5), zorder=4)

    # Vertical component arrow (Fy)
    ax.annotate("", xy=pt_top, xytext=pt_right,
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45",
                                color=DEEP["green"], lw=2.5), zorder=4)

    # Hypotenuse vector (F)
    ax.annotate("", xy=pt_top, xytext=origin,
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.5",
                                color=DEEP["orange"], lw=3.2), zorder=5)

    # Labels with bboxes to prevent overlapping
    # Vector F label
    mid_hyp = (origin + pt_top) / 2
    offset_hyp = np.array([-np.sin(theta_rad), np.cos(theta_rad)]) * 0.45
    f_pos = mid_hyp + offset_hyp
    ax.text(f_pos[0], f_pos[1], r"$\mathbf{F}$", fontsize=18, color=DEEP["orange"],
            ha="center", va="center", weight="bold",
            bbox=dict(fc="white", ec="none", pad=2))

    # Horizontal component label Fx = F cos(theta)
    mid_base = (origin + pt_right) / 2
    ax.text(mid_base[0], mid_base[1] - 0.45, r"$F_x = F \cos(\theta)$",
            fontsize=16, color=DEEP["blue"], ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=2))

    # Vertical component label Fy = F sin(theta)
    mid_vert = (pt_right + pt_top) / 2
    ax.text(mid_vert[0] + 0.35, mid_vert[1], r"$F_y = F \sin(\theta)$",
            fontsize=16, color=DEEP["green"], ha="left", va="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Bounds
    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(0.2, 5.0)

    save(fig, out)
