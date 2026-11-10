from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 8)
    ax.axis('off')

    # Glass block coordinates
    gx0, gx1 = 1.0, 9.5
    gy0, gy1 = 1.8, 5.2
    block = patches.Rectangle(
        (gx0, gy0), gx1 - gx0, gy1 - gy0,
        facecolor=BLUE, alpha=0.25, edgecolor=DEEP['blue'], lw=2, zorder=1
    )
    ax.add_patch(block)
    ax.text(8.8, 4.7, "Glass Block", fontsize=15, color=DEEP['blue'],
            ha='right', va='top', fontweight='bold')

    # Incident point on top surface
    # Let incident ray come at 45 deg to normal
    # Normal is vertical: x = x1
    x1, y1 = 3.5, gy1
    angle_i_deg = 50.0
    angle_i = np.radians(angle_i_deg)
    
    # Snell's law: n1 * sin(i) = n2 * sin(r), n1=1.0, n2=1.5
    n_glass = 1.52
    sin_r = np.sin(angle_i) / n_glass
    angle_r = np.arcsin(sin_r)
    angle_r_deg = np.degrees(angle_r)

    # Ray inside block: dy = -(gy1 - gy0)
    dy_block = gy1 - gy0
    dx_block = dy_block * np.tan(angle_r)
    x2 = x1 + dx_block
    y2 = gy0

    # Ray lengths outside
    len_in = 2.5
    x0 = x1 - len_in * np.sin(angle_i)
    y0 = y1 + len_in * np.cos(angle_i)

    len_out = 3.2
    x3 = x2 + len_out * np.sin(angle_i)
    y3 = y2 - len_out * np.cos(angle_i)

    # Extension of incident ray
    len_ext = 5.6
    x_ext = x1 + len_ext * np.sin(angle_i)
    y_ext = y1 - len_ext * np.cos(angle_i)

    # Normals
    norm_len = 1.2
    # Normal at (x1, y1)
    ax.plot([x1, x1], [y1 - norm_len, y1 + norm_len], color=GREY, ls='--', lw=1.8, zorder=2)
    ax.text(x1, y1 + norm_len + 0.15, "Normal", fontsize=14, color=INK, ha='center', va='bottom')

    # Normal at (x2, y2)
    ax.plot([x2, x2], [y2 - norm_len, y2 + norm_len], color=GREY, ls='--', lw=1.8, zorder=2)
    ax.text(x2, y2 - norm_len - 0.2, "Normal", fontsize=14, color=INK, ha='center', va='top')

    # Ray drawing
    # 1. Incident Ray
    ax.plot([x0, x1], [y0, y1], color=DEEP['pink'], lw=2.8, zorder=3)
    # Arrow on incident ray
    mid_in_x = (x0 + x1) / 2
    mid_in_y = (y0 + y1) / 2
    ax.annotate('', xy=(mid_in_x + 0.15 * np.sin(angle_i), mid_in_y - 0.15 * np.cos(angle_i)),
                xytext=(mid_in_x - 0.15 * np.sin(angle_i), mid_in_y + 0.15 * np.cos(angle_i)),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=2.5, mutation_scale=18))

    # 2. Refracted Ray inside
    ax.plot([x1, x2], [y1, y2], color=DEEP['pink'], lw=2.8, zorder=3)
    mid_ref_x = (x1 + x2) / 2
    mid_ref_y = (y1 + y2) / 2
    ax.annotate('', xy=(mid_ref_x + 0.15 * np.sin(angle_r), mid_ref_y - 0.15 * np.cos(angle_r)),
                xytext=(mid_ref_x - 0.15 * np.sin(angle_r), mid_ref_y + 0.15 * np.cos(angle_r)),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=2.5, mutation_scale=18))

    # 3. Emergent Ray
    ax.plot([x2, x3], [y2, y3], color=DEEP['pink'], lw=2.8, zorder=3)
    mid_em_x = (x2 + x3) / 2
    mid_em_y = (y2 + y3) / 2
    ax.annotate('', xy=(mid_em_x + 0.15 * np.sin(angle_i), mid_em_y - 0.15 * np.cos(angle_i)),
                xytext=(mid_em_x - 0.15 * np.sin(angle_i), mid_em_y + 0.15 * np.cos(angle_i)),
                arrowprops=dict(arrowstyle="-|>", color=DEEP['pink'], lw=2.5, mutation_scale=18))

    # 4. Undeviated ray path (dashed straight line extending incident ray)
    ax.plot([x1, x_ext], [y1, y_ext], color=DEEP['orange'], ls='--', lw=2.0, zorder=2)

    # Lateral displacement perpendicular line
    # Choose a point along emergent ray
    s_em = 1.8
    p_em = np.array([x2 + s_em * np.sin(angle_i), y2 - s_em * np.cos(angle_i)])
    
    # Vector along ray is u = (sin(i), -cos(i))
    # Vector perpendicular towards undeviated ray is n = (cos(i), sin(i))
    # Undeviated ray line starts at (x1, y1) with direction u
    # Vector from (x1, y1) to p_em:
    diff = p_em - np.array([x1, y1])
    n_vec = np.array([np.cos(angle_i), np.sin(angle_i)])
    # The perpendicular distance d:
    d_val = np.dot(diff, n_vec)
    # Point on undeviated ray:
    p_undev = p_em - d_val * n_vec

    # Perpendicular line labeled 'd'
    ax.plot([p_em[0], p_undev[0]], [p_em[1], p_undev[1]], color=INK, lw=2.0, zorder=4)
    # Right angle square at p_undev
    sq_size = 0.22
    u_vec = np.array([np.sin(angle_i), -np.cos(angle_i)])
    sq_p1 = p_undev + sq_size * n_vec
    sq_p2 = sq_p1 + sq_size * u_vec
    sq_p3 = p_undev + sq_size * u_vec
    ax.plot([sq_p1[0], sq_p2[0], sq_p3[0]], [sq_p1[1], sq_p2[1], sq_p3[1]], color=INK, lw=1.2)

    # Label 'd'
    mid_d = (p_em + p_undev) / 2
    ax.text(mid_d[0] + 0.2, mid_d[1] - 0.2, "d", fontsize=17, fontweight='bold', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))

    # Angle arcs
    # Angle i (incident angle with upper normal, from 90 to 90 + angle_i_deg)
    arc_i = patches.Arc((x1, y1), 1.5, 1.5, angle=0, theta1=90, theta2=90 + angle_i_deg,
                        color=INK, lw=1.6)
    ax.add_patch(arc_i)
    ax.text(x1 - 0.35, y1 + 0.65, "i", fontsize=16, fontstyle='italic', color=INK)

    # Angle r (refracted angle with normal inside, between -90 and -90 + angle_r_deg)
    arc_r = patches.Arc((x1, y1), 1.6, 1.6, angle=0, theta1=270, theta2=270 + angle_r_deg,
                        color=INK, lw=1.6)
    ax.add_patch(arc_r)
    ax.text(x1 + 0.25, y1 - 0.7, "r", fontsize=16, fontstyle='italic', color=INK)

    # Angle r at bottom (alternate interior angle)
    arc_r2 = patches.Arc((x2, y2), 1.4, 1.4, angle=0, theta1=90 + 180 - angle_r_deg, theta2=270,
                         color=INK, lw=1.6)
    # Emergent angle e
    arc_e = patches.Arc((x2, y2), 1.5, 1.5, angle=0, theta1=270, theta2=270 + angle_i_deg,
                        color=INK, lw=1.6)
    ax.add_patch(arc_e)
    ax.text(x2 + 0.35, y2 - 0.65, "e", fontsize=16, fontstyle='italic', color=INK)

    # Annotations and text labels
    ax.text(x0 - 0.2, y0 + 0.1, "Incident ray", fontsize=15, color=INK, ha='right', va='center')
    ax.text(mid_ref_x - 0.2, mid_ref_y, "Refracted ray", fontsize=15, color=INK, ha='right', va='center',
            bbox=dict(fc='white', ec='none', alpha=0.8, pad=1))
    ax.text(x3 + 0.1, y3 - 0.2, "Emergent ray", fontsize=15, color=INK, ha='left', va='top')
    ax.text(x_ext + 0.1, y_ext + 0.2, "Original path", fontsize=14, color=DEEP['orange'], ha='left', va='bottom')

    # Lateral displacement explanation
    ax.annotate("Lateral displacement (d)", xy=(mid_d[0], mid_d[1]), xytext=(mid_d[0] - 2.8, mid_d[1] - 1.2),
                fontsize=15, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, connectionstyle="arc3,rad=-0.1"),
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Title
    ax.text(5.0, 7.3, "Lateral Displacement through a Glass Block", fontsize=18,
            fontweight='bold', color=INK, ha='center')

    save(fig, out)
