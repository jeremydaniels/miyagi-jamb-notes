from style import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 8.5)
    ax.axis('off')

    # Pyramid geometry
    # Peak at (4.5, 7.5), Base from (0.5, 0.5) to (8.5, 0.5)
    # 4 tiers:
    y_levels = [0.5, 2.25, 4.0, 5.75, 7.5]
    
    def x_left(y):
        return 4.5 - 4.5 * (7.5 - y) / 7.0

    def x_right(y):
        return 4.5 + 4.5 * (7.5 - y) / 7.0

    tiers = [
        {
            "name": "Magistrate Courts /\nArea & Customary Courts",
            "y0": y_levels[0], "y1": y_levels[1],
            "fc": CREAM, "ec": DEEP["orange"],
            "fs": 14.5
        },
        {
            "name": "Federal High Court / State High Courts /\nSharia & Customary Courts of Appeal",
            "y0": y_levels[1], "y1": y_levels[2],
            "fc": LAV, "ec": DEEP["lav"],
            "fs": 14.0
        },
        {
            "name": "Court of Appeal",
            "y0": y_levels[2], "y1": y_levels[3],
            "fc": BLUE, "ec": DEEP["blue"],
            "fs": 14.5
        },
        {
            "name": "Supreme Court",
            "y0": y_levels[3], "y1": y_levels[4],
            "fc": GREEN, "ec": DEEP["green"],
            "fs": 14.0
        }
    ]

    for tier in tiers:
        y0, y1 = tier["y0"], tier["y1"]
        x0_l, x0_r = x_left(y0), x_right(y0)
        x1_l, x1_r = x_left(y1), x_right(y1)
        pts = [(x0_l, y0), (x1_l, y1), (x1_r, y1), (x0_r, y0)]
        poly = Polygon(pts, closed=True, facecolor=tier["fc"], edgecolor=tier["ec"], lw=2.5, zorder=2)
        ax.add_patch(poly)

        # Label center
        y_mid = (y0 + y1) / 2.0
        if y1 == 7.5:
            y_mid = y0 + (y1 - y0) * 0.4
        
        ax.text(4.5, y_mid, tier["name"], ha='center', va='center',
                fontsize=tier["fs"], color=INK, weight='bold', zorder=3)

    # Side upward arrow indicating "Direction of Appeals"
    arrow_x = 9.3
    y_start = 0.8
    y_end = 7.2
    ax.annotate(
        "", xy=(arrow_x, y_end), xytext=(arrow_x, y_start),
        arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.7", color=DEEP["blue"], lw=3.0),
        zorder=4
    )

    # Label along arrow
    ax.text(arrow_x + 0.35, (y_start + y_end) / 2.0, "Direction of Appeals",
            ha='left', va='center', rotation=90, fontsize=15, weight='bold',
            color=DEEP["blue"], zorder=4)

    # Title
    ax.text(4.5, 8.0, "Hierarchy of Courts in Nigeria", ha='center', va='center',
            fontsize=17, weight='bold', color=INK)

    save(fig, out)
