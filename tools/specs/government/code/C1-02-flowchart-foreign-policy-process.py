from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(7, 9.5, "The Foreign Policy Process", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Style helper for boxes
    def draw_box(x, y, w, h, text, fc, ec, fontsize=14, bold=False):
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.2,rounding_size=0.15",
            facecolor=fc, edgecolor=ec, linewidth=2, zorder=3
        )
        ax.add_patch(rect)
        weight = "bold" if bold else "normal"
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize, fontweight=weight, color=INK, zorder=4, multialignment="center")

    # 1. Top box: The Executive (President)
    exec_x, exec_y = 7.0, 8.0
    draw_box(exec_x, exec_y, 4.6, 1.0, "The Executive (President)", BLUE, DEEP["blue"], fontsize=15, bold=True)

    # 2. Side box: The Legislature
    leg_x, leg_y = 1.9, 8.0
    draw_box(leg_x, leg_y, 2.6, 1.0, "The Legislature", LAV, DEEP["lav"], fontsize=14, bold=True)

    # Dashed arrow from Legislature to Executive
    ax.annotate(
        "", xy=(exec_x - 2.3, exec_y), xytext=(leg_x + 1.3, leg_y),
        arrowprops=dict(arrowstyle="->", linestyle="--", color=DEEP["lav"], lw=2.2, mutation_scale=18),
        zorder=2
    )
    # Label for dashed line
    ax.text(
        (leg_x + 1.3 + exec_x - 2.3) / 2, exec_y + 0.35,
        "Ratifies treaties and\napproves budget",
        ha="center", va="center", fontsize=14, color=INK,
        bbox=dict(fc="white", ec="none", pad=2), zorder=5
    )

    # Arrow from Executive down to Ministry of Foreign Affairs
    mfa_x, mfa_y = 7.0, 5.8
    ax.annotate(
        "", xy=(mfa_x, mfa_y + 0.5), xytext=(exec_x, exec_y - 0.5),
        arrowprops=dict(arrowstyle="->", color=INK, lw=2.8, mutation_scale=22),
        zorder=2
    )

    # 3. Middle box: Ministry of Foreign Affairs
    draw_box(mfa_x, mfa_y, 5.2, 1.0, "Ministry of Foreign Affairs", CREAM, DEEP["orange"], fontsize=15, bold=True)

    # Large arrow pointing down to Implementation Tools
    tools_y = 3.9
    ax.annotate(
        "", xy=(7.0, tools_y + 0.4), xytext=(mfa_x, mfa_y - 0.5),
        arrowprops=dict(arrowstyle="->", color=INK, lw=3.2, mutation_scale=24),
        zorder=2
    )

    # 4. Section Title: Implementation Tools
    ax.text(
        7.0, tools_y, "Implementation Tools",
        ha="center", va="center", fontsize=16, fontweight="bold", color=INK,
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4", lw=1.5), zorder=4
    )

    # Connector line branching out to the four tools
    branch_y = 2.8
    ax.plot([7.0, 7.0], [tools_y - 0.35, branch_y], color=DEEP["green"], lw=2, zorder=2)

    boxes_info = [
        (1.9, "Diplomacy\n(Embassies &\nHigh Commissions)"),
        (5.3, "Economic\nInstruments\n(Aid & Sanctions)"),
        (8.7, "Military\nAction"),
        (12.1, "Cultural\nExchange")
    ]

    ax.plot([1.9, 12.1], [branch_y, branch_y], color=DEEP["green"], lw=2, zorder=2)

    # 5. Four smaller boxes in a row
    for bx, text in boxes_info:
        ax.annotate(
            "", xy=(bx, 2.0 + 0.7), xytext=(bx, branch_y),
            arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2, mutation_scale=16),
            zorder=2
        )
        draw_box(bx, 1.7, 3.1, 1.4, text, GREEN, DEEP["green"], fontsize=14, bold=False)

    save(fig, out)
