from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-6.2, 6.8)
    ax.axis("off")

    # Title
    ax.text(0, 6.2, "Checks and Balances in the Oyo Empire", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Node positions (equilateral triangle layout)
    # Alaafin at top, Oyomesi at bottom-right, Ogboni at bottom-left
    pos = {
        "Alaafin": np.array([0.0, 4.2]),
        "Oyomesi": np.array([3.6, -2.6]),
        "Ogboni": np.array([-3.6, -2.6])
    }

    # Helper function to draw rounded boxes for nodes
    def draw_node(center, title, subtitle, fill_color, border_color):
        w, h = 3.6, 1.5
        x, y = center[0] - w / 2, center[1] - h / 2
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15,rounding_size=0.3",
                                     fc=fill_color, ec=border_color, lw=2.5, zorder=3)
        ax.add_patch(box)
        ax.text(center[0], center[1] + 0.22, title, ha="center", va="center",
                fontsize=16, weight="bold", color=INK, zorder=4)
        ax.text(center[0], center[1] - 0.25, subtitle, ha="center", va="center",
                fontsize=14, fontstyle="italic", color=INK, zorder=4)

    draw_node(pos["Alaafin"], "Alaafin", "(King / Monarch)", CREAM, DEEP["orange"])
    draw_node(pos["Oyomesi"], "Oyomesi", "(Council of Chiefs)", BLUE, DEEP["blue"])
    draw_node(pos["Ogboni"], "Ogboni", "(Earth Cult / Elders)", GREEN, DEEP["green"])

    # Draw arrows with labels
    # 1. Alaafin -> Oyomesi (Consultation)
    ax.annotate("", xy=(3.0, -1.6), xytext=(0.8, 3.4),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=DEEP["blue"],
                                mutation_scale=22, shrinkA=0, shrinkB=0))
    ax.text(3.3, 1.4, "Must be consulted on\nmajor state matters",
            ha="center", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))

    # 2. Oyomesi -> Alaafin (Calabash rejection)
    ax.annotate("", xy=(-0.4, 3.3), xytext=(2.0, -1.8),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=DEEP["orange"],
                                mutation_scale=22, shrinkA=0, shrinkB=0))
    ax.text(0.1, 0.4, "Can present an empty calabash\nto force his suicide",
            ha="center", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))

    # 3. Oyomesi -> Ogboni (Approval of calabash)
    ax.annotate("", xy=(-1.7, -3.1), xytext=(1.7, -3.1),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=DEEP["pink"],
                                mutation_scale=22, shrinkA=0, shrinkB=0))
    ax.text(0, -3.9, "Ogboni must approve the\npresentation of the empty calabash",
            ha="center", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))

    # 4. Ogboni -> Alaafin (Mediator / check)
    ax.annotate("", xy=(-0.9, 3.4), xytext=(-2.9, -1.6),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=DEEP["green"],
                                mutation_scale=22, shrinkA=0, shrinkB=0))
    
    # 5. Ogboni -> Oyomesi (Check on Oyomesi)
    ax.annotate("", xy=(1.7, -2.2), xytext=(-1.7, -2.2),
                arrowprops=dict(arrowstyle="-|>", lw=2.2, color=DEEP["green"],
                                mutation_scale=22, shrinkA=0, shrinkB=0))

    # Unified label for Ogboni's dual checks
    ax.text(-3.4, 1.4, "Acts as a mediator and\nreligious check on both\nAlaafin and Oyomesi",
            ha="center", va="center", fontsize=14, color=INK, weight="bold",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.2))

    save(fig, out)
