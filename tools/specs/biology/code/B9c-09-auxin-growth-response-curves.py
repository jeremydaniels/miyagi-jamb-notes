from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9.5, 6)
    ax = fig.add_subplot(111)
    
    # Hide default box spines
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)
        
    x = np.linspace(1.8, 10.5, 600)
    
    # Mathematical models for the bell-shaped response curves
    # Roots: peaks around 3.2, drops below 0 around 4.5, levels off around -0.6
    # Buds: starts near 0, peaks around 5.8, drops below 0 around 7.2
    # Stems: starts near 0, peaks around 8.2, drops below 0 around 9.8
    y_root = 1.6 * np.exp(-((x - 3.2) ** 2) / (2 * 0.85 ** 2)) - 0.6
    y_bud  = 1.7 * np.exp(-((x - 5.8) ** 2) / (2 * 0.95 ** 2)) - 0.6
    y_stem = 1.9 * np.exp(-((x - 8.2) ** 2) / (2 * 1.05 ** 2)) - 0.6
    
    # Cut off roots curve at very low concentrations so it starts cleanly from baseline
    y_root = np.maximum(y_root, -0.6)
    y_bud  = np.maximum(y_bud, -0.6)
    y_stem = np.maximum(y_stem, -0.6)
    
    # Zero response horizontal line
    ax.axhline(0, color=GREY, lw=1.5, linestyle="--", zorder=1)
    
    # Colors
    BROWN = "#8B4513"
    
    # Plot curves
    ax.plot(x, y_root, color=BROWN, lw=3.2, zorder=3)
    ax.plot(x, y_bud, color=DEEP["green"], lw=3.2, zorder=3)
    ax.plot(x, y_stem, color=DEEP["blue"], lw=3.2, zorder=3)
    
    # Axis lines with arrows
    # X-axis line at bottom (-0.95)
    ax.annotate('', xy=(10.5, -0.95), xytext=(1.4, -0.95),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6))
    
    # Y-axis vertical line at left (x = 1.4)
    ax.annotate('', xy=(1.4, 1.55), xytext=(1.4, -0.95),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.6))
    
    # Labels for the curves directly on the plot
    ax.text(3.2, 1.15, "roots", color=BROWN, fontsize=13, weight="bold", ha="center",
            bbox=dict(fc="white", ec="none", pad=1.5))
    ax.text(5.8, 1.25, "buds", color=DEEP["green"], fontsize=13, weight="bold", ha="center",
            bbox=dict(fc="white", ec="none", pad=1.5))
    ax.text(8.2, 1.45, "stems", color=DEEP["blue"], fontsize=13, weight="bold", ha="center",
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Y-axis annotations placed clearly to the left of x = 1.4 axis line to prevent overlap
    ax.text(1.15, 0.75, "stimulation", color=INK, fontsize=13, rotation=90, va="center", ha="center")
    ax.text(1.15, -0.5, "inhibition", color=INK, fontsize=13, rotation=90, va="center", ha="center")
    ax.text(1.55, 0.07, "0", color=INK, fontsize=12, va="bottom", ha="left")
    
    # X-axis annotations
    ax.text(6.0, -1.22, "auxin concentration", color=INK, fontsize=13.5, ha="center")
    ax.text(1.6, -1.08, "low", color=INK, fontsize=11.5, ha="left")
    ax.text(10.3, -1.08, "high", color=INK, fontsize=11.5, ha="right")
    
    ax.set_xlim(0.4, 10.8)
    ax.set_ylim(-1.35, 1.65)
    ax.set_xticks([])
    ax.set_yticks([])
    
    save(fig, out)
