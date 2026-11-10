from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Time", "Concentration", 10, 10)

    # Time values
    t = np.linspace(0, 9.5, 300)
    
    # Kinetic parameters (first order A -> B)
    k = 0.45
    c0 = 8.5
    reactants = c0 * np.exp(-k * t)
    products = c0 * (1 - np.exp(-k * t))

    # Plot reaction curves
    ax.plot(t, reactants, color=DEEP["pink"], lw=3.5, label="Reactants")
    ax.plot(t, products, color=DEEP["blue"], lw=3.5, label="Products")

    # Curve labels directly placed
    ax.text(6.0, reactants[int(6.0 / 9.5 * 300)] + 0.6, "Reactants", 
            fontsize=15, color=DEEP["pink"], fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(6.0, products[int(6.0 / 9.5 * 300)] + 0.6, "Products", 
            fontsize=15, color=DEEP["blue"], fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=2))

    # Tangent 1: Initial rate at products curve near origin (t = 0.4)
    t1 = 0.4
    y1 = c0 * (1 - np.exp(-k * t1))
    slope1 = c0 * k * np.exp(-k * t1)
    dt1 = 1.6
    t_tang1 = np.array([max(0, t1 - dt1), t1 + dt1])
    y_tang1 = y1 + slope1 * (t_tang1 - t1)

    ax.plot(t_tang1, y_tang1, color=DEEP["orange"], lw=2.2, ls="--")
    ax.plot(t1, y1, marker="o", markersize=6, color=DEEP["orange"])

    # Tangent 2: Later rate at products curve (t = 3.2)
    t2 = 3.2
    y2 = c0 * (1 - np.exp(-k * t2))
    slope2 = c0 * k * np.exp(-k * t2)
    dt2 = 2.4
    t_tang2 = np.array([t2 - dt2, t2 + dt2])
    y_tang2 = y2 + slope2 * (t_tang2 - t2)

    ax.plot(t_tang2, y_tang2, color=DEEP["green"], lw=2.2, ls="--")
    ax.plot(t2, y2, marker="o", markersize=6, color=DEEP["green"])

    # Annotations for tangents
    ax.annotate("Initial rate\n(steep gradient)", 
                xy=(t1 + 0.6, y1 + slope1 * 0.6), 
                xytext=(0.6, 6.2),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Decreasing rate\n(shallower gradient)", 
                xy=(t2 + 1.2, y2 + slope2 * 1.2), 
                xytext=(4.2, 4.0),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Limits and style adjustments
    ax.set_xlim(-0.2, 9.8)
    ax.set_ylim(-0.2, 9.8)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    save(fig, out)
