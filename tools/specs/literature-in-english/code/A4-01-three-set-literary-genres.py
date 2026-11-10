from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.2, 5.8)
    ax.set_aspect("equal")
    ax.axis("off")

    # Geometry for 3-set symmetric Venn diagram
    # Top circle: Poetry
    # Bottom-left: Drama
    # Bottom-right: Prose
    r = 3.3
    d = 1.75  # offset from center
    c_drama = (-d * np.cos(np.pi / 6), -d * np.sin(np.pi / 6))   # (-1.515, -0.875)
    c_prose = (d * np.cos(np.pi / 6), -d * np.sin(np.pi / 6))    # (1.515, -0.875)
    c_poetry = (0, d)                                           # (0, 1.75)

    # Draw shaded circles
    circle_drama = patches.Circle(c_drama, r, facecolor=BLUE, edgecolor=DEEP["blue"], linewidth=2.5, alpha=0.35)
    circle_prose = patches.Circle(c_prose, r, facecolor=GREEN, edgecolor=DEEP["green"], linewidth=2.5, alpha=0.35)
    circle_poetry = patches.Circle(c_poetry, r, facecolor=PINK, edgecolor=DEEP["pink"], linewidth=2.5, alpha=0.35)

    ax.add_patch(circle_drama)
    ax.add_patch(circle_prose)
    ax.add_patch(circle_poetry)

    # Title
    ax.text(0, 5.3, "Literary Forms & Shared Features", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Circle Labels (Headings)
    ax.text(-3.3, 0.8, "Drama", fontsize=18, fontweight="bold", ha="center", va="center", color=DEEP["blue"])
    ax.text(3.3, 0.8, "Prose", fontsize=18, fontweight="bold", ha="center", va="center", color=DEEP["green"])
    ax.text(0, 4.4, "Poetry", fontsize=18, fontweight="bold", ha="center", va="center", color=DEEP["pink"])

    # Unique content: Drama
    ax.text(-3.0, -1.5, "Stage directions\nActs / Scenes", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.85))

    # Unique content: Prose
    ax.text(3.0, -1.5, "Chapters\nParagraphs", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.85))

    # Unique content: Poetry
    ax.text(0, 3.2, "Stanzas\nRhyme schemes", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.85))

    # Intersections of two circles:
    # 1. Drama & Poetry (upper-left overlap)
    ax.text(-1.9, 1.7, "Verse\n(Poetic Drama)", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8))

    # 2. Prose & Poetry (upper-right overlap)
    ax.text(1.9, 1.7, "Prose\nPoetry", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8))

    # 3. Drama & Prose (bottom overlap)
    ax.text(0, -2.5, "Extensive\nCharacterisation", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8))

    # Exact centre: overlap of all three
    ax.text(0, 0.05, "Narration\nDialogue\nFigures of Speech\nTheme\nSetting", fontsize=14,
            ha="center", va="center", color=INK, fontweight="semibold",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.0))

    save(fig, out)
