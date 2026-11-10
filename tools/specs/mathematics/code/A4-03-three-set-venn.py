from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Universal set rectangle
    rect = patches.FancyBboxPatch(
        (0.5, 0.5), 9.0, 7.5,
        boxstyle="round,pad=0.1,rounding_size=0.3",
        linewidth=2.5, edgecolor=INK, facecolor='white'
    )
    ax.add_patch(rect)

    # Label for Universal Set U
    ax.text(0.9, 7.5, 'U', fontsize=18, fontweight='bold', color=INK, ha='left', va='top')

    # Circle parameters
    # Top left: A, Top right: B, Bottom center: C
    r = 2.35
    ca = (3.7, 5.0)
    cb = (6.3, 5.0)
    cc = (5.0, 3.1)

    # Shaded circles with soft palette
    circle_a = patches.Circle(ca, r, facecolor=BLUE, alpha=0.35, edgecolor=DEEP['blue'], linewidth=2.5)
    circle_b = patches.Circle(cb, r, facecolor=PINK, alpha=0.35, edgecolor=DEEP['pink'], linewidth=2.5)
    circle_c = patches.Circle(cc, r, facecolor=GREEN, alpha=0.35, edgecolor=DEEP['green'], linewidth=2.5)

    ax.add_patch(circle_a)
    ax.add_patch(circle_b)
    ax.add_patch(circle_c)

    # Outer circle labels (A, B, C)
    ax.text(ca[0] - 1.6, ca[1] + 1.6, 'A', fontsize=18, fontweight='bold', color=DEEP['blue'], ha='center', va='center')
    ax.text(cb[0] + 1.6, cb[1] + 1.6, 'B', fontsize=18, fontweight='bold', color=DEEP['pink'], ha='center', va='center')
    ax.text(cc[0], cc[1] - 2.0, 'C', fontsize=18, fontweight='bold', color=DEEP['green'], ha='center', va='top')

    # Style helper for region text boxes
    box_props = dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85)

    # Region 1: Only A
    ax.text(2.65, 5.3, 'Only A', fontsize=14, color=INK, ha='center', va='center', bbox=box_props)

    # Region 2: Only B
    ax.text(7.35, 5.3, 'Only B', fontsize=14, color=INK, ha='center', va='center', bbox=box_props)

    # Region 3: Only C
    ax.text(5.0, 1.85, 'Only C', fontsize=14, color=INK, ha='center', va='center', bbox=box_props)

    # Region 4: A and B only
    ax.text(5.0, 5.75, 'A and B only', fontsize=14, color=INK, ha='center', va='center', bbox=box_props)

    # Region 5: A and C only
    ax.text(3.55, 3.65, 'A and C\nonly', fontsize=14, color=INK, ha='center', va='center', multialignment='center', bbox=box_props)

    # Region 6: B and C only
    ax.text(6.45, 3.65, 'B and C\nonly', fontsize=14, color=INK, ha='center', va='center', multialignment='center', bbox=box_props)

    # Region 7: All three (A ∩ B ∩ C)
    ax.text(5.0, 4.35, 'All three\n(A ∩ B ∩ C)', fontsize=14, color=INK, ha='center', va='center', multialignment='center', bbox=box_props)

    # Region 8: Outside area (A ∪ B ∪ C)'
    ax.text(8.8, 1.2, "(A ∪ B ∪ C)'", fontsize=15, color=INK, ha='right', va='center', bbox=dict(boxstyle='round,pad=0.3', facecolor=CREAM, edgecolor=GREY))

    save(fig, out)
