from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5)
    ax = fig.add_subplot(111)
    ax.axis('off')

    # Left side: Exponential equation
    # 2^3 = 8
    ax.text(0.15, 0.45, "2", fontsize=48, ha="center", va="center", color=INK)
    ax.text(0.2, 0.55, "3", fontsize=32, ha="center", va="center", color=DEEP["blue"])
    ax.text(0.28, 0.45, "=", fontsize=48, ha="center", va="center", color=INK)
    ax.text(0.36, 0.45, "8", fontsize=48, ha="center", va="center", color=DEEP["pink"])

    # Labels for left side
    ax.text(0.15, 0.7, "Base", fontsize=20, ha="center", va="center", color=INK)
    ax.text(0.25, 0.7, "Index", fontsize=20, ha="center", va="center", color=DEEP["blue"])
    ax.text(0.36, 0.7, "Result", fontsize=20, ha="center", va="center", color=DEEP["pink"])

    # Double-headed arrow
    ax.annotate("", xy=(0.42, 0.45), xytext=(0.58, 0.45),
                arrowprops=dict(arrowstyle="<|-|>", color=DEEP["orange"], lw=3, mutation_scale=20))
    ax.text(0.5, 0.55, "Equivalent", fontsize=20, ha="center", va="center", color=DEEP["orange"])

    # Right side: Logarithmic equation
    # log_2 8 = 3
    ax.text(0.66, 0.45, "log", fontsize=48, ha="center", va="center", color=INK)
    ax.text(0.74, 0.38, "2", fontsize=32, ha="center", va="center", color=INK)
    ax.text(0.82, 0.45, "8", fontsize=48, ha="center", va="center", color=DEEP["pink"])
    ax.text(0.9, 0.45, "=", fontsize=48, ha="center", va="center", color=INK)
    ax.text(0.98, 0.45, "3", fontsize=48, ha="center", va="center", color=DEEP["blue"])

    # Labels for right side
    ax.text(0.74, 0.2, "Base", fontsize=20, ha="center", va="center", color=INK)
    ax.text(0.82, 0.2, "Result", fontsize=20, ha="center", va="center", color=DEEP["pink"])
    ax.text(0.98, 0.2, "Index", fontsize=20, ha="center", va="center", color=DEEP["blue"])

    ax.set_xlim(0, 1.1)
    ax.set_ylim(0, 1)

    save(fig, out)
