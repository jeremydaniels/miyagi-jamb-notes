from style import *
import numpy as np

def draw_resistor_h(ax, cx, cy, width=1.4, height=0.45, label="", color=CREAM, label_offset=0.35):
    # Draw rectangular resistor box
    rect = plt.Rectangle((cx - width / 2, cy - height / 2), width, height, 
                         facecolor=color, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(rect)
    if label:
        ax.text(cx, cy + label_offset, label, ha='center', va='bottom', 
                fontsize=16, color=INK, fontweight='bold', zorder=5)

def draw(out):
    fig = canvas(12, 6.5)
    
    # Left subplot: Series Circuit
    ax1 = fig.add_subplot(121)
    ax1.set_xlim(-0.5, 9.5)
    ax1.set_ylim(-1.5, 6.2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Title & Subtitle
    ax1.text(4.5, 5.8, "Series Circuit", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    ax1.text(4.5, 5.15, "Single continuous path", ha='center', va='center', fontsize=14, color=GREY, style='italic')
    
    # Terminals
    t_left = (0.5, 2.5)
    t_right = (8.5, 2.5)
    
    # Continuous wire
    ax1.plot([t_left[0], t_right[0]], [2.5, 2.5], color=INK, lw=2.5, zorder=1)
    
    # Terminal circles
    ax1.scatter([t_left[0], t_right[0]], [2.5, 2.5], s=80, facecolor='white', edgecolor=INK, lw=2, zorder=4)
    ax1.text(t_left[0] - 0.3, 2.5, "A", ha='right', va='center', fontsize=16, fontweight='bold', color=INK)
    ax1.text(t_right[0] + 0.3, 2.5, "B", ha='left', va='center', fontsize=16, fontweight='bold', color=INK)
    
    # Resistors R1, R2, R3
    draw_resistor_h(ax1, 2.2, 2.5, width=1.4, height=0.5, label=r"$R_1$", color=CREAM, label_offset=0.4)
    draw_resistor_h(ax1, 4.5, 2.5, width=1.4, height=0.5, label=r"$R_2$", color=CREAM, label_offset=0.4)
    draw_resistor_h(ax1, 6.8, 2.5, width=1.4, height=0.5, label=r"$R_3$", color=CREAM, label_offset=0.4)
    
    # Current arrow
    ax1.annotate("", xy=(5.2, 1.4), xytext=(3.8, 1.4),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5))
    ax1.text(4.5, 0.9, "Current (I)", ha='center', va='center', fontsize=14, color=DEEP["blue"], fontweight='bold')
    
    # Formula / Note
    ax1.text(4.5, -0.4, r"$R_{\mathrm{total}} = R_1 + R_2 + R_3$", ha='center', va='center', 
             fontsize=15, color=INK, bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=GREY))
    
    # Right subplot: Parallel Circuit
    ax2 = fig.add_subplot(122)
    ax2.set_xlim(-0.5, 9.5)
    ax2.set_ylim(-1.5, 6.2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    # Title & Subtitle with plenty of clearance from R1
    ax2.text(4.5, 5.8, "Parallel Circuit", ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    ax2.text(4.5, 5.15, "Three parallel branches", ha='center', va='center', fontsize=14, color=GREY, style='italic')
    
    # Terminals & Junctions (lowered to leave room for subtitle and R1 label)
    j_left = 2.5
    j_right = 6.5
    y_mid = 2.3
    y_top = 3.6
    y_bot = 1.0
    
    # Leads from outside to junctions
    ax2.plot([0.5, j_left], [y_mid, y_mid], color=INK, lw=2.5, zorder=1)
    ax2.plot([j_right, 8.5], [y_mid, y_mid], color=INK, lw=2.5, zorder=1)
    
    # Vertical junction bus bars
    ax2.plot([j_left, j_left], [y_bot, y_top], color=INK, lw=2.5, zorder=1)
    ax2.plot([j_right, j_right], [y_bot, y_top], color=INK, lw=2.5, zorder=1)
    
    # Branch wires across
    ax2.plot([j_left, j_right], [y_top, y_top], color=INK, lw=2.5, zorder=1)
    ax2.plot([j_left, j_right], [y_mid, y_mid], color=INK, lw=2.5, zorder=1)
    ax2.plot([j_left, j_right], [y_bot, y_bot], color=INK, lw=2.5, zorder=1)
    
    # Junction dots
    ax2.scatter([j_left, j_left, j_left, j_right, j_right, j_right], 
                [y_top, y_mid, y_bot, y_top, y_mid, y_bot], 
                s=60, color=INK, zorder=4)
    
    # Terminal circles
    ax2.scatter([0.5, 8.5], [y_mid, y_mid], s=80, facecolor='white', edgecolor=INK, lw=2, zorder=4)
    ax2.text(0.2, y_mid, "A", ha='right', va='center', fontsize=16, fontweight='bold', color=INK)
    ax2.text(8.8, y_mid, "B", ha='left', va='center', fontsize=16, fontweight='bold', color=INK)
    
    # Resistors R1, R2, R3 on parallel branches
    # y_top is 3.6, with label_offset=0.32, label reaches ~4.0, comfortably below subtitle at 5.15
    draw_resistor_h(ax2, 4.5, y_top, width=1.5, height=0.45, label=r"$R_1$", color=CREAM, label_offset=0.32)
    draw_resistor_h(ax2, 4.5, y_mid, width=1.5, height=0.45, label=r"$R_2$", color=CREAM, label_offset=0.32)
    draw_resistor_h(ax2, 4.5, y_bot, width=1.5, height=0.45, label=r"$R_3$", color=CREAM, label_offset=0.32)
    
    # Formula / Note
    ax2.text(4.5, -0.4, r"$\frac{1}{R_{\mathrm{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$", 
             ha='center', va='center', fontsize=15, color=INK, 
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=GREY))
    
    save(fig, out)
