from style import *
import numpy as np

def pchip(x, y, x_new):
    d = np.diff(y) / np.diff(x)
    m = np.zeros_like(x)
    for i in range(1, len(x)-1):
        if d[i-1] * d[i] > 0:
            m[i] = (2 * d[i-1] * d[i]) / (d[i-1] + d[i])
        else:
            m[i] = 0.0
    m[0] = d[0]
    m[-1] = d[-1]
    
    y_new = np.zeros(len(x_new))
    for i, xi in enumerate(x_new):
        idx = np.searchsorted(x, xi) - 1
        idx = np.clip(idx, 0, len(x)-2)
        h = x[idx+1] - x[idx]
        t = (xi - x[idx]) / h
        t2, t3 = t*t, t*t*t
        h00 = 2*t3 - 3*t2 + 1
        h10 = t3 - 2*t2 + t
        h01 = -2*t3 + 3*t2
        h11 = t3 - t2
        y_new[i] = h00*y[idx] + h10*h*m[idx] + h01*y[idx+1] + h11*h*m[idx+1]
    return y_new

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)

    # Base data points
    x_pts = np.array([39.5, 49.5, 59.5, 69.5, 79.5, 89.5, 99.5])
    y_pts = np.array([0.0, 5.0, 20.0, 60.0, 85.0, 95.0, 100.0])

    # To hit exact specified values for Q1, Median, Q3:
    extra_x = [60.75, 67.0, 75.5]
    extra_y = [25.0, 50.0, 75.0]

    all_x = np.sort(np.concatenate([x_pts, extra_x]))
    interp_base = {39.5: 0.0, 49.5: 5.0, 59.5: 20.0, 60.75: 25.0, 67.0: 50.0, 69.5: 60.0, 75.5: 75.0, 79.5: 85.0, 89.5: 95.0, 99.5: 100.0}
    all_y = np.array([interp_base[x] for x in all_x])

    x_fine = np.linspace(39.5, 99.5, 300)
    y_fine = pchip(all_x, all_y, x_fine)

    # Plot gridlines
    ax.grid(True, which='major', color=GREY, linestyle='-', linewidth=0.7, alpha=0.5)

    # Plot ogive curve
    ax.plot(x_fine, y_fine, color=DEEP["blue"], lw=3.0, zorder=4, label="Cumulative Frequency Curve")
    ax.scatter(x_pts, y_pts, color=DEEP["blue"], s=35, zorder=5)

    # Quartiles info: (label, y_val, x_val, color)
    quartiles = [
        ("Lower Quartile ($Q_1$)", 25.0, 60.75, DEEP["orange"]),
        ("Median ($Q_2$)", 50.0, 67.0, DEEP["pink"]),
        ("Upper Quartile ($Q_3$)", 75.0, 75.5, DEEP["green"])
    ]

    for label, y_val, x_val, col in quartiles:
        # Horizontal dashed line
        ax.plot([35.0, x_val], [y_val, y_val], color=col, linestyle='--', lw=2.0, zorder=3)
        # Vertical dashed line
        ax.plot([x_val, x_val], [0, y_val], color=col, linestyle='--', lw=2.0, zorder=3)
        # Intersection dot
        ax.scatter([x_val], [y_val], color=col, s=40, zorder=6)
        
        # Label on the curve/line
        ax.annotate(f"{label}\n≈ {x_val:.1f} kg",
                    xy=(x_val, y_val),
                    xytext=(x_val - 7.5, y_val + 5.5),
                    fontsize=14,
                    color=INK,
                    bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=col, lw=1.2),
                    arrowprops=dict(arrowstyle="->", color=col, lw=1.5),
                    zorder=7)

    # Axis limits & styling
    ax.set_xlim(35, 105)
    ax.set_ylim(0, 105)

    # X-axis ticks: exactly upper class boundaries
    ax.set_xticks(x_pts)
    ax.set_xticklabels([f"{x:.1f}" for x in x_pts], fontsize=14, color=INK)

    # Y-axis ticks: 0 to 100 in steps of 10
    y_ticks = np.arange(0, 101, 10)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([str(y) for y in y_ticks], fontsize=14, color=INK)

    # Axis labels
    ax.set_xlabel("Weight (kg)", fontsize=16, color=INK, labelpad=10, fontweight="bold")
    ax.set_ylabel("Cumulative Frequency", fontsize=16, color=INK, labelpad=10, fontweight="bold")
    ax.set_title("Cumulative Frequency Curve (Ogive)", fontsize=18, color=INK, pad=15, fontweight="bold")

    # Spines styling
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    fig.tight_layout()
    save(fig, out)
