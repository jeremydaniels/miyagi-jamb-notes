from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes setup
    axes_clean(ax, "Quantity Demanded (units)", "Price (₦)", 10, 10)
    
    # Demand curve: straight downward-sloping line
    x_vals = np.linspace(1.2, 8.5, 100)
    y_vals = 9.7 - x_vals
    
    ax.plot(x_vals, y_vals, color=DEEP["blue"], lw=3.5)
    
    # Label for Demand curve 'D'
    ax.text(8.7, 1.2, "D", fontsize=18, fontweight="bold", color=DEEP["blue"], va="center", ha="left")
    ax.text(1.0, 8.8, "D", fontsize=18, fontweight="bold", color=DEEP["blue"], va="center", ha="right")
    
    # Points P1, P2 and Q1, Q2
    p1, q1 = 7.0, 2.7
    p2, q2 = 3.8, 5.9
    
    # Dotted projection lines
    ax.plot([0, q1, q1], [p1, p1, 0], color=DEEP["pink"], lw=2.0, ls="--")
    ax.plot([0, q2, q2], [p2, p2, 0], color=DEEP["pink"], lw=2.0, ls="--")
    
    # Markers on the curve
    ax.plot([q1, q2], [p1, p2], "o", color=DEEP["blue"], markersize=7)
    
    # Axis ticks/labels for P1, P2, Q1, Q2
    ax.set_xticks([q1, q2])
    ax.set_xticklabels(["Q₁", "Q₂"], fontsize=16, fontweight="bold", color=INK)
    ax.set_yticks([p2, p1])
    ax.set_yticklabels(["P₂", "P₁"], fontsize=16, fontweight="bold", color=INK)
    
    # Direction arrows to illustrate price fall and quantity rise (placed slightly inside the graph)
    ax.annotate("", xy=(0.2, p2 + 0.3), xytext=(0.2, p1 - 0.3),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0))
    ax.annotate("", xy=(q2 - 0.3, 0.2), xytext=(q1 + 0.3, 0.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0))
    
    # Explanatory note
    ax.text(5.5, 7.5, "Law of Demand:\nAs price falls (P₁ → P₂),\nquantity increases (Q₁ → Q₂)",
            fontsize=14, color=INK, linespacing=1.4,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.5"))

    save(fig, out)
