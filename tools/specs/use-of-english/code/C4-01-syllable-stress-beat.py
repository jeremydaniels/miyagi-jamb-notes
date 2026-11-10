from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(5, 7.0, "Word Stress Patterns", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    # Legend / Key at the top
    # Large circle key
    key_y = 6.2
    c_large_key = plt.Circle((0.9, key_y), 0.28, facecolor=DEEP["orange"], edgecolor=INK, lw=1.5)
    ax.add_patch(c_large_key)
    ax.text(1.35, key_y, "= stressed (loud, long, full vowel)", fontsize=14, color=INK, va="center", ha="left")

    # Small circle key
    c_small_key = plt.Circle((5.7, key_y), 0.14, facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax.add_patch(c_small_key)
    ax.text(6.05, key_y, "= unstressed (quiet, short, often /ə/)", fontsize=14, color=INK, va="center", ha="left")

    # Data for the three rows
    # Each row: (word_label, y_pos, [(syllable_text, is_stressed), ...])
    rows = [
        ("TA – ble", 4.8, [("TA", True), ("ble", False)]),
        ("ba – NA – na", 3.2, [("ba", False), ("NA", True), ("na", False)]),
        ("pho – TO – gra – phy", 1.6, [("pho", False), ("TO", True), ("gra", False), ("phy", False)])
    ]

    r_large = 0.45
    r_small = 0.22

    for word, y_center, syllables in rows:
        # Word title / transcription label on the left
        ax.text(0.8, y_center, word, fontsize=16, fontweight="bold", color=INK, ha="left", va="center")
        
        # Draw background guide line / baseline for rhythm
        ax.plot([3.4, 9.2], [y_center, y_center], color=GREY, lw=1.0, linestyle=":", zorder=1)

        # Positions for syllables along the row
        x_start = 4.0
        x_spacing = 1.35

        for i, (syll, stressed) in enumerate(syllables):
            x = x_start + i * x_spacing
            if stressed:
                circle = plt.Circle((x, y_center), r_large, facecolor=DEEP["orange"], edgecolor=INK, lw=2.0, zorder=3)
                ax.add_patch(circle)
                # Syllable text below circle
                ax.text(x, y_center - r_large - 0.32, syll, fontsize=16, fontweight="bold", color=DEEP["orange"], ha="center", va="top")
            else:
                circle = plt.Circle((x, y_center), r_small, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=3)
                ax.add_patch(circle)
                # Syllable text below circle
                ax.text(x, y_center - r_large - 0.32, syll, fontsize=15, color=INK, ha="center", va="top")

    save(fig, out)
