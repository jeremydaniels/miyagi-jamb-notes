import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    # Tall flowchart: 7 steps top to bottom
    fig = canvas(11, 16)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 16)
    ax.axis('off')

    # Step parameters
    # 7 boxes stacked vertically from y ~ 15 down to y ~ 1
    box_w = 9.4
    box_h = 1.65
    gap = 0.45
    left_x = 0.8
    y_starts = [16.0 - 0.7 - (i + 1) * (box_h + gap) + gap for i in range(7)]

    # Titles and descriptions
    titles = [
        "1  Choose parents (high yield × pest resistant)",
        "2  Emasculation and hand pollination",
        "3  F₁ hybrid generation",
        "4  F₂: characters segregate",
        "5  Select the best for several generations",
        "6  Field trials",
        "7  Release new variety to farmers"
    ]

    fill_colors = [CREAM, BLUE, GREEN, LAV, ORANGE, GREEN, PINK]
    border_colors = [DEEP["orange"], DEEP["blue"], DEEP["green"], DEEP["lav"], DEEP["orange"], DEEP["green"], DEEP["pink"]]

    # Helper function to draw a simple leafy plant stem
    def draw_plant(cx, cy, h, pods=False, damaged=False, color=DEEP["green"]):
        # Stem
        ax.plot([cx, cx], [cy, cy + h], color=color, lw=2.5)
        # Leaves
        for leaf_y, side in [(cy + h*0.3, -1), (cy + h*0.55, 1), (cy + h*0.8, -1)]:
            leaf = patches.Ellipse((cx + side * 0.22, leaf_y), 0.35, 0.15, angle=side * 25,
                                   fc=GREEN, ec=color, lw=1.5)
            ax.add_patch(leaf)
        # Pods
        if pods:
            for py, side in [(cy + h*0.4, 1), (cy + h*0.65, -1), (cy + h*0.85, 1)]:
                pod = patches.Ellipse((cx + side * 0.25, py), 0.38, 0.12, angle=side * -35,
                                      fc=DEEP["orange"], ec=INK, lw=1.2)
                ax.add_patch(pod)
        # Pest damage
        if damaged:
            ax.text(cx + 0.25, cy + h*0.6, "✕", color=DEEP["pink"], fontsize=14, weight="bold", ha="center", va="center")
            ax.text(cx - 0.25, cy + h*0.35, "✕", color=DEEP["pink"], fontsize=14, weight="bold", ha="center", va="center")

    for i in range(7):
        by = y_starts[i]
        
        # Outer rounded box
        rect = patches.FancyBboxPatch((left_x, by), box_w, box_h,
                                      boxstyle="round,pad=0.15,rounding_size=0.2",
                                      fc=fill_colors[i], ec=border_colors[i], lw=2.0)
        ax.add_patch(rect)

        # Title bar inside box
        ax.text(left_x + 0.3, by + box_h - 0.32, titles[i],
                fontsize=15, weight="bold", color=INK, va="center")

        # Arrow to next box
        if i < 6:
            arrow_y_start = by
            arrow_y_end = by - gap
            mid_x = left_x + box_w / 2
            ax.annotate("", xy=(mid_x, arrow_y_end), xytext=(mid_x, arrow_y_start),
                        arrowprops=dict(arrowstyle="->", lw=2.5, color=INK))

        # Content drawings per box
        mid_y = by + (box_h - 0.35) / 2

        if i == 0:
            # Box 1: Two parent plants (High yield & Pest resistant)
            # Parent 1: High yield
            p1_x = left_x + 2.5
            draw_plant(p1_x, by + 0.2, 0.8, pods=True)
            ax.text(p1_x, by + 0.18, "Parent A (High yield)", ha="center", fontsize=14, color=INK)

            # Cross 'x'
            ax.text(left_x + 4.7, mid_y, "×", fontsize=24, ha="center", va="center", weight="bold", color=INK)

            # Parent 2: Pest resistant with shield
            p2_x = left_x + 6.9
            draw_plant(p2_x, by + 0.2, 0.8, pods=False)
            shield = patches.RegularPolygon((p2_x + 0.5, by + 0.75), 3, radius=0.28,
                                            orientation=np.pi, fc=BLUE, ec=DEEP["blue"], lw=2)
            ax.add_patch(shield)
            ax.text(p2_x + 0.5, by + 0.72, "★", ha="center", va="center", color=INK, fontsize=14)
            ax.text(p2_x, by + 0.18, "Parent B (Pest resistant)", ha="center", fontsize=14, color=INK)

        elif i == 1:
            # Box 2: Emasculation & hand pollination
            # Flower 1: Tweezers removing stamen
            f1_x = left_x + 2.2
            ax.text(f1_x, mid_y + 0.3, "Flower ♀", ha="center", fontsize=14, weight="bold", color=INK)
            # Flower base / petals
            ax.plot([f1_x, f1_x], [by + 0.2, mid_y], color=DEEP["green"], lw=3)
            ax.scatter([f1_x - 0.2, f1_x + 0.2, f1_x], [mid_y, mid_y, mid_y + 0.2], color=PINK, s=200, ec=DEEP["pink"], lw=1.5)
            # Tweezers sketch
            ax.plot([f1_x + 0.1, f1_x + 0.7], [mid_y + 0.05, mid_y + 0.3], color=GREY, lw=2.5)
            ax.plot([f1_x + 0.1, f1_x + 0.7], [mid_y + 0.15, mid_y + 0.3], color=GREY, lw=2.5)
            ax.text(f1_x + 0.8, mid_y + 0.3, "tweezers (emasculation)", fontsize=14, va="center", color=INK)

            # Bagged flower / pollination
            f2_x = left_x + 6.8
            ax.plot([f2_x, f2_x], [by + 0.2, mid_y + 0.1], color=DEEP["green"], lw=3)
            # Paper bag covering flower
            bag = patches.Rectangle((f2_x - 0.35, mid_y - 0.05), 0.7, 0.5, fc=CREAM, ec=INK, lw=1.5, ls="--")
            ax.add_patch(bag)
            ax.text(f2_x + 0.6, mid_y + 0.2, "brush pollination\n& paper bag cover", fontsize=14, va="center", color=INK)

        elif i == 2:
            # Box 3: F1 plants (uniform vigorous)
            f1_xs = [left_x + 2.2, left_x + 4.7, left_x + 7.2]
            for fx in f1_xs:
                draw_plant(fx, by + 0.2, 0.85, pods=True)
            ax.text(left_x + 4.7, by + 0.18, "Uniform hybrid plants (all pest resistant, moderate-high yield)",
                    ha="center", fontsize=14, color=INK)

        elif i == 3:
            # Box 4: F2 plants showing segregation
            types = [
                ("Tall, high yield", 0.9, True, False),
                ("Short, few pods", 0.6, False, False),
                ("High yield, pest attacked", 0.85, True, True),
                ("Resistant, high yield", 0.85, True, False)
            ]
            xs = np.linspace(left_x + 1.5, left_x + 7.9, 4)
            for idx, (lbl, h, pods, damaged) in enumerate(types):
                draw_plant(xs[idx], by + 0.35, h, pods=pods, damaged=damaged)
                ax.text(xs[idx], by + 0.15, lbl, ha="center", fontsize=14, color=INK)

        elif i == 4:
            # Box 5: Selection across generations
            xs = [left_x + 2.0, left_x + 4.7, left_x + 7.4]
            draw_plant(xs[0], by + 0.3, 0.7, pods=False, damaged=True)
            ax.text(xs[0], by + 1.05, "✗", color=DEEP["pink"], fontsize=22, weight="bold", ha="center")
            ax.text(xs[0], by + 0.15, "Discard weak", ha="center", fontsize=14, color=INK)

            draw_plant(xs[1], by + 0.3, 0.85, pods=True, damaged=False)
            ax.text(xs[1], by + 1.15, "✓", color=DEEP["green"], fontsize=26, weight="bold", ha="center")
            ax.text(xs[1], by + 0.15, "Select best", ha="center", fontsize=14, color=INK)

            draw_plant(xs[2], by + 0.3, 0.6, pods=False, damaged=False)
            ax.text(xs[2], by + 0.95, "✗", color=DEEP["pink"], fontsize=22, weight="bold", ha="center")
            ax.text(xs[2], by + 0.15, "Discard low yield", ha="center", fontsize=14, color=INK)

        elif i == 5:
            # Box 6: Field trial plots in rows
            plot_w, plot_h = 1.6, 0.65
            for r in range(2):
                for c in range(3):
                    px = left_x + 0.8 + c * 1.9
                    py = by + 0.2 + (1 - r) * 0.45
                    plot_rect = patches.Rectangle((px, py), plot_w, 0.35, fc=GREEN, ec=DEEP["green"], lw=1.2)
                    ax.add_patch(plot_rect)
                    ax.text(px + plot_w / 2, py + 0.17, f"Plot {r*3 + c + 1}", ha="center", va="center", fontsize=14, color=INK)
            ax.text(left_x + 7.5, mid_y, "Multi-location\nreplicated trials", ha="center", va="center", fontsize=14, color=INK)

        elif i == 6:
            # Box 7: Certified seed bag handed to farmer
            bag_x = left_x + 2.8
            # Seed bag outline
            bag = patches.Polygon([[bag_x - 0.6, by + 0.2], [bag_x + 0.6, by + 0.2],
                                  [bag_x + 0.5, by + 0.95], [bag_x - 0.5, by + 0.95]],
                                 closed=True, fc=CREAM, ec=DEEP["orange"], lw=2)
            ax.add_patch(bag)
            ax.text(bag_x, by + 0.65, "SEEDS", ha="center", va="center", fontsize=14, weight="bold", color=INK)
            # Certified tag
            tag = patches.Rectangle((bag_x - 0.35, by + 0.35), 0.7, 0.2, fc=BLUE, ec=DEEP["blue"], lw=1)
            ax.add_patch(tag)
            ax.text(bag_x, by + 0.45, "Certified Variety", ha="center", va="center", fontsize=14, color=INK)

            # Arrow indicating handover to farmer
            ax.annotate("", xy=(bag_x + 2.6, mid_y), xytext=(bag_x + 1.0, mid_y),
                        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["pink"]))

            # Farmer symbol / label
            farmer_x = left_x + 6.8
            ax.text(farmer_x, mid_y + 0.15, "Distribution to Farmers", fontsize=15, weight="bold", ha="center", color=INK)
            ax.text(farmer_x, mid_y - 0.2, "High-yielding & pest-resistant harvest", fontsize=14, ha="center", color=INK)

    # Title header
    ax.text(5.5, 15.65, "Plant Breeding Programme: Developing Improved Crop Varieties",
            fontsize=17, weight="bold", ha="center", va="center", color=INK)

    save(fig, out)
