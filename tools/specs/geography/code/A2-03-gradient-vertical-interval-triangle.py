from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.8, 5.5)
    ax.axis("off")

    # Triangle coordinates: right angle at C(6.5, 1.0)
    # A (base start / foot of hill): (1.0, 1.0)
    # B (top of hill): (6.5, 4.2)
    # C (base right angle): (6.5, 1.0)
    ax_x, ax_y = 1.0, 1.0
    bx, by = 6.5, 4.2
    cx, cy = 6.5, 1.0

    # Fill slope / ground
    poly = plt.Polygon([[ax_x, ax_y], [bx, by], [cx, cy]], facecolor=CREAM, edgecolor="none")
    ax.add_patch(poly)

    # Right angle symbol at C
    sq_size = 0.35
    ax.plot([cx - sq_size, cx - sq_size, cx], [cy, cy + sq_size, cy + sq_size], color=INK, lw=1.5)

    # Main triangle lines
    # Base (Horizontal Equivalent)
    ax.plot([ax_x, cx], [ax_y, cy], color=INK, lw=2.5)
    # Vertical (Vertical Interval)
    ax.plot([cx, bx], [cy, by], color=INK, lw=2.5)
    # Hypotenuse (Slope)
    ax.plot([ax_x, bx], [ax_y, by], color=DEEP["green"], lw=3.5)

    # Hypotenuse label
    mid_x, mid_y = (ax_x + bx) / 2, (ax_y + by) / 2
    angle = np.degrees(np.arctan2(by - ax_y, bx - ax_x))
    ax.text(mid_x - 0.3, mid_y + 0.3, "Slope of the hill", fontsize=15, color=DEEP["green"],
            rotation=angle, rotation_mode='anchor', ha='center', va='bottom',
            weight='bold', bbox=dict(fc="white", ec="none", pad=2))

    # Base label (HE)
    ax.annotate("", xy=(cx, cy - 0.45), xytext=(ax_x, ax_y - 0.45),
                arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=1.8))
    ax.text((ax_x + cx) / 2, cy - 0.75, "Horizontal Equivalent (HE) = 2500 m",
            fontsize=14.5, color=DEEP["blue"], ha="center", va="top", weight="bold")

    # Vertical label (VI)
    ax.annotate("", xy=(cx + 0.4, by), xytext=(cx + 0.4, cy),
                arrowprops=dict(arrowstyle="<->", color=DEEP["orange"], lw=1.8))
    ax.text(cx + 0.65, (cy + by) / 2, "Vertical Interval (VI) = 250 m",
            fontsize=14.5, color=DEEP["orange"], ha="left", va="center", weight="bold")

    # Calculation text box
    calc_text = (
        "Gradient Calculation:\n\n"
        "Gradient = VI / HE\n"
        "              = 250 / 2500\n"
        "              = 1 in 10"
    )
    ax.text(7.2, 2.0, calc_text, fontsize=15, color=INK, va="center", ha="left",
            linespacing=1.4,
            bbox=dict(boxstyle="round,pad=0.8", fc="white", ec=GREY, lw=1.5))

    # Ground level line dashed
    ax.plot([0.5, ax_x], [ax_y, ax_y], color=GREY, ls="--", lw=1.5)

    save(fig, out)
