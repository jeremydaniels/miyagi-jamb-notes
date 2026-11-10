from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Overall Title
    ax.text(6, 7.5, "Test Cross in Guinea Pigs", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)

    # Function to draw a guinea pig icon
    def draw_guinea_pig(cx, cy, is_black, w=0.85, h=0.52):
        fc = "#2B2B2B" if is_black else "#F8F8F6"
        ec = "#1A1A1A" if is_black else GREY
        body = patches.Ellipse((cx, cy), w, h, angle=0, facecolor=fc, edgecolor=ec, lw=1.6, zorder=3)
        ax.add_patch(body)
        
        # Snout
        snout_x = cx + w * 0.38
        snout_y = cy - h * 0.05
        snout = patches.Ellipse((snout_x, snout_y), w * 0.42, h * 0.58, angle=-10, facecolor=fc, edgecolor=ec, lw=1.6, zorder=4)
        ax.add_patch(snout)
        
        # Ear
        ear_x = cx + w * 0.15
        ear_y = cy + h * 0.28
        ear_color = "#3D3D3D" if is_black else PINK
        ear = patches.Ellipse((ear_x, ear_y), w * 0.16, h * 0.28, angle=25, facecolor=ear_color, edgecolor=ec, lw=1.3, zorder=5)
        ax.add_patch(ear)
        
        # Eye
        eye_x = cx + w * 0.35
        eye_y = cy + h * 0.08
        eye_fc = "white" if is_black else "#222222"
        ax.plot(eye_x, eye_y, marker='o', markersize=3.5, color=eye_fc, zorder=6)

    # Separator line between left and right test crosses
    ax.plot([6, 6], [0.6, 6.7], color=GREY, lw=1.2, ls="--")

    panels = [
        {
            "cx": 3.0,
            "title": "Case 1: Parent is Homozygous Dominant",
            "p1_label": "BB?",
            "offspring": [True, True, True, True],
            "conclusion": "all black: parent was BB"
        },
        {
            "cx": 9.0,
            "title": "Case 2: Parent is Heterozygous",
            "p1_label": "Bb?",
            "offspring": [True, False, True, False],
            "conclusion": "1 black : 1 white: parent was Bb"
        }
    ]

    for p in panels:
        xc = p["cx"]
        
        # Subtitle well clear of annotations
        ax.text(xc, 6.7, p["title"], fontsize=13, fontweight="bold", ha="center", va="center", color=INK)

        # Parents
        py = 5.0
        p1_x = xc - 1.45
        p2_x = xc + 1.45

        # P1 (Black guinea pig)
        draw_guinea_pig(p1_x, py, is_black=True)
        ax.text(p1_x, py - 0.48, p["p1_label"], fontsize=12.5, fontweight="bold", ha="center", va="center", color=INK)

        # Cross symbol
        ax.text(xc, py, "×", fontsize=20, ha="center", va="center", color=INK)

        # P2 (White guinea pig)
        draw_guinea_pig(p2_x, py, is_black=False)
        ax.text(p2_x, py - 0.48, "bb", fontsize=12.5, fontweight="bold", ha="center", va="center", color=INK)

        # Connector arrow downwards to distribution
        ax.annotate('', xy=(xc, 3.6), xytext=(xc, py - 0.25),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.6))
        
        # Offspring row
        oy = 2.2
        off_xs = [xc - 1.8, xc - 0.6, xc + 0.6, xc + 1.8]

        # Horizontal distribution line
        ax.plot([xc - 1.8, xc + 1.8], [3.2, 3.2], color=DEEP["blue"], lw=1.5)
        ax.plot([xc, xc], [3.6, 3.2], color=DEEP["blue"], lw=1.5)

        for ox, is_b in zip(off_xs, p["offspring"]):
            ax.plot([ox, ox], [3.2, oy + 0.45], color=DEEP["blue"], lw=1.5)
            draw_guinea_pig(ox, oy, is_black=is_b, w=0.72, h=0.44)
            gen_label = "Bb" if is_b else "bb"
            ax.text(ox, oy - 0.42, gen_label, fontsize=11.5, ha="center", va="center", color=INK)

        # Conclusion Box
        bbox_style = dict(boxstyle="round,pad=0.45", fc=CREAM, ec=DEEP["orange"], lw=1.5)
        ax.text(xc, 0.9, p["conclusion"], fontsize=12, fontweight="bold", ha="center", va="center", color=INK, bbox=bbox_style)

    # Annotated labels positioned cleanly above parents without overlapping titles
    # "unknown black parent" pointing to left black parent
    ax.annotate("unknown black parent",
                xy=(3.0 - 1.45, 5.0 + 0.35), xytext=(3.0 - 1.45, 5.95),
                ha="center", va="bottom", fontsize=11, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # "homozygous recessive white parent (bb)" pointing to right white parent
    ax.annotate("homozygous recessive\nwhite parent (bb)",
                xy=(9.0 + 1.45, 5.0 + 0.35), xytext=(9.0 + 1.45, 5.9),
                ha="center", va="bottom", fontsize=11, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
