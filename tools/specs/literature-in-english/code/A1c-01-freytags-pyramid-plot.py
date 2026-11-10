from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    
    # Coordinates of the pyramid points
    # 1. Exposition (flat start): (0.8, 1.2) to (2.2, 1.2)
    # 2. Rising Action: (2.2, 1.2) to (5.0, 5.0)
    # 3. Climax: peak at (5.0, 5.0)
    # 4. Falling Action: (5.0, 5.0) to (7.8, 1.2)
    # 5. Resolution / Denouement: (7.8, 1.2) to (9.2, 1.2)
    
    x_pts = [0.8, 2.2, 5.0, 7.8, 9.2]
    y_pts = [1.2, 1.2, 5.0, 1.2, 1.2]
    
    # Light shaded background under the pyramid
    ax.fill_between(x_pts, y_pts, 0.4, color=CREAM, alpha=0.5, zorder=1)
    
    # Plot the pyramid line
    ax.plot(x_pts, y_pts, color=DEEP["blue"], lw=4.5, solid_capstyle='round', zorder=3)
    
    # Dashed line inside peak to indicate tension
    ax.plot([5.0, 5.0], [1.2, 4.85], color=GREY, ls='--', lw=1.8, zorder=2)
    
    # Highlight vertex nodes
    for x, y in zip(x_pts, y_pts):
        ax.plot(x, y, 'o', color=DEEP["blue"], mfc='white', mew=2.5, markersize=8, zorder=4)

    # 1. Exposition
    ax.text(1.5, 1.6, "1. Exposition", fontsize=15, weight="bold", color=INK,
            ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))

    # 2. Rising Action (angled or placed alongside the rising slope)
    ax.text(3.3, 3.4, "2. Rising Action", fontsize=15, weight="bold", color=INK,
            ha="right", va="bottom", rotation=48, rotation_mode="anchor",
            bbox=dict(fc="white", ec="none", pad=2))

    # 3. Climax (at top peak)
    ax.text(5.0, 5.35, "3. Climax", fontsize=16, weight="bold", color=DEEP["pink"],
            ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=3))

    # 4. Falling Action (placed alongside falling slope)
    ax.text(6.7, 3.4, "4. Falling Action", fontsize=15, weight="bold", color=INK,
            ha="left", va="bottom", rotation=-48, rotation_mode="anchor",
            bbox=dict(fc="white", ec="none", pad=2))

    # 5. Resolution / Denouement
    ax.text(8.5, 1.6, "5. Resolution / Denouement", fontsize=15, weight="bold", color=INK,
            ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))

    # "Tension" annotation under the peak
    ax.text(5.0, 3.0, "Tension", fontsize=16, weight="bold", color=DEEP["orange"],
            ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.5),
            zorder=5)

    # Secondary text explaining tension at climax
    ax.text(5.0, 2.3, "(highest at climax)", fontsize=14, style="italic", color=INK,
            ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=1.5),
            zorder=5)

    # Overall diagram title
    ax.text(5.0, 6.0, "Freytag's Pyramid", fontsize=18, weight="bold", color=INK, ha="center")

    # Clean axes layout
    ax.set_xlim(0, 10)
    ax.set_ylim(0.4, 6.5)
    ax.axis("off")
    
    save(fig, out)
