from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)

    classes = [
        "35–39",
        "40–44",
        "45–49",
        "50–54",
        "55–59",
        "60–64",
        "65–69"
    ]
    heights = [2, 5, 9, 12, 7, 4, 1]
    n_bars = len(heights)
    x_pos = np.arange(n_bars, dtype=float)

    # Touching bars: width=1.0
    ax.bar(
        x_pos, heights, width=1.0,
        color=GREEN, edgecolor=DEEP["green"], linewidth=1.5,
        align='center', zorder=2
    )

    # Key points: starts at 0, strictly passes through each midpoint, tails off smoothly (longer on right)
    # Using monotonic/clamped cubic spline interpolation so it passes EXACTLY through all midpoints
    # Endpoints: left at -0.6 (height 0), right at 7.2 (height 0) to make it slightly longer on the right side
    curve_x_pts = np.array([-0.6, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.2])
    curve_y_pts = np.array([0.0,  2.0, 5.0, 9.0, 12.0, 7.0, 4.0, 1.0, 0.0])

    # Monotonic cubic interpolation (Fritsch-Carlson)
    n = len(curve_x_pts)
    dx = np.diff(curve_x_pts)
    dy = np.diff(curve_y_pts)
    m = dy / dx

    c = np.zeros(n)
    c[0] = m[0]
    c[-1] = m[-1]
    for i in range(1, n - 1):
        if m[i - 1] * m[i] <= 0:
            c[i] = 0.0
        else:
            c[i] = (m[i - 1] + m[i]) / 2.0

    # Fine evaluation of Hermite cubic spline
    x_fine = np.linspace(curve_x_pts[0], curve_x_pts[-1], 300)
    y_fine = np.zeros_like(x_fine)
    for j, x in enumerate(x_fine):
        # find segment
        idx = np.searchsorted(curve_x_pts, x) - 1
        idx = max(0, min(n - 2, idx))
        h = dx[idx]
        t = (x - curve_x_pts[idx]) / h
        t2 = t * t
        t3 = t2 * t
        h00 = 2 * t3 - 3 * t2 + 1
        h10 = t3 - 2 * t2 + t
        h01 = -2 * t3 + 3 * t2
        h11 = t3 - t2
        y_fine[j] = (h00 * curve_y_pts[idx] +
                     h10 * h * c[idx] +
                     h01 * curve_y_pts[idx + 1] +
                     h11 * h * c[idx + 1])

    y_fine = np.clip(y_fine, 0, None)
    ax.plot(x_fine, y_fine, color=DEEP["green"], lw=3.0, zorder=4)

    # Set axes limits and ticks
    ax.set_xlim(-0.8, 7.6)
    ax.set_ylim(0, 14)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(classes, fontsize=12, color=INK)
    ax.set_yticks(np.arange(0, 15, 2))
    ax.tick_params(axis='both', which='major', labelsize=12, colors=INK)

    # Labels and title
    ax.set_xlabel("Weight (kg)", fontsize=13, color=INK, labelpad=10)
    ax.set_ylabel("Frequency (number of pupils)", fontsize=13, color=INK, labelpad=10)
    ax.set_title("Weights of 40 pupils aged 15 (invented sample data)", fontsize=15, color=INK, pad=16, weight='bold')

    # Style spines and grid
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.2)
    ax.spines['bottom'].set_linewidth(1.2)
    ax.grid(axis='y', linestyle='--', alpha=0.5, color=GREY, zorder=1)

    # Annotations
    # Modal class annotation pointing to top of 50–54 bar (index 3, height 12)
    ax.annotate(
        "modal class (50–54 kg)",
        xy=(3, 12),
        xytext=(3, 13.1),
        ha="center",
        va="bottom",
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
        zorder=5
    )

    # Frequency curve annotation pointing to the smooth curve
    curve_pt_x = 4.7
    idx_pt = np.argmin(np.abs(x_fine - curve_pt_x))
    curve_pt_y = y_fine[idx_pt]
    ax.annotate(
        "frequency curve",
        xy=(curve_pt_x, curve_pt_y),
        xytext=(5.6, 8.8),
        ha="center",
        va="bottom",
        fontsize=12,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
        zorder=5
    )

    save(fig, out)
