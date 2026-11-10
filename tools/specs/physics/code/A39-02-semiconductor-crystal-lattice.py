from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    def draw_lattice(center_x, center_y, dopant_type):
        coords = [-1.5, 0, 1.5]
        
        # Horizontal and vertical double lines for covalent bonds
        for r in coords:
            # Horizontal lines across the 3 nodes
            y = center_y + r
            ax.plot([center_x - 1.5, center_x + 1.5], [y - 0.08, y - 0.08], color=GREY, lw=2.5, zorder=1)
            ax.plot([center_x - 1.5, center_x + 1.5], [y + 0.08, y + 0.08], color=GREY, lw=2.5, zorder=1)
        for c in coords:
            # Vertical lines across the 3 nodes
            x = center_x + c
            ax.plot([x - 0.08, x - 0.08], [center_y - 1.5, center_y + 1.5], color=GREY, lw=2.5, zorder=1)
            ax.plot([x + 0.08, x + 0.08], [center_y - 1.5, center_y + 1.5], color=GREY, lw=2.5, zorder=1)

        # Draw outer/edge bond stubs to show lattice continuation
        stub_len = 0.6
        for r in coords:
            y = center_y + r
            # Left stub
            ax.plot([center_x - 1.5 - stub_len, center_x - 1.5], [y - 0.08, y - 0.08], color=GREY, lw=2, ls="--", zorder=1)
            ax.plot([center_x - 1.5 - stub_len, center_x - 1.5], [y + 0.08, y + 0.08], color=GREY, lw=2, ls="--", zorder=1)
            # Right stub
            ax.plot([center_x + 1.5, center_x + 1.5 + stub_len], [y - 0.08, y - 0.08], color=GREY, lw=2, ls="--", zorder=1)
            ax.plot([center_x + 1.5, center_x + 1.5 + stub_len], [y + 0.08, y + 0.08], color=GREY, lw=2, ls="--", zorder=1)

        for c in coords:
            x = center_x + c
            # Bottom stub
            ax.plot([x - 0.08, x - 0.08], [center_y - 1.5 - stub_len, center_y - 1.5], color=GREY, lw=2, ls="--", zorder=1)
            ax.plot([x + 0.08, x + 0.08], [center_y - 1.5 - stub_len, center_y - 1.5], color=GREY, lw=2, ls="--", zorder=1)
            # Top stub
            ax.plot([x - 0.08, x - 0.08], [center_y + 1.5, center_y + 1.5 + stub_len], color=GREY, lw=2, ls="--", zorder=1)
            ax.plot([x + 0.08, x + 0.08], [center_y + 1.5, center_y + 1.5 + stub_len], color=GREY, lw=2, ls="--", zorder=1)

        # Draw Si atoms
        radius = 0.45
        for r in coords:
            for c in coords:
                if r == 0 and c == 0:
                    continue  # center atom handled separately
                x = center_x + c
                y = center_y + r
                circle = plt.Circle((x, y), radius, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
                ax.add_patch(circle)
                ax.text(x, y, "Si", ha="center", va="center", fontsize=15, weight="bold", color=INK, zorder=4)

        # Central dopant atom
        if dopant_type == "n":
            dop_circle = plt.Circle((center_x, center_y), radius, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, zorder=3)
            ax.add_patch(dop_circle)
            ax.text(center_x, center_y, "P", ha="center", va="center", fontsize=16, weight="bold", color=INK, zorder=4)

            # Extra free electron
            elec_x, elec_y = center_x + 0.75, center_y + 0.75
            elec = plt.Circle((elec_x, elec_y), 0.18, facecolor=DEEP["pink"], edgecolor="red", lw=2, zorder=5)
            ax.add_patch(elec)
            ax.text(elec_x, elec_y, "e⁻", ha="center", va="center", fontsize=14, weight="bold", color="white", zorder=6)

            # Label for free electron
            ax.annotate("Free electron", xy=(elec_x + 0.15, elec_y + 0.15), xytext=(center_x + 1.6, center_y + 1.9),
                        fontsize=14, fontweight="bold", color=DEEP["pink"],
                        arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2),
                        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.5),
                        ha="left", va="center", zorder=7)

        else:
            # p-type (Boron)
            dop_circle = plt.Circle((center_x, center_y), radius, facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5, zorder=3)
            ax.add_patch(dop_circle)
            ax.text(center_x, center_y, "B", ha="center", va="center", fontsize=16, weight="bold", color=INK, zorder=4)

            # Missing bond / Hole between B and right Si: cover one of the double lines to show single bond
            ax.plot([center_x + radius, center_x + 1.5 - radius], [center_y + 0.08, center_y + 0.08],
                    color="white", lw=4, zorder=2)

            # Hole represented as an empty white circle with dashed/solid border
            hole_x, hole_y = center_x + 0.75, center_y + 0.08
            hole = plt.Circle((hole_x, hole_y), 0.22, facecolor="white", edgecolor=DEEP["blue"], lw=2.5, ls="--", zorder=5)
            ax.add_patch(hole)

            # Label for hole
            ax.annotate("Hole (missing\nelectron)", xy=(hole_x, hole_y + 0.22), xytext=(center_x + 1.1, center_y + 1.5),
                        fontsize=14, fontweight="bold", color=DEEP["blue"],
                        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2),
                        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1.5),
                        ha="left", va="center", zorder=7)

    # Draw n-type lattice (left)
    draw_lattice(3.5, 3.4, "n")
    ax.text(3.5, 6.7, "n-type Semiconductor", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(3.5, 6.2, "(Doped with Phosphorus, P)", ha="center", va="center", fontsize=14, color=GREY)

    # Draw p-type lattice (right)
    draw_lattice(10.5, 3.4, "p")
    ax.text(10.5, 6.7, "p-type Semiconductor", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(10.5, 6.2, "(Doped with Boron, B)", ha="center", va="center", fontsize=14, color=GREY)

    # Bottom explanatory notes
    ax.text(3.5, 0.7, "5 valence electrons:\n4 form covalent bonds, 1 extra free electron",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4", lw=1))
    ax.text(10.5, 0.7, "3 valence electrons:\n3 covalent bonds formed, leaving an electron vacancy (hole)",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4", lw=1))

    # Divider between left and right
    ax.plot([7.0, 7.0], [0.5, 7.0], color=GREY, lw=1.5, ls=":", zorder=1)

    save(fig, out)
