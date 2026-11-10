from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)

    # Title
    ax.text(6, 6.3, "Common Folder Operations", ha='center', va='center',
            fontsize=18, weight='bold', color=INK)

    # Helper function to draw a standard closed folder
    def draw_folder(cx, cy, w=1.2, h=0.85):
        # Back tab and body
        tab_w = w * 0.45
        tab_h = h * 0.22
        # Tab
        tab = patches.Polygon([
            [cx - w/2, cy + h/2],
            [cx - w/2 + tab_w, cy + h/2],
            [cx - w/2 + tab_w + 0.1, cy + h/2 - tab_h],
            [cx - w/2, cy + h/2 - tab_h]
        ], closed=True, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=2)
        ax.add_patch(tab)
        # Folder back
        back = patches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h - tab_h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=2
        )
        ax.add_patch(back)
        # Folder front pocket
        front = patches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h * 0.72,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=ORANGE, edgecolor=INK, lw=1.8, zorder=3
        )
        ax.add_patch(front)

    # Helper function to draw an open folder
    def draw_open_folder(cx, cy, w=1.2, h=0.85):
        tab_w = w * 0.45
        tab_h = h * 0.22
        # Tab
        tab = patches.Polygon([
            [cx - w/2, cy + h/2],
            [cx - w/2 + tab_w, cy + h/2],
            [cx - w/2 + tab_w + 0.1, cy + h/2 - tab_h],
            [cx - w/2, cy + h/2 - tab_h]
        ], closed=True, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=2)
        ax.add_patch(tab)
        # Back
        back = patches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h - tab_h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=2
        )
        ax.add_patch(back)
        # Interior paper
        paper = patches.Rectangle(
            (cx - w*0.35, cy - h*0.2), w*0.7, h*0.65,
            facecolor="white", edgecolor=INK, lw=1.5, zorder=3
        )
        ax.add_patch(paper)
        # Front flap (slanted open)
        flap = patches.Polygon([
            [cx - w*0.55, cy - h*0.5],
            [cx + w*0.45, cy - h*0.5],
            [cx + w*0.55, cy - h*0.05],
            [cx - w*0.45, cy - h*0.05]
        ], closed=True, facecolor=ORANGE, edgecolor=INK, lw=1.8, zorder=4)
        ax.add_patch(flap)

    # Centers for 5 columns
    cols = [1.5, 3.75, 6.0, 8.25, 10.5]
    y_card = 3.5

    cards = [
        {"action": "Create", "col": cols[0], "color": GREEN, "symbol": "plus"},
        {"action": "Open",   "col": cols[1], "color": BLUE,  "symbol": "open"},
        {"action": "View",   "col": cols[2], "color": LAV,   "symbol": "eye"},
        {"action": "Copy",   "col": cols[3], "color": CREAM, "symbol": "copy"},
        {"action": "Delete", "col": cols[4], "color": PINK,  "symbol": "trash"},
    ]

    for item in cards:
        cx = item["col"]
        # Background container card
        box = patches.FancyBboxPatch(
            (cx - 0.95, y_card - 2.1), 1.9, 4.2,
            boxstyle="round,pad=0.05,rounding_size=0.15",
            facecolor="white", edgecolor=GREY, lw=1.5, zorder=1
        )
        ax.add_patch(box)

        # Folder placement
        fy = y_card + 0.9
        if item["symbol"] == "open":
            draw_open_folder(cx, fy)
        else:
            draw_folder(cx, fy)

        # Action symbol badge
        bx = cx
        by = y_card - 0.45
        badge_r = 0.42
        badge = patches.Circle((bx, by), badge_r, facecolor=item["color"], edgecolor=INK, lw=1.8, zorder=5)
        ax.add_patch(badge)

        sym = item["symbol"]
        if sym == "plus":
            # Plus sign
            ax.plot([bx - 0.22, bx + 0.22], [by, by], color=DEEP["green"], lw=3.5, solid_capstyle='round', zorder=6)
            ax.plot([bx, bx], [by - 0.22, by + 0.22], color=DEEP["green"], lw=3.5, solid_capstyle='round', zorder=6)
        elif sym == "open":
            # Small open folder for the badge
            w, h = 0.4, 0.28
            back = patches.Rectangle((bx - w/2, by - h/2 + 0.05), w, h, facecolor="white", edgecolor=DEEP["blue"], lw=1.8, zorder=6)
            ax.add_patch(back)
            tab = patches.Rectangle((bx - w/2, by + h/2 + 0.05), w*0.4, 0.08, facecolor="white", edgecolor=DEEP["blue"], lw=1.8, zorder=5)
            ax.add_patch(tab)
            flap = patches.Polygon([
                [bx - w*0.6, by - h*0.6 + 0.05],
                [bx + w*0.4, by - h*0.6 + 0.05],
                [bx + w*0.6, by + h*0.2 + 0.05],
                [bx - w*0.4, by + h*0.2 + 0.05]
            ], closed=True, facecolor="white", edgecolor=DEEP["blue"], lw=1.8, zorder=7)
            ax.add_patch(flap)
        elif sym == "eye":
            # Eye symbol (horizontal)
            t = np.linspace(0, np.pi, 50)
            x_eye = 0.28 * np.cos(t)
            y_eye = 0.15 * np.sin(t)
            ex = np.concatenate([x_eye, x_eye[::-1]])
            ey = np.concatenate([y_eye, -y_eye[::-1]])
            ax.plot(bx + ex, by + ey, color=DEEP["lav"], lw=2.2, zorder=6)
            pupil = patches.Circle((bx, by), 0.08, facecolor=DEEP["lav"], edgecolor=DEEP["lav"], zorder=7)
            ax.add_patch(pupil)
        elif sym == "copy":
            # Two overlapping pages
            p_w, p_h = 0.22, 0.28
            # Back page
            p1 = patches.Rectangle((bx - 0.18, by - 0.08), p_w, p_h,
                                   facecolor="white", edgecolor=INK, lw=1.6, zorder=6)
            # Front page
            p2 = patches.Rectangle((bx - 0.06, by - 0.2), p_w, p_h,
                                   facecolor=CREAM, edgecolor=INK, lw=1.6, zorder=7)
            ax.add_patch(p1)
            ax.add_patch(p2)
        elif sym == "trash":
            # Trash can symbol
            tw_top, tw_bot = 0.26, 0.2
            th = 0.28
            # Can body
            body = patches.Polygon([
                [bx - tw_top/2, by + 0.02],
                [bx + tw_top/2, by + 0.02],
                [bx + tw_bot/2, by - th],
                [bx - tw_bot/2, by - th]
            ], closed=True, facecolor="white", edgecolor=DEEP["pink"], lw=1.8, zorder=6)
            ax.add_patch(body)
            # Lid
            ax.plot([bx - 0.18, bx + 0.18], [by + 0.04, by + 0.04], color=DEEP["pink"], lw=2.2, zorder=7)
            # Lid handle
            ax.plot([bx - 0.06, bx - 0.06, bx + 0.06, bx + 0.06],
                    [by + 0.04, by + 0.10, by + 0.10, by + 0.04], color=DEEP["pink"], lw=1.8, zorder=7)
            # Vertical ribs
            ax.plot([bx - 0.05, bx - 0.04], [by - 0.03, by - 0.22], color=DEEP["pink"], lw=1.4, zorder=7)
            ax.plot([bx + 0.05, bx + 0.04], [by - 0.03, by - 0.22], color=DEEP["pink"], lw=1.4, zorder=7)

        # Label text
        ax.text(cx, y_card - 1.45, item["action"], ha='center', va='center',
                fontsize=16, weight='bold', color=INK)

    save(fig, out)
