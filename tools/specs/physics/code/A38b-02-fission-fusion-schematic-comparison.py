from style import *
import numpy as np
import matplotlib.patches as patches

def draw_starburst(ax, center, r_inner, r_outer, num_points=12, fc=CREAM, ec=DEEP["orange"]):
    angles = np.linspace(0, 2 * np.pi, num_points * 2, endpoint=False)
    radii = np.array([r_outer if i % 2 == 0 else r_inner for i in range(num_points * 2)])
    xy = np.column_stack([center[0] + radii * np.cos(angles), center[1] + radii * np.sin(angles)])
    poly = patches.Polygon(xy, closed=True, facecolor=fc, edgecolor=ec, lw=2, zorder=3)
    ax.add_patch(poly)

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Central divider
    ax.plot([7, 7], [0.8, 7.2], color=GREY, lw=2, linestyle='--')

    # Main titles
    ax.text(3.5, 7.3, "Fission", fontsize=18, fontweight='bold', ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))
    ax.text(10.5, 7.3, "Fusion", fontsize=18, fontweight='bold', ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # --- LEFT SIDE: FISSION ---
    # 1. Incident Neutron
    c_n1 = patches.Circle((0.8, 4.0), 0.16, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(c_n1)
    ax.annotate("Neutron", xy=(0.8, 4.2), xytext=(0.8, 5.2), fontsize=14, ha='center', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec='none', pad=1))
    # Arrow showing neutron moving toward U-235
    ax.annotate("", xy=(1.6, 4.0), xytext=(1.05, 4.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))

    # 2. Uranium-235 Nucleus
    c_u = patches.Circle((2.5, 4.0), 0.75, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=4)
    ax.add_patch(c_u)
    ax.text(2.5, 4.0, "U-235", fontsize=14, fontweight='bold', ha='center', va='center', color=INK, zorder=5)
    ax.text(2.5, 2.7, "Uranium-235", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))

    # Arrow to splitting phase
    ax.annotate("", xy=(3.8, 4.0), xytext=(3.35, 4.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    # Starburst for Fission Energy
    draw_starburst(ax, (4.7, 4.0), 0.7, 1.1, num_points=12, fc=CREAM, ec=DEEP["orange"])
    ax.text(4.7, 4.0, "Energy", fontsize=15, fontweight='bold', ha='center', va='center', color=DEEP["orange"], zorder=6)

    # 3. Fission Products (Barium & Krypton)
    # Upper product
    c_p1 = patches.Circle((5.7, 5.2), 0.48, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=4)
    ax.add_patch(c_p1)
    ax.text(5.7, 5.2, "Ba", fontsize=14, fontweight='bold', ha='center', va='center', color=INK, zorder=5)
    # Lower product
    c_p2 = patches.Circle((5.7, 2.8), 0.42, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=4)
    ax.add_patch(c_p2)
    ax.text(5.7, 2.8, "Kr", fontsize=14, fontweight='bold', ha='center', va='center', color=INK, zorder=5)

    # Label for Fission Products
    ax.text(5.7, 6.2, "Fission products", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))
    # Bracket or indicator line
    ax.plot([5.7, 5.7], [5.75, 6.0], color=DEEP["green"], lw=1.5)

    # Separation arrows from center
    ax.annotate("", xy=(5.2, 4.8), xytext=(4.8, 4.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
    ax.annotate("", xy=(5.2, 3.2), xytext=(4.8, 3.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # 4. Three Neutrons released
    neutrons_y = [4.4, 4.0, 3.6]
    for y_pos in neutrons_y:
        cn = patches.Circle((6.5, y_pos), 0.14, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=4)
        ax.add_patch(cn)
        ax.annotate("", xy=(6.3, y_pos), xytext=(5.6, 4.0 + (y_pos - 4.0)*0.5),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5))
    ax.text(6.5, 4.8, "3 Neutrons", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))


    # --- RIGHT SIDE: FUSION ---
    # 1. Deuterium and Tritium
    # Deuterium (top left of fusion side)
    c_d = patches.Circle((8.0, 5.3), 0.38, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=4)
    ax.add_patch(c_d)
    ax.text(8.0, 5.3, "²H", fontsize=14, fontweight='bold', ha='center', va='center', color=INK, zorder=5)
    ax.text(8.0, 6.1, "Deuterium", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))

    # Tritium (bottom left of fusion side)
    c_t = patches.Circle((8.0, 2.7), 0.42, facecolor=LAV, edgecolor=DEEP["lav"], lw=2, zorder=4)
    ax.add_patch(c_t)
    ax.text(8.0, 2.7, "³H", fontsize=14, fontweight='bold', ha='center', va='center', color=INK, zorder=5)
    ax.text(8.0, 1.9, "Tritium", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))

    # Collision arrows pointing toward center starburst
    ax.annotate("", xy=(9.1, 4.3), xytext=(8.4, 5.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5))
    ax.annotate("", xy=(9.1, 3.7), xytext=(8.4, 3.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=2.5))

    # 2. Massive Fusion Starburst
    draw_starburst(ax, (9.7, 4.0), 0.9, 1.45, num_points=14, fc=CREAM, ec=DEEP["orange"])
    ax.text(9.7, 4.0, "Energy", fontsize=16, fontweight='bold', ha='center', va='center', color=DEEP["orange"], zorder=6)

    # 3. Released Helium-4 and 1 Neutron
    # Helium-4
    c_he = patches.Circle((12.2, 5.1), 0.55, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, zorder=4)
    ax.add_patch(c_he)
    ax.text(12.2, 5.1, "⁴He", fontsize=15, fontweight='bold', ha='center', va='center', color=INK, zorder=5)
    ax.text(12.2, 6.1, "Helium-4", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))
    ax.annotate("", xy=(11.5, 4.8), xytext=(10.7, 4.3),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    # Released 1 Neutron
    c_fn = patches.Circle((12.2, 2.9), 0.16, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(c_fn)
    ax.text(12.2, 2.1, "Neutron", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=1))
    ax.annotate("", xy=(11.9, 3.0), xytext=(10.7, 3.7),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    save(fig, out)
