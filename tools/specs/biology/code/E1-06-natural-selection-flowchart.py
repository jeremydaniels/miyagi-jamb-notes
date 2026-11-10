from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas size: vertical flowchart with 7 boxes
    fig = canvas(12, 18)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Overall Title
    ax.text(50, 97.5, "Darwin's Theory of Natural Selection", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Box specifications
    box_w = 84
    box_h = 10.5
    box_x = 8
    
    # Centers for the 7 stages vertically from top to bottom
    y_centers = [90, 77, 64, 51, 38, 25, 12]
    
    # Text data (spelled exactly as required)
    stages = [
        {
            "title": "1 Overproduction",
            "desc": "Organisms produce more offspring than the environment can support.",
            "sub": "(e.g. female frog lays hundreds of eggs)"
        },
        {
            "title": "2 Population stays fairly constant",
            "desc": "Despite overproduction, adult population sizes remain stable over time.",
            "sub": "(limited environmental carrying capacity)"
        },
        {
            "title": "3 Struggle for existence",
            "desc": "Intraspecific competition for limited resources and danger from predators.",
            "sub": "(competition for food, shelter, and survival)"
        },
        {
            "title": "4 Variation",
            "desc": "Individuals in a population show phenotypic and genetic variations.",
            "sub": "(differences in speed, leg length, and camouflage)"
        },
        {
            "title": "5 Survival of the fittest (natural selection)",
            "desc": "Individuals best adapted survive; poorly adapted are eliminated.",
            "sub": "(faster individuals escape predators, slower are caught)"
        },
        {
            "title": "6 Favourable variations inherited",
            "desc": "Survivors reproduce, passing advantageous characteristics to offspring.",
            "sub": "(favourable traits increase in frequency in the next generation)"
        },
        {
            "title": "7 New species over many generations",
            "desc": "Accumulation of adaptive changes eventually leads to speciation.",
            "sub": "(branching lineages diverge to form distinct new species)"
        }
    ]

    # Draw boxes and connector arrows
    for i in range(7):
        yc = y_centers[i]
        yb = yc - box_h / 2
        
        # Soft background card
        bg_col = CREAM if i % 2 == 0 else "#F4F6F9"
        card = patches.FancyBboxPatch((box_x, yb), box_w, box_h,
                                      boxstyle="round,pad=0.5,rounding_size=1.5",
                                      facecolor=bg_col, edgecolor=GREY, lw=1.5)
        ax.add_patch(card)
        
        # Icon area panel (left side of each box): x from 9.2 to 31.2, width 22
        icon_panel = patches.Rectangle((box_x + 1.2, yb + 1), 22, box_h - 2,
                                       facecolor="white", edgecolor=GREY, lw=1, zorder=2)
        ax.add_patch(icon_panel)

        # Connector arrow to next box
        if i < 6:
            next_yb = y_centers[i+1] + box_h / 2
            ax.annotate("", xy=(50, next_yb + 0.2), xytext=(50, yb - 0.2),
                        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                        color=DEEP["blue"], lw=2.5))

        # Text labels on the right
        text_x = box_x + 25.5
        ax.text(text_x, yc + 2.5, stages[i]["title"], 
                fontsize=14, fontweight="bold", color=INK, va="center")
        ax.text(text_x, yc - 0.3, stages[i]["desc"], 
                fontsize=11.5, color=INK, va="center")
        ax.text(text_x, yc - 2.8, stages[i]["sub"], 
                fontsize=10.5, fontstyle="italic", color=DEEP["blue"], va="center")

    # --- Draw Icons inside icon panels ---
    # Icon panel bounds: x in [9.2, 31.2], center x = 20.2
    
    # Icon 1: Frog surrounded by eggs
    ic1_x, ic1_y = 20.2, 90
    ax.add_patch(patches.Ellipse((ic1_x, ic1_y - 0.4), 4.2, 2.8, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5, zorder=3))
    ax.add_patch(patches.Circle((ic1_x - 1.2, ic1_y + 1.1), 0.7, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2, zorder=4))
    ax.add_patch(patches.Circle((ic1_x + 1.2, ic1_y + 1.1), 0.7, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2, zorder=4))
    ax.plot([ic1_x - 1.2], [ic1_y + 1.2], marker='o', markersize=3, color=INK, zorder=5)
    ax.plot([ic1_x + 1.2], [ic1_y + 1.2], marker='o', markersize=3, color=INK, zorder=5)
    egg_angles = np.linspace(0, 2 * np.pi, 22, endpoint=False)
    for ang in egg_angles:
        rad = 3.6 + 0.8 * np.sin(ang * 3)
        ex = ic1_x + rad * np.cos(ang)
        ey = ic1_y + (rad * 0.65) * np.sin(ang)
        ax.add_patch(patches.Circle((ex, ey), 0.35, facecolor="#E0F2FE", edgecolor=DEEP["blue"], lw=0.8, zorder=3))
        ax.plot([ex], [ey], marker='.', markersize=2, color=INK, zorder=4)

    # Icon 2: Graph with flat line (population stays constant)
    ic2_x, ic2_y = 20.2, 77
    ax.plot([ic2_x - 7.0, ic2_x + 7.5], [ic2_y - 3.0, ic2_y - 3.0], color=INK, lw=1.5, zorder=3)
    ax.plot([ic2_x - 7.0, ic2_x - 7.0], [ic2_y - 3.0, ic2_y + 3.2], color=INK, lw=1.5, zorder=3)
    xs_exp = np.linspace(ic2_x - 7.0, ic2_x + 2.0, 30)
    ys_exp = (ic2_y - 3.0) + 0.1 * np.exp(0.55 * (xs_exp - (ic2_x - 7.0)))
    ax.plot(xs_exp[ys_exp <= ic2_y + 3.2], ys_exp[ys_exp <= ic2_y + 3.2], 
            linestyle="--", color=GREY, lw=1.4, zorder=3)
    xs_plat = np.linspace(ic2_x - 6.8, ic2_x + 7.2, 50)
    ys_plat = ic2_y + 0.2 + 0.22 * np.sin(xs_plat * 2.5)
    ax.plot(xs_plat, ys_plat, color=DEEP["green"], lw=2.2, zorder=4)
    ax.text(ic2_x + 5.0, ic2_y - 4.0, "Time", fontsize=8, ha="center", color=INK)
    ax.text(ic2_x - 7.8, ic2_y + 2.4, "Pop.", fontsize=8, ha="right", color=INK)

    # Helper function for quadruped
    def draw_beast(bx, by, scale, col, outline, leg_len=1.0, is_lion=False):
        body_h = 0.9 * scale
        body_w = 2.0 * scale
        ax.add_patch(patches.Ellipse((bx, by), body_w, body_h, facecolor=col, edgecolor=outline, lw=1.2, zorder=4))
        hx = bx + (1.2 * scale)
        hy = by + (0.8 * scale)
        ax.add_patch(patches.Circle((hx, hy), 0.5 * scale, facecolor=col, edgecolor=outline, lw=1.2, zorder=4))
        if not is_lion:
            ax.plot([hx, hx + 0.3 * scale], [hy + 0.4 * scale, hy + 1.1 * scale], color=outline, lw=1.3, zorder=5)
        else:
            ax.add_patch(patches.Circle((hx - 0.2 * scale, hy), 0.7 * scale, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1, zorder=3))
        fl_y = by - (1.2 * scale * leg_len)
        ax.plot([bx + 0.6 * scale, bx + 0.6 * scale], [by - 0.2 * scale, fl_y], color=outline, lw=1.5, zorder=4)
        ax.plot([bx - 0.6 * scale, bx - 0.6 * scale], [by - 0.2 * scale, fl_y], color=outline, lw=1.5, zorder=4)

    # Icon 3: Two antelopes competing for grass, lion in background
    ic3_x, ic3_y = 20.2, 64
    gx, gy = ic3_x - 0.5, ic3_y - 2.5
    for dx, gh in [(-0.6, 1.4), (-0.2, 1.8), (0.2, 2.0), (0.6, 1.5)]:
        ax.plot([gx + dx, gx + dx + 0.2], [gy, gy + gh], color=DEEP["green"], lw=1.6, zorder=5)
    draw_beast(ic3_x - 4.5, ic3_y - 1.2, 1.1, CREAM, DEEP["orange"])
    draw_beast(ic3_x + 3.5, ic3_y - 1.2, 1.1, CREAM, DEEP["orange"])
    draw_beast(ic3_x + 5.5, ic3_y + 1.6, 0.75, ORANGE, DEEP["orange"], is_lion=True)
    ax.text(ic3_x + 5.5, ic3_y + 3.0, "lion", fontsize=7.5, ha="center", color=DEEP["orange"], fontweight="bold")

    # Icon 4: Five antelopes with different leg lengths and colours
    ic4_x, ic4_y = 20.2, 51
    leg_factors = [0.7, 0.9, 1.05, 1.25, 1.45]
    shades = ["#FEE2E2", "#FEF3C7", "#E0F2FE", "#DCFCE7", "#F3E8FF"]
    outlines = [DEEP["pink"], DEEP["orange"], DEEP["blue"], DEEP["green"], DEEP["lav"]]
    x_pos = np.linspace(ic4_x - 7.5, ic4_x + 7.5, 5)
    for idx in range(5):
        draw_beast(x_pos[idx], ic4_y + 0.3, 0.65, shades[idx], outlines[idx], leg_len=leg_factors[idx])
        ax.plot([x_pos[idx] - 1.0, x_pos[idx] + 1.0], [ic4_y - 2.5, ic4_y - 2.5], color=GREY, lw=1)

    # Icon 5: Faster antelopes escaping lion while slower is caught
    ic5_x, ic5_y = 20.2, 38
    draw_beast(ic5_x + 6.0, ic5_y + 0.8, 0.9, "#DCFCE7", DEEP["green"], leg_len=1.4)
    ax.annotate("", xy=(ic5_x + 9.5, ic5_y + 1.5), xytext=(ic5_x + 7.5, ic5_y + 1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=1.8))
    draw_beast(ic5_x + 1.0, ic5_y + 1.2, 0.8, "#E0F2FE", DEEP["blue"], leg_len=1.2)
    draw_beast(ic5_x - 3.5, ic5_y - 1.0, 0.8, "#FEE2E2", DEEP["pink"], leg_len=0.7)
    draw_beast(ic5_x - 6.5, ic5_y - 0.8, 1.0, ORANGE, DEEP["orange"], is_lion=True)
    ax.text(ic5_x - 3.5, ic5_y + 1.5, "caught", fontsize=7.5, ha="center", color=DEEP["pink"], fontweight="bold")
    ax.text(ic5_x + 6.0, ic5_y - 2.5, "escapes", fontsize=7.5, ha="center", color=DEEP["green"], fontweight="bold")

    # Icon 6: Fast antelope with its young
    ic6_x, ic6_y = 20.2, 25
    draw_beast(ic6_x - 2.5, ic6_y + 0.2, 1.25, "#DCFCE7", DEEP["green"], leg_len=1.35)
    draw_beast(ic6_x + 5.0, ic6_y - 1.2, 0.65, "#DCFCE7", DEEP["green"], leg_len=1.35)
    ax.annotate("", xy=(ic6_x + 3.2, ic6_y - 0.6), xytext=(ic6_x + 0.2, ic6_y + 0.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=1.5, linestyle="--"))
    ax.text(ic6_x + 5.0, ic6_y + 1.5, "offspring", fontsize=8, ha="center", color=DEEP["green"])

    # Icon 7: Branching tree with new species at end of branch
    # Panel 7: x in [9.2, 31.2], center = (20.2, 12). Keep all graphics inside [10.5, 30.0].
    ic7_x, ic7_y = 19.5, 12
    # Time vertical arrow shifted neatly inside panel on the far left
    ax.annotate("", xy=(ic7_x - 8.2, ic7_y + 2.8), xytext=(ic7_x - 8.2, ic7_y - 2.8),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2))
    ax.text(ic7_x - 8.2, ic7_y + 3.3, "Time", fontsize=7.5, ha="center", va="bottom", color=GREY)

    # Phylogenetic tree
    # Trunk
    ax.plot([ic7_x - 6.0, ic7_x - 2.5], [ic7_y - 1.8, ic7_y - 0.2], color=INK, lw=2.2, zorder=3)
    # Ancestral branch
    ax.plot([ic7_x - 2.5, ic7_x + 2.8], [ic7_y - 0.2, ic7_y - 1.8], color=GREY, lw=1.8, zorder=3)
    ax.add_patch(patches.Circle((ic7_x + 3.2, ic7_y - 1.8), 0.5, facecolor=GREY, edgecolor=INK, lw=1, zorder=4))
    ax.text(ic7_x + 4.1, ic7_y - 1.8, "Ancestral", fontsize=7.5, va="center", ha="left", color=INK)

    # Diverging new species branch
    ax.plot([ic7_x - 2.5, ic7_x + 0.5], [ic7_y - 0.2, ic7_y + 1.5], color=DEEP["green"], lw=2.0, zorder=3)
    ax.plot([ic7_x + 0.5, ic7_x + 2.8], [ic7_y + 1.5, ic7_y + 2.0], color=DEEP["green"], lw=2.0, zorder=3)
    ax.add_patch(patches.Circle((ic7_x + 3.2, ic7_y + 2.0), 0.7, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.4, zorder=4))
    ax.text(ic7_x + 4.1, ic7_y + 2.0, "New\nspecies", fontsize=7.5, fontweight="bold", va="center", ha="left", color=DEEP["green"])

    save(fig, out)
