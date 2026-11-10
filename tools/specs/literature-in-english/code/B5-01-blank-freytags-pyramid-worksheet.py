from style import *
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis("off")

    # Title
    ax.text(50, 66, "Freytag's Pyramid", fontsize=18, fontweight="bold", color=INK, ha="center", va="center")

    # Coordinates for the pyramid peak and line
    # Left base, Climax peak, Right base
    p_expo = (10, 24)
    p_rising = (30, 39)
    p_climax = (50, 54)
    p_falling = (70, 39)
    p_resol = (90, 24)

    # Main plot mountain lines
    ax.plot([p_expo[0], p_climax[0], p_resol[0]], [p_expo[1], p_climax[1], p_resol[1]], 
            color=DEEP["blue"], lw=3.5, zorder=2)

    # Dots at each stage
    stages = [
        {"name": "Exposition", "pt": p_expo, "box_pos": (2, 4), "box_w": 16, "box_h": 14, "line_top": 24},
        {"name": "Rising Action", "pt": p_rising, "box_pos": (22, 19), "box_w": 16, "box_h": 14, "line_top": 39},
        {"name": "Climax", "pt": p_climax, "box_pos": (42, 34), "box_w": 16, "box_h": 14, "line_top": 54},
        {"name": "Falling Action", "pt": p_falling, "box_pos": (62, 19), "box_w": 16, "box_h": 14, "line_top": 39},
        {"name": "Resolution", "pt": p_resol, "box_pos": (82, 4), "box_w": 16, "box_h": 14, "line_top": 24},
    ]

    for stage in stages:
        x, y = stage["pt"]
        # Marker on mountain
        ax.plot(x, y, "o", color=DEEP["blue"], markersize=8, zorder=4)

        # Label above or near stage point
        label_y = y + 3.2
        ax.text(x, label_y, stage["name"], fontsize=14, fontweight="bold", 
                color=INK, ha="center", va="bottom",
                bbox=dict(fc="white", ec="none", pad=1.5))

        # Vertical connector to student response box
        bx, by = stage["box_pos"]
        bw, bh = stage["box_w"], stage["box_h"]
        box_top = by + bh
        
        ax.plot([x, x], [y, box_top], color=GREY, lw=1.5, ls="--", zorder=1)

        # Student writing box
        rect = patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.3,rounding_size=0.8",
            facecolor="white",
            edgecolor=GREY,
            linewidth=1.5,
            zorder=3
        )
        ax.add_patch(rect)

        # Subtle faint lined guide marks inside the box for student writing
        for line_y_offset in [0.25, 0.5, 0.75]:
            line_y = by + bh * line_y_offset
            ax.plot([bx + 1.2, bx + bw - 1.2], [line_y, line_y], 
                    color=CREAM, lw=1.0, ls=":", zorder=3)

    save(fig, out)
