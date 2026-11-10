from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0.05, 0.1, 0.58, 0.78])
    
    categories = ['Food', 'Transport', 'Savings', 'Books']
    percentages = [40, 25, 20, 15]
    colors = [GREEN, BLUE, ORANGE, PINK]
    edge_colors = [DEEP['green'], DEEP['blue'], DEEP['orange'], DEEP['pink']]
    
    # Draw pie chart
    wedges, texts, autotexts = ax.pie(
        percentages,
        labels=None,
        autopct='%1.0f%%',
        startangle=90,
        pctdistance=0.65,
        colors=colors,
        wedgeprops=dict(edgecolor='white', linewidth=2.5, antialiased=True)
    )
    
    for autotext in autotexts:
        autotext.set_fontsize(15)
        autotext.set_fontweight('bold')
        autotext.set_color(INK)
        
    ax.axis('equal')
    
    # Title
    fig.text(0.5, 0.92, 'Monthly Budget Distribution', fontsize=18, fontweight='bold', ha='center', color=INK)
    
    # Legend / Key on the right side
    # Using patches with corresponding colours and details
    legend_labels = [
        f"Food (144°, 40%)",
        f"Transport (90°, 25%)",
        f"Savings (72°, 20%)",
        f"Books (54°, 15%)"
    ]
    
    legend_patches = [
        plt.Line2D([0], [0], marker='s', markersize=14, color='w',
                   markerfacecolor=col, markeredgecolor=ecol, markeredgewidth=1.5)
        for col, ecol in zip(colors, edge_colors)
    ]
    
    leg = fig.legend(
        legend_patches, legend_labels,
        loc='center left',
        bbox_to_anchor=(0.62, 0.55),
        frameon=True,
        fontsize=14,
        edgecolor=GREY,
        title="Categories",
        title_fontsize=15,
        borderpad=1.0,
        labelspacing=0.9
    )
    leg.get_title().set_fontweight('bold')
    leg.get_title().set_color(INK)
    for text in leg.get_texts():
        text.set_color(INK)
        
    # Total budget box below legend
    fig.text(
        0.77, 0.30,
        "Total Budget:\n₦10,000",
        fontsize=16,
        fontweight='bold',
        color=INK,
        ha='center',
        va='center',
        bbox=dict(boxstyle="round,pad=0.6", facecolor=CREAM, edgecolor=GREY, lw=1.5)
    )

    save(fig, out)
