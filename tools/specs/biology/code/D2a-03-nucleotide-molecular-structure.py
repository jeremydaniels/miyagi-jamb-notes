from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Main title
    ax.text(5.5, 6.3, "Structure of a Nucleotide", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK)

    # Dashed grouping outline for the single nucleotide
    nuc_box = patches.FancyBboxPatch((0.8, 1.8), 5.7, 3.8,
                                     boxstyle="Round,pad=0.2",
                                     fc="none", ec=GREY, ls="--", lw=1.5)
    ax.add_patch(nuc_box)
    ax.text(3.65, 5.85, "nucleotide", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # --- Nucleotide Components ---
    # 1. Phosphate group (yellow circle)
    p_center = (1.8, 4.3)
    p_radius = 0.55
    phos = patches.Circle(p_center, p_radius, fc="#FDE047", ec=DEEP["orange"], lw=2, zorder=3)
    ax.add_patch(phos)
    ax.text(p_center[0], p_center[1], "P", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK, zorder=4)

    # 2. Deoxyribose sugar (pale orange pentagon)
    # Standard orientation: pointing upwards
    s_center = (3.6, 3.2)
    s_radius = 0.85
    # Calculate regular pentagon vertices rotated so apex is up
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 6)[:-1]
    sugar_coords = np.column_stack([s_center[0] + s_radius * np.cos(angles),
                                    s_center[1] + s_radius * np.sin(angles)])
    sugar = patches.Polygon(sugar_coords, closed=True, fc=ORANGE, ec=DEEP["orange"], lw=2, zorder=3)
    ax.add_patch(sugar)
    ax.text(s_center[0], s_center[1] - 0.05, "Deoxy-\nribose", ha="center", va="center",
            fontsize=11, fontweight="bold", color=INK, zorder=4)

    # 3. Nitrogenous base (coloured rectangle)
    b_x, b_y, b_w, b_h = 4.8, 2.7, 1.4, 1.0
    base = patches.Rectangle((b_x, b_y), b_w, b_h, fc=BLUE, ec=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(base)
    ax.text(b_x + b_w/2, b_y + b_h/2, "Base", ha="center", va="center",
            fontsize=13, fontweight="bold", color=INK, zorder=4)

    # Connecting bonds (lines between shapes)
    # Bond: Phosphate (bottom-right edge) to Sugar (upper-left edge)
    ax.plot([p_center[0] + 0.38, sugar_coords[1][0]], 
            [p_center[1] - 0.38, sugar_coords[1][1]], 
            color=INK, lw=3, zorder=2)
    # Bond: Sugar (right edge) to Base (left edge)
    ax.plot([sugar_coords[4][0], b_x], 
            [sugar_coords[4][1], b_y + b_h/2], 
            color=INK, lw=3, zorder=2)

    # Labels for the nucleotide components
    # Phosphate label
    ax.annotate("phosphate", xy=(p_center[0], p_center[1] - p_radius),
                xytext=(p_center[0] - 0.3, 2.4),
                fontsize=13, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1))

    # Deoxyribose sugar label
    ax.annotate("deoxyribose sugar", xy=(s_center[0], sugar_coords[2][1]),
                xytext=(s_center[0], 1.2),
                fontsize=13, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1))

    # Nitrogenous base label
    ax.annotate("nitrogenous base", xy=(b_x + b_w/2, b_y + b_h),
                xytext=(b_x + b_w/2 + 0.2, 4.9),
                fontsize=13, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1))

    # --- Four Nitrogenous Bases (Right Side) ---
    bases_panel = patches.FancyBboxPatch((7.2, 1.3), 3.4, 4.6,
                                         boxstyle="Round,pad=0.2",
                                         fc=CREAM, ec=GREY, lw=1.2)
    ax.add_patch(bases_panel)
    ax.text(8.9, 5.5, "Four Bases", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=INK)

    base_specs = [
        ("adenine (A)", GREEN, DEEP["green"], 4.6),
        ("thymine (T)", PINK, DEEP["pink"], 3.7),
        ("guanine (G)", BLUE, DEEP["blue"], 2.8),
        ("cytosine (C)", "#FDBA74", DEEP["orange"], 1.9)
    ]

    for label, col, ec_col, y_pos in base_specs:
        rect = patches.Rectangle((7.5, y_pos - 0.28), 0.75, 0.56,
                                 fc=col, ec=ec_col, lw=1.8)
        ax.add_patch(rect)
        ax.text(8.45, y_pos, label, ha="left", va="center",
                fontsize=12, color=INK, fontweight="semibold")

    save(fig, out)
