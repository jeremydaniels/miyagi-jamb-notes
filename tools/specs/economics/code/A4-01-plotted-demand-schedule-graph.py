from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 6.5)
    ax = fig.add_subplot(111)

    # Set up axes
    axes_clean(ax, "Quantity Demanded (cups)", "Price (₦)", 30, 300)

    # Data points
    quantities = np.array([5, 10, 15, 20, 25])
    prices = np.array([250, 200, 150, 100, 50])

    # Extend line slightly for textbook style
    x_line = np.linspace(2, 28, 100)
    y_line = 300 - 10 * x_line
    ax.plot(x_line, y_line, color=DEEP["blue"], lw=3.5, zorder=3)

    # Label 'D' at both ends of the demand curve
    ax.text(2, 300 - 10 * 2 + 8, 'D', fontsize=16, fontweight='bold', color=DEEP["blue"], ha='center', va='bottom')
    ax.text(28.5, 300 - 10 * 28, 'D', fontsize=16, fontweight='bold', color=DEEP["blue"], ha='left', va='center')

    # Dotted lines connecting axes to the point (10, 200)
    ax.plot([10, 10], [0, 200], color=GREY, linestyle=':', lw=2, zorder=2)
    ax.plot([0, 10], [200, 200], color=GREY, linestyle=':', lw=2, zorder=2)

    # Plot coordinate points
    ax.scatter(quantities, prices, color=DEEP["blue"], s=50, zorder=4)

    # Configure ticks and grid marks
    ax.set_xticks([5, 10, 15, 20, 25])
    ax.set_yticks([50, 100, 150, 200, 250])
    ax.tick_params(axis='both', which='major', labelsize=14, colors=INK)

    # Set limits
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 300)

    save(fig, out)
