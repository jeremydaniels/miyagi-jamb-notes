from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Left subplot: Continuous variation
    ax1 = fig.add_subplot(1, 2, 1)
    
    # 9 touching bars for continuous variation (histogram)
    bar_centers = np.array([140, 145, 150, 155, 160, 165, 170, 175, 180])
    bar_width = 5.0  # touching bars (gap = 0)
    # Bell-shaped heights
    bar_heights = np.array([3, 7, 14, 22, 28, 23, 15, 6, 2])
    
    ax1.bar(bar_centers, bar_heights, width=bar_width, color=BLUE, edgecolor=DEEP["blue"], linewidth=1.2, align='center')
    
    # Smooth bell-shaped curve over the top
    x_smooth = np.linspace(136, 184, 200)
    # Gaussian fit to bar tops
    mean = 160
    std = 8.5
    y_smooth = 28.5 * np.exp(-0.5 * ((x_smooth - mean) / std) ** 2)
    ax1.plot(x_smooth, y_smooth, color=DEEP["blue"], lw=2.5)
    
    # Axes limits and styling
    ax1.set_xlim(135, 185)
    ax1.set_ylim(0, 32)
    ax1.set_xticks(bar_centers)
    ax1.set_xlabel("Height (cm)", fontsize=13, color=INK, labelpad=8)
    ax1.set_ylabel("Number of pupils", fontsize=13, color=INK, labelpad=8)
    ax1.set_title("Continuous variation (e.g. height)", fontsize=14, color=INK, pad=14, fontweight='bold')
    
    # Annotations for Left Graph
    ax1.annotate("normal curve", 
                 xy=(164, 27.5), xytext=(171, 30),
                 fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                 ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
                 
    ax1.annotate("no gaps between bars", 
                 xy=(147.5, 10), xytext=(144, 22),
                 fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                 ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    # Right subplot: Discontinuous variation
    ax2 = fig.add_subplot(1, 2, 2)
    
    # Four distinct blood groups: O, A, B, AB with gaps
    groups = ["O", "A", "B", "AB"]
    x_pos = np.arange(len(groups))
    # Tallest first, two medium, then short
    blood_counts = [26, 19, 14, 5]
    bar_width_disc = 0.55  # clear gaps between bars (spacing is 1.0)
    
    ax2.bar(x_pos, blood_counts, width=bar_width_disc, color=ORANGE, edgecolor=DEEP["orange"], linewidth=1.2)
    
    ax2.set_xlim(-0.6, 3.6)
    ax2.set_ylim(0, 32)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(groups, fontsize=13)
    ax2.set_ylabel("Number of pupils", fontsize=13, color=INK, labelpad=8)
    ax2.set_title("Discontinuous variation (e.g. ABO blood group)", fontsize=14, color=INK, pad=14, fontweight='bold')
    
    # Annotation for gaps
    ax2.annotate("gaps between bars", 
                 xy=(0.5, 8), xytext=(1.5, 25),
                 fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                 ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    # Style cleanup for both axes
    for ax in (ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['bottom'].set_color(INK)
        ax.tick_params(colors=INK, labelsize=11)
        ax.set_facecolor("white")
    
    fig.tight_layout(w_pad=4.0)
    save(fig, out)
