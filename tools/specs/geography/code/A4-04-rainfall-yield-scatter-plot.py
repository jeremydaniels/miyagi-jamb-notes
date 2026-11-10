import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)

    # Set up axes
    axes_clean(ax, "Annual Rainfall (mm)", "Crop Yield (tonnes)", 1000, 10)

    # Generate synthetic data with a clear positive correlation
    np.random.seed(42)
    n_points = 55
    x = np.random.uniform(150, 900, n_points)
    # Linear trend: y ≈ 1.0 + 0.0085 * x + noise
    noise = np.random.normal(0, 0.65, n_points)
    y = 1.0 + 0.0085 * x + noise

    # Clip y to reasonable positive bounds within axes
    y = np.clip(y, 0.5, 9.2)

    # Plot scatter points
    ax.scatter(
        x, y,
        s=55,
        color=BLUE,
        edgecolor=DEEP["blue"],
        linewidth=1.2,
        alpha=0.9,
        zorder=3,
        label="Observed data"
    )

    # Line of best fit
    x_line = np.linspace(120, 920, 100)
    # Fit line using linear regression
    slope, intercept = np.polyfit(x, y, 1)
    y_line = slope * x_line + intercept

    ax.plot(
        x_line, y_line,
        color=DEEP["orange"],
        lw=3.0,
        zorder=4,
        label="Line of best fit"
    )

    # Annotation explaining the trend / correlation
    ax.annotate(
        "Positive correlation:\nhigher rainfall is associated\nwith higher crop yield",
        xy=(550, slope * 550 + intercept),
        xytext=(320, 7.8),
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        ha="center",
        va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4", lw=1.2),
        zorder=5
    )

    # Grid lines to assist textbook clarity
    ax.grid(True, linestyle="--", alpha=0.35, color=GREY, zorder=1)

    # Legend
    ax.legend(
        loc="lower right",
        frameon=True,
        fontsize=14,
        edgecolor=GREY,
        facecolor="white",
        framealpha=0.95
    )

    # Axis limits
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 10)

    save(fig, out)
