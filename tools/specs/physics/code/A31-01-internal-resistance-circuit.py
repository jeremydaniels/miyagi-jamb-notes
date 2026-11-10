from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 7.5)
    ax.axis("off")

    # Circuit coordinates:
    # Loop corners: Bottom-left (1.5, 1.5), Bottom-right (8.5, 1.5),
    # Top-right (8.5, 5.5), Top-left (1.5, 5.5)

    # Wire color & linewidth
    wire_color = INK
    wire_lw = 2.2

    # Top branch: Cell (EMF 'E') + internal resistance 'r'
    # Dashed box around cell + internal resistance
    # Cell is at x ~ 3.2, internal resistance at x ~ 5.2
    
    # 1. Main loop wires
    # Left wire: from (1.5, 1.5) to (1.5, 5.5)
    # Switch is on the left wire or top wire. Let's place Switch on the left wire:
    # Wire from (1.5, 1.5) to (1.5, 3.0), Switch from (1.5, 3.0) to (1.5, 4.0), Wire from (1.5, 4.0) to (1.5, 5.5)
    ax.plot([1.5, 1.5], [1.5, 3.0], color=wire_color, lw=wire_lw)
    ax.plot([1.5, 1.5], [4.0, 5.5], color=wire_color, lw=wire_lw)
    # Switch terminals & blade (closed or slightly open? Closed circuit to show current I)
    ax.scatter([1.5, 1.5], [3.0, 4.0], s=35, color="white", edgecolor=wire_color, lw=2, zorder=5)
    # Closed switch representation
    ax.plot([1.5, 1.5], [3.0, 4.0], color=wire_color, lw=wire_lw)
    ax.text(0.7, 3.5, "Switch", fontsize=14, color=INK, va="center", ha="right")

    # Top wire segments
    ax.plot([1.5, 2.5], [5.5, 5.5], color=wire_color, lw=wire_lw)
    # Inside dashed box:
    # Long plate (positive): at x=3.2, y in [4.9, 6.1]
    # Short plate (negative): at x=3.5, y in [5.15, 5.85]
    ax.plot([2.5, 3.2], [5.5, 5.5], color=wire_color, lw=wire_lw)
    ax.plot([3.2, 3.2], [4.9, 6.1], color=wire_color, lw=3.0) # + plate
    ax.text(3.05, 6.1, "+", fontsize=15, fontweight="bold", color=INK, ha="center")
    
    ax.plot([3.5, 3.5], [5.15, 5.85], color=wire_color, lw=5.0) # - plate
    ax.text(3.65, 6.1, "−", fontsize=15, fontweight="bold", color=INK, ha="center")

    ax.plot([3.5, 4.3], [5.5, 5.5], color=wire_color, lw=wire_lw)

    # Internal resistor 'r' rectangle from x=4.3 to 5.5, height 0.4
    r_rect = patches.Rectangle((4.3, 5.3), 1.2, 0.4, facecolor="white", edgecolor=wire_color, lw=2, zorder=4)
    ax.add_patch(r_rect)

    ax.plot([5.5, 8.5], [5.5, 5.5], color=wire_color, lw=wire_lw)

    # Dashed box around cell & internal resistance
    cell_box = patches.Rectangle((2.3, 4.6), 4.6, 1.8, facecolor="none", edgecolor=DEEP["blue"],
                                 lw=1.8, linestyle="--", zorder=3)
    ax.add_patch(cell_box)
    ax.text(4.6, 6.6, "Cell with internal resistance", fontsize=14, color=DEEP["blue"], ha="center", weight="bold")

    # Labels for E and r
    ax.text(3.35, 4.15, "E (EMF)", fontsize=14, color=INK, ha="center",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(4.9, 4.15, "r (internal resistance)", fontsize=14, color=INK, ha="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Right branch: contains Ammeter 'A'
    ax.plot([8.5, 8.5], [5.5, 4.0], color=wire_color, lw=wire_lw)
    # Ammeter circle at (8.5, 3.5)
    a_circle = patches.Circle((8.5, 3.5), 0.5, facecolor="white", edgecolor=wire_color, lw=2.2, zorder=4)
    ax.add_patch(a_circle)
    ax.text(8.5, 3.5, "A", fontsize=16, weight="bold", ha="center", va="center", color=INK, zorder=5)
    ax.text(9.2, 3.5, "A (ammeter)", fontsize=14, color=INK, va="center", ha="left")

    ax.plot([8.5, 8.5], [3.0, 1.5], color=wire_color, lw=wire_lw)

    # Bottom branch: External Resistor R
    # Wire from (8.5, 1.5) to (6.0, 1.5) and (4.0, 1.5) to (1.5, 1.5)
    ax.plot([8.5, 6.0], [1.5, 1.5], color=wire_color, lw=wire_lw)
    ax.plot([4.0, 1.5], [1.5, 1.5], color=wire_color, lw=wire_lw)

    # Resistor R rectangle from x=4.0 to 6.0, centered at y=1.5
    R_rect = patches.Rectangle((4.0, 1.25), 2.0, 0.5, facecolor=CREAM, edgecolor=wire_color, lw=2.2, zorder=4)
    ax.add_patch(R_rect)
    ax.text(5.0, 1.5, "R", fontsize=15, weight="bold", color=INK, ha="center", va="center", zorder=5)
    ax.text(5.0, 0.85, "R (external resistance)", fontsize=14, color=INK, ha="center")

    # Voltmeter 'V' in parallel across R
    # Junction dots at (3.5, 1.5) and (6.5, 1.5)
    junc1 = patches.Circle((3.4, 1.5), 0.08, facecolor=INK, zorder=6)
    junc2 = patches.Circle((6.6, 1.5), 0.08, facecolor=INK, zorder=6)
    ax.add_patch(junc1)
    ax.add_patch(junc2)

    # Voltmeter parallel branch drops to y = 2.7 or loops below?
    # Better: place voltmeter in parallel above R, at y = 2.6
    ax.plot([3.4, 3.4], [1.5, 2.7], color=wire_color, lw=1.8)
    ax.plot([3.4, 4.5], [2.7, 2.7], color=wire_color, lw=1.8)
    ax.plot([5.5, 6.6], [2.7, 2.7], color=wire_color, lw=1.8)
    ax.plot([6.6, 6.6], [2.7, 1.5], color=wire_color, lw=1.8)

    v_circle = patches.Circle((5.0, 2.7), 0.5, facecolor="white", edgecolor=wire_color, lw=2.2, zorder=4)
    ax.add_patch(v_circle)
    ax.text(5.0, 2.7, "V", fontsize=16, weight="bold", ha="center", va="center", color=INK, zorder=5)
    ax.text(5.0, 3.4, "V (terminal p.d.)", fontsize=14, color=INK, ha="center")

    # Current direction arrows (Conventional current flows clockwise: from + terminal left/downwards? No, + is on left pointing leftwards)
    # + is at x=3.2 facing left, so current flows counter-clockwise or clockwise?
    # Positive plate is on the left (x=3.2), negative is on right (x=3.5).
    # Current leaves positive terminal going left: (2.5, 5.5) -> (1.5, 5.5) -> down left side -> through R to the right -> up right side -> negative terminal.
    # Arrow on left wire pointing down:
    ax.annotate("", xy=(1.5, 2.1), xytext=(1.5, 2.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3, mutation_scale=18))
    # Arrow on bottom wire pointing right:
    ax.annotate("", xy=(7.7, 1.5), xytext=(7.3, 1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3, mutation_scale=18))
    # Arrow on top wire pointing left:
    ax.annotate("", xy=(2.0, 5.5), xytext=(2.3, 5.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=3, mutation_scale=18))
    
    # Label for current direction
    ax.text(1.9, 2.2, "I (current direction)", fontsize=14, color=DEEP["pink"], weight="bold", va="center")

    save(fig, out)
