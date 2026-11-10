from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Light intensity", "Rate of photosynthesis", 10, 10)

    x = np.linspace(0, 10, 200)

    def curve(top, k):
        return top * (1 - np.exp(-k * x))

    c1 = curve(3.0, 0.75)
    c2 = curve(5.6, 0.5)
    c3 = curve(8.4, 0.5)

    ax.plot(x, c1, color=DEEP["green"], lw=3.2, label="low CO₂, 25 °C")
    ax.plot(x, c2, color=DEEP["blue"], lw=3.2, label="high CO₂, 25 °C")
    ax.plot(x, c3, color=DEEP["orange"], lw=3.2, label="high CO₂, 35 °C")

    # Annotations on the lowest curve
    ax.annotate(
        "light is the\nlimiting factor",
        xy=(1.0, curve(3.0, 0.75)[20]),
        xytext=(2.2, 0.8),
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        ha="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    ax.annotate(
        "another factor\nis limiting",
        xy=(6.5, 3.0),
        xytext=(6.5, 1.4),
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        ha="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    ax.legend(loc="upper left", frameon=True, fontsize=12, edgecolor=GREY, facecolor="white")

    save(fig, out)
