from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(8, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 7)
    ax.set_aspect("equal")
    ax.axis("off")

    # Table coordinates
    table_y = 2.2
    ax.plot([-0.5, 8.5], [table_y, table_y], color=INK, lw=2.5)

    # Hatching below table
    hatch_xs = np.linspace(0.0, 8.0, 21)
    for hx in hatch_xs:
        ax.plot([hx, hx - 0.35], [table_y, table_y - 0.35], color=GREY, lw=1.5)

    # Rectangular block coordinates
    bx, by = 2.5, table_y
    bw, bh = 3.0, 1.8
    cx, cy = bx + bw / 2.0, by + bh / 2.0

    # Draw block
    rect = patches.Rectangle(
        (bx, by), bw, bh,
        facecolor=BLUE, edgecolor=DEEP["blue"],
        linewidth=2.5, zorder=2
    )
    ax.add_patch(rect)

    # Centre of mass dot
    ax.scatter([cx], [cy], color=INK, s=36, zorder=4)

    # Force Arrow Helper
    arrow_kw = dict(
        arrowstyle="-|>",
        mutation_scale=20,
        lw=2.5,
    )

    # 1. Weight (W) - downwards from centre
    w_end_y = cy - 2.4
    ax.annotate(
        "", xy=(cx, w_end_y), xytext=(cx, cy),
        arrowprops=dict(**arrow_kw, color=DEEP["orange"])
    )
    ax.text(
        cx, w_end_y - 0.2, "Weight ($W$)",
        ha="center", va="top", fontsize=15, color=INK,
        bbox=dict(fc="white", ec="none", pad=1)
    )

    # 2. Normal Reaction (R) - upwards from table / block
    r_end_y = (by + bh) + 1.8
    ax.annotate(
        "", xy=(cx, r_end_y), xytext=(cx, by + bh),
        arrowprops=dict(**arrow_kw, color=DEEP["green"])
    )
    ax.text(
        cx, r_end_y + 0.2, "Normal Reaction ($R$)",
        ha="center", va="bottom", fontsize=15, color=INK,
        bbox=dict(fc="white", ec="none", pad=1)
    )

    # 3. Applied Force (P) - to the right
    p_end_x = (bx + bw) + 2.0
    ax.annotate(
        "", xy=(p_end_x, cy), xytext=(bx + bw, cy),
        arrowprops=dict(**arrow_kw, color=DEEP["pink"])
    )
    ax.text(
        p_end_x + 0.15, cy, "Applied Force ($P$)",
        ha="left", va="center", fontsize=15, color=INK,
        bbox=dict(fc="white", ec="none", pad=1)
    )

    # 4. Frictional Force (F) - to the left along the boundary
    f_end_x = bx - 2.0
    ax.annotate(
        "", xy=(f_end_x, table_y), xytext=(bx, table_y),
        arrowprops=dict(**arrow_kw, color=INK)
    )
    ax.text(
        f_end_x - 0.15, table_y, "Frictional Force ($F$)",
        ha="right", va="center", fontsize=15, color=INK,
        bbox=dict(fc="white", ec="none", pad=1)
    )

    # Table label
    ax.text(
        7.8, table_y - 0.5, "Horizontal table",
        ha="right", va="top", fontsize=14, color=GREY, fontstyle="italic"
    )

    save(fig, out)
