from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Pyramid dimensions
    # Apex at (5, 6.2), Base from x = 1.0 to 9.0 at y = 1.0
    x_apex = 5.0
    y_top = 6.2
    y_base = 1.0
    half_base = 3.6

    # 4 levels: y boundaries
    # Levels from bottom to top: 1, 2, 3, 4
    y_bounds = [1.0, 2.3, 3.6, 4.9, 6.2]
    
    # Function to get left and right x for a given y
    def get_x_bounds(y):
        frac = (y_top - y) / (y_top - y_base)
        w = half_base * frac
        return x_apex - w, x_apex + w

    colors = [
        (GREEN, DEEP["green"]),
        (BLUE, DEEP["blue"]),
        (ORANGE, DEEP["orange"]),
        (LAV, DEEP["lav"])
    ]

    labels = [
        ("1. The Qur'an", "(The Word of Allah)"),
        ("2. The Sunnah", "(The practice of the Prophet)"),
        ("3. Ijma'", "(Consensus of Scholars)"),
        ("4. Qiyas", "(Analogical Deduction)")
    ]

    for i in range(4):
        y_b = y_bounds[i]
        y_t = y_bounds[i+1]
        
        xl_b, xr_b = get_x_bounds(y_b)
        xl_t, xr_t = get_x_bounds(y_t)
        
        if i == 3:
            # Triangular tip
            pts = [[xl_b, y_b], [xr_b, y_b], [x_apex, y_top]]
        else:
            # Trapezoid
            pts = [[xl_b, y_b], [xr_b, y_b], [xr_t, y_t], [xl_t, y_t]]
            
        poly = Polygon(pts, closed=True, facecolor=colors[i][0], edgecolor=colors[i][1], lw=2.5, zorder=2)
        ax.add_patch(poly)
        
        # Center of the level for text
        y_mid = (y_b + y_t) / 2.0
        main_txt, sub_txt = labels[i]
        
        if i == 3:
            # Shift slightly downward for the tip so text fits nicely
            y_mid = y_b + (y_t - y_b) * 0.38
            ax.text(x_apex, y_mid + 0.18, main_txt, ha='center', va='center', fontsize=14, fontweight='bold', color=INK, zorder=4)
            ax.text(x_apex, y_mid - 0.20, sub_txt, ha='center', va='center', fontsize=13, color=INK, zorder=4)
        else:
            ax.text(x_apex, y_mid + 0.20, main_txt, ha='center', va='center', fontsize=15, fontweight='bold', color=INK, zorder=4)
            ax.text(x_apex, y_mid - 0.22, sub_txt, ha='center', va='center', fontsize=13.5, color=INK, zorder=4)

    # Title
    ax.text(5.0, 6.65, "Sources of Islamic Law (Usul al-Fiqh)", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Left upward arrow showing order of consultation
    arrow_x = 0.8
    ax.annotate(
        "",
        xy=(arrow_x, 5.8),
        xytext=(arrow_x, 1.4),
        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=DEEP["green"], lw=2.5),
        zorder=3
    )
    ax.text(
        arrow_x, 3.6, "Order of Consultation\n(Hierarchy of Authority)",
        rotation=90, ha='right', va='center', fontsize=14, fontweight='bold', color=INK,
        bbox=dict(fc="white", ec="none", pad=3)
    )

    # Base annotation: Primary vs Secondary Sources bracket / note
    ax.text(9.1, 2.3, "Primary\nSources", ha='left', va='center', fontsize=14, fontweight='bold', color=DEEP["blue"])
    ax.text(9.1, 4.9, "Secondary\n(Derived)\nSources", ha='left', va='center', fontsize=14, fontweight='bold', color=DEEP["orange"])

    save(fig, out)
