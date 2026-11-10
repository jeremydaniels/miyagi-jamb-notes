from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 4.5)
    
    # 3 subplots side by side
    axes = [fig.add_subplot(1, 3, i + 1) for i in range(3)]
    
    titles = [
        "Object at rest",
        "Uniform velocity",
        "Acceleration"
    ]
    
    t = np.linspace(0, 10, 100)
    
    # Left graph: horizontal line (object at rest)
    s_rest = np.full_like(t, 5.0)
    axes[0].plot(t, s_rest, color=DEEP["blue"], lw=3.5)
    
    # Middle graph: straight diagonal line (constant velocity)
    s_const = 0.8 * t
    axes[1].plot(t, s_const, color=DEEP["green"], lw=3.5)
    
    # Right graph: curve bending upwards (acceleration)
    s_accel = 0.08 * (t ** 2)
    axes[2].plot(t, s_accel, color=DEEP["orange"], lw=3.5)
    
    for i, ax in enumerate(axes):
        # Configure axes styling
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        
        # Remove tick numbers for a conceptual textbook diagram
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Spines styling
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['bottom'].set_color(INK)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        
        # Axis labels
        ax.set_xlabel("Time, t (s)", fontsize=14, color=INK, labelpad=8)
        ax.set_ylabel("Distance, s (m)", fontsize=14, color=INK, labelpad=8)
        
        # Subplot Title
        ax.set_title(titles[i], fontsize=15, color=INK, pad=12, fontweight='bold')
    
    fig.subplots_adjust(left=0.08, right=0.96, bottom=0.18, top=0.84, wspace=0.35)
    save(fig, out)
