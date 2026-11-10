from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(16, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 15.5)
    ax.set_ylim(-1.5, 8.5)
    ax.axis("off")

    # Title
    ax.text(7.5, 7.8, "Internal Resistance to Apartheid", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    # Main horizontal timeline spine
    y_line = 3.5
    ax.plot([0.5, 14.5], [y_line, y_line], color=GREY, lw=4, zorder=1)
    ax.scatter([0.5, 14.5], [y_line, y_line], color=GREY, s=50, zorder=2)

    # Events data
    # 8 milestones
    events = [
        {"year": "1912", "title": "ANC Formed", "type": "anc"},
        {"year": "1952", "title": "Defiance\nCampaign", "type": "defiance"},
        {"year": "1955", "title": "Freedom\nCharter", "type": "charter"},
        {"year": "1960", "title": "Sharpeville\nMassacre", "type": "passbook"},
        {"year": "1961", "title": "MK Armed\nStruggle begins", "type": "mk"},
        {"year": "1964", "title": "Mandela sentenced\nto life", "type": "prison"},
        {"year": "1976", "title": "Soweto\nUprising", "type": "fist"},
        {"year": "1983", "title": "UDF Formed", "type": "udf"}
    ]

    xs = np.linspace(1.2, 13.8, len(events))

    # Helper functions to draw mini-icons
    def draw_icon(icon_type, cx, cy):
        # Background disk
        circ = patches.Circle((cx, cy), 0.55, facecolor="white", edgecolor=GREY, lw=1.5, zorder=4)
        ax.add_patch(circ)
        
        if icon_type == "anc":
            # Three stripes representing ANC historic colours / shield badge
            ax.add_patch(patches.Rectangle((cx - 0.28, cy + 0.1), 0.56, 0.16, facecolor=DEEP["green"], edgecolor="none", zorder=5))
            ax.add_patch(patches.Rectangle((cx - 0.28, cy - 0.08), 0.56, 0.16, facecolor=ORANGE, edgecolor="none", zorder=5))
            ax.add_patch(patches.Rectangle((cx - 0.28, cy - 0.26), 0.56, 0.16, facecolor=INK, edgecolor="none", zorder=5))
            ax.add_patch(patches.Rectangle((cx - 0.28, cy - 0.26), 0.56, 0.52, fill=False, edgecolor=INK, lw=1.2, zorder=6))

        elif icon_type == "defiance":
            # Two hands breaking chains / crossing bars
            ax.plot([cx - 0.22, cx + 0.22], [cy - 0.18, cy + 0.18], color=DEEP["blue"], lw=3, zorder=5)
            ax.plot([cx - 0.22, cx + 0.22], [cy + 0.18, cy - 0.18], color=DEEP["blue"], lw=3, zorder=5)
            ax.plot([cx - 0.28, cx + 0.28], [cy, cy], color=DEEP["orange"], lw=2.5, ls="--", zorder=6)

        elif icon_type == "charter":
            # Parchment / scroll sheet
            rect = patches.Rectangle((cx - 0.22, cy - 0.3), 0.44, 0.6, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=5)
            ax.add_patch(rect)
            # Lines of writing on charter
            for ly in [0.15, 0.03, -0.09, -0.21]:
                ax.plot([cx - 0.14, cx + 0.14], [cy + ly, cy + ly], color=INK, lw=1.2, zorder=6)

        elif icon_type == "passbook":
            # Passbook on fire
            # Book
            rect = patches.Rectangle((cx - 0.24, cy - 0.25), 0.48, 0.35, facecolor=LAV, edgecolor=INK, lw=1.4, zorder=5)
            ax.add_patch(rect)
            ax.plot([cx, cx], [cy - 0.25, cy + 0.1], color=INK, lw=1, zorder=5)
            # Flame above / burning pass
            flame = patches.Polygon([[cx, cy + 0.35], [cx + 0.18, cy + 0.05], [cx + 0.08, cy - 0.02], 
                                     [cx, cy + 0.12], [cx - 0.08, cy - 0.02], [cx - 0.18, cy + 0.05]],
                                    closed=True, facecolor=DEEP["orange"], edgecolor=DEEP["pink"], lw=1.2, zorder=6)
            ax.add_patch(flame)

        elif icon_type == "mk":
            # Spear (Umkhonto) and shield silhouette
            ax.plot([cx - 0.25, cx + 0.25], [cy - 0.25, cy + 0.25], color=INK, lw=2.5, zorder=5)
            # Spearhead
            spear = patches.Polygon([[cx + 0.22, cy + 0.3], [cx + 0.28, cy + 0.22], [cx + 0.18, cy + 0.2]],
                                    closed=True, facecolor=DEEP["pink"], edgecolor=INK, lw=1, zorder=6)
            ax.add_patch(spear)
            # Small shield
            shield = patches.Ellipse((cx - 0.02, cy - 0.02), 0.26, 0.42, angle=-45, facecolor=BLUE, edgecolor=INK, lw=1.2, zorder=6)
            ax.add_patch(shield)

        elif icon_type == "prison":
            # Prison bars
            rect = patches.Rectangle((cx - 0.25, cy - 0.28), 0.5, 0.56, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=5)
            ax.add_patch(rect)
            for bx in np.linspace(cx - 0.16, cx + 0.16, 4):
                ax.plot([bx, bx], [cy - 0.28, cy + 0.28], color=INK, lw=1.8, zorder=6)

        elif icon_type == "fist":
            # Raised fist (Soweto youth)
            fist_box = patches.Rectangle((cx - 0.16, cy - 0.18), 0.32, 0.28, facecolor=DEEP["orange"], edgecolor=INK, lw=1.5, zorder=5)
            ax.add_patch(fist_box)
            # Arm
            arm = patches.Rectangle((cx - 0.1, cy - 0.35), 0.2, 0.2, facecolor=DEEP["orange"], edgecolor=INK, lw=1.5, zorder=5)
            ax.add_patch(arm)
            # Knuckles lines
            for kx in np.linspace(cx - 0.1, cx + 0.1, 3):
                ax.plot([kx, kx], [cy - 0.06, cy + 0.08], color=INK, lw=1.2, zorder=6)

        elif icon_type == "udf":
            # Multiple united figures / hands together (UDF banner motif)
            for dx, col in zip([-0.14, 0.0, 0.14], [DEEP["blue"], DEEP["pink"], DEEP["green"]]):
                head = patches.Circle((cx + dx, cy + 0.12), 0.09, facecolor=col, edgecolor=INK, lw=1.1, zorder=6)
                ax.add_patch(head)
                body = patches.Polygon([[cx + dx - 0.1, cy - 0.25], [cx + dx + 0.1, cy - 0.25], 
                                        [cx + dx + 0.08, cy], [cx + dx - 0.08, cy]],
                                       closed=True, facecolor=col, edgecolor=INK, lw=1.1, zorder=5)
                ax.add_patch(body)

    # Plot milestones alternating above and below the timeline
    for i, ev in enumerate(events):
        x = xs[i]
        is_above = (i % 2 == 0)
        
        # Timeline node point
        node_color = DEEP["blue"] if is_above else DEEP["orange"]
        ax.scatter([x], [y_line], color=node_color, s=120, zorder=5, edgecolors=INK, linewidths=1.5)

        if is_above:
            stem_y = y_line + 1.2
            icon_y = y_line + 2.0
            text_y = y_line + 3.0
            year_y = y_line + 0.4
            
            # Stem line
            ax.plot([x, x], [y_line, stem_y + 0.2], color=GREY, lw=2, zorder=2)
            # Year badge
            ax.text(x, year_y, ev["year"], ha="center", va="bottom", fontsize=15, 
                    fontweight="bold", color=node_color, bbox=dict(fc="white", ec="none", pad=1))
            # Icon
            draw_icon(ev["type"], x, icon_y)
            # Event label
            ax.text(x, text_y, ev["title"], ha="center", va="center", fontsize=14, 
                    fontweight="bold", color=INK, bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=0.8))
        else:
            stem_y = y_line - 1.2
            icon_y = y_line - 2.0
            text_y = y_line - 3.2
            year_y = y_line - 0.4
            
            # Stem line
            ax.plot([x, x], [y_line, stem_y - 0.2], color=GREY, lw=2, zorder=2)
            # Year badge
            ax.text(x, year_y, ev["year"], ha="center", va="top", fontsize=15, 
                    fontweight="bold", color=node_color, bbox=dict(fc="white", ec="none", pad=1))
            # Icon
            draw_icon(ev["type"], x, icon_y)
            # Event label
            ax.text(x, text_y, ev["title"], ha="center", va="center", fontsize=14, 
                    fontweight="bold", color=INK, bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=0.8))

    save(fig, out)
    plt.close(fig)
