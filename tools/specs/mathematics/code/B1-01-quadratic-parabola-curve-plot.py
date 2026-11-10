from style import *
import numpy as np

def draw(out):
    fig = canvas(8, 7)
    ax = fig.add_subplot(111)

    # Plot domain and curve
    x = np.linspace(-0.8, 4.8, 300)
    y = x**2 - 4*x + 3

    # Set up axes centered at (0, 0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color(INK)
    ax.spines['bottom'].set_color(INK)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Set limits
    ax.set_xlim(-1.2, 5.2)
    ax.set_ylim(-2.0, 5.5)

    # Grid
    ax.grid(True, which='both', color=GREY, linestyle='--', linewidth=0.8, alpha=0.5)

    # Axis arrows
    ax.plot(5.2, 0, marker='>', color=INK, markersize=7, clip_on=False)
    ax.plot(0, 5.5, marker='^', color=INK, markersize=7, clip_on=False)

    # Axis labels
    ax.text(5.1, -0.45, '$x$', fontsize=16, color=INK, ha='center', va='center')
    ax.text(-0.35, 5.3, '$y$', fontsize=16, color=INK, ha='center', va='center')

    # Curve plot
    ax.plot(x, y, color=DEEP['blue'], lw=3.0, zorder=3, label=r'$y = x^2 - 4x + 3$')

    # Key points
    points = [
        (1, 0, '(1, 0)'),
        (3, 0, '(3, 0)'),
        (0, 3, '(0, 3)'),
        (2, -1, '(2, -1)')
    ]

    for px, py, plab in points:
        ax.scatter([px], [py], color=DEEP['pink'], s=60, zorder=5, edgecolor=INK, linewidth=1.2)

    # Minimum dashed lines
    ax.plot([2, 2], [0, -1], color=INK, linestyle=':', lw=1.2, zorder=2)
    ax.plot([0, 2], [-1, -1], color=INK, linestyle=':', lw=1.2, zorder=2)

    # Annotations / Labels with clean white boxes
    bbox_style = dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.9)

    # Intercepts
    ax.text(1, 0.45, 'x = 1', fontsize=14, color=INK, ha='center', va='bottom', bbox=bbox_style)
    ax.text(3, 0.45, 'x = 3', fontsize=14, color=INK, ha='center', va='bottom', bbox=bbox_style)
    ax.text(-0.3, 3, 'y = 3', fontsize=14, color=INK, ha='right', va='center', bbox=bbox_style)

    # Vertex annotation
    ax.annotate('Minimum (2, -1)', xy=(2, -1), xytext=(2.7, -1.6),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle='->', color=INK, lw=1.2),
                bbox=bbox_style, ha='left', va='center')

    # Curve label / Title
    ax.text(3.8, 3.8, r'$y = x^2 - 4x + 3$', fontsize=16, color=DEEP['blue'],
            bbox=bbox_style, weight='bold')

    # Custom ticks
    ax.set_xticks([-1, 1, 2, 3, 4])
    ax.set_yticks([-1, 1, 2, 3, 4])
    ax.tick_params(axis='both', which='major', labelsize=14, colors=INK)

    save(fig, out)
