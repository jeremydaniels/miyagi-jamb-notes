from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # Dividing line between the two systems
    ax.plot([7, 7], [0.8, 7.8], color=GREY, lw=1.5, ls="--")

    # Titles
    ax.text(3.5, 7.7, "Presidential System", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)
    ax.text(10.5, 7.7, "Parliamentary System", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # Subtitles / Key concept labels
    ax.text(3.5, 7.15, "Separate Elections", ha="center", va="center",
            fontsize=15, fontstyle="italic", color=DEEP["blue"])
    ax.text(10.5, 7.15, "Fusion of Powers", ha="center", va="center",
            fontsize=15, fontstyle="italic", color=DEEP["orange"])

    # ---------------- LEFT SIDE: Presidential System ----------------
    # "The People" Box
    people_pres = patches.FancyBboxPatch(
        (1.8, 5.7), 3.4, 0.9,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        fc=CREAM, ec=DEEP["orange"], lw=2
    )
    ax.add_patch(people_pres)
    ax.text(3.5, 6.15, "The People", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # "Elected President (Executive)" Box
    pres_exec = patches.FancyBboxPatch(
        (0.5, 2.7), 2.7, 1.4,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        fc=BLUE, ec=DEEP["blue"], lw=2
    )
    ax.add_patch(pres_exec)
    ax.text(1.85, 3.4, "Elected President\n(Executive)", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    # "Elected Legislature" Box
    pres_leg = patches.FancyBboxPatch(
        (3.8, 2.7), 2.7, 1.4,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        fc=GREEN, ec=DEEP["green"], lw=2
    )
    ax.add_patch(pres_leg)
    ax.text(5.15, 3.4, "Elected\nLegislature", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    # Arrows from People to Executive and Legislature
    arrow_props_down = dict(arrowstyle="->", lw=2, color=INK)
    ax.annotate("", xy=(1.85, 4.2), xytext=(2.7, 5.7),
                arrowprops=arrow_props_down)
    ax.annotate("", xy=(5.15, 4.2), xytext=(4.3, 5.7),
                arrowprops=arrow_props_down)

    # "Votes for" small indicators
    ax.text(2.0, 5.0, "votes for", ha="center", va="center", fontsize=14,
            color=INK, bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))
    ax.text(5.0, 5.0, "votes for", ha="center", va="center", fontsize=14,
            color=INK, bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # Bidirectional arrow between Executive and Legislature: "Checks and Balances"
    ax.annotate("", xy=(3.15, 3.4), xytext=(3.85, 3.4),
                arrowprops=dict(arrowstyle="<->", lw=2, color=DEEP["pink"]))
    ax.text(3.5, 2.0, "Checks and\nBalances", ha="center", va="center",
            fontsize=14, fontweight="bold", color=DEEP["pink"],
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["pink"], lw=1.5))
    ax.annotate("", xy=(3.5, 3.35), xytext=(3.5, 2.5),
                arrowprops=dict(arrowstyle="-", lw=1.5, color=DEEP["pink"], ls=":"))

    # ---------------- RIGHT SIDE: Parliamentary System ----------------
    # "The People" Box
    people_parl = patches.FancyBboxPatch(
        (8.8, 5.7), 3.4, 0.9,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        fc=CREAM, ec=DEEP["orange"], lw=2
    )
    ax.add_patch(people_parl)
    ax.text(10.5, 6.15, "The People", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # Arrow from People to Legislature
    ax.annotate("", xy=(10.5, 4.6), xytext=(10.5, 5.7),
                arrowprops=arrow_props_down)
    ax.text(10.5, 5.15, "votes for", ha="center", va="center", fontsize=14,
            color=INK, bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

    # Large Outer Box: "Elected Legislature"
    parl_leg = patches.FancyBboxPatch(
        (8.0, 1.4), 5.0, 3.1,
        boxstyle="round,pad=0.1,rounding_size=0.2",
        fc=GREEN, ec=DEEP["green"], lw=2
    )
    ax.add_patch(parl_leg)
    ax.text(10.5, 4.15, "Elected Legislature", ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # Inner Box inside Legislature: "Prime Minister & Cabinet (Executive)"
    parl_exec = patches.FancyBboxPatch(
        (8.4, 1.7), 4.2, 1.3,
        boxstyle="round,pad=0.1,rounding_size=0.15",
        fc=LAV, ec=DEEP["lav"], lw=2
    )
    ax.add_patch(parl_exec)
    ax.text(10.5, 2.35, "Prime Minister & Cabinet\n(Executive)", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    # Arrow inside Legislature pointing to Cabinet
    ax.annotate("", xy=(10.5, 3.05), xytext=(10.5, 3.8),
                arrowprops=dict(arrowstyle="->", lw=2, color=DEEP["lav"]))
    ax.text(10.5, 3.4, "drawn from / formed by", ha="center", va="center", fontsize=14,
            color=INK, bbox=dict(boxstyle="square,pad=0.15", fc=GREEN, ec="none"))

    save(fig, out)
