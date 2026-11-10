from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 110)
    ax.axis("off")

    # Title
    ax.text(50, 104, "Cow-Horn Formation (Impondo zankomo)", ha="center", va="center",
            fontsize=17, weight="bold", color=INK)

    # 1. Enemy Force at the top
    enemy_box = patches.FancyBboxPatch(
        (32, 80), 36, 12,
        boxstyle="round,pad=1.0",
        facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5
    )
    ax.add_patch(enemy_box)
    ax.text(50, 86, "Enemy Force", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # 2. Chest (Isifuba) - main attacking force engaging the enemy
    chest_box = patches.FancyBboxPatch(
        (30, 52), 40, 14,
        boxstyle="round,pad=1.0",
        facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5
    )
    ax.add_patch(chest_box)
    ax.text(50, 59, "Chest (Isifuba)\nMain attacking force", ha="center", va="center",
            fontsize=14.5, weight="bold", color=INK, multialignment="center")

    # Direct engagement arrows from Chest toward Enemy
    ax.annotate("", xy=(42, 78), xytext=(42, 68),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"]))
    ax.annotate("", xy=(58, 78), xytext=(58, 68),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"]))

    # 3. Horns (Izimpondo) - flanking pincers curving around the enemy
    # Left Horn
    left_horn_pts = np.array([
        [28, 52],
        [24, 48],
        [15, 55],
        [12, 72],
        [18, 88],
        [28, 92],
        [27, 85],
        [21, 80],
        [19, 68],
        [23, 58],
        [28, 55]
    ])
    horn_left = patches.Polygon(left_horn_pts, closed=True,
                                facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    ax.add_patch(horn_left)

    # Right Horn
    right_horn_pts = np.array([
        [72, 52],
        [76, 48],
        [85, 55],
        [88, 72],
        [82, 88],
        [72, 92],
        [73, 85],
        [79, 80],
        [81, 68],
        [77, 58],
        [72, 55]
    ])
    horn_right = patches.Polygon(right_horn_pts, closed=True,
                                 facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    ax.add_patch(horn_right)

    # Encirclement motion arrows from horns around enemy
    ax.annotate("", xy=(30, 88), xytext=(24, 91),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["blue"]))
    ax.annotate("", xy=(70, 88), xytext=(76, 91),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["blue"]))

    # Labels for Left and Right Horns
    ax.text(12, 47, "Left Horn\n(Izimpondo)", ha="center", va="top",
            fontsize=14.5, weight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", alpha=0.9))
    ax.text(88, 47, "Right Horn\n(Izimpondo)", ha="center", va="top",
            fontsize=14.5, weight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", alpha=0.9))

    # 4. Loins (Umuva) - reserves seated behind the chest
    loins_box = patches.FancyBboxPatch(
        (33, 16), 34, 13,
        boxstyle="round,pad=1.0",
        facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5
    )
    ax.add_patch(loins_box)
    ax.text(50, 22.5, "Loins (Umuva)\nReserves (seated facing away)", ha="center", va="center",
            fontsize=14.5, weight="bold", color=INK, multialignment="center")

    # Flow / reinforcement arrow from Loins towards Chest
    ax.annotate("", xy=(50, 48), xytext=(50, 32),
                arrowprops=dict(arrowstyle="->", lw=2.2, color=DEEP["lav"], linestyle="--"))
    ax.text(50, 40, "reinforcement", ha="center", va="center",
            fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    save(fig, out)
