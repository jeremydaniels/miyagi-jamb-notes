from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 10)
    ax.axis('off')

    # Coordinates of triangle vertices
    top = np.array([5.0, 7.2])
    bottom_left = np.array([1.2, 1.8])
    bottom_right = np.array([8.8, 1.8])

    # Fill central triangle with soft cream
    triangle = Polygon([top, bottom_left, bottom_right], closed=True, 
                       facecolor=CREAM, edgecolor=DEEP['blue'], lw=3.0, zorder=1)
    ax.add_patch(triangle)

    # Top title box: Tawhīd (Oneness of Allah)
    ax.text(top[0], top[1] + 0.9, "Tawhīd\n(Oneness of Allah)", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK,
            bbox=dict(boxstyle='round,pad=0.6', facecolor=LAV, edgecolor=DEEP['lav'], lw=2.0),
            zorder=4)

    # Side 1: Left side (Rubūbiyyah)
    # midpoint between top and bottom_left
    mid_left = (top + bottom_left) / 2.0
    ax.text(mid_left[0] - 0.5, mid_left[1], 
            "1. Rubūbiyyah\n(Lordship – Creator and Sustainer)", 
            ha='right', va='center', fontsize=14, color=INK, multialignment='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=DEEP['green'], lw=2.0),
            zorder=4)

    # Side 2: Right side (Ulūhiyyah)
    # midpoint between top and bottom_right
    mid_right = (top + bottom_right) / 2.0
    ax.text(mid_right[0] + 0.5, mid_right[1], 
            "2. Ulūhiyyah\n(Worship – The Only One worthy of worship)", 
            ha='left', va='center', fontsize=14, color=INK, multialignment='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=DEEP['orange'], lw=2.0),
            zorder=4)

    # Side 3: Bottom side (Asmā' wa as-Sifāt)
    # midpoint between bottom_left and bottom_right
    mid_bottom = (bottom_left + bottom_right) / 2.0
    ax.text(mid_bottom[0], mid_bottom[1] - 0.9, 
            "3. Asmā' wa as-Sifāt\n(Names and Attributes – Unique and Perfect)", 
            ha='center', va='center', fontsize=14, color=INK, multialignment='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=DEEP['pink'], lw=2.0),
            zorder=4)

    # Decorative dots at vertices
    for pt in [top, bottom_left, bottom_right]:
        ax.plot(pt[0], pt[1], 'o', color=DEEP['blue'], markersize=9, zorder=3)

    # Overall diagram title / subtitle inside triangle
    ax.text(5.0, 3.8, "The Three Categories\nof Tawhīd", 
            ha='center', va='center', fontsize=15, fontstyle='italic', color=GREY,
            zorder=2)

    save(fig, out)
