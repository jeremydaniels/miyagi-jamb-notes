from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.2)
    ax = fig.add_subplot(111)
    
    # Axes setup
    axes_clean(ax, "Time (days)", "Antibody concentration", 65, 110)
    
    # Generate smooth time points
    t = np.linspace(0, 60, 1000)
    
    # Smooth mathematical representation of primary response:
    def primary(x):
        dt = np.maximum(0, x - 3.0)
        res = 24.0 * (dt / 9.0)**2.5 * np.exp(-2.5 * (dt - 9.0) / 9.0)
        res[x < 3.0] = 0.0
        return res
        
    # Smooth mathematical representation of secondary response:
    def secondary(x):
        dt = np.maximum(0, x - 28.0)
        peak_t = 7.5
        alpha = 2.2
        beta = alpha / peak_t
        res = 95.0 * ((dt / peak_t) ** alpha) * np.exp(-beta * (dt - peak_t))
        res[x < 28.0] = 0.0
        return res

    # Combine responses seamlessly
    y = primary(t) + secondary(t)
    
    # Plot curve
    ax.plot(t, y, color=DEEP["blue"], lw=3.5, zorder=3)
    
    # Protection threshold line
    ax.axhline(35, color=DEEP["orange"], ls="--", lw=2, zorder=2)
    ax.text(12, 38, "Level needed for protection", color=DEEP["orange"], 
            fontsize=12, fontweight="bold", ha="center",
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    # First exposure arrow & annotation
    ax.annotate("First exposure\n(vaccine)", xy=(0, 2), xytext=(0, 52),
                fontsize=12, color=INK, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2, mutation_scale=15),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))
                
    # Primary response label
    ax.annotate("Primary response:\nslow and small", xy=(12, 24), xytext=(12, 65),
                fontsize=12, color=INK, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Second exposure arrow & annotation
    ax.annotate("Second exposure\n(same pathogen)", xy=(28, 6), xytext=(28, 75),
                fontsize=12, color=INK, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2, mutation_scale=15),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))
                
    # Secondary response label
    ax.annotate("Secondary response:\nfast and large", xy=(35.5, 95), xytext=(45, 95),
                fontsize=12, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Tick marks styling
    ax.set_xticks([0, 10, 20, 28, 40, 50, 60])
    ax.set_xticklabels(["0", "10", "20", "28", "40", "50", "60"], fontsize=11)
    ax.set_yticks([])
    
    save(fig, out)
