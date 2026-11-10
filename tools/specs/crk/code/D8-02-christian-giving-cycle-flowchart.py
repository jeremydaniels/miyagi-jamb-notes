from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw(out):
    fig = canvas(10, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title
    ax.text(5, 7.5, "The Cycle of Christian Giving (2 Corinthians 9)", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Box properties and positions
    # 4 stages arranged in a clear rectangular/diamond cycle
    stages = [
        {
            "text": "God provides seeds (resources)\nto the giver",
            "pos": (5, 6.2),
            "color": CREAM,
            "border": DEEP["orange"]
        },
        {
            "text": "The Christian gives cheerfully\nand bountifully",
            "pos": (8.1, 3.8),
            "color": BLUE,
            "border": DEEP["blue"]
        },
        {
            "text": "The needs of the saints\nare met",
            "pos": (5, 1.4),
            "color": GREEN,
            "border": DEEP["green"]
        },
        {
            "text": "The receivers give thanks\nand glory to God",
            "pos": (1.9, 3.8),
            "color": LAV,
            "border": DEEP["lav"]
        }
    ]

    # Draw boxes
    for s in stages:
        ax.text(s["pos"][0], s["pos"][1], s["text"],
                ha="center", va="center", fontsize=15, color=INK,
                bbox=dict(boxstyle="round,pad=0.7", facecolor=s["color"], 
                          edgecolor=s["border"], lw=2.5))

    # Arrows connecting the cycle
    arrow_props = dict(arrowstyle="-|>", mutation_scale=22, lw=2.5, color=INK)

    # 1. God provides -> Christian gives (Top to Right)
    ax.annotate("", xy=(8.1, 4.6), xytext=(6.8, 6.2),
                arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_props))

    # 2. Christian gives -> Needs met (Right to Bottom)
    ax.annotate("", xy=(6.6, 1.4), xytext=(8.1, 3.0),
                arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_props))

    # 3. Needs met -> Receivers give thanks (Bottom to Left)
    ax.annotate("", xy=(1.9, 3.0), xytext=(3.4, 1.4),
                arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_props))

    # 4. Receivers give thanks -> God (Left to Top)
    ax.annotate("", xy=(3.2, 6.2), xytext=(1.9, 4.6),
                arrowprops=dict(connectionstyle="arc3,rad=-0.2", **arrow_props))

    save(fig, out)
