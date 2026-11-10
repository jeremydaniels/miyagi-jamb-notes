from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 5.9, 'Stress-Beat Diagram (Neutral Intonation)', fontsize=18, fontweight="bold", ha="center", va="top", color=INK)

    # Sentence words along the baseline
    words = ["Tunde", "bought", "a", "new", "bicycle."]
    x_positions = [1.8, 4.0, 5.8, 7.5, 9.8]
    word_y = 1.8
    beat_y = 3.4

    # Horizontal guide line representing the sentence baseline
    ax.plot([0.8, 11.2], [word_y - 0.4, word_y - 0.4], color=GREY, lw=2, zorder=1)

    # Print each word strictly along the horizontal baseline
    for x, w in zip(x_positions, words):
        ax.text(x, word_y, w, fontsize=18, ha="center", va="center", color=INK, fontweight="bold")

    # Beat circles above the words:
    # "Tunde": medium circle
    c1 = plt.Circle((x_positions[0], beat_y), 0.35, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    # "bought": medium circle
    c2 = plt.Circle((x_positions[1], beat_y), 0.35, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    # "a": very small circle
    c3 = plt.Circle((x_positions[2], beat_y), 0.12, facecolor=GREY, edgecolor=INK, lw=1.8, zorder=3)
    # "new": medium circle
    c4 = plt.Circle((x_positions[3], beat_y), 0.35, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    # "bicycle": largest, dark-orange circle
    c5 = plt.Circle((x_positions[4], beat_y), 0.55, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=3.0, zorder=3)

    for c in [c1, c2, c3, c4, c5]:
        ax.add_patch(c)

    # Vertical dotted connector lines from baseline words up to beat circles
    radii = [0.35, 0.35, 0.12, 0.35, 0.55]
    for x, r in zip(x_positions, radii):
        ax.plot([x, x], [word_y + 0.35, beat_y - r], color=GREY, lw=1.5, linestyle=":", zorder=2)

    # Annotation 1: Medium circles -> "stressed content words"
    ax.annotate(
        "stressed\ncontent words",
        xy=(x_positions[1], beat_y + 0.38),
        xytext=(2.9, 4.7),
        fontsize=15,
        fontweight="bold",
        color=DEEP["blue"],
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.8)
    )
    # Secondary arrow from same label to "Tunde"
    ax.annotate(
        "",
        xy=(x_positions[0], beat_y + 0.38),
        xytext=(2.6, 4.7),
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.8)
    )

    # Annotation 2: Small circle -> "unstressed function word"
    ax.annotate(
        "unstressed\nfunction word",
        xy=(x_positions[2], beat_y + 0.15),
        xytext=(5.8, 4.7),
        fontsize=14,
        color=INK,
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5)
    )

    # Annotation 3: Largest circle -> "nuclear (main) stress"
    ax.annotate(
        "nuclear (main)\nstress",
        xy=(x_positions[4], beat_y + 0.6),
        xytext=(9.8, 4.7),
        fontsize=15,
        fontweight="bold",
        color=DEEP["orange"],
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2)
    )

    save(fig, out)
