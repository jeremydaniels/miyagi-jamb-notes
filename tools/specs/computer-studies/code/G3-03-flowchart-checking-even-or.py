from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(9, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Styles
    box_kw = dict(ec=INK, lw=2.0)
    arrow_kw = dict(arrowstyle="-|>", mutation_scale=18, color=INK, lw=2.0)

    # 1. Start (Oval / Rounded Box)
    # Center at (3.5, 10.0)
    start_box = patches.FancyBboxPatch((2.3, 9.6), 2.4, 0.8, boxstyle="round,pad=0.1,rounding_size=0.4",
                                      fc=LAV, **box_kw)
    ax.add_patch(start_box)
    ax.text(3.5, 10.0, "Start", ha='center', va='center', fontsize=16, color=INK, weight='bold')

    # Arrow 1: Start -> Input N
    ax.annotate("", xy=(3.5, 8.8), xytext=(3.5, 9.6), arrowprops=arrow_kw)

    # 2. Input N (Parallelogram)
    # Center at (3.5, 8.3), w=2.8, h=0.8, slant=0.3
    slant = 0.35
    w, h = 2.8, 0.8
    x_c, y_c = 3.5, 8.3
    pts_input = [
        [x_c - w/2 + slant, y_c - h/2],
        [x_c + w/2 + slant, y_c - h/2],
        [x_c + w/2 - slant, y_c + h/2],
        [x_c - w/2 - slant, y_c + h/2]
    ]
    input_box = patches.Polygon(pts_input, closed=True, fc=BLUE, **box_kw)
    ax.add_patch(input_box)
    ax.text(x_c, y_c, "Input N", ha='center', va='center', fontsize=15, color=INK)

    # Arrow 2: Input N -> Process
    ax.annotate("", xy=(3.5, 7.1), xytext=(3.5, 7.9), arrowprops=arrow_kw)

    # 3. Rectangle (R = N MOD 2)
    # Center at (3.5, 6.6), w=3.0, h=0.8
    proc_box = patches.Rectangle((2.0, 6.2), 3.0, 0.8, fc=CREAM, **box_kw)
    ax.add_patch(proc_box)
    ax.text(3.5, 6.6, "R = N MOD 2", ha='center', va='center', fontsize=15, color=INK)

    # Arrow 3: Process -> Decision
    ax.annotate("", xy=(3.5, 5.3), xytext=(3.5, 6.2), arrowprops=arrow_kw)

    # 4. Diamond (Is R == 0?)
    # Center at (3.5, 4.3), dw=1.8, dh=1.0
    dw, dh = 1.8, 1.0
    pts_diamond = [
        [3.5, 4.3 + dh],  # Top: (3.5, 5.3)
        [3.5 + dw, 4.3],  # Right: (5.3, 4.3)
        [3.5, 4.3 - dh],  # Bottom: (3.5, 3.3)
        [3.5 - dw, 4.3]   # Left: (1.7, 4.3)
    ]
    diamond_box = patches.Polygon(pts_diamond, closed=True, fc=ORANGE, **box_kw)
    ax.add_patch(diamond_box)
    ax.text(3.5, 4.3, "Is R == 0?", ha='center', va='center', fontsize=15, color=INK)

    # Branch Right: "Yes" -> Print 'Even'
    # Diamond right edge is at (5.3, 4.3)
    # Arrow to Parallelogram (Print 'Even') centered at (7.2, 4.3)
    ax.annotate("", xy=(5.9, 4.3), xytext=(5.3, 4.3), arrowprops=arrow_kw)
    ax.text(5.55, 4.55, "Yes", ha='center', va='bottom', fontsize=14, color=INK, weight='bold')

    # Parallelogram (Print 'Even')
    x_e, y_e = 7.3, 4.3
    w_p, h_p = 2.4, 0.8
    pts_even = [
        [x_e - w_p/2 + slant, y_e - h_p/2],
        [x_e + w_p/2 + slant, y_e - h_p/2],
        [x_e + w_p/2 - slant, y_e + h_p/2],
        [x_e - w_p/2 - slant, y_e + h_p/2]
    ]
    even_box = patches.Polygon(pts_even, closed=True, fc=GREEN, **box_kw)
    ax.add_patch(even_box)
    ax.text(x_e, y_e, "Print 'Even'", ha='center', va='center', fontsize=15, color=INK)

    # Branch Down: "No" -> Print 'Odd'
    # Diamond bottom edge is at (3.5, 3.3)
    ax.annotate("", xy=(3.5, 2.7), xytext=(3.5, 3.3), arrowprops=arrow_kw)
    ax.text(3.75, 3.0, "No", ha='left', va='center', fontsize=14, color=INK, weight='bold')

    # Parallelogram (Print 'Odd')
    x_o, y_o = 3.5, 2.3
    pts_odd = [
        [x_o - w_p/2 + slant, y_o - h_p/2],
        [x_o + w_p/2 + slant, y_o - h_p/2],
        [x_o + w_p/2 - slant, y_o + h_p/2],
        [x_o - w_p/2 - slant, y_o + h_p/2]
    ]
    odd_box = patches.Polygon(pts_odd, closed=True, fc=GREEN, **box_kw)
    ax.add_patch(odd_box)
    ax.text(x_o, y_o, "Print 'Odd'", ha='center', va='center', fontsize=15, color=INK)

    # 5. Stop (Oval)
    # Centered at (3.5, 0.7)
    stop_box = patches.FancyBboxPatch((2.3, 0.3), 2.4, 0.8, boxstyle="round,pad=0.1,rounding_size=0.4",
                                     fc=PINK, **box_kw)
    ax.add_patch(stop_box)
    ax.text(3.5, 0.7, "Stop", ha='center', va='center', fontsize=16, color=INK, weight='bold')

    # Connect Print 'Odd' down to Stop
    ax.annotate("", xy=(3.5, 1.1), xytext=(3.5, 1.9), arrowprops=arrow_kw)

    # Connect Print 'Even' to Stop
    # Route: Down from bottom of Even (7.3, 3.9) to y=1.5, then left to x=4.9, then into Stop
    # Actually, simpler routing: from bottom of Even (7.3, 3.9) -> (7.3, 0.7) -> Stop right edge (4.7, 0.7)
    ax.plot([7.3, 7.3, 4.7], [3.9, 0.7, 0.7], color=INK, lw=2.0)
    ax.annotate("", xy=(4.7, 0.7), xytext=(5.1, 0.7), arrowprops=arrow_kw)

    save(fig, out)
