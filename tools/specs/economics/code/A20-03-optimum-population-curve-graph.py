from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Population Size", "Per Capita Income", 10, 10)

    # Bell-shaped curve rising from near origin, peaking, and falling
    x = np.linspace(0.4, 9.6, 300)
    # Scaled Gaussian or smooth inverted parabola/bell shape
    # Peak at x = 5.0, peak height = 8.0, falls towards axes
    y = 8.0 * np.exp(-((x - 5.0) ** 2) / (2 * 1.9 ** 2))

    # Plot the curve
    ax.plot(x, y, color=DEEP["blue"], lw=3.5)

    # Dotted vertical line from peak to x-axis
    peak_x = 5.0
    peak_y = 8.0
    ax.plot([peak_x, peak_x], [0, peak_y], color=INK, lw=2.0, linestyle=":")

    # Shading areas under the curve
    mask_left = x <= peak_x
    mask_right = x >= peak_x
    ax.fill_between(x[mask_left], 0, y[mask_left], color=BLUE, alpha=0.18)
    ax.fill_between(x[mask_right], 0, y[mask_right], color=ORANGE, alpha=0.18)

    # Label the regions under the curve
    ax.text(2.6, 2.8, "Under-population", fontsize=15, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=3, alpha=0.85))
    ax.text(7.4, 2.8, "Over-population", fontsize=15, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=3, alpha=0.85))

    # Peak dot
    ax.scatter([peak_x], [peak_y], color=DEEP["blue"], s=50, zorder=5)

    # Label "Optimum Population" at the x-axis where the dotted line meets it
    ax.annotate("Optimum Population",
                xy=(peak_x, 0), xytext=(peak_x, -1.0),
                fontsize=15, color=INK, ha="center", va="top",
                annotation_clip=False)

    # Title / diagram label
    ax.text(5.0, 9.2, "Optimum Population Theory", fontsize=17, fontweight="bold",
            color=INK, ha="center", va="center")

    save(fig, out)
