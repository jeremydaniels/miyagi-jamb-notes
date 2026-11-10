from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Helper to draw rounded box
    def draw_box(x, y, w, h, text, title_fc, border_col):
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.2,rounding_size=0.2",
            facecolor=title_fc,
            edgecolor=border_col,
            linewidth=2.5,
            zorder=3
        )
        ax.add_patch(rect)
        ax.text(
            x,
            y,
            text,
            ha="center",
            va="center",
            fontsize=15,
            fontweight="bold",
            color=INK,
            zorder=4
        )

    # 1. Top block: IASB
    draw_box(6.0, 9.8, 5.0, 1.1, "IASB (International)", BLUE, DEEP["blue"])

    # Arrow 1: IASB -> FRCN
    ax.annotate(
        "",
        xy=(6.0, 7.85),
        xytext=(6.0, 9.25),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["blue"]),
        zorder=2
    )
    ax.text(
        6.0,
        8.55,
        "Creates IFRS",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2),
        zorder=5
    )

    # 2. Middle block: FRCN
    draw_box(6.0, 7.3, 4.8, 1.1, "FRCN (Nigeria)", GREEN, DEEP["green"])

    # Arrow 2: FRCN down to Company / Auditors
    ax.annotate(
        "",
        xy=(6.0, 4.45),
        xytext=(6.0, 6.75),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"]),
        zorder=2
    )
    ax.text(
        6.0,
        5.6,
        "Enforces IFRS &\nregisters auditors",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2),
        zorder=5
    )

    # Central Company Building representation
    # Draw building container
    b_x, b_y, b_w, b_h = 4.2, 1.0, 3.6, 3.4
    b_rect = patches.FancyBboxPatch(
        (b_x, b_y),
        b_w,
        b_h,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        facecolor=CREAM,
        edgecolor=INK,
        linewidth=2.0,
        zorder=3
    )
    ax.add_patch(b_rect)

    # Roof decoration
    roof = patches.Polygon(
        [[b_x - 0.2, b_y + b_h], [b_x + b_w / 2, b_y + b_h + 0.6], [b_x + b_w + 0.2, b_y + b_h]],
        closed=True,
        facecolor=GREY,
        edgecolor=INK,
        linewidth=2.0,
        zorder=3
    )
    ax.add_patch(roof)

    # Company Building Title
    ax.text(
        6.0,
        4.0,
        "Company Building",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color=INK,
        zorder=4
    )

    # Accountants inside building
    acc_box = patches.FancyBboxPatch(
        (4.5, 1.5),
        3.0,
        1.9,
        boxstyle="round,pad=0.15,rounding_size=0.15",
        facecolor="white",
        edgecolor=DEEP["lav"],
        linewidth=2.0,
        zorder=4
    )
    ax.add_patch(acc_box)
    ax.text(
        6.0,
        2.7,
        "Accountants",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color=DEEP["lav"],
        zorder=5
    )
    ax.text(
        6.0,
        2.0,
        "(Financial Reporting\n& Auditing Staff)",
        ha="center",
        va="center",
        fontsize=12,
        color=INK,
        zorder=5
    )

    # 3. Bottom left block: CAC (Nigeria)
    draw_box(1.8, 2.7, 3.0, 1.3, "CAC\n(Nigeria)", BLUE, DEEP["blue"])

    # Arrow from CAC to Company Building
    ax.annotate(
        "",
        xy=(4.2, 3.2),
        xytext=(3.3, 3.2),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["blue"]),
        zorder=6
    )
    ax.text(
        3.75,
        3.8,
        "Registers company &\nenforces CAMA laws",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        color=INK,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1.0),
        zorder=7
    )

    # 4. Bottom right block: ICAN / ANAN (Nigeria)
    draw_box(10.2, 2.7, 3.1, 1.3, "ICAN / ANAN\n(Nigeria)", GREEN, DEEP["green"])

    # Arrow from ICAN / ANAN to Accountants inside company
    ax.annotate(
        "",
        xy=(7.5, 2.4),
        xytext=(8.65, 2.4),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=DEEP["green"]),
        zorder=6
    )
    ax.text(
        8.2,
        1.6,
        "Trains & disciplines\naccountants",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        color=INK,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1.0),
        zorder=7
    )

    save(fig, out)
