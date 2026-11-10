from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(
        4.5, 6.4,
        "Transfer of Power in Nigeria (1993)",
        ha="center", va="center",
        fontsize=18, fontweight="bold", color=INK
    )

    # Box specifications: (center_x, center_y, width, height, text, bg_color, border_color)
    boxes = [
        (4.5, 5.3, 7.2, 0.9, "General Ibrahim Babangida\n(Military Rule)", CREAM, DEEP["orange"]),
        (4.5, 3.4, 7.2, 0.9, "Chief Ernest Shonekan\n(Interim National Government)", BLUE, DEEP["blue"]),
        (4.5, 1.5, 7.2, 0.9, "General Sani Abacha\n(Military Rule)", CREAM, DEEP["orange"])
    ]

    for cx, cy, w, h, text, bg, border in boxes:
        rect = patches.FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor=bg, edgecolor=border, linewidth=2.5
        )
        ax.add_patch(rect)
        ax.text(
            cx, cy, text,
            ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK
        )

    # Downward arrow 1: Top to Middle
    ax.annotate(
        "",
        xy=(4.5, 3.9), xytext=(4.5, 4.8),
        arrowprops=dict(
            arrowstyle="-|>",
            color=INK,
            lw=2.5,
            mutation_scale=22
        )
    )
    # Label for Arrow 1
    ax.text(
        4.5, 4.35, "Steps aside (Aug 26)",
        ha="center", va="center",
        fontsize=14, color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2)
    )

    # Downward arrow 2: Middle to Bottom
    ax.annotate(
        "",
        xy=(4.5, 2.0), xytext=(4.5, 2.9),
        arrowprops=dict(
            arrowstyle="-|>",
            color=INK,
            lw=2.5,
            mutation_scale=22
        )
    )
    # Label for Arrow 2
    ax.text(
        4.5, 2.45, "Forced resignation (Nov 17)",
        ha="center", va="center",
        fontsize=14, color=INK,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2)
    )

    save(fig, out)
