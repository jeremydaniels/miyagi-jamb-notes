from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(16, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(8.0, 7.0, "The Evolution of Money", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Main horizontal timeline arrow
    ax.annotate(
        "", xy=(15.2, 3.4), xytext=(0.8, 3.4),
        arrowprops=dict(arrowstyle="->", lw=2.5, color=GREY, mutation_scale=20)
    )

    stage_centers = [2.3, 6.1, 9.9, 13.7]

    # Stage panels / backgrounds
    for x in stage_centers:
        panel = patches.FancyBboxPatch(
            (x - 1.7, 1.4), 3.4, 4.8,
            boxstyle="round,pad=0.15,rounding_size=0.3",
            facecolor="white", edgecolor=GREY, lw=1.5
        )
        ax.add_patch(panel)

    # Connecting subtle arrows between stages
    for i in range(3):
        ax.annotate(
            "", xy=(stage_centers[i+1] - 1.75, 3.8), xytext=(stage_centers[i] + 1.75, 3.8),
            arrowprops=dict(arrowstyle="->", lw=2.0, color=DEEP["blue"], mutation_scale=15)
        )

    # -------------------------------------------------------------
    # STAGE 1: Commodity money (Cowries, Manillas)
    # -------------------------------------------------------------
    # Manilla (horseshoe/c-shaped flared bronze ornament)
    manilla_arc = patches.Arc(
        (2.3, 3.9), 2.2, 2.0, angle=0, theta1=45, theta2=315,
        color=DEEP["orange"], lw=8, capstyle="round"
    )
    ax.add_patch(manilla_arc)
    # Flared ends of manilla
    ax.scatter([1.55, 1.55], [4.55, 3.25], s=140, color=DEEP["orange"], zorder=4)

    # Cowrie shells (smooth ovals with jagged slit in the center)
    shell_data = [
        (2.0, 3.5, -20),
        (2.6, 3.4, 25),
        (2.1, 4.3, 10),
        (2.7, 4.2, -15)
    ]
    for sx, sy, rot in shell_data:
        shell = patches.Ellipse((sx, sy), 0.75, 0.5, angle=rot, facecolor=CREAM, edgecolor=INK, lw=1.4, zorder=5)
        ax.add_patch(shell)
        # Characteristic cowrie slit
        rad = np.radians(rot)
        dx, dy = 0.25 * np.cos(rad), 0.25 * np.sin(rad)
        ax.plot([sx - dx, sx + dx], [sy - dy, sy + dy], color=INK, lw=1.5, zorder=6)
        # Tiny teeth across slit
        for t in np.linspace(-0.18, 0.18, 5):
            px = sx + t * np.cos(rad)
            py = sy + t * np.sin(rad)
            ax.plot([px - 0.06 * np.sin(rad), px + 0.06 * np.sin(rad)],
                    [py + 0.06 * np.cos(rad), py - 0.06 * np.cos(rad)],
                    color=INK, lw=1.0, zorder=7)

    # -------------------------------------------------------------
    # STAGE 2: Metallic money (Coins)
    # -------------------------------------------------------------
    # Gold and silver overlapping coins
    coins = [
        # (x, y, r, fill, edge, label)
        (5.7, 3.4, 0.52, CREAM, DEEP["orange"], "Au"),
        (6.5, 3.4, 0.55, "#E8E8E8", GREY, "Ag"),
        (5.4, 4.0, 0.50, "#E8E8E8", GREY, "Ag"),
        (6.2, 4.0, 0.58, CREAM, DEEP["orange"], "Au"),
        (5.8, 4.6, 0.52, CREAM, DEEP["orange"], "Au"),
        (6.6, 4.4, 0.48, "#E8E8E8", GREY, "Ag"),
    ]
    for cx, cy, r, fc, ec, lbl in coins:
        coin = patches.Circle((cx, cy), r, facecolor=fc, edgecolor=ec, lw=2.0, zorder=4)
        inner = patches.Circle((cx, cy), r * 0.8, fill=False, edgecolor=ec, lw=1.0, linestyle=":", zorder=5)
        ax.add_patch(coin)
        ax.add_patch(inner)
        ax.text(cx, cy, lbl, fontsize=14, ha="center", va="center", color=ec, fontweight="bold", zorder=6)

    # -------------------------------------------------------------
    # STAGE 3: Early paper money (Goldsmiths' receipts)
    # -------------------------------------------------------------
    # Old-fashioned parchment receipt
    receipt = patches.FancyBboxPatch(
        (8.8, 3.0), 2.2, 2.7,
        boxstyle="round,pad=0.04,rounding_size=0.1",
        facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.8, zorder=4
    )
    ax.add_patch(receipt)
    # Receipt header
    ax.text(9.9, 5.3, "RECEIPT", fontsize=14, fontweight="bold", ha="center", va="center", color=INK, zorder=5)
    ax.plot([9.1, 10.7], [5.05, 5.05], color=GREY, lw=1.0, zorder=5)
    # Cursive-like wavy text lines
    wave_x = np.linspace(9.1, 10.7, 40)
    for wy in [4.7, 4.3, 3.9, 3.5]:
        wave_y = wy + 0.03 * np.sin(wave_x * 25)
        ax.plot(wave_x, wave_y, color=INK, lw=1.2, zorder=5)
    # Wax seal
    seal = patches.Circle((10.5, 3.3), 0.28, facecolor=DEEP["pink"], edgecolor=INK, lw=1.0, zorder=6)
    ax.add_patch(seal)

    # -------------------------------------------------------------
    # STAGE 4: Modern fiat and electronic money
    # -------------------------------------------------------------
    # ₦1,000 banknote
    note = patches.FancyBboxPatch(
        (12.4, 4.1), 2.5, 1.4,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        facecolor="#EBF5ED", edgecolor=DEEP["green"], lw=1.8, zorder=4
    )
    ax.add_patch(note)
    ax.text(12.6, 5.15, "₦1000", fontsize=14, fontweight="bold", color=DEEP["green"], zorder=5)
    ax.text(14.6, 4.35, "₦1000", fontsize=14, fontweight="bold", color=DEEP["green"], zorder=5)
    # Central portrait silhouette / emblem box
    portrait = patches.Rectangle((13.3, 4.4), 0.75, 0.8, facecolor="white", edgecolor=DEEP["green"], lw=1.0, zorder=5)
    ax.add_patch(portrait)
    ax.text(13.67, 4.8, "CBN", fontsize=14, ha="center", va="center", color=DEEP["green"], fontweight="bold", zorder=6)

    # ATM Card (overlapping below)
    card = patches.FancyBboxPatch(
        (12.7, 2.8), 2.2, 1.3,
        boxstyle="round,pad=0.03,rounding_size=0.1",
        facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.8, zorder=6
    )
    ax.add_patch(card)
    # EMV Chip
    chip = patches.FancyBboxPatch(
        (12.95, 3.4), 0.38, 0.3,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.2, zorder=7
    )
    ax.add_patch(chip)
    # Card details (wireless logo & numbers)
    ax.text(14.7, 3.8, "DEBIT", fontsize=14, ha="right", va="center", color=DEEP["blue"], fontweight="bold", zorder=7)
    ax.text(12.95, 3.05, "•••• 4821", fontsize=14, ha="left", va="center", color=INK, zorder=7)

    # Stage description labels (bottom of each stage)
    labels = [
        "1. Commodity money\n(Cowries, Manillas)",
        "2. Metallic money\n(Coins)",
        "3. Early paper money\n(Goldsmiths' receipts)",
        "4. Modern fiat and\nelectronic money"
    ]

    for x, lbl in zip(stage_centers, labels):
        ax.text(
            x, 0.7, lbl,
            fontsize=14, ha="center", va="center", color=INK, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=2.0)
        )

    save(fig, out)
