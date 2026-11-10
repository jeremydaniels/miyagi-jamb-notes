from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Central Circle
    center_circle = plt.Circle((0, 0), 1.25, facecolor=CREAM, edgecolor=DEEP["orange"], lw=3, zorder=3)
    ax.add_patch(center_circle)
    ax.text(0, 0, "1 Mole", ha="center", va="center", fontsize=18, fontweight="bold", color=INK, zorder=4)

    # Configuration of three branches
    # 1. Mass (Top-Left / Up-Left): 120 degrees
    # 2. Particles (Top-Right / Up-Right): 60 degrees (or Top and Bottoms)
    # Let's arrange nicely:
    # Arrow 1: Top (90 deg) -> Mass in grams (Molar Mass)
    # Arrow 2: Bottom-Right (-30 deg / 330 deg) -> 6.02 × 10²³ particles (Avogadro's Number)
    # Arrow 3: Bottom-Left (210 deg) -> 22.4 dm³ of gas at s.t.p. (Molar Volume)
    
    branches = [
        {
            "angle": 90,
            "title": "Mass in grams\n(Molar Mass)",
            "color": BLUE,
            "edge": DEEP["blue"],
            "dist": 2.9,
            "w": 3.4,
            "h": 1.3
        },
        {
            "angle": -30,
            "title": "6.02 × 10²³ particles\n(Avogadro's Number)",
            "color": GREEN,
            "edge": DEEP["green"],
            "dist": 3.1,
            "w": 3.8,
            "h": 1.3
        },
        {
            "angle": 210,
            "title": "22.4 dm³ of gas at s.t.p.\n(Molar Volume)",
            "color": PINK,
            "edge": DEEP["pink"],
            "dist": 3.1,
            "w": 3.8,
            "h": 1.3
        }
    ]

    r_c = 1.25
    for b in branches:
        rad = np.radians(b["angle"])
        dx = np.cos(rad)
        dy = np.sin(rad)

        # Center of outer box
        bx = b["dist"] * dx
        by = b["dist"] * dy

        # Draw arrow from edge of center circle to edge of box
        start_x = r_c * dx
        start_y = r_c * dy
        
        # Approximate intersection with outer box
        # Box is centered at (bx, by)
        end_dist = b["dist"] - 0.75
        end_x = end_dist * dx
        end_y = end_dist * dy

        ax.annotate(
            "",
            xy=(end_x, end_y),
            xytext=(start_x, start_y),
            arrowprops=dict(
                arrowstyle="-|>",
                color=b["edge"],
                lw=2.5,
                mutation_scale=20,
            ),
            zorder=2
        )

        # Outer rounded box
        box_style = dict(
            boxstyle="round,pad=0.5,rounding_size=0.3",
            facecolor=b["color"],
            edgecolor=b["edge"],
            lw=2.5
        )
        ax.text(
            bx, by,
            b["title"],
            ha="center",
            va="center",
            fontsize=15,
            fontweight="semibold",
            color=INK,
            bbox=box_style,
            zorder=4
        )

    # Title
    ax.text(
        0, 4.0,
        "The Mole Concept",
        ha="center",
        va="center",
        fontsize=20,
        fontweight="bold",
        color=INK
    )

    save(fig, out)
