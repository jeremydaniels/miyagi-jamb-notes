from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.2, 11.8)
    ax.set_ylim(-0.2, 7.8)
    ax.set_aspect("equal")
    ax.axis("off")

    # Axes arrows
    ax.annotate("", xy=(11.4, 0.6), xytext=(0.6, 0.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.annotate("", xy=(0.6, 7.4), xytext=(0.6, 0.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    ax.text(11.4, 0.22, "Time / Succession", fontsize=12, ha="right", va="bottom", color=INK, weight="bold")
    ax.text(0.3, 7.4, "Biomass & Structural Complexity", fontsize=12, ha="left", va="bottom", color=INK, weight="bold")

    # Stages definition: (x_start, x_end, y_level, label)
    stages = [
        (1.0, 2.3, 1.0, "bare soil"),
        (2.4, 3.7, 2.0, "weeds"),
        (3.8, 5.2, 3.0, "grasses"),
        (5.5, 6.9, 4.2, "shrubs"),
        (7.2, 8.6, 5.3, "young trees"),
        (8.9, 10.7, 6.4, "climax forest")
    ]

    # Colors for steps
    step_colors = [GREY, CREAM, GREEN, GREEN, DEEP["green"], DEEP["green"]]
    
    for i, (x1, x2, y, label) in enumerate(stages):
        # Fill under step
        rect = patches.Rectangle((x1, 0.6), x2 - x1, y - 0.6, fc=step_colors[i], ec="none", alpha=0.3)
        ax.add_patch(rect)
        # Top line of step
        ax.plot([x1, x2], [y, y], color=DEEP["green"], lw=3.2)
        
        # Label placement
        y_offset = 0.2
        if label == "climax forest":
            y_offset = 0.35
            
        ax.text((x1 + x2) / 2, y + y_offset, label, fontsize=11.5, ha="center", va="bottom",
                color=INK, weight="semibold", zorder=5,
                bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.9))

    # Connect staircase risers
    ax.plot([2.3, 2.4], [1.0, 2.0], color=DEEP["green"], lw=2.2, ls=":")
    ax.plot([3.7, 3.8], [2.0, 3.0], color=DEEP["green"], lw=2.2, ls=":")
    ax.plot([5.2, 5.5], [3.0, 4.2], color=DEEP["green"], lw=2.2)
    ax.plot([6.9, 7.2], [4.2, 5.3], color=DEEP["green"], lw=2.2)
    ax.plot([8.6, 8.9], [5.3, 6.4], color=DEEP["green"], lw=2.2)

    # Curved overarching arrow for natural succession
    ax.annotate("", xy=(8.8, 6.6), xytext=(4.2, 3.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3.0,
                                connectionstyle="arc3,rad=-0.16"))
    
    # Label for natural succession along the path
    ax.text(6.4, 5.9, "natural succession", fontsize=13, ha="center", va="center",
            color=DEEP["green"], weight="bold", rotation=27, zorder=6,
            bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.35", lw=1.3))

    # Plagioclimax horizontal branch staying flat at grass stage
    plagio_x_start = 5.2
    plagio_x_end = 11.2
    plagio_y = 3.0

    # Plagioclimax zone shading
    plagio_rect = patches.Rectangle((plagio_x_start, 0.6), plagio_x_end - plagio_x_start, plagio_y - 0.6,
                                   fc=ORANGE, ec="none", alpha=0.18)
    ax.add_patch(plagio_rect)

    # Flat line with arrow
    ax.annotate("", xy=(plagio_x_end, plagio_y), xytext=(plagio_x_start, plagio_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.5))

    # Label for plagioclimax
    ax.text(8.2, 2.3, "plagioclimax (held at grass stage)", fontsize=12, ha="center", va="top",
            color=INK, weight="bold", zorder=6,
            bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.4", lw=1.4))

    # Human intervention annotation
    ax.text(8.2, 4.0, "repeated burning and grazing", fontsize=11.5, ha="center", va="bottom",
            color=DEEP["orange"], weight="bold", zorder=6,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=0.9))

    # Distinct Flame Icon
    def draw_flame(fx, fy, s=1.0):
        # A wide teardrop with distinct wavy points to clearly look like fire, not an arrow
        t = np.linspace(0, 2 * np.pi, 50)
        x = fx + s * 0.35 * np.sin(t) * (1 - 0.3 * np.cos(t))
        y = fy + s * 0.4 * (1.2 * np.cos(t) - 0.8 * np.cos(2*t) - 0.4)
        ax.fill(x, y, fc=ORANGE, ec=DEEP["orange"], lw=1.5, zorder=5)
        # Inner flame
        xi = fx + s * 0.15 * np.sin(t)
        yi = fy + s * 0.2 * (1.2 * np.cos(t) - 0.8 * np.cos(2*t) - 0.6)
        ax.fill(xi, yi, fc=CREAM, ec="none", zorder=6)

    # Distinct Cow Silhouette
    def draw_cow(cx, cy, s=1.0):
        # Draw recognizable animal silhouette (body, legs, head, horns, tail)
        # Body
        ax.add_patch(patches.Rectangle((cx - 0.4*s, cy - 0.2*s), 0.8*s, 0.4*s, fc=GREY, ec=INK, lw=1, zorder=5))
        # Legs
        for lx in [-0.3, -0.1, 0.1, 0.3]:
            ax.plot([cx + lx*s, cx + lx*s], [cy - 0.2*s, cy - 0.6*s], color=INK, lw=2, zorder=5)
        # Head (grazing downward)
        head = patches.Polygon([
            [cx + 0.4*s, cy + 0.2*s],
            [cx + 0.6*s, cy - 0.3*s],
            [cx + 0.45*s, cy - 0.4*s],
            [cx + 0.3*s, cy]
        ], closed=True, fc=GREY, ec=INK, lw=1, zorder=5)
        ax.add_patch(head)
        # Horn
        ax.plot([cx + 0.45*s, cx + 0.55*s], [cy + 0.1*s, cy + 0.3*s], color=INK, lw=1.5, zorder=5)
        # Tail
        ax.plot([cx - 0.4*s, cx - 0.5*s], [cy + 0.1*s, cy - 0.4*s], color=INK, lw=1.5, zorder=5)

    # Place flame and grazing cattle icons distinctly along the plagioclimax line
    draw_flame(6.2, 3.4, s=0.8)
    draw_cow(7.0, 3.4, s=0.6)
    
    draw_flame(9.4, 3.4, s=0.8)
    draw_cow(10.2, 3.4, s=0.6)

    # Deflection arrow showing arrest/deflection down to plagioclimax
    ax.annotate("", xy=(5.4, 3.1), xytext=(5.7, 3.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, ls="--"))

    save(fig, out)
