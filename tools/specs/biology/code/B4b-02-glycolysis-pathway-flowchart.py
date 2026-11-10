from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    # Pale cytoplasm-coloured box
    cyto_box = patches.FancyBboxPatch(
        (0.5, 0.5), 11.0, 9.5,
        boxstyle="round,pad=0.2,rounding_size=0.4",
        facecolor=CREAM, edgecolor=GREY, linewidth=1.5
    )
    ax.add_patch(cyto_box)

    # Cytoplasm title tag
    ax.text(1.0, 9.4, "cytoplasm", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2))

    # Exact required label: "no oxygen needed"
    ax.text(1.0, 8.8, "no oxygen needed", fontsize=12, fontstyle="italic", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1.0))

    # Helper function to draw carbon chains
    # Triose phosphate should be exactly 3 circles (with optional small phosphate tag at end)
    def draw_chain(cx, cy, n, r=0.21, color=BLUE, edge_color=DEEP["blue"], p_tag_both=False, p_tag_one=False):
        spacing = 0.52
        start_x = cx - (n - 1) * spacing / 2.0
        for i in range(n):
            x = start_x + i * spacing
            c = patches.Circle((x, cy), r, facecolor=color, edgecolor=edge_color, lw=1.8, zorder=4)
            ax.add_patch(c)
            ax.text(x, cy, "C", color=INK, fontsize=11, fontweight="bold", ha="center", va="center", zorder=5)

        # 6C sugar phosphate has phosphate tags at each end
        if p_tag_both:
            lx = start_x - 0.44
            ax.plot([lx + 0.15, start_x - r], [cy, cy], color=DEEP["orange"], lw=2, zorder=3)
            p1 = patches.Circle((lx, cy), 0.16, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.6, zorder=4)
            ax.add_patch(p1)
            ax.text(lx, cy, "P", color=INK, fontsize=9.5, fontweight="bold", ha="center", va="center", zorder=5)

            rx = start_x + (n - 1) * spacing + 0.44
            ax.plot([start_x + (n - 1) * spacing + r, rx - 0.15], [cy, cy], color=DEEP["orange"], lw=2, zorder=3)
            p2 = patches.Circle((rx, cy), 0.16, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.6, zorder=4)
            ax.add_patch(p2)
            ax.text(rx, cy, "P", color=INK, fontsize=9.5, fontweight="bold", ha="center", va="center", zorder=5)

    # Top: glucose (6C)
    draw_chain(4.8, 8.8, 6, color=BLUE, edge_color=DEEP["blue"])
    ax.text(4.8, 9.4, "glucose (6C)", fontsize=13.5, fontweight="bold", color=INK, ha="center")

    # Arrow 1: Glucose to 6C sugar phosphate
    ax.annotate("", xy=(4.8, 7.55), xytext=(4.8, 8.45),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=INK))

    # "2 ATP used" label on arrow 1
    ax.annotate("2 ATP used", xy=(4.8, 8.0), xytext=(3.0, 8.0),
                fontsize=12, color=DEEP["pink"], fontweight="bold", ha="center", va="center",
                arrowprops=dict(arrowstyle="->", lw=1.6, color=DEEP["pink"], connectionstyle="arc3,rad=-0.15"),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["pink"], lw=1.2))

    # 6C sugar phosphate (6 circles with phosphate tag at each end)
    draw_chain(4.8, 7.15, 6, color=BLUE, edge_color=DEEP["blue"], p_tag_both=True)
    ax.text(4.8, 6.55, "6C sugar phosphate", fontsize=13, fontweight="bold", color=INK, ha="center")

    # Split arrows to two 3C chains
    ax.annotate("", xy=(2.7, 5.5), xytext=(4.0, 6.25),
                arrowprops=dict(arrowstyle="->", lw=2.2, color=INK))
    ax.annotate("", xy=(6.9, 5.5), xytext=(5.6, 6.25),
                arrowprops=dict(arrowstyle="->", lw=2.2, color=INK))
    ax.text(4.8, 5.9, "splits into 2", fontsize=10.5, fontstyle="italic", color=GREY, ha="center")

    # 2 triose phosphate (3C): exactly two chains of 3 circles
    draw_chain(2.7, 5.15, 3, color=GREEN, edge_color=DEEP["green"])
    draw_chain(6.9, 5.15, 3, color=GREEN, edge_color=DEEP["green"])
    # Label placed safely above the two chains, fully clear of circles
    ax.text(4.8, 5.15, "2 triose phosphate (3C)", fontsize=12.5, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.28", fc="white", ec=GREY, lw=1.1))

    # Downward pathways from triose phosphate to pyruvic acid
    ax.annotate("", xy=(2.7, 2.15), xytext=(2.7, 4.6),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=INK))
    ax.annotate("", xy=(6.9, 2.15), xytext=(6.9, 4.6),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=INK))

    # Left offshoots
    ax.annotate("NADH", xy=(2.7, 4.0), xytext=(1.25, 4.0),
                fontsize=11.5, color=DEEP["blue"], fontweight="bold", ha="center", va="center",
                arrowprops=dict(arrowstyle="<-", lw=1.5, color=DEEP["blue"], connectionstyle="arc3,rad=0.18"),
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=DEEP["blue"], lw=1.2))
    ax.annotate("2 ATP", xy=(2.7, 2.9), xytext=(1.25, 2.9),
                fontsize=11.5, color=DEEP["green"], fontweight="bold", ha="center", va="center",
                arrowprops=dict(arrowstyle="<-", lw=1.5, color=DEEP["green"], connectionstyle="arc3,rad=0.18"),
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=DEEP["green"], lw=1.2))

    # Right offshoots
    ax.annotate("NADH", xy=(6.9, 4.0), xytext=(8.35, 4.0),
                fontsize=11.5, color=DEEP["blue"], fontweight="bold", ha="center", va="center",
                arrowprops=dict(arrowstyle="<-", lw=1.5, color=DEEP["blue"], connectionstyle="arc3,rad=-0.18"),
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=DEEP["blue"], lw=1.2))
    ax.annotate("2 ATP", xy=(6.9, 2.9), xytext=(8.35, 2.9),
                fontsize=11.5, color=DEEP["green"], fontweight="bold", ha="center", va="center",
                arrowprops=dict(arrowstyle="<-", lw=1.5, color=DEEP["green"], connectionstyle="arc3,rad=-0.18"),
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=DEEP["green"], lw=1.2))

    # Total labels between the two branches
    ax.text(4.8, 4.0, "2 NADH", fontsize=12.5, fontweight="bold", color=DEEP["blue"], ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["blue"], lw=1.2))
    ax.text(4.8, 2.9, "4 ATP made", fontsize=12.5, fontweight="bold", color=DEEP["green"], ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["green"], lw=1.2))

    # Bottom: pyruvic acid (3C)
    draw_chain(2.7, 1.7, 3, color=ORANGE, edge_color=DEEP["orange"])
    draw_chain(6.9, 1.7, 3, color=ORANGE, edge_color=DEEP["orange"])
    ax.text(4.8, 1.7, "2 pyruvic acid (3C)", fontsize=13, fontweight="bold", color=INK, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1.2))

    # Right side tally box
    tally_x = 10.35
    tally_y = 6.2
    tally_box = patches.FancyBboxPatch(
        (tally_x - 1.15, tally_y - 1.6), 2.3, 3.2,
        boxstyle="round,pad=0.2,rounding_size=0.25",
        facecolor="white", edgecolor=INK, linewidth=1.6
    )
    ax.add_patch(tally_box)

    ax.text(tally_x, tally_y + 1.25, "ENERGY TALLY", fontsize=11.5, fontweight="bold", color=INK, ha="center")
    ax.plot([tally_x - 0.9, tally_x + 0.9], [tally_y + 0.95, tally_y + 0.95], color=GREY, lw=1.2)

    ax.text(tally_x, tally_y + 0.45, "ATP used: 2", fontsize=12, color=DEEP["pink"], fontweight="bold", ha="center")
    ax.text(tally_x, tally_y - 0.2, "ATP made: 4", fontsize=12, color=DEEP["green"], fontweight="bold", ha="center")
    ax.plot([tally_x - 0.85, tally_x + 0.85], [tally_y - 0.65, tally_y - 0.65], color=INK, lw=1.4)
    ax.text(tally_x, tally_y - 1.15, "net gain: 2 ATP", fontsize=12.5, fontweight="bold", color=INK, ha="center")

    save(fig, out)
