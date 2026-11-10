from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 14)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14)
    ax.axis('off')

    # Main Title
    ax.text(6, 13.4, "Word Stress: Noun vs Verb", ha="center", va="center",
            fontsize=20, weight="bold", color=INK)

    # Column Headers
    # Left Header: Noun (Soft Blue)
    rect_left = patches.FancyBboxPatch((0.8, 12.3), 5.0, 0.7, boxstyle="round,pad=0.1",
                                       fc=BLUE, ec=DEEP["blue"], lw=2)
    ax.add_patch(rect_left)
    ax.text(3.3, 12.65, "NOUN: stress first", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # Right Header: Verb (Soft Orange)
    rect_right = patches.FancyBboxPatch((6.2, 12.3), 5.0, 0.7, boxstyle="round,pad=0.1",
                                        fc=ORANGE, ec=DEEP["orange"], lw=2)
    ax.add_patch(rect_right)
    ax.text(8.7, 12.65, "VERB: stress second", ha="center", va="center",
            fontsize=16, weight="bold", color=INK)

    # Divider line
    ax.plot([6, 6], [0.8, 12.1], color=GREY, lw=1.5, ls="--")

    # Row y-centers
    rows_y = [10.6, 7.8, 5.0, 2.2]

    # Helper: draw beat circles
    def draw_beats(cx, cy, pattern="first"):
        # pattern: "first" (large, small) or "second" (small, large)
        spacing = 0.35
        r_large = 0.12
        r_small = 0.06
        if pattern == "first":
            c1 = patches.Circle((cx - spacing/2, cy), r_large, fc=DEEP["blue"], ec=INK, lw=1)
            c2 = patches.Circle((cx + spacing/2, cy), r_small, fc=GREY, ec=INK, lw=1)
        else:
            c1 = patches.Circle((cx - spacing/2, cy), r_small, fc=GREY, ec=INK, lw=1)
            c2 = patches.Circle((cx + spacing/2, cy), r_large, fc=DEEP["orange"], ec=INK, lw=1)
        ax.add_patch(c1)
        ax.add_patch(c2)

    # Helper: draw word and beats
    def draw_word_entry(x, y, word, pattern):
        ax.text(x, y, word, ha="center", va="center", fontsize=17, weight="bold", color=INK)
        draw_beats(x, y + 0.45, pattern=pattern)

    # --- ROW 1: REcord vs reCORD ---
    y1 = rows_y[0]
    # Row dividing border lines
    for y_sep in [9.2, 6.4, 3.6]:
        ax.plot([0.8, 11.2], [y_sep, y_sep], color=CREAM, lw=2)

    # Icon 1L: Vinyl disc
    disc_c = (2.0, y1)
    ax.add_patch(patches.Circle(disc_c, 0.65, fc="#222222", ec=INK, lw=1.5))
    ax.add_patch(patches.Circle(disc_c, 0.5, fc="none", ec="#555555", lw=1))
    ax.add_patch(patches.Circle(disc_c, 0.38, fc="none", ec="#555555", lw=1))
    ax.add_patch(patches.Circle(disc_c, 0.22, fc=PINK, ec=INK, lw=1))
    ax.add_patch(patches.Circle(disc_c, 0.05, fc="white", ec=INK, lw=1))

    draw_word_entry(4.2, y1, "REcord", "first")

    # Icon 1R: Microphone
    mic_x, mic_y = 7.4, y1
    # capsule
    ax.add_patch(patches.FancyBboxPatch((mic_x - 0.15, mic_y), 0.3, 0.55,
                                        boxstyle="round,pad=0.08", fc=GREY, ec=INK, lw=1.5))
    # U-mount
    arc_theta = np.linspace(np.pi, 2*np.pi, 30)
    ax.plot(mic_x + 0.3*np.cos(arc_theta), mic_y + 0.15 + 0.35*np.sin(arc_theta),
            color=INK, lw=2)
    # stem & base
    ax.plot([mic_x, mic_x], [mic_y - 0.2, mic_y - 0.5], color=INK, lw=2)
    ax.plot([mic_x - 0.3, mic_x + 0.3], [mic_y - 0.5, mic_y - 0.5], color=INK, lw=2.5)

    draw_word_entry(9.6, y1, "reCORD", "second")

    # --- ROW 2: PREsent vs preSENT ---
    y2 = rows_y[1]
    # Icon 2L: Wrapped gift box
    gx, gy = 2.0, y2 - 0.1
    # Box body
    ax.add_patch(patches.Rectangle((gx - 0.45, gy - 0.4), 0.9, 0.75, fc=PINK, ec=INK, lw=1.5))
    # Box lid
    ax.add_patch(patches.Rectangle((gx - 0.52, gy + 0.35), 1.04, 0.18, fc=PINK, ec=INK, lw=1.5))
    # Ribbons
    ax.plot([gx, gx], [gy - 0.4, gy + 0.53], color=DEEP["blue"], lw=3)
    ax.plot([gx - 0.45, gx + 0.45], [gy - 0.02, gy - 0.02], color=DEEP["blue"], lw=3)
    # Bow
    ax.add_patch(patches.Circle((gx - 0.15, gy + 0.62), 0.12, fc="none", ec=DEEP["blue"], lw=2))
    ax.add_patch(patches.Circle((gx + 0.15, gy + 0.62), 0.12, fc="none", ec=DEEP["blue"], lw=2))

    draw_word_entry(4.2, y2, "PREsent", "first")

    # Icon 2R: Handing over a certificate
    px, py = 7.4, y2
    # Person 1 (left, giver)
    ax.add_patch(patches.Circle((px - 0.45, py + 0.35), 0.12, fc=CREAM, ec=INK, lw=1.5))
    ax.plot([px - 0.45, px - 0.45], [py + 0.23, py - 0.3], color=INK, lw=2)
    # Arm handing over
    ax.plot([px - 0.45, px - 0.15], [py + 0.05, py + 0.0], color=INK, lw=2)
    # Person 2 (right, receiver)
    ax.add_patch(patches.Circle((px + 0.45, py + 0.35), 0.12, fc=CREAM, ec=INK, lw=1.5))
    ax.plot([px + 0.45, px + 0.45], [py + 0.23, py - 0.3], color=INK, lw=2)
    # Arm reaching
    ax.plot([px + 0.45, px + 0.15], [py + 0.05, py + 0.0], color=INK, lw=2)
    # Certificate / scroll
    cert = patches.Rectangle((px - 0.18, py - 0.1), 0.36, 0.25, angle=10,
                             fc="white", ec=DEEP["orange"], lw=1.5)
    ax.add_patch(cert)
    ax.plot([px - 0.1, px + 0.1], [py + 0.02, py + 0.05], color=GREY, lw=1)

    draw_word_entry(9.6, y2, "preSENT", "second")

    # --- ROW 3: PROtest vs proTEST ---
    y3 = rows_y[2]
    # Icon 3L: Group holding placards
    gx3, gy3 = 2.0, y3
    # Heads of group
    for hx, hy in [(-0.35, -0.1), (0.0, 0.0), (0.35, -0.1)]:
        ax.add_patch(patches.Circle((gx3 + hx, gy3 + hy), 0.12, fc=CREAM, ec=INK, lw=1.3))
        ax.plot([gx3 + hx, gx3 + hx], [gy3 + hy - 0.12, gy3 - 0.5], color=INK, lw=1.8)
    # Placard sticks & boards
    # Left placard
    ax.plot([gx3 - 0.35, gx3 - 0.35], [gy3 - 0.1, gy3 + 0.4], color=INK, lw=1.5)
    ax.add_patch(patches.Rectangle((gx3 - 0.6, gy3 + 0.25), 0.5, 0.3, fc="white", ec=INK, lw=1.5))
    # Right placard
    ax.plot([gx3 + 0.2, gx3 + 0.2], [gy3, gy3 + 0.55], color=INK, lw=1.5)
    ax.add_patch(patches.Rectangle((gx3 - 0.05, gy3 + 0.4), 0.5, 0.3, fc="white", ec=INK, lw=1.5))

    draw_word_entry(4.2, y3, "PROtest", "first")

    # Icon 3R: Person raising a hand to object
    rx3, ry3 = 7.4, y3
    # Head & torso
    ax.add_patch(patches.Circle((rx3 - 0.1, ry3 + 0.15), 0.15, fc=CREAM, ec=INK, lw=1.5))
    ax.plot([rx3 - 0.1, rx3 - 0.1], [ry3, ry3 - 0.5], color=INK, lw=2)
    # Raised hand / arm
    ax.plot([rx3 - 0.1, rx3 + 0.25, rx3 + 0.3], [ry3 - 0.05, ry3 + 0.25, ry3 + 0.55],
            color=INK, lw=2.2)
    # Palm lines
    ax.plot([rx3 + 0.3, rx3 + 0.32], [ry3 + 0.55, ry3 + 0.65], color=INK, lw=2)
    # Speech exclamation mark to signify objection
    ax.text(rx3 + 0.55, ry3 + 0.4, "!", fontsize=18, weight="bold", color=DEEP["orange"])

    draw_word_entry(9.6, y3, "proTEST", "second")

    # --- ROW 4: EXport vs exPORT ---
    y4 = rows_y[3]
    # Icon 4L: Ship with containers
    sx, sy = 2.0, y4
    # Hull
    hull_pts = [[sx - 0.65, sy - 0.05], [sx + 0.65, sy - 0.05],
                [sx + 0.45, sy - 0.35], [sx - 0.45, sy - 0.35]]
    ax.add_patch(patches.Polygon(hull_pts, fc=DEEP["blue"], ec=INK, lw=1.5))
    # Containers
    c_w, c_h = 0.25, 0.22
    for cx_offset, fc_c in [(-0.35, GREEN), (-0.05, ORANGE), (0.25, PINK)]:
        ax.add_patch(patches.Rectangle((sx + cx_offset, sy - 0.05), c_w, c_h,
                                       fc=fc_c, ec=INK, lw=1.2))
    # Second tier container
    ax.add_patch(patches.Rectangle((sx - 0.2, sy - 0.05 + c_h), c_w, c_h,
                                   fc=CREAM, ec=INK, lw=1.2))
    # Water ripples
    ax.plot([sx - 0.65, sx + 0.65], [sy - 0.42, sy - 0.42], color=DEEP["blue"], lw=1.5, ls=":")

    draw_word_entry(4.2, y4, "EXport", "first")

    # Icon 4R: Arrow leaving map of Nigeria
    nx, ny = 7.4, y4
    # Real Nigeria polygon outline
    poly_pts = nigeria_poly()
    # Normalize and fit Nigeria in roughly 1x1 unit box around (nx - 0.2, ny - 0.1)
    min_x, max_x = poly_pts[:, 0].min(), poly_pts[:, 0].max()
    min_y, max_y = poly_pts[:, 1].min(), poly_pts[:, 1].max()
    scale = 1.0 / max(max_x - min_x, max_y - min_y)
    norm_pts = np.zeros_like(poly_pts)
    norm_pts[:, 0] = (poly_pts[:, 0] - (min_x + max_x) / 2) * scale + (nx - 0.15)
    norm_pts[:, 1] = (poly_pts[:, 1] - (min_y + max_y) / 2) * scale + (ny - 0.1)
    ax.add_patch(patches.Polygon(norm_pts, closed=True, fc=GREEN, ec=DEEP["green"], lw=1.5))
    # Country label
    ax.text(nx - 0.15, ny - 0.12, "Nigeria", ha="center", va="center", fontsize=9, color=INK)

    # Big arrow leaving the map
    ax.annotate("", xy=(nx + 0.65, ny + 0.4), xytext=(nx, ny),
                arrowprops=dict(facecolor=DEEP["orange"], edgecolor=INK,
                                width=3, headwidth=9, shrink=0.05))

    draw_word_entry(9.6, y4, "exPORT", "second")

    save(fig, out)
