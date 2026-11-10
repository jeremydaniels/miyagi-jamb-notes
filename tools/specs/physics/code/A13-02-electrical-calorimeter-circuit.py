from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Color palette aliases
    outer_lagging = CREAM
    inner_beaker = GREY
    liquid_color = BLUE
    deep_blue = DEEP['blue']
    deep_orange = DEEP['orange']
    deep_green = DEEP['green']

    # --- Calorimeter and Lagging ---
    # Outer lagging jacket
    lag_rect = patches.Rectangle((1.5, 0.8), 4.2, 4.0, fc=outer_lagging, ec=INK, lw=2, zorder=2)
    ax.add_patch(lag_rect)
    
    # Lagging pattern/hatching indication
    ax.text(1.7, 1.0, "lagging", fontsize=14, color=GREY, rotation=90, zorder=3)

    # Inner calorimeter vessel
    inner_rect = patches.Rectangle((2.0, 1.2), 3.2, 3.4, fc='white', ec=INK, lw=2, zorder=3)
    ax.add_patch(inner_rect)

    # Liquid inside
    liq_rect = patches.Rectangle((2.05, 1.25), 3.1, 2.7, fc=liquid_color, ec='none', alpha=0.5, zorder=4)
    ax.add_patch(liq_rect)
    # Liquid surface line
    ax.plot([2.05, 5.15], [3.95, 3.95], color=deep_blue, lw=1.8, zorder=5)

    # Lid / Stopper
    lid = patches.Rectangle((1.8, 4.6), 3.6, 0.4, fc=CREAM, ec=INK, lw=2, zorder=6)
    ax.add_patch(lid)

    # --- Immersion Heater ---
    # Coil / heater element
    heater_body = patches.Rectangle((3.3, 1.5), 0.6, 1.8, fc=PINK, ec=DEEP['pink'], lw=2, zorder=6)
    ax.add_patch(heater_body)
    # Coils lines
    for y_coil in np.linspace(1.7, 3.1, 6):
        ax.plot([3.3, 3.9], [y_coil, y_coil], color=DEEP['pink'], lw=1.5, zorder=7)

    # Heater stems going up through lid
    ax.plot([3.4, 3.4], [3.3, 5.5], color=INK, lw=2, zorder=7)
    ax.plot([3.8, 3.8], [3.3, 5.5], color=INK, lw=2, zorder=7)

    # --- Thermometer ---
    # Glass tube
    ax.plot([2.5, 2.5], [1.8, 6.2], color=INK, lw=3, zorder=7)
    # Bulb
    t_bulb = patches.Circle((2.5, 1.8), 0.18, fc=DEEP['orange'], ec=INK, lw=1.5, zorder=8)
    ax.add_patch(t_bulb)
    # Mercury thread
    ax.plot([2.5, 2.5], [1.8, 4.8], color=DEEP['orange'], lw=1.5, zorder=9)

    # --- Stirrer ---
    # Stirrer rod & loop
    ax.plot([4.6, 4.6], [1.8, 5.8], color=GREY, lw=2.5, zorder=7)
    stirrer_loop = patches.Circle((4.6, 1.8), 0.35, fill=False, ec=GREY, lw=2.5, zorder=7)
    ax.add_patch(stirrer_loop)
    # Handle
    ax.plot([4.3, 4.9], [5.8, 5.8], color=INK, lw=3, zorder=8)

    # --- Circuit Components ---
    # Terminals on heater top: (3.4, 5.5) and (3.8, 5.5)
    # Right wire to Ammeter, Switch, DC Supply, then back to left terminal
    
    # Ammeter 'A'
    a_x, a_y = 6.2, 5.5
    circ_a = patches.Circle((a_x, a_y), 0.45, fc='white', ec=INK, lw=2, zorder=10)
    ax.add_patch(circ_a)
    ax.text(a_x, a_y, "A", fontsize=16, weight='bold', ha='center', va='center', zorder=11, color=INK)

    # Voltmeter 'V' in parallel with heater
    v_x, v_y = 3.6, 6.8
    circ_v = patches.Circle((v_x, v_y), 0.45, fc='white', ec=INK, lw=2, zorder=10)
    ax.add_patch(circ_v)
    ax.text(v_x, v_y, "V", fontsize=16, weight='bold', ha='center', va='center', zorder=11, color=INK)

    # Voltmeter parallel connections
    ax.plot([3.4, 3.4, 3.15, 3.15], [5.5, 6.8, 6.8, 6.8], color=INK, lw=2, zorder=5)
    ax.plot([3.8, 3.8, 4.05, 4.05], [5.5, 6.8, 6.8, 6.8], color=INK, lw=2, zorder=5)
    # Dots for junctions
    ax.plot([3.4, 3.8], [5.5, 5.5], 'o', color=INK, markersize=5, zorder=10)

    # Main series circuit
    # From heater right lead (3.8, 5.5) -> Ammeter (5.75, 5.5)
    ax.plot([3.8, 5.75], [5.5, 5.5], color=INK, lw=2, zorder=5)

    # From Ammeter (6.65, 5.5) -> Switch -> DC Supply -> (1.0, 7.3) -> (1.0, 5.5) -> heater left lead (3.4, 5.5)
    ax.plot([6.65, 7.8, 7.8], [5.5, 5.5, 6.2], color=INK, lw=2, zorder=5)
    
    # Switch at (7.8, 6.4)
    ax.plot([7.8, 7.8], [6.2, 6.3], color=INK, lw=2, zorder=5)
    ax.plot([7.8], [6.3], 'o', color=INK, markersize=4, zorder=6)
    ax.plot([7.8, 7.55], [6.3, 6.8], color=INK, lw=2, zorder=5) # Open/tilted blade
    ax.plot([7.8], [6.9], 'o', color=INK, markersize=4, zorder=6)
    ax.plot([7.8, 7.8, 7.3], [6.9, 7.5, 7.5], color=INK, lw=2, zorder=5)

    # DC Power Supply at y=7.5, x around 6.5
    # Long plate (positive)
    ax.plot([7.1, 7.1], [7.2, 7.8], color=INK, lw=2.5, zorder=6)
    ax.text(7.1, 8.0, "+", fontsize=15, ha='center', va='center', weight='bold')
    # Short plate (negative)
    ax.plot([6.8, 6.8], [7.35, 7.65], color=INK, lw=4, zorder=6)
    ax.text(6.8, 8.0, "–", fontsize=15, ha='center', va='center', weight='bold')

    # Supply text
    ax.text(6.95, 7.1, "d.c. supply", fontsize=14, ha='center', va='top', color=INK)

    # Connect from DC supply back to heater left lead
    ax.plot([6.8, 1.2, 1.2, 3.4], [7.5, 7.5, 5.5, 5.5], color=INK, lw=2, zorder=5)

    # --- Labels & Annotations with exact required texts ---
    # "thermometer"
    ax.annotate("thermometer", xy=(2.5, 5.0), xytext=(1.2, 6.3),
                fontsize=15, color=INK, ha='right', va='center',
                bbox=dict(fc='white', ec='none', pad=2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # "stirrer"
    ax.annotate("stirrer", xy=(4.6, 4.5), xytext=(6.2, 4.3),
                fontsize=15, color=INK, ha='left', va='center',
                bbox=dict(fc='white', ec='none', pad=2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # "immersion heater"
    ax.annotate("immersion heater", xy=(3.9, 2.3), xytext=(6.0, 2.3),
                fontsize=15, color=INK, ha='left', va='center',
                bbox=dict(fc='white', ec='none', pad=2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # "liquid"
    ax.annotate("liquid", xy=(3.0, 3.2), xytext=(1.0, 3.2),
                fontsize=15, color=INK, ha='right', va='center',
                bbox=dict(fc='white', ec='none', pad=2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # "lagged calorimeter"
    ax.annotate("lagged calorimeter", xy=(1.5, 2.0), xytext=(1.0, 1.4),
                fontsize=15, color=INK, ha='right', va='center',
                bbox=dict(fc='white', ec='none', pad=2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    save(fig, out)
