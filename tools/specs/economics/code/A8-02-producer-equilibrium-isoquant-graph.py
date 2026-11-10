from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 7)
    ax = fig.add_subplot(111)
    
    # Axes limits and setup
    xmax = 10
    ymax = 10
    axes_clean(ax, "Labour (L)", "Capital (K)", xmax, ymax)
    
    # Parameters for equilibrium
    # Tangency point E at (L*, K*) = (4.5, 4.5)
    # Slope of isocost is -1: K = 9 - L
    # Isoquant tangent to K = 9 - L at (4.5, 4.5): K * L = 4.5^2 = 20.25 => K = 20.25 / L
    
    # Isocost line from (0, 9) to (9, 0)
    x_ic = np.array([0, 9])
    y_ic = 9 - x_ic
    ax.plot(x_ic, y_ic, color=DEEP["blue"], lw=3, label="Isocost line")
    
    # Isoquant curve (IQ)
    x_iq = np.linspace(2.1, 8.8, 200)
    y_iq = 20.25 / x_iq
    ax.plot(x_iq, y_iq, color=DEEP["green"], lw=3, label="Isoquant (IQ)")
    
    # Tangency point E
    l_star, k_star = 4.5, 4.5
    ax.plot([l_star], [k_star], marker="o", markersize=8, color=INK, zorder=5)
    
    # Dashed lines to axes
    ax.plot([l_star, l_star], [0, k_star], color=GREY, linestyle="--", lw=2)
    ax.plot([0, l_star], [k_star, k_star], color=GREY, linestyle="--", lw=2)
    
    # Labels for equilibrium quantities on axes
    ax.text(l_star, -0.4, "L*", fontsize=15, color=INK, ha="center", va="top")
    ax.text(-0.3, k_star, "K*", fontsize=15, color=INK, ha="right", va="center")
    
    # Annotations
    # Equilibrium point E
    ax.annotate("E", 
                xy=(l_star, k_star), 
                xytext=(l_star + 0.5, k_star + 0.5),
                fontsize=16, 
                fontweight="bold", 
                color=INK)
    
    # Label for Isoquant (IQ)
    ax.text(8.5, 20.25 / 8.5 + 0.4, "IQ", fontsize=15, fontweight="bold", color=DEEP["green"],
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Label for Isocost line
    ax.text(7.6, 9 - 7.6 + 0.6, "Isocost", fontsize=15, color=DEEP["blue"],
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Title / diagram header
    ax.set_title("Producer Equilibrium", fontsize=18, pad=20, color=INK, fontweight="bold")
    
    save(fig, out)
