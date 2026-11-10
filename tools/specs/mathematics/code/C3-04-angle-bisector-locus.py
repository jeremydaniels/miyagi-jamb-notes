from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

    # Intersection point
    ox, oy = 0, 0
    L = 3.6

    # Two solid lines forming an 'X'
    # Angles in degrees:
    # Let Line 1 be at 30 deg (and 210 deg)
    # Let Line 2 be at 130 deg (and 310 deg)
    theta1 = 30.0
    theta2 = 130.0

    # Draw solid lines
    rad1 = np.radians(theta1)
    rad2 = np.radians(theta2)
    ax.plot([-L * np.cos(rad1), L * np.cos(rad1)],
            [-L * np.sin(rad1), L * np.sin(rad1)],
            color=INK, lw=2.5, zorder=2)
    ax.plot([-L * np.cos(rad2), L * np.cos(rad2)],
            [-L * np.sin(rad2), L * np.sin(rad2)],
            color=INK, lw=2.5, zorder=2)

    # Bisectors:
    # Angle 1 (acute/obtuse depending on diff):
    # Sector 1: between 30 and 130 -> width 100 deg -> bisector at 80 deg (and 260 deg)
    # Sector 2: between 130 and 210 -> width 80 deg -> bisector at 170 deg (and 350 deg)
    b1 = (theta1 + theta2) / 2.0  # 80 deg
    b2 = b1 + 90.0                # 170 deg

    rad_b1 = np.radians(b1)
    rad_b2 = np.radians(b2)
    
    # Draw dotted bisecting lines
    ax.plot([-L * np.cos(rad_b1), L * np.cos(rad_b1)],
            [-L * np.sin(rad_b1), L * np.sin(rad_b1)],
            color=DEEP["blue"], lw=2.2, ls=":", dashes=(2, 3), zorder=2)
    ax.plot([-L * np.cos(rad_b2), L * np.cos(rad_b2)],
            [-L * np.sin(rad_b2), L * np.sin(rad_b2)],
            color=DEEP["blue"], lw=2.2, ls=":", dashes=(2, 3), zorder=2)

    # Label lines / bisectors
    ax.text(0, 3.7, "Angle Bisectors of Intersecting Lines", 
            ha="center", va="center", fontsize=16, color=INK, weight="bold")

    # Draw arcs and tick marks
    # Sector 1: [30, 80] and [80, 130] (equal halves, 50 deg each) -> 1 tick
    # Sector 3 (opposite): [210, 260] and [260, 310] (equal halves, 50 deg each) -> 1 tick
    # Sector 2: [130, 170] and [170, 210] (equal halves, 40 deg each) -> 2 ticks
    # Sector 4 (opposite): [310, 350] and [350, 390] (equal halves, 40 deg each) -> 2 ticks

    def draw_arc_with_ticks(a_start, a_end, r, num_ticks, color):
        # Arc
        arc = Arc((ox, oy), 2*r, 2*r, angle=0, theta1=a_start, theta2=a_end,
                  color=color, lw=1.8, zorder=3)
        ax.add_patch(arc)
        
        # Ticks at mid angle
        mid_ang = np.radians((a_start + a_end) / 2.0)
        tick_len = 0.12
        if num_ticks == 1:
            offsets = [0]
        else:
            offsets = [-0.04, 0.04]
            
        for off in offsets:
            ang = mid_ang + off
            r_in = r - tick_len
            r_out = r + tick_len
            ax.plot([r_in * np.cos(ang), r_out * np.cos(ang)],
                    [r_in * np.sin(ang), r_out * np.sin(ang)],
                    color=color, lw=1.6, zorder=4)

    r_wide = 1.3
    r_narrow = 1.5

    # Top & Bottom sectors (50 deg halves, single tick)
    draw_arc_with_ticks(30, 80, r_wide, 1, DEEP["orange"])
    draw_arc_with_ticks(80, 130, r_wide, 1, DEEP["orange"])
    draw_arc_with_ticks(210, 260, r_wide, 1, DEEP["orange"])
    draw_arc_with_ticks(260, 310, r_wide, 1, DEEP["orange"])

    # Left & Right sectors (40 deg halves, double tick)
    draw_arc_with_ticks(130, 170, r_narrow, 2, DEEP["green"])
    draw_arc_with_ticks(170, 210, r_narrow, 2, DEEP["green"])
    draw_arc_with_ticks(310, 350, r_narrow, 2, DEEP["green"])
    draw_arc_with_ticks(350, 390, r_narrow, 2, DEEP["green"])

    # Intersection dot
    ax.scatter([0], [0], color=INK, s=40, zorder=5)

    # Annotations
    ax.annotate("angle bisector", xy=(L * np.cos(rad_b1) * 0.75, L * np.sin(rad_b1) * 0.75),
                xytext=(1.8, 3.0), fontsize=14, color=DEEP["blue"],
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.2),
                bbox=dict(fc="white", ec="none", pad=2))

    save(fig, out)
