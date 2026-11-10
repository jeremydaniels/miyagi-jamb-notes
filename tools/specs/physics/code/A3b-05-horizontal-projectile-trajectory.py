from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-2.5, 9.5)
    ax.set_ylim(-1.5, 7.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Coordinates and dimensions
    cliff_x = 1.0
    ground_y = 1.0
    cliff_h = 4.5
    cliff_top_y = ground_y + cliff_h  # 5.5
    R_val = 6.0
    impact_x = cliff_x + R_val        # 7.0

    # Draw ground
    ax.plot([-2.0, 9.0], [ground_y, ground_y], color=INK, lw=2.5)
    
    # Ground hatching marks
    for gx in np.linspace(-1.8, 8.8, 25):
        ax.plot([gx, gx - 0.25], [ground_y, ground_y - 0.3], color=GREY, lw=1.5)

    # Draw cliff face and body
    cliff_poly = np.array([
        [-2.0, ground_y],
        [cliff_x, ground_y],
        [cliff_x, cliff_top_y],
        [-2.0, cliff_top_y]
    ])
    ax.fill(cliff_poly[:, 0], cliff_poly[:, 1], color=CREAM, zorder=1)
    # Cliff edges
    ax.plot([-2.0, cliff_x], [cliff_top_y, cliff_top_y], color=INK, lw=2.5, zorder=2)
    ax.plot([cliff_x, cliff_x], [ground_y, cliff_top_y], color=INK, lw=2.5, zorder=2)

    # Stone trajectory (half-parabola: y = cliff_top_y - cliff_h * ((x - cliff_x)/R_val)^2)
    px = np.linspace(cliff_x, impact_x, 150)
    py = cliff_top_y - cliff_h * ((px - cliff_x) / R_val) ** 2
    ax.plot(px, py, color=DEEP['blue'], lw=2.5, ls='--', zorder=3)

    # Stone at launch point
    stone_radius = 0.18
    stone = plt.Circle((cliff_x, cliff_top_y), stone_radius, color=INK, zorder=5)
    ax.add_patch(stone)

    # Velocity arrow 'u'
    arrow_len = 1.8
    ax.annotate(
        '', 
        xy=(cliff_x + arrow_len, cliff_top_y), 
        xytext=(cliff_x, cliff_top_y),
        arrowprops=dict(arrowstyle="-|>", color=DEEP['orange'], lw=3.0, mutation_scale=20),
        zorder=6
    )
    ax.text(cliff_x + arrow_len * 0.5, cliff_top_y + 0.35, "u", fontsize=18, fontweight='bold',
            color=DEEP['orange'], ha='center', va='bottom')

    # Stone at impact
    stone_impact = plt.Circle((impact_x, ground_y), stone_radius * 0.8, color=INK, alpha=0.4, zorder=4)
    ax.add_patch(stone_impact)

    # Height dimension 'h' (left side or vertical span)
    dim_x = cliff_x - 0.6
    ax.annotate(
        '', 
        xy=(dim_x, cliff_top_y), 
        xytext=(dim_x, ground_y),
        arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.8, shrinkA=0, shrinkB=0),
        zorder=4
    )
    # Ticks for height
    ax.plot([dim_x - 0.2, dim_x + 0.2], [cliff_top_y, cliff_top_y], color=INK, lw=1.5)
    ax.plot([dim_x - 0.2, dim_x + 0.2], [ground_y, ground_y], color=INK, lw=1.5)
    ax.text(dim_x - 0.35, ground_y + cliff_h / 2, "h", fontsize=18, fontweight='bold',
            color=INK, ha='right', va='center', bbox=dict(fc='white', ec='none', pad=1))

    # Range dimension 'R' (horizontal span along ground)
    dim_y = ground_y - 0.6
    ax.annotate(
        '', 
        xy=(impact_x, dim_y), 
        xytext=(cliff_x, dim_y),
        arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=1.8, shrinkA=0, shrinkB=0),
        zorder=4
    )
    # Ticks for range
    ax.plot([cliff_x, cliff_x], [dim_y - 0.2, dim_y + 0.2], color=INK, lw=1.5)
    ax.plot([impact_x, impact_x], [dim_y - 0.2, dim_y + 0.2], color=INK, lw=1.5)
    ax.text(cliff_x + R_val / 2, dim_y - 0.35, "R", fontsize=18, fontweight='bold',
            color=INK, ha='center', va='top', bbox=dict(fc='white', ec='none', pad=1))

    # Cliff label
    ax.text(-0.5, cliff_top_y - 1.0, "Cliff", fontsize=16, color=INK, ha='center', va='center')

    # Trajectory / path label (placed well away from lines)
    ax.text(impact_x + 0.3, ground_y + 0.4, "impact point", fontsize=14, color=INK,
            ha='left', va='center')

    save(fig, out)
