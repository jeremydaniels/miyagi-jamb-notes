from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 5.8, "Islamic Legal Spectrum of Actions", fontsize=18, weight="bold", ha="center", va="center", color=INK)

    # Gradient spectrum bar in the middle
    # Left: Halal (Green), Middle: Mushtabihat (Yellow/Grey blend), Right: Haram (Red/Deep Pink)
    colors = ["#2ecc71", "#70c27f", "#d6d895", "#dcd088", "#d8b08c", "#e27c7c", "#e74c3c"]
    cmap = LinearSegmentedColormap.from_list("halal_haram", colors, N=256)

    # Draw gradient bar
    gradient = np.linspace(0, 1, 500).reshape(1, -1)
    bar_y = 2.7
    bar_h = 1.2
    bar_x = 1.0
    bar_w = 10.0
    ax.imshow(gradient, extent=[bar_x, bar_x + bar_w, bar_y, bar_y + bar_h], aspect="auto", cmap=cmap, zorder=2)

    # Outline for the spectrum bar
    rect_outline = patches.Rectangle((bar_x, bar_y), bar_w, bar_h, fill=False, edgecolor=INK, lw=2.0, zorder=3)
    ax.add_patch(rect_outline)

    # Dividing zones (dashed lines on the bar)
    ax.plot([4.3, 4.3], [bar_y, bar_y + bar_h], color=INK, lw=1.5, linestyle="--", zorder=4)
    ax.plot([7.7, 7.7], [bar_y, bar_y + bar_h], color=INK, lw=1.5, linestyle="--", zorder=4)

    # Three "Traffic Light" Indicator Discs above the bar
    # Halal light (Green)
    circle_halal = patches.Circle((2.65, 4.5), 0.45, facecolor="#2ecc71", edgecolor=INK, lw=2, zorder=5)
    ax.add_patch(circle_halal)

    # Mushtabihat light (Muted yellow-grey)
    circle_doubt = patches.Circle((6.0, 4.5), 0.45, facecolor="#e0d68a", edgecolor=INK, lw=2, zorder=5)
    ax.add_patch(circle_doubt)

    # Haram light (Red)
    circle_haram = patches.Circle((9.35, 4.5), 0.45, facecolor="#e74c3c", edgecolor=INK, lw=2, zorder=5)
    ax.add_patch(circle_haram)

    # Labels below the spectrum bar with clean boxes
    # Left: Halal (Clearly Lawful)
    ax.text(2.65, 2.0, "Halal", fontsize=16, weight="bold", ha="center", va="center", color=DEEP["green"])
    ax.text(2.65, 1.45, "(Clearly Lawful)", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1))

    # Middle: Mushtabihat (Doubtful Matters - Avoid)
    ax.text(6.0, 2.0, "Mushtabihat", fontsize=16, weight="bold", ha="center", va="center", color="#856404")
    ax.text(6.0, 1.45, "(Doubtful Matters - Avoid)", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1))

    # Right: Haram (Clearly Unlawful)
    ax.text(9.35, 2.0, "Haram", fontsize=16, weight="bold", ha="center", va="center", color=DEEP["pink"])
    ax.text(9.35, 1.45, "(Clearly Unlawful)", fontsize=14, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1))

    # Descriptive note / ruling guideline
    ax.text(6.0, 0.6, "Permissible (Clear)  ←  Leave what makes you doubt  →  Prohibited (Clear)",
            fontsize=14, ha="center", va="center", color=INK, style="italic")

    save(fig, out)
