from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 6.5)
    ax.axis('off')

    # Coordinates
    # Wire AB
    xA, xB = 1.5, 7.5
    y_wire = 3.5

    # Top loop (Driver cell circuit)
    y_top = 5.5

    # Bottom loop (Test cell circuit)
    y_bot = 1.5
    x_jockey = 4.8  # Balance point J

    # Draw Potentiometer Wire AB
    ax.plot([xA, xB], [y_wire, y_wire], color=DEEP['orange'], lw=5, solid_capstyle='round', zorder=2)
    
    # Terminals A and B
    ax.scatter([xA, xB], [y_wire, y_wire], color=INK, s=60, zorder=4)
    ax.text(xA - 0.25, y_wire + 0.15, 'A', fontsize=16, fontweight='bold', color=INK, ha='right', va='center')
    ax.text(xB + 0.25, y_wire + 0.15, 'B', fontsize=16, fontweight='bold', color=INK, ha='left', va='center')

    # Top Driver Circuit wires
    # From A up to y_top, across to B, down to B
    ax.plot([xA, xA], [y_wire, y_top], color=INK, lw=2)
    ax.plot([xB, xB], [y_wire, y_top], color=INK, lw=2)
    
    # Driver cell at top center: (4.0 to 5.0)
    x_cell_mid = 4.5
    ax.plot([xA, x_cell_mid - 0.5], [y_top, y_top], color=INK, lw=2)
    ax.plot([x_cell_mid + 0.5, xB], [y_top, y_top], color=INK, lw=2)

    # Battery symbol for E_driver (Long thin line = +, Short thick line = -)
    # Long plate (+)
    ax.plot([x_cell_mid - 0.15, x_cell_mid - 0.15], [y_top - 0.35, y_top + 0.35], color=INK, lw=2.5)
    # Short plate (-)
    ax.plot([x_cell_mid + 0.15, x_cell_mid + 0.15], [y_top - 0.2, y_top + 0.2], color=INK, lw=4.5)
    # Connect plates to leads
    ax.plot([x_cell_mid - 0.5, x_cell_mid - 0.15], [y_top, y_top], color=INK, lw=2)
    ax.plot([x_cell_mid + 0.15, x_cell_mid + 0.5], [y_top, y_top], color=INK, lw=2)
    # Polarity labels
    ax.text(x_cell_mid - 0.35, y_top + 0.25, '+', fontsize=14, color=INK, ha='center')
    ax.text(x_cell_mid + 0.35, y_top + 0.25, '–', fontsize=14, color=INK, ha='center')
    # Label driver cell
    ax.text(x_cell_mid, y_top + 0.5, r'$E_{\mathrm{driver}}$', fontsize=16, color=INK, ha='center', va='bottom')

    # Rheostat / Key schematic indicator (optional, but keep it clean textbook)
    
    # Secondary Circuit:
    # From A down to y_bot, across to E1, then Galvanometer G, then jockey J
    ax.plot([xA, xA], [y_wire, y_bot], color=INK, lw=2)
    
    # Test cell E1 around x = 2.8
    xE1 = 2.8
    ax.plot([xA, xE1 - 0.4], [y_bot, y_bot], color=INK, lw=2)
    # E1 battery symbol (+ on left to match A)
    ax.plot([xE1 - 0.15, xE1 - 0.15], [y_bot - 0.35, y_bot + 0.35], color=INK, lw=2.5)
    ax.plot([xE1 + 0.15, xE1 + 0.15], [y_bot - 0.2, y_bot + 0.2], color=INK, lw=4.5)
    ax.plot([xE1 - 0.4, xE1 - 0.15], [y_bot, y_bot], color=INK, lw=2)
    ax.plot([xE1 + 0.15, xE1 + 0.4], [y_bot, y_bot], color=INK, lw=2)
    ax.text(xE1 - 0.35, y_bot + 0.25, '+', fontsize=14, color=INK, ha='center')
    ax.text(xE1 + 0.35, y_bot + 0.25, '–', fontsize=14, color=INK, ha='center')
    ax.text(xE1, y_bot - 0.5, r'$E_1$', fontsize=16, color=INK, ha='center', va='top')

    # Wire to Galvanometer at x = 4.2
    xG = 4.2
    ax.plot([xE1 + 0.4, xG - 0.35], [y_bot, y_bot], color=INK, lw=2)
    # Galvanometer circle
    circle = plt.Circle((xG, y_bot), 0.35, facecolor='white', edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(circle)
    ax.text(xG, y_bot, 'G', fontsize=15, fontweight='bold', color=INK, ha='center', va='center', zorder=4)
    # Galvanometer label below
    ax.text(xG, y_bot - 0.5, 'Galvanometer', fontsize=14, color=INK, ha='center', va='top')

    # From Galvanometer to jockey
    ax.plot([xG + 0.35, x_jockey], [y_bot, y_bot], color=INK, lw=2)
    ax.plot([x_jockey, x_jockey], [y_bot, y_wire - 0.1], color=INK, lw=2)
    # Jockey arrowhead touching wire
    ax.annotate('', xy=(x_jockey, y_wire), xytext=(x_jockey, y_wire - 0.7),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2, mutation_scale=15))
    ax.text(x_jockey + 0.2, y_wire - 0.4, 'Jockey (J)', fontsize=14, color=INK, va='center', ha='left')
    ax.text(x_jockey, y_wire + 0.2, 'J', fontsize=16, fontweight='bold', color=INK, ha='center', va='bottom')

    # Balance length annotation below wire
    y_bar = 2.7
    ax.annotate('', xy=(xA, y_bar), xytext=(x_jockey, y_bar),
                arrowprops=dict(arrowstyle="<->", color=DEEP['blue'], lw=1.8))
    ax.plot([xA, xA], [y_wire - 0.2, y_bar - 0.2], color=GREY, lw=1, ls='--')
    ax.plot([x_jockey, x_jockey], [y_wire - 0.2, y_bar - 0.2], color=GREY, lw=1, ls='--')
    ax.text((xA + x_jockey) / 2, y_bar + 0.1, r"balance length $l$", fontsize=15, color=DEEP['blue'],
            ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=2))

    # Wire label
    ax.text((xA + xB) / 2, y_wire + 0.35, 'Uniform resistance wire AB', fontsize=14, color=INK,
            ha='center', va='bottom', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))

    save(fig, out)
