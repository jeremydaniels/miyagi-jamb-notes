from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_bracket(ax, x, y_min, y_max, is_left=True, width=0.15, color=INK, lw=2):
    sign = 1 if is_left else -1
    ax.plot([x + sign * width, x, x, x + sign * width],
            [y_max, y_max, y_min, y_min],
            color=color, lw=lw, solid_capstyle='round')

def draw(out):
    fig = canvas(11, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Color palette aliases
    RED_BORDER = DEEP["pink"]
    RED_FILL = PINK
    BLUE_BORDER = DEEP["blue"]
    BLUE_FILL = BLUE

    # --- Matrix 1 (First Matrix) ---
    # Center around x = 1.6, y = 3.6
    m1_x, m1_y = 1.6, 3.6
    draw_bracket(ax, m1_x - 0.9, m1_y - 0.9, m1_y + 0.9, is_left=True, width=0.2)
    draw_bracket(ax, m1_x + 0.9, m1_y - 0.9, m1_y + 0.9, is_left=False, width=0.2)

    # Highlight Row 1
    row_rect = patches.FancyBboxPatch((m1_x - 0.75, m1_y + 0.05), 1.5, 0.75,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=RED_FILL, edgecolor=RED_BORDER, lw=2.2)
    ax.add_patch(row_rect)

    # Matrix 1 elements
    ax.text(m1_x - 0.4, m1_y + 0.42, "a", fontsize=18, fontweight='bold', ha='center', va='center', color=RED_BORDER)
    ax.text(m1_x + 0.4, m1_y + 0.42, "b", fontsize=18, fontweight='bold', ha='center', va='center', color=RED_BORDER)
    ax.text(m1_x - 0.4, m1_y - 0.42, "c", fontsize=18, ha='center', va='center', color=INK)
    ax.text(m1_x + 0.4, m1_y - 0.42, "d", fontsize=18, ha='center', va='center', color=INK)

    # Row 1 arrow and label
    ax.annotate("", xy=(m1_x + 0.65, m1_y + 0.95), xytext=(m1_x - 0.65, m1_y + 0.95),
                arrowprops=dict(arrowstyle="->", color=RED_BORDER, lw=2.5))
    ax.text(m1_x, m1_y + 1.25, "Row 1", fontsize=16, fontweight='bold', color=RED_BORDER, ha='center', va='center')

    # Multiplication dot
    ax.text(3.0, m1_y, "·", fontsize=28, ha='center', va='center', color=INK, fontweight='bold')

    # --- Matrix 2 (Second Matrix) ---
    # Center around x = 4.4, y = 3.6
    m2_x, m2_y = 4.4, 3.6
    draw_bracket(ax, m2_x - 0.9, m2_y - 0.9, m2_y + 0.9, is_left=True, width=0.2)
    draw_bracket(ax, m2_x + 0.9, m2_y - 0.9, m2_y + 0.9, is_left=False, width=0.2)

    # Highlight Column 1
    col_rect = patches.FancyBboxPatch((m2_x - 0.75, m2_y - 0.78), 0.75, 1.56,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=BLUE_FILL, edgecolor=BLUE_BORDER, lw=2.2)
    ax.add_patch(col_rect)

    # Matrix 2 elements
    ax.text(m2_x - 0.38, m2_y + 0.42, "e", fontsize=18, fontweight='bold', ha='center', va='center', color=BLUE_BORDER)
    ax.text(m2_x + 0.38, m2_y + 0.42, "f", fontsize=18, ha='center', va='center', color=INK)
    ax.text(m2_x - 0.38, m2_y - 0.42, "g", fontsize=18, fontweight='bold', ha='center', va='center', color=BLUE_BORDER)
    ax.text(m2_x + 0.38, m2_y - 0.42, "h", fontsize=18, ha='center', va='center', color=INK)

    # Column 1 arrow and label
    ax.annotate("", xy=(m2_x - 0.98, m2_y - 0.55), xytext=(m2_x - 0.98, m2_y + 0.55),
                arrowprops=dict(arrowstyle="->", color=BLUE_BORDER, lw=2.5))
    ax.text(m2_x - 0.38, m2_y + 1.25, "Column 1", fontsize=16, fontweight='bold', color=BLUE_BORDER, ha='center', va='center')

    # Equals sign
    ax.text(5.8, m1_y, "=", fontsize=26, ha='center', va='center', color=INK)

    # --- Resulting Matrix ---
    # Center around x = 8.5, y = 3.6
    m3_x, m3_y = 8.5, 3.6
    draw_bracket(ax, m3_x - 2.3, m3_y - 0.9, m3_y + 0.9, is_left=True, width=0.25)
    draw_bracket(ax, m3_x + 2.3, m3_y - 0.9, m3_y + 0.9, is_left=False, width=0.25)

    # Highlight top-left result cell
    res_rect = patches.FancyBboxPatch((m3_x - 2.15, m3_y + 0.05), 2.7, 0.75,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.2)
    ax.add_patch(res_rect)

    # Formula breakdown in the highlighted top-left box: a·e + b·g
    calc_base_x = m3_x - 0.8
    calc_y = m3_y + 0.42

    ax.text(calc_base_x - 0.9, calc_y, "a", fontsize=18, fontweight='bold', color=RED_BORDER, ha='center', va='center')
    ax.text(calc_base_x - 0.65, calc_y, "·", fontsize=18, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(calc_base_x - 0.4, calc_y, "e", fontsize=18, fontweight='bold', color=BLUE_BORDER, ha='center', va='center')
    ax.text(calc_base_x, calc_y, "+", fontsize=16, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(calc_base_x + 0.4, calc_y, "b", fontsize=18, fontweight='bold', color=RED_BORDER, ha='center', va='center')
    ax.text(calc_base_x + 0.65, calc_y, "·", fontsize=18, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(calc_base_x + 0.9, calc_y, "g", fontsize=18, fontweight='bold', color=BLUE_BORDER, ha='center', va='center')

    # Other matrix elements
    ax.text(m3_x + 1.35, m3_y + 0.42, "· · ·", fontsize=16, ha='center', va='center', color=GREY)
    ax.text(m3_x - 0.8, m3_y - 0.42, "· · ·", fontsize=16, ha='center', va='center', color=GREY)
    ax.text(m3_x + 1.35, m3_y - 0.42, "· · ·", fontsize=16, ha='center', va='center', color=GREY)

    # Result annotation pointing to top-left
    ax.text(m3_x - 0.8, m3_y + 1.25, "Result goes in Row 1, Column 1",
            fontsize=15, fontweight='bold', color=DEEP["orange"], ha='center', va='center')

    # --- Bottom explanatory panel ---
    panel = patches.FancyBboxPatch((1.2, 0.7), 8.6, 1.25,
                                  boxstyle="round,pad=0.2,rounding_size=0.2",
                                  facecolor="#F8FAFC", edgecolor=GREY, lw=1.5)
    ax.add_patch(panel)

    ax.text(5.5, 1.5, "Multiply matching elements and add",
            fontsize=17, fontweight='bold', color=INK, ha='center', va='center')

    # Formula breakdown legend
    ax.text(3.7, 1.05, "a", fontsize=17, fontweight='bold', color=RED_BORDER, ha='center', va='center')
    ax.text(4.0, 1.05, "·", fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(4.3, 1.05, "e", fontsize=17, fontweight='bold', color=BLUE_BORDER, ha='center', va='center')
    ax.text(4.8, 1.05, "(1st elements)", fontsize=14, color=INK, ha='center', va='center')

    ax.text(5.6, 1.05, "+", fontsize=16, fontweight='bold', color=INK, ha='center', va='center')

    ax.text(6.4, 1.05, "b", fontsize=17, fontweight='bold', color=RED_BORDER, ha='center', va='center')
    ax.text(6.7, 1.05, "·", fontsize=17, fontweight='bold', color=INK, ha='center', va='center')
    ax.text(7.0, 1.05, "g", fontsize=17, fontweight='bold', color=BLUE_BORDER, ha='center', va='center')
    ax.text(7.55, 1.05, "(2nd elements)", fontsize=14, color=INK, ha='center', va='center')

    save(fig, out)
