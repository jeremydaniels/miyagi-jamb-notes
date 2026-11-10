from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 8)
    ax.axis("off")

    # Dimensions
    x_left = 3.2
    x_right = 6.8
    y_bottom = 2.0
    plate_h = 4.5
    plate_w = 0.45
    y_top = y_bottom + plate_h

    # Draw Plates (side view / thick slabs)
    rect_left = patches.Rectangle((x_left - plate_w, y_bottom), plate_w, plate_h,
                                  facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    rect_right = patches.Rectangle((x_right, y_bottom), plate_w, plate_h,
                                   facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(rect_left)
    ax.add_patch(rect_right)

    # Positive and negative charge signs on plates
    y_charges = np.linspace(y_bottom + 0.45, y_top - 0.45, 6)
    for y_c in y_charges:
        ax.text(x_left - plate_w/2, y_c, "+", fontsize=15, fontweight="bold",
                ha="center", va="center", color=DEEP["pink"], zorder=4)
        ax.text(x_right + plate_w/2, y_c, "−", fontsize=16, fontweight="bold",
                ha="center", va="center", color=DEEP["blue"], zorder=4)

    # Uniform electric field lines (straight arrows from positive to negative plate)
    y_fields = np.linspace(y_bottom + 0.5, y_top - 0.5, 5)
    for y_f in y_fields:
        ax.annotate("", xy=(x_right - 0.05, y_f), xytext=(x_left + 0.05, y_f),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.45",
                                    lw=2, color=DEEP["orange"]), zorder=2)

    # Electric field label
    y_mid = (y_bottom + y_top) / 2
    x_mid = (x_left + x_right) / 2
    ax.text(x_mid, y_mid + 0.6, "Electric field E", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.9), zorder=5)

    # Distance d annotation (dimension line with arrows)
    y_d = y_bottom - 0.55
    ax.annotate("", xy=(x_left, y_d), xytext=(x_right, y_d),
                arrowprops=dict(arrowstyle="<->,head_width=0.3,head_length=0.4",
                                lw=1.5, color=INK), zorder=4)
    # Extension tick lines for distance d
    ax.plot([x_left, x_left], [y_bottom, y_d - 0.2], lw=1, ls="--", color=GREY)
    ax.plot([x_right, x_right], [y_bottom, y_d - 0.2], lw=1, ls="--", color=GREY)
    ax.text(x_mid, y_d - 0.35, "Distance d", fontsize=15, ha="center", va="top", color=INK)

    # Plate Labels
    ax.text(x_left - 0.7, y_top + 0.5, "Positive plate (+Q)", fontsize=15, ha="right", va="bottom",
            color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1))
    ax.annotate("", xy=(x_left - plate_w/2, y_top), xytext=(x_left - 0.8, y_top + 0.5),
                arrowprops=dict(arrowstyle="->", lw=1.3, color=INK))

    ax.text(x_right + 0.7, y_top + 0.5, "Negative plate (−Q)", fontsize=15, ha="left", va="bottom",
            color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1))
    ax.annotate("", xy=(x_right + plate_w/2, y_top), xytext=(x_right + 0.8, y_top + 0.5),
                arrowprops=dict(arrowstyle="->", lw=1.3, color=INK))

    # Circuit / Wires connecting plates to battery below
    y_wire_bottom = -1.2
    # Left wire
    ax.plot([x_left - plate_w/2, 1.2, 1.2, x_mid - 0.7],
            [y_mid, y_mid, y_wire_bottom, y_wire_bottom],
            color=INK, lw=2.2, zorder=2)
    # Right wire
    ax.plot([x_right + plate_w/2, 8.8, 8.8, x_mid + 0.7],
            [y_mid, y_mid, y_wire_bottom, y_wire_bottom],
            color=INK, lw=2.2, zorder=2)

    # Battery Symbol at center bottom
    # Long line: positive terminal (left)
    bat_h_long = 0.9
    ax.plot([x_mid - 0.7, x_mid - 0.25], [y_wire_bottom, y_wire_bottom], color=INK, lw=2.2)
    ax.plot([x_mid - 0.25, x_mid - 0.25], [y_wire_bottom - bat_h_long/2, y_wire_bottom + bat_h_long/2],
            color=INK, lw=3)

    # Short thick line: negative terminal (right)
    bat_h_short = 0.45
    ax.plot([x_mid + 0.25, x_mid + 0.25], [y_wire_bottom - bat_h_short/2, y_wire_bottom + bat_h_short/2],
            color=INK, lw=5)
    ax.plot([x_mid + 0.25, x_mid + 0.7], [y_wire_bottom, y_wire_bottom], color=INK, lw=2.2)

    # Battery polarity signs
    ax.text(x_mid - 0.45, y_wire_bottom + 0.5, "+", fontsize=15, ha="center", va="center", color=INK)
    ax.text(x_mid + 0.45, y_wire_bottom + 0.5, "−", fontsize=15, ha="center", va="center", color=INK)

    # Battery label
    ax.text(x_mid, y_wire_bottom - 0.75, "Battery (V)", fontsize=15, ha="center", va="top",
            color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    save(fig, out)
