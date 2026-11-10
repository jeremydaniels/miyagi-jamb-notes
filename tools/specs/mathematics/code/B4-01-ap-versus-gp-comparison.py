from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Subplot 1: Arithmetic Progression (A.P.)
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "Term number (n)", "Value of term", 5, 10)
    ax1.set_title("Arithmetic Progression (A.P.)", fontsize=16, color=INK, pad=12, fontweight="bold")
    
    n_ap = np.array([1, 2, 3, 4])
    val_ap = np.array([2, 4, 6, 8])
    
    # Continuous trend line
    x_ap_line = np.linspace(0.8, 4.5, 100)
    ax1.plot(x_ap_line, 2 * x_ap_line, color=DEEP["blue"], lw=3, zorder=2)
    
    # Stepped dashed lines to highlight linear staircase nature
    for i in range(len(n_ap) - 1):
        ax1.plot([n_ap[i], n_ap[i+1]], [val_ap[i], val_ap[i]], color=GREY, ls=":", lw=1.5, zorder=1)
        ax1.plot([n_ap[i+1], n_ap[i+1]], [val_ap[i], val_ap[i+1]], color=GREY, ls=":", lw=1.5, zorder=1)
    
    # Data points and labels
    ax1.scatter(n_ap, val_ap, color=DEEP["blue"], s=70, zorder=3)
    for x, y in zip(n_ap, val_ap):
        ax1.annotate(f"({x}, {y})", xy=(x, y), xytext=(x - 0.25, y + 0.5),
                     fontsize=14, color=INK,
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))
    
    ax1.set_xticks([1, 2, 3, 4])
    ax1.set_yticks([2, 4, 6, 8])
    ax1.tick_params(labelsize=14)
    
    # Subplot 2: Geometric Progression (G.P.)
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "Term number (n)", "Value of term", 5, 18)
    ax2.set_title("Geometric Progression (G.P.)", fontsize=16, color=INK, pad=12, fontweight="bold")
    
    n_gp = np.array([1, 2, 3, 4])
    val_gp = np.array([2, 4, 8, 16])
    
    # Continuous exponential curve
    x_gp_curve = np.linspace(0.8, 4.2, 100)
    ax2.plot(x_gp_curve, 2 ** x_gp_curve, color=DEEP["orange"], lw=3, zorder=2)
    
    # Data points and labels
    ax2.scatter(n_gp, val_gp, color=DEEP["orange"], s=70, zorder=3)
    for x, y in zip(n_gp, val_gp):
        offset_x = -0.55 if x == 4 else -0.3
        offset_y = 0.3 if x == 4 else 0.8
        ax2.annotate(f"({x}, {y})", xy=(x, y), xytext=(x + offset_x, y + offset_y),
                     fontsize=14, color=INK,
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))
        
    ax2.set_xticks([1, 2, 3, 4])
    ax2.set_yticks([2, 4, 8, 12, 16])
    ax2.tick_params(labelsize=14)
    
    fig.tight_layout(w_pad=4)
    save(fig, out)
