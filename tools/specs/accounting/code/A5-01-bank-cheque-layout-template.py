from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Cheque dimensions & outer boundary
    cx, cy, cw, ch = 2.0, 1.2, 9.6, 4.8
    cheque_bg = patches.Rectangle((cx, cy), cw, ch, facecolor=CREAM, edgecolor=DEEP["blue"], linewidth=2, zorder=1)
    ax.add_patch(cheque_bg)

    # Cheque border decorative inner line
    cheque_inner = patches.Rectangle((cx + 0.1, cy + 0.1), cw - 0.2, ch - 0.2, facecolor='none', edgecolor=BLUE, linewidth=1, linestyle='-', zorder=2)
    ax.add_patch(cheque_inner)

    # Bank Name & Address (Drawee) - clearly separated vertically
    ax.text(cx + 0.5, cy + ch - 0.55, "MIYAGI BANK PLC", fontsize=18, fontweight='bold', color=INK, zorder=3)
    ax.text(cx + 0.5, cy + ch - 1.05, "Victoria Island Branch, Lagos, Nigeria", fontsize=14, color=INK, zorder=3)

    # Date Box
    date_x = cx + cw - 3.2
    date_y = cy + ch - 0.8
    ax.text(date_x - 0.85, date_y + 0.05, "Date:", fontsize=14, fontweight='bold', color=INK, zorder=3)
    date_str = "15102023"
    for i, char in enumerate(date_str):
        bx = date_x + i * 0.35
        rect = patches.Rectangle((bx, date_y - 0.05), 0.32, 0.4, facecolor='white', edgecolor=GREY, linewidth=1.2, zorder=3)
        ax.add_patch(rect)
        ax.text(bx + 0.16, date_y + 0.12, char, fontsize=14, color=INK, ha='center', va='center', zorder=4)

    # Pay line
    ax.text(cx + 0.5, cy + 2.8, "Pay", fontsize=16, fontweight='bold', color=INK, zorder=3)
    ax.plot([cx + 1.2, cx + 6.3], [cy + 2.7, cy + 2.7], color=GREY, lw=1.2, zorder=3)
    ax.text(cx + 1.4, cy + 2.85, "Chukwudi Enterprises", fontsize=15, fontweight='bold', color=DEEP["blue"], zorder=3)
    ax.text(cx + 6.45, cy + 2.8, "or Bearer", fontsize=14, color=INK, zorder=3)

    # Amount in figures box
    box_x = cx + cw - 2.8
    box_y = cy + 2.5
    amount_box = patches.Rectangle((box_x, box_y), 2.5, 0.75, facecolor='white', edgecolor=DEEP["blue"], linewidth=1.5, zorder=3)
    ax.add_patch(amount_box)
    ax.text(box_x + 1.25, box_y + 0.36, "₦145,000", fontsize=16, fontweight='bold', color=INK, ha='center', va='center', zorder=4)

    # Amount in words line ("The sum of")
    ax.text(cx + 0.5, cy + 1.9, "The sum of", fontsize=14, fontweight='bold', color=INK, zorder=3)
    ax.plot([cx + 2.0, cx + cw - 0.5], [cy + 1.8, cy + 1.8], color=GREY, lw=1.2, zorder=3)
    ax.text(cx + 2.1, cy + 1.95, "One hundred and forty-five thousand naira only ----------------", fontsize=14, fontweight='bold', color=INK, zorder=3)

    # Drawer Signature line
    sig_line_x = cx + cw - 3.4
    sig_y = cy + 0.85
    ax.plot([sig_line_x, sig_line_x + 3.0], [sig_y, sig_y], color=GREY, lw=1.2, zorder=3)
    # Simulated signature curve
    sx = np.linspace(sig_line_x + 0.2, sig_line_x + 2.8, 120)
    sy = sig_y + 0.2 + 0.15 * np.sin(4 * np.pi * (sx - sig_line_x)) * np.exp(-(sx - sig_line_x - 1.4)**2) + 0.1 * np.sin(9 * np.pi * (sx - sig_line_x))
    ax.plot(sx, sy, color=DEEP["pink"], lw=2.2, zorder=4)
    ax.text(sig_line_x + 1.5, sig_y - 0.25, "Authorised Signatory", fontsize=14, color=INK, ha='center', zorder=3)

    # MICR line at bottom
    ax.text(cx + 0.5, cy + 0.25, "⑈ 001245 ⑈   057150014 ⑆   0123456789 ⑈ 21", fontsize=14, family='monospace', color=GREY, zorder=3)

    # ANNOTATIONS with ARROWS
    # Drawee (The bank)
    ax.annotate(
        "Drawee\n(The Bank)",
        xy=(cx + 2.4, cy + ch - 0.55), xycoords='data',
        xytext=(1.0, 6.7), textcoords='data',
        fontsize=15, fontweight='bold', color=INK,
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2, shrinkA=3, shrinkB=6),
        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3"),
        ha="center"
    )

    # Payee (Chukwudi Enterprises)
    ax.annotate(
        "Payee\n(Beneficiary)",
        xy=(cx + 3.2, cy + 3.0), xycoords='data',
        xytext=(0.95, 3.8), textcoords='data',
        fontsize=15, fontweight='bold', color=INK,
        arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2, shrinkA=3, shrinkB=6),
        bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3"),
        ha="center"
    )

    # Drawer (The signature)
    ax.annotate(
        "Drawer\n(Account Holder)",
        xy=(sig_line_x + 1.5, sig_y + 0.2), xycoords='data',
        xytext=(sig_line_x + 1.5, 0.35), textcoords='data',
        fontsize=15, fontweight='bold', color=INK,
        arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2, shrinkA=3, shrinkB=6),
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3"),
        ha="center"
    )

    save(fig, out)
