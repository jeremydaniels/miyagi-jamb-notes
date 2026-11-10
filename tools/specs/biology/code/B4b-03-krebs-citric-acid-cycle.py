from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 13)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6.5, 6.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Background: Pale mitochondrion matrix shape
    mito = patches.FancyBboxPatch(
        (-5.5, -6.0), 11.0, 12.0,
        boxstyle="round,pad=0.3,rounding_size=1.2",
        fc=CREAM, ec=GREY, lw=2.0, zorder=0
    )
    ax.add_patch(mito)
    ax.text(-5.0, 5.4, "mitochondrial matrix", fontsize=15, color=GREY, style='italic', weight='bold')

    # Helper for carbon circles
    def draw_carbons(x, y, n, col=INK, spacing=0.28, radius=0.1):
        x_start = x - (n - 1) * spacing / 2.0
        for i in range(n):
            c = patches.Circle((x_start + i * spacing, y), radius, fc=col, ec=INK, lw=1.2, zorder=5)
            ax.add_patch(c)

    # 1. LINK REACTION (Top area)
    # Pyruvic acid (3C)
    ax.text(0, 4.9, "pyruvic acid (3C)", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(0, 4.45, 3)

    # Arrow down for link reaction
    ax.annotate("", xy=(0, 3.2), xytext=(0, 4.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=18))
    ax.text(0.3, 3.75, "link reaction", fontsize=15, ha="left", va="center", color=DEEP["blue"], style="italic")

    # Link reaction by-products (curved side arrows)
    # CO2 leaving right/top
    ax.annotate("CO₂", xy=(0.0, 3.9), xytext=(2.2, 4.3),
                arrowprops=dict(arrowstyle="<-", color=GREY, lw=2.0, connectionstyle="arc3,rad=-0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=GREY,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    # NADH leaving left/top
    ax.annotate("NADH", xy=(0.0, 3.5), xytext=(-2.2, 3.9),
                arrowprops=dict(arrowstyle="<-", color=DEEP["orange"], lw=2.0, connectionstyle="arc3,rad=0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["orange"],
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2"))

    # Acetyl CoA (2C)
    ax.text(0, 2.85, "acetyl CoA (2C)", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(0, 2.45, 2)

    # Arrow from Acetyl CoA entering Krebs cycle
    ax.annotate("", xy=(1.0, 1.6), xytext=(0, 2.25),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=18))

    # Center title: Krebs cycle
    ax.text(0, -0.9, "Krebs cycle", fontsize=18, ha="center", va="center", weight="bold", color=INK)

    # Main Cycle circle
    R = 2.7
    cy = -1.0
    cx = 0.0

    # Clockwise circular pathway sections
    def draw_arc_arrow(deg_start, deg_end):
        arc = patches.Arc((cx, cy), 2 * R, 2 * R, angle=0, theta1=deg_end, theta2=deg_start,
                          color=DEEP["blue"], lw=3.5, zorder=2)
        ax.add_patch(arc)
        # Arrowhead at deg_end (clockwise direction: moving towards decreasing angle)
        rad = np.radians(deg_end)
        # Tangent vector for clockwise motion (-sin(theta), cos(theta) is counterclockwise, so sin, -cos is clockwise)
        dx = np.sin(rad) * 0.01
        dy = -np.cos(rad) * 0.01
        px = cx + R * np.cos(rad)
        py = cy + R * np.sin(rad)
        ax.annotate("", xy=(px + dx * 10, py + dy * 10), xytext=(px, py),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.5, mutation_scale=18))

    # Arcs between main stations
    # 1. Top to Right: Citric acid (6C) -> 5C acid (~60 deg down to ~ -15 deg)
    draw_arc_arrow(48, -5)
    # 2. Right to Bottom: 5C acid -> 4C acid (~ -35 deg to ~ -105 deg)
    draw_arc_arrow(-30, -85)
    # 3. Bottom to Left: 4C acid bottom -> 4C acid left (~ -130 deg to ~ -195 deg)
    draw_arc_arrow(-125, -170)
    # 4. Left to Top: 4C acid / Oxaloacetic acid back to top (~ -215 deg to ~ -290 deg [70 deg])
    draw_arc_arrow(170, 115)

    # STATIONS AROUND THE CYCLE

    # Top-right / entry: Citric acid (6C)
    c6_x, c6_y = 2.1, 1.45
    ax.text(c6_x, c6_y + 0.35, "citric acid (6C)", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(c6_x, c6_y - 0.1, 6)

    # Arc 1 by-products: CO2 & NADH
    ax.annotate("CO₂", xy=(3.0, 0.45), xytext=(4.7, 0.9),
                arrowprops=dict(arrowstyle="<-", color=GREY, lw=2.0, connectionstyle="arc3,rad=-0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=GREY,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    ax.annotate("NADH", xy=(2.9, 0.05), xytext=(4.7, 0.1),
                arrowprops=dict(arrowstyle="<-", color=DEEP["orange"], lw=2.0, connectionstyle="arc3,rad=-0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["orange"],
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2"))

    # Mid-right: 5C acid
    c5_x, c5_y = 2.8, -1.9
    ax.text(c5_x + 0.1, c5_y + 0.35, "5C acid", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(c5_x + 0.1, c5_y - 0.1, 5)

    # Arc 2 by-products: second CO2 & NADH
    ax.annotate("CO₂", xy=(2.1, -3.0), xytext=(3.8, -3.3),
                arrowprops=dict(arrowstyle="<-", color=GREY, lw=2.0, connectionstyle="arc3,rad=-0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=GREY,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    ax.annotate("NADH", xy=(1.5, -3.5), xytext=(2.9, -4.3),
                arrowprops=dict(arrowstyle="<-", color=DEEP["orange"], lw=2.0, connectionstyle="arc3,rad=-0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["orange"],
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2"))

    # Bottom: 4C acid
    c4b_x, c4b_y = -0.5, -4.2
    ax.text(c4b_x, c4b_y + 0.35, "4C acid", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(c4b_x, c4b_y - 0.1, 4)

    # Arc 3 by-products: ATP & FADH2
    ax.annotate("ATP", xy=(-1.7, -3.5), xytext=(-3.1, -4.3),
                arrowprops=dict(arrowstyle="<-", color=DEEP["green"], lw=2.0, connectionstyle="arc3,rad=0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["green"],
                bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.2"))
    ax.annotate("FADH₂", xy=(-2.6, -2.6), xytext=(-4.4, -2.9),
                arrowprops=dict(arrowstyle="<-", color=DEEP["orange"], lw=2.0, connectionstyle="arc3,rad=0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["orange"],
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2"))

    # Left / Arc 4 by-product: NADH
    ax.annotate("NADH", xy=(-2.85, -0.6), xytext=(-4.5, -0.6),
                arrowprops=dict(arrowstyle="<-", color=DEEP["orange"], lw=2.0, connectionstyle="arc3,rad=0.2"),
                fontsize=15, ha="center", va="center", weight="bold", color=DEEP["orange"],
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.2"))

    # Top-left: oxaloacetic acid (4C)
    c4t_x, c4t_y = -2.2, 1.45
    ax.text(c4t_x, c4t_y + 0.35, "oxaloacetic acid (4C)", fontsize=16, ha="center", va="center", weight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    draw_carbons(c4t_x, c4t_y - 0.1, 4)

    # Arrow from oxaloacetic acid meeting Acetyl CoA at Citric acid
    ax.annotate("", xy=(0.8, 1.6), xytext=(-1.0, 1.6),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=18))

    save(fig, out)
