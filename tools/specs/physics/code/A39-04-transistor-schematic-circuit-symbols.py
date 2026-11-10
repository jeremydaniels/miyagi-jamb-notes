from style import *
import numpy as np

def draw_transistor(ax, cx, cy, is_npn=True, title="npn transistor", mnemonic=""):
    # Circle enclosing the transistor symbol
    circle_r = 1.35
    circle = plt.Circle((cx, cy), circle_r, fill=False, edgecolor=INK, lw=2.5)
    ax.add_patch(circle)

    # Base vertical line
    bar_x = cx - 0.35
    bar_y_top = cy + 0.75
    bar_y_bot = cy - 0.75
    ax.plot([bar_x, bar_x], [bar_y_bot, bar_y_top], color=INK, lw=4, solid_capstyle='round')

    # Base lead
    ax.plot([cx - 2.0, bar_x], [cy, cy], color=INK, lw=2.5)
    ax.text(cx - 2.2, cy, "B", fontsize=18, fontweight='bold', ha='right', va='center', color=INK)

    # Collector lead: starts at bar, angles up-right to circle top, then goes up
    c_start = (bar_x, cy + 0.4)
    c_bend = (cx + 0.45, cy + 0.95)
    c_end = (cx + 0.45, cy + 2.0)
    ax.plot([c_start[0], c_bend[0]], [c_start[1], c_bend[1]], color=INK, lw=2.5)
    ax.plot([c_bend[0], c_end[0]], [c_bend[1], c_end[1]], color=INK, lw=2.5)
    ax.text(c_end[0], c_end[1] + 0.25, "C", fontsize=18, fontweight='bold', ha='center', va='bottom', color=INK)

    # Emitter lead: starts at bar, angles down-right to circle bot, then goes down
    e_start = (bar_x, cy - 0.4)
    e_bend = (cx + 0.45, cy - 0.95)
    e_end = (cx + 0.45, cy - 2.0)
    ax.plot([e_start[0], e_bend[0]], [e_start[1], e_bend[1]], color=INK, lw=2.5)
    ax.plot([e_bend[0], e_end[0]], [e_bend[1], e_end[1]], color=INK, lw=2.5)
    ax.text(e_end[0], e_end[1] - 0.25, "E", fontsize=18, fontweight='bold', ha='center', va='top', color=INK)

    # Arrow on the emitter branch
    if is_npn:
        # Arrow pointing outwards (down-right along emitter slant)
        ax.annotate("", 
                    xy=(bar_x + 0.65 * (e_bend[0] - bar_x), cy - 0.4 + 0.65 * (e_bend[1] - (cy - 0.4))),
                    xytext=(bar_x + 0.25 * (e_bend[0] - bar_x), cy - 0.4 + 0.25 * (e_bend[1] - (cy - 0.4))),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.5, mutation_scale=22))
    else:
        # Arrow pointing inwards (up-left along emitter slant towards base)
        ax.annotate("", 
                    xy=(bar_x + 0.25 * (e_bend[0] - bar_x), cy - 0.4 + 0.25 * (e_bend[1] - (cy - 0.4))),
                    xytext=(bar_x + 0.65 * (e_bend[0] - bar_x), cy - 0.4 + 0.65 * (e_bend[1] - (cy - 0.4))),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=2.5, mutation_scale=22))

    # Titles and labels
    ax.text(cx, cy + 2.7, title, fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(cx, cy - 2.8, mnemonic, fontsize=14, fontstyle='italic', ha='center', va='top', 
            color=INK, bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"))

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Main Title
    ax.text(6.0, 6.4, "Bipolar Junction Transistor (BJT) Symbols", 
            fontsize=20, fontweight='bold', ha='center', va='center', color=INK)

    # Draw npn transistor (Left)
    draw_transistor(ax, cx=3.2, cy=3.4, is_npn=True, 
                    title="NPN Transistor", 
                    mnemonic="Arrow points outwards\n(\"Not Pointing iN\")")

    # Draw pnp transistor (Right)
    draw_transistor(ax, cx=8.8, cy=3.4, is_npn=False, 
                    title="PNP Transistor", 
                    mnemonic="Arrow points inwards\n(\"Pointing iN Proudly\")")

    save(fig, out)
