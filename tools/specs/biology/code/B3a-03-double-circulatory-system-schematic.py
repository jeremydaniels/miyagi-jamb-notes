from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 13)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 13)
    ax.axis("off")

    # Colors
    c_blue = DEEP["blue"]
    c_red = DEEP["pink"]  # Deep reddish-pink for oxygenated
    bg_blue = BLUE
    bg_red = PINK
    ec_box = INK

    # Loop section background labels / titles
    ax.text(6.0, 12.3, "pulmonary circulation", ha="center", va="center", fontsize=17, fontweight="bold", color=INK)
    ax.text(6.0, 0.7, "systemic circulation", ha="center", va="center", fontsize=17, fontweight="bold", color=INK)

    # Key / Legend at bottom corners or top corners
    # Let's put a clean key box
    key_y = 12.1
    ax.plot([0.8, 1.4], [key_y, key_y], color=c_blue, lw=3)
    ax.text(1.5, key_y, "deoxygenated blood", ha="left", va="center", fontsize=14, color=INK)
    ax.plot([7.8, 8.4], [key_y, key_y], color=c_red, lw=3)
    ax.text(8.5, key_y, "oxygenated blood", ha="left", va="center", fontsize=14, color=INK)

    # 1. Lungs box (top)
    lungs_box = patches.FancyBboxPatch((4.0, 10.0), 4.0, 1.3, boxstyle="round,pad=0.2",
                                        facecolor=CREAM, edgecolor=INK, lw=2)
    ax.add_patch(lungs_box)
    ax.text(6.0, 10.65, "lungs", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    # 2. Body organs box (bottom)
    organs_box = patches.FancyBboxPatch((4.0, 1.7), 4.0, 1.3, boxstyle="round,pad=0.2",
                                         facecolor=CREAM, edgecolor=INK, lw=2)
    ax.add_patch(organs_box)
    ax.text(6.0, 2.35, "body organs", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    # 3. Heart (centre) - 4 boxes
    # Center of heart at x=6, y=6.2
    # Right side of heart (viewer's left): x from 3.8 to 5.8
    # Left side of heart (viewer's right): x from 6.2 to 8.2
    # Atria: y from 6.6 to 7.8
    # Ventricles: y from 4.8 to 6.0

    # Right Atrium (top-left viewer)
    ra = patches.Rectangle((3.7, 6.7), 2.1, 1.4, facecolor=bg_blue, edgecolor=ec_box, lw=2)
    ax.add_patch(ra)
    ax.text(4.75, 7.4, "right", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(4.75, 7.0, "atrium", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Right Ventricle (bottom-left viewer)
    rv = patches.Rectangle((3.7, 4.7), 2.1, 1.6, facecolor=bg_blue, edgecolor=ec_box, lw=2)
    ax.add_patch(rv)
    ax.text(4.75, 5.7, "right", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(4.75, 5.3, "ventricle", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Left Atrium (top-right viewer)
    la = patches.Rectangle((6.2, 6.7), 2.1, 1.4, facecolor=bg_red, edgecolor=ec_box, lw=2)
    ax.add_patch(la)
    ax.text(7.25, 7.4, "left", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(7.25, 7.0, "atrium", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Left Ventricle (bottom-right viewer)
    lv = patches.Rectangle((6.2, 4.7), 2.1, 1.6, facecolor=bg_red, edgecolor=ec_box, lw=2)
    ax.add_patch(lv)
    ax.text(7.25, 5.7, "left", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
    ax.text(7.25, 5.3, "ventricle", ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

    # Internal flows (RA -> RV and LA -> LV)
    ax.annotate("", xy=(4.75, 6.3), xytext=(4.75, 6.7),
                arrowprops=dict(arrowstyle="->", color=c_blue, lw=3, mutation_scale=18))
    ax.annotate("", xy=(7.25, 6.3), xytext=(7.25, 6.7),
                arrowprops=dict(arrowstyle="->", color=c_red, lw=3, mutation_scale=18))

    # Helper function to draw routed vessel path with arrows
    # UPPER LOOP:
    # 1. Pulmonary Artery: from Right Ventricle (x=4.0, y=5.5 out to left) -> up to lungs (x=4.8, y=10.0)
    # Let's route: (3.7, 5.2) -> (2.2, 5.2) -> (2.2, 10.3) -> (4.0, 10.3)
    p_pa = np.array([
        [3.7, 5.2],
        [2.2, 5.2],
        [2.2, 10.3],
        [4.0, 10.3]
    ])
    ax.plot(p_pa[:, 0], p_pa[:, 1], color=c_blue, lw=3.5)
    # Arrows on pulmonary artery
    ax.annotate("", xy=(2.2, 8.2), xytext=(2.2, 7.8),
                arrowprops=dict(arrowstyle="->", color=c_blue, lw=3.5, mutation_scale=20))
    ax.annotate("", xy=(3.4, 10.3), xytext=(3.0, 10.3),
                arrowprops=dict(arrowstyle="->", color=c_blue, lw=3.5, mutation_scale=20))

    ax.text(2.1, 8.6, "pulmonary artery", ha="right", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 2. Pulmonary Vein: from lungs (8.0, 10.3) -> right -> down to Left Atrium (8.3, 7.4)
    # Let's route: (8.0, 10.3) -> (9.8, 10.3) -> (9.8, 7.4) -> (8.3, 7.4)
    p_pv = np.array([
        [8.0, 10.3],
        [9.8, 10.3],
        [9.8, 7.4],
        [8.3, 7.4]
    ])
    ax.plot(p_pv[:, 0], p_pv[:, 1], color=c_red, lw=3.5)
    # Arrows on pulmonary vein
    ax.annotate("", xy=(9.0, 10.3), xytext=(8.6, 10.3),
                arrowprops=dict(arrowstyle="->", color=c_red, lw=3.5, mutation_scale=20))
    ax.annotate("", xy=(9.8, 8.6), xytext=(9.8, 9.0),
                arrowprops=dict(arrowstyle="->", color=c_red, lw=3.5, mutation_scale=20))

    ax.text(9.9, 8.6, "pulmonary vein", ha="left", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # LOWER LOOP:
    # 3. Aorta: from Left Ventricle (8.3, 5.2) -> (10.4, 5.2) -> (10.4, 2.7) -> (8.0, 2.7)
    p_ao = np.array([
        [8.3, 5.2],
        [10.4, 5.2],
        [10.4, 2.7],
        [8.0, 2.7]
    ])
    ax.plot(p_ao[:, 0], p_ao[:, 1], color=c_red, lw=3.5)
    # Arrows on aorta
    ax.annotate("", xy=(10.4, 3.8), xytext=(10.4, 4.2),
                arrowprops=dict(arrowstyle="->", color=c_red, lw=3.5, mutation_scale=20))
    ax.annotate("", xy=(8.9, 2.7), xytext=(9.3, 2.7),
                arrowprops=dict(arrowstyle="->", color=c_red, lw=3.5, mutation_scale=20))

    ax.text(10.5, 4.0, "aorta", ha="left", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # 4. Vena Cava: from body organs (4.0, 2.7) -> (1.6, 2.7) -> (1.6, 7.4) -> (3.7, 7.4)
    p_vc = np.array([
        [4.0, 2.7],
        [1.6, 2.7],
        [1.6, 7.4],
        [3.7, 7.4]
    ])
    ax.plot(p_vc[:, 0], p_vc[:, 1], color=c_blue, lw=3.5)
    # Arrows on vena cava
    ax.annotate("", xy=(2.6, 2.7), xytext=(3.0, 2.7),
                arrowprops=dict(arrowstyle="->", color=c_blue, lw=3.5, mutation_scale=20))
    ax.annotate("", xy=(1.6, 5.3), xytext=(1.6, 4.9),
                arrowprops=dict(arrowstyle="->", color=c_blue, lw=3.5, mutation_scale=20))

    ax.text(1.5, 4.0, "vena cava", ha="right", va="center", fontsize=15, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    save(fig, out)
