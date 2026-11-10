from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Left subplot: Volume vs Temperature
    ax1 = fig.add_subplot(1, 2, 1)
    # Right subplot: Density vs Temperature
    ax2 = fig.add_subplot(1, 2, 2)
    
    T = np.linspace(0, 12, 200)
    
    # Left graph: Volume minimum at 4°C
    V = 1.0 + 0.005 * (T - 4)**2
    
    # Right graph: Density maximum at 4°C
    rho = 1.0 / V
    
    for ax, y, ylabel, title, is_min in [
        (ax1, V, "Volume", "Volume vs Temperature", True),
        (ax2, rho, "Density", "Density vs Temperature", False)
    ]:
        ax.set_facecolor('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['bottom'].set_color(INK)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        
        ax.set_xlabel("Temperature (°C)", fontsize=15, color=INK, labelpad=8)
        ax.set_ylabel(ylabel, fontsize=15, color=INK, labelpad=8)
        ax.set_title(title, fontsize=16, color=INK, pad=14, fontweight='bold')
        
        color_line = DEEP["blue"] if is_min else DEEP["orange"]
        ax.plot(T, y, color=color_line, lw=3.5)
        
        y_val_4 = 1.0
        y_min_lim = 0.95 if is_min else 0.65
        y_max_lim = 1.45 if is_min else 1.05
        ax.set_ylim(y_min_lim, y_max_lim)
        ax.set_xlim(0, 12)
        
        # Dotted line to 4°C
        ax.plot([4, 4], [y_min_lim, y_val_4], color=GREY, linestyle='--', lw=1.8)
        
        # Turning point dot
        ax.scatter([4], [y_val_4], color=color_line, s=70, zorder=5)
        
        # Annotation for min/max
        point_text = "Minimum volume\nat 4°C" if is_min else "Maximum density\nat 4°C"
        xytext_offset = (5.5, 1.15) if is_min else (6.5, 0.95)
        ax.annotate(
            point_text,
            xy=(4, y_val_4),
            xytext=xytext_offset,
            fontsize=14,
            color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
        )
        
        # Custom ticks on x-axis
        ax.set_xticks([0, 4, 8, 12])
        ax.set_xticklabels(["0", "4°C", "8", "12"], fontsize=14, color=INK)
        ax.set_yticks([])  # Qualitative/conceptual axis values
        ax.tick_params(colors=INK, width=1.5, length=5)

    plt.tight_layout(pad=3.0)
    save(fig, out)
