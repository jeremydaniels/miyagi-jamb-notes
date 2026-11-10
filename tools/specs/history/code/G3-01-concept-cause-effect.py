from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Center circle for "African Discontent"
    center_x, center_y = 6.0, 4.25
    center_r = 1.6

    circle = patches.Circle(
        (center_x, center_y),
        center_r,
        facecolor=CREAM,
        edgecolor=DEEP["orange"],
        linewidth=3.5,
        zorder=3
    )
    ax.add_patch(circle)

    ax.text(
        center_x, center_y,
        "African\nDiscontent",
        ha="center", va="center",
        fontsize=18, fontweight="bold",
        color=INK, zorder=4
    )

    # 3 categories of causes: Political (top-left), Economic (top-right), Social (bottom)
    # Positions and contents
    cards = [
        {
            "title": "Political",
            "color": PINK,
            "border": DEEP["pink"],
            "box_xy": (0.4, 5.0),
            "box_wh": (3.6, 2.7),
            "text": "• Loss of sovereignty\n• Exclusion of elites\n• Harsh laws like indigénat",
            "arrow_start": (4.1, 5.7),
            "arrow_end": (5.0, 5.1)
        },
        {
            "title": "Economic",
            "color": GREEN,
            "border": DEEP["green"],
            "box_xy": (7.8, 5.0),
            "box_wh": (4.0, 2.7),
            "text": "• Land alienation\n• Heavy taxation\n• Forced labour\n• Low prices for cash crops",
            "arrow_start": (7.7, 5.7),
            "arrow_end": (7.0, 5.1)
        },
        {
            "title": "Social",
            "color": BLUE,
            "border": DEEP["blue"],
            "box_xy": (3.9, 0.5),
            "box_wh": (4.2, 2.4),
            "text": "• Racial discrimination\n• Poor education\n• Separate settlements",
            "arrow_start": (6.0, 3.0),
            "arrow_end": (6.0, 3.8)
        }
    ]

    for card in cards:
        bx, by = card["box_xy"]
        bw, bh = card["box_wh"]

        # Card container
        rect = patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.15,rounding_size=0.3",
            facecolor=card["color"],
            edgecolor=card["border"],
            linewidth=2.5,
            zorder=2
        )
        ax.add_patch(rect)

        # Title of category
        ax.text(
            bx + bw / 2.0, by + bh - 0.45,
            card["title"],
            ha="center", va="center",
            fontsize=16, fontweight="bold",
            color=card["border"],
            zorder=3
        )

        # Content bullets
        ax.text(
            bx + 0.25, by + (bh - 0.45) / 2.0,
            card["text"],
            ha="left", va="center",
            fontsize=14, color=INK,
            linespacing=1.45,
            zorder=3
        )

        # Large prominent pointing arrow into central circle
        sx, sy = card["arrow_start"]
        ex, ey = card["arrow_end"]
        arrow = patches.FancyArrowPatch(
            (sx, sy), (ex, ey),
            arrowstyle="-|>,head_length=12,head_width=9",
            color=card["border"],
            linewidth=4.5,
            zorder=3
        )
        ax.add_patch(arrow)

    # Main diagram title
    ax.text(
        6.0, 8.1,
        "Causes of African Discontent under Colonial Rule",
        ha="center", va="center",
        fontsize=18, fontweight="bold",
        color=INK
    )

    save(fig, out)
