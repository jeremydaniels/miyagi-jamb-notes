from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes setup
    xmax = 10
    ymax = 100
    axes_clean(ax, "Quantity", "Revenue / Price", xmax, ymax)
    
    # Values
    P = 20
    x = np.linspace(0, 8.5, 200)
    
    # Total Revenue (TR = P * Q) - linear ray from origin
    # At Q = 4.5, TR = 90
    tr = 10 * x  # Slope to fit nicely within axes (schematic TR line)
    
    # Plot Total Revenue Curve
    ax.plot(x, tr, color=DEEP["blue"], lw=3.5, label="Total Revenue (TR)")
    
    # Horizontal line at price level (₦20) representing P = AR = MR = Demand Curve
    ax.axhline(y=P, xmin=0, xmax=0.88, color=DEEP["orange"], lw=3.5)
    
    # Price level tick/label on vertical axis
    ax.text(-0.25, P, "₦20", color=INK, fontsize=15, va="center", ha="right", fontweight="bold")
    ax.plot([0, 0.15], [P, P], color=INK, lw=1.5)
    
    # Label for P = AR = MR = Demand Curve
    ax.text(8.7, P, "P = AR = MR = Demand Curve", color=INK, fontsize=14, va="center", ha="left",
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Label for Total Revenue
    ax.text(8.6, tr[-1], "Total Revenue (TR)", color=INK, fontsize=14, va="center", ha="left",
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Title / header annotation
    ax.text(4.5, 95, "Revenue under Perfect Competition", color=INK, fontsize=16, 
            ha="center", va="top", fontweight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    
    # Origin label
    ax.text(-0.25, -2.5, "0", color=INK, fontsize=15, ha="right", va="top")
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 105)
    
    save(fig, out)
