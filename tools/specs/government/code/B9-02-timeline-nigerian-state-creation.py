from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_axes([0.05, 0.08, 0.90, 0.84])
    ax.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(1956, 2000)
    ax.set_ylim(-1.5, 5.5)

    # Title & Subtitle
    ax.text(1978, 5.0, "Nigeria's State Creation Timeline (1960–1996)", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    ax.text(1978, 4.4, "Evolution of administrative divisions from Independence to 36 States", 
            ha='center', va='center', fontsize=14, fontstyle='italic', color=GREY)

    # Timeline events data
    events = [
        {"year": 1960, "title": "3 Regions", "sub": "(Independence)", "leader": "Independence", "n_div": 3, "color": DEEP["green"]},
        {"year": 1963, "title": "4 Regions", "sub": "(Balewa)", "leader": "Balewa", "n_div": 4, "color": DEEP["blue"]},
        {"year": 1967, "title": "12 States", "sub": "(Gowon)", "leader": "Gowon", "n_div": 12, "color": DEEP["orange"]},
        {"year": 1976, "title": "19 States", "sub": "(Murtala)", "leader": "Murtala", "n_div": 19, "color": DEEP["pink"]},
        {"year": 1987, "title": "21 States", "sub": "(Babangida)", "leader": "Babangida", "n_div": 21, "color": DEEP["lav"]},
        {"year": 1991, "title": "30 States", "sub": "(Babangida)", "leader": "Babangida", "n_div": 30, "color": DEEP["blue"]},
        {"year": 1996, "title": "36 States", "sub": "(Abacha)", "leader": "Abacha", "n_div": 36, "color": DEEP["green"]}
    ]

    # Main timeline axis line
    y_axis = 1.0
    ax.plot([1958, 1998.5], [y_axis, y_axis], color=INK, lw=2.5, zorder=2)
    # Arrow head for timeline
    ax.annotate('', xy=(1999, y_axis), xytext=(1998, y_axis),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=15))

    # Helper to draw a schematic map icon split into roughly n_div pieces
    def draw_map_icon(center_x, center_y, n_div, primary_color):
        w, h = 3.6, 1.3
        rx, ry = center_x - w/2, center_y - h/2
        
        # Base container / border
        bg_rect = patches.FancyBboxPatch((rx, ry), w, h, boxstyle="round,pad=0.08,rounding_size=0.15",
                                         facecolor=CREAM, edgecolor=GREY, lw=1.2, zorder=3)
        ax.add_patch(bg_rect)

        # Draw schematic partitioning inside
        if n_div == 3:
            # 3 Regions (North, West, East)
            # horizontal divide at 55%
            ax.plot([rx + 0.1, rx + w - 0.1], [ry + 0.55*h, ry + 0.55*h], color=primary_color, lw=1.5, zorder=4)
            # vertical divide in southern half
            ax.plot([rx + 0.5*w, rx + 0.5*w], [ry + 0.1, ry + 0.55*h], color=primary_color, lw=1.5, zorder=4)
        elif n_div == 4:
            # 4 Regions (North, West, Mid-West, East)
            ax.plot([rx + 0.1, rx + w - 0.1], [ry + 0.55*h, ry + 0.55*h], color=primary_color, lw=1.5, zorder=4)
            ax.plot([rx + 0.4*w, rx + 0.4*w], [ry + 0.1, ry + 0.55*h], color=primary_color, lw=1.5, zorder=4)
            ax.plot([rx + 0.7*w, rx + 0.7*w], [ry + 0.1, ry + 0.55*h], color=primary_color, lw=1.5, zorder=4)
        elif n_div == 12:
            # 3 rows, 4 cols
            for frac in [0.35, 0.68]:
                ax.plot([rx + 0.1, rx + w - 0.1], [ry + frac*h, ry + frac*h], color=primary_color, lw=1.1, zorder=4)
            for frac in [0.28, 0.52, 0.76]:
                ax.plot([rx + frac*w, rx + frac*w], [ry + 0.1, ry + h - 0.1], color=primary_color, lw=1.1, zorder=4)
        elif n_div == 19:
            # 4 rows, 5 cols
            for frac in [0.25, 0.5, 0.75]:
                ax.plot([rx + 0.1, rx + w - 0.1], [ry + frac*h, ry + frac*h], color=primary_color, lw=1.0, zorder=4)
            for frac in [0.22, 0.42, 0.62, 0.80]:
                ax.plot([rx + frac*w, rx + frac*w], [ry + 0.1, ry + h - 0.1], color=primary_color, lw=1.0, zorder=4)
        elif n_div == 21:
            for frac in [0.25, 0.5, 0.75]:
                ax.plot([rx + 0.1, rx + w - 0.1], [ry + frac*h, ry + frac*h], color=primary_color, lw=1.0, zorder=4)
            for frac in [0.20, 0.38, 0.55, 0.72, 0.86]:
                ax.plot([rx + frac*w, rx + frac*w], [ry + 0.1, ry + h - 0.1], color=primary_color, lw=0.9, zorder=4)
        elif n_div == 30:
            for frac in [0.2, 0.4, 0.6, 0.8]:
                ax.plot([rx + 0.1, rx + w - 0.1], [ry + frac*h, ry + frac*h], color=primary_color, lw=0.9, zorder=4)
            for frac in [0.18, 0.35, 0.52, 0.68, 0.84]:
                ax.plot([rx + frac*w, rx + frac*w], [ry + 0.1, ry + h - 0.1], color=primary_color, lw=0.9, zorder=4)
        elif n_div == 36:
            for frac in [0.2, 0.4, 0.6, 0.8]:
                ax.plot([rx + 0.1, rx + w - 0.1], [ry + frac*h, ry + frac*h], color=primary_color, lw=0.9, zorder=4)
            for frac in [0.15, 0.30, 0.45, 0.60, 0.75, 0.88]:
                ax.plot([rx + frac*w, rx + frac*w], [ry + 0.1, ry + h - 0.1], color=primary_color, lw=0.9, zorder=4)

    for i, ev in enumerate(events):
        yr = ev["year"]
        c = ev["color"]

        # Timeline marker dot
        ax.scatter([yr], [y_axis], s=120, color=c, edgecolors=INK, linewidth=1.8, zorder=5)

        # Connecting vertical line up to map icon
        map_y = 2.6
        ax.plot([yr, yr], [y_axis, map_y - 0.65], color=GREY, linestyle=':', lw=1.5, zorder=1)

        # Draw schematic map icon
        draw_map_icon(yr, map_y, ev["n_div"], c)

        # Label above map icon (number of divisions)
        ax.text(yr, map_y + 0.85, f"{ev['n_div']} units", ha='center', va='bottom',
                fontsize=14, fontweight='bold', color=c)

        # Text below the timeline: Year, Title, Sub/Leader
        # Alternating slightly in y to ensure zero overlap between dense consecutive years (1960/1963, 1987/1991)
        stagger = -0.35 if (i % 2 == 1) else 0.0

        ax.text(yr, y_axis - 0.45 + stagger, str(yr), ha='center', va='top',
                fontsize=15, fontweight='bold', color=INK,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none"))

        ax.text(yr, y_axis - 0.85 + stagger, ev["title"], ha='center', va='top',
                fontsize=14, fontweight='bold', color=c,
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none"))

        ax.text(yr, y_axis - 1.25 + stagger, ev["sub"], ha='center', va='top',
                fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none"))

    save(fig, out)
