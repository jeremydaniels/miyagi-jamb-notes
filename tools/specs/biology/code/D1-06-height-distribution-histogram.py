from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)

    # Class intervals and frequencies
    labels = [
        "140–144", "145–149", "150–154", "155–159",
        "160–164", "165–169", "170–174", "175–179"
    ]
    frequencies = np.array([1, 3, 6, 10, 11, 6, 2, 1], dtype=float)
    n_bars = len(frequencies)
    x_indices = np.arange(n_bars, dtype=float)

    # Bars touching each other: width = 1.0, drawn in soft blue with thin dark outlines
    ax.bar(
        x_indices,
        frequencies,
        width=1.0,
        color=BLUE,
        edgecolor=INK,
        linewidth=1.2,
        align='center',
        zorder=2
    )

    # Smooth bell-shaped curve joining the midpoints of the bar tops
    # Natural cubic spline interpolation using pure numpy
    n = len(x_indices)
    h = np.diff(x_indices)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = (3 / h[i]) * (frequencies[i + 1] - frequencies[i]) - (3 / h[i - 1]) * (frequencies[i] - frequencies[i - 1])

    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    for i in range(1, n - 1):
        l[i] = 2 * (x_indices[i + 1] - x_indices[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    c = np.zeros(n)
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)
    a = frequencies[:-1]

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (frequencies[j + 1] - frequencies[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    x_smooth = np.linspace(x_indices[0], x_indices[-1], 300)
    y_smooth = np.zeros_like(x_smooth)

    for i in range(n - 1):
        mask = (x_smooth >= x_indices[i]) & (x_smooth <= x_indices[i + 1]) if i == n - 2 else (x_smooth >= x_indices[i]) & (x_smooth < x_indices[i + 1])
        dx = x_smooth[mask] - x_indices[i]
        y_smooth[mask] = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3

    ax.plot(x_smooth, y_smooth, color=DEEP["blue"], lw=2.5, zorder=3)

    # Dots at midpoints of bar tops
    ax.scatter(x_indices, frequencies, color=DEEP["blue"], s=28, zorder=4)

    # Axes configuration
    ax.set_xlim(-0.7, n_bars - 0.3)
    ax.set_ylim(0, 12.5)

    ax.set_xticks(x_indices)
    ax.set_xticklabels(labels, fontsize=11.5, color=INK)
    ax.set_yticks(range(0, 13, 2))
    ax.tick_params(axis='both', which='both', length=4, color=INK, labelsize=11.5)

    # Gridlines every 2 on the y-axis
    ax.yaxis.grid(True, linestyle='--', color=GREY, alpha=0.7, zorder=1)
    ax.xaxis.grid(False)

    # Spines styling
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.2)
    ax.spines['bottom'].set_linewidth(1.2)

    # Labels and Title
    ax.set_xlabel("Height (cm)", fontsize=13, color=INK, labelpad=10, fontweight='bold')
    ax.set_ylabel("Frequency (number of pupils)", fontsize=13, color=INK, labelpad=10, fontweight='bold')
    ax.set_title("Heights of 40 pupils aged 15 (invented sample data)", fontsize=14.5, color=INK, pad=18, fontweight='bold')

    # Annotations
    # 1. modal class (160–164 cm) pointing to the tallest bar
    ax.annotate(
        "modal class (160–164 cm)",
        xy=(4, 11),
        xytext=(4.8, 11.6),
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        ha="left",
        va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.95),
        zorder=5
    )

    # 2. normal distribution curve pointing to the curve
    target_x = 2.15
    i_seg = 2
    dx_val = target_x - x_indices[i_seg]
    target_y = a[i_seg] + b[i_seg] * dx_val + c[i_seg] * dx_val**2 + d[i_seg] * dx_val**3

    ax.annotate(
        "normal distribution curve",
        xy=(target_x, target_y),
        xytext=(0.5, 9.2),
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        ha="center",
        va="center",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.95),
        zorder=5
    )

    save(fig, out)
