from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Column x-coordinates
    x_input = 2.0
    x_hidden = 4.5
    x_output = 7.0

    # Node y-coordinates
    # 3 input nodes
    y_input = [4.5, 3.25, 2.0]
    # 4 hidden nodes
    y_hidden = [5.125, 3.875, 2.625, 1.375]
    # 2 output nodes
    y_output = [4.0, 2.5]

    # Draw connection lines first (behind nodes)
    # Input to Hidden
    for yi in y_input:
        for yh in y_hidden:
            ax.plot([x_input, x_hidden], [yi, yh], color=GREY, lw=1.5, zorder=1)

    # Hidden to Output
    for yh in y_hidden:
        for yo in y_output:
            ax.plot([x_hidden, x_output], [yh, yo], color=GREY, lw=1.5, zorder=1)

    # Node radius
    r = 0.32

    # Draw nodes helper
    def draw_nodes(x_pos, y_positions, fill_color, border_color):
        for y in y_positions:
            circle = plt.Circle((x_pos, y), r, facecolor=fill_color, edgecolor=border_color, lw=2.2, zorder=2)
            ax.add_patch(circle)

    draw_nodes(x_input, y_input, BLUE, DEEP["blue"])
    draw_nodes(x_hidden, y_hidden, GREEN, DEEP["green"])
    draw_nodes(x_output, y_output, ORANGE, DEEP["orange"])

    # Column labels above each layer
    label_y = 5.9
    ax.text(x_input, label_y, "Input Layer", ha="center", va="center",
            fontsize=15, weight="bold", color=INK,
            bbox=dict(facecolor="white", edgecolor="none", pad=2.0))
    ax.text(x_hidden, label_y, "Hidden Layer", ha="center", va="center",
            fontsize=15, weight="bold", color=INK,
            bbox=dict(facecolor="white", edgecolor="none", pad=2.0))
    ax.text(x_output, label_y, "Output Layer", ha="center", va="center",
            fontsize=15, weight="bold", color=INK,
            bbox=dict(facecolor="white", edgecolor="none", pad=2.0))

    # Overall title at the top
    ax.text(4.5, 6.25, "Artificial Neural Network", ha="center", va="top",
            fontsize=17, weight="bold", color=INK)

    save(fig, out)
