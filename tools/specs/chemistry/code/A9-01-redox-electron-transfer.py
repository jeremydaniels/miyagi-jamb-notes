from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Title / Mnemonic Header
    ax.text(5, 5.3, "OILRIG: Redox Reactions", fontsize=18, fontweight="bold",
            color=INK, ha="center", va="center")

    # Section Headers
    # Left: Oxidation Is Loss (OIL)
    ax.text(2.3, 4.3, "Oxidation Is Loss (OIL)", fontsize=16, fontweight="bold",
            color=DEEP["blue"], ha="center", va="center",
            bbox=dict(fc=CREAM, ec=DEEP["blue"], boxstyle="round,pad=0.4", lw=1.5))

    # Right: Reduction Is Gain (RIG)
    ax.text(7.7, 4.3, "Reduction Is Gain (RIG)", fontsize=16, fontweight="bold",
            color=DEEP["pink"], ha="center", va="center",
            bbox=dict(fc=CREAM, ec=DEEP["pink"], boxstyle="round,pad=0.4", lw=1.5))

    # Atom A (Left, Blue)
    atom_a_center = (2.3, 2.2)
    circle_a = patches.Circle(atom_a_center, radius=1.1, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=2)
    ax.add_patch(circle_a)
    ax.text(atom_a_center[0], atom_a_center[1] + 0.15, "Atom A", fontsize=16, fontweight="bold",
            color=INK, ha="center", va="center", zorder=3)
    ax.text(atom_a_center[0], atom_a_center[1] - 0.35, "(Loses e⁻)", fontsize=14,
            color=INK, ha="center", va="center", zorder=3)

    # Atom B (Right, Red/Pink)
    atom_b_center = (7.7, 2.2)
    circle_b = patches.Circle(atom_b_center, radius=1.1, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5, zorder=2)
    ax.add_patch(circle_b)
    ax.text(atom_b_center[0], atom_b_center[1] + 0.15, "Atom B", fontsize=16, fontweight="bold",
            color=INK, ha="center", va="center", zorder=3)
    ax.text(atom_b_center[0], atom_b_center[1] - 0.35, "(Gains e⁻)", fontsize=14,
            color=INK, ha="center", va="center", zorder=3)

    # Curved transfer path / arrow from Atom A to Atom B
    arrow = patches.FancyArrowPatch(
        (3.4, 2.8), (6.6, 2.8),
        connectionstyle="arc3,rad=-0.35",
        color=GREY,
        arrowstyle="-|>",
        mutation_scale=22,
        lw=2.5,
        ls="--",
        zorder=2
    )
    ax.add_patch(arrow)

    # Electron Sphere mid-flight along the arc
    e_center = (5.0, 3.4)
    electron = patches.Circle(e_center, radius=0.42, facecolor="#FDE047", edgecolor=DEEP["orange"], lw=2, zorder=4)
    ax.add_patch(electron)
    ax.text(e_center[0], e_center[1], "e⁻", fontsize=16, fontweight="bold",
            color=INK, ha="center", va="center", zorder=5)

    # Subtitle label for the electron
    ax.text(5.0, 4.05, "electron transfer", fontsize=14, style="italic",
            color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Explanatory summary text at the bottom
    ax.text(2.3, 0.7, "Atom A is Oxidised", fontsize=15, color=DEEP["blue"], ha="center", va="center", fontweight="bold")
    ax.text(7.7, 0.7, "Atom B is Reduced", fontsize=15, color=DEEP["pink"], ha="center", va="center", fontweight="bold")

    save(fig, out)
