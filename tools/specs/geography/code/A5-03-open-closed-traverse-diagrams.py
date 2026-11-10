from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 7.5)
    
    # Subplot 1: Open Traverse
    ax1 = fig.add_subplot(121)
    ax1.set_xlim(-0.5, 6.5)
    ax1.set_ylim(-0.5, 7.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    ax1.set_title("Open Traverse", fontsize=18, color=INK, weight='bold', pad=15)
    
    # Winding river alongside open traverse
    t = np.linspace(0.8, 6.8, 100)
    rx = 1.0 + 0.5 * np.sin(1.8 * t)
    ry = t
    ax1.plot(rx, ry, color=BLUE, lw=6, alpha=0.4, zorder=1)
    ax1.plot(rx, ry, color=DEEP["blue"], lw=1.5, ls="--", alpha=0.7, zorder=2)
    
    # Arrow along the river
    ax1.annotate("River flow", xy=(rx[15], ry[15]), xytext=(rx[40], ry[40]),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0),
                 fontsize=14, color=DEEP["blue"], ha="right", va="center",
                 bbox=dict(fc="white", ec="none", pad=2))
    
    # Open traverse points: A -> B -> C -> D -> E zigzagging downwards
    pts_open = {
        'A': (2.8, 6.5),
        'B': (4.8, 5.2),
        'C': (3.2, 3.7),
        'D': (5.2, 2.2),
        'E': (3.5, 0.8)
    }
    order_open = ['A', 'B', 'C', 'D', 'E']
    
    # Draw traverse lines
    for i in range(len(order_open) - 1):
        p1 = pts_open[order_open[i]]
        p2 = pts_open[order_open[i+1]]
        ax1.annotate("", xy=p2, xytext=p1,
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, shrinkA=8, shrinkB=8))
        
    # Draw stations (points) & labels
    for name, (x, y) in pts_open.items():
        ax1.plot(x, y, marker='o', markersize=9, color=DEEP["orange"], zorder=5)
        offset = (0.45, 0.1) if name in ['A', 'C', 'E'] else (-0.45, 0.1)
        ax1.text(x + offset[0], y + offset[1], name, fontsize=16, color=INK,
                 weight='bold', ha='center', va='center',
                 bbox=dict(fc="white", ec=GREY, boxstyle="circle,pad=0.2"))
                 
    # Subplot 2: Closed Traverse
    ax2 = fig.add_subplot(122)
    ax2.set_xlim(-0.5, 6.5)
    ax2.set_ylim(-0.5, 7.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    ax2.set_title("Closed Traverse", fontsize=18, color=INK, weight='bold', pad=15)
    
    # Pentagon points: A, B, C, D, E
    # A (top), B (right), C (lower right), D (lower left), E (left)
    pts_closed = [
        (3.0, 6.1),   # A
        (5.3, 4.5),   # B
        (4.4, 1.8),   # C
        (1.6, 1.8),   # D
        (0.8, 4.3),   # E
    ]
    
    # Closing line from E terminates slightly offset from A (at A')
    # A is at (3.0, 6.1). Let A' be at (2.4, 5.8) - so incoming from E(0.8, 4.3)
    # The gap is between A' and A.
    a_true = np.array(pts_closed[0])
    a_error = np.array([2.35, 5.75])
    
    names_closed = ['A', 'B', 'C', 'D', 'E']
    
    # Lines A -> B -> C -> D -> E
    for i in range(4):
        p1 = pts_closed[i]
        p2 = pts_closed[i+1]
        ax2.annotate("", xy=p2, xytext=p1,
                     arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5, shrinkA=8, shrinkB=8))
                     
    # E -> A' (traverse line terminating at computed point A')
    ax2.annotate("", xy=tuple(a_error), xytext=pts_closed[4],
                 arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5, shrinkA=8, shrinkB=6))
                 
    # Error of closure dashed line between A' and A
    ax2.plot([a_error[0], a_true[0]], [a_error[1], a_true[1]],
             color=DEEP["pink"], lw=2.5, ls="--", zorder=4)
             
    # Plot stations A, B, C, D, E
    for i, name in enumerate(names_closed):
        x, y = pts_closed[i]
        ax2.plot(x, y, marker='o', markersize=9, color=DEEP["green"], zorder=5)
        
        # Position labels cleanly away from vertices and traverse lines
        if name == 'A':
            dx, dy = 0.25, 0.42
        elif name == 'B':
            dx, dy = 0.48, 0.15
        elif name == 'C':
            dx, dy = 0.42, -0.35
        elif name == 'D':
            dx, dy = -0.42, -0.35
        elif name == 'E':
            dx, dy = -0.48, 0.05
            
        ax2.text(x + dx, y + dy, name, fontsize=16, color=INK,
                 weight='bold', ha='center', va='center',
                 bbox=dict(fc="white", ec=GREY, boxstyle="circle,pad=0.2"))
                 
    # Plot closure point A'
    ax2.plot(a_error[0], a_error[1], marker='o', markersize=7, color=DEEP["pink"], zorder=5)
    # A' label positioned above and to the left of A', well clear of line E->A'
    ax2.text(a_error[0] - 0.25, a_error[1] + 0.35, "A'", fontsize=15, color=DEEP["pink"],
             weight='bold', ha='center', va='center',
             bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.15", lw=0.8))
             
    # Annotation for Error of Closure
    # Place inside the upper-middle polygon interior, away from A->B and E->A' lines
    mid_error = (a_true + a_error) / 2
    ax2.annotate("Error of Closure",
                 xy=(mid_error[0], mid_error[1]),
                 xytext=(3.0, 4.3),
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8),
                 fontsize=15, color=DEEP["pink"], weight='bold', ha='center', va='center',
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
                 
    # Subtle dividing line
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.1, 0.9], color=GREY, lw=1.2, ls=":", alpha=0.6))
    
    save(fig, out)
