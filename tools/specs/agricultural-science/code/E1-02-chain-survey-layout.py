from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8, 6.8)

    # Land boundary (irregular patch of land)
    boundary_x = [0.2, 2.0, 5.0, 8.5, 9.8, 9.5, 7.5, 4.5, 1.5, 0.2]
    boundary_y = [2.8, 5.8, 6.0, 5.2, 3.2, 1.2, 0.4, 0.2, 0.8, 2.8]
    ax.fill(boundary_x, boundary_y, color=CREAM, alpha=0.45, zorder=1)
    ax.plot(boundary_x, boundary_y, color=GREY, lw=2, linestyle='-', zorder=2)

    # Baseline: straight dashed line running through the middle
    p_start = (0.8, 3.0)
    p_end = (9.2, 3.0)
    ax.plot([p_start[0], p_end[0]], [p_start[1], p_end[1]], 
            color=DEEP["blue"], lw=2.5, linestyle='--', zorder=3)

    # Triangulation network (Survey framework)
    stations = {
        'A': (0.8, 3.0),
        'B': (3.5, 3.0),
        'C': (6.5, 3.0),
        'D': (9.2, 3.0),
        'T1': (2.2, 5.3),
        'T2': (6.0, 5.5),
        'B1': (2.5, 0.9),
        'B2': (6.8, 0.8)
    }

    # Triangle solid lines
    triangle_edges = [
        ('A', 'T1'), ('T1', 'B'), ('B', 'T2'), ('T2', 'C'), ('T2', 'D'), ('C', 'D'),
        ('A', 'B1'), ('B1', 'B'), ('B', 'B2'), ('B2', 'C'), ('B2', 'D')
    ]

    for p1_key, p2_key in triangle_edges:
        p1, p2 = stations[p1_key], stations[p2_key]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=DEEP["green"], lw=2.0, zorder=3)

    # Draw right-angled Offset line to the boundary
    offset_base = (4.8, 3.0)
    offset_target = (4.8, 5.95)
    ax.plot([offset_base[0], offset_target[0]], [offset_base[1], offset_target[1]], 
            color=DEEP["orange"], lw=2.2, linestyle='-', zorder=4)

    # Right angle symbol at offset
    sq_size = 0.3
    ax.plot([offset_base[0], offset_base[0] + sq_size, offset_base[0] + sq_size, offset_base[0]],
            [offset_base[1] + sq_size, offset_base[1] + sq_size, offset_base[1], offset_base[1]],
            color=DEEP["orange"], lw=1.5, zorder=4)

    # Draw Survey stations (Pegs) - small circles at triangle corners
    for s_name, (sx, sy) in stations.items():
        ax.scatter([sx], [sy], s=90, color=DEEP["pink"], edgecolor=INK, lw=1.5, zorder=5)

    # Baseline label
    ax.text(7.8, 3.3, "Baseline", color=DEEP["blue"], fontsize=15, fontweight='bold',
            bbox=dict(fc="white", ec="none", pad=2.0), zorder=6)

    # Offset label
    ax.annotate("Offset", xy=(4.8, 4.5), xytext=(3.6, 4.5),
                fontsize=15, color=DEEP["orange"], fontweight='bold',
                ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

    # Survey stations label pointing to a peg
    ax.annotate("Survey stations (Pegs)", xy=(6.0, 5.5), xytext=(6.5, 6.3),
                fontsize=14, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=6)

    # Diagram title
    ax.text(5.0, 0.0, "Chain Survey Layout", fontsize=16, ha="center", va="center",
            fontweight='bold', color=INK)

    save(fig, out)
