from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 6)
    
    # Subplot 1: Constant force (rectangle)
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "Distance", "Force", 1.3, 1.3)
    
    # Parameters
    s_val = 1.0
    F_val = 1.0
    
    # Fill area (Work done = F * s)
    ax1.fill_between([0, s_val], [0, 0], [F_val, F_val], color=BLUE, alpha=0.35)
    
    # Lines
    ax1.plot([0, s_val], [F_val, F_val], color=DEEP["blue"], lw=3)
    ax1.plot([s_val, s_val], [0, F_val], color=DEEP["blue"], lw=1.5, ls="--")
    
    # Annotations and ticks
    ax1.set_xticks([s_val])
    ax1.set_xticklabels(["$s$"], fontsize=16)
    ax1.set_yticks([F_val])
    ax1.set_yticklabels(["$F$"], fontsize=16)
    
    ax1.text(0.5 * s_val, 0.5 * F_val, "Work done\n$W = F \\times s$", fontsize=15, 
             color=INK, ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.7, pad=2))
    
    ax1.set_title("Constant Force", fontsize=16, color=INK, pad=15)
    
    # Subplot 2: Linearly increasing force (triangle)
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "Distance", "Force", 1.3, 1.3)
    
    # Fill area (Work done = 1/2 * F * s)
    ax2.fill_between([0, s_val], [0, 0], [0, F_val], color=ORANGE, alpha=0.35)
    
    # Lines
    ax2.plot([0, s_val], [0, F_val], color=DEEP["orange"], lw=3)
    ax2.plot([s_val, s_val], [0, F_val], color=DEEP["orange"], lw=1.5, ls="--")
    ax2.plot([0, s_val], [F_val, F_val], color=GREY, lw=1.5, ls=":")
    
    # Annotations and ticks
    ax2.set_xticks([s_val])
    ax2.set_xticklabels(["$s$"], fontsize=16)
    ax2.set_yticks([F_val])
    ax2.set_yticklabels(["$F$"], fontsize=16)
    
    ax2.text(0.65 * s_val, 0.32 * F_val, "Work done\n$W = \\frac{1}{2} F s$", fontsize=15, 
             color=INK, ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.7, pad=2))
    
    ax2.set_title("Varying Force (e.g. Spring)", fontsize=16, color=INK, pad=15)
    
    fig.tight_layout(w_pad=4.0)
    save(fig, out)
