from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(13, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Colors
    AFFECTED_COLOR = DEEP["blue"]
    NORMAL_FILL = "white"
    LINE_COLOR = INK
    LINE_WIDTH = 2.0

    def draw_male(x, y, size=0.6, shaded=False, half=False):
        r = size / 2.0
        rect = patches.Rectangle((x - r, y - r), size, size, 
                                 facecolor=NORMAL_FILL, edgecolor=LINE_COLOR, lw=LINE_WIDTH, zorder=3)
        ax.add_patch(rect)
        if shaded:
            rect.set_facecolor(AFFECTED_COLOR)
        elif half:
            half_rect = patches.Rectangle((x - r, y - r), r, size, 
                                          facecolor=AFFECTED_COLOR, edgecolor='none', zorder=4)
            ax.add_patch(half_rect)
            border = patches.Rectangle((x - r, y - r), size, size, 
                                       facecolor='none', edgecolor=LINE_COLOR, lw=LINE_WIDTH, zorder=5)
            ax.add_patch(border)

    def draw_female(x, y, radius=0.3, shaded=False, half=False):
        circ = patches.Circle((x, y), radius, facecolor=NORMAL_FILL, edgecolor=LINE_COLOR, lw=LINE_WIDTH, zorder=3)
        ax.add_patch(circ)
        if shaded:
            circ.set_facecolor(AFFECTED_COLOR)
        elif half:
            wedge = patches.Wedge((x, y), radius, 90, 270, facecolor=AFFECTED_COLOR, edgecolor='none', zorder=4)
            ax.add_patch(wedge)
            border = patches.Circle((x, y), radius, facecolor='none', edgecolor=LINE_COLOR, lw=LINE_WIDTH, zorder=5)
            ax.add_patch(border)

    # Generation levels (y-coordinates)
    y1 = 6.6
    y2 = 4.3
    y3 = 2.0

    # Generation labels (I, II, III)
    ax.text(0.6, y1, "I", fontsize=16, fontweight="bold", va="center", ha="center", color=INK)
    ax.text(0.6, y2, "II", fontsize=16, fontweight="bold", va="center", ha="center", color=INK)
    ax.text(0.6, y3, "III", fontsize=16, fontweight="bold", va="center", ha="center", color=INK)

    # Generation I: Normal Father (Aa) & Normal Mother (Aa)
    x_p1, x_p2 = 3.6, 5.2
    draw_male(x_p1, y1, size=0.6, shaded=False)
    draw_female(x_p2, y1, radius=0.3, shaded=False)

    # Marriage line Gen I
    ax.plot([x_p1 + 0.3, x_p2 - 0.3], [y1, y1], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)
    # Line down from marriage to sibling bar
    x_p_mid = (x_p1 + x_p2) / 2.0
    ax.plot([x_p_mid, x_p_mid], [y1, 5.5], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)

    # Sibship line for Gen II children
    x_c1, x_c2, x_c3, x_c4 = 1.5, 2.9, 4.3, 7.3
    ax.plot([x_c1, x_c4], [5.5, 5.5], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)
    for xc in [x_c1, x_c2, x_c3, x_c4]:
        ax.plot([xc, xc], [5.5, y2 + 0.3], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)

    # Draw Gen II individuals
    draw_male(x_c1, y2, size=0.6, shaded=False)                 # unshaded square
    draw_female(x_c2, y2, radius=0.3, shaded=True)              # fully shaded circle (albinism)
    draw_female(x_c3, y2, radius=0.3, half=True)                # half-shaded circle (carrier daughter)
    draw_male(x_c4, y2, size=0.6, shaded=False)                 # unshaded square

    # Gen II Marriage: carrier daughter (x_c3=4.3) married to unshaded square (normal male at x=5.7)
    x_spouse = 5.7
    draw_male(x_spouse, y2, size=0.6, shaded=False)
    ax.plot([x_c3 + 0.3, x_spouse - 0.3], [y2, y2], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)

    # Line down from Gen II marriage to Gen III
    x_m2 = (x_c3 + x_spouse) / 2.0
    ax.plot([x_m2, x_m2], [y2, 3.2], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)

    # Gen III children: unshaded circle and fully shaded square
    x_g3_1 = 4.2
    x_g3_2 = 5.8
    ax.plot([x_g3_1, x_g3_2], [3.2, 3.2], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)
    ax.plot([x_g3_1, x_g3_1], [3.2, y3 + 0.3], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)
    ax.plot([x_g3_2, x_g3_2], [3.2, y3 + 0.3], color=LINE_COLOR, lw=LINE_WIDTH, zorder=2)

    draw_female(x_g3_1, y3, radius=0.3, shaded=False)           # unshaded circle
    draw_male(x_g3_2, y3, size=0.6, shaded=True)                # fully shaded square

    # Genotypes and Labels
    # Gen I labels: "Aa", "Aa"
    ax.text(x_p1, y1 - 0.55, "Aa", fontsize=13, ha="center", va="top", color=INK, fontweight="bold")
    ax.text(x_p2, y1 - 0.55, "Aa", fontsize=13, ha="center", va="top", color=INK, fontweight="bold")

    # Annotation for parents: "both parents must be carriers (Aa)"
    ax.annotate("both parents must be carriers (Aa)",
                xy=(x_p_mid, y1), xytext=(x_p_mid, 7.7),
                fontsize=12, ha="center", va="bottom", color=INK,
                arrowprops=dict(arrowstyle="->", color=LINE_COLOR, lw=1.3),
                bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY))

    # Gen II genotype for affected daughter: "aa"
    ax.text(x_c2, y2 - 0.55, "aa", fontsize=13, ha="center", va="top", color=INK, fontweight="bold")

    # Legend / Key on the right side
    leg_x = 9.8
    leg_y_top = 6.8
    leg_spacing = 1.1

    # Key box background
    key_box = patches.FancyBboxPatch((9.2, 2.5), 3.4, 5.0,
                                     boxstyle="round,pad=0.2",
                                     fc=CREAM, ec=GREY, lw=1.0, zorder=1)
    ax.add_patch(key_box)

    ax.text(leg_x + 0.5, 7.1, "Key", fontsize=14, fontweight="bold", color=INK, ha="left", va="center")

    # Key 1: Normal male
    draw_male(leg_x, leg_y_top - 0.7, size=0.5, shaded=False)
    ax.text(leg_x + 0.55, leg_y_top - 0.7, "normal male", fontsize=12, va="center", color=INK)

    # Key 2: Normal female
    y_k2 = leg_y_top - 0.7 - leg_spacing
    draw_female(leg_x, y_k2, radius=0.25, shaded=False)
    ax.text(leg_x + 0.55, y_k2, "normal female", fontsize=12, va="center", color=INK)

    # Key 3: Carrier
    y_k3 = y_k2 - leg_spacing
    draw_female(leg_x, y_k3, radius=0.25, half=True)
    ax.text(leg_x + 0.55, y_k3, "carrier", fontsize=12, va="center", color=INK)

    # Key 4: Affected (albinism)
    y_k4 = y_k3 - leg_spacing
    draw_female(leg_x, y_k4, radius=0.25, shaded=True)
    ax.text(leg_x + 0.55, y_k4, "affected (albinism)", fontsize=12, va="center", color=INK)

    save(fig, out)
