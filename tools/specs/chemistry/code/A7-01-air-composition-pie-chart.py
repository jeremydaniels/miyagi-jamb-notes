from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    sizes = [78.0, 21.0, 0.9, 0.03]
    colors = [BLUE, GREEN, "#FDFD96", "#FF6B6B"]
    
    wedges, _ = ax.pie(
        sizes,
        startangle=90,
        counterclock=False,
        colors=colors,
        wedgeprops=dict(edgecolor=INK, linewidth=1.5)
    )
    
    ax.axis('equal')
    
    # Title
    ax.set_title("Composition of Unpolluted Dry Air", fontsize=18, weight="bold", color=INK, pad=25)
    
    # Labels
    # Nitrogen (78%) - Right and bottom
    ax.text(0.4, -0.4, "Nitrogen\n(78%)", fontsize=16, weight="bold", color=INK, ha='center', va='center')
    
    # Oxygen (21%) - Top left
    ax.text(-0.5, 0.3, "Oxygen\n(21%)", fontsize=15, weight="bold", color=INK, ha='center', va='center')
    
    # Argon (0.9%) - Top, slightly left
    ax.annotate(
        "Argon (0.9%)",
        xy=(-0.05, 1.0),
        xytext=(-0.5, 1.15),
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        ha="center",
        va="center",
        bbox=dict(fc="white", ec="none", pad=2)
    )
    
    # Carbon (IV) oxide (0.03%) - Top center
    ax.annotate(
        "Carbon (IV) oxide (0.03%)",
        xy=(0.0, 1.0),
        xytext=(0.5, 1.15),
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        ha="center",
        va="center",
        bbox=dict(fc="white", ec="none", pad=2)
    )
    
    save(fig, out)
