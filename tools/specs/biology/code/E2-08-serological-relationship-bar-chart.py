from style import *
import numpy as np

def draw(out):
    fig = canvas(11, 7.0)
    
    # Left axis for horizontal bar chart, right axis for test tubes illustration
    ax_bar = fig.add_axes([0.22, 0.12, 0.48, 0.70])
    ax_tubes = fig.add_axes([0.74, 0.12, 0.22, 0.70])
    
    # Data for the precipitin test
    animals = [
        "human",
        "chimpanzee",
        "gorilla",
        "baboon",
        "spider monkey",
        "dog",
        "pig",
        "chicken"
    ]
    # Relative precipitin amounts (pattern only, human = 100)
    values = [100, 97, 92, 60, 42, 15, 12, 2]
    
    # Reverse so human is at the top
    animals_rev = animals[::-1]
    values_rev = values[::-1]
    y_pos_rev = np.arange(len(animals_rev))
    
    # Color palette for bars
    bar_colors = [
        DEEP["blue"] if val >= 90 else 
        DEEP["green"] if val >= 40 else 
        DEEP["orange"] if val >= 10 else 
        GREY 
        for val in values_rev
    ]
    
    # Bar chart
    ax_bar.barh(y_pos_rev, values_rev, height=0.62, color=bar_colors, edgecolor=INK, lw=1.2)
    
    # Labels & ticks
    ax_bar.set_yticks(y_pos_rev)
    ax_bar.set_yticklabels(animals_rev, fontsize=13, fontweight='medium', color=INK)
    ax_bar.set_xlabel("relative amount of precipitate (%)", fontsize=13, color=INK, labelpad=8)
    ax_bar.set_xlim(0, 115)
    # The prompt specifies: "The bar lengths show the pattern only, no exact numbers other than human = 100."
    ax_bar.set_xticks([0, 100])
    ax_bar.tick_params(axis='both', which='both', labelsize=12, color=INK)
    
    # Axis limits to neatly frame the bars without extending past top bar
    ax_bar.set_ylim(-0.6, 7.6)
    
    ax_bar.spines['top'].set_visible(False)
    ax_bar.spines['right'].set_visible(False)
    ax_bar.spines['left'].set_color(INK)
    ax_bar.spines['bottom'].set_color(INK)
    ax_bar.spines['left'].set_linewidth(1.3)
    ax_bar.spines['bottom'].set_linewidth(1.3)
    
    # Label "100" at the human bar
    ax_bar.text(102, y_pos_rev[-1], "100", va='center', ha='left', fontsize=12.5, color=INK, fontweight='bold')
    
    # Title & Subtitles positioned via figure coordinates or nicely above the plot to avoid overlapping y-axis spine
    fig.text(0.22, 0.93, "precipitin test", fontsize=16, fontweight='bold', color=INK, va='top')
    fig.text(0.22, 0.88, "more precipitate = more closely related to humans", 
             fontsize=12.5, fontstyle='italic', color=DEEP["blue"], va='top')
    
    # Right panel: Test tubes showing decreasing cloudiness (precipitation)
    ax_tubes.set_xlim(0, 10)
    ax_tubes.set_ylim(-0.6, 7.6)
    ax_tubes.axis('off')
    
    tube_w = 5.0
    tube_x = 2.5
    
    for y, val in zip(y_pos_rev, values_rev):
        tube_y = y - 0.28
        h = 0.56
        
        # Draw tube background (clear fluid)
        rect_bg = plt.Rectangle((tube_x, tube_y), tube_w, h, fc=CREAM, ec="none")
        ax_tubes.add_patch(rect_bg)
        
        # Precipitate cloudiness proportional to precipitate amount
        alpha_cloud = max(0.04, (val / 100.0) * 0.85)
        rect_cloud = plt.Rectangle((tube_x, tube_y), tube_w, h, fc=DEEP["blue"], alpha=alpha_cloud, ec="none")
        ax_tubes.add_patch(rect_cloud)
        
        # Bottom precipitate pellet / denser zone at bottom of horizontal tube
        pellet_w = max(0.15, (val / 100.0) * 1.6)
        rect_pellet = plt.Rectangle((tube_x + tube_w - pellet_w, tube_y), pellet_w, h, 
                                    fc=DEEP["blue"], alpha=min(1.0, alpha_cloud * 1.5), ec="none")
        ax_tubes.add_patch(rect_pellet)
        
        # Tube outline border
        rect_border = plt.Rectangle((tube_x, tube_y), tube_w, h, fc="none", ec=INK, lw=1.2)
        ax_tubes.add_patch(rect_border)
        # Meniscus / rim
        rim = plt.Line2D([tube_x, tube_x], [tube_y - 0.05, tube_y + h + 0.05], color=INK, lw=1.5)
        ax_tubes.add_line(rim)
        
    fig.text(0.85, 0.88, "precipitate in tube", ha='center', va='top', fontsize=12, color=INK, style='italic')
    
    save(fig, out)
