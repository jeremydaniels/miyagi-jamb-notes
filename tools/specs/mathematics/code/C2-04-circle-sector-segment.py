from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6.5)
    
    # Left Circle: Sector
    ax1 = fig.add_axes([0.05, 0.08, 0.42, 0.84])
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.4, 1.4)

    # Right Circle: Segment
    ax2 = fig.add_axes([0.53, 0.08, 0.42, 0.84])
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_xlim(-1.4, 1.4)
    ax2.set_ylim(-1.4, 1.4)

    r = 1.0
    theta1, theta2 = 25.0, 115.0  # degrees
    rad1, rad2 = np.radians(theta1), np.radians(theta2)

    # --- LEFT: SECTOR ---
    ax1.set_title("Sector of a Circle", fontsize=18, color=INK, pad=15, weight='bold')
    
    # Full circle outline (light)
    full_circle1 = patches.Circle((0, 0), r, ec=GREY, fc='none', lw=2)
    ax1.add_patch(full_circle1)

    # Sector Wedge
    sector = patches.Wedge((0, 0), r, theta1, theta2, facecolor=BLUE, edgecolor=DEEP['blue'], lw=2.5)
    ax1.add_patch(sector)

    # Center point
    ax1.scatter([0], [0], color=INK, s=30, zorder=5)
    ax1.text(0, -0.12, "O", fontsize=15, color=INK, ha='center', va='top')

    # Angle arc & label theta
    angle_arc = patches.Arc((0, 0), 0.45, 0.45, angle=0, theta1=theta1, theta2=theta2, color=DEEP['blue'], lw=1.8)
    ax1.add_patch(angle_arc)
    mid_angle = np.radians((theta1 + theta2) / 2)
    ax1.text(0.32 * np.cos(mid_angle), 0.32 * np.sin(mid_angle), r"$\theta$", 
             fontsize=16, color=DEEP['blue'], ha='center', va='center', weight='bold')

    # Radius labels
    mid_r1 = 0.55 * np.array([np.cos(rad1), np.sin(rad1)])
    ax1.text(mid_r1[0] + 0.08, mid_r1[1] - 0.08, "radius ($r$)", fontsize=14, color=INK, ha='left', va='top')

    mid_r2 = 0.55 * np.array([np.cos(rad2), np.sin(rad2)])
    ax1.text(mid_r2[0] - 0.08, mid_r2[1] + 0.05, "radius ($r$)", fontsize=14, color=INK, ha='right', va='bottom')

    # Arc label
    arc_pos = 1.08 * np.array([np.cos(mid_angle), np.sin(mid_angle)])
    ax1.text(arc_pos[0], arc_pos[1] + 0.08, "arc", fontsize=15, color=DEEP['blue'], ha='center', va='bottom', weight='bold')

    # Sector annotation
    ax1.annotate("Sector", xy=(0.45 * np.cos(mid_angle), 0.65 * np.sin(mid_angle)),
                 xytext=(0.85, 0.9), fontsize=15, color=INK, weight='bold',
                 ha='center', va='center',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY))

    # --- RIGHT: SEGMENT ---
    ax2.set_title("Segment of a Circle", fontsize=18, color=INK, pad=15, weight='bold')

    # Full circle outline (light)
    full_circle2 = patches.Circle((0, 0), r, ec=GREY, fc='none', lw=2)
    ax2.add_patch(full_circle2)

    # Segment fill: polygon along arc and straight back chord
    arc_thetas = np.linspace(rad1, rad2, 100)
    seg_x = list(np.cos(arc_thetas))
    seg_y = list(np.sin(arc_thetas))
    segment_poly = patches.Polygon(list(zip(seg_x, seg_y)), facecolor=ORANGE, edgecolor=DEEP['orange'], lw=2.5)
    ax2.add_patch(segment_poly)

    # Dashed radii to show chord vs radius relationship
    ax2.plot([0, np.cos(rad1)], [0, np.sin(rad1)], ls='--', color=GREY, lw=1.5)
    ax2.plot([0, np.cos(rad2)], [0, np.sin(rad2)], ls='--', color=GREY, lw=1.5)
    ax2.scatter([0], [0], color=INK, s=30, zorder=5)
    ax2.text(0, -0.12, "O", fontsize=15, color=INK, ha='center', va='top')

    # Chord line (bold)
    ax2.plot([np.cos(rad1), np.cos(rad2)], [np.sin(rad1), np.sin(rad2)], color=DEEP['orange'], lw=2.5)

    # Chord label
    chord_mid = 0.5 * np.array([np.cos(rad1) + np.cos(rad2), np.sin(rad1) + np.sin(rad2)])
    ax2.text(chord_mid[0] - 0.1, chord_mid[1] - 0.12, "chord", fontsize=15, color=INK, ha='right', va='top')

    # Arc label
    ax2.text(arc_pos[0], arc_pos[1] + 0.08, "arc", fontsize=15, color=DEEP['orange'], ha='center', va='bottom', weight='bold')

    # Minor segment annotation
    seg_center = 0.88 * np.array([np.cos(mid_angle), np.sin(mid_angle)])
    ax2.annotate("Minor Segment", xy=(seg_center[0], seg_center[1]),
                 xytext=(0.85, 0.9), fontsize=15, color=INK, weight='bold',
                 ha='center', va='center',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY))

    save(fig, out)
