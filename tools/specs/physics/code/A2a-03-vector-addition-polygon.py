from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw_vector(ax, start, end, color, label, label_pos='auto', offset=(0, 0), lw=3):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    ax.annotate(
        '', xy=end, xytext=start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=22,
            shrinkA=0,
            shrinkB=0
        )
    )
    mid = ((start[0] + end[0]) / 2 + offset[0], (start[1] + end[1]) / 2 + offset[1])
    ax.text(
        mid[0], mid[1], label,
        color=INK, fontsize=15, weight='bold',
        ha='center', va='center',
        bbox=dict(fc='white', ec='none', pad=2.0, alpha=0.9)
    )

def draw(out):
    fig = canvas(12, 6)
    
    # Left subplot: Triangle method
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_xlim(-0.5, 5.5)
    ax1.set_ylim(-0.5, 4.5)
    ax1.set_title("Triangle Method (Tip-to-Tail)", fontsize=16, color=INK, pad=15, weight='bold')

    # Points for Triangle
    # Start: (0.5, 0.8)
    p0 = np.array([0.5, 0.8])
    p1 = np.array([3.8, 0.8])
    p2 = np.array([2.6, 3.6])

    draw_vector(ax1, p0, p1, DEEP['blue'], "Vector A", offset=(0, -0.35))
    draw_vector(ax1, p1, p2, DEEP['green'], "Vector B", offset=(0.4, 0.2))
    draw_vector(ax1, p0, p2, DEEP['orange'], "R = A + B", offset=(-0.5, 0.2), lw=3.5)

    # Right subplot: Polygon method
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_xlim(-0.5, 6.0)
    ax2.set_ylim(-0.5, 4.5)
    ax2.set_title("Polygon Method (Head-to-Tail)", fontsize=16, color=INK, pad=15, weight='bold')

    # Points for Polygon
    q0 = np.array([0.6, 0.8])
    q1 = np.array([3.4, 0.8])
    q2 = np.array([4.8, 2.0])
    q3 = np.array([3.5, 3.8])
    q4 = np.array([1.2, 3.4])

    draw_vector(ax2, q0, q1, DEEP['blue'], "Vector A", offset=(0, -0.35))
    draw_vector(ax2, q1, q2, DEEP['green'], "Vector B", offset=(0.35, -0.25))
    draw_vector(ax2, q2, q3, DEEP['pink'], "Vector C", offset=(0.45, 0.2))
    draw_vector(ax2, q3, q4, DEEP['lav'], "Vector D", offset=(-0.1, 0.35))
    draw_vector(ax2, q0, q4, DEEP['orange'], "R = A + B + C + D", offset=(-0.6, -0.1), lw=3.5)

    save(fig, out)
