from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    def draw_molecule(xc, yc, is_cis=True, title=""):
        # C=C coordinates
        dx_c = 0.9
        c1 = np.array([xc - dx_c, yc])
        c2 = np.array([xc + dx_c, yc])

        # Double bond lines
        d_sep = 0.09
        ax.plot([c1[0], c2[0]], [c1[1] + d_sep, c2[1] + d_sep], color=INK, lw=3.5, solid_capstyle='round')
        ax.plot([c1[0], c2[0]], [c1[1] - d_sep, c2[1] - d_sep], color=INK, lw=3.5, solid_capstyle='round')

        # Bond vectors
        arm_x = 1.3
        arm_y = 1.1

        # Groups on C1 (left C)
        # Top-left is CH3, bottom-left is H
        p_c1_up = c1 + np.array([-arm_x, arm_y])
        p_c1_down = c1 + np.array([-arm_x, -arm_y])

        # Groups on C2 (right C)
        if is_cis:
            # Cis: both CH3 point up
            p_c2_up = c2 + np.array([arm_x, arm_y])
            p_c2_down = c2 + np.array([arm_x, -arm_y])
            c2_up_group = r"$\mathbf{CH_3}$"
            c2_up_color = DEEP["blue"]
            c2_down_group = r"$\mathbf{H}$"
            c2_down_color = INK
        else:
            # Trans: C2 has H pointing up, CH3 pointing down
            p_c2_up = c2 + np.array([arm_x, arm_y])
            p_c2_down = c2 + np.array([arm_x, -arm_y])
            c2_up_group = r"$\mathbf{H}$"
            c2_up_color = INK
            c2_down_group = r"$\mathbf{CH_3}$"
            c2_down_color = DEEP["blue"]

        # Draw single bonds
        for p_start, p_end in [(c1, p_c1_up), (c1, p_c1_down), (c2, p_c2_up), (c2, p_c2_down)]:
            ax.plot([p_start[0], p_end[0]], [p_start[1], p_end[1]], color=INK, lw=3, solid_capstyle='round')

        # Carbons at double bond
        for c_pos in [c1, c2]:
            ax.text(c_pos[0], c_pos[1], r"$\mathbf{C}$", fontsize=20, ha='center', va='center',
                    color=INK, bbox=dict(boxstyle='circle,pad=0.25', facecolor='white', edgecolor='none'))

        # Substituents
        # C1 substituents: up = CH3 (or H3C), down = H
        ax.text(p_c1_up[0], p_c1_up[1], r"$\mathbf{H_3C}$", fontsize=18, ha='center', va='center',
                color=DEEP["blue"], bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none'))
        ax.text(p_c1_down[0], p_c1_down[1], r"$\mathbf{H}$", fontsize=18, ha='center', va='center',
                color=INK, bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none'))

        # C2 substituents
        ax.text(p_c2_up[0], p_c2_up[1], c2_up_group, fontsize=18, ha='center', va='center',
                color=c2_up_color, bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none'))
        ax.text(p_c2_down[0], p_c2_down[1], c2_down_group, fontsize=18, ha='center', va='center',
                color=c2_down_color, bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none'))

        # Name / Title underneath
        ax.text(xc, yc - 2.2, title, fontsize=17, ha='center', va='center',
                fontweight='bold', color=INK,
                bbox=dict(boxstyle='round,pad=0.4', facecolor=CREAM, edgecolor=GREY, lw=1))

    # Overall diagram title
    ax.text(6.0, 6.2, "Geometric Isomerism in But-2-ene", fontsize=20, ha='center', va='center',
            fontweight='bold', color=INK)

    # Dividing dashed line between isomers
    ax.plot([6.0, 6.0], [0.8, 5.5], color=GREY, linestyle='--', lw=1.5)

    # Draw both isomers
    draw_molecule(3.0, 3.4, is_cis=True, title="cis-but-2-ene\n(Z-but-2-ene)")
    draw_molecule(9.0, 3.4, is_cis=False, title="trans-but-2-ene\n(E-but-2-ene)")

    # Explanatory annotations
    ax.text(3.0, 1.6, "methyl groups on same side", fontsize=14, ha='center', va='center',
            color=DEEP["blue"], style='italic')
    ax.text(9.0, 1.6, "methyl groups on opposite sides", fontsize=14, ha='center', va='center',
            color=DEEP["blue"], style='italic')

    save(fig, out)
