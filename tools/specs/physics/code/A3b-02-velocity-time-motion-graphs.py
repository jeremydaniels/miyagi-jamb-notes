from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(13, 4.5)
    
    # Create 3 subplots with explicit positioning to avoid overlaps
    ax1 = fig.add_axes([0.09, 0.18, 0.21, 0.62])
    ax2 = fig.add_axes([0.42, 0.18, 0.21, 0.62])
    ax3 = fig.add_axes([0.75, 0.18, 0.21, 0.62])
    
    axes = [ax1, ax2, ax3]
    titles = [
        "Uniform velocity\n(zero acceleration)",
        "Uniform acceleration",
        "Uniform deceleration"
    ]
    
    for ax, title in zip(axes, titles):
        axes_clean(ax, "Time, t (s)", "Velocity, v (m/s)", 5, 5)
        ax.set_title(title, fontsize=15, color=INK, pad=12, weight='semibold')
        ax.set_xticks([])
        ax.set_yticks([])
    
    # Left graph: horizontal line
    t1 = np.linspace(0, 4.2, 100)
    v1 = np.full_like(t1, 3.0)
    ax1.plot(t1, v1, color=DEEP["blue"], lw=3.5)
    
    # Middle graph: straight diagonal line starting from origin
    t2 = np.linspace(0, 4.2, 100)
    v2 = (3.8 / 4.2) * t2
    ax2.plot(t2, v2, color=DEEP["green"], lw=3.5)
    
    # Right graph: straight line sloping down from y-axis to x-axis
    t3 = np.linspace(0, 4.2, 100)
    v3 = 3.8 - (3.8 / 4.2) * t3
    ax3.plot(t3, v3, color=DEEP["pink"], lw=3.5)
    
    save(fig, out)
