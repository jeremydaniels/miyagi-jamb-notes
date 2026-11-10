import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc
from style import *

def draw(out):
    fig = canvas(14, 8)
    
    # Left: Self-Inductance, Right: Mutual Inductance
    ax1 = fig.add_axes([0.04, 0.05, 0.44, 0.88])
    ax2 = fig.add_axes([0.52, 0.05, 0.44, 0.88])
    
    for ax in [ax1, ax2]:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

    # Helper function to draw a solenoid coil
    def draw_coil(ax, x_start, x_end, y_center, radius, n_turns, color=DEEP["blue"]):
        xs = np.linspace(x_start, x_end, n_turns)
        pitch = (x_end - x_start) / n_turns
        # Draw soft core cylinder inside
        core = patches.Rectangle((x_start - 0.2, y_center - radius * 0.75), 
                                 (x_end - x_start) + 0.4, radius * 1.5, 
                                 fc=CREAM, ec=GREY, lw=1.5, zorder=1)
        ax.add_patch(core)
        
        # Draw back turns (dashed/light) and front turns (solid)
        for i in range(n_turns):
            xc = xs[i]
            # Back arc
            arc_back = Arc((xc, y_center), pitch, radius * 2, angle=0, theta1=90, theta2=270,
                           color=color, lw=2.5, ls="--", alpha=0.5, zorder=2)
            # Front arc
            arc_front = Arc((xc + pitch * 0.5, y_center), pitch, radius * 2, angle=0, theta1=270, theta2=90,
                            color=color, lw=3.0, zorder=3)
            ax.add_patch(arc_back)
            ax.add_patch(arc_front)

    # Helper function to draw switch
    def draw_switch(ax, x, y, closed=False):
        ax.plot([x - 0.4, x - 0.15], [y, y], color=INK, lw=2.5)
        ax.plot([x + 0.15, x + 0.4], [y, y], color=INK, lw=2.5)
        ax.plot(x - 0.15, y, 'o', color=INK, ms=4)
        ax.plot(x + 0.15, y, 'o', color=INK, ms=4)
        if closed:
            ax.plot([x - 0.15, x + 0.15], [y, y], color=INK, lw=2.5)
        else:
            ax.plot([x - 0.15, x + 0.1], [y, y + 0.3], color=INK, lw=2.5)
        ax.text(x, y - 0.4, "Switch", ha='center', va='top', fontsize=14, color=INK)

    # Helper function to draw battery
    # Left plate: positive (+), long; Right plate: negative (–), short & thick
    def draw_battery(ax, x, y):
        ax.plot([x - 0.3, -0.08 + x], [y, y], color=INK, lw=2.5)
        ax.plot([x - 0.08, x - 0.08], [y - 0.35, y + 0.35], color=INK, lw=3)
        ax.plot([x + 0.08, x + 0.08], [y - 0.2, y + 0.2], color=INK, lw=4)
        ax.plot([x + 0.08, x + 0.3], [y, y], color=INK, lw=2.5)
        ax.text(x - 0.15, y + 0.45, "+", ha='center', va='center', fontsize=14, fontweight='bold', color=INK)
        ax.text(x + 0.15, y + 0.45, "–", ha='center', va='center', fontsize=14, fontweight='bold', color=INK)
        ax.text(x, y - 0.4, "Battery", ha='center', va='top', fontsize=14, color=INK)

    # ================= PANEL 1: Self-Inductance =================
    ax1.set_title("Self-Inductance", fontsize=18, fontweight='bold', pad=15, color=INK)
    
    # Coil
    draw_coil(ax1, 2.8, 7.2, 5.5, 0.9, 7, color=DEEP["blue"])
    ax1.text(5.0, 5.5, "Iron core", ha='center', va='center', fontsize=14, color=INK, 
             bbox=dict(fc='white', ec='none', pad=2), zorder=2)

    # Circuit connecting coil to battery and switch
    wire_color = INK
    ax1.plot([2.8, 1.8, 1.8, 3.5], [5.5 - 0.9, 5.5 - 0.9, 2.0, 2.0], color=wire_color, lw=2.5)
    draw_switch(ax1, 4.0, 2.0, closed=False)
    ax1.plot([4.4, 4.8, 4.8, 7.2], [2.0, 2.0, 5.5 + 0.9, 5.5 + 0.9], color=wire_color, lw=2.5)
    # Put battery on left vertical leg or bottom rail correctly
    # Let's connect battery cleanly on bottom rail:
    # Redo wiring for ax1 cleanly:
    # Left side: from coil (x=2.8, y=4.6) down to (1.8, 2.0)
    # Positive terminal of battery at x=2.5, facing left; current leaves + to the left and up to coil
    ax1.cla()
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title("Self-Inductance", fontsize=18, fontweight='bold', pad=15, color=INK)

    draw_coil(ax1, 2.8, 7.2, 5.5, 0.9, 7, color=DEEP["blue"])
    ax1.text(5.0, 5.5, "Iron core", ha='center', va='center', fontsize=14, color=INK, 
             bbox=dict(fc='white', ec='none', pad=2), zorder=2)

    # Wires
    # Coil bottom-left terminal at (2.8, 4.6), top-right terminal at (7.2, 6.4)
    # Left wire down to rail: (2.8, 4.6) -> (1.8, 4.6) -> (1.8, 2.0) -> (2.8, 2.0)
    ax1.plot([2.8, 1.8, 1.8, 2.8], [4.6, 4.6, 2.0, 2.0], color=wire_color, lw=2.5)
    # Battery at (3.3, 2.0): + at 3.22, - at 3.38
    draw_battery(ax1, 3.3, 2.0)
    # From battery (-) at 3.6 to switch at 5.5
    ax1.plot([3.6, 5.1], [2.0, 2.0], color=wire_color, lw=2.5)
    draw_switch(ax1, 5.5, 2.0, closed=False)
    # From switch (5.9) to right side (8.2, 2.0) -> (8.2, 6.4) -> (7.2, 6.4)
    ax1.plot([5.9, 8.2, 8.2, 7.2], [2.0, 2.0, 6.4, 6.4], color=wire_color, lw=2.5)

    # Current arrow (battery current): flows AWAY from positive terminal (+ is at x=3.22, pointing left)
    # Current flows left along bottom rail: from 3.0 towards 2.0, then up to the coil
    arr_i = FancyArrowPatch((2.7, 2.0), (1.9, 2.0), arrowstyle='->', mutation_scale=18, color=DEEP["blue"], lw=2.5)
    ax1.add_patch(arr_i)
    ax1.text(2.3, 2.4, "Current, $I$", ha='center', va='bottom', fontsize=14, color=DEEP["blue"], fontweight='bold')

    # Current goes UP through left wire into coil:
    arr_i_up = FancyArrowPatch((1.8, 2.8), (1.8, 3.8), arrowstyle='->', mutation_scale=16, color=DEEP["blue"], lw=2.2)
    ax1.add_patch(arr_i_up)

    # Magnetic field lines expanding around the coil
    for r_y in [1.5, 2.2, 2.9]:
        ellipse = patches.Arc((5.0, 5.5), 5.5, r_y * 2, angle=0, theta1=15, theta2=165, 
                              color=DEEP["green"], lw=2.0, ls=':')
        ellipse_bot = patches.Arc((5.0, 5.5), 5.5, r_y * 2, angle=0, theta1=195, theta2=345, 
                                  color=DEEP["green"], lw=2.0, ls=':')
        ax1.add_patch(ellipse)
        ax1.add_patch(ellipse_bot)
        # Small field direction arrows
        ax1.annotate("", xy=(5.2, 5.5 + r_y), xytext=(4.8, 5.5 + r_y),
                     arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0))
        ax1.annotate("", xy=(4.8, 5.5 - r_y), xytext=(5.2, 5.5 - r_y),
                     arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0))

    ax1.text(5.0, 8.8, "Expanding magnetic\nfield lines (flux)", ha='center', va='center', 
             fontsize=14, color=DEEP["green"], bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Forward current enters coil from left and travels towards right.
    # Induced back e.m.f. arrow points opposite to battery current (points right to left)
    arr_emf = FancyArrowPatch((6.8, 4.0), (3.2, 4.0), arrowstyle='->', mutation_scale=20, 
                              color=DEEP["pink"], lw=3.0)
    ax1.add_patch(arr_emf)
    ax1.text(5.0, 3.5, 'Induced "back e.m.f."\n(opposes battery current)', ha='center', va='top', 
             fontsize=14, fontweight='bold', color=DEEP["pink"], 
             bbox=dict(fc='white', ec=DEEP["pink"], boxstyle='round,pad=0.3'))

    # ================= PANEL 2: Mutual Inductance =================
    ax2.set_title("Mutual Inductance", fontsize=18, fontweight='bold', pad=15, color=INK)

    # Primary coil (left) & Secondary coil (right)
    draw_coil(ax2, 1.8, 4.2, 5.5, 0.85, 5, color=DEEP["blue"])
    draw_coil(ax2, 5.8, 8.2, 5.5, 0.85, 5, color=DEEP["orange"])

    ax2.text(3.0, 7.0, "Primary coil", ha='center', va='bottom', fontsize=15, fontweight='bold', color=DEEP["blue"])
    ax2.text(7.0, 7.0, "Secondary coil", ha='center', va='bottom', fontsize=15, fontweight='bold', color=DEEP["orange"])

    # Circuit for Primary: switch and battery
    # Left wire down: (1.8, 4.65) -> (0.9, 4.65) -> (0.9, 2.0) -> (1.6, 2.0)
    ax2.plot([1.8, 0.9, 0.9, 1.6], [5.5 - 0.85, 5.5 - 0.85, 2.0, 2.0], color=wire_color, lw=2.5)
    draw_battery(ax2, 2.1, 2.0)
    ax2.plot([2.4, 3.1], [2.0, 2.0], color=wire_color, lw=2.5)
    draw_switch(ax2, 3.5, 2.0, closed=False)
    ax2.plot([3.9, 4.7, 4.7, 4.2], [2.0, 2.0, 5.5 + 0.85, 5.5 + 0.85], color=wire_color, lw=2.5)

    # Battery current arrow on primary pointing away from positive terminal (leftwards)
    arr_ip = FancyArrowPatch((1.6, 2.0), (1.0, 2.0), arrowstyle='->', mutation_scale=16, color=DEEP["blue"], lw=2.2)
    ax2.add_patch(arr_ip)

    # Circuit for Secondary: Galvanometer
    ax2.plot([5.8, 5.3, 5.3, 6.4], [5.5 - 0.85, 5.5 - 0.85, 2.0, 2.0], color=wire_color, lw=2.5)
    # Galvanometer circle at (7.0, 2.0)
    g_circ = patches.Circle((7.0, 2.0), 0.55, fc='white', ec=INK, lw=2.2, zorder=4)
    ax2.add_patch(g_circ)
    ax2.text(7.0, 2.0, "G", ha='center', va='center', fontsize=16, fontweight='bold', color=INK, zorder=5)
    # Galvanometer needle deflecting
    ax2.annotate("", xy=(7.2, 2.3), xytext=(6.9, 1.8),
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.0), zorder=6)
    ax2.text(7.0, 1.1, "Galvanometer", ha='center', va='top', fontsize=14, color=INK)
    ax2.plot([7.6, 8.8, 8.8, 8.2], [2.0, 2.0, 5.5 + 0.85, 5.5 + 0.85], color=wire_color, lw=2.5)

    # Expanding magnetic field lines from Primary cutting through Secondary
    for dy, rx, ry in [(0.8, 4.8, 1.4), (1.5, 5.4, 2.2), (2.2, 6.0, 3.0)]:
        arc_top = patches.Arc((3.5, 5.5), rx, ry, angle=0, theta1=20, theta2=160, 
                              color=DEEP["green"], lw=2.0, ls=':')
        arc_bot = patches.Arc((3.5, 5.5), rx, ry, angle=0, theta1=200, theta2=340, 
                              color=DEEP["green"], lw=2.0, ls=':')
        ax2.add_patch(arc_top)
        ax2.add_patch(arc_bot)
        # Field arrows towards secondary
        ax2.annotate("", xy=(4.8, 5.5 + ry/2), xytext=(4.3, 5.5 + ry/2),
                     arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=1.8))

    ax2.text(5.0, 8.8, "Magnetic field lines cut\nthrough secondary coil", ha='center', va='center', 
             fontsize=14, color=DEEP["green"], bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Induced current in secondary label
    arr_ind = FancyArrowPatch((7.6, 3.2), (6.4, 3.2), arrowstyle='->', mutation_scale=18, 
                              color=DEEP["pink"], lw=2.5)
    ax2.add_patch(arr_ind)
    ax2.text(7.0, 3.5, "Induced secondary\ncurrent", ha='center', va='bottom', 
             fontsize=14, fontweight='bold', color=DEEP["pink"],
             bbox=dict(fc='white', ec=DEEP["pink"], boxstyle='round,pad=0.2'))

    save(fig, out)
