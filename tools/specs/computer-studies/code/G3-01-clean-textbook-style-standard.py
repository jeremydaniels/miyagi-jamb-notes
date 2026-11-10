from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Title
    ax.text(4.5, 10.3, "Standard Flowchart Symbols", fontsize=18, fontweight='bold', 
            ha='center', va='center', color=INK)

    # Style parameters
    fill_col = BLUE
    edge_col = INK
    lw = 2.0
    text_x = 4.2
    sym_cx = 2.2

    # Row 1: Oval - Start / Stop (Terminator)
    # y = 9.2
    y1 = 9.1
    oval = patches.FancyBboxPatch((sym_cx - 1.2, y1 - 0.35), 2.4, 0.7,
                                  boxstyle="round,pad=0.0,rounding_size=0.35",
                                  facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(oval)
    ax.text(text_x, y1, "Start / Stop (Terminator)", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 2: Parallelogram - Input / Output
    # y = 7.8
    y2 = 7.7
    w2, h2, skew = 2.2, 0.75, 0.35
    poly2 = patches.Polygon([
        [sym_cx - w2/2 + skew, y2 - h2/2],
        [sym_cx + w2/2 + skew, y2 - h2/2],
        [sym_cx + w2/2 - skew, y2 + h2/2],
        [sym_cx - w2/2 - skew, y2 + h2/2]
    ], closed=True, facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(poly2)
    ax.text(text_x, y2, "Input / Output", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 3: Rectangle - Process
    # y = 6.3
    y3 = 6.3
    w3, h3 = 2.2, 0.75
    rect = patches.Rectangle((sym_cx - w3/2, y3 - h3/2), w3, h3,
                             facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(rect)
    ax.text(text_x, y3, "Process", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 4: Diamond - Decision
    # y = 4.9
    y4 = 4.9
    w4, h4 = 2.4, 0.95
    diamond = patches.Polygon([
        [sym_cx, y4 + h4/2],
        [sym_cx + w4/2, y4],
        [sym_cx, y4 - h4/2],
        [sym_cx - w4/2, y4]
    ], closed=True, facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(diamond)
    ax.text(text_x, y4, "Decision", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 5: Hexagon - Loop (Preparation)
    # y = 3.5
    y5 = 3.5
    w5, h5, side = 2.4, 0.75, 0.4
    hexagon = patches.Polygon([
        [sym_cx - w5/2, y5],
        [sym_cx - w5/2 + side, y5 + h5/2],
        [sym_cx + w5/2 - side, y5 + h5/2],
        [sym_cx + w5/2, y5],
        [sym_cx + w5/2 - side, y5 - h5/2],
        [sym_cx - w5/2 + side, y5 - h5/2]
    ], closed=True, facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(hexagon)
    ax.text(text_x, y5, "Loop (Preparation)", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 6: Circle - Continuation (Connector)
    # y = 2.1
    y6 = 2.1
    r6 = 0.42
    circle = patches.Circle((sym_cx, y6), r6, facecolor=fill_col, edgecolor=edge_col, linewidth=lw)
    ax.add_patch(circle)
    ax.text(text_x, y6, "Continuation (Connector)", fontsize=15, va='center', color=INK, fontweight='medium')

    # Row 7: Arrow line - Flowline
    # y = 0.8
    y7 = 0.8
    ax.annotate('', xy=(sym_cx + 1.1, y7), xytext=(sym_cx - 1.1, y7),
                arrowprops=dict(arrowstyle="->", color=edge_col, lw=2.4, mutation_scale=22))
    ax.text(text_x, y7, "Flowline", fontsize=15, va='center', color=INK, fontweight='medium')

    # Subtle dividing grid lines between rows
    for div_y in [8.4, 7.0, 5.6, 4.2, 2.8, 1.4]:
        ax.plot([0.8, 8.2], [div_y, div_y], color=GREY, lw=0.75, linestyle=':')

    save(fig, out)
