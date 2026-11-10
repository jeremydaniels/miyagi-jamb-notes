from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title & Subtitle
    ax.text(5.0, 7.05, "Tactical Map: The Battle of Ai", fontsize=18, weight="bold", color=INK, ha="center")
    ax.text(5.0, 6.62, "Joshua draws out the army of Ai while the ambush captures the city",
            fontsize=14, color=GREY, ha="center", style="italic")

    # Wilderness plain in the southeast
    wilderness_pts = [[5.2, 0.4], [9.6, 0.4], [9.6, 3.8], [6.8, 3.2], [5.2, 1.8]]
    wilderness = patches.Polygon(wilderness_pts, closed=True, facecolor=CREAM, edgecolor="none", alpha=0.7, zorder=1)
    ax.add_patch(wilderness)
    ax.text(8.3, 0.75, "Wilderness\n(Desert Plain)", fontsize=14, color=GREY,
            ha="center", va="center", style="italic", zorder=2)

    # Hill / Ridge to the west (behind which the ambush forms)
    hx = np.linspace(0.8, 4.4, 120)
    hy = 4.7 + 0.65 * np.sin((hx - 0.8) / 3.6 * np.pi)
    ax.fill_between(hx, 3.6, hy, color=GREEN, alpha=0.35, zorder=1)
    ax.plot(hx, hy, color=DEEP["green"], lw=2.5, ls="--", zorder=2)
    ax.text(2.6, 5.75, "Hills West of Ai\n(Concealed Valley)", fontsize=14, color=DEEP["green"],
            ha="center", va="center", weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["green"], lw=1.3), zorder=4)

    # City of Ai (Walled enclosure)
    cx, cy = 5.2, 4.2
    cw, ch = 1.9, 1.5
    city_wall = patches.Rectangle((cx, cy), cw, ch, facecolor="#FDF6EE",
                                  edgecolor=DEEP["orange"], lw=3.2, zorder=3)
    ax.add_patch(city_wall)

    # Crenellations on top and bottom walls
    for pos_x in np.linspace(cx + 0.15, cx + cw - 0.15, 6):
        ax.plot([pos_x, pos_x], [cy + ch, cy + ch + 0.14], color=DEEP["orange"], lw=2.8, zorder=4)
        ax.plot([pos_x, pos_x], [cy - 0.14, cy], color=DEEP["orange"], lw=2.8, zorder=4)

    # City labels placed clearly in upper half
    ax.text(cx + cw / 2.0, cy + ch - 0.35, "City of Ai", fontsize=16, weight="bold", color=INK, ha="center", zorder=5)
    ax.text(cx + cw / 2.0, cy + ch - 0.72, "(Undefended)", fontsize=14, color=DEEP["orange"], ha="center", style="italic", zorder=5)

    # Open Gate on south/east wall
    ax.plot([cx + cw, cx + cw], [cy + 0.1, cy + 0.55], color="white", lw=4.5, zorder=4)
    ax.text(cx + cw + 0.15, cy + 0.32, "City Gate\n(Open)", fontsize=14, color=DEEP["pink"], ha="left", va="center", weight="bold")

    # Ambush Arrow: from behind the hill directly into the city
    ax.annotate("", xy=(cx + 0.3, cy + 0.4), xytext=(2.6, 4.3),
                arrowprops=dict(arrowstyle="-|>", mutation_scale=24, color=DEEP["blue"], lw=4.5),
                zorder=6)
    ax.text(2.3, 3.45, "Ambush (30,000 men)\nenters undefended city", fontsize=14, weight="bold",
            color=DEEP["blue"], ha="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["blue"], lw=1.3),
            zorder=7)

    # Joshua's retreat arrow (Blue arrow heading toward wilderness)
    ret_start = (cx + cw + 0.2, cy + 0.1)
    ret_end = (9.4, 2.0)
    ax.annotate("", xy=ret_end, xytext=ret_start,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=24, color=DEEP["blue"], lw=4.5),
                zorder=5)
    ax.text(9.2, 1.4, "Joshua's Main Force\n(Feigning retreat to wilderness)", fontsize=14, weight="bold",
            color=DEEP["blue"], ha="right",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["blue"], lw=1.3),
            zorder=7)

    # King of Ai's army arrow: originates explicitly from within/at the open gate
    pursue_start = (cx + cw - 0.2, cy + 0.32)
    pursue_end = (8.4, 2.5)
    ax.annotate("", xy=pursue_end, xytext=pursue_start,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=22, color=DEEP["pink"], lw=4.0),
                zorder=6)
    ax.text(6.4, 2.5, "King of Ai's Army\n(Pursuing out of city)", fontsize=14, weight="bold",
            color=DEEP["pink"], ha="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["pink"], lw=1.3),
            zorder=7)

    # North indicator
    nx, ny = 0.9, 1.8
    ax.annotate("", xy=(nx, ny + 0.8), xytext=(nx, ny),
                arrowprops=dict(arrowstyle="-|>", mutation_scale=16, color=INK, lw=2), zorder=5)
    ax.text(nx, ny + 0.9, "N", fontsize=15, weight="bold", color=INK, ha="center", va="bottom")

    # Legend box
    leg_x, leg_y = 0.5, 0.4
    leg_w, leg_h = 3.6, 1.2
    leg_rect = patches.Rectangle((leg_x, leg_y), leg_w, leg_h, facecolor="white",
                                 edgecolor=GREY, lw=1.2, zorder=5)
    ax.add_patch(leg_rect)
    ax.plot([leg_x + 0.25, leg_x + 0.8], [leg_y + 0.8, leg_y + 0.8], color=DEEP["blue"], lw=3.5, zorder=6)
    ax.text(leg_x + 0.95, leg_y + 0.8, "Israelite movements", fontsize=14, color=INK, va="center", zorder=6)
    ax.plot([leg_x + 0.25, leg_x + 0.8], [leg_y + 0.35, leg_y + 0.35], color=DEEP["pink"], lw=3.5, zorder=6)
    ax.text(leg_x + 0.95, leg_y + 0.35, "Pursuit by King of Ai", fontsize=14, color=INK, va="center", zorder=6)

    save(fig, out)
