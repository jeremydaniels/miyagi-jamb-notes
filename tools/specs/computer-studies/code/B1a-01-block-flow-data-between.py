from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Box styles and coordinates
    # Central CPU
    cpu_w, cpu_h = 3.6, 2.0
    cpu_x, cpu_y = 6.0 - cpu_w / 2, 4.3 - cpu_h / 2

    # Left: Input Unit
    in_w, in_h = 2.4, 1.8
    in_x, in_y = 1.0, 4.3 - in_h / 2

    # Right: Output Unit
    out_w, out_h = 2.4, 1.8
    out_x, out_y = 12.0 - 1.0 - out_w, 4.3 - out_h / 2

    # Below: Storage Unit
    st_w, st_h = 3.6, 1.5
    st_x, st_y = 6.0 - st_w / 2, 0.9

    # Draw boxes with rounded corners
    boxes = [
        (in_x, in_y, in_w, in_h, GREEN, DEEP["green"], "Input Unit"),
        (cpu_x, cpu_y, cpu_w, cpu_h, BLUE, DEEP["blue"], "Processing Unit\n(CPU)"),
        (out_x, out_y, out_w, out_h, ORANGE, DEEP["orange"], "Output Unit"),
        (st_x, st_y, st_w, st_h, LAV, DEEP["lav"], "Storage Unit"),
    ]

    for bx, by, bw, bh, fc, ec, label in boxes:
        rect = patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.08,rounding_size=0.25",
            facecolor=fc, edgecolor=ec, linewidth=2.5
        )
        ax.add_patch(rect)
        ax.text(
            bx + bw / 2, by + bh / 2, label,
            ha="center", va="center", fontsize=16, fontweight="bold",
            color=INK, multialignment="center"
        )

    # Arrow Helper
    arrow_kw = dict(
        arrowstyle="-|>",
        mutation_scale=22,
        color=INK,
        lw=2.5
    )

    # 1. Input Unit -> CPU
    ax.annotate(
        "",
        xy=(cpu_x, 4.3),
        xytext=(in_x + in_w, 4.3),
        arrowprops=arrow_kw
    )

    # 2. CPU -> Output Unit
    ax.annotate(
        "",
        xy=(out_x, 4.3),
        xytext=(cpu_x + cpu_w, 4.3),
        arrowprops=arrow_kw
    )

    # 3. CPU <-> Storage Unit (two vertical parallel arrows between them)
    # CPU bottom is at cpu_y = 3.3, Storage top is at st_y + st_h = 2.4
    # Down arrow (CPU -> Storage)
    ax.annotate(
        "",
        xy=(5.4, st_y + st_h),
        xytext=(5.4, cpu_y),
        arrowprops=arrow_kw
    )

    # Up arrow (Storage -> CPU)
    ax.annotate(
        "",
        xy=(6.6, cpu_y),
        xytext=(6.6, st_y + st_h),
        arrowprops=arrow_kw
    )

    # Optional clean data flow label above arrows or title
    ax.text(6.0, 6.4, "Functional Units of a Computer", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    save(fig, out)
