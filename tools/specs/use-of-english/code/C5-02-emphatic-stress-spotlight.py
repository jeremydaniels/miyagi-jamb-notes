import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
from style import *

def draw(out):
    # Canvas size: wide enough to comfortably separate sentence, arrows, and speech bubbles
    fig = canvas(14, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title
    ax.text(7, 8.4, "Sentence Stress & Meaning (The Spotlight Effect)", 
            fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    words = ["MY", "FATHER", "BOUGHT", "A", "NEW", "CAR", "YESTERDAY"]
    focus_indices = [0, 1, 2, 4, 5, 6]
    
    questions = [
        "Your friend's father?",
        "Your mother?",
        "Did he sell one?",
        "A used car?",
        "A new bus?",
        "Last week?"
    ]

    # Word horizontal layout: starting at 0.7, ending well before speech bubbles
    # Sentence spans roughly from x = 0.7 to x = 8.6
    word_widths = [0.85, 1.45, 1.5, 0.45, 0.95, 0.85, 2.1]
    start_x = 0.65

    word_x = []
    curr = start_x
    for w in word_widths:
        word_x.append(curr + w / 2.0)
        curr += w

    # Row vertical positions
    y_positions = np.linspace(7.2, 1.2, 6)

    spotlight_color = CREAM
    spotlight_edge = ORANGE

    for row_idx, (f_idx, q_text) in enumerate(zip(focus_indices, questions)):
        y = y_positions[row_idx]
        fx = word_x[f_idx]
        fw = word_widths[f_idx]

        # Spotlight beam coming from above
        beam_top_y = y + 0.58
        beam_bot_y = y - 0.32
        beam_pts = [
            [fx - 0.15, beam_top_y],
            [fx + 0.15, beam_top_y],
            [fx + fw * 0.52, beam_bot_y],
            [fx - fw * 0.52, beam_bot_y]
        ]
        beam = Polygon(beam_pts, closed=True, facecolor=spotlight_color, 
                       edgecolor=spotlight_edge, linewidth=1.2, alpha=0.45, zorder=1)
        ax.add_patch(beam)

        # Highlight oval / rounded base under the word
        base_patch = FancyBboxPatch((fx - fw * 0.48, y - 0.26), fw * 0.96, 0.52,
                                    boxstyle="round,pad=0.08,rounding_size=0.18",
                                    facecolor=spotlight_color, edgecolor=DEEP["orange"],
                                    linewidth=1.5, alpha=0.85, zorder=2)
        ax.add_patch(base_patch)

        # Render sentence words
        for w_i, word in enumerate(words):
            wx = word_x[w_i]
            if w_i == f_idx:
                ax.text(wx, y, word, fontsize=16, fontweight="bold",
                        color=DEEP["orange"], ha="center", va="center", zorder=4)
            else:
                ax.text(wx, y, word, fontsize=14, fontweight="normal",
                        color=GREY, ha="center", va="center", zorder=3)

        # Connecting dashed cue / arrow towards speech bubble
        # Words end around x = 8.8. Arrow spans 9.15 to 9.75.
        ax.annotate("", xy=(9.75, y), xytext=(9.15, y),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5, ls="--"))

        # Speech bubble on the right: placed safely from x = 9.9 to 13.5
        bubble_x = 9.9
        bubble_w = 3.6
        bubble_h = 0.68
        bubble = FancyBboxPatch((bubble_x, y - bubble_h / 2.0), bubble_w, bubble_h,
                                boxstyle="round,pad=0.08,rounding_size=0.2",
                                facecolor="white", edgecolor=DEEP["blue"],
                                linewidth=1.6, zorder=3)
        ax.add_patch(bubble)

        # Little pointer tail on speech bubble pointing back towards sentence
        tail_pts = [
            [bubble_x, y + 0.12],
            [bubble_x - 0.18, y],
            [bubble_x, y - 0.12]
        ]
        tail = Polygon(tail_pts, closed=True, facecolor="white", 
                       edgecolor=DEEP["blue"], linewidth=1.6, zorder=4)
        ax.add_patch(tail)

        # Question text inside speech bubble
        ax.text(bubble_x + bubble_w / 2.0, y, q_text,
                fontsize=14.5, fontweight="bold", color=INK,
                ha="center", va="center", zorder=5)

    save(fig, out)
