from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Beaker dimensions
    bx, by, bw, bh = 2.5, 1.0, 5.0, 4.2
    
    # Electrolyte solution (blue)
    sol_h = 3.2
    electrolyte = patches.Rectangle((bx + 0.05, by + 0.05), bw - 0.1, sol_h, 
                                    facecolor=BLUE, edgecolor='none', alpha=0.45)
    ax.add_patch(electrolyte)

    # Electrolyte surface meniscus line
    ax.plot([bx + 0.05, bx + bw - 0.05], [by + sol_h + 0.05, by + sol_h + 0.05], 
            color=DEEP["blue"], lw=2, linestyle='-')

    # Glass beaker outline
    ax.plot([bx, bx, bx + bw, bx + bw], [by + bh, by, by, by + bh], 
            color=INK, lw=3, solid_capstyle='round')
    # Beaker lip/rim
    ax.plot([bx - 0.2, bx], [by + bh, by + bh], color=INK, lw=3)
    ax.plot([bx + bw, bx + bw + 0.2], [by + bh, by + bh], color=INK, lw=3)

    # Carbon rods (Electrodes)
    rod_w = 0.6
    rod_h = 3.6
    rod_y = 1.6
    
    # Left rod: Anode
    rx_left = 3.5
    anode_patch = patches.Rectangle((rx_left, rod_y), rod_w, rod_h, 
                                    facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(anode_patch)

    # Right rod: Cathode
    rx_right = 5.9
    cathode_patch = patches.Rectangle((rx_right, rod_y), rod_w, rod_h, 
                                      facecolor=GREY, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(cathode_patch)

    # Wires & External Circuit
    wire_y_top = 6.8
    # Left rod top to circuit
    ax.plot([rx_left + rod_w/2, rx_left + rod_w/2, 4.0], 
            [rod_y + rod_h, wire_y_top, wire_y_top], color=INK, lw=2.5)
    
    # Battery at center top: 4.0 to 5.0
    # Long line: positive terminal (left)
    ax.plot([4.0, 4.3], [wire_y_top, wire_y_top], color=INK, lw=2.5)
    ax.plot([4.3, 4.3], [wire_y_top - 0.45, wire_y_top + 0.45], color=INK, lw=3.5)
    # Short thick line: negative terminal (right)
    ax.plot([4.7, 4.7], [wire_y_top - 0.25, wire_y_top + 0.25], color=INK, lw=5.5)
    ax.plot([4.7, 5.0], [wire_y_top, wire_y_top], color=INK, lw=2.5)
    
    # +/- battery signs
    ax.text(4.2, wire_y_top + 0.55, "+", fontsize=16, ha='center', va='center', weight='bold', color=INK)
    ax.text(4.8, wire_y_top + 0.55, "−", fontsize=16, ha='center', va='center', weight='bold', color=INK)
    ax.text(4.5, wire_y_top + 0.75, "DC Battery", fontsize=15, ha='center', va='bottom', weight='bold', color=INK)

    # Switch between battery and cathode
    # Terminal dots
    ax.plot([5.0, 5.8], [wire_y_top, wire_y_top], color=INK, lw=2.5)
    ax.plot([5.8], [wire_y_top], 'o', color=INK, markersize=6)
    # Open / closed switch lever (slanted line representing closed/closing switch)
    ax.plot([5.8, 6.4], [wire_y_top, wire_y_top + 0.3], color=INK, lw=2.5)
    ax.plot([6.4], [wire_y_top], 'o', color=INK, markersize=6)
    ax.text(6.1, wire_y_top + 0.55, "Switch", fontsize=14, ha='center', va='bottom', color=INK)
    
    # Cathode connection from switch
    ax.plot([6.4, rx_right + rod_w/2, rx_right + rod_w/2], 
            [wire_y_top, wire_y_top, rod_y + rod_h], color=INK, lw=2.5)

    # Labels for electrodes
    # Anode label on left
    ax.annotate("Anode (+)", xy=(rx_left, 4.5), xytext=(1.2, 5.2),
                fontsize=15, weight='bold', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Cathode label on right
    ax.annotate("Cathode (−)", xy=(rx_right + rod_w, 4.5), xytext=(7.5, 5.2),
                fontsize=15, weight='bold', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Electrolyte label
    ax.annotate("Electrolyte\n(solution with ions)", xy=(bx + bw - 0.1, 2.5), xytext=(7.6, 2.5),
                fontsize=14, color=INK, va='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Helper function for ions
    def draw_ion(x, y, text, col, border_col):
        circ = patches.Circle((x, y), 0.26, facecolor=col, edgecolor=border_col, lw=2, zorder=4)
        ax.add_patch(circ)
        ax.text(x, y, text, fontsize=14, ha='center', va='center', weight='bold', color=INK, zorder=5)

    # Negative ions (anions) moving towards Anode (left)
    draw_ion(4.7, 3.4, "−", PINK, DEEP["pink"])
    ax.annotate("", xy=(rx_left + rod_w + 0.1, 3.4), xytext=(4.4, 3.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=15), zorder=5)

    draw_ion(4.9, 2.2, "−", PINK, DEEP["pink"])
    ax.annotate("", xy=(rx_left + rod_w + 0.2, 2.3), xytext=(4.6, 2.25),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=15), zorder=5)

    # Positive ions (cations) moving towards Cathode (right)
    draw_ion(5.1, 2.8, "+", ORANGE, DEEP["orange"])
    ax.annotate("", xy=(rx_right - 0.1, 2.8), xytext=(5.4, 2.8),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=15), zorder=5)

    draw_ion(4.5, 1.7, "+", ORANGE, DEEP["orange"])
    ax.annotate("", xy=(rx_right - 0.3, 1.8), xytext=(4.8, 1.75),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=15), zorder=5)

    # Legend / explanatory annotations at the bottom
    ax.text(2.6, 0.45, "Negative ions migrate to Anode (+)", fontsize=14, color=DEEP["pink"], weight='bold')
    ax.text(5.5, 0.45, "Positive ions migrate to Cathode (−)", fontsize=14, color=DEEP["orange"], weight='bold')

    save(fig, out)
