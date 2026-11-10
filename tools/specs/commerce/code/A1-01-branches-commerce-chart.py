from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(17, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 10)
    ax.axis('off')

    def draw_box(x, y, w, h, text, bg_color, border_color, fontsize=14, bold=False):
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.1,rounding_size=0.15",
            facecolor=bg_color,
            edgecolor=border_color,
            linewidth=2,
            zorder=3
        )
        ax.add_patch(rect)
        weight = 'bold' if bold else 'normal'
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=INK, weight=weight, zorder=4)

    # 1. Top box: COMMERCE
    draw_box(8.5, 9.2, 4.0, 0.9, "COMMERCE", CREAM, DEEP["orange"], fontsize=17, bold=True)

    # Branches from COMMERCE to TRADE and AIDS TO TRADE
    ax.plot([8.5, 8.5], [8.75, 8.35], color=INK, lw=2, zorder=2)
    ax.plot([3.675, 12.5], [8.35, 8.35], color=INK, lw=2, zorder=2)
    ax.plot([3.675, 3.675], [8.35, 7.8], color=INK, lw=2, zorder=2)
    ax.plot([12.5, 12.5], [8.35, 7.8], color=INK, lw=2, zorder=2)

    # 2. Main Branches
    draw_box(3.675, 7.35, 3.2, 0.8, "TRADE", BLUE, DEEP["blue"], fontsize=16, bold=True)
    draw_box(12.5, 7.35, 4.4, 0.8, "AIDS TO TRADE", LAV, DEEP["lav"], fontsize=16, bold=True)

    # --- UNDER TRADE ---
    ax.plot([3.675, 3.675], [6.95, 6.4], color=INK, lw=2, zorder=2)
    ax.plot([1.75, 5.6], [6.4, 6.4], color=INK, lw=2, zorder=2)
    ax.plot([1.75, 1.75], [6.4, 5.85], color=INK, lw=2, zorder=2)
    ax.plot([5.6, 5.6], [6.4, 5.85], color=INK, lw=2, zorder=2)

    draw_box(1.75, 5.4, 2.6, 0.8, "Home Trade", GREEN, DEEP["green"], fontsize=15, bold=True)
    draw_box(5.6, 5.4, 2.8, 0.8, "Foreign Trade", GREEN, DEEP["green"], fontsize=15, bold=True)

    # Sub-branches under Home Trade
    ax.plot([1.75, 1.75], [5.0, 4.2], color=INK, lw=2, zorder=2)
    ax.plot([1.0, 2.5], [4.2, 4.2], color=INK, lw=2, zorder=2)
    ax.plot([1.0, 1.0], [4.2, 3.4], color=INK, lw=2, zorder=2)
    ax.plot([2.5, 2.5], [4.2, 3.4], color=INK, lw=2, zorder=2)

    draw_box(1.0, 2.9, 1.3, 0.9, "Wholesale", PINK, DEEP["pink"], fontsize=14)
    draw_box(2.5, 2.9, 1.3, 0.9, "Retail", PINK, DEEP["pink"], fontsize=14)

    # Sub-branches under Foreign Trade
    ax.plot([5.6, 5.6], [5.0, 4.2], color=INK, lw=2, zorder=2)
    ax.plot([4.2, 7.0], [4.2, 4.2], color=INK, lw=2, zorder=2)
    ax.plot([4.2, 4.2], [4.2, 3.4], color=INK, lw=2, zorder=2)
    ax.plot([5.6, 5.6], [4.2, 3.4], color=INK, lw=2, zorder=2)
    ax.plot([7.0, 7.0], [4.2, 3.4], color=INK, lw=2, zorder=2)

    draw_box(4.2, 2.9, 1.25, 0.9, "Import", PINK, DEEP["pink"], fontsize=14)
    draw_box(5.6, 2.9, 1.25, 0.9, "Export", PINK, DEEP["pink"], fontsize=14)
    draw_box(7.0, 2.9, 1.35, 0.9, "Entrepot", PINK, DEEP["pink"], fontsize=14)

    # --- UNDER AIDS TO TRADE ---
    aids = [
        "Banking",
        "Insurance",
        "Transportation",
        "Warehousing",
        "Advertising",
        "Communication",
        "Tourism"
    ]
    
    xs = np.linspace(8.6, 16.4, 7)

    ax.plot([12.5, 12.5], [6.95, 6.0], color=INK, lw=2, zorder=2)
    ax.plot([xs[0], xs[-1]], [6.0, 6.0], color=INK, lw=2, zorder=2)

    for x_pos, name in zip(xs, aids):
        ax.plot([x_pos, x_pos], [6.0, 5.4], color=INK, lw=2, zorder=2)
        label = name
        if name == "Transportation":
            label = "Transpor-\ntation"
        elif name == "Warehousing":
            label = "Ware-\nhousing"
        elif name == "Communication":
            label = "Communi-\ncation"
        elif name == "Advertising":
            label = "Adverti-\nsing"
        draw_box(x_pos, 4.4, 1.15, 1.9, label, CREAM, DEEP["orange"], fontsize=14)

    save(fig, out)
