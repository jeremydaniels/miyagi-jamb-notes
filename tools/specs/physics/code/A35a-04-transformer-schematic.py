from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-4.2, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(0, 3.8, "Step-up Transformer", ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Core Dimensions
    outer_w, outer_h = 6.4, 5.0
    inner_w, inner_h = 3.6, 2.6

    # Draw laminated core background
    core_outer = patches.Rectangle((-outer_w/2, -outer_h/2), outer_w, outer_h, 
                                   facecolor=CREAM, edgecolor=GREY, lw=2, zorder=1)
    ax.add_patch(core_outer)

    # Lamination lines inside core (vertical hatch effect)
    for x in np.linspace(-outer_w/2 + 0.2, outer_w/2 - 0.2, 22):
        ax.plot([x, x], [-outer_h/2, outer_h/2], color="#E5E0D8", lw=1.2, zorder=1)

    # Hollow center
    core_inner = patches.Rectangle((-inner_w/2, -inner_h/2), inner_w, inner_h, 
                                   facecolor="white", edgecolor=GREY, lw=2, zorder=2)
    ax.add_patch(core_inner)

    # Re-draw the strong core outlines
    rect_outer_line = patches.Rectangle((-outer_w/2, -outer_h/2), outer_w, outer_h, 
                                        fill=False, edgecolor=INK, lw=2.5, zorder=3)
    rect_inner_line = patches.Rectangle((-inner_w/2, -inner_h/2), inner_w, inner_h, 
                                        fill=False, edgecolor=INK, lw=2.5, zorder=3)
    ax.add_patch(rect_outer_line)
    ax.add_patch(rect_inner_line)

    # Magnetic flux loop (dashed line running through middle of core)
    # Mid-line coordinates: x at +-2.5, y at +-1.9
    flux_x = [-2.5, 2.5, 2.5, -2.5, -2.5]
    flux_y = [1.9, 1.9, -1.9, -1.9, 1.9]
    ax.plot(flux_x, flux_y, color=DEEP["pink"], lw=2.5, linestyle="--", zorder=4)

    # Flux direction arrows (clockwise loop)
    # Top arm (moving right)
    ax.annotate("", xy=(0.8, 1.9), xytext=(0.1, 1.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18), zorder=5)
    # Right arm (moving down)
    ax.annotate("", xy=(2.5, -0.6), xytext=(2.5, 0.1),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18), zorder=5)
    # Bottom arm (moving left)
    ax.annotate("", xy=(-0.8, -1.9), xytext=(-0.1, -1.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18), zorder=5)
    # Left arm (moving up)
    ax.annotate("", xy=(-2.5, 0.6), xytext=(-2.5, -0.1),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18), zorder=5)

    # Core label placed above the top arm with an arrow pointing cleanly to the core
    ax.annotate("Laminated soft iron core", xy=(0, 2.5), xytext=(0, 3.1),
                ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, shrinkB=4),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1.2), zorder=7)

    # Magnetic flux label placed in the center opening or bottom arm with a clean opaque box
    ax.text(0, -1.9, "Magnetic flux (Φ)", ha="center", va="center", 
            fontsize=14, color=DEEP["pink"], fontweight="bold",
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.3), zorder=7)

    # Left arm coil (Primary coil, few turns)
    p_turns = 4
    p_ys = np.linspace(1.2, -1.2, p_turns)
    
    # Input terminals
    ax.plot([-4.6, -3.2], [p_ys[0] + 0.3, p_ys[0] + 0.3], color=DEEP["blue"], lw=3.5, zorder=6)
    ax.plot([-3.2, -1.8], [p_ys[0] + 0.3, p_ys[0]], color=DEEP["blue"], lw=4, zorder=6)
    ax.text(-4.8, p_ys[0] + 0.3, "AC Input", ha="right", va="center", fontsize=14, color=INK)

    for i in range(p_turns):
        y_top = p_ys[i]
        y_bot = y_top - 0.45
        ax.plot([-3.2, -1.8], [y_top, y_bot], color=DEEP["blue"], lw=4, zorder=6)
        if i < p_turns - 1:
            next_top = p_ys[i+1]
            ax.plot([-1.8, -3.2], [y_bot, next_top], color=DEEP["blue"], lw=2.5, linestyle=":", zorder=2)

    # Bottom lead out
    ax.plot([-1.8, -3.2], [p_ys[-1] - 0.45, p_ys[-1] - 0.6], color=DEEP["blue"], lw=4, zorder=6)
    ax.plot([-3.2, -4.6], [p_ys[-1] - 0.6, p_ys[-1] - 0.6], color=DEEP["blue"], lw=3.5, zorder=6)

    # Right arm coil (Secondary coil, many turns)
    s_turns = 9
    s_ys = np.linspace(1.2, -1.2, s_turns)

    # Top lead from back
    ax.plot([4.6, 3.2], [s_ys[0] + 0.2, s_ys[0] + 0.2], color=DEEP["orange"], lw=3.5, zorder=6)
    ax.plot([3.2, 1.8], [s_ys[0] + 0.2, s_ys[0]], color=DEEP["orange"], lw=3.5, zorder=6)
    ax.text(4.8, s_ys[0] + 0.2, "AC Output", ha="left", va="center", fontsize=14, color=INK)

    for i in range(s_turns):
        y_top = s_ys[i]
        y_bot = y_top - 0.2
        ax.plot([1.8, 3.2], [y_top, y_bot], color=DEEP["orange"], lw=3.5, zorder=6)
        if i < s_turns - 1:
            next_top = s_ys[i+1]
            ax.plot([3.2, 1.8], [y_bot, next_top], color=DEEP["orange"], lw=2, linestyle=":", zorder=2)

    # Bottom lead out
    ax.plot([1.8, 3.2], [s_ys[-1] - 0.2, s_ys[-1] - 0.35], color=DEEP["orange"], lw=3.5, zorder=6)
    ax.plot([3.2, 4.6], [s_ys[-1] - 0.35, s_ys[-1] - 0.35], color=DEEP["orange"], lw=3.5, zorder=6)

    # Labels for Coils
    ax.annotate("Primary coil\n(few turns)", xy=(-3.2, 0), xytext=(-4.4, -2.8),
                fontsize=15, fontweight="bold", color=INK, ha="center",
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.35", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, shrinkB=4), zorder=7)

    ax.annotate("Secondary coil\n(many turns)", xy=(3.2, 0), xytext=(4.4, -2.8),
                fontsize=15, fontweight="bold", color=INK, ha="center",
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, shrinkB=4), zorder=7)

    save(fig, out)
