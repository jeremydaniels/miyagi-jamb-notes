from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 14)
    
    # Create two subplots: top for compressional, bottom for tensional
    ax1 = fig.add_axes([0.05, 0.52, 0.9, 0.43])
    ax2 = fig.add_axes([0.05, 0.05, 0.9, 0.43])
    
    for ax in (ax1, ax2):
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
    # ==========================================
    # TOP HALF: COMPRESSIONAL FORCES & FOLDING
    # ==========================================
    ax1.text(6.0, 6.4, "COMPRESSIONAL FORCES (FOLD MOUNTAINS)", 
             fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
    
    # Draw inward arrows for compression
    arrow_kw = dict(arrowstyle="-|>,head_length=0.8,head_width=0.4", lw=3.5, color=DEEP["blue"])
    ax1.annotate("", xy=(2.0, 2.5), xytext=(0.5, 2.5), arrowprops=arrow_kw)
    ax1.text(1.25, 3.1, "Compressional\nforce", fontsize=14, color=DEEP["blue"], ha='center', va='bottom', fontweight='bold')
    
    ax1.annotate("", xy=(10.0, 2.5), xytext=(11.5, 2.5), arrowprops=arrow_kw)
    ax1.text(10.75, 3.1, "Compressional\nforce", fontsize=14, color=DEEP["blue"], ha='center', va='bottom', fontweight='bold')

    # Wavy folded layers
    # Domain for fold: x from 2.2 to 9.8
    xf = np.linspace(2.2, 9.8, 300)
    # Wave function: Anticline around x=4.0, Syncline around x=6.5, Anticline/Peak around x=8.5
    # Let's create an anticline at x=4.5 and syncline at x=7.5
    # y = base_y + A * sin(k * (x - x0))
    # Let's make an anticline at x=4.3, syncline at 6.7, anticline at 8.7
    # Or just one major anticline, one syncline, one fold mountain peak
    # Function for fold envelope:
    def wave(x, y0):
        return y0 + 0.8 * np.sin((x - 2.8) * 1.3)
    
    # 4 distinct rock strata
    layers_y = [1.0, 1.8, 2.6, 3.4, 4.2]
    colors_fold = [CREAM, ORANGE, LAV, GREEN]
    edge_col = INK
    
    for i in range(len(colors_fold)):
        y_bot = wave(xf, layers_y[i])
        y_top = wave(xf, layers_y[i+1])
        verts = list(zip(xf, y_bot)) + list(zip(xf[::-1], y_top[::-1]))
        poly = Polygon(verts, facecolor=colors_fold[i], edgecolor=edge_col, lw=1.8)
        ax1.add_patch(poly)
        
    # Vertical block end caps
    ax1.plot([2.2, 2.2], [wave(2.2, layers_y[0]), wave(2.2, layers_y[-1])], color=edge_col, lw=2)
    ax1.plot([9.8, 9.8], [wave(9.8, layers_y[0]), wave(9.8, layers_y[-1])], color=edge_col, lw=2)
    
    # Labels for Anticline, Syncline, Fold Mountain
    # Wave peak 1 is at x ≈ 4.0, trough at x ≈ 6.4, peak 2 at x ≈ 8.8
    # Let's locate them accurately:
    # (x - 2.8)*1.3 = pi/2 => x = 2.8 + 1.57/1.3 = 4.01 (Peak 1)
    # (x - 2.8)*1.3 = 3pi/2 => x = 2.8 + 4.71/1.3 = 6.43 (Trough)
    # (x - 2.8)*1.3 = 5pi/2 => x = 2.8 + 7.85/1.3 = 8.84 (Peak 2)
    
    # Label: Anticline (upfold)
    ax1.annotate("Anticline (upfold)", xy=(4.0, wave(4.0, 4.2)), xytext=(4.0, 5.7),
                 ha='center', va='bottom', fontsize=14, fontweight='bold', color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
                 
    # Label: Syncline (downfold)
    ax1.annotate("Syncline (downfold)", xy=(6.43, wave(6.43, 4.2)), xytext=(6.43, 1.8),
                 ha='center', va='top', fontsize=14, fontweight='bold', color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
                 
    # Label: Fold Mountain
    ax1.annotate("Fold Mountain", xy=(8.84, wave(8.84, 4.2)), xytext=(8.84, 5.7),
                 ha='center', va='bottom', fontsize=15, fontweight='bold', color=DEEP["green"],
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                 arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=1.8))

    # ==========================================
    # BOTTOM HALF: TENSIONAL FORCES & FAULTING
    # ==========================================
    ax2.text(6.0, 6.4, "TENSIONAL FORCES (RIFT VALLEYS & HORSTS)", 
             fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
             
    # Draw outward arrows for tension
    ax2.annotate("", xy=(0.5, 3.2), xytext=(2.0, 3.2), arrowprops=arrow_kw)
    ax2.text(1.25, 3.8, "Tensional\nforce", fontsize=14, color=DEEP["blue"], ha='center', va='bottom', fontweight='bold')
    
    ax2.annotate("", xy=(11.5, 3.2), xytext=(10.0, 3.2), arrowprops=arrow_kw)
    ax2.text(10.75, 3.8, "Tensional\nforce", fontsize=14, color=DEEP["blue"], ha='center', va='bottom', fontweight='bold')

    # Three blocks: Left Horst, Central Graben (dropped), Right Horst
    # Fault 1: diagonal from (4.2, 4.8) down to (5.3, 1.0)
    # Fault 2: diagonal from (7.8, 4.8) down to (6.7, 1.0)
    # The middle block is dropped down by dy = 1.3
    
    dy_drop = 1.2
    y_levels_horst = [1.2, 2.1, 3.0, 3.9, 4.8]
    colors_fault = [CREAM, ORANGE, LAV, GREEN]
    
    # Left Block: x from 2.2 to fault 1
    # Fault 1 line: x(y) = 5.3 - (y - 1.0) * (5.3 - 4.2) / 3.8 = 5.3 - (y - 1.0) * (1.1 / 3.8)
    def x_fault1(y):
        return 5.3 - (y - 1.0) * (1.1 / 3.8)

    # Right Block: Fault 2 line: x(y) = 6.7 + (y - 1.0) * (1.1 / 3.8)
    def x_fault2(y):
        return 6.7 + (y - 1.0) * (1.1 / 3.8)
        
    # Draw Left Block layers
    for i in range(4):
        y0, y1 = y_levels_horst[i], y_levels_horst[i+1]
        pts = [[2.2, y0], [x_fault1(y0), y0], [x_fault1(y1), y1], [2.2, y1]]
        ax2.add_patch(Polygon(pts, facecolor=colors_fault[i], edgecolor=INK, lw=1.8))
        
    # Draw Right Block layers
    for i in range(4):
        y0, y1 = y_levels_horst[i], y_levels_horst[i+1]
        pts = [[x_fault2(y0), y0], [9.8, y0], [9.8, y1], [x_fault2(y1), y1]]
        ax2.add_patch(Polygon(pts, facecolor=colors_fault[i], edgecolor=INK, lw=1.8))

    # Center Graben (dropped block)
    # Layers are shifted down by dy_drop
    for i in range(4):
        y0, y1 = y_levels_horst[i] - dy_drop, y_levels_horst[i+1] - dy_drop
        pts = [[x_fault1(y0 + dy_drop), y0], [x_fault2(y0 + dy_drop), y0],
               [x_fault2(y1 + dy_drop), y1], [x_fault1(y1 + dy_drop), y1]]
        ax2.add_patch(Polygon(pts, facecolor=colors_fault[i], edgecolor=INK, lw=1.8))

    # Bold Fault lines
    ax2.plot([x_fault1(1.0), x_fault1(4.8)], [1.0, 4.8], color=DEEP["pink"], lw=3, ls="--")
    ax2.plot([x_fault2(1.0), x_fault2(4.8)], [1.0, 4.8], color=DEEP["pink"], lw=3, ls="--")
    
    # Downward motion arrow in the middle
    ax2.annotate("", xy=(6.0, 2.1), xytext=(6.0, 3.1),
                 arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.35", lw=2.5, color=DEEP["pink"]))

    # Labels for bottom diagram
    # "Normal faults"
    ax2.annotate("Normal faults", xy=(4.65, 3.2), xytext=(3.3, 2.0),
                 ha='center', va='top', fontsize=14, fontweight='bold', color=DEEP["pink"],
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5))
                 
    # "Rift Valley (Graben)"
    ax2.annotate("Rift Valley (Graben)", xy=(6.0, 3.6), xytext=(6.0, 4.9),
                 ha='center', va='bottom', fontsize=15, fontweight='bold', color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
                 
    # "Block Mountains (Horsts)"
    ax2.text(3.1, 5.2, "Block Mountain\n(Horst)", fontsize=14, fontweight='bold', color=INK,
             ha='center', va='bottom', bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax2.text(8.9, 5.2, "Block Mountain\n(Horst)", fontsize=14, fontweight='bold', color=INK,
             ha='center', va='bottom', bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Dividing horizontal line between sections
    line = plt.Line2D([0.08, 0.92], [0.50, 0.50], transform=fig.transFigure,
                      color=GREY, linestyle='-', linewidth=1.5)
    fig.lines.append(line)

    save(fig, out)
