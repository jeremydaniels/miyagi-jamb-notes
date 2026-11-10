from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title
    ax.text(7, 7.3, "The Four Rightly Guided Caliphs (Al-Khulafa' ar-Rashidun)", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Timeline main arrow
    timeline_y = 4.4
    ax.annotate("", xy=(13.2, timeline_y), xytext=(0.8, timeline_y),
                arrowprops=dict(arrowstyle="-|>", lw=3, color=INK, mutation_scale=20))

    caliphs = [
        {
            "name": "Abu Bakr",
            "dates": "632–634 CE\n11–13 AH",
            "achievement": "Riddah wars",
            "detail": "Preserved unity\nof the state",
            "x": 2.2,
            "color": DEEP["orange"],
            "fill": ORANGE,
            "icon": "sword_shield"
        },
        {
            "name": "'Umar",
            "dates": "634–644 CE\n13–23 AH",
            "achievement": "Diwan &\nAdministration",
            "detail": "Organized governance\n& calendar",
            "x": 5.4,
            "color": DEEP["blue"],
            "fill": BLUE,
            "icon": "scroll"
        },
        {
            "name": "'Uthman",
            "dates": "644–656 CE\n23–35 AH",
            "achievement": "Standardized\nMushaf",
            "detail": "Compilation of\nthe Qur'an",
            "x": 8.6,
            "color": DEEP["green"],
            "fill": GREEN,
            "icon": "book"
        },
        {
            "name": "'Ali",
            "dates": "656–661 CE\n35–40 AH",
            "achievement": "Justice &\nPreservation",
            "detail": "Exemplary rule\nof law",
            "x": 11.8,
            "color": DEEP["lav"],
            "fill": LAV,
            "icon": "scale"
        }
    ]

    for c in caliphs:
        cx = c["x"]
        
        # Timeline node
        node_circle = plt.Circle((cx, timeline_y), 0.15, facecolor="white", edgecolor=c["color"], lw=3, zorder=5)
        ax.add_patch(node_circle)
        
        # Top Card (Name & Dates)
        ax.plot([cx, cx], [timeline_y + 0.15, timeline_y + 0.7], color=c["color"], lw=2)
        
        card_w, card_h = 2.6, 1.4
        card_rect = patches.FancyBboxPatch((cx - card_w/2, timeline_y + 0.7), card_w, card_h,
                                           boxstyle="round,pad=0.1,rounding_size=0.15",
                                           linewidth=2, edgecolor=c["color"], facecolor=c["fill"], alpha=0.35, zorder=3)
        ax.add_patch(card_rect)
        
        # White text-backing for clarity
        ax.text(cx, timeline_y + 1.65, c["name"], ha="center", va="center", fontsize=16, fontweight="bold", color=INK, zorder=4)
        ax.text(cx, timeline_y + 1.1, c["dates"], ha="center", va="center", fontsize=14, color=INK, zorder=4)

        # Bottom section: Connector and Icon Box
        ax.plot([cx, cx], [timeline_y - 0.15, timeline_y - 0.7], color=c["color"], lw=2)

        icon_box_w, icon_box_h = 3.0, 3.0
        icon_rect = patches.FancyBboxPatch((cx - icon_box_w/2, timeline_y - 0.7 - icon_box_h), icon_box_w, icon_box_h,
                                           boxstyle="round,pad=0.1,rounding_size=0.15",
                                           linewidth=1.5, edgecolor=GREY, facecolor="white", zorder=2)
        ax.add_patch(icon_rect)

        # Drawing Icons
        icon_cy = 2.6
        if c["icon"] == "sword_shield":
            # Shield
            shield_verts = [(cx - 0.35, icon_cy + 0.35), (cx + 0.35, icon_cy + 0.35),
                            (cx + 0.35, icon_cy), (cx, icon_cy - 0.45),
                            (cx - 0.35, icon_cy)]
            shield = patches.Polygon(shield_verts, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2, zorder=4)
            ax.add_patch(shield)
            # Crossing Sword
            ax.plot([cx - 0.55, cx + 0.55], [icon_cy - 0.35, icon_cy + 0.45], color=INK, lw=2.5, zorder=3)
            ax.plot([cx - 0.45, cx - 0.25], [icon_cy - 0.15, icon_cy - 0.4], color=INK, lw=2.5, zorder=3)
            # Shield boss
            ax.scatter([cx], [icon_cy], s=40, color=DEEP["orange"], zorder=5)

        elif c["icon"] == "scroll":
            # Ancient Scroll / Register
            rect = patches.Rectangle((cx - 0.4, icon_cy - 0.35), 0.8, 0.75, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=4)
            ax.add_patch(rect)
            # Top roll
            top_roll = patches.Ellipse((cx, icon_cy + 0.4), 0.9, 0.2, facecolor="white", edgecolor=DEEP["blue"], lw=2, zorder=5)
            ax.add_patch(top_roll)
            # Bottom roll
            bot_roll = patches.Ellipse((cx, icon_cy - 0.35), 0.9, 0.2, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=5)
            ax.add_patch(bot_roll)
            # Text lines on scroll
            ax.plot([cx - 0.25, cx + 0.25], [icon_cy + 0.15, icon_cy + 0.15], color=DEEP["blue"], lw=1.8, zorder=6)
            ax.plot([cx - 0.25, cx + 0.25], [icon_cy - 0.05, icon_cy - 0.05], color=DEEP["blue"], lw=1.8, zorder=6)

        elif c["icon"] == "book":
            # Open Book (Standardized Mushaf)
            left_page = patches.Polygon([(cx, icon_cy - 0.3), (cx - 0.55, icon_cy - 0.2),
                                         (cx - 0.55, icon_cy + 0.35), (cx, icon_cy + 0.25)],
                                        closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=4)
            right_page = patches.Polygon([(cx, icon_cy - 0.3), (cx + 0.55, icon_cy - 0.2),
                                          (cx + 0.55, icon_cy + 0.35), (cx, icon_cy + 0.25)],
                                         closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=4)
            ax.add_patch(left_page)
            ax.add_patch(right_page)
            # Spine
            ax.plot([cx, cx], [icon_cy - 0.35, icon_cy + 0.25], color=DEEP["green"], lw=2.5, zorder=5)
            # Book stand (Rehal sketch)
            ax.plot([cx - 0.45, cx + 0.45], [icon_cy - 0.5, icon_cy - 0.25], color=INK, lw=2, zorder=3)
            ax.plot([cx + 0.45, cx - 0.45], [icon_cy - 0.5, icon_cy - 0.25], color=INK, lw=2, zorder=3)

        elif c["icon"] == "scale":
            # Scale of Justice
            ax.plot([cx, cx], [icon_cy - 0.45, icon_cy + 0.45], color=INK, lw=2.5, zorder=4)
            # Base
            ax.plot([cx - 0.3, cx + 0.3], [icon_cy - 0.45, icon_cy - 0.45], color=INK, lw=2.5, zorder=4)
            # Beam
            ax.plot([cx - 0.5, cx + 0.5], [icon_cy + 0.35, icon_cy + 0.35], color=INK, lw=2, zorder=4)
            # Left pan
            ax.plot([cx - 0.5, cx - 0.65], [icon_cy + 0.35, icon_cy + 0.05], color=DEEP["lav"], lw=1.2, zorder=4)
            ax.plot([cx - 0.5, cx - 0.35], [icon_cy + 0.35, icon_cy + 0.05], color=DEEP["lav"], lw=1.2, zorder=4)
            left_pan = patches.Arc((cx - 0.5, icon_cy + 0.05), 0.35, 0.2, angle=0, theta1=180, theta2=360, color=DEEP["lav"], lw=2, zorder=4)
            ax.add_patch(left_pan)
            # Right pan
            ax.plot([cx + 0.5, cx + 0.35], [icon_cy + 0.35, icon_cy + 0.05], color=DEEP["lav"], lw=1.2, zorder=4)
            ax.plot([cx + 0.5, cx + 0.65], [icon_cy + 0.35, icon_cy + 0.05], color=DEEP["lav"], lw=1.2, zorder=4)
            right_pan = patches.Arc((cx + 0.5, icon_cy + 0.05), 0.35, 0.2, angle=0, theta1=180, theta2=360, color=DEEP["lav"], lw=2, zorder=4)
            ax.add_patch(right_pan)

        # Achievement Labels
        ax.text(cx, 1.55, c["achievement"], ha="center", va="center", fontsize=14, fontweight="bold", color=INK, zorder=4)
        ax.text(cx, 1.05, c["detail"], ha="center", va="center", fontsize=14, color=GREY, zorder=4)

    save(fig, out)
