from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Title
    ax.text(6.0, 7.9, "Hierarchy of Programming Languages", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # Pyramid coordinates
    # Center of pyramid at x = 5.2
    # Base width = 7.0 (from 1.7 to 8.7), top width = 2.2 (from 4.1 to 6.3)
    # Heights for 4 layers:
    # Layer 0 (Hardware): y from 1.0 to 2.4
    # Layer 1 (Machine Language): y from 2.5 to 3.9
    # Layer 2 (Assembly Language): y from 4.0 to 5.4
    # Layer 3 (High-Level Languages): y from 5.5 to 6.9

    cx = 5.0
    layers = [
        {"y0": 1.0, "y1": 2.3, "color": GREY, "deep": INK,
         "title": "Hardware", "sub": "(CPU, Memory, Registers)"},
        {"y0": 2.45, "y1": 3.75, "color": PINK, "deep": DEEP["pink"],
         "title": "Machine Language", "sub": "(1s and 0s)"},
        {"y0": 3.9, "y1": 5.2, "color": ORANGE, "deep": DEEP["orange"],
         "title": "Assembly Language", "sub": "(Mnemonics)"},
        {"y0": 5.35, "y1": 6.65, "color": BLUE, "deep": DEEP["blue"],
         "title": "High-Level Languages", "sub": "(Python, Java, C, etc.)"}
    ]

    # Calculate half-widths linearly with y
    # At y = 0.8, w = 3.8; at y = 7.0, w = 1.3
    def half_width(y):
        return 3.8 - (y - 0.8) * (3.8 - 1.3) / (7.0 - 0.8)

    for lay in layers:
        y0 = lay["y0"]
        y1 = lay["y1"]
        w0 = half_width(y0)
        w1 = half_width(y1)
        
        pts = [
            [cx - w0, y0],
            [cx + w0, y0],
            [cx + w1, y1],
            [cx - w1, y1]
        ]
        poly = Polygon(pts, closed=True, facecolor=lay["color"], edgecolor=lay["deep"], linewidth=2.0)
        ax.add_patch(poly)

        # Labels
        y_mid = (y0 + y1) / 2.0
        ax.text(cx, y_mid + 0.16, lay["title"], ha='center', va='center',
                fontsize=15, weight='bold', color=INK)
        ax.text(cx, y_mid - 0.22, lay["sub"], ha='center', va='center',
                fontsize=14, color=INK)

    # Side Arrows indicating abstraction levels
    # Arrow 1: Pointing Upwards labeled "Closer to human language"
    # Arrow 2: Pointing Downwards labeled "Closer to machine hardware"
    ax_x = 9.8

    # Upward arrow
    ax.annotate('', xy=(ax_x - 0.35, 6.65), xytext=(ax_x - 0.35, 3.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=22))
    ax.text(ax_x + 0.0, 5.27, "Closer to\nhuman language", ha='left', va='center',
            fontsize=14, weight='bold', color=DEEP["blue"])

    # Downward arrow
    ax.annotate('', xy=(ax_x - 0.35, 1.0), xytext=(ax_x - 0.35, 3.75),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.0, mutation_scale=22))
    ax.text(ax_x + 0.0, 2.37, "Closer to\nmachine hardware", ha='left', va='center',
            fontsize=14, weight='bold', color=DEEP["orange"])

    save(fig, out)
