from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Title
    ax.text(50, 93, "Unitary System of Government", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # Top Box: Central Government
    cg_x, cg_y, cg_w, cg_h = 15, 68, 70, 15
    rect_cg = patches.FancyBboxPatch((cg_x, cg_y), cg_w, cg_h,
                                     boxstyle="round,pad=1.5,rounding_size=2",
                                     linewidth=2.5, edgecolor=DEEP["blue"],
                                     facecolor=BLUE)
    ax.add_patch(rect_cg)

    ax.text(50, 78, "Central Government", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)
    ax.text(50, 72, "(Holds all constitutional power)", ha="center", va="center",
            fontsize=14, fontstyle="italic", color=INK)

    # Bottom Boxes: Local Authorities
    local_boxes = ["Local Authority A", "Local Authority B", "Local Authority C"]
    local_xs = [8, 38, 68]
    local_w, local_h = 24, 12
    local_y = 20

    for i, name in enumerate(local_boxes):
        lx = local_xs[i]
        rect_loc = patches.FancyBboxPatch((lx, local_y), local_w, local_h,
                                          boxstyle="round,pad=1.2,rounding_size=1.5",
                                          linewidth=2, edgecolor=DEEP["green"],
                                          facecolor=GREEN)
        ax.add_patch(rect_loc)
        ax.text(lx + local_w / 2, local_y + local_h / 2, name,
                ha="center", va="center", fontsize=14, fontweight="bold", color=INK)

        # Downward arrows from Central Government to each Local Authority
        target_x = lx + local_w / 2
        ax.annotate("", xy=(target_x, local_y + local_h + 0.5),
                    xytext=(target_x, cg_y - 0.5),
                    arrowprops=dict(arrowstyle="->", lw=2.2, color=DEEP["blue"],
                                    shrinkA=4, shrinkB=4))

    # Dotted line / return arrow representing powers delegated & revocable
    # Drawn curving back from right/bottom to the right side of Central Government
    arc = patches.FancyArrowPatch((86, local_y + local_h + 1), (86, cg_y - 1),
                                  connectionstyle="arc3,rad=-0.45",
                                  linestyle="--", linewidth=2.2,
                                  arrowstyle="->", color=DEEP["orange"])
    ax.add_patch(arc)

    # Label on dotted line / arrow
    ax.text(93, 49, "Powers delegated and\ncan be withdrawn",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=INK, bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP["orange"], lw=1.5))

    save(fig, out)
