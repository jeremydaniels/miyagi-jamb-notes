from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Yam (Million Tonnes)", "Cassava (Million Tonnes)", 50, 110)

    # Base PPF Points
    pts = {
        'A': (0, 100),
        'B': (10, 90),
        'C': (20, 70),
        'D': (30, 40),
        'E': (40, 0)
    }

    px = [0, 10, 20, 30, 40]
    py = [100, 90, 70, 40, 0]
    poly_coeff = np.polyfit(px, py, 3)
    
    x_curve = np.linspace(0, 40, 200)
    y_curve = np.polyval(poly_coeff, x_curve)

    # Plot initial PPF
    ax.plot(x_curve, y_curve, color=DEEP["blue"], lw=3.5)

    # Shifted outward PPF (Economic Growth)
    x_growth = np.linspace(0, 48, 200)
    y_growth = 1.15 * np.polyval(poly_coeff, x_growth / 1.2)
    ax.plot(x_growth, y_growth, color=DEEP["green"], lw=3.0, ls="--")

    # Arrow indicating shift outward
    ax.annotate("", xy=(28, 80), xytext=(21, 67),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5))
    ax.text(30, 82, "Economic Growth", fontsize=15, color=DEEP["green"], fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=1))

    # Plot dots for A, B, C, D, E
    for label, (x, y) in pts.items():
        ax.plot(x, y, 'o', color=DEEP["blue"], markersize=8, zorder=5)
        
        # Position labels cleanly
        if label == 'A':
            dx, dy = 2, 2
        elif label == 'B':
            dx, dy = -6.5, -4
        elif label == 'C':
            dx, dy = -7, -4
        elif label == 'D':
            dx, dy = -7.5, -4
        elif label == 'E':
            dx, dy = -7.5, 3
        ax.text(x + dx, y + dy, f"{label} ({x}, {y})", fontsize=14, color=INK,
                bbox=dict(fc="white", ec="none", pad=1.5), zorder=10)

    # Point U (Inefficiency / Unemployment) inside
    u_x, u_y = 15, 35
    ax.plot(u_x, u_y, 'o', color=DEEP["orange"], markersize=8, zorder=5)
    ax.annotate("U (Unemployment /\nInefficiency)", xy=(u_x, u_y), xytext=(u_x + 2, u_y - 15),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=10)

    # Point F (Unattainable) outside
    f_x, f_y = 38, 75
    ax.plot(f_x, f_y, 'o', color=DEEP["pink"], markersize=8, zorder=5)
    ax.annotate("F (Unattainable)", xy=(f_x, f_y), xytext=(f_x - 12, f_y + 16),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=10)

    # Axis limits
    ax.set_xlim(0, 52)
    ax.set_ylim(0, 115)

    # Set integer tick steps
    ax.set_xticks(np.arange(0, 51, 10))
    ax.set_yticks(np.arange(0, 111, 20))
    ax.tick_params(labelsize=14)

    save(fig, out)
