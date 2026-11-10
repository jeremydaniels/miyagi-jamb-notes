from style import *
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # 8 blocks, from bottom to top
    # The bottom and largest block is labeled "Faith".
    # Stacked above it in ascending order:
    # "Virtue", "Knowledge", "Temperance", "Patience", "Godliness", "Brotherly Kindness", "Charity (Love)"
    labels = [
        "Faith",
        "Virtue",
        "Knowledge",
        "Temperance",
        "Patience",
        "Godliness",
        "Brotherly Kindness",
        "Charity (Love)"
    ]

    # Colors for each block (palette from style)
    # Using alternating/balanced bright soft tones with deep outline accents
    block_colors = [
        (BLUE, DEEP["blue"]),
        (GREEN, DEEP["green"]),
        (ORANGE, DEEP["orange"]),
        (LAV, DEEP["lav"]),
        (PINK, DEEP["pink"]),
        (CREAM, DEEP["orange"]),
        (BLUE, DEEP["blue"]),
        (PINK, DEEP["pink"])
    ]

    block_height = 0.82
    gap = 0.08
    y_start = 0.6
    center_x = 5.0

    # Widths linearly decreasing from bottom to top
    widths = [8.2, 7.4, 6.6, 5.8, 5.0, 4.2, 3.5, 2.8]

    for i, label in enumerate(labels):
        w = widths[i]
        h = block_height
        y = y_start + i * (h + gap)
        x = center_x - w / 2.0
        bg_col, edge_col = block_colors[i]

        # Draw block rectangle with rounded corners
        rect = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            facecolor=bg_col,
            edgecolor=edge_col,
            linewidth=2.2
        )
        ax.add_patch(rect)

        # Label inside block
        ax.text(
            center_x, y + h / 2.0,
            label,
            ha="center", va="center",
            fontsize=15.5,
            fontweight="semibold",
            color=INK
        )

    save(fig, out)
