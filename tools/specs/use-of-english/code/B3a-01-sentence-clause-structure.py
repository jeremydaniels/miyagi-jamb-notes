from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 6.9, "Clause Structure of a Complex Sentence", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Main sentence container box
    sentence_box = patches.FancyBboxPatch(
        (0.6, 5.0), 10.8, 1.2,
        boxstyle="round,pad=0.1,rounding_size=0.2",
        ec=GREY, fc=CREAM, lw=1.5
    )
    ax.add_patch(sentence_box)

    # Words of sentence with specific approximate horizontal positions
    # Sentence: "When the rain stopped, the children who were waiting ran outside."
    # Total span: x ~ 0.9 to 11.1
    ax.text(2.1, 5.6, "When the rain stopped,", fontsize=16, weight="bold", color=DEEP["orange"], ha="center", va="center")
    ax.text(4.45, 5.6, "the children", fontsize=16, weight="bold", color=DEEP["blue"], ha="center", va="center")
    ax.text(6.85, 5.6, "who were waiting", fontsize=16, weight="bold", color=DEEP["green"], ha="center", va="center")
    ax.text(9.5, 5.6, "ran outside.", fontsize=16, weight="bold", color=DEEP["blue"], ha="center", va="center")

    def draw_bracket(x1, x2, y_top, depth, color, label, sublabel=None):
        # Draw a downward square bracket
        mid_x = (x1 + x2) / 2
        y_bot = y_top - depth
        ax.plot([x1, x1, x2, x2], [y_top, y_bot, y_bot, y_top], color=color, lw=2.5)
        
        # Label below bracket
        text = label if not sublabel else f"{label}\n({sublabel})"
        ax.text(mid_x, y_bot - 0.25, text, ha="center", va="top", fontsize=14, weight="bold", color=color,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # 1. Orange bracket under "When the rain stopped"
    # Span x: 0.9 to 3.3
    draw_bracket(0.9, 3.3, 4.8, 0.4, DEEP["orange"], "Adverbial clause (time)")

    # 2. Green bracket under "who were waiting"
    # Span x: 5.7 to 8.0
    draw_bracket(5.7, 8.0, 4.8, 0.4, DEEP["green"], "Adjective clause")

    # Arrow from Adjective clause pointing to "the children"
    # Starting from top of adjective clause area up to word "the children"
    ax.annotate("describes 'children'",
                xy=(4.8, 5.25), xytext=(6.5, 3.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0,
                                connectionstyle="arc3,rad=-0.25"),
                fontsize=14, weight="bold", color=DEEP["green"], ha="left", va="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["green"], lw=1.2))

    # 3. Blue bracket under Main clause: encompasses "the children ... ran outside"
    # Span: Two segments linked, or overarching main clause bracket under whole clause
    # Span x: 3.7 to 11.1 at lower depth
    x_mc1, x_mc2 = 3.6, 5.3
    x_mc3, x_mc4 = 8.3, 11.1
    y_mc = 2.4
    depth_mc = 0.4

    # Split bracket showing disconnected parts of the main clause
    ax.plot([x_mc1, x_mc1, x_mc2, x_mc2], [y_mc + depth_mc, y_mc, y_mc, y_mc + depth_mc], color=DEEP["blue"], lw=2.5)
    ax.plot([x_mc3, x_mc3, x_mc4, x_mc4], [y_mc + depth_mc, y_mc, y_mc, y_mc + depth_mc], color=DEEP["blue"], lw=2.5)
    # Dashed line bridging across the embedded relative clause
    ax.plot([x_mc2, x_mc3], [y_mc, y_mc], color=DEEP["blue"], lw=2, linestyle="--")

    # Connector lines from sentence down to the main clause bracket
    ax.plot([4.45, 4.45], [4.8, y_mc + depth_mc], color=DEEP["blue"], lw=1.5, linestyle=":")
    ax.plot([9.5, 9.5], [4.8, y_mc + depth_mc], color=DEEP["blue"], lw=1.5, linestyle=":")

    ax.text((x_mc1 + x_mc4) / 2, y_mc - 0.25, "Main clause\n(\"the children ... ran outside\")",
            ha="center", va="top", fontsize=15, weight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.2))

    save(fig, out)
