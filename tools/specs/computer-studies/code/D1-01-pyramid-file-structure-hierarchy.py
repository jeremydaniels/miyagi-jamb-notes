from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw(out):
    # Canvas setup
    fig = canvas(10, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Hierarchy data from top to bottom
    # Top is narrowest, bottom is widest
    levels = [
        {"title": "Database", "example": "(e.g., 'School_System')", "color": LAV, "edge": DEEP["lav"]},
        {"title": "File", "example": "(e.g., 'SS3_Students.txt')", "color": BLUE, "edge": DEEP["blue"]},
        {"title": "Record", "example": "(e.g., 'Musa, 17, SS3')", "color": GREEN, "edge": DEEP["green"]},
        {"title": "Field", "example": "(e.g., 'First Name')", "color": CREAM, "edge": DEEP["orange"]},
        {"title": "Data Item", "example": "(e.g., 'Musa')", "color": ORANGE, "edge": DEEP["orange"]},
        {"title": "Character", "example": "(e.g., 'M')", "color": PINK, "edge": DEEP["pink"]},
    ]

    n_levels = len(levels)
    y_start = 1.0
    layer_height = 0.95
    layer_gap = 0.12

    center_x = 5.0
    top_half_w = 2.1 # widened to prevent text overlap in the top blocks
    bot_half_w = 4.4

    # Title at the top
    ax.text(center_x, 8.0, "File Structure Hierarchy", fontsize=18, fontweight='bold',
            ha='center', va='center', color=INK)

    for i, lvl in enumerate(levels):
        # i = 0 is Database (top), i = 5 is Character (bottom)
        # Calculate vertical position from bottom to top
        layer_idx_from_bottom = n_levels - 1 - i
        y_bot = y_start + layer_idx_from_bottom * (layer_height + layer_gap)
        y_top = y_bot + layer_height

        # Fractional positions across entire pyramid height (0 at bottom base, 1 at top peak)
        total_span = n_levels * (layer_height + layer_gap) - layer_gap
        f_bot = (y_bot - y_start) / total_span
        f_top = (y_top - y_start) / total_span

        w_bot = bot_half_w - f_bot * (bot_half_w - top_half_w)
        w_top = bot_half_w - f_top * (bot_half_w - top_half_w)

        # Polygon coordinates for trapezoid
        poly_x = [center_x - w_bot, center_x + w_bot, center_x + w_top, center_x - w_top]
        poly_y = [y_bot, y_bot, y_top, y_top]

        # Draw trapezoid
        ax.fill(poly_x, poly_y, color=lvl["color"], ec=lvl["edge"], lw=2.2, zorder=2)

        # Text label (title and example)
        y_mid = (y_bot + y_top) / 2.0
        
        # Split text into two lines if it's the top level to avoid overlap if it's still tight
        if i <= 1:
            label_text = f"{lvl['title']}\n{lvl['example']}"
        else:
            label_text = f"{lvl['title']}  {lvl['example']}"
            
        ax.text(center_x, y_mid, label_text, fontsize=14, fontweight='semibold',
                ha='center', va='center', color=INK, zorder=3)

    # Hierarchy side arrows/labels
    # Arrow showing increasing scope / aggregation
    arrow_x = 0.35
    ax.annotate('', xy=(arrow_x, 7.3), xytext=(arrow_x, 1.1),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0), zorder=4)
    ax.text(arrow_x + 0.18, 4.2, "Increasing Aggregation", fontsize=14, color=INK,
            rotation=90, va='center', ha='left')

    save(fig, out)
