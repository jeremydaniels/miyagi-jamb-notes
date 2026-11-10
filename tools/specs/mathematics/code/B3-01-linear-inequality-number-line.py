from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 3.5)
    ax = fig.add_subplot(111)
    
    # Hide standard axes
    ax.set_axis_off()
    ax.set_xlim(-4.2, 2.2)
    ax.set_ylim(-1.5, 1.8)
    
    # Base number line with arrows on both ends
    ax.annotate('', xy=(1.8, 0), xytext=(-3.8, 0),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=2.0, mutation_scale=15))
    
    # Tick marks and labels: "-3, -2, -1, 0, 1"
    ticks = [-3, -2, -1, 0, 1]
    for x in ticks:
        ax.plot([x, x], [-0.12, 0.12], color=INK, lw=1.8)
        ax.text(x, -0.45, str(x), ha='center', va='top', fontsize=16, color=INK)
    
    # Inequality ray: x >= -2
    # Thick line with an arrow pointing to the right
    ax.annotate('', xy=(1.65, 0), xytext=(-2, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=4.5, mutation_scale=18))
    
    # Shaded closed circle at -2
    ax.plot(-2, 0, marker='o', markersize=11, color=DEEP["blue"], zorder=5)
    
    # Label "x >= -2"
    ax.text(-0.5, 0.8, r"$x \geq -2$", ha='center', va='center', fontsize=18, color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3', lw=1.2))
    
    save(fig, out)
