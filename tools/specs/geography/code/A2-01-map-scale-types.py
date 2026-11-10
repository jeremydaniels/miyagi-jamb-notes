from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 8.5)

    # 3 horizontal panels vertically stacked
    ax1 = fig.add_axes([0.06, 0.73, 0.88, 0.22])
    ax2 = fig.add_axes([0.06, 0.46, 0.88, 0.22])
    ax3 = fig.add_axes([0.06, 0.07, 0.88, 0.34])

    for ax in [ax1, ax2, ax3]:
        ax.set_facecolor('white')
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_linewidth(1.5)
        ax.set_xticks([])
        ax.set_yticks([])

    # ------------------ Top Panel: Statement scale ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.text(0.5, 7.8, "1. Verbal / Statement Scale", fontsize=15, fontweight='bold', color=DEEP['blue'], ha='left', va='center')
    ax1.text(5.0, 3.8, "Statement scale: 1 cm represents 500 m", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.6', fc=CREAM, ec=DEEP['blue'], lw=1.5))

    # ------------------ Middle Panel: Representative Fraction ------------------
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.text(0.5, 7.8, "2. Representative Fraction (RF) Scale", fontsize=15, fontweight='bold', color=DEEP['blue'], ha='left', va='center')
    ax2.text(5.0, 3.8, "Representative Fraction (RF): 1:50,000", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.6', fc=CREAM, ec=DEEP['blue'], lw=1.5))

    # ------------------ Bottom Panel: Linear scale ------------------
    # Provide comfortable margin so no labels hit panel borders
    ax3.set_xlim(-1.8, 5.0)
    ax3.set_ylim(-1.8, 2.5)
    ax3.text(-1.6, 2.1, "3. Linear / Graphical Scale", fontsize=15, fontweight='bold', color=DEEP['blue'], ha='left', va='center')

    # Ruler dimensions
    y_bar = 0.05
    h_bar = 0.35

    # Secondary subdivisions extending left from 0 to -1 km (10 segments of 100 m = 0.1 km each)
    for i in range(10):
        x_start = -(i + 1) * 0.1
        color = 'white' if (i % 2 == 0) else INK
        rect = plt.Rectangle((x_start, y_bar), 0.1, h_bar, facecolor=color, edgecolor=INK, lw=1.2)
        ax3.add_patch(rect)

    # Primary divisions extending right from 0 to 4 km (each 1 km divided into 2 half-km blocks)
    for km in range(4):
        rect1 = plt.Rectangle((km, y_bar), 0.5, h_bar, facecolor=INK, edgecolor=INK, lw=1.2)
        ax3.add_patch(rect1)
        rect2 = plt.Rectangle((km + 0.5, y_bar), 0.5, h_bar, facecolor='white', edgecolor=INK, lw=1.2)
        ax3.add_patch(rect2)

    # Full outline border
    full_rect = plt.Rectangle((-1.0, y_bar), 5.0, h_bar, fill=False, edgecolor=INK, lw=1.5)
    ax3.add_patch(full_rect)

    # Ticks along the top of the bar
    for i in range(11):
        x_pos = - i * 0.1
        tick_len = 0.14 if (i % 2 == 0 or i == 5) else 0.07
        ax3.plot([x_pos, x_pos], [y_bar + h_bar, y_bar + h_bar + tick_len], color=INK, lw=1.2)

    for km in range(5):
        ax3.plot([km, km], [y_bar + h_bar, y_bar + h_bar + 0.14], color=INK, lw=1.2)
        if km < 4:
            ax3.plot([km + 0.5, km + 0.5], [y_bar + h_bar, y_bar + h_bar + 0.07], color=INK, lw=1.0)

    # Text labels above the bar
    label_y = y_bar + h_bar + 0.25

    # Zero mark
    ax3.text(0.0, label_y, "0", fontsize=15, ha='center', va='bottom', color=INK, fontweight='bold')

    # Primary division labels
    for km in [1, 2, 3, 4]:
        ax3.text(km, label_y, str(km), fontsize=15, ha='center', va='bottom', color=INK)
    ax3.text(4.25, label_y, "km", fontsize=15, ha='left', va='bottom', fontweight='bold', color=INK)

    # Secondary subdivision labels (1000, 500)
    for m in [500, 1000]:
        x_pos = - m / 1000.0
        ax3.text(x_pos, label_y, str(m), fontsize=14, ha='center', va='bottom', color=INK)

    ax3.text(-1.0, label_y + 0.38, "metres", fontsize=14, ha='center', va='bottom', fontweight='bold', color=INK)

    # Annotations below the ruler
    ax3.annotate("Secondary subdivisions\n(100s of metres)", xy=(-0.5, y_bar), xytext=(-0.5, -0.85),
                 ha='center', va='top', fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.5))

    ax3.annotate("Primary divisions\n(kilometres)", xy=(2.0, y_bar), xytext=(2.0, -0.85),
                 ha='center', va='top', fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.5))

    save(fig, out)
    plt.close(fig)
