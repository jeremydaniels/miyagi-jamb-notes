from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_subplot(111)

    # Coordinate ranges
    xmin, xmax = -2, 6
    ymin, ymax = -1, 8

    # Set up custom centered/clean axes
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Styling axes lines
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Axis ticks and labels
    ax.set_xticks([-1, 1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7])
    ax.tick_params(colors=INK, labelsize=14)

    # Axis name labels
    ax.text(5.8, -0.6, "x-axis", fontsize=15, color=INK, ha='right', va='top', fontweight='bold')
    ax.text(-0.3, 7.8, "y-axis", fontsize=15, color=INK, ha='right', va='top', fontweight='bold')

    # Plot function in two segments around x = 2
    x1 = np.linspace(-1.5, 1.96, 100)
    x2 = np.linspace(2.04, 5.2, 100)
    ax.plot(x1, x1 + 2, color=DEEP["blue"], lw=3.5)
    ax.plot(x2, x2 + 2, color=DEEP["blue"], lw=3.5)

    # Dashed reference lines to (2, 4)
    ax.plot([2, 2], [0, 4], color=GREY, linestyle='--', lw=1.8, zorder=2)
    ax.plot([0, 2], [4, 4], color=GREY, linestyle='--', lw=1.8, zorder=2)

    # The hole at (2, 4)
    ax.plot(2, 4, marker='o', markersize=10, markerfacecolor='white', markeredgecolor=DEEP["blue"], markeredgewidth=2.5, zorder=5)

    # Title / Line Label
    ax.text(3.7, 6.4, r"Curve y = (x^2 - 4)/(x - 2)", fontsize=15, color=DEEP["blue"], ha='left', va='bottom',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.2))

    # Hole annotation
    ax.annotate("Hole at (2, 4)", xy=(2, 4), xytext=(0.8, 5.5),
                fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1))

    # Approaching arrows along x-axis towards 2
    ax.annotate('', xy=(1.85, 0), xytext=(0.8, 0),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=16))
    ax.annotate('', xy=(2.15, 0), xytext=(3.2, 0),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=16))
    ax.text(2, -1.2, "x approaches 2", fontsize=14, color=DEEP["pink"], ha='center', va='top',
            fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Approaching arrows along y-axis towards 4
    ax.annotate('', xy=(0, 3.85), xytext=(0, 2.7),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=2.5, mutation_scale=16))
    ax.annotate('', xy=(0, 4.15), xytext=(0, 5.3),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=2.5, mutation_scale=16))
    ax.text(-0.5, 4, "y approaches 4", fontsize=14, color=DEEP["green"], ha='right', va='center',
            fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    save(fig, out)
