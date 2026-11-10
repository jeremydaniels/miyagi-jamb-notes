from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "Buffer Stock Scheme", fontsize=18, weight="bold", ha="center", va="center", color=INK)

    # 1. Left side: Bumper Harvest
    # Box for Bumper Harvest
    ax.annotate(
        "Bumper Harvest\n(Oversupply)",
        xy=(2.0, 5.4),
        ha="center", va="center",
        fontsize=14, weight="bold", color=INK,
        bbox=dict(boxstyle="round,pad=0.6", fc=GREEN, ec=DEEP["green"], lw=2)
    )

    # 2. Right side: Poor Harvest
    # Box for Poor Harvest
    ax.annotate(
        "Poor Harvest\n(Scarcity)",
        xy=(10.0, 5.4),
        ha="center", va="center",
        fontsize=14, weight="bold", color=INK,
        bbox=dict(boxstyle="round,pad=0.6", fc=PINK, ec=DEEP["pink"], lw=2)
    )

    # 3. Center Top: Government Silo
    # Silo representation
    ax.annotate(
        "Government Silo\n(Buffer Stock)",
        xy=(6.0, 5.4),
        ha="center", va="center",
        fontsize=15, weight="bold", color=INK,
        bbox=dict(boxstyle="round,pad=0.7", fc=BLUE, ec=DEEP["blue"], lw=2.5)
    )

    # Arrow Left -> Center: "Government Buys Excess to Stop Prices Falling"
    ax.annotate(
        "", xy=(4.65, 5.4), xytext=(3.35, 5.4),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"], mutation_scale=20)
    )
    ax.text(
        4.0, 5.95,
        "Government Buys Excess\nto Stop Prices Falling",
        fontsize=14, ha="center", va="bottom", color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1)
    )

    # Arrow Center -> Right Market: "Government Sells Reserves to Stop Prices Rising"
    # To right side
    ax.annotate(
        "", xy=(8.65, 5.4), xytext=(7.35, 5.4),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["pink"], mutation_scale=20)
    )
    ax.text(
        8.0, 5.95,
        "Government Sells Reserves\nto Stop Prices Rising",
        fontsize=14, ha="center", va="bottom", color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1)
    )

    # Market stall label near Poor Harvest
    ax.text(
        10.0, 4.3,
        "Market Stall\n(Supplied from reserves)",
        fontsize=14, ha="center", va="center", color=INK,
        bbox=dict(boxstyle="square,pad=0.4", fc=CREAM, ec=ORANGE, lw=1.5)
    )
    # Downward small arrow to Market Stall from Poor harvest
    ax.annotate(
        "", xy=(10.0, 4.7), xytext=(10.0, 4.9),
        arrowprops=dict(arrowstyle="->", lw=1.8, color=INK)
    )

    # 4. Center Bottom: Balanced Scale for "Stable Prices and Stable Farmer Incomes"
    # Arrows from Silo down to Balanced Scale
    ax.annotate(
        "", xy=(6.0, 3.2), xytext=(6.0, 4.7),
        arrowprops=dict(arrowstyle="->", lw=2, color=DEEP["lav"], mutation_scale=18)
    )

    # Draw a balanced scale icon schematically
    # Base triangle
    ax.plot([5.7, 6.3], [2.1, 2.1], color=INK, lw=2.5)
    ax.plot([5.7, 6.0, 6.3], [2.1, 2.6, 2.1], color=INK, lw=2.5)
    # Vertical pillar
    ax.plot([6.0, 6.0], [2.6, 3.1], color=INK, lw=3)
    # Horizontal crossbeam (balanced)
    ax.plot([5.0, 7.0], [3.1, 3.1], color=INK, lw=3)
    # Left pan strings & pan
    ax.plot([5.0, 4.7], [3.1, 2.6], color=INK, lw=1.5)
    ax.plot([5.0, 5.3], [3.1, 2.6], color=INK, lw=1.5)
    pan_l = patches.Arc((5.0, 2.6), 0.7, 0.4, theta1=180, theta2=360, color=INK, lw=2)
    ax.add_patch(pan_l)
    # Right pan strings & pan
    ax.plot([7.0, 6.7], [3.1, 2.6], color=INK, lw=1.5)
    ax.plot([7.0, 7.3], [3.1, 2.6], color=INK, lw=1.5)
    pan_r = patches.Arc((7.0, 2.6), 0.7, 0.4, theta1=180, theta2=360, color=INK, lw=2)
    ax.add_patch(pan_r)

    # Box for Balanced Scale Result
    ax.annotate(
        "Stable Prices and Stable Farmer Incomes",
        xy=(6.0, 1.2),
        ha="center", va="center",
        fontsize=16, weight="bold", color=INK,
        bbox=dict(boxstyle="round,pad=0.6", fc=CREAM, ec=DEEP["orange"], lw=2.5)
    )

    save(fig, out)
