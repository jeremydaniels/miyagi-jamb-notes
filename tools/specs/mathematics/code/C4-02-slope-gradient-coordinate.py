from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)

    # Grid and limits
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 7.5)
    ax.set_aspect('equal')
    ax.grid(True, color=GREY, linestyle='-', linewidth=0.8, alpha=0.6)

    # Clean axes with arrows
    ax.axhline(0, color=INK, lw=1.5)
    ax.axvline(0, color=INK, lw=1.5)
    
    # Tick marks
    ax.set_xticks(range(0, 10))
    ax.set_yticks(range(0, 8))
    ax.tick_params(labelsize=14, colors=INK)

    # Spine styling
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Coordinates for points
    x1, y1 = 2, 2
    x2, y2 = 7, 5

    # Right-angled triangle fill (below the line)
    triangle_x = [x1, x2, x2]
    triangle_y = [y1, y1, y2]
    ax.fill(triangle_x, triangle_y, color=CREAM, alpha=0.8, zorder=2)

    # The line passing through both points
    # Equation: y - 2 = (3/5)*(x - 2) => y = 0.6x + 0.8
    x_vals = np.linspace(0.5, 8.5, 100)
    y_vals = 0.6 * x_vals + 0.8
    ax.plot(x_vals, y_vals, color=DEEP["blue"], lw=3.5, zorder=4)

    # Run side (horizontal)
    ax.plot([x1, x2], [y1, y1], color=DEEP["orange"], lw=3, linestyle='--', zorder=3)
    # Rise side (vertical)
    ax.plot([x2, x2], [y1, y2], color=DEEP["pink"], lw=3, linestyle='--', zorder=3)

    # Right-angle indicator at (x2, y1)
    sq_size = 0.4
    ax.plot([x2 - sq_size, x2 - sq_size, x2], [y1, y1 + sq_size, y1 + sq_size], color=INK, lw=1.5, zorder=3)

    # Points (x1, y1) and (x2, y2)
    ax.scatter([x1, x2], [y1, y2], color=DEEP["blue"], s=100, zorder=5)

    # Annotate points
    ax.text(x1 - 0.3, y1 + 0.4, r"$(x_1,\, y_1)$", fontsize=15, color=INK, ha='right',
            bbox=dict(fc='white', ec='none', pad=2))
    ax.text(x2 + 0.3, y2 + 0.3, r"$(x_2,\, y_2)$", fontsize=15, color=INK, ha='left',
            bbox=dict(fc='white', ec='none', pad=2))

    # Labels for Rise and Run
    ax.text((x1 + x2) / 2, y1 - 0.5, r"$\mathrm{Run} = \Delta x = x_2 - x_1$", 
            fontsize=15, color=DEEP["orange"], ha='center', va='top', weight='bold',
            bbox=dict(fc='white', ec='none', pad=2))
    
    ax.text(x2 + 0.5, (y1 + y2) / 2, r"$\mathrm{Rise} = \Delta y = y_2 - y_1$", 
            fontsize=15, color=DEEP["pink"], ha='left', va='center', weight='bold',
            bbox=dict(fc='white', ec='none', pad=2))

    # Formula / Summary Box
    formula_text = r"$\mathrm{Gradient\ (slope)} = \frac{\mathrm{Rise}}{\mathrm{Run}} = \frac{\Delta y}{\Delta x}$"
    ax.text(1.0, 6.4, formula_text, fontsize=16, color=INK,
            bbox=dict(boxstyle='round,pad=0.5', fc='white', ec=GREY, lw=1.5))

    # Axis labels
    ax.set_xlabel("$x$", fontsize=16, loc="right", color=INK)
    ax.set_ylabel("$y$", fontsize=16, loc="top", color=INK)

    save(fig, out)
