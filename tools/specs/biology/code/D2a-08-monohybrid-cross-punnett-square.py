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

    # Helper function to draw pea plant icon
    def draw_plant(cx, cy, tall=True, scale=1.0):
        stem_h = (1.5 if tall else 0.6) * scale
        stem_w = 0.05 * scale
        # Stem
        stem = patches.Rectangle((cx - stem_w/2, cy), stem_w, stem_h, color=DEEP["green"])
        ax.add_patch(stem)
        
        # Leaves along the stem
        num_leaves = 3 if tall else 1
        leaf_spacing = stem_h / (num_leaves + 1)
        for i in range(1, num_leaves + 1):
            ly = cy + i * leaf_spacing
            # Left leaf
            leaf_l = patches.Ellipse((cx - 0.25 * scale, ly + 0.05 * scale), 0.35 * scale, 0.15 * scale,
                                     angle=25, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2)
            # Right leaf
            leaf_r = patches.Ellipse((cx + 0.25 * scale, ly + 0.05 * scale), 0.35 * scale, 0.15 * scale,
                                     angle=-25, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2)
            ax.add_patch(leaf_l)
            ax.add_patch(leaf_r)
        
        # Top flower / bud
        top_flower = patches.Circle((cx, cy + stem_h + 0.08 * scale), 0.12 * scale,
                                    facecolor=PINK, edgecolor=DEEP["pink"], lw=1.2)
        ax.add_patch(top_flower)

    # Helper function for gamete circle
    def draw_gamete(cx, cy, label, r=0.3):
        circ = patches.Circle((cx, cy), r, facecolor=CREAM, edgecolor=DEEP["blue"], lw=1.5)
        ax.add_patch(circ)
        ax.text(cx, cy, label, ha="center", va="center", fontsize=13, fontweight="bold", color=INK)

    # ------------------ TOP TIER (P) ------------------
    # Header label
    ax.text(6.0, 12.3, "P: pure tall (TT) × pure dwarf (tt)", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Parents
    draw_plant(4.0, 10.3, tall=True, scale=1.0)
    ax.text(4.0, 10.0, "TT", ha="center", va="top", fontsize=13, fontweight="bold", color=INK)
    
    ax.text(6.0, 11.0, "×", ha="center", va="center", fontsize=24, fontweight="bold", color=INK)
    
    draw_plant(8.0, 10.3, tall=False, scale=1.0)
    ax.text(8.0, 10.0, "tt", ha="center", va="top", fontsize=13, fontweight="bold", color=INK)

    # Gametes arrows and circles
    ax.annotate("", xy=(4.0, 9.25), xytext=(4.0, 9.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
    draw_gamete(4.0, 8.9, "T")
    ax.text(2.6, 8.9, "gametes T", ha="center", va="center", fontsize=12, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    ax.annotate("", xy=(8.0, 9.25), xytext=(8.0, 9.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
    draw_gamete(8.0, 8.9, "t")
    ax.text(9.4, 8.9, "gametes t", ha="center", va="center", fontsize=12, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Dividing line / flow down to F1
    ax.annotate("", xy=(6.0, 7.9), xytext=(6.0, 8.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))

    # ------------------ MIDDLE TIER (F1) ------------------
    ax.text(6.0, 7.8, "F1: all tall (Tt)", ha="center", va="bottom",
            fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Four identical tall plants
    f1_xs = [3.3, 5.1, 6.9, 8.7]
    for x in f1_xs:
        draw_plant(x, 6.0, tall=True, scale=0.85)
        ax.text(x, 5.75, "Tt", ha="center", va="top", fontsize=12, fontweight="bold", color=INK)

    # Transition to F2
    ax.annotate("", xy=(6.0, 4.8), xytext=(6.0, 5.3),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
    ax.text(6.0, 4.6, "F1 × F1 (Tt × Tt)", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # ------------------ BOTTOM TIER (F2) ------------------
    ax.text(1.8, 3.4, "F2", ha="center", va="center", fontsize=16, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))

    # 2x2 Punnett Square
    # Grid origin and dimension
    gx, gy = 3.8, 1.0
    cell_w, cell_h = 2.0, 1.8

    # Labels for alleles along top and left
    # Top alleles
    ax.text(gx + 0.5 * cell_w, gy + 2 * cell_h + 0.35, "T", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(gx + 1.5 * cell_w, gy + 2 * cell_h + 0.35, "t", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    
    # Left alleles
    ax.text(gx - 0.45, gy + 1.5 * cell_h, "T", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(gx - 0.45, gy + 0.5 * cell_h, "t", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # Draw cells
    cells = [
        {"row": 1, "col": 0, "tall": True, "genotype": "TT", "bg": CREAM},
        {"row": 1, "col": 1, "tall": True, "genotype": "Tt", "bg": CREAM},
        {"row": 0, "col": 0, "tall": True, "genotype": "Tt", "bg": CREAM},
        {"row": 0, "col": 1, "tall": False, "genotype": "tt", "bg": "#f0f4f8"}
    ]

    for cell in cells:
        cx = gx + cell["col"] * cell_w
        cy = gy + cell["row"] * cell_h
        rect = patches.Rectangle((cx, cy), cell_w, cell_h, facecolor=cell["bg"], edgecolor=GREY, lw=1.5)
        ax.add_patch(rect)
        
        # Plant icon inside cell
        plant_y = cy + 0.35
        plant_x = cx + cell_w * 0.38
        draw_plant(plant_x, plant_y, tall=cell["tall"], scale=0.7)
        
        # Genotype label
        ax.text(cx + cell_w * 0.75, cy + cell_h * 0.5, cell["genotype"],
                ha="center", va="center", fontsize=13, fontweight="bold", color=INK)

    # Outer border for Punnett Square
    outer_rect = patches.Rectangle((gx, gy), 2 * cell_w, 2 * cell_h, fill=False, edgecolor=INK, lw=2.0)
    ax.add_patch(outer_rect)

    # F2 summary ratios on the right
    ax.text(9.5, 3.1, "3 tall : 1 dwarf", ha="left", va="center",
            fontsize=13, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.text(9.5, 2.3, "1 TT : 2 Tt : 1 tt", ha="left", va="center",
            fontsize=13, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    save(fig, out)
