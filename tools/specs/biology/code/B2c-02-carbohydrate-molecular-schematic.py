from style import *
import numpy as np
import matplotlib.patches as patches

def draw_hex(ax, cx, cy, r=0.35, color=BLUE, border_color=DEEP["blue"], lw=1.5):
    angles = np.linspace(0, 2*np.pi, 7) + np.pi/6
    x = cx + r * np.cos(angles)
    y = cy + r * np.sin(angles)
    poly = patches.Polygon(np.column_stack([x, y]), facecolor=color, edgecolor=border_color, linewidth=lw, zorder=3)
    ax.add_patch(poly)

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    # ---------------- TOP ROW: MONOSACCHARIDE ----------------
    ax.text(1.2, 8.8, "Monosaccharide", fontsize=14, fontweight="bold", ha="left", va="center", color=INK)
    ax.text(1.2, 8.4, "(single sugar unit)", fontsize=11, fontstyle="italic", ha="left", va="center", color=GREY)
    
    mono_x, mono_y = 6.0, 8.8
    draw_hex(ax, mono_x, mono_y, r=0.45, color=CREAM, border_color=DEEP["orange"], lw=2)
    ax.text(mono_x, mono_y, "glucose", fontsize=11, ha="center", va="center", color=INK, fontweight="bold")
    ax.text(mono_x, mono_y - 0.75, "monosaccharide (glucose)", fontsize=12, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # ---------------- REACTION ARROWS BETWEEN MONO AND DI ----------------
    arrow_down = patches.FancyArrowPatch((7.6, 8.3), (7.6, 6.7),
                                        connectionstyle="arc3,rad=-0.25",
                                        arrowstyle="->,head_length=5,head_width=3.5",
                                        color=DEEP["blue"], lw=1.8, zorder=4)
    ax.add_patch(arrow_down)
    ax.text(8.0, 7.5, "condensation (water removed)", fontsize=11, ha="left", va="center", color=DEEP["blue"])

    arrow_up = patches.FancyArrowPatch((4.4, 6.7), (4.4, 8.3),
                                      connectionstyle="arc3,rad=-0.25",
                                      arrowstyle="->,head_length=5,head_width=3.5",
                                      color=DEEP["pink"], lw=1.8, zorder=4)
    ax.add_patch(arrow_up)
    ax.text(4.0, 7.5, "hydrolysis (water added)", fontsize=11, ha="right", va="center", color=DEEP["pink"])

    # ---------------- MIDDLE ROW: DISACCHARIDE ----------------
    ax.text(1.2, 6.0, "Disaccharide", fontsize=14, fontweight="bold", ha="left", va="center", color=INK)
    ax.text(1.2, 5.6, "(two units joined)", fontsize=11, fontstyle="italic", ha="left", va="center", color=GREY)

    di_x1, di_y1 = 5.4, 6.0
    di_x2, di_y2 = 6.6, 6.0
    ax.plot([di_x1, di_x2], [di_y1, di_y2], color=DEEP["orange"], lw=3, zorder=2)
    draw_hex(ax, di_x1, di_y1, r=0.45, color=CREAM, border_color=DEEP["orange"], lw=2)
    draw_hex(ax, di_x2, di_y2, r=0.45, color=CREAM, border_color=DEEP["orange"], lw=2)
    ax.text(di_x1, di_y1, "glucose", fontsize=10, ha="center", va="center", color=INK)
    ax.text(di_x2, di_y2, "glucose", fontsize=10, ha="center", va="center", color=INK)

    ax.text(6.0, 5.15, "disaccharide (maltose)", fontsize=12, ha="center", va="center", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Divider line
    ax.plot([1.0, 11.0], [4.5, 4.5], color=GREY, lw=0.8, linestyle="--")

    # ---------------- BOTTOM ROW: POLYSACCHARIDES ----------------
    ax.text(1.2, 4.0, "Polysaccharide", fontsize=14, fontweight="bold", ha="left", va="center", color=INK)
    ax.text(1.2, 3.6, "(long chains of many units)", fontsize=11, fontstyle="italic", ha="left", va="center", color=GREY)
    ax.text(6.0, 4.2, "polysaccharide", fontsize=13, fontweight="bold", ha="center", va="center", color=INK)

    # 1. Starch: a long chain of many hexagons
    ax.text(1.2, 3.2, "starch", fontsize=13, fontweight="bold", ha="left", va="center", color=DEEP["green"])
    
    starch_x_start = 4.2
    starch_y = 3.2
    spacing = 0.82
    num_starch = 8
    
    ax.plot([starch_x_start, starch_x_start + (num_starch - 1) * spacing], [starch_y, starch_y],
            color=DEEP["green"], lw=3, zorder=2)
    ax.plot([starch_x_start + (num_starch - 1) * spacing + 0.35, starch_x_start + (num_starch - 1) * spacing + 1.1],
            [starch_y, starch_y], color=DEEP["green"], lw=2, linestyle=":", zorder=2)

    for i in range(num_starch):
        cx = starch_x_start + i * spacing
        draw_hex(ax, cx, starch_y, r=0.33, color=GREEN, border_color=DEEP["green"], lw=1.5)

    # 2. Glycogen: branched chain
    ax.text(1.2, 1.2, "glycogen", fontsize=13, fontweight="bold", ha="left", va="center", color=DEEP["blue"])
    
    gly_x_start = 4.2
    gly_y_main = 1.0
    num_gly = 8
    ax.plot([gly_x_start, gly_x_start + (num_gly - 1) * spacing], [gly_y_main, gly_y_main],
            color=DEEP["blue"], lw=3, zorder=2)
    ax.plot([gly_x_start + (num_gly - 1) * spacing + 0.35, gly_x_start + (num_gly - 1) * spacing + 1.1],
            [gly_y_main, gly_y_main], color=DEEP["blue"], lw=2, linestyle=":", zorder=2)

    for i in range(num_gly):
        cx = gly_x_start + i * spacing
        draw_hex(ax, cx, gly_y_main, r=0.33, color=LAV, border_color=DEEP["blue"], lw=1.5)

    # Branch 1 from hex 2 (index 2)
    b1_x0 = gly_x_start + 2 * spacing
    b1_nodes = [(b1_x0 + 0.3, gly_y_main + 0.6), (b1_x0 + 0.8, gly_y_main + 1.0), (b1_x0 + 1.5, gly_y_main + 1.1)]
    ax.plot([b1_x0, b1_nodes[0][0], b1_nodes[1][0], b1_nodes[2][0]],
            [gly_y_main, b1_nodes[0][1], b1_nodes[1][1], b1_nodes[2][1]],
            color=DEEP["blue"], lw=2.5, zorder=2)
    for bx, by in b1_nodes:
        draw_hex(ax, bx, by, r=0.3, color=LAV, border_color=DEEP["blue"], lw=1.5)

    # Sub-branch off branch 1
    sub_x, sub_y = b1_nodes[1][0] + 0.2, b1_nodes[1][1] + 0.55
    ax.plot([b1_nodes[1][0], sub_x], [b1_nodes[1][1], sub_y], color=DEEP["blue"], lw=2, zorder=2)
    draw_hex(ax, sub_x, sub_y, r=0.28, color=LAV, border_color=DEEP["blue"], lw=1.5)

    # Branch 2 from hex 5 (index 5)
    b2_x0 = gly_x_start + 5 * spacing
    b2_nodes = [(b2_x0 + 0.3, gly_y_main + 0.65), (b2_x0 + 0.8, gly_y_main + 1.1), (b2_x0 + 1.4, gly_y_main + 1.25)]
    ax.plot([b2_x0, b2_nodes[0][0], b2_nodes[1][0], b2_nodes[2][0]],
            [gly_y_main, b2_nodes[0][1], b2_nodes[1][1], b2_nodes[2][1]],
            color=DEEP["blue"], lw=2.5, zorder=2)
    for bx, by in b2_nodes:
        draw_hex(ax, bx, by, r=0.3, color=LAV, border_color=DEEP["blue"], lw=1.5)

    save(fig, out)
