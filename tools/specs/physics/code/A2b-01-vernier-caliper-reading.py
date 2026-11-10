from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    # Coordinates and dimensions
    main_y = 3.0
    vernier_y = 2.8
    vernier_start = 3.14
    
    # Draw main scale background and edge
    ax.add_patch(patches.Rectangle((1.8, main_y), 2.4, 1.5, facecolor=CREAM, edgecolor=GREY, lw=1))
    ax.plot([1.8, 4.2], [main_y, main_y], color=INK, lw=2)
    
    # Draw vernier scale background and edge
    ax.add_patch(patches.Rectangle((vernier_start - 0.2, vernier_y - 1.5), 1.3, 1.5, facecolor=CREAM, edgecolor=GREY, lw=1))
    ax.plot([vernier_start - 0.2, vernier_start + 1.1], [vernier_y, vernier_y], color=INK, lw=2)
    
    # Main scale markings (2.0 to 4.0 cm)
    for i in range(20, 41):
        x = i / 10.0
        if i % 10 == 0:
            tick_len = 0.4
            ax.text(x, main_y + tick_len + 0.1, f"{int(x)}", ha='center', va='bottom', fontsize=16, color=INK)
        elif i % 5 == 0:
            tick_len = 0.25
        else:
            tick_len = 0.15
        ax.plot([x, x], [main_y, main_y + tick_len], color=INK, lw=1.5)
        
    # Vernier scale markings (0 to 10)
    for i in range(11):
        x = vernier_start + i * 0.09
        if i % 5 == 0:
            tick_len = 0.4
            ax.text(x, vernier_y - tick_len - 0.1, f"{i}", ha='center', va='top', fontsize=14, color=INK)
        else:
            tick_len = 0.2
        ax.plot([x, x], [vernier_y, vernier_y - tick_len], color=INK, lw=1.5)
        
    # Highlight alignment (Vernier mark 4 aligns with Main mark 3.5)
    align_x = vernier_start + 4 * 0.09
    ax.plot([align_x, align_x], [vernier_y - 0.3, main_y + 0.3], color=DEEP['orange'], lw=2.5, ls='--', zorder=5)
    
    # Labels
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.8)
    
    ax.text(2.5, 4.0, "Main Scale: 3.1 cm", ha='center', va='center', fontsize=16, color=DEEP['blue'], bbox=bbox_props)
    ax.text(3.5, 1.0, "Vernier: 0.04 cm", ha='center', va='center', fontsize=16, color=DEEP['green'], bbox=bbox_props)
    ax.text(3.0, 0.4, "Reading = 3.14 cm", ha='center', va='center', fontsize=18, color=INK, fontweight='bold', bbox=dict(boxstyle="round,pad=0.4", fc=LAV, ec=DEEP['lav'], lw=2))
    
    # Connecting arrows for labels
    ax.annotate("", xy=(3.1, main_y + 0.15), xytext=(2.5, 3.8),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2))
    ax.annotate("", xy=(align_x, vernier_y - 0.2), xytext=(3.5, 1.2),
                arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=2))

    ax.set_xlim(1.5, 4.5)
    ax.set_ylim(0.0, 4.8)
    
    save(fig, out)
