from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6)
    
    # Subplot 1: Parallel lines
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlim(-1, 6)
    ax1.set_ylim(-1, 7)
    ax1.set_aspect('equal')
    
    # Draw axes for left subplot
    ax1.axhline(0, color=GREY, lw=1.5, zorder=1)
    ax1.axvline(0, color=GREY, lw=1.5, zorder=1)
    ax1.text(5.7, -0.5, "x", fontsize=15, color=INK, ha='center', va='center')
    ax1.text(-0.5, 6.7, "y", fontsize=15, color=INK, ha='center', va='center')
    ax1.axis('off')
    
    # Parallel lines: slope m = 1.0
    # L1: y = x + 2
    # L2: y = x - 0.5
    x_vals = np.array([-0.5, 4.5])
    y_l1 = x_vals + 2.0
    y_l2 = x_vals - 0.5
    
    ax1.plot(x_vals, y_l1, color=DEEP["blue"], lw=3, zorder=2)
    ax1.plot(x_vals, y_l2, color=DEEP["blue"], lw=3, zorder=2)
    
    # Arrows on parallel lines to indicate parallelism
    # Midpoints for arrows
    p1 = (2.0, 4.0)
    p2 = (2.5, 2.0)
    dx, dy = 0.4, 0.4
    ax1.annotate('', xy=(p1[0] + dx, p1[1] + dy), xytext=(p1[0], p1[1]),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2, mutation_scale=15),
                 zorder=3)
    ax1.annotate('', xy=(p2[0] + dx, p2[1] + dy), xytext=(p2[0], p2[1]),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2, mutation_scale=15),
                 zorder=3)
    
    # Labels L1 and L2
    ax1.text(4.2, 6.5, r"$L_1$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc="white", ec="none", pad=2))
    ax1.text(4.7, 4.0, r"$L_2$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc="white", ec="none", pad=2))
    
    ax1.text(2.5, -1.2, "Parallel Lines", fontsize=16, color=INK, ha='center', weight='bold')

    # Subplot 2: Perpendicular lines
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlim(-1, 6)
    ax2.set_ylim(-1, 7)
    ax2.set_aspect('equal')
    
    # Draw axes for right subplot
    ax2.axhline(0, color=GREY, lw=1.5, zorder=1)
    ax2.axvline(0, color=GREY, lw=1.5, zorder=1)
    ax2.text(5.7, -0.5, "x", fontsize=15, color=INK, ha='center', va='center')
    ax2.text(-0.5, 6.7, "y", fontsize=15, color=INK, ha='center', va='center')
    ax2.axis('off')
    
    # Perpendicular lines intersecting at (2.5, 3)
    # L3: slope m = 4/3 => (y - 3) = 4/3 * (x - 2.5) => angle ~ 53.13 deg
    # L4: slope m = -3/4 => (y - 3) = -3/4 * (x - 2.5) => angle ~ -36.87 deg
    cx, cy = 2.5, 3.0
    
    # L3: vector u = (0.6, 0.8)
    u = np.array([0.6, 0.8])
    l3_start = np.array([cx, cy]) - 3.8 * u
    l3_end = np.array([cx, cy]) + 3.8 * u
    
    # L4: vector v = (0.8, -0.6)
    v = np.array([0.8, -0.6])
    l4_start = np.array([cx, cy]) - 3.8 * v
    l4_end = np.array([cx, cy]) + 3.8 * v
    
    ax2.plot([l3_start[0], l3_end[0]], [l3_start[1], l3_end[1]], color=DEEP["orange"], lw=3, zorder=2)
    ax2.plot([l4_start[0], l4_end[0]], [l4_start[1], l4_end[1]], color=DEEP["orange"], lw=3, zorder=2)
    
    # Right-angle symbol at intersection
    s = 0.5
    corner_poly = np.array([
        [cx, cy],
        [cx + s * u[0], cy + s * u[1]],
        [cx + s * (u[0] + v[0]), cy + s * (u[1] + v[1])],
        [cx + s * v[0], cy + s * v[1]]
    ])
    ax2.plot(corner_poly[1:, 0], corner_poly[1:, 1], color=INK, lw=1.5, zorder=3)
    
    # Labels L3 and L4
    ax2.text(l3_end[0] + 0.2, l3_end[1] + 0.2, r"$L_3$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc="white", ec="none", pad=2))
    ax2.text(l4_end[0] + 0.3, l4_end[1] - 0.2, r"$L_4$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc="white", ec="none", pad=2))
             
    ax2.text(2.5, -1.2, "Perpendicular Lines", fontsize=16, color=INK, ha='center', weight='bold')
    
    plt.subplots_adjust(bottom=0.15, top=0.9, left=0.08, right=0.95, wspace=0.25)
    save(fig, out)
