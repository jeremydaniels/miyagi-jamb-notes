from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    
    # Hide standard axes
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1.0, 7.5)
    ax.axis('off')
    
    # Points defining Freytag's pyramid
    # 1. Exposition (bottom left)
    # 2. Rising action (rising slope)
    # 3. Climax (peak)
    # 4. Falling action (falling slope)
    # 5. Resolution (bottom right)
    
    x_coords = [0.8, 2.9, 5.0, 7.1, 9.2]
    y_coords = [1.2, 3.4, 5.6, 3.4, 1.2]
    
    # Plot connecting line segments (the mountain-shaped line)
    ax.plot(x_coords, y_coords, color=DEEP["blue"], lw=4, zorder=2)
    
    # Plot circular markers
    ax.scatter(x_coords, y_coords, s=180, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, zorder=3)
    
    # Labels and offsets
    labels = [
        ("Exposition", (0.8, 0.4), "center"),
        ("Rising action", (2.2, 4.0), "right"),
        ("Climax", (5.0, 6.4), "center"),
        ("Falling action", (7.8, 4.0), "left"),
        ("Resolution", (9.2, 0.4), "center")
    ]
    
    for text, (lx, ly), align in labels:
        ax.text(lx, ly, text, fontsize=15, color=INK, ha=align, va="center", weight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.9))
    
    # Bottom timeline arrow
    arrow_y = -0.3
    ax.annotate('', xy=(9.6, arrow_y), xytext=(0.4, arrow_y),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color=GREY, lw=2))
    
    ax.text(5.0, arrow_y - 0.45, "Time / order of events", fontsize=14, color=INK, ha="center", va="top")
    
    save(fig, out)
