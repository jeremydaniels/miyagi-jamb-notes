from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Data points
    quantities = np.array([20, 40, 60, 80, 100])
    prices = np.array([10000, 15000, 20000, 25000, 30000])

    # Clean axes setup
    axes_clean(ax, "Quantity Supplied (Bags)", "Price (₦)", 120, 35000)

    # Dashed guide lines from axes to points
    for q, p in zip(quantities, prices):
        ax.plot([0, q], [p, p], color=GREY, linestyle="--", lw=1.2, zorder=1)
        ax.plot([q, q], [0, p], color=GREY, linestyle="--", lw=1.2, zorder=1)

    # Extended line for standard supply curve appearance
    x_line = np.linspace(10, 110, 100)
    # Line equation: P = 250 * Q + 5000
    y_line = 250 * x_line + 5000
    ax.plot(x_line, y_line, color=DEEP["blue"], lw=3.5, zorder=2)

    # Plot data points
    ax.scatter(quantities, prices, color=DEEP["blue"], s=60, zorder=3, edgecolor='white', linewidth=1.5)

    # Label supply curve "S" at the top end
    ax.text(112, 250 * 110 + 5000, "S", fontsize=18, fontweight="bold", color=DEEP["blue"], va="center", ha="left")

    # Set custom ticks and tick labels
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_xticklabels(["0", "20", "40", "60", "80", "100"], fontsize=14, color=INK)

    ax.set_yticks([0, 10000, 15000, 20000, 25000, 30000])
    ax.set_yticklabels(["0", "10,000", "15,000", "20,000", "25,000", "30,000"], fontsize=14, color=INK)

    # Ensure labels have enough room and proper font size
    ax.set_xlabel("Quantity Supplied (Bags)", fontsize=15, color=INK, labelpad=10)
    ax.set_ylabel("Price (₦)", fontsize=15, color=INK, labelpad=12)

    save(fig, out)
