from style import *
import numpy as np

def draw_cell_horiz(ax, cx, cy, d=0.25, h_long=0.9, h_short=0.5, lw=2.5):
    # Left is long (+), right is short (-)
    # Long plate at cx - d/2
    ax.plot([cx - d/2, cx - d/2], [cy - h_long/2, cy + h_long/2], color=INK, lw=lw, solid_capstyle='round')
    # Short plate at cx + d/2
    ax.plot([cx + d/2, cx + d/2], [cy - h_short/2, cy + h_short/2], color=INK, lw=lw*1.8, solid_capstyle='round')

def draw_cell_vert(ax, cx, cy, d=0.22, w_long=0.8, w_short=0.45, lw=2.5):
    # Top is long (+), bottom is short (-)
    # Long plate at cy + d/2
    ax.plot([cx - w_long/2, cx + w_long/2], [cy + d/2, cy + d/2], color=INK, lw=lw, solid_capstyle='round')
    # Short plate at cy - d/2
    ax.plot([cx - w_short/2, cx + w_short/2], [cy - d/2, cy - d/2], color=INK, lw=lw*1.8, solid_capstyle='round')

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Titles
    ax.text(3.0, 5.8, "Cells in Series", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(9.0, 5.8, "Cells in Parallel", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Divider line between two diagrams
    ax.plot([6.0, 6.0], [0.8, 5.8], color=GREY, lw=1.2, linestyle='--')

    # ==================== LEFT: SERIES ====================
    # 3 cells connected end-to-end at y = 3.2
    # Centers of the 3 cells: x = 2.0, 3.0, 4.0
    y_s = 3.2
    xs = [2.0, 3.0, 4.0]
    d_plate = 0.22

    # Draw wire running through and connecting them
    # Left terminal from x = 0.8 to (xs[0] - d_plate/2)
    ax.plot([0.8, xs[0] - d_plate/2], [y_s, y_s], color=INK, lw=2.5)
    # Between cell 1 and 2
    ax.plot([xs[0] + d_plate/2, xs[1] - d_plate/2], [y_s, y_s], color=INK, lw=2.5)
    # Between cell 2 and 3
    ax.plot([xs[1] + d_plate/2, xs[2] - d_plate/2], [y_s, y_s], color=INK, lw=2.5)
    # Right terminal from (xs[2] + d_plate/2) to 5.2
    ax.plot([xs[2] + d_plate/2, 5.2], [y_s, y_s], color=INK, lw=2.5)

    # Terminals dots
    ax.scatter([0.8, 5.2], [y_s, y_s], s=40, color=INK, zorder=5)

    # Draw cells
    for x in xs:
        draw_cell_horiz(ax, x, y_s, d=d_plate, h_long=0.9, h_short=0.5)
        # Individual cell voltage label E
        ax.text(x, y_s + 0.75, "E", fontsize=15, ha='center', va='bottom', color=DEEP['blue'])

    # +/- polarity indicators for series
    ax.text(0.9, y_s + 0.25, "+", fontsize=16, ha='center', va='bottom', color=INK)
    ax.text(5.1, y_s + 0.25, "−", fontsize=16, ha='center', va='bottom', color=INK)

    # Total voltage dimension / bracket below
    y_dim_s = 1.6
    ax.plot([0.8, 0.8], [y_s - 0.3, y_dim_s], color=GREY, lw=1.5, linestyle=':')
    ax.plot([5.2, 5.2], [y_s - 0.3, y_dim_s], color=GREY, lw=1.5, linestyle=':')
    ax.annotate("", xy=(5.2, y_dim_s), xytext=(0.8, y_dim_s),
                arrowprops=dict(arrowstyle="<->", color=DEEP['pink'], lw=2))
    ax.text(3.0, y_dim_s - 0.45, "Total Voltage = 3E", fontsize=16, fontweight='bold',
            ha='center', va='top', color=DEEP['pink'],
            bbox=dict(fc="white", ec="none", pad=2))

    # ==================== RIGHT: PARALLEL ====================
    # 3 battery symbols arranged vertically
    # Common top wire at y = 4.4, common bottom wire at y = 2.0
    # Branches at x = 7.8, 9.0, 10.2
    y_top = 4.4
    y_bot = 2.0
    y_cells = [3.2, 3.2, 3.2] # each cell placed in vertical branch at y=3.2
    x_branches = [7.8, 9.0, 10.2]

    # Top horizontal bus from 7.2 to 10.2 (with terminal at 7.2)
    ax.plot([7.2, 10.2], [y_top, y_top], color=INK, lw=2.5)
    # Bottom horizontal bus from 7.2 to 10.2 (with terminal at 7.2)
    ax.plot([7.2, 10.2], [y_bot, y_bot], color=INK, lw=2.5)

    # Terminal dots on the left
    ax.scatter([7.2, 7.2], [y_top, y_bot], s=40, color=INK, zorder=5)

    # Terminal labels
    ax.text(6.85, y_top, "+", fontsize=17, ha='center', va='center', color=INK)
    ax.text(6.85, y_bot, "−", fontsize=17, ha='center', va='center', color=INK)

    # Vertical branches with cells
    d_vert_plate = 0.22
    for x in x_branches:
        # Branch wire from top bus to top plate (+)
        ax.plot([x, x], [y_top, 3.2 + d_vert_plate/2], color=INK, lw=2.5)
        # Branch wire from bottom plate (-) to bottom bus
        ax.plot([x, x], [3.2 - d_vert_plate/2, y_bot], color=INK, lw=2.5)
        # Draw cell
        draw_cell_vert(ax, x, 3.2, d=d_vert_plate, w_long=0.75, w_short=0.42)
        # Junction dots on top and bottom bus
        ax.scatter([x, x], [y_top, y_bot], s=30, color=INK, zorder=4)
        # Label E for each cell
        ax.text(x + 0.55, 3.2, "E", fontsize=15, ha='left', va='center', color=DEEP['blue'])

    # Total voltage dimension for parallel on the left side
    x_dim_p = 6.4
    ax.annotate("", xy=(x_dim_p, y_top), xytext=(x_dim_p, y_bot),
                arrowprops=dict(arrowstyle="<->", color=DEEP['pink'], lw=2))
    ax.text(x_dim_p - 0.15, (y_top + y_bot)/2, "Total Voltage = E", fontsize=16, fontweight='bold',
            ha='right', va='center', color=DEEP['pink'], rotation=90)

    save(fig, out)
