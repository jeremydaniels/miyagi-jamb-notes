from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(15, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Overall title
    ax.text(7.5, 6.1, "Classic Coleoptile Phototropism Experiments", 
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Color definitions
    POT_COLOR = "#C87D55"
    SOIL_COLOR = "#5D4037"
    COLEO_COLOR = GREEN
    COLEO_EDGE = DEEP["green"]
    AGAR_COLOR = "#FFF59D"
    AGAR_EDGE = "#FBC02D"
    BLACK_CAP = "#212121"
    MICA_COLOR = "#78909C"
    YELLOW_LIGHT = "#FBC02D"
    DARK_PANEL = "#ECEFF1"

    # 7 Experiment center X positions
    xs = np.linspace(1.2, 13.8, 7)
    pot_top_y = 1.6
    pot_w_top = 1.2
    pot_w_bot = 0.9
    pot_h = 0.7

    # Draw dark panel for experiment 7 first (in background)
    p7_x = xs[6]
    dark_rect = patches.FancyBboxPatch((p7_x - 0.95, 1.4), 1.9, 4.3,
                                      boxstyle="round,pad=0.1",
                                      fc=DARK_PANEL, ec=GREY, lw=1.2, zorder=1)
    ax.add_patch(dark_rect)
    ax.text(p7_x, 5.5, "darkness", ha="center", va="center", fontsize=11,
            color=INK, style="italic", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8), zorder=4)

    # Helper to draw a pot
    def draw_pot(xc):
        # Soil / pot trapezoid
        pot_poly = patches.Polygon([
            [xc - pot_w_top/2, pot_top_y],
            [xc + pot_w_top/2, pot_top_y],
            [xc + pot_w_bot/2, pot_top_y - pot_h],
            [xc - pot_w_bot/2, pot_top_y - pot_h]
        ], closed=True, fc=POT_COLOR, ec=INK, lw=1.5, zorder=3)
        ax.add_patch(pot_poly)
        # Rim ellipse / soil top
        soil_ellipse = patches.Ellipse((xc, pot_top_y), pot_w_top, 0.16,
                                      fc=SOIL_COLOR, ec=INK, lw=1.2, zorder=4)
        ax.add_patch(soil_ellipse)

    # Helper to draw straight coleoptile (decapitated or full)
    def draw_straight_coleo(xc, height=2.4, decapitated=False, zorder=2):
        w = 0.34
        if decapitated:
            rect = patches.Rectangle((xc - w/2, pot_top_y), w, height,
                                     fc=COLEO_COLOR, ec=COLEO_EDGE, lw=1.5, zorder=zorder)
            ax.add_patch(rect)
            # flat cut top line
            ax.plot([xc - w/2, xc + w/2], [pot_top_y + height, pot_top_y + height],
                    color=COLEO_EDGE, lw=1.5, zorder=zorder+1)
        else:
            # Rounded top
            path_data = [
                (Path.MOVETO, [xc - w/2, pot_top_y]),
                (Path.LINETO, [xc - w/2, pot_top_y + height - 0.2]),
                (Path.CURVE4, [xc - w/2, pot_top_y + height + 0.3]),
                (Path.CURVE4, [xc + w/2, pot_top_y + height + 0.3]),
                (Path.LINETO, [xc + w/2, pot_top_y + height - 0.2]),
                (Path.LINETO, [xc + w/2, pot_top_y]),
                (Path.CLOSEPOLY, [xc - w/2, pot_top_y])
            ]
            codes, verts = zip(*path_data)
            path = Path(verts, codes)
            patch = patches.PathPatch(path, fc=COLEO_COLOR, ec=COLEO_EDGE, lw=1.5, zorder=zorder)
            ax.add_patch(patch)

    # Helper to draw curved (bending right) coleoptile
    def draw_bending_coleo(xc, has_gap=False, zorder=2):
        # We can construct a smooth bending tube towards the right
        # Bottom at (xc, pot_top_y)
        w = 0.34
        # Points along center line: (0, 0) to curved right
        t = np.linspace(0, 1, 30)
        # Bending curve
        bend_x = 0.65 * (t**2.2)
        bend_y = 2.4 * t
        
        # Left boundary
        left_x = xc - w/2 + bend_x - 0.15 * (t**2)
        left_y = pot_top_y + bend_y
        
        # Right boundary
        right_x = xc + w/2 + bend_x + 0.15 * (t**2)
        right_y = pot_top_y + bend_y

        tip_x = xc + bend_x[-1] + 0.05
        tip_y = pot_top_y + bend_y[-1] + 0.15

        verts = []
        verts.append((left_x[0], left_y[0]))
        for lx, ly in zip(left_x, left_y):
            verts.append((lx, ly))
        # Rounded tip
        verts.append((tip_x, tip_y + 0.12))
        for rx, ry in zip(reversed(right_x), reversed(right_y)):
            verts.append((rx, ry))
        verts.append((verts[0][0], verts[0][1]))

        poly = patches.Polygon(verts, closed=True, fc=COLEO_COLOR, ec=COLEO_EDGE, lw=1.5, zorder=zorder)
        ax.add_patch(poly)
        return left_x, left_y, right_x, right_y

    # Draw pots for all 7
    for xc in xs:
        draw_pot(xc)

    # Draw Yellow Light Arrows from right for Exps 1-6
    for xc in xs[:6]:
        for ay in [3.0, 3.6, 4.2]:
            ax.annotate("", xy=(xc + 0.35, ay), xytext=(xc + 0.85, ay),
                        arrowprops=dict(arrowstyle="->", color=YELLOW_LIGHT, lw=2.2, mutation_scale=12),
                        zorder=5)

    # Label "light" above exp 1
    ax.text(xs[0] + 0.62, 4.5, "light", color="#E65100", fontsize=11, weight="bold", ha="center")

    # ---------------- EXPERIMENT 1: Intact, bending ----------------
    draw_bending_coleo(xs[0])
    ax.annotate("intact", xy=(xs[0], pot_top_y + 1.6), xytext=(xs[0] - 0.65, pot_top_y + 2.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 2: Tip removed, straight & short ----------------
    draw_straight_coleo(xs[1], height=1.6, decapitated=True)
    ax.annotate("tip removed", xy=(xs[1], pot_top_y + 1.6), xytext=(xs[1] - 0.45, pot_top_y + 2.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 3: Opaque cap, straight ----------------
    draw_straight_coleo(xs[2], height=2.4, decapitated=False)
    # Black cap on tip
    cap_w = 0.42
    cap_h = 0.65
    cap = patches.FancyBboxPatch((xs[2] - cap_w/2, pot_top_y + 2.4 - 0.35), cap_w, cap_h,
                                 boxstyle="round,pad=0.04", fc=BLACK_CAP, ec=BLACK_CAP, lw=1, zorder=4)
    ax.add_patch(cap)
    ax.annotate("opaque cap", xy=(xs[2], pot_top_y + 2.4 + 0.2), xytext=(xs[2] - 0.55, pot_top_y + 3.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 4: Opaque sleeve below tip, bending ----------------
    draw_bending_coleo(xs[3])
    # Sleeve on stem below tip: between t = 0.25 and 0.6
    # Draw curved polygon covering the stem segment
    sleeve_poly = patches.Polygon([
        [xs[3] - 0.22 + 0.05, pot_top_y + 0.7],
        [xs[3] + 0.24 + 0.05, pot_top_y + 0.7],
        [xs[3] + 0.34 + 0.2, pot_top_y + 1.6],
        [xs[3] - 0.18 + 0.2, pot_top_y + 1.6]
    ], closed=True, fc=BLACK_CAP, ec=BLACK_CAP, lw=1, zorder=4)
    ax.add_patch(sleeve_poly)
    ax.annotate("opaque sleeve", xy=(xs[3] + 0.1, pot_top_y + 1.15), xytext=(xs[3] - 0.6, pot_top_y + 2.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 5: Tip replaced on agar block, bending ----------------
    draw_bending_coleo(xs[4])
    # Draw thin agar block slice across the bent stem near top (approx y = pot_top_y + 1.9)
    agar_poly = patches.Polygon([
        [xs[4] - 0.15 + 0.32, pot_top_y + 1.8],
        [xs[4] + 0.26 + 0.32, pot_top_y + 1.86],
        [xs[4] + 0.29 + 0.37, pot_top_y + 2.02],
        [xs[4] - 0.12 + 0.37, pot_top_y + 1.96]
    ], closed=True, fc=AGAR_COLOR, ec=AGAR_EDGE, lw=1.2, zorder=4)
    ax.add_patch(agar_poly)
    # Cut lines to show block separation
    ax.plot([xs[4] - 0.15 + 0.32, xs[4] + 0.26 + 0.32], [pot_top_y + 1.8, pot_top_y + 1.86], color=INK, lw=1, zorder=5)
    ax.plot([xs[4] - 0.12 + 0.37, xs[4] + 0.29 + 0.37], [pot_top_y + 1.96, pot_top_y + 2.02], color=INK, lw=1, zorder=5)
    ax.annotate("agar block", xy=(xs[4] + 0.2, pot_top_y + 1.9), xytext=(xs[4] - 0.55, pot_top_y + 2.7),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 6: Mica sheet vertically on shaded side, straight ----------------
    draw_straight_coleo(xs[5], height=2.4, decapitated=False)
    # Mica sheet: vertical thin grey plate inserted vertically into shaded left side just below tip
    mica_x = xs[5] - 0.17  # on left edge
    mica_y = pot_top_y + 1.6
    mica_rect = patches.Rectangle((mica_x - 0.03, mica_y), 0.14, 0.45,
                                  fc=MICA_COLOR, ec=INK, lw=1.2, zorder=4)
    ax.add_patch(mica_rect)
    ax.annotate("mica sheet", xy=(mica_x + 0.04, mica_y + 0.22), xytext=(xs[5] - 0.55, pot_top_y + 2.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=11, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6))

    # ---------------- EXPERIMENT 7: Decapitated, agar on left side, bends right (in darkness) ----------------
    # Stem bending to right
    draw_bending_coleo(xs[6])
    # Decapitated tip top: mask off tip or draw block on left side of the cut
    # Draw small agar block on left half of cut stem
    # Cut level at t ~ 0.75: x ~ xs[6] + 0.3, y ~ pot_top_y + 1.7
    agar_b7 = patches.Rectangle((xs[6] + 0.14, pot_top_y + 1.75), 0.18, 0.22,
                                angle=18, fc=AGAR_COLOR, ec=AGAR_EDGE, lw=1.2, zorder=5)
    ax.add_patch(agar_b7)
    # Mask top tip to represent decapitated stem
    cover_tip = patches.Rectangle((xs[6] + 0.2, pot_top_y + 2.05), 0.8, 0.8,
                                  fc=DARK_PANEL, ec=DARK_PANEL, zorder=3)
    ax.add_patch(cover_tip)
    # Outline of cut top
    ax.plot([xs[6] + 0.12, xs[6] + 0.44], [pot_top_y + 1.74, pot_top_y + 1.85], color=COLEO_EDGE, lw=1.5, zorder=4)

    ax.annotate("agar block\ncontaining auxin", xy=(xs[6] + 0.22, pot_top_y + 1.9),
                xytext=(xs[6] - 0.45, pot_top_y + 2.7),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1),
                fontsize=10.5, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.6), zorder=6)

    # ---------------- Numbers and Captions below each pot ----------------
    captions = [
        "Intact tip:\nbends to light",
        "Tip removed:\nno growth / bend",
        "Opaque cap:\nno bending",
        "Opaque sleeve:\nbends to light",
        "Tip on agar block:\nbends to light",
        "Vertical mica (left):\nblocks bend / straight",
        "Auxin agar block\non left side: bends"
    ]

    for i, (xc, cap_text) in enumerate(zip(xs, captions)):
        # Number badge
        ax.text(xc, 0.75, f"Experiment {i+1}", ha="center", va="center",
                fontsize=11.5, weight="bold", color=INK)
        # Caption
        ax.text(xc, 0.32, cap_text, ha="center", va="center",
                fontsize=10.5, color=INK)

    save(fig, out)
