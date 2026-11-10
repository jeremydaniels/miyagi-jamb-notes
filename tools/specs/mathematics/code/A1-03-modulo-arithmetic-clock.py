from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(7, 7)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)

    # Title
    ax.text(0, 1.95, "Modulo 7 Arithmetic ($\mathbb{Z}_7$)", fontsize=17, weight="bold", color=INK, ha="center", va="center")

    # Main dial circle
    r = 1.2
    main_circle = patches.Circle((0, 0), r, fill=False, edgecolor=GREY, lw=2.5, zorder=1)
    ax.add_patch(main_circle)

    # 7 positions: 0 at top (pi/2), clockwise order means angle decreases by 2*pi/7
    n = 7
    node_radius = 0.22
    
    # Outer curved arrows showing clockwise direction / addition
    arrow_r = 1.62
    arc_angles = np.linspace(0, 2*np.pi, 4, endpoint=False) + np.pi/4
    for start_ang in arc_angles:
        # Arc segment from start_ang down to start_ang - pi/3 (clockwise)
        theta = np.linspace(start_ang, start_ang - 0.7, 30)
        ax.plot(arrow_r * np.cos(theta), arrow_r * np.sin(theta), color=DEEP["blue"], lw=2.2, zorder=2)
        # Arrowhead at the end
        end_pt = (arrow_r * np.cos(theta[-1]), arrow_r * np.sin(theta[-1]))
        tangent = (-np.sin(theta[-1]), np.cos(theta[-1])) # direction of increasing theta
        # Clockwise means pointing in -tangent direction
        dx = -(-np.sin(theta[-1])) * 0.01
        dy = -(np.cos(theta[-1])) * 0.01
        ax.annotate(
            "",
            xy=end_pt,
            xytext=(end_pt[0] - dx, end_pt[1] - dy),
            arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.2, mutation_scale=16),
            zorder=3
        )

    # Label for addition direction
    ax.text(0, 1.62, "+ (addition)", fontsize=14, color=DEEP["blue"], weight="bold", ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Modulo nodes (0 to 6)
    for i in range(n):
        # 0 at top (angle = pi/2), clockwise step = -2*pi/7
        angle = np.pi/2 - i * (2 * np.pi / n)
        x = r * np.cos(angle)
        y = r * np.sin(angle)

        # Node disk
        node_bg = patches.Circle((x, y), node_radius, facecolor=CREAM, edgecolor=DEEP["orange"] if i == 0 else INK, lw=2.2, zorder=4)
        ax.add_patch(node_bg)

        # Node label
        ax.text(x, y, str(i), fontsize=16, weight="bold", color=DEEP["orange"] if i == 0 else INK,
                ha="center", va="center", zorder=5)

    # Center label/info
    ax.text(0, 0, "$\mathbb{Z}/7\mathbb{Z}$\nClock", fontsize=15, color=INK, ha="center", va="center", linespacing=1.2)

    save(fig, out)
