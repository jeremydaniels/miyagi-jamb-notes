from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Helper function to draw a stylized person icon
    def draw_person(x, y, badge_letter, badge_bg, badge_deep_col, scale=1.0):
        # Head
        head = patches.Circle((x, y + 0.7 * scale), 0.32 * scale, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=3)
        ax.add_patch(head)
        # Body (torso)
        body = patches.FancyBboxPatch((x - 0.4 * scale, y - 0.45 * scale), 0.8 * scale, 0.9 * scale, 
                                     boxstyle="round,pad=0.15,rounding_size=0.25",
                                     facecolor=LAV, edgecolor=INK, lw=1.5, zorder=2)
        ax.add_patch(body)
        # Badge on chest
        badge = patches.Circle((x, y), 0.28 * scale, facecolor=badge_bg, edgecolor=badge_deep_col, lw=2, zorder=4)
        ax.add_patch(badge)
        ax.text(x, y - 0.02 * scale, badge_letter, ha='center', va='center', fontsize=14 * scale, 
                fontweight='bold', color=INK, zorder=5)

    # Positions - spread mother and child vertically and position labels cleanly
    x_mother = 2.0
    y_mother = 5.3

    x_child = 2.0
    y_child = 1.9

    x_man1 = 6.8
    y_man1 = 5.3

    x_man2 = 6.8
    y_man2 = 2.7

    # Draw connecting line between Mother and Child (behind boxes and figures)
    ax.plot([x_mother, x_child], [y_mother - 0.5, y_child + 0.6], color=INK, lw=2, linestyle='--', zorder=1)

    # Draw figures
    # Mother: group A (blue badge)
    draw_person(x_mother, y_mother, "A", BLUE, DEEP["blue"])
    # Child: group B (green badge, slightly smaller)
    draw_person(x_child, y_child, "B", GREEN, DEEP["green"], scale=0.9)
    # Man 1: group O (grey badge)
    draw_person(x_man1, y_man1, "O", GREY, INK)
    # Man 2: group B (green badge)
    draw_person(x_man2, y_man2, "B", GREEN, DEEP["green"])

    # Red cross beside Man 1
    cx, cy = x_man1 + 0.9, y_man1
    ax.plot([cx - 0.25, cx + 0.25], [cy - 0.25, cy + 0.25], color=DEEP["pink"], lw=4.5, solid_capstyle='round', zorder=5)
    ax.plot([cx - 0.25, cx + 0.25], [cy + 0.25, cy - 0.25], color=DEEP["pink"], lw=4.5, solid_capstyle='round', zorder=5)

    # Orange question mark beside Man 2
    qx, qy = x_man2 + 0.9, y_man2 - 0.05
    ax.text(qx, qy, "?", ha='center', va='center', fontsize=32, fontweight='bold', 
            color=DEEP["orange"], zorder=5)

    # Main titles / Labels above figures
    # Mother label (above figure)
    ax.text(x_mother, y_mother + 1.25, "Mother (group A)", ha='center', va='bottom',
            fontsize=13, fontweight='bold', color=INK)
    # Child label (above child, placed neatly between mother's alleles and child)
    ax.text(x_child, y_child + 0.85, "Child (group B)", ha='center', va='bottom',
            fontsize=13, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Allele tags (small tags under each person)
    # Mother
    ax.text(x_mother, y_mother - 0.75, r"$I^A i$", ha='center', va='top', fontsize=12.5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1), color=INK, zorder=4)
    # Child
    ax.text(x_child, y_child - 0.7, r"$I^B i$", ha='center', va='top', fontsize=12.5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1), color=INK, zorder=4)
    # Man 1
    ax.text(x_man1, y_man1 - 0.8, r"$i\ i$", ha='center', va='top', fontsize=12.5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1), color=INK, zorder=4)
    # Man 2
    ax.text(x_man2, y_man2 - 0.8, r"$I^B I^B$ or $I^B i$", ha='center', va='top', fontsize=12.5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1), color=INK, zorder=4)

    # Descriptive text beside Man 1 and Man 2
    # Man 1 label
    ax.text(x_man1 + 1.45, y_man1, "Man 1 (group O): excluded, has no $I^B$ allele",
            ha='left', va='center', fontsize=12.5, color=INK)
    # Man 2 label
    ax.text(x_man2 + 1.45, y_man2, "Man 2 (group B): could be the father, not proved",
            ha='left', va='center', fontsize=12.5, color=INK)

    # Deduction annotation: "Child's I^B must come from the father"
    ax.annotate("Child's $I^B$ must come from the father",
                xy=(x_child + 0.5, y_child - 0.7),
                xytext=(x_child + 1.8, 0.65),
                fontsize=12,
                fontweight='bold',
                color=DEEP["green"],
                ha='left', va='center',
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2, shrinkB=4),
                bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["green"], lw=1.5))

    save(fig, out)
