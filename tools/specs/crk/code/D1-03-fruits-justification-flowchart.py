from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 5.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    # Overall title
    ax.text(7, 4.9, "The Sequence of Hope in Romans 5:3–5", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ax.text(7, 4.45, "“...suffering produces endurance, and endurance produces character, and character produces hope...”", 
            ha="center", va="center", fontsize=14, style="italic", color=INK)

    # Box specifications
    box_w = 2.4
    box_h = 3.0
    y_box = 0.8
    x_centers = [1.8, 5.2, 8.6, 12.0]

    box_data = [
        {
            "title": "Suffering",
            "sub": "(Tribulation)",
            "bg": GREY,
            "border": DEEP["orange"],
            "icon": "cloud"
        },
        {
            "title": "Endurance",
            "sub": "(Patience)",
            "bg": BLUE,
            "border": DEEP["blue"],
            "icon": "mountain"
        },
        {
            "title": "Character",
            "sub": "(Experience)",
            "bg": LAV,
            "border": DEEP["lav"],
            "icon": "diamond"
        },
        {
            "title": "Hope",
            "sub": "",
            "bg": ORANGE,
            "border": DEEP["pink"],
            "icon": "sunrise"
        }
    ]

    # Draw boxes and contents
    for i, (xc, d) in enumerate(zip(x_centers, box_data)):
        # Card outline
        rect = patches.FancyBboxPatch(
            (xc - box_w / 2, y_box), box_w, box_h,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor="white", edgecolor=d["border"],
            linewidth=2.5, zorder=2
        )
        ax.add_patch(rect)

        # Header banner inside card
        header_bg = patches.FancyBboxPatch(
            (xc - box_w / 2 + 0.05, y_box + box_h - 1.15), box_w - 0.1, 1.05,
            boxstyle="round,pad=0.05,rounding_size=0.15",
            facecolor=d["bg"], edgecolor="none", zorder=3
        )
        ax.add_patch(header_bg)

        # Title text
        if d["sub"]:
            ax.text(xc, y_box + box_h - 0.45, d["title"], ha="center", va="center",
                    fontsize=15, weight="bold", color=INK, zorder=4)
            ax.text(xc, y_box + box_h - 0.8, d["sub"], ha="center", va="center",
                    fontsize=13.5, color=INK, zorder=4)
        else:
            ax.text(xc, y_box + box_h - 0.6, d["title"], ha="center", va="center",
                    fontsize=16, weight="bold", color=INK, zorder=4)

        # Icon drawing area (xc, y_box + 0.9)
        iy = y_box + 0.95
        icon_type = d["icon"]

        if icon_type == "cloud":
            # Storm cloud icon with raindrops
            # Cloud puffs
            c1 = patches.Circle((xc - 0.35, iy - 0.05), 0.28, facecolor=GREY, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
            c2 = patches.Circle((xc, iy + 0.15), 0.38, facecolor=GREY, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
            c3 = patches.Circle((xc + 0.35, iy - 0.05), 0.28, facecolor=GREY, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
            cb = patches.Rectangle((xc - 0.35, iy - 0.33), 0.7, 0.3, facecolor=GREY, edgecolor="none", zorder=4)
            base_line = plt.Line2D([xc - 0.38, xc + 0.38], [iy - 0.33, iy - 0.33], color=DEEP["blue"], lw=1.5, zorder=5)
            ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(cb)
            ax.add_line(base_line)
            # Rain streaks
            for dx in [-0.28, -0.05, 0.2]:
                ax.plot([xc + dx, xc + dx - 0.1], [iy - 0.45, iy - 0.7], color=DEEP["blue"], lw=2, zorder=4)

        elif icon_type == "mountain":
            # Mountain with climber
            # Mountain peak
            peak = patches.Polygon([[xc - 0.75, iy - 0.65], [xc - 0.1, iy + 0.45], [xc + 0.55, iy - 0.65]],
                                   closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5, zorder=4)
            snow = patches.Polygon([[xc - 0.3, iy + 0.15], [xc - 0.1, iy + 0.45], [xc + 0.12, iy + 0.15],
                                    [xc, iy + 0.2], [xc - 0.15, iy + 0.12]],
                                   closed=True, facecolor="white", edgecolor=DEEP["blue"], lw=1.2, zorder=5)
            ax.add_patch(peak); ax.add_patch(snow)
            # Mountain climber on the left slope
            cx, cy = xc - 0.38, iy - 0.05
            head = patches.Circle((cx, cy + 0.12), 0.07, facecolor=INK, zorder=6)
            ax.add_patch(head)
            # Body, stick, backpack
            ax.plot([cx, cx - 0.06], [cy + 0.05, cy - 0.15], color=INK, lw=2.2, zorder=6) # torso/leg
            ax.plot([cx, cx + 0.08], [cy - 0.05, cy - 0.2], color=INK, lw=2, zorder=6) # front leg
            ax.plot([cx - 0.02, cx + 0.14], [cy + 0.02, cy - 0.22], color=DEEP["orange"], lw=2, zorder=6) # staff

        elif icon_type == "diamond":
            # Shining diamond icon
            # Diamond vertices
            top_y = iy + 0.35
            mid_y = iy + 0.12
            bot_y = iy - 0.55
            left_x = xc - 0.55
            right_x = xc + 0.55
            t_left = xc - 0.3
            t_right = xc + 0.3

            dia_poly = patches.Polygon([
                [left_x, mid_y], [t_left, top_y], [t_right, top_y],
                [right_x, mid_y], [xc, bot_y]
            ], closed=True, facecolor=LAV, edgecolor=DEEP["lav"], lw=1.8, zorder=4)
            ax.add_patch(dia_poly)
            # Facet lines
            ax.plot([left_x, right_x], [mid_y, mid_y], color=DEEP["lav"], lw=1.2, zorder=5)
            ax.plot([t_left, xc, t_right], [top_y, bot_y, top_y], color=DEEP["lav"], lw=1.2, zorder=5)
            ax.plot([t_left, xc, t_right], [mid_y, bot_y, mid_y], color=DEEP["lav"], lw=1.2, zorder=5)

            # Sparkle accents
            for sx, sy in [(xc - 0.65, iy + 0.4), (xc + 0.65, iy + 0.3), (xc + 0.5, iy - 0.35)]:
                ax.plot([sx - 0.08, sx + 0.08], [sy, sy], color=DEEP["orange"], lw=1.8, zorder=5)
                ax.plot([sx, sx], [sy - 0.08, sy + 0.08], color=DEEP["orange"], lw=1.8, zorder=5)

        elif icon_type == "sunrise":
            # Bright sunrise over horizon
            # Horizon line
            hy = iy - 0.3
            ax.plot([xc - 0.65, xc + 0.65], [hy, hy], color=DEEP["orange"], lw=2, zorder=5)
            # Sun semi-circle
            sun = patches.Wedge((xc, hy), 0.38, 0, 180, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5, zorder=4)
            ax.add_patch(sun)
            # Sun rays
            angles = np.linspace(20, 160, 7)
            for ang in angles:
                rad = np.radians(ang)
                r1, r2 = 0.46, 0.68
                x1, y1 = xc + r1 * np.cos(rad), hy + r1 * np.sin(rad)
                x2, y2 = xc + r2 * np.cos(rad), hy + r2 * np.sin(rad)
                ax.plot([x1, x2], [y1, y2], color=DEEP["orange"], lw=2, zorder=4)

    # Connecting arrows between boxes
    for i in range(3):
        x_start = x_centers[i] + box_w / 2 + 0.1
        x_end = x_centers[i+1] - box_w / 2 - 0.1
        y_mid = y_box + box_h / 2
        ax.annotate(
            "", xy=(x_end, y_mid), xytext=(x_start, y_mid),
            arrowprops=dict(
                arrowstyle="-|>", mutation_scale=22,
                color=DEEP["blue"], lw=3.0
            ), zorder=6
        )

    save(fig, out)
