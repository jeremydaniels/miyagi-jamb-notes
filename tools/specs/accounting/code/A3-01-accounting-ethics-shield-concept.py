from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis("off")

    # Title
    ax.text(0, 4.4, "Core Ethical Principles in Accounting", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    # Positions for 5 outer nodes arranged radially
    # Top (90 deg), Top Right (18 deg), Bottom Right (306 deg / -54 deg), Bottom Left (234 deg), Top Left (162 deg)
    angles_deg = [90, 18, -54, 234, 162]
    r = 3.2

    coords = [
        (r * np.cos(np.radians(a)), r * np.sin(np.radians(a)))
        for a in angles_deg
    ]

    labels = [
        "Integrity",
        "Honesty",
        "Fairness",
        "Accountability",
        "Transparency"
    ]

    node_colors = [
        (CREAM, DEEP["orange"]),
        (GREEN, DEEP["green"]),
        (LAV, DEEP["lav"]),
        (PINK, DEEP["pink"]),
        (BLUE, DEEP["blue"])
    ]

    # Connecting lines / rays from centre to shields
    for (cx, cy), (_, edge_c) in zip(coords, node_colors):
        ax.plot([0, cx], [-0.1, cy], color=edge_c, lw=2.5, ls="--", zorder=1, alpha=0.7)

    # Centre: Professional Accountant representation
    # Outer glow / circle
    glow = patches.Circle((0, -0.1), 1.35, facecolor="#F0F4F8", edgecolor=GREY, lw=1.5, zorder=2)
    ax.add_patch(glow)

    # Simple clean professional accountant icon
    # Head
    head = patches.Circle((0, 0.45), 0.32, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=3)
    ax.add_patch(head)
    # Hair
    hair = patches.Arc((0, 0.52), 0.65, 0.5, theta1=20, theta2=160, color=INK, lw=2.5, zorder=4)
    ax.add_patch(hair)
    # Body / Suit
    suit = patches.Polygon([(-0.65, -0.75), (-0.4, 0.05), (0.4, 0.05), (0.65, -0.75)],
                           closed=True, facecolor=BLUE, edgecolor=INK, lw=1.8, zorder=3)
    ax.add_patch(suit)
    # Shirt / Tie
    shirt = patches.Polygon([(-0.2, 0.05), (0, -0.3), (0.2, 0.05)],
                            closed=True, facecolor="white", edgecolor=None, zorder=4)
    ax.add_patch(shirt)
    tie = patches.Polygon([(-0.06, -0.05), (0.06, -0.05), (0.08, -0.45), (0, -0.58), (-0.08, -0.45)],
                          closed=True, facecolor=DEEP["pink"], edgecolor=INK, lw=1, zorder=5)
    ax.add_patch(tie)
    # Ledger / Calculator in hand
    ledger = patches.Rectangle((0.25, -0.65), 0.35, 0.45, facecolor=CREAM, edgecolor=INK, lw=1.4, zorder=6)
    ax.add_patch(ledger)
    ax.plot([0.3, 0.55], [-0.35, -0.35], color=INK, lw=1, zorder=7)
    ax.plot([0.3, 0.55], [-0.45, -0.45], color=INK, lw=1, zorder=7)
    ax.plot([0.3, 0.5], [-0.55, -0.55], color=INK, lw=1, zorder=7)

    # Label for accountant
    ax.text(0, -1.05, "Professional\nAccountant", ha="center", va="center",
            fontsize=14, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=GREY, lw=1), zorder=8)

    # Helper function to draw shield
    def draw_shield(cx, cy, w, h, bg_c, border_c):
        # Shield polygon outline
        pts = [
            (cx - w/2, cy + h*0.35),
            (cx - w/2, cy - h*0.05),
            (cx, cy - h*0.5),
            (cx + w/2, cy - h*0.05),
            (cx + w/2, cy + h*0.35),
            (cx, cy + h*0.48),
        ]
        # Glow effect
        glow_shield = patches.Polygon([(x, y) for x, y in pts], closed=True,
                                      facecolor="white", edgecolor=border_c, lw=6, alpha=0.3, zorder=3)
        ax.add_patch(glow_shield)
        shield = patches.Polygon(pts, closed=True, facecolor=bg_c, edgecolor=border_c, lw=2.2, zorder=4)
        ax.add_patch(shield)

    shield_w, shield_h = 1.6, 1.7

    for (cx, cy), (bg, border) in zip(coords, node_colors):
        draw_shield(cx, cy, shield_w, shield_h, bg, border)

    # --- Icon 1: Top ("Integrity" - Star) ---
    c1x, c1y = coords[0]
    star_angles = np.linspace(0, 2*np.pi, 11)[:-1] - np.pi/2
    r_ext = 0.35
    r_int = 0.16
    radii = np.where(np.arange(10) % 2 == 0, r_ext, r_int)
    star_pts = np.column_stack([c1x + radii * np.cos(star_angles), (c1y + 0.05) + radii * np.sin(star_angles)])
    star = patches.Polygon(star_pts, closed=True, facecolor=DEEP["orange"], edgecolor=INK, lw=1.2, zorder=5)
    ax.add_patch(star)
    ax.text(c1x, c1y - 1.25, "Integrity", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY, lw=1), zorder=6)

    # --- Icon 2: Top right ("Honesty" - Checkmark) ---
    c2x, c2y = coords[1]
    # Checkmark poly
    chk_x = [c2x - 0.28, c2x - 0.08, c2x + 0.32]
    chk_y = [c2y + 0.05, c2y - 0.18, c2y + 0.25]
    ax.plot(chk_x, chk_y, color=DEEP["green"], lw=5, solid_capstyle='round', zorder=5)
    ax.text(c2x, c2y - 1.25, "Honesty", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY, lw=1), zorder=6)

    # --- Icon 3: Bottom right ("Fairness" - Balance scale) ---
    c3x, c3y = coords[2]
    # Central stem
    ax.plot([c3x, c3x], [c3y - 0.3, c3y + 0.28], color=INK, lw=2.5, zorder=5)
    # Base
    ax.plot([c3x - 0.25, c3x + 0.25], [c3y - 0.3, c3y - 0.3], color=INK, lw=2.5, zorder=5)
    # Beam
    ax.plot([c3x - 0.38, c3x + 0.38], [c3y + 0.22, c3y + 0.22], color=INK, lw=2.5, zorder=5)
    # Left pan strings & pan
    ax.plot([c3x - 0.38, c3x - 0.52], [c3y + 0.22, c3y], color=INK, lw=1.2, zorder=5)
    ax.plot([c3x - 0.38, c3x - 0.24], [c3y + 0.22, c3y], color=INK, lw=1.2, zorder=5)
    pan_l = patches.Arc((c3x - 0.38, c3y), 0.3, 0.16, theta1=180, theta2=360, color=DEEP["lav"], lw=2.5, zorder=5)
    ax.add_patch(pan_l)
    # Right pan strings & pan
    ax.plot([c3x + 0.38, c3x + 0.24], [c3y + 0.22, c3y], color=INK, lw=1.2, zorder=5)
    ax.plot([c3x + 0.38, c3x + 0.52], [c3y + 0.22, c3y], color=INK, lw=1.2, zorder=5)
    pan_r = patches.Arc((c3x + 0.38, c3y), 0.3, 0.16, theta1=180, theta2=360, color=DEEP["lav"], lw=2.5, zorder=5)
    ax.add_patch(pan_r)
    ax.text(c3x, c3y - 1.25, "Fairness", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY, lw=1), zorder=6)

    # --- Icon 4: Bottom left ("Accountability" - Document with signature) ---
    c4x, c4y = coords[3]
    # Doc
    doc = patches.Rectangle((c4x - 0.26, c4y - 0.26), 0.52, 0.65, facecolor="white", edgecolor=INK, lw=1.5, zorder=5)
    ax.add_patch(doc)
    # Text lines on doc
    ax.plot([c4x - 0.18, c4x + 0.18], [c4y + 0.22, c4y + 0.22], color=GREY, lw=1.5, zorder=6)
    ax.plot([c4x - 0.18, c4x + 0.18], [c4y + 0.08, c4y + 0.08], color=GREY, lw=1.5, zorder=6)
    ax.plot([c4x - 0.18, c4x + 0.05], [c4y - 0.04, c4y - 0.04], color=GREY, lw=1.5, zorder=6)
    # Signature line & squiggle
    sig_x = np.linspace(c4x - 0.16, c4x + 0.16, 25)
    sig_y = (c4y - 0.17) + 0.04 * np.sin(np.linspace(0, 4*np.pi, 25))
    ax.plot(sig_x, sig_y, color=DEEP["pink"], lw=1.8, zorder=6)
    ax.text(c4x, c4y - 1.25, "Accountability", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY, lw=1), zorder=6)

    # --- Icon 5: Top left ("Transparency" - Magnifying glass over clear doc) ---
    c5x, c5y = coords[4]
    # Clear doc behind
    doc_trans = patches.Rectangle((c5x - 0.32, c5y - 0.2), 0.45, 0.55,
                                  facecolor="#FFFFFF", edgecolor=DEEP["blue"], lw=1.5, linestyle="--", zorder=5)
    ax.add_patch(doc_trans)
    ax.plot([c5x - 0.25, c5x + 0.02], [c5y + 0.2, c5y + 0.2], color=GREY, lw=1.2, zorder=5)
    ax.plot([c5x - 0.25, c5x + 0.02], [c5y + 0.08, c5y + 0.08], color=GREY, lw=1.2, zorder=5)
    # Magnifying glass circle & handle
    mag_centre = (c5x + 0.05, c5y + 0.08)
    mag_lens = patches.Circle(mag_centre, 0.22, facecolor="#E6F2FF", edgecolor=INK, lw=2, zorder=6)
    ax.add_patch(mag_lens)
    ax.plot([mag_centre[0] + 0.15, mag_centre[0] + 0.32],
            [mag_centre[1] - 0.15, mag_centre[1] - 0.32], color=INK, lw=3.5, solid_capstyle='round', zorder=7)
    ax.text(c5x, c5y - 1.25, "Transparency", ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY, lw=1), zorder=6)

    save(fig, out)
