import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)

    # Set up data
    t = [0.0, 0.003, 0.006]
    F = [0.0, 50.0, 0.0]

    # Limits
    xmax = 0.008
    ymax = 60.0

    # Axes setup
    axes_clean(ax, "Time, t (s)", "Force, F (N)", xmax, ymax)

    # Fill area under the triangle
    ax.fill_between(t, F, color=BLUE, alpha=0.5)

    # Draw the triangular force curve
    ax.plot(t, F, color=DEEP["blue"], lw=3.5)

    # Dashed guide lines for peak
    ax.plot([0.003, 0.003], [0, 50], color=GREY, ls="--", lw=1.5)
    ax.plot([0, 0.003], [50, 50], color=GREY, ls="--", lw=1.5)

    # Ticks and custom tick labels
    ax.set_xticks([0.0, 0.003, 0.006])
    ax.set_xticklabels(["0", "0.003", "0.006"], fontsize=14, color=INK)

    ax.set_yticks([0, 25, 50])
    ax.set_yticklabels(["0", "25", "50"], fontsize=14, color=INK)

    # Bold label for the area inside/near the triangle
    ax.text(0.003, 20.0, "Area = Impulse\n= Change in Momentum", 
            fontsize=15, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=3.0))

    save(fig, out)
