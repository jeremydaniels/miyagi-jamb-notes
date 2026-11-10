from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 7)
    ax = fig.add_subplot(111)
    
    # Range setup
    xmax = 9
    ymax = 8
    ax.set_xlim(-0.8, xmax)
    ax.set_ylim(-0.8, ymax)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw main axes with arrows
    ax.annotate('', xy=(8.5, 0), xytext=(-0.5, 0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.annotate('', xy=(0, 7.5), xytext=(0, -0.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    
    # Axis labels and Origin
    ax.text(8.5, -0.4, '$x$', fontsize=16, color=INK, ha='center', va='center')
    ax.text(-0.4, 7.5, '$y$', fontsize=16, color=INK, ha='center', va='center')
    ax.text(-0.35, -0.35, '$O$', fontsize=16, color=INK, ha='center', va='center')

    # Coordinates for P and Q
    x1, y1 = 2.0, 1.8
    x2, y2 = 6.8, 5.4

    # Dotted projection lines to axes
    ax.plot([x1, x1], [0, y1], color=GREY, ls=':', lw=1.5)
    ax.plot([x2, x2], [0, y2], color=GREY, ls=':', lw=1.5)
    ax.plot([0, x1], [y1, y1], color=GREY, ls=':', lw=1.5)
    ax.plot([0, x2], [y2, y2], color=GREY, ls=':', lw=1.5)

    # Ticks / labels on axes
    ax.text(x1, -0.4, '$x_1$', fontsize=15, color=INK, ha='center', va='center')
    ax.text(x2, -0.4, '$x_2$', fontsize=15, color=INK, ha='center', va='center')
    ax.text(-0.4, y1, '$y_1$', fontsize=15, color=INK, ha='center', va='center')
    ax.text(-0.4, y2, '$y_2$', fontsize=15, color=INK, ha='center', va='center')

    # Dotted lines forming right-angled triangle under PQ
    ax.plot([x1, x2], [y1, y1], color=DEEP["blue"], ls='--', lw=2)
    ax.plot([x2, x2], [y1, y2], color=DEEP["blue"], ls='--', lw=2)

    # Right angle marker at (x2, y1)
    sq = 0.4
    ax.plot([x2 - sq, x2 - sq, x2], [y1, y1 + sq, y1 + sq], color=DEEP["blue"], lw=1.5)

    # Line d connecting P and Q
    ax.plot([x1, x2], [y1, y2], color=DEEP["orange"], lw=3)

    # Label for line d
    mid_x = (x1 + x2) / 2.0
    mid_y = (y1 + y2) / 2.0
    ax.text(mid_x - 0.25, mid_y + 0.35, '$d$', fontsize=17, color=DEEP["orange"],
            fontweight='bold', ha='center', va='center')

    # Points P and Q
    ax.plot([x1, x2], [y1, y2], 'o', color=INK, markersize=6, zorder=5)
    ax.text(x1 - 0.25, y1 + 0.35, '$P(x_1, y_1)$', fontsize=15, color=INK, ha='right', va='center')
    ax.text(x2 + 0.25, y2 + 0.2, '$Q(x_2, y_2)$', fontsize=15, color=INK, ha='left', va='center')

    # Leg labels
    ax.text((x1 + x2) / 2.0, y1 - 0.4, '$(x_2 - x_1)$', fontsize=15, color=INK,
            ha='center', va='top', bbox=dict(fc='white', ec='none', pad=2))
    ax.text(x2 + 0.35, (y1 + y2) / 2.0, '$(y_2 - y_1)$', fontsize=15, color=INK,
            ha='left', va='center', bbox=dict(fc='white', ec='none', pad=2))

    save(fig, out)
