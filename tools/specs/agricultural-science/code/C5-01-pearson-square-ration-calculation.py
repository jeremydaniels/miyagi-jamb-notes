from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Pearson Square coordinates
    sq_x, sq_y, sq_w, sq_h = 3.5, 2.0, 3.0, 3.0
    center_x = sq_x + sq_w / 2.0
    center_y = sq_y + sq_h / 2.0

    # Draw the main square
    rect = patches.Rectangle(
        (sq_x, sq_y), sq_w, sq_h,
        linewidth=2.5,
        edgecolor=DEEP["blue"],
        facecolor=CREAM,
        alpha=0.35,
        zorder=1
    )
    ax.add_patch(rect)

    # Diagonal arrows crossing the box:
    # 1. From bottom-left (Fish meal, 70) up to top-right (54 parts Sorghum)
    ax.annotate(
        "",
        xy=(sq_x + sq_w - 0.15, sq_y + sq_h - 0.15),
        xytext=(sq_x + 0.15, sq_y + 0.15),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["orange"],
            lw=2.5,
            mutation_scale=20
        ),
        zorder=2
    )

    # 2. From top-left (Sorghum, 10) down to bottom-right (6 parts Fish meal)
    ax.annotate(
        "",
        xy=(sq_x + sq_w - 0.15, sq_y + 0.15),
        xytext=(sq_x + 0.15, sq_y + sq_h - 0.15),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["green"],
            lw=2.5,
            mutation_scale=20
        ),
        zorder=2
    )

    # Center target label with white background
    ax.text(
        center_x, center_y,
        "16% (Target)",
        fontsize=16,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["blue"], lw=1.8),
        zorder=3
    )

    # Top-left label: "Sorghum (10%)"
    ax.text(
        sq_x - 0.25, sq_y + sq_h,
        "Sorghum (10%)",
        fontsize=15,
        fontweight="bold",
        color=INK,
        ha="right",
        va="center"
    )

    # Bottom-left label: "Fish meal (70%)"
    ax.text(
        sq_x - 0.25, sq_y,
        "Fish meal (70%)",
        fontsize=15,
        fontweight="bold",
        color=INK,
        ha="right",
        va="center"
    )

    # Top-right label: "70 - 16 = 54 parts of Sorghum"
    ax.text(
        sq_x + sq_w + 0.25, sq_y + sq_h,
        "70 - 16 = 54 parts of Sorghum",
        fontsize=15,
        fontweight="bold",
        color=INK,
        ha="left",
        va="center"
    )

    # Bottom-right label: "16 - 10 = 6 parts of Fish meal"
    ax.text(
        sq_x + sq_w + 0.25, sq_y,
        "16 - 10 = 6 parts of Fish meal",
        fontsize=15,
        fontweight="bold",
        color=INK,
        ha="left",
        va="center"
    )

    # Total parts below the square
    ax.text(
        center_x, sq_y - 0.9,
        "Total parts = 54 + 6 = 60",
        fontsize=16,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5", fc=CREAM, ec=GREY, lw=1.2)
    )

    # Title at the top
    ax.text(
        center_x, 6.2,
        "Pearson Square Formulation",
        fontsize=18,
        fontweight="bold",
        color=INK,
        ha="center",
        va="center"
    )

    save(fig, out)
