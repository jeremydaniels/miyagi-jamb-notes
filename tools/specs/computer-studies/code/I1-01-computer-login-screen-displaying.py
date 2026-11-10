from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Background screen frame representing computer login screen
    screen_bg = patches.FancyBboxPatch((0.6, 0.5), 10.8, 6.5, boxstyle="round,pad=0.2,rounding_size=0.4",
                                       fc="white", ec=GREY, lw=2)
    ax.add_patch(screen_bg)

    # Top title bar
    ax.text(6.0, 6.4, "Authentication Methods", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)
    ax.text(6.0, 5.95, "Select an authentication method to log in",
            ha="center", va="center", fontsize=14, color=GREY)

    # Divider line
    ax.plot([1.2, 10.8], [5.6, 5.6], color=GREY, lw=1.2, ls="--")

    # Three Authentication Cards:
    # 1. Username and Password
    # 2. Fingerprint Scanner
    # 3. Smart Card Reader
    cards = [
        {"x": 1.1, "title": "Username and Password", "color": BLUE, "deep": DEEP["blue"]},
        {"x": 4.6, "title": "Fingerprint Scanner", "color": GREEN, "deep": DEEP["green"]},
        {"x": 8.1, "title": "Smart Card Reader", "color": LAV, "deep": DEEP["lav"]}
    ]

    card_w = 2.8
    card_h = 4.4
    card_y = 0.9

    for c in cards:
        card_box = patches.FancyBboxPatch((c["x"], card_y), card_w, card_h,
                                          boxstyle="round,pad=0.1,rounding_size=0.2",
                                          fc=c["color"], ec=c["deep"], lw=2)
        ax.add_patch(card_box)

        # Header Title
        ax.text(c["x"] + card_w / 2.0, card_y + card_h - 0.45, c["title"],
                ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # --- CARD 1: Username and Password ---
    c1_cx = 1.1 + card_w / 2.0

    # User avatar circle
    avatar_bg = patches.Circle((c1_cx, 4.0), 0.55, fc="white", ec=DEEP["blue"], lw=2)
    ax.add_patch(avatar_bg)
    head = patches.Circle((c1_cx, 4.12), 0.2, fc=DEEP["blue"])
    ax.add_patch(head)
    shoulder = patches.Arc((c1_cx, 3.65), 0.6, 0.5, theta1=0, theta2=180, color=DEEP["blue"], lw=3)
    ax.add_patch(shoulder)

    # Username label & box
    ax.text(1.4, 3.15, "Username", fontsize=14, color=INK, weight="bold")
    u_box = patches.FancyBboxPatch((1.4, 2.5), 2.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.08",
                                   fc="white", ec=GREY, lw=1.5)
    ax.add_patch(u_box)
    ax.text(1.55, 2.72, "user@domain", fontsize=14, color=INK, va="center")

    # Password label & box
    ax.text(1.4, 2.15, "Password", fontsize=14, color=INK, weight="bold")
    p_box = patches.FancyBboxPatch((1.4, 1.5), 2.2, 0.45, boxstyle="round,pad=0.04,rounding_size=0.08",
                                   fc="white", ec=GREY, lw=1.5)
    ax.add_patch(p_box)
    # Password masked dots
    for dx in np.linspace(1.65, 2.7, 6):
        ax.plot(dx, 1.72, marker='o', markersize=6, color=INK)

    # --- CARD 2: Fingerprint Scanner ---
    c2_cx = 4.6 + card_w / 2.0
    scan_cy = 3.2

    # Scanner pad base
    pad = patches.FancyBboxPatch((c2_cx - 0.9, scan_cy - 1.1), 1.8, 2.2,
                                 boxstyle="round,pad=0.1,rounding_size=0.25",
                                 fc="white", ec=DEEP["green"], lw=2)
    ax.add_patch(pad)

    # Concentric fingerprint ridges
    radii = [0.2, 0.35, 0.5, 0.65, 0.8]
    angles = [(20, 160), (30, 150), (15, 165), (35, 145), (40, 140)]
    for r, (t1, t2) in zip(radii, angles):
        arc_top = patches.Arc((c2_cx, scan_cy), r * 1.3, r * 1.8,
                              angle=0, theta1=t1, theta2=t2, color=DEEP["green"], lw=2.5)
        ax.add_patch(arc_top)

    # Lower fingerprint loops
    for r in [0.35, 0.55, 0.75]:
        arc_bot1 = patches.Arc((c2_cx - 0.1, scan_cy - 0.2), r * 0.9, r * 1.2,
                               angle=-20, theta1=200, theta2=330, color=DEEP["green"], lw=2.2)
        ax.add_patch(arc_bot1)

    # Instruction text
    ax.text(c2_cx, 1.45, "Touch sensor\nto scan fingerprint", ha="center", va="center",
            fontsize=14, color=INK, weight="bold")

    # --- CARD 3: Smart Card Reader ---
    c3_cx = 8.1 + card_w / 2.0

    # Reader slot / device
    reader_base = patches.Rectangle((c3_cx - 1.05, 1.9), 2.1, 1.2,
                                    fc="white", ec=DEEP["lav"], lw=2.5)
    ax.add_patch(reader_base)
    # Reader slot opening
    slot = patches.Rectangle((c3_cx - 0.8, 2.85), 1.6, 0.1, fc=DEEP["lav"], ec=DEEP["lav"])
    ax.add_patch(slot)

    # Smart Card inserted into slot
    card_shape = patches.FancyBboxPatch((c3_cx - 0.7, 2.6), 1.4, 1.8,
                                        boxstyle="round,pad=0.03,rounding_size=0.1",
                                        fc=CREAM, ec=INK, lw=2)
    ax.add_patch(card_shape)

    # Gold chip on card
    chip = patches.Rectangle((c3_cx - 0.25, 3.4), 0.5, 0.45,
                             fc=ORANGE, ec=DEEP["orange"], lw=1.5)
    ax.add_patch(chip)
    # Chip contact grid
    ax.plot([c3_cx, c3_cx], [3.4, 3.85], color=DEEP["orange"], lw=1.2)
    ax.plot([c3_cx - 0.25, c3_cx + 0.25], [3.62, 3.62], color=DEEP["orange"], lw=1.2)

    # Arrow indicating insertion
    ax.annotate("", xy=(c3_cx, 2.3), xytext=(c3_cx, 2.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=3))

    # Instruction text
    ax.text(c3_cx, 1.45, "Insert smart card\ninto card reader", ha="center", va="center",
            fontsize=14, color=INK, weight="bold")

    save(fig, out)
