from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Truncated pyramid geometry to ensure enough width for top layer text
    # Base at y = 1.0, Top at y = 6.8
    y_levels = [6.8, 5.64, 4.48, 3.32, 2.16, 1.0]
    
    def get_x_bounds(y):
        # Base half-width = 4.0, Top half-width = 2.4
        hw = 4.0 - (y - 1.0) * (4.0 - 2.4) / (6.8 - 1.0)
        return 6.0 - hw, 6.0 + hw

    colors = [
        (CREAM, DEEP["orange"]),
        (LAV, DEEP["lav"]),
        (BLUE, DEEP["blue"]),
        (GREEN, DEEP["green"]),
        (GREY, INK)
    ]

    labels = [
        ("Administrative Class", "(Permanent Secretaries, Directors)"),
        ("Professional/Technical Class", "(Doctors, Engineers, Lawyers)"),
        ("Executive Class", "(Executive Officers)"),
        ("Clerical Class", "(Clerks, Typists)"),
        ("Auxiliary/Manipulative Class", "(Cleaners, Messengers)")
    ]

    # Draw pyramid layers from top to bottom
    for i in range(5):
        y_top = y_levels[i]
        y_bot = y_levels[i+1]
        
        x_top_l, x_top_r = get_x_bounds(y_top)
        x_bot_l, x_bot_r = get_x_bounds(y_bot)
        
        verts = [(x_top_l, y_top), (x_top_r, y_top), (x_bot_r, y_bot), (x_bot_l, y_bot)]
        fill_col, edge_col = colors[i]
        
        poly = Polygon(verts, closed=True, facecolor=fill_col, edgecolor=edge_col, linewidth=2.0)
        ax.add_patch(poly)
        
        # Center of current layer
        y_center = (y_top + y_bot) / 2.0
        title_text, subtitle_text = labels[i]
        
        ax.text(6.0, y_center + 0.18, title_text, ha='center', va='center',
                fontsize=14.5, fontweight='bold', color=INK)
        ax.text(6.0, y_center - 0.22, subtitle_text, ha='center', va='center',
                fontsize=14, color=INK)

    # Title at the top
    ax.text(6.0, 7.15, "Hierarchical Structure of the Civil Service", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Left Arrow: pointing upwards, "Increasing Authority and Salary"
    arrow_left_x = 1.0
    ax.annotate(
        "", 
        xy=(arrow_left_x, 6.6), 
        xytext=(arrow_left_x, 1.2),
        arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.0, mutation_scale=22)
    )
    ax.text(arrow_left_x - 0.35, 3.9, "Increasing Authority and Salary", 
            ha='center', va='center', rotation=90, fontsize=15, fontweight='bold', color=INK)

    # Right Arrow: pointing downwards, "Increasing Number of Staff"
    arrow_right_x = 11.0
    ax.annotate(
        "", 
        xy=(arrow_right_x, 1.2), 
        xytext=(arrow_right_x, 6.6),
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=22)
    )
    ax.text(arrow_right_x + 0.35, 3.9, "Increasing Number of Staff", 
            ha='center', va='center', rotation=-90, fontsize=15, fontweight='bold', color=INK)

    save(fig, out)
