from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(6, 9.4, "The Path of Christ (Philippians 2:5–11)", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)

    # Sub-headings for descent and ascent
    ax.text(2.5, 8.8, "Descent (Humiliation)", ha='center', va='center', 
            fontsize=15, fontweight='bold', color=DEEP['orange'])
    ax.text(9.5, 8.8, "Ascent (Exaltation)", ha='center', va='center', 
            fontsize=15, fontweight='bold', color=DEEP['blue'])

    # Coordinates for the V-shape
    # Left descending steps: 5 points from top left to bottom apex
    descent_x = [1.5, 2.3, 3.2, 4.1, 6.0]
    descent_y = [8.0, 6.5, 5.0, 3.5, 1.6]

    # Right ascending steps: bottom apex up to top right
    ascent_x = [6.0, 7.8, 8.7, 9.6, 10.5]
    ascent_y = [1.6, 3.5, 5.0, 6.5, 8.0]

    # Draw arrows along the V
    # Downward path
    ax.annotate("", xy=(descent_x[-1], descent_y[-1]), xytext=(descent_x[0], descent_y[0]),
                arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=4, mutation_scale=20))
    # Upward path
    ax.annotate("", xy=(ascent_x[-1], ascent_y[-1]), xytext=(ascent_x[0], descent_y[-1]),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=4, mutation_scale=20))

    # Descent labels and markers
    descent_labels = [
        "Equal with God",
        "Made Himself of no reputation",
        "Took the form of a servant",
        "Made in human likeness",
        "Obedient to death on a cross"
    ]

    for i in range(4):
        x, y = descent_x[i], descent_y[i]
        ax.plot(x, y, marker='o', markersize=9, color=DEEP['orange'], zorder=4)
        ax.text(x - 0.25, y, descent_labels[i], ha='right', va='center', fontsize=14,
                color=INK, bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='none', alpha=0.9))

    # Bottom apex label ("Obedient to death on a cross")
    ax.plot(6.0, 1.6, marker='o', markersize=11, color=DEEP['pink'], zorder=4)
    ax.text(6.0, 0.9, descent_labels[4], ha='center', va='top', fontsize=15, fontweight='bold',
            color=INK, bbox=dict(boxstyle='round,pad=0.35', facecolor=CREAM, edgecolor=DEEP['pink'], lw=1.5))

    # Ascent labels and markers
    ascent_labels = [
        "Highly exalted by God",
        "Given the Name above all names",
        "Every knee shall bow",
        "Every tongue confess"
    ]

    for i in range(1, 5):
        x, y = ascent_x[i], ascent_y[i]
        ax.plot(x, y, marker='o', markersize=9, color=DEEP['blue'], zorder=4)
        ax.text(x + 0.25, y, ascent_labels[i-1], ha='left', va='center', fontsize=14,
                color=INK, bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='none', alpha=0.9))

    save(fig, out)
