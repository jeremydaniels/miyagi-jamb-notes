from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)

    # Set up smooth exponential decay curve
    x = np.linspace(0, 4.2, 200)
    y = 100 * (0.5 ** x)

    # Key points
    points_x = [0, 1, 2, 3, 4]
    points_y = [100, 50, 25, 12.5, 6.25]

    # Draw dashed guide lines for the half-lives
    for px, py in zip(points_x[1:4], points_y[1:4]):
        ax.plot([px, px], [0, py], color=GREY, linestyle="--", linewidth=1.5, zorder=1)
        ax.plot([0, px], [py, py], color=GREY, linestyle="--", linewidth=1.5, zorder=1)

    # Plot decay curve
    ax.plot(x, y, color=DEEP["blue"], lw=3.5, zorder=3)

    # Plot points
    ax.scatter(points_x[:4], points_y[:4], color=DEEP["blue"], s=60, zorder=4)

    # Axis limits
    ax.set_xlim(0, 4.5)
    ax.set_ylim(0, 110)

    # Spines styling
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # X-axis ticks and labels
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['0', '1', '2', '3', '4'], fontsize=15, color=INK)
    ax.set_xlabel('Time (half-lives)', fontsize=16, color=INK, labelpad=10)

    # Y-axis ticks and labels
    ax.set_yticks([12.5, 25, 50, 100])
    ax.set_yticklabels(['12.5%', '25%', '50%', '100%'], fontsize=15, color=INK)
    ax.set_ylabel('Amount of radioactive substance remaining', fontsize=16, color=INK, labelpad=12)

    # Clean layout and save
    plt.tight_layout()
    save(fig, out)
