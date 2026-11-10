from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 7.5)
    
    # Left diagram: Attraction (Parallel currents)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-4, 4)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Right diagram: Repulsion (Anti-parallel currents)
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # Coordinates and parameters
    d = 1.6  # wire separation half-width
    y_wire_bot = -3.2
    y_wire_top = 3.2
    
    # -------------------------------------------------------------
    # Helper to draw vertical wires
    def draw_wire(ax, x_pos, current_dir="up", label="Current $I$"):
        # Wire body (thick grey bar with dark border)
        ax.plot([x_pos, x_pos], [y_wire_bot, y_wire_top], color=GREY, lw=9, solid_capstyle='round', zorder=2)
        ax.plot([x_pos, x_pos], [y_wire_bot, y_wire_top], color=INK, lw=2, zorder=3)
        
        # Current arrows on the wire
        arrow_color = DEEP["orange"]
        if current_dir == "up":
            # Arrow pointing up near top and bottom
            for y_arr in [1.8, -1.8]:
                ax.annotate('', xy=(x_pos, y_arr + 0.4), xytext=(x_pos, y_arr - 0.4),
                            arrowprops=dict(arrowstyle="-|>", color=arrow_color, lw=3, mutation_scale=18),
                            zorder=6)
            ax.text(x_pos, y_wire_top + 0.25, label, fontsize=15, ha='center', va='bottom',
                    color=INK, weight='bold', bbox=dict(fc="white", ec="none", pad=1.5))
        else:
            # Arrow pointing down
            for y_arr in [1.8, -1.8]:
                ax.annotate('', xy=(x_pos, y_arr - 0.4), xytext=(x_pos, y_arr + 0.4),
                            arrowprops=dict(arrowstyle="-|>", color=arrow_color, lw=3, mutation_scale=18),
                            zorder=6)
            ax.text(x_pos, y_wire_top + 0.25, label, fontsize=15, ha='center', va='bottom',
                    color=INK, weight='bold', bbox=dict(fc="white", ec="none", pad=1.5))

    # ==================== LEFT: ATTRACTION ====================
    ax1.set_title("Currents in Same Direction", fontsize=16, pad=18, color=INK, weight='bold')

    # Field lines: in middle plane, perspective ellipses representing magnetic field
    # 1. Individual loops around each wire
    theta = np.linspace(0, 2*np.pi, 200)
    for r in [0.5, 0.9]:
        # Around wire 1
        x1_loop = -d + r * np.cos(theta)
        y1_loop = 0.35 * r * np.sin(theta)
        ax1.plot(x1_loop, y1_loop, color=DEEP["blue"], lw=1.8, zorder=4)
        
        # Around wire 2
        x2_loop = d + r * np.cos(theta)
        y2_loop = 0.35 * r * np.sin(theta)
        ax1.plot(x2_loop, y2_loop, color=DEEP["blue"], lw=1.8, zorder=4)

    # 2. Large combined outer loops enclosing both wires (peanut/oval shapes)
    for a, b in [(2.6, 0.75), (3.3, 1.15)]:
        x_comb = a * np.cos(theta)
        # Squash middle slightly to give combined field shape
        pinch = 1.0 - 0.25 * np.cos(theta)**2
        y_comb = b * np.sin(theta) * pinch
        ax1.plot(x_comb, y_comb, color=DEEP["blue"], lw=2.0, zorder=4)

    # Direction arrows on outer magnetic loops (counter-clockwise viewed from above)
    # Front section (y < 0) flows to the right; back section (y > 0) flows to the left
    ax1.annotate('', xy=(0.3, -0.85), xytext=(-0.3, -0.85),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.2, mutation_scale=16), zorder=5)
    ax1.annotate('', xy=(-0.3, 0.85), xytext=(0.3, 0.85),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.2, mutation_scale=16), zorder=5)
    
    # Draw vertical wires
    draw_wire(ax1, -d, "up", "$I_1$ (up)")
    draw_wire(ax1, d, "up", "$I_2$ (up)")

    # Force arrows pointing inwards between wires
    ax1.annotate('', xy=(-0.35, 0), xytext=(-1.3, 0),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.5, mutation_scale=22), zorder=7)
    ax1.annotate('', xy=(0.35, 0), xytext=(1.3, 0),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.5, mutation_scale=22), zorder=7)
    
    # Label for force placed clearly below the horizontal center
    ax1.text(0, -2.5, "Force of Attraction", fontsize=15, ha="center", va="center",
             color=DEEP["pink"], weight='bold',
             bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.35", lw=1.5), zorder=8)
    
    ax1.text(0, -3.5, "Magnetic field lines combine into\nlarge loops enclosing both wires",
             fontsize=14, ha="center", va="center", color=INK, style="italic")

    # ==================== RIGHT: REPULSION ====================
    ax2.set_title("Currents in Opposite Directions", fontsize=16, pad=18, color=INK, weight='bold')

    # Magnetic field lines crowd between the wires and push outward
    # Left side circles flattened/crowded on right side
    for rx, ry, cx in [(0.5, 0.28, -d), (0.9, 0.50, -d), (1.3, 0.75, -d - 0.2)]:
        x_loop = cx + rx * np.cos(theta)
        y_loop = ry * np.sin(theta)
        ax2.plot(x_loop, y_loop, color=DEEP["blue"], lw=1.8, zorder=4)

    # Right side circles flattened/crowded on left side
    for rx, ry, cx in [(0.5, 0.28, d), (0.9, 0.50, d), (1.3, 0.75, d + 0.2)]:
        x_loop = cx + rx * np.cos(theta)
        y_loop = ry * np.sin(theta)
        ax2.plot(x_loop, y_loop, color=DEEP["blue"], lw=1.8, zorder=4)

    # Vertical crowding field lines in the central gap
    for offset in [-0.2, 0.0, 0.2]:
        y_line = np.linspace(-1.1, 1.1, 100)
        # hyperbolic bowing outward
        x_line = offset * (1 + 0.3 * (y_line**2))
        ax2.plot(x_line, y_line, color=DEEP["blue"], lw=1.8, zorder=4)
        
    # Crowding field direction arrows in the center
    ax2.annotate('', xy=(0, 0.6), xytext=(0, 0.4),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.0, mutation_scale=15), zorder=5)
    ax2.annotate('', xy=(0, -0.4), xytext=(0, -0.6),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.0, mutation_scale=15), zorder=5)

    # Draw vertical wires
    draw_wire(ax2, -d, "up", "$I_1$ (up)")
    draw_wire(ax2, d, "down", "$I_2$ (down)")

    # Force arrows pointing outwards
    ax2.annotate('', xy=(-2.6, 0), xytext=(-1.8, 0),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.5, mutation_scale=22), zorder=7)
    ax2.annotate('', xy=(2.6, 0), xytext=(1.8, 0),
                 arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.5, mutation_scale=22), zorder=7)

    # Label for force placed clearly below
    ax2.text(0, -2.5, "Force of Repulsion", fontsize=15, ha="center", va="center",
             color=DEEP["pink"], weight='bold',
             bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.35", lw=1.5), zorder=8)

    ax2.text(0, -3.5, "Magnetic field lines crowd between wires\nand exert mutual repulsion",
             fontsize=14, ha="center", va="center", color=INK, style="italic")

    plt.tight_layout()
    save(fig, out)
