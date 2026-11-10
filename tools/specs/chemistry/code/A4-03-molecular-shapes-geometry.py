from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 10)
    
    # 4 subpanels arranged in a 2x2 grid
    # Panel layout:
    # 1. Linear (180°)                 2. Non-linear / V-shaped (104.5°)
    # 3. Pyramidal (107°)              4. Tetrahedral (109.5°)
    
    axes = [
        fig.add_axes([0.05, 0.53, 0.42, 0.40]),
        fig.add_axes([0.53, 0.53, 0.42, 0.40]),
        fig.add_axes([0.05, 0.05, 0.42, 0.40]),
        fig.add_axes([0.53, 0.05, 0.42, 0.40])
    ]
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-2.0, 2.0)
        ax.axis('off')

    # Helper function to draw an atom circle with label
    def draw_atom(ax, x, y, r, color, ec=INK, label=None, label_color=INK):
        circle = plt.Circle((x, y), r, facecolor=color, edgecolor=ec, lw=2, zorder=5)
        ax.add_patch(circle)
        if label:
            ax.text(x, y, label, ha='center', va='center', fontsize=14, fontweight='bold', color=label_color, zorder=6)

    # Helper function to draw bonds
    def draw_bond(ax, p1, p2, lw=5, color=GREY, zorder=3):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, solid_capstyle='round', zorder=zorder)

    # Helper to draw angle arc
    def draw_arc(ax, center, r, theta1, theta2, text):
        t = np.linspace(np.radians(theta1), np.radians(theta2), 100)
        xs = center[0] + r * np.cos(t)
        ys = center[1] + r * np.sin(t)
        ax.plot(xs, ys, color=INK, lw=1.5, ls='--', zorder=4)
        mid_theta = np.radians((theta1 + theta2) / 2)
        label_r = r + 0.35
        lx = center[0] + label_r * np.cos(mid_theta)
        ly = center[1] + label_r * np.sin(mid_theta)
        ax.text(lx, ly, text, ha='center', va='center', fontsize=14, color=INK,
                bbox=dict(fc='white', ec='none', pad=2), zorder=7)

    # ----------------------------------------------------
    # 1. Linear (180°) - e.g. CO2 / generic
    # Central grey atom, two green atoms at 180 degrees
    # ----------------------------------------------------
    ax1 = axes[0]
    ax1.set_title("Linear (180°)", fontsize=16, fontweight='bold', pad=15, color=INK)
    c1 = (0, -0.2)
    left1 = (-1.3, -0.2)
    right1 = (1.3, -0.2)
    
    # Bonds (double bonds representation or single thick rod; stick model uses standard rods)
    draw_bond(ax1, c1, left1, lw=6, color=GREY)
    draw_bond(ax1, c1, right1, lw=6, color=GREY)
    
    # Atoms
    draw_atom(ax1, c1[0], c1[1], 0.38, GREY, ec=INK, label="C", label_color=INK)
    draw_atom(ax1, left1[0], left1[1], 0.32, GREEN, ec=DEEP["green"], label="O", label_color=INK)
    draw_atom(ax1, right1[0], right1[1], 0.32, GREEN, ec=DEEP["green"], label="O", label_color=INK)
    
    # Angle arc
    draw_arc(ax1, c1, 0.7, 0, 180, "180°")
    ax1.text(0, -1.5, "e.g., CO₂", ha='center', fontsize=14, color=INK, style='italic')

    # ----------------------------------------------------
    # 2. Non-linear / V-shaped (104.5°) - H2O
    # Central red atom (Oxygen), two white atoms (Hydrogen)
    # ----------------------------------------------------
    ax2 = axes[1]
    ax2.set_title("Non-linear / V-shaped (104.5°)", fontsize=16, fontweight='bold', pad=15, color=INK)
    c2 = (0, 0.3)
    angle = 104.5
    half_a = angle / 2.0
    # Point downwards in V shape
    th_left = 270 - half_a
    th_right = 270 + half_a
    r_bond = 1.2
    h1 = (c2[0] + r_bond * np.cos(np.radians(th_left)), c2[1] + r_bond * np.sin(np.radians(th_left)))
    h2 = (c2[0] + r_bond * np.cos(np.radians(th_right)), c2[1] + r_bond * np.sin(np.radians(th_right)))
    
    draw_bond(ax2, c2, h1, lw=6, color=GREY)
    draw_bond(ax2, c2, h2, lw=6, color=GREY)
    
    draw_atom(ax2, c2[0], c2[1], 0.38, PINK, ec=DEEP["pink"], label="O", label_color=INK)
    draw_atom(ax2, h1[0], h1[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    draw_atom(ax2, h2[0], h2[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    
    draw_arc(ax2, c2, 0.6, th_left, th_right, "104.5°")
    ax2.text(0, -1.5, "e.g., H₂O", ha='center', fontsize=14, color=INK, style='italic')

    # ----------------------------------------------------
    # 3. Pyramidal (107°) - NH3
    # Central blue atom (Nitrogen), three white atoms at base
    # ----------------------------------------------------
    ax3 = axes[2]
    ax3.set_title("Pyramidal (107°)", fontsize=16, fontweight='bold', pad=15, color=INK)
    c3 = (0, 0.4)
    # 3 base atoms: left, back-middle, right
    base_left = (-1.1, -0.6)
    base_mid = (0.2, -0.25)
    base_right = (1.0, -0.7)
    
    # Back bond first
    draw_bond(ax3, c3, base_mid, lw=5, color=GREY, zorder=2)
    draw_atom(ax3, base_mid[0], base_mid[1], 0.24, CREAM, ec=INK, label="H", label_color=INK)
    
    # Front bonds
    draw_bond(ax3, c3, base_left, lw=6, color=GREY, zorder=3)
    draw_bond(ax3, c3, base_right, lw=6, color=GREY, zorder=3)
    
    draw_atom(ax3, c3[0], c3[1], 0.38, BLUE, ec=DEEP["blue"], label="N", label_color=INK)
    draw_atom(ax3, base_left[0], base_left[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    draw_atom(ax3, base_right[0], base_right[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    
    # Arc between left and right base
    th_l = np.degrees(np.arctan2(base_left[1] - c3[1], base_left[0] - c3[0]))
    th_r = np.degrees(np.arctan2(base_right[1] - c3[1], base_right[0] - c3[0]))
    draw_arc(ax3, c3, 0.65, th_l, th_r, "107°")
    ax3.text(0, -1.5, "e.g., NH₃", ha='center', fontsize=14, color=INK, style='italic')

    # ----------------------------------------------------
    # 4. Tetrahedral (109.5°) - CH4
    # Central dark atom (Carbon), four white atoms (H)
    # ----------------------------------------------------
    ax4 = axes[3]
    ax4.set_title("Tetrahedral (109.5°)", fontsize=16, fontweight='bold', pad=15, color=INK)
    c4 = (0, 0.0)
    top = (0, 1.25)
    b_left = (-1.1, -0.65)
    b_mid = (-0.2, -0.85)  # coming forward slightly
    b_right = (1.1, -0.55)
    
    # Bonds
    draw_bond(ax4, c4, top, lw=6, color=GREY, zorder=3)
    draw_bond(ax4, c4, b_left, lw=6, color=GREY, zorder=3)
    draw_bond(ax4, c4, b_mid, lw=6, color=GREY, zorder=4)
    draw_bond(ax4, c4, b_right, lw=6, color=GREY, zorder=3)
    
    # Atoms
    draw_atom(ax4, c4[0], c4[1], 0.38, GREY, ec=INK, label="C", label_color=INK)
    draw_atom(ax4, top[0], top[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    draw_atom(ax4, b_left[0], b_left[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    draw_atom(ax4, b_mid[0], b_mid[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    draw_atom(ax4, b_right[0], b_right[1], 0.28, CREAM, ec=INK, label="H", label_color=INK)
    
    # Angle arc between top and left
    th_t = 90.0
    th_bl = np.degrees(np.arctan2(b_left[1] - c4[1], b_left[0] - c4[0]))
    draw_arc(ax4, c4, 0.65, th_t, th_bl, "109.5°")
    ax4.text(0, -1.5, "e.g., CH₄", ha='center', fontsize=14, color=INK, style='italic')

    save(fig, out)
