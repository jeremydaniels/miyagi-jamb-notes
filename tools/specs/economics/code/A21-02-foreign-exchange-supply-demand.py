from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Range of values
    xmax, ymax = 10, 10
    axes_clean(ax, "Quantity of USD", "Exchange Rate (₦/USD)", xmax, ymax)
    
    # Curves: Supply and Demand
    # Intersection at (5, 5)
    x = np.linspace(1, 9, 200)
    # Demand curve: downward sloping
    y_d = 8.5 - 0.7 * x
    # Supply curve: upward sloping
    y_s = 1.5 + 0.7 * x
    
    # Equilibrium point
    eq_x = 5.0
    eq_y = 5.0
    
    # Plot curves
    ax.plot(x, y_d, color=DEEP["blue"], lw=3.5)
    ax.plot(x, y_s, color=DEEP["orange"], lw=3.5)
    
    # Labels for curves
    ax.text(8.8, y_d[-5], "D (Importers)", fontsize=15, color=DEEP["blue"], weight="bold",
            va="center", ha="left", bbox=dict(fc="white", ec="none", pad=2))
    ax.text(8.8, y_s[-5], "S (Exporters)", fontsize=15, color=DEEP["orange"], weight="bold",
            va="center", ha="left", bbox=dict(fc="white", ec="none", pad=2))
    
    # Dotted projection lines to axes
    ax.plot([eq_x, eq_x], [0, eq_y], ls="--", color=GREY, lw=2)
    ax.plot([0, eq_x], [eq_y, eq_y], ls="--", color=GREY, lw=2)
    
    # Equilibrium point dot
    ax.scatter([eq_x], [eq_y], color=INK, s=80, zorder=5)
    
    # Ticks / labels at projections
    ax.text(eq_x, -0.6, "Equilibrium Quantity", fontsize=14, color=INK,
            ha="center", va="top", bbox=dict(fc="white", ec="none", pad=1))
    
    ax.annotate("Equilibrium Exchange Rate", xy=(0, eq_y), xytext=(0.5, eq_y + 0.8),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                ha="left", va="bottom", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Title
    ax.set_title("Market determination of floating exchange rate", fontsize=16, color=INK, pad=20, weight="bold")
    
    # Adjust limits to ensure labels fit cleanly
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-1.0, 10.5)
    
    save(fig, out)
