from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 13)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13)
    ax.axis('off')

    # Title
    ax.text(5, 12.4, "Biblical Chain of Civil Authority (Romans 13)",
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # ----------------- LEVEL 1: GOD -----------------
    # Container box
    god_box = patches.FancyBboxPatch((1.5, 9.6), 7.0, 2.3, boxstyle="round,pad=0.3",
                                    facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(god_box)

    # Glowing Symbol: radiating sun/light rays + golden disk
    cx, cy = 3.0, 10.75
    # Rays
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        rx0 = cx + 0.5 * np.cos(angle)
        ry0 = cy + 0.5 * np.sin(angle)
        rx1 = cx + 0.8 * np.cos(angle)
        ry1 = cy + 0.8 * np.sin(angle)
        ax.plot([rx0, rx1], [ry0, ry1], color=ORANGE, lw=2.5, solid_capstyle='round')

    # Central glowing circle with cross motif / shining center
    sun = patches.Circle((cx, cy), 0.42, facecolor="#FFE57F", edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(sun)
    ax.text(cx, cy, "✝", ha="center", va="center", fontsize=20, color=DEEP["orange"], weight="bold")

    # Labels for God
    ax.text(4.2, 11.0, "God (Source of all power)", fontsize=16, weight="bold", color=INK, va="center")
    ax.text(4.2, 10.45, "Supreme Lawgiver & Ruler\n\"There is no authority except from God\"", 
            fontsize=14, color=INK, va="center")

    # ----------------- ARROW 1 -----------------
    ax.annotate("", xy=(5, 8.8), xytext=(5, 9.6),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=10, headlength=10))
    ax.text(5, 9.2, "God ordains governing authorities.", ha="center", va="center",
            fontsize=14, weight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["blue"], lw=1.2))

    # ----------------- LEVEL 2: GOVERNMENT -----------------
    gov_box = patches.FancyBboxPatch((0.8, 5.0), 8.4, 3.6, boxstyle="round,pad=0.3",
                                     facecolor="#EEF4F8", edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(gov_box)

    # Government Building sketch (left of box)
    # Pediment / Roof
    roof = patches.Polygon([[1.3, 7.5], [2.7, 7.5], [2.0, 8.2]], closed=True,
                           facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(roof)
    # Base and pediment strip
    ax.add_patch(patches.Rectangle((1.3, 7.35), 1.4, 0.15, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5))
    # Columns
    for col_x in [1.4, 1.8, 2.2, 2.5]:
        ax.add_patch(patches.Rectangle((col_x, 6.3), 0.12, 1.05, facecolor="white", edgecolor=DEEP["blue"], lw=1.2))
    # Steps
    ax.add_patch(patches.Rectangle((1.2, 6.15), 1.6, 0.15, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5))

    # Judge holding gavel sketch
    # Judge body/robe
    ax.add_patch(patches.Polygon([[3.4, 6.15], [4.2, 6.15], [4.0, 7.1], [3.6, 7.1]], closed=True,
                                 facecolor="#37474F", edgecolor=INK, lw=1.5))
    # Head
    ax.add_patch(patches.Circle((3.8, 7.35), 0.22, facecolor=CREAM, edgecolor=INK, lw=1.5))
    # Arm holding gavel
    ax.plot([3.9, 4.3, 4.2], [6.9, 7.1, 7.4], color=INK, lw=2.5)
    # Gavel head & handle
    ax.plot([4.0, 4.5], [7.2, 7.6], color=DEEP["orange"], lw=3)
    ax.plot([4.1, 4.4], [7.7, 7.4], color=INK, lw=5)

    # Texts for Government
    ax.text(4.8, 7.8, "Government (Minister of God for good /\nbears the sword to punish evil)", fontsize=14, weight="bold", color=INK, va="center")
    ax.text(4.8, 6.7, "• Promotes justice and public order\n• Restrains evil & protects the innocent",
            fontsize=14, color=INK, va="center")

    # ----------------- ARROW 2 -----------------
    ax.annotate("", xy=(5, 4.0), xytext=(5, 5.0),
                arrowprops=dict(facecolor=DEEP["green"], edgecolor=DEEP["green"], width=3, headwidth=10, headlength=10))
    ax.text(5, 4.5, "Subjection & Honor", ha="center", va="center",
            fontsize=14, weight="bold", color=DEEP["green"],
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["green"], lw=1.2))

    # ----------------- LEVEL 3: CITIZENS -----------------
    cit_box = patches.FancyBboxPatch((0.8, 0.5), 8.4, 3.3, boxstyle="round,pad=0.3",
                                     facecolor="#EBF5ED", edgecolor=DEEP["green"], lw=2.5)
    ax.add_patch(cit_box)

    # Visuals: Traffic Light (obeying law) & Tax Form/Coin (paying taxes)
    # Traffic light pole and housing
    ax.plot([1.6, 1.6], [1.0, 3.2], color=INK, lw=3)
    ax.add_patch(patches.Rectangle((1.35, 1.9), 0.5, 1.3, facecolor="#37474F", edgecolor=INK, lw=1.5))
    # Lights (Red, Yellow, Green active)
    ax.add_patch(patches.Circle((1.6, 2.9), 0.12, facecolor="#B0BEC5", edgecolor=INK, lw=1))
    ax.add_patch(patches.Circle((1.6, 2.55), 0.12, facecolor="#B0BEC5", edgecolor=INK, lw=1))
    ax.add_patch(patches.Circle((1.6, 2.2), 0.13, facecolor="#00E676", edgecolor=DEEP["green"], lw=1.5))
    ax.text(1.6, 0.85, "Traffic light", ha="center", fontsize=14, color=INK)

    # Citizens sketch
    # Person 1
    ax.add_patch(patches.Circle((2.7, 2.6), 0.2, facecolor=CREAM, edgecolor=INK, lw=1.5))
    ax.plot([2.7, 2.7], [1.6, 2.4], color=INK, lw=2)
    ax.plot([2.7, 2.4], [1.1, 1.6], color=INK, lw=2)
    ax.plot([2.7, 3.0], [1.1, 1.6], color=INK, lw=2)
    ax.plot([2.4, 2.7, 3.0], [2.0, 2.2, 2.0], color=INK, lw=2)

    # Tax Document / Paying taxes sketch
    ax.add_patch(patches.Rectangle((3.4, 1.6), 0.7, 0.9, facecolor="white", edgecolor=INK, lw=1.5))
    ax.text(3.75, 2.25, "TAX", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["orange"])
    ax.plot([3.5, 4.0], [1.9, 1.9], color=GREY, lw=1.5)
    ax.plot([3.5, 3.9], [1.75, 1.75], color=GREY, lw=1.5)
    # Coin next to tax document
    ax.add_patch(patches.Circle((4.25, 1.55), 0.18, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5))
    ax.text(4.25, 1.55, "$", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["orange"])
    ax.text(3.8, 0.85, "Paying taxes", ha="center", fontsize=14, color=INK)

    # Texts for Citizens
    ax.text(4.8, 3.0, "Citizens (Submit for conscience sake)", fontsize=16, weight="bold", color=INK, va="center")
    ax.text(4.8, 1.9, "• Obey laws and civil ordinances\n• Pay taxes, revenue, respect, and honor\n• Do what is good and live peacefully",
            fontsize=14, color=INK, va="center")

    save(fig, out)
