from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Titles for the two panels
    ax.text(3.5, 8.4, "Untwisted DNA (ladder model)", fontsize=16, weight="bold", ha="center", color=INK)
    ax.text(10.5, 8.4, "Double helix", fontsize=16, weight="bold", ha="center", color=INK)

    # Base Colors
    c_A = "#4CAF50"  # green
    c_T = "#E53935"  # red
    c_G = "#1E88E5"  # blue
    c_C = "#FB8C00"  # orange
    c_phos = "#FDD835"  # yellow
    c_sugar = "#FF9800" # orange/amber

    # Left Ladder Layout
    # 5 rungs, vertical coordinates:
    y_rungs = [7.0, 5.7, 4.4, 3.1, 1.8]
    pairs = [('A', 'T', c_A, c_T, 2),
             ('G', 'C', c_G, c_C, 3),
             ('T', 'A', c_T, c_A, 2),
             ('C', 'G', c_C, c_G, 3),
             ('A', 'T', c_A, c_T, 2)]

    x_left_bb = 2.1
    x_right_bb = 4.9

    # Draw ladder vertical backbone lines
    ax.plot([x_left_bb, x_left_bb], [1.2, 7.6], color=GREY, lw=2, zorder=1)
    ax.plot([x_right_bb, x_right_bb], [1.2, 7.6], color=GREY, lw=2, zorder=1)

    # 5' and 3' labels for antiparallel strands
    ax.text(x_left_bb, 7.7, "5'", fontsize=14, weight="bold", ha="center", va="bottom", color=INK)
    ax.text(x_left_bb, 1.1, "3'", fontsize=14, weight="bold", ha="center", va="top", color=INK)
    ax.text(x_right_bb, 7.7, "3'", fontsize=14, weight="bold", ha="center", va="bottom", color=INK)
    ax.text(x_right_bb, 1.1, "5'", fontsize=14, weight="bold", ha="center", va="top", color=INK)

    # Helper function to create an explicit 5-point pentagon pointing UP or DOWN
    def pentagon_points(cx, cy, r, point_up=True):
        if point_up:
            angles = [np.pi/2 + i * 2 * np.pi / 5 for i in range(5)]
        else:
            angles = [-np.pi/2 + i * 2 * np.pi / 5 for i in range(5)]
        return np.array([[cx + r * np.cos(a), cy + r * np.sin(a)] for a in angles])

    # Draw Sugars and Phosphates on backbones
    # Left strand: 5' (top) -> 3' (bottom), deoxyribose sugar points UP (apex towards 5')
    # Right strand: 3' (top) -> 5' (bottom), deoxyribose sugar points DOWN (apex towards 5')
    r_sugar = 0.28
    for i, y in enumerate(y_rungs):
        poly_left = patches.Polygon(pentagon_points(x_left_bb, y, r_sugar, point_up=True),
                                    closed=True, fc=c_sugar, ec=INK, lw=1.2, zorder=4)
        poly_right = patches.Polygon(pentagon_points(x_right_bb, y, r_sugar, point_up=False),
                                     closed=True, fc=c_sugar, ec=INK, lw=1.2, zorder=4)
        ax.add_patch(poly_left)
        ax.add_patch(poly_right)

        # Phosphates between sugars
        if i < len(y_rungs) - 1:
            y_phos = (y + y_rungs[i+1]) / 2.0
            p_left = patches.Circle((x_left_bb, y_phos), 0.20, fc=c_phos, ec=INK, lw=1.2, zorder=4)
            p_right = patches.Circle((x_right_bb, y_phos), 0.20, fc=c_phos, ec=INK, lw=1.2, zorder=4)
            ax.add_patch(p_left)
            ax.add_patch(p_right)

    # Draw rungs (bases and hydrogen bonds)
    for i, (b1, b2, col1, col2, n_h) in enumerate(pairs):
        y = y_rungs[i]

        # Left base rectangle
        r1 = patches.FancyBboxPatch((x_left_bb + 0.25, y - 0.24), 0.95, 0.48,
                                    boxstyle="round,pad=0.04", fc=col1, ec="none", zorder=3)
        ax.add_patch(r1)
        ax.text(x_left_bb + 0.72, y, b1, fontsize=14, weight="bold", ha="center", va="center", color="white", zorder=4)

        # Right base rectangle
        r2 = patches.FancyBboxPatch((x_right_bb - 1.20, y - 0.24), 0.95, 0.48,
                                    boxstyle="round,pad=0.04", fc=col2, ec="none", zorder=3)
        ax.add_patch(r2)
        ax.text(x_right_bb - 0.72, y, b2, fontsize=14, weight="bold", ha="center", va="center", color="white", zorder=4)

        # Hydrogen bonds (dotted lines)
        mid_x1 = x_left_bb + 1.25
        mid_x2 = x_right_bb - 1.25
        if n_h == 2:
            ax.plot([mid_x1, mid_x2], [y + 0.08, y + 0.08], ":", color=INK, lw=2.2, zorder=3)
            ax.plot([mid_x1, mid_x2], [y - 0.08, y - 0.08], ":", color=INK, lw=2.2, zorder=3)
        else:
            ax.plot([mid_x1, mid_x2], [y + 0.12, y + 0.12], ":", color=INK, lw=2.2, zorder=3)
            ax.plot([mid_x1, mid_x2], [y, y], ":", color=INK, lw=2.2, zorder=3)
            ax.plot([mid_x1, mid_x2], [y - 0.12, y - 0.12], ":", color=INK, lw=2.2, zorder=3)

    # RIGHT PANEL: Smooth Right-Handed Double Helix
    # For a right-handed helix rising along +y:
    # As y increases, strand 1 winds clockwise looking down +y, meaning:
    # x = center_x + w * cos(phi), z = sin(phi), phi = -2*pi*y/period
    # Moving along the front (z > 0), as y rises, x moves from left to right (dx/dy > 0 in foreground).
    center_x = 10.5
    w = 1.3
    period = 3.2

    # Draw discrete rungs along helix (base pairs)
    rung_ys = np.linspace(1.5, 7.3, 14)
    helix_pairs = [
        ('A', 'T', c_A, c_T),
        ('G', 'C', c_G, c_C),
        ('C', 'G', c_C, c_G),
        ('T', 'A', c_T, c_A),
    ]

    for j, ry in enumerate(rung_ys):
        phi = -2 * np.pi * (ry - 1.2) / period
        rx1 = center_x + w * np.cos(phi)
        rx2 = center_x - w * np.cos(phi)
        rz = np.sin(phi)  # z > 0: strand 1 in front; z < 0: strand 2 in front
        pair = helix_pairs[j % len(helix_pairs)]

        mx = (rx1 + rx2) / 2.0
        # Rung is drawn at zorder 2 (behind front ribbon) so ribbons cross cleanly in front
        ax.plot([rx1, mx], [ry, ry], color=pair[2], lw=5.5, solid_capstyle="butt", zorder=2)
        ax.plot([mx, rx2], [ry, ry], color=pair[3], lw=5.5, solid_capstyle="butt", zorder=2)

    # Segmented ribbons to correctly handle right-handed depth layering (front in front of back)
    y_fine = np.linspace(1.2, 7.6, 500)
    for k in range(len(y_fine) - 1):
        y_seg = y_fine[k:k+2]
        phi_seg = -2 * np.pi * (y_seg - 1.2) / period
        
        # Strand 1
        x1_seg = center_x + w * np.cos(phi_seg)
        z1_mid = np.sin(np.mean(phi_seg))
        zo1 = 5 if z1_mid > 0 else 1
        ax.plot(x1_seg, y_seg, color="#00838F", lw=5.5, solid_capstyle="round", zorder=zo1)

        # Strand 2 (opposite phase, phi + pi)
        x2_seg = center_x - w * np.cos(phi_seg)
        z2_mid = -z1_mid
        zo2 = 5 if z2_mid > 0 else 1
        ax.plot(x2_seg, y_seg, color="#00ACC1", lw=5.5, solid_capstyle="round", zorder=zo2)

    # Annotations & Labels for Left Diagram
    # Sugar-phosphate backbone
    ax.annotate("sugar-phosphate backbone", xy=(x_left_bb, 6.35), xytext=(0.3, 6.7),
                fontsize=14, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    # Phosphate
    ax.annotate("phosphate", xy=(x_left_bb, 5.05), xytext=(0.3, 5.3),
                fontsize=14, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    # Deoxyribose sugar
    ax.annotate("deoxyribose sugar", xy=(x_left_bb, 4.4), xytext=(0.3, 4.0),
                fontsize=14, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    # Base pair
    ax.annotate("base pair", xy=(3.5, 4.4), xytext=(3.5, 3.7),
                fontsize=14, color=INK, ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    # Hydrogen bonds: point to the dotted lines of G-C rung (y=5.7) with label placed clearly above
    # without overlapping any base or text
    ax.annotate("hydrogen bonds", xy=(3.5, 5.7), xytext=(3.5, 6.25),
                fontsize=14, color=INK, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=2))

    # Strand direction description
    ax.text(3.5, 0.45, "two strands run in opposite directions", fontsize=14,
            style="italic", ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Annotations for Right Diagram
    ax.annotate("double helix", xy=(center_x + w, 4.8), xytext=(12.4, 5.2),
                fontsize=14, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    # Legend for Nitrogenous Bases A, T, G, C
    base_legend_items = [("A", c_A), ("T", c_T), ("G", c_G), ("C", c_C)]
    lx_start = 8.4
    for idx, (b_name, b_col) in enumerate(base_legend_items):
        lx = lx_start + idx * 1.2
        patch = patches.FancyBboxPatch((lx, 0.35), 0.9, 0.45, boxstyle="round,pad=0.04", fc=b_col, ec="none")
        ax.add_patch(patch)
        ax.text(lx + 0.45, 0.575, b_name, fontsize=14, weight="bold", color="white", ha="center", va="center")

    save(fig, out)
