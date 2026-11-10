from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 9.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9.0)
    ax.axis("off")

    # Title
    ax.text(7.5, 8.45, "Pathway of Sound Through the Ear",
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Coordinates for two rows of four cards
    xs = [2.0, 5.6, 9.2, 12.8]
    y1 = 6.0
    y2 = 2.4

    box_w, box_h = 2.7, 2.1

    def draw_card(cx, cy, title_text):
        rect = patches.FancyBboxPatch(
            (cx - box_w/2, cy - box_h/2), box_w, box_h,
            boxstyle="round,pad=0.08,rounding_size=0.18",
            fc="white", ec=GREY, lw=1.5
        )
        ax.add_patch(rect)
        ax.text(cx, cy - box_h/2 - 0.28, title_text,
                ha="center", va="top", fontsize=11.5, weight="bold", color=INK)

    def draw_arrow(x_start, y_start, x_end, y_end):
        ax.annotate("", xy=(x_end, y_end), xytext=(x_start, y_start),
                    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                    color=DEEP["blue"], lw=2.5))

    # ================= ROW 1 =================

    # 1. Sound waves
    draw_card(xs[0], y1, "sound waves")
    c1_x, c1_y = xs[0], y1 + 0.05
    # Speaker / sound source
    ax.plot([c1_x - 0.85, c1_x - 0.55, c1_x - 0.55, c1_x - 0.85, c1_x - 0.85],
            [c1_y - 0.25, c1_y - 0.45, c1_y + 0.45, c1_y + 0.25, c1_y - 0.25],
            color=DEEP["orange"], lw=2.2)
    # Concentric curved wavefronts
    for r in [0.35, 0.65, 0.95]:
        arc = np.linspace(-np.pi/3, np.pi/3, 30)
        ax.plot((c1_x - 0.45) + r * np.cos(arc),
                c1_y + r * np.sin(arc),
                color=DEEP["blue"], lw=2.5)

    # 2. Pinna
    draw_card(xs[1], y1, "pinna")
    c2_x, c2_y = xs[1], y1 + 0.05
    ear_t = np.linspace(-1.4, 1.4, 100)
    ey = c2_y + ear_t * 0.45
    ex = c2_x + 0.45 * np.cos(ear_t * 1.1) - 0.25 * (ear_t**2) * 0.25
    ax.plot(ex, ey, color=DEEP["pink"], lw=3.2)
    ax.plot([c2_x - 0.05, c2_x + 0.15, c2_x + 0.05],
            [c2_y + 0.35, c2_y + 0.18, c2_y - 0.1],
            color=DEEP["pink"], lw=2.2)
    ax.plot([c2_x - 0.1, c2_x, c2_x - 0.1],
            [c2_y - 0.05, c2_y - 0.2, c2_y - 0.45],
            color=DEEP["pink"], lw=2.2)
    ax.annotate("", xy=(c2_x + 0.2, c2_y), xytext=(c2_x - 0.7, c2_y + 0.2),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.6, ls="--"))

    # 3. Ear canal
    draw_card(xs[2], y1, "ear canal")
    c3_x, c3_y = xs[2], y1 + 0.05
    can_x = np.linspace(c3_x - 0.85, c3_x + 0.85, 60)
    top_y = c3_y + 0.25 + 0.07 * np.sin((can_x - c3_x)*2.8)
    bot_y = c3_y - 0.25 + 0.07 * np.sin((can_x - c3_x)*2.8)
    ax.fill_between(can_x, bot_y, top_y, color=CREAM, alpha=0.7)
    ax.plot(can_x, top_y, color=INK, lw=2)
    ax.plot(can_x, bot_y, color=INK, lw=2)
    sw_x = np.linspace(c3_x - 0.65, c3_x + 0.5, 60)
    sw_y = c3_y + 0.1 * np.sin((sw_x - c3_x) * 13)
    ax.plot(sw_x, sw_y, color=DEEP["blue"], lw=2, linestyle=":")
    ax.annotate("", xy=(c3_x + 0.7, c3_y), xytext=(c3_x + 0.5, c3_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))

    # 4. Eardrum (vibrating)
    draw_card(xs[3], y1, "eardrum")
    c4_x, c4_y = xs[3], y1 + 0.05
    ax.plot([c4_x - 0.8, c4_x - 0.15], [c4_y + 0.38, c4_y + 0.35], color=GREY, lw=2)
    ax.plot([c4_x - 0.8, c4_x + 0.05], [c4_y - 0.38, c4_y - 0.35], color=GREY, lw=2)
    # Tilted tympanic membrane
    ax.plot([c4_x - 0.15, c4_x + 0.05], [c4_y + 0.42, c4_y - 0.42], color=DEEP["pink"], lw=3.5)
    # Vibration dashed lines
    for offset in [-0.09, 0.09]:
        ax.plot([c4_x - 0.15 + offset, c4_x + 0.05 + offset],
                [c4_y + 0.35, c4_y - 0.35], color=DEEP["orange"], lw=1.6, linestyle="--")
    # Vibration arrows and text
    ax.annotate("", xy=(c4_x + 0.3, c4_y + 0.1), xytext=(c4_x - 0.02, c4_y + 0.1),
                arrowprops=dict(arrowstyle="<->", color=DEEP["orange"], lw=1.8))
    ax.text(c4_x + 0.4, c4_y - 0.08, "vibrates", fontsize=10.5, color=DEEP["orange"], ha="left")

    # Connect Row 1
    draw_arrow(xs[0] + box_w/2, y1, xs[1] - box_w/2, y1)
    draw_arrow(xs[1] + box_w/2, y1, xs[2] - box_w/2, y1)
    draw_arrow(xs[2] + box_w/2, y1, xs[3] - box_w/2, y1)

    # Transition arrow from Row 1 end around to Row 2 start (clear path outside cards)
    # Route: exit right of card 4 -> down outside -> back along bottom -> enter left of card 5
    path_x = [xs[3] + box_w/2 + 0.15, 14.5, 14.5, 0.45, 0.45, xs[0] - box_w/2]
    path_y = [y1, y1, 4.0, 4.0, y2, y2]
    # Draw via rounded path / segments
    ax.plot([xs[3] + box_w/2, 14.45], [y1, y1], color=DEEP["blue"], lw=2.4)
    ax.plot([14.45, 14.45], [y1, 4.05], color=DEEP["blue"], lw=2.4)
    ax.plot([14.45, 0.55], [4.05, 4.05], color=DEEP["blue"], lw=2.4)
    ax.plot([0.55, 0.55], [4.05, y2], color=DEEP["blue"], lw=2.4)
    ax.annotate("", xy=(xs[0] - box_w/2, y2), xytext=(0.55, y2),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6",
                                color=DEEP["blue"], lw=2.4))

    # ================= ROW 2 =================

    # 5. Ossicles (malleus, incus, stapes)
    draw_card(xs[0], y2, "ossicles (malleus, incus, stapes)")
    c5_x, c5_y = xs[0], y2 + 0.12
    # Malleus (hammer)
    ax.plot([c5_x - 0.7, c5_x - 0.35], [c5_y - 0.3, c5_y + 0.32], color=DEEP["orange"], lw=3)
    ax.plot([c5_x - 0.35, c5_x - 0.2], [c5_y + 0.32, c5_y + 0.2], color=DEEP["orange"], lw=3)
    # Incus (anvil)
    ax.plot([c5_x - 0.2, c5_x + 0.1, c5_x - 0.02], [c5_y + 0.2, c5_y + 0.25, c5_y - 0.12],
            color=DEEP["blue"], lw=3)
    # Stapes (stirrup)
    ax.plot([c5_x - 0.02, c5_x + 0.35], [c5_y - 0.12, c5_y - 0.06], color=DEEP["green"], lw=2.5)
    ax.plot([c5_x - 0.02, c5_x + 0.35], [c5_y - 0.12, c5_y - 0.26], color=DEEP["green"], lw=2.5)
    ax.plot([c5_x + 0.35, c5_x + 0.35], [c5_y + 0.03, c5_y - 0.35], color=DEEP["green"], lw=3.5)
    # Labels
    ax.text(c5_x - 0.65, c5_y + 0.35, "M", fontsize=10, weight="bold", color=DEEP["orange"])
    ax.text(c5_x - 0.05, c5_y + 0.35, "I", fontsize=10, weight="bold", color=DEEP["blue"])
    ax.text(c5_x + 0.45, c5_y - 0.16, "S", fontsize=10, weight="bold", color=DEEP["green"])

    # 6. Oval window
    draw_card(xs[1], y2, "oval window")
    c6_x, c6_y = xs[1], y2 + 0.12
    # Cochlea wall
    ax.plot([c6_x + 0.1, c6_x + 0.1], [c6_y + 0.45, c6_y + 0.16], color=GREY, lw=4)
    ax.plot([c6_x + 0.1, c6_x + 0.1], [c6_y - 0.16, c6_y - 0.45], color=GREY, lw=4)
    # Oval window membrane
    ax.plot([c6_x + 0.1, c6_x + 0.1], [c6_y + 0.16, c6_y - 0.16], color=DEEP["pink"], lw=3, ls="--")
    # Stapes footplate
    ax.plot([c6_x - 0.38, c6_x + 0.05], [c6_y, c6_y], color=DEEP["green"], lw=3.2)
    ax.plot([c6_x + 0.05, c6_x + 0.05], [c6_y + 0.13, c6_y - 0.13], color=DEEP["green"], lw=4)
    # Pressure ripples
    for r in [0.28, 0.48]:
        arc = np.linspace(-np.pi/3, np.pi/3, 20)
        ax.plot((c6_x + 0.18) + r * np.cos(arc), c6_y + r * np.sin(arc), color=DEEP["blue"], lw=1.8)
    ax.text(c6_x + 0.35, c6_y - 0.38, "fluid waves", fontsize=9.5, color=DEEP["blue"], ha="center")

    # 7. Cochlea fluid and hair cells
    draw_card(xs[2], y2, "cochlea fluid and hair cells")
    c7_x, c7_y = xs[2], y2 + 0.12
    c7_left, c7_right = c7_x - 0.95, c7_x + 0.95
    # Outer uncoiled tube
    ax.plot([c7_left, c7_right], [c7_y + 0.35, c7_y + 0.35], color=INK, lw=1.8)
    ax.plot([c7_left, c7_right], [c7_y - 0.35, c7_y - 0.35], color=INK, lw=1.8)
    ax.plot([c7_right, c7_right], [c7_y - 0.35, c7_y + 0.35], color=INK, lw=1.8)
    # Fluid background
    ax.fill_between([c7_left, c7_right], [c7_y - 0.35, c7_y - 0.35], [c7_y + 0.35, c7_y + 0.35],
                    color=BLUE, alpha=0.15)
    # Basilar membrane
    ax.plot([c7_left, c7_right - 0.15], [c7_y - 0.05, c7_y - 0.05], color=DEEP["blue"], lw=2.4)
    # Hair cells
    for hx in np.linspace(c7_left + 0.2, c7_right - 0.3, 7):
        ax.plot([hx, hx], [c7_y - 0.05, c7_y + 0.12], color=DEEP["green"], lw=2)
        ax.plot([hx, hx + 0.04], [c7_y + 0.12, c7_y + 0.22], color=DEEP["orange"], lw=1.6)
    ax.text(c7_x, c7_y - 0.24, "basilar membrane", fontsize=9, color=DEEP["blue"], ha="center")

    # 8. Auditory nerve leading to auditory area of brain
    draw_card(xs[3], y2, "auditory nerve")
    c8_x, c8_y = xs[3], y2 + 0.12

    # Auditory nerve fibers
    for dy in [-0.08, 0.0, 0.08]:
        ax.plot([c8_x - 1.05, c8_x - 0.3], [c8_y - 0.05 + dy, c8_y - 0.05 + dy*0.5],
                color=DEEP["orange"], lw=2.2)
    ax.text(c8_x - 0.68, c8_y + 0.18, "auditory\nnerve", fontsize=9.5,
            color=DEEP["orange"], weight="bold", ha="center")

    # Brain outline
    bang = np.linspace(0, 2*np.pi, 100)
    bx = (c8_x + 0.45) + 0.5 * np.cos(bang) * (1 + 0.15 * np.cos(2*bang))
    by = (c8_y + 0.02) + 0.42 * np.sin(bang) * (1 - 0.2 * np.sin(bang))
    ax.fill(bx, by, color=CREAM, ec=INK, lw=1.6)

    # Shaded temporal lobe / auditory area
    t_lobe = patches.Ellipse((c8_x + 0.35, c8_y - 0.06), 0.52, 0.3, angle=-10,
                             fc=PINK, ec=DEEP["pink"], lw=1.5)
    ax.add_patch(t_lobe)
    ax.text(c8_x + 0.35, c8_y - 0.06, "auditory\narea of\nbrain", fontsize=8.5,
            color=INK, ha="center", va="center", weight="bold")

    # Connect Row 2
    draw_arrow(xs[0] + box_w/2, y2, xs[1] - box_w/2, y2)
    draw_arrow(xs[1] + box_w/2, y2, xs[2] - box_w/2, y2)
    draw_arrow(xs[2] + box_w/2, y2, xs[3] - box_w/2, y2)

    save(fig, out)
