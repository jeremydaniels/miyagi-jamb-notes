from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8, 9.2)
    ax.axis("off")

    x_left = 1.8
    x_right = 8.2
    L = x_right - x_left
    x = np.linspace(x_left, x_right, 400)

    # Base heights for the 3 modes
    y_centers = [7.0, 4.3, 1.6]
    harmonics = [1, 2, 3]
    titles = [
        "Fundamental mode (1st harmonic, n = 1)",
        "1st overtone (2nd harmonic, n = 2)",
        "2nd overtone (3rd harmonic, n = 3)"
    ]
    wavelength_texts = [
        r"$L = \frac{1}{2}\lambda_1$",
        r"$L = \lambda_2$",
        r"$L = \frac{3}{2}\lambda_3$"
    ]
    amp = 0.65

    # Fixed support blocks styling
    support_w = 0.3
    support_h = 1.6

    for y_c, n, title, w_text in zip(y_centers, harmonics, titles, wavelength_texts):
        # Mode Title
        ax.text(x_left, y_c + amp + 0.55, title, fontsize=15, weight="bold", color=INK, ha="left", va="bottom")
        ax.text(x_right, y_c + amp + 0.55, w_text, fontsize=15, color=DEEP["blue"], ha="right", va="bottom")

        # Supports (left and right)
        for sx in [x_left - support_w, x_right]:
            rect = plt.Rectangle((sx, y_c - support_h / 2), support_w, support_h,
                                 facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=2)
            ax.add_patch(rect)
            # Hatch lines on supports
            for hy in np.linspace(y_c - support_h / 2 + 0.2, y_c + support_h / 2 - 0.2, 5):
                ax.plot([sx, sx + support_w], [hy - 0.1, hy + 0.1], color=GREY, lw=1.2, zorder=3)

        # Baseline dashed (equilibrium)
        ax.plot([x_left, x_right], [y_c, y_c], color=GREY, ls=":", lw=1.2, zorder=1)

        # Waves
        wave_pos = y_c + amp * np.sin(n * np.pi * (x - x_left) / L)
        wave_neg = y_c - amp * np.sin(n * np.pi * (x - x_left) / L)

        # Shading between loops
        ax.fill_between(x, wave_pos, wave_neg, color=BLUE, alpha=0.15, zorder=1)

        # Solid and dashed standing wave envelopes
        ax.plot(x, wave_pos, color=DEEP["blue"], lw=2.5, zorder=4)
        ax.plot(x, wave_neg, color=DEEP["blue"], lw=2.0, ls="--", dashes=(4, 3), zorder=4)

        # Nodes (N)
        node_indices = np.linspace(0, n, n + 1)
        node_xs = x_left + node_indices * (L / n)
        for nx in node_xs:
            ax.plot(nx, y_c, marker='o', markersize=5, color=DEEP["pink"], zorder=5)
            ax.text(nx, y_c - 0.28, "N", fontsize=14, color=DEEP["pink"], weight="bold",
                    ha="center", va="top",
                    bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.8))

        # Antinodes (A)
        antinode_indices = np.arange(n) + 0.5
        antinode_xs = x_left + antinode_indices * (L / n)
        for ax_pos in antinode_xs:
            ax.text(ax_pos, y_c + amp + 0.08, "A", fontsize=14, color=DEEP["green"], weight="bold",
                    ha="center", va="bottom",
                    bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none", alpha=0.8))

    # Length L indicator bar at the bottom
    y_dim = 0.35
    ax.annotate("", xy=(x_left, y_dim), xytext=(x_right, y_dim),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    # Vertical end tics for dimension line
    ax.plot([x_left, x_left], [y_dim - 0.15, y_dim + 0.15], color=INK, lw=1.5)
    ax.plot([x_right, x_right], [y_dim - 0.15, y_dim + 0.15], color=INK, lw=1.5)

    ax.text((x_left + x_right) / 2, y_dim, "Length L", fontsize=16, weight="bold", color=INK,
            ha="center", va="center", bbox=dict(boxstyle="square,pad=0.25", fc="white", ec="none"))

    # Legend / Key for N and A
    ax.text(5.0, -0.4, "N = Node (zero amplitude)       A = Antinode (maximum amplitude)",
            fontsize=14, color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=GREY, lw=1))

    save(fig, out)
