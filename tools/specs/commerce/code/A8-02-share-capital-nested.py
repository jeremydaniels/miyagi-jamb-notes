from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Definitions of nested rectangles (x, y, width, height, fill_color, border_color, label)
    # Bottom aligned or nested concentrically / neatly stacked
    # Centered horizontally around x = 5.0
    rectangles = [
        {
            "w": 9.0, "h": 6.2, "x": 0.5, "y": 0.6,
            "fc": BLUE, "ec": DEEP["blue"],
            "title": "Authorized Capital (₦200,000)",
            "label_y": 6.45
        },
        {
            "w": 7.4, "h": 4.8, "x": 1.3, "y": 0.8,
            "fc": GREEN, "ec": DEEP["green"],
            "title": "Issued Capital (₦160,000)",
            "label_y": 5.25
        },
        {
            "w": 5.8, "h": 3.4, "x": 2.1, "y": 1.0,
            "fc": ORANGE, "ec": DEEP["orange"],
            "title": "Called-up Capital (₦120,000)",
            "label_y": 4.05
        },
        {
            "w": 4.2, "h": 2.0, "x": 2.9, "y": 1.2,
            "fc": PINK, "ec": DEEP["pink"],
            "title": "Paid-up Capital (₦117,500)",
            "label_y": 2.2
        }
    ]

    for r in rectangles:
        rect = patches.FancyBboxPatch(
            (r["x"], r["y"]), r["w"], r["h"],
            boxstyle="round,pad=0.08,rounding_size=0.15",
            linewidth=2.5,
            edgecolor=r["ec"],
            facecolor=r["fc"],
            zorder=2
        )
        ax.add_patch(rect)

    # Add labels on each band/layer
    for r in rectangles:
        ax.text(
            5.0, r["label_y"],
            r["title"],
            ha="center", va="center",
            fontsize=15,
            fontweight="bold",
            color=INK,
            zorder=5
        )

    save(fig, out)
