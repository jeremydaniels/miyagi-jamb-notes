from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Title
    ax.text(6.0, 7.0, "Forms of Fiction: Scope and Length", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # Shelf/ground line
    ax.plot([0.8, 11.2], [2.2, 2.2], color=GREY, lw=2, zorder=1)

    books_data = [
        {
            "cx": 2.2,
            "width": 0.45,
            "height": 3.6,
            "color": GREEN,
            "deep": DEEP["green"],
            "title": "Short Story",
            "desc": "One main conflict,\nfew characters,\nread in one sitting."
        },
        {
            "cx": 5.8,
            "width": 1.25,
            "height": 3.6,
            "color": BLUE,
            "deep": DEEP["blue"],
            "title": "Novella/Novelette",
            "desc": "Longer than a short story,\nsingle focus but more\ncharacter development."
        },
        {
            "cx": 9.8,
            "width": 2.3,
            "height": 3.6,
            "color": ORANGE,
            "deep": DEEP["orange"],
            "title": "Novel",
            "desc": "Long, complex,\nmany characters,\nmultiple sub-plots."
        }
    ]

    for b in books_data:
        cx = b["cx"]
        w = b["width"]
        h = b["height"]
        y_bot = 2.2
        x_left = cx - w / 2.0

        # Spine rectangle (standing book facing viewer)
        rect = patches.FancyBboxPatch(
            (x_left, y_bot), w, h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            fc=b["color"], ec=b["deep"], lw=2.2, zorder=2
        )
        ax.add_patch(rect)

        # Spine decorative ribs/bands
        band_y = [y_bot + 0.4, y_bot + 0.5, y_bot + h - 0.5, y_bot + h - 0.4]
        for by in band_y:
            ax.plot([x_left + 0.05, x_left + w - 0.05], [by, by], 
                    color=b["deep"], lw=1.5, zorder=3)

        # Spine center label (rotated for thin/medium or stacked)
        if w < 0.8:
            ax.text(cx, y_bot + h/2.0, "SHORT STORY", rotation=90,
                    ha='center', va='center', fontsize=11, weight='bold', 
                    color=b["deep"], zorder=4)
        elif w < 1.8:
            ax.text(cx, y_bot + h/2.0, "NOVELLA", rotation=90,
                    ha='center', va='center', fontsize=13, weight='bold', 
                    color=b["deep"], zorder=4)
        else:
            ax.text(cx, y_bot + h/2.0, "NOVEL", rotation=0,
                    ha='center', va='center', fontsize=15, weight='bold', 
                    color=b["deep"], zorder=4)

        # Top Label
        ax.text(cx, 6.2, b["title"], ha='center', va='center',
                fontsize=16, weight='bold', color=INK)

        # Description text below book
        ax.text(cx, 1.1, b["desc"], ha='center', va='center',
                fontsize=14, color=INK, linespacing=1.35)

    save(fig, out)
