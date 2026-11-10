from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Left: Industry, Right: Firm
    ax1 = fig.add_axes([0.08, 0.15, 0.38, 0.72])
    ax2 = fig.add_axes([0.56, 0.15, 0.38, 0.72])
    
    axes_clean(ax1, "Quantity", "Price / Cost", 10, 10)
    axes_clean(ax2, "Quantity", "Price / Cost", 10, 10)
    
    ax1.set_title("Industry", fontsize=16, color=INK, pad=12, fontweight="bold")
    ax2.set_title("Firm", fontsize=16, color=INK, pad=12, fontweight="bold")
    
    # Industry Curves
    # Equilibrium at (5, 5) -> P1 = 5, Q1 = 5
    x_ind = np.linspace(1, 9, 100)
    supply = 1.0 + 0.8 * x_ind
    demand = 9.0 - 0.8 * x_ind
    
    ax1.plot(x_ind, supply, color=DEEP["blue"], lw=3)
    ax1.plot(x_ind, demand, color=DEEP["orange"], lw=3)
    
    ax1.text(9.1, supply[-1], "S", fontsize=16, color=DEEP["blue"], va="center", fontweight="bold")
    ax1.text(9.1, demand[-1], "D", fontsize=16, color=DEEP["orange"], va="center", fontweight="bold")
    
    # Intersection dashed guides on Industry
    ax1.plot([0, 5], [5, 5], color=GREY, ls="--", lw=1.8)
    ax1.plot([5, 5], [0, 5], color=GREY, ls="--", lw=1.8)
    ax1.plot(5, 5, "o", color=INK, markersize=6)
    
    # Industry tick labels
    ax1.text(-0.4, 5, "P₁", fontsize=15, color=INK, va="center", ha="right")
    ax1.text(5, -0.6, "Q₁", fontsize=15, color=INK, ha="center", va="top")
    
    # Connecting dotted line across axes from Industry P1 to Firm
    # In figure coordinates or drawing directly:
    con = matplotlib.patches.ConnectionPatch(
        xyA=(5, 5), coordsA=ax1.transData,
        xyB=(0, 5), coordsB=ax2.transData,
        color=GREY, ls=":", lw=2
    )
    fig.add_artist(con)
    
    # Firm graph
    x_firm = np.linspace(0, 9, 100)
    p_firm = np.full_like(x_firm, 5.0)
    
    ax2.plot(x_firm, p_firm, color=DEEP["green"], lw=3)
    ax2.text(-0.4, 5, "P₁", fontsize=15, color=INK, va="center", ha="right")
    
    # Label for firm's demand curve
    ax2.text(4.5, 5.6, "D = P = AR = MR", fontsize=15, color=DEEP["green"],
             ha="center", va="bottom", fontweight="bold",
             bbox=dict(fc="white", ec="none", pad=2))
    
    # Firm Q indicator (arbitrary individual firm quantity q1)
    ax2.plot([4.5, 4.5], [0, 5], color=GREY, ls="--", lw=1.8)
    ax2.plot(4.5, 5, "o", color=INK, markersize=6)
    ax2.text(4.5, -0.6, "q₁", fontsize=15, color=INK, ha="center", va="top")
    
    save(fig, out)
