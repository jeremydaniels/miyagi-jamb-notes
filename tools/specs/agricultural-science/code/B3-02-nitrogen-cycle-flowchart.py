from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    def draw_box(x, y, w, h, text, bg_color, border_color):
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.15,rounding_size=0.2",
            facecolor=bg_color, edgecolor=border_color, linewidth=2, zorder=2
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=15, color=INK,
                weight='bold', zorder=3)

    # Top: Atmospheric Nitrogen (N2)
    draw_box(6.0, 8.0, 6.0, 0.9, "Atmospheric Nitrogen (N₂)", BLUE, DEEP["blue"])

    # Left: Legume roots
    draw_box(4.0, 5.0, 3.5, 0.9, "Legume Roots", GREEN, DEEP["green"])

    # Upper Right: Dead Animal
    draw_box(9.5, 5.5, 3.0, 0.9, "Dead Animal", PINK, DEEP["pink"])

    # Middle Right: Ammonification
    draw_box(9.5, 3.5, 3.0, 0.9, "Ammonification", CREAM, DEEP["orange"])

    # Bottom Right: Ammonium
    draw_box(9.5, 1.5, 3.0, 0.9, "Ammonium (NH₄⁺)", LAV, DEEP["lav"])

    # Bottom Center: Nitrites
    draw_box(6.0, 1.5, 3.0, 0.9, "Nitrites (NO₂⁻)", CREAM, DEEP["orange"])

    # Bottom Left: Nitrates
    draw_box(2.5, 1.5, 3.0, 0.9, "Nitrates (NO₃⁻)", GREEN, DEEP["green"])

    def draw_arrow(start, end, label=None, label_pos=0.5, offset=(0, 0), rad=0.0, color=INK):
        connectionstyle = f"arc3,rad={rad}"
        ax.annotate(
            "", xy=end, xytext=start,
            arrowprops=dict(
                arrowstyle="-|>",
                color=color,
                lw=2.5,
                mutation_scale=20,
                shrinkA=8,
                shrinkB=8,
                connectionstyle=connectionstyle
            ),
            zorder=1
        )
        if label:
            mx = (1 - label_pos) * start[0] + label_pos * end[0] + offset[0]
            my = (1 - label_pos) * start[1] + label_pos * end[1] + offset[1]
            ax.text(mx, my, label, ha='center', va='center', fontsize=14, color=INK,
                    bbox=dict(fc="white", ec="none", pad=3), zorder=4)

    # 1. Atmospheric Nitrogen -> Legume roots
    draw_arrow((5.0, 7.5), (4.0, 5.5), "Nitrogen Fixation\nby Rhizobium", label_pos=0.5, offset=(-1.0, 0.2), color=DEEP["blue"])

    # 3. Dead Animal -> Ammonification
    draw_arrow((9.5, 5.0), (9.5, 4.0), color=DEEP["pink"])

    # 4. Ammonification -> Ammonium
    draw_arrow((9.5, 3.0), (9.5, 2.0), color=DEEP["orange"])

    # 5. Ammonium -> Nitrites (labeled Nitrosomonas)
    draw_arrow((7.8, 1.5), (7.6, 1.5), "Nitrosomonas", offset=(0, 0.4), color=DEEP["lav"])

    # 6. Nitrites -> Nitrates (labeled Nitrobacter)
    draw_arrow((4.4, 1.5), (4.2, 1.5), "Nitrobacter", offset=(0, 0.4), color=DEEP["orange"])

    # 7. Nitrates -> Atmospheric Nitrogen (Denitrification by Pseudomonas)
    draw_arrow((1.0, 1.7), (3.0, 8.0), rad=-0.3, color=DEEP["green"])
    ax.text(1.2, 5.0, "Denitrification\nby Pseudomonas", ha='center', va='center', fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=3), zorder=4)

    save(fig, out)
