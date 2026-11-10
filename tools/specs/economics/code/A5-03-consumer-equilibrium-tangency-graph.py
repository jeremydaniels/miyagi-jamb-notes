from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Good X", "Good Y", 10, 10)

    # Budget Line AB
    # Let budget line be: y = 8 - x
    # Intercepts: A at (0, 8), B at (8, 0)
    x_b = np.array([0, 8])
    y_b = 8 - x_b
    ax.plot(x_b, y_b, color=INK, lw=2.5, zorder=2)

    # Labels for budget line endpoints A and B
    ax.text(-0.3, 8.0, "A", fontsize=16, color=INK, fontweight="bold", ha="right", va="center")
    ax.text(8.0, -0.4, "B", fontsize=16, color=INK, fontweight="bold", ha="center", va="top")

    # Range of x
    x_ic = np.linspace(1.2, 8.5, 300)

    # IC1: passes below IC2, intersects budget line at two points
    y_ic1 = 9.5 / x_ic
    ax.plot(x_ic, y_ic1, color=DEEP["blue"], lw=2.5, zorder=3)
    ax.text(8.6, y_ic1[-1], r"$\mathrm{IC}_1$", fontsize=15, color=DEEP["blue"], fontweight="bold", va="center")

    # IC2: tangent to budget line at (4, 4)
    y_ic2 = 16.0 / x_ic
    ax.plot(x_ic, y_ic2, color=DEEP["green"], lw=3.0, zorder=3)
    ax.text(8.6, y_ic2[-1], r"$\mathrm{IC}_2$", fontsize=15, color=DEEP["green"], fontweight="bold", va="center")

    # IC3: strictly above budget line
    y_ic3 = 24.0 / x_ic
    valid3 = y_ic3 <= 9.8
    ax.plot(x_ic[valid3], y_ic3[valid3], color=DEEP["pink"], lw=2.5, zorder=3)
    ax.text(8.6, y_ic3[-1], r"$\mathrm{IC}_3$", fontsize=15, color=DEEP["pink"], fontweight="bold", va="center")

    # Point of tangency E: (4, 4)
    ax.plot(4.0, 4.0, marker="o", markersize=8, color=DEEP["green"], zorder=5)
    ax.plot(4.0, 4.0, marker="o", markersize=4, color="white", zorder=6)
    
    # Label E with a white bbox to prevent any overlapping with the lines
    ax.text(4.2, 4.2, "E", fontsize=16, color=INK, fontweight="bold", ha="left", va="bottom", bbox=dict(fc="white", ec="none", pad=1.5), zorder=7)

    # Dashed lines from E to axes
    ax.plot([4, 4], [0, 4], color=GREY, linestyle="--", lw=1.5, zorder=1)
    ax.plot([0, 4], [4, 4], color=GREY, linestyle="--", lw=1.5, zorder=1)

    # Annotation for Consumer Equilibrium
    ax.annotate(
        "Consumer Equilibrium\n(Point E)",
        xy=(4.0, 4.0),
        xytext=(5.6, 6.2),
        fontsize=14,
        color=INK,
        fontweight="bold",
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, shrinkA=3, shrinkB=6),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4", lw=1.2),
        zorder=7
    )

    # Annotation describing the budget line AB
    ax.text(1.2, 7.3, "Budget Line (AB)", fontsize=14, color=INK, rotation=-45,
            bbox=dict(fc="white", ec="none", pad=1), zorder=7)

    save(fig, out)
