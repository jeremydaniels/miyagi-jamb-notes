from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 11)
    
    # 3 subplots for First, Second, Third class levers
    axes = [fig.add_subplot(3, 1, i + 1) for i in range(3)]
    
    titles = [
        "First-Class Lever (Fulcrum in middle)",
        "Second-Class Lever (Load in middle)",
        "Third-Class Lever (Effort in middle)"
    ]
    
    # Helper to draw fulcrum (triangle)
    def draw_fulcrum(ax, x, y_bar_bottom, size=0.45):
        # Fulcrum apex touches bottom of the bar
        triangle = patches.Polygon(
            [[x, y_bar_bottom], [x - size, y_bar_bottom - size * 1.5], [x + size, y_bar_bottom - size * 1.5]],
            closed=True, facecolor=GREY, edgecolor=INK, lw=2, zorder=3
        )
        ax.add_patch(triangle)
        # Ground under fulcrum
        ax.plot([x - size * 1.3, x + size * 1.3], [y_bar_bottom - size * 1.5, y_bar_bottom - size * 1.5], color=INK, lw=2)
        ax.text(x, y_bar_bottom - size * 1.5 - 0.25, "Fulcrum", ha="center", va="top", fontsize=14, color=INK, fontweight="bold")

    # Helper to draw load (weight box on top of the bar)
    def draw_load(ax, x, y_bar_top, w=0.9, h=0.7):
        rect = patches.Rectangle(
            (x - w / 2, y_bar_top), w, h,
            facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3
        )
        ax.add_patch(rect)
        ax.text(x, y_bar_top + h / 2, "Load", ha="center", va="center", fontsize=14, color=INK, fontweight="bold")

    # Helper to draw effort arrow
    def draw_effort(ax, x, y_start, y_end, label_pos="above"):
        ax.annotate(
            "", xy=(x, y_end), xytext=(x, y_start),
            arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=10, headlength=10),
            zorder=4
        )
        if label_pos == "above":
            text_y = max(y_start, y_end) + 0.25
            va = "bottom"
        else:
            text_y = min(y_start, y_end) - 0.25
            va = "top"
        ax.text(x, text_y, "Effort", ha="center", va=va, fontsize=14, color=DEEP["blue"], fontweight="bold",
                bbox=dict(fc="white", ec="none", pad=1))

    # Helper to draw the horizontal lever bar
    def draw_bar(ax, x1, x2, y, thickness=0.2):
        bar = patches.Rectangle(
            (x1, y - thickness / 2), x2 - x1, thickness,
            facecolor=CREAM, edgecolor=INK, lw=2, zorder=2
        )
        ax.add_patch(bar)

    bar_y = 1.0
    bar_thick = 0.25
    y_top = bar_y + bar_thick / 2
    y_bot = bar_y - bar_thick / 2
    x_left, x_mid, x_right = 2.0, 5.0, 8.0

    for i, ax in enumerate(axes):
        ax.set_xlim(0.5, 9.5)
        ax.set_ylim(-0.4, 2.9)
        ax.axis("off")
        ax.set_title(titles[i], fontsize=16, pad=12, fontweight="bold", color=INK, loc="left")

        # Draw horizontal bar
        draw_bar(ax, 1.5, 8.5, bar_y, bar_thick)

        if i == 0:
            # First-class: Effort pushes down on left, Fulcrum in middle, Load on right
            draw_effort(ax, x_left, 2.2, y_top + 0.05, label_pos="above")
            draw_fulcrum(ax, x_mid, y_bot)
            draw_load(ax, x_right, y_top)

        elif i == 1:
            # Second-class: Fulcrum far left, Load in middle, Effort pulls up on right
            draw_fulcrum(ax, x_left, y_bot)
            draw_load(ax, x_mid, y_top)
            draw_effort(ax, x_right, y_top, 2.2, label_pos="above")

        elif i == 2:
            # Third-class: Fulcrum far left, Effort pulls up in middle, Load on right
            draw_fulcrum(ax, x_left, y_bot)
            draw_effort(ax, x_mid, y_top, 2.2, label_pos="above")
            draw_load(ax, x_right, y_top)

    plt.subplots_adjust(hspace=0.45)
    save(fig, out)
