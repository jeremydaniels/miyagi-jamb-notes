from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 9)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-4.6, 5.0)

    # Title
    ax.text(0, 4.6, "Floral Diagram of Hibiscus (Malvaceae)", 
            ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # 1. Mother Axis at the top
    mother_axis_y = 3.9
    ax.plot(0, mother_axis_y, 'o', color=INK, markersize=8, zorder=10)
    ax.plot(0, mother_axis_y, 'o', color='white', markersize=4, zorder=10)

    # Helper function for sepal / bract crescent
    def sepal_path(r, theta_start, theta_end, width=0.18):
        angles = np.linspace(theta_start, theta_end, 50)
        mid_idx = len(angles) // 2
        r_outer = np.full_like(angles, r + width)
        # make midrib peak
        peak = 0.15 * (1 - (np.abs(angles - angles[mid_idx]) / ((angles[-1] - angles[0]) / 2)))
        r_outer += peak
        r_inner = np.full_like(angles, r - width)
        
        x_out = r_outer * np.cos(angles)
        y_out = r_outer * np.sin(angles)
        x_in = r_inner * np.cos(angles[::-1])
        y_in = r_inner * np.sin(angles[::-1])
        
        xs = np.concatenate([x_out, x_in])
        ys = np.concatenate([y_out, y_in])
        return xs, ys

    # 2. Epicalyx: 5 small bracts (outer ring, r ~ 3.4)
    r_epi = 3.4
    epi_angles = [np.pi/10 + i * (2*np.pi / 5) for i in range(5)]
    for ang in epi_angles:
        span = 0.28
        xs, ys = sepal_path(r_epi, ang - span, ang + span, width=0.08)
        ax.fill(xs, ys, color=GREEN, ec=DEEP["green"], lw=1.5, zorder=2)

    # 3. Calyx: 5 sepals, joined (valvate calyx connected at margins)
    r_calyx = 2.7
    calyx_angles = [np.pi/2 + i * (2*np.pi / 5) for i in range(5)]
    span_calyx = np.pi / 5.5
    
    for i in range(5):
        ang = calyx_angles[i]
        th1, th2 = ang - span_calyx, ang + span_calyx
        xs, ys = sepal_path(r_calyx, th1, th2, width=0.12)
        ax.fill(xs, ys, color=GREEN, ec=DEEP["green"], lw=1.5, zorder=3)
        
        # Connect to the next sepal with an arc to show fusion (joined sepals)
        next_ang = calyx_angles[(i + 1) % 5]
        th_next_start = next_ang - span_calyx
        # Arc connecting th2 to th_next_start
        connect_thetas = np.linspace(th2, th_next_start, 15)
        if th_next_start < th2:
            connect_thetas = np.linspace(th2, th_next_start + 2*np.pi, 15)
        cx = r_calyx * np.cos(connect_thetas)
        cy = r_calyx * np.sin(connect_thetas)
        ax.plot(cx, cy, color=DEEP["green"], lw=2.0, zorder=3)

    # 4. Corolla: 5 free petals, overlapping (convolute aestivation)
    r_petals = 2.0
    petal_offset = np.pi / 5
    petal_angles = [petal_offset + i * (2*np.pi / 5) for i in range(5)]
    
    for i in range(5):
        ang = petal_angles[i]
        # Widened span to ensure overlapping without gaps
        t = np.linspace(ang - 0.3, ang + 1.3, 80)
        r_out = r_petals + 0.25 + 0.15 * np.sin(np.linspace(0, np.pi, 80))
        r_in  = r_petals - 0.25 - 0.10 * np.sin(np.linspace(0, np.pi, 80))
        # Twist effect: shift radius along curve to show overlapping clearly
        r_out += np.linspace(0.2, -0.2, 80)
        r_in  += np.linspace(0.2, -0.2, 80)
        
        xs = np.concatenate([r_out * np.cos(t), (r_in * np.cos(t))[::-1]])
        ys = np.concatenate([r_out * np.sin(t), (r_in * np.sin(t))[::-1]])
        ax.fill(xs, ys, color=PINK, ec=DEEP["pink"], lw=1.8, zorder=4)

    # 5. Staminal tube with anthers
    r_tube = 1.25
    tube_circle = plt.Circle((0, 0), r_tube, fill=False, color=DEEP["orange"], lw=2.2, linestyle='-', zorder=5)
    ax.add_patch(tube_circle)

    # Ring of monadelphous anthers (reniform/two-lobed)
    n_anthers = 20
    for i in range(n_anthers):
        ang = i * (2*np.pi / n_anthers)
        x_base = r_tube * np.cos(ang)
        y_base = r_tube * np.sin(ang)
        r_anth = r_tube + 0.22
        x_a = r_anth * np.cos(ang)
        y_a = r_anth * np.sin(ang)
        ax.plot([x_base, x_a], [y_base, y_a], color=DEEP["orange"], lw=1.2, zorder=5)
        
        # 2-lobed reniform anther
        tangent = ang + np.pi/2
        dx = 0.07 * np.cos(tangent)
        dy = 0.07 * np.sin(tangent)
        for sign in [-1, 1]:
            lobe_x = x_a + sign * dx
            lobe_y = y_a + sign * dy
            lobe = patches.Circle((lobe_x, lobe_y), 0.05, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.0, zorder=6)
            ax.add_patch(lobe)

    # 6. Ovary cross section: 5 carpels, syncarpous, 5 chambers, axile placentation
    r_ovary = 0.72
    ovary_wall = plt.Circle((0, 0), r_ovary, facecolor='white', edgecolor=DEEP["blue"], lw=2.0, zorder=7)
    ax.add_patch(ovary_wall)

    # 5 Septa dividing the ovary into 5 distinct chambers
    septa_angles = [np.pi/2 + i * (2*np.pi / 5) for i in range(5)]
    for s_ang in septa_angles:
        ax.plot([0, r_ovary * np.cos(s_ang)], [0, r_ovary * np.sin(s_ang)], color=DEEP["blue"], lw=1.5, zorder=8)
    
    # Center axis column
    center_col = plt.Circle((0, 0), 0.12, facecolor='white', edgecolor=DEEP["blue"], lw=1.2, zorder=9)
    ax.add_patch(center_col)
    ax.plot(0, 0, 'o', color=DEEP["blue"], markersize=3, zorder=10)

    # Ovules: exactly 2 in EACH of the 5 chambers, attached to the central axis (axile placentation)
    for i in range(5):
        mid_ang = septa_angles[i] + (np.pi / 5)
        for offset in [-0.22, 0.22]:
            ov_ang = mid_ang + offset
            ov_r = 0.38
            ox = ov_r * np.cos(ov_ang)
            oy = ov_r * np.sin(ov_ang)
            ovule = patches.Ellipse((ox, oy), 0.14, 0.09, angle=np.degrees(ov_ang),
                                    facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.0, zorder=10)
            ax.add_patch(ovule)

    # Labels and Annotations
    bbox_style = dict(fc="white", ec=GREY, boxstyle="round,pad=0.25")

    # Mother axis
    ax.annotate("mother axis",
                xy=(0, mother_axis_y), xytext=(1.8, 4.0),
                fontsize=11.5, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    # Epicalyx
    epi_sample_ang = epi_angles[0]
    ax.annotate("epicalyx",
                xy=(r_epi * np.cos(epi_sample_ang), r_epi * np.sin(epi_sample_ang)),
                xytext=(3.6, 1.8),
                fontsize=11.5, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    # Calyx
    calyx_sample_ang = calyx_angles[1]  # ~ 162 degrees
    ax.annotate("calyx (5, joined)",
                xy=(r_calyx * np.cos(calyx_sample_ang), r_calyx * np.sin(calyx_sample_ang)),
                xytext=(-3.9, 2.8),
                fontsize=11.5, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    # Corolla
    corolla_sample_ang = petal_angles[2]  # ~ 180 degrees
    ax.annotate("corolla (5, free)",
                xy=(r_petals * np.cos(corolla_sample_ang), r_petals * np.sin(corolla_sample_ang)),
                xytext=(-3.9, 0.8),
                fontsize=11.5, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    # Staminal tube with anthers
    anth_sample_ang = 14 * (2*np.pi / n_anthers)
    ax.annotate("staminal tube\nwith anthers",
                xy=((r_tube + 0.22) * np.cos(anth_sample_ang), (r_tube + 0.22) * np.sin(anth_sample_ang)),
                xytext=(-3.7, -1.8),
                fontsize=11.5, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    # Ovary 
    target_ovary_x = 0.35 * np.cos(-np.pi/4)
    target_ovary_y = 0.35 * np.sin(-np.pi/4)
    ax.annotate("ovary (5 carpels,\naxile placentation)",
                xy=(target_ovary_x, target_ovary_y),
                xytext=(2.6, -2.6),
                fontsize=11.5, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=bbox_style)

    save(fig, out)
