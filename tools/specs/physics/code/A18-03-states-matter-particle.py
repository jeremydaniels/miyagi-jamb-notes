from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5)
    
    # Create 3 subplots for Solid, Liquid, Gas
    ax1 = fig.add_axes([0.05, 0.15, 0.27, 0.68])
    ax2 = fig.add_axes([0.37, 0.15, 0.27, 0.68])
    ax3 = fig.add_axes([0.69, 0.15, 0.27, 0.68])
    
    for ax, title, desc in zip([ax1, ax2, ax3], 
                               ["Solid", "Liquid", "Gas"],
                               ["Neat, closely packed lattice\nSmall vibrations",
                                "Closely packed, irregular\nModerate movement",
                                "Spread far apart\nRapid, random motion"]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        # Draw clean beaker/box container
        for spine in ax.spines.values():
            spine.set_color(INK)
            spine.set_linewidth(2)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(title, fontsize=18, fontweight='bold', color=INK, pad=12)
        ax.text(5, -1.8, desc, ha='center', va='top', fontsize=14, color=INK)

    # 1. SOLID: Neat, closely packed regular lattice (e.g. 5x5 grid)
    r_solid = 0.75
    xs = np.linspace(1.5, 8.5, 5)
    ys = np.linspace(1.5, 8.5, 5)
    for x in xs:
        for y in ys:
            circle = plt.Circle((x, y), r_solid, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=3)
            ax1.add_patch(circle)
            # Small vibration arcs/ticks around spheres
            ax1.plot([x - r_solid - 0.2, x - r_solid - 0.2], [y - 0.3, y + 0.3], color=DEEP["blue"], lw=1.2, zorder=2)
            ax1.plot([x + r_solid + 0.2, x + r_solid + 0.2], [y - 0.3, y + 0.3], color=DEEP["blue"], lw=1.2, zorder=2)

    # 2. LIQUID: Closely packed but randomly arranged spheres (dense in lower 75% of container)
    np.random.seed(42)
    liquid_pts = []
    r_liq = 0.72
    attempts = 0
    while len(liquid_pts) < 24 and attempts < 2000:
        attempts += 1
        px = np.random.uniform(1.2, 8.8)
        py = np.random.uniform(1.2, 7.5)
        # Check collision with existing particles
        collision = False
        for (ox, oy) in liquid_pts:
            if np.hypot(px - ox, py - oy) < 2 * r_liq * 0.95:
                collision = True
                break
        if not collision:
            liquid_pts.append((px, py))

    for (x, y) in liquid_pts:
        circle = plt.Circle((x, y), r_liq, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, zorder=3)
        ax2.add_patch(circle)
        # Moderate movement curved swoosh / short displacement line
        angle = np.random.uniform(0, 2 * np.pi)
        dx, dy = 0.45 * np.cos(angle), 0.45 * np.sin(angle)
        ax2.annotate("", xy=(x + dx, y + dy), xytext=(x - dx*0.5, y - dy*0.5),
                     arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=1.4, mutation_scale=8), zorder=4)

    # 3. GAS: Very few spheres spread far apart with long straight velocity arrows
    gas_pts = [
        (2.0, 2.5, 2.2, 1.8),
        (3.5, 7.5, 1.8, -2.0),
        (7.8, 8.0, -2.4, -1.2),
        (8.0, 3.2, -1.5, 2.3),
        (5.0, 4.2, -2.0, -1.8)
    ]
    r_gas = 0.65
    for (gx, gy, vx, vy) in gas_pts:
        circle = plt.Circle((gx, gy), r_gas, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=3)
        ax3.add_patch(circle)
        # Long straight arrows indicating high-speed motion
        ax3.annotate("", xy=(gx + vx, gy + vy), xytext=(gx, gy),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=12), zorder=4)

    save(fig, out)
