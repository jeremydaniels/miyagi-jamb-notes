from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5.5)
    
    # Left subplot: Direct Proportion
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "x", "y", 6, 6)
    
    x1 = np.linspace(0, 5.2, 100)
    y1 = 0.95 * x1
    ax1.plot(x1, y1, color=DEEP["blue"], lw=3.5)
    
    ax1.set_title("Direct Proportion (y = kx)", fontsize=16, color=INK, pad=18, weight="bold")
    
    # Text annotation with formula and feature
    ax1.text(0.4, 0.2, "O (0,0)", fontsize=14, color=INK, ha="left", va="center",
             bbox=dict(fc="white", ec="none", pad=0.1))
    ax1.scatter([0], [0], color=DEEP["blue"], s=40, zorder=5)
    ax1.text(3.0, 1.8, "Straight line\nthrough origin", fontsize=14, color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Right subplot: Inverse Proportion
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "x", "y", 6, 6)
    
    x2 = np.linspace(0.65, 5.4, 200)
    y2 = 3.2 / x2
    ax2.plot(x2, y2, color=DEEP["orange"], lw=3.5)
    
    ax2.set_title("Inverse Proportion (xy = k)", fontsize=16, color=INK, pad=18, weight="bold")
    
    # Text annotation
    ax2.text(2.6, 2.6, "Hyperbolic curve\n(asymptotic to axes)", fontsize=14, color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    plt.subplots_adjust(wspace=0.3)
    save(fig, out)
