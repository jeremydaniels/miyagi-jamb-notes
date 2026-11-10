from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Quantity of Labour", "Wage Rate / MRP", 10, 10)

    # MRP curve: downward sloping
    x_mrp = np.linspace(1, 9, 200)
    y_mrp = 1.2 + 8.0 * np.exp(-0.25 * x_mrp)
    ax.plot(x_mrp, y_mrp, color=DEEP["blue"], lw=3.5)

    # Horizontal Supply / Wage Rate line at W = 4.5
    wage_val = 4.5
    x_eq = -np.log((wage_val - 1.2) / 8.0) / 0.25  # ~3.54
    y_eq = wage_val

    ax.axhline(y=wage_val, xmin=0, xmax=0.88, color=DEEP["green"], lw=3.5)

    # Dotted line to axes from equilibrium point
    ax.plot([x_eq, x_eq], [0, y_eq], color=GREY, linestyle="--", lw=2)
    ax.plot([0, x_eq], [y_eq, y_eq], color=GREY, linestyle="--", lw=1.5)

    # Equilibrium point dot
    ax.plot(x_eq, y_eq, "o", color=INK, markersize=7, zorder=5)

    # Labels and Annotations
    # Label for MRP curve (placed carefully to avoid overlap)
    ax.text(6.0, 3.5, "MRP (Demand for Labour)", fontsize=14, color=DEEP["blue"],
            fontweight="bold", bbox=dict(fc="white", ec="none", pad=2))

    # Label for Wage Rate / Supply of Labour
    ax.text(8.9, wage_val, "Wage Rate (Supply of Labour)", fontsize=14, color=DEEP["green"],
            va="center", ha="left", fontweight="bold", bbox=dict(fc="white", ec="none", pad=2))

    # Equilibrium wage label on Y-axis
    ax.text(-0.25, wage_val, "W", fontsize=15, color=INK, va="center", ha="right", fontweight="bold")

    # Equilibrium quantity label on X-axis
    ax.text(x_eq, -0.6, "Equilibrium quantity of labour\n(Q)", fontsize=14, color=INK,
            ha="center", va="top")

    # Title
    ax.set_title("Marginal Productivity Theory of Wages", fontsize=16, pad=18, color=INK, fontweight="bold")

    save(fig, out)
