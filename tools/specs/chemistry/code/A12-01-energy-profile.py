from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Base axes
    axes_clean(ax, "Reaction Coordinate", "Energy", 10, 10)

    # Energy levels and coordinates
    # Reactants plateau: x in [1, 2.5], y = 5.0
    # Peak: x = 5.0, y = 8.5
    # Products plateau: x in [7.5, 9.5], y = 2.2
    
    # Constructing a smooth profile
    x_react = np.linspace(1.0, 2.5, 50)
    y_react = np.full_like(x_react, 5.0)

    # Transition curve (smooth cubic / bell shape connecting 2.5 to 7.5 with peak at 5.0)
    x_curve = np.linspace(2.5, 7.5, 200)
    # Bell curve atop linear transition
    # at 2.5: y=5.0, slope=0; at 7.5: y=2.2, slope=0; peak at 5.0: y=8.5
    t = (x_curve - 2.5) / 5.0  # 0 to 1
    # Base baseline drops from 5.0 to 2.2 smoothly
    s_curve = 5.0 - 2.8 * (3 * t**2 - 2 * t**3)
    # Add a hump symmetric around t = 0.5 that reaches peak 8.5
    # At t = 0.5, s_curve = 5.0 - 1.4 = 3.6. We need hump = 8.5 - 3.6 = 4.9
    hump = 4.9 * np.sin(np.pi * t)**2
    y_curve = s_curve + hump

    x_prod = np.linspace(7.5, 9.5, 50)
    y_prod = np.full_like(x_prod, 2.2)

    # Plot full reaction curve
    x_full = np.concatenate([x_react, x_curve, x_prod])
    y_full = np.concatenate([y_react, y_curve, y_prod])
    ax.plot(x_full, y_full, color=DEEP["blue"], lw=3.5)

    # Horizontal reference dashed lines
    ax.plot([1.0, 9.5], [5.0, 5.0], color=GREY, ls="--", lw=1.5)
    ax.plot([5.0, 5.0], [5.0, 8.5], color=GREY, ls=":", lw=1.0)
    ax.plot([7.5, 9.5], [2.2, 2.2], color=GREY, ls="--", lw=1.5)

    # Labels for Reactants and Products
    ax.text(1.75, 5.3, "Reactants", fontsize=15, ha="center", va="bottom", color=INK, fontweight="bold")
    ax.text(8.8, 2.5, "Products", fontsize=15, ha="center", va="bottom", color=INK, fontweight="bold")

    # Red arrows as specified: "red arrows" -> DEEP["pink"] or strong red
    RED = "#D32F2F"

    # Activation Energy (E_a) arrow: points UP from Reactants line to peak of curve
    ax.annotate(
        "",
        xy=(5.0, 8.5),
        xytext=(5.0, 5.0),
        arrowprops=dict(arrowstyle="->", color=RED, lw=2.5, shrinkA=0, shrinkB=0)
    )
    ax.text(
        4.85, 6.75, "Activation Energy ($E_a$)",
        fontsize=14, ha="right", va="center", color=INK,
        bbox=dict(fc="white", ec="none", pad=2)
    )

    # Enthalpy Change (\Delta H) arrow: points DOWN from Reactants line to Products line
    arrow_x = 7.8
    ax.annotate(
        "",
        xy=(arrow_x, 2.2),
        xytext=(arrow_x, 5.0),
        arrowprops=dict(arrowstyle="->", color=RED, lw=2.5, shrinkA=0, shrinkB=0)
    )
    ax.text(
        arrow_x + 0.2, 3.6, "Enthalpy Change ($\Delta H$)",
        fontsize=14, ha="left", va="center", color=INK,
        bbox=dict(fc="white", ec="none", pad=2)
    )

    save(fig, out)
