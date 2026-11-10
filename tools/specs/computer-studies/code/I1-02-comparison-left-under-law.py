import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Main Title
    ax.text(6.0, 7.1, "Methods of Protecting Data", ha="center", va="center",
            fontsize=20, weight="bold", color=INK)

    # Dividing line
    ax.plot([6.0, 6.0], [0.5, 6.6], color=GREY, lw=2, linestyle="--")

    # Left Column Header: "By Law"
    ax.text(3.0, 6.4, "By Law", ha="center", va="center",
            fontsize=18, weight="bold", color=DEEP["blue"],
            bbox=dict(fc=BLUE, ec=DEEP["blue"], boxstyle="round,pad=0.4", lw=1.5))

    # Right Column Header: "Electronically"
    ax.text(9.0, 6.4, "Electronically", ha="center", va="center",
            fontsize=18, weight="bold", color=DEEP["green"],
            bbox=dict(fc=GREEN, ec=DEEP["green"], boxstyle="round,pad=0.4", lw=1.5))

    # ------------------ LEFT SIDE: BY LAW ------------------
    # Document 1: "Data Protection Act"
    doc1 = patches.FancyBboxPatch((0.8, 3.2), 2.1, 2.5, boxstyle="round,pad=0.1",
                                 facecolor=CREAM, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(doc1)
    ax.plot([2.6, 2.9, 2.6, 2.6], [5.7, 5.4, 5.4, 5.7], color=DEEP["orange"], lw=1.5)
    for ly in [5.1, 4.7, 4.3, 3.9, 3.5]:
        ax.plot([1.2, 2.6], [ly, ly], color=GREY, lw=2)
    ax.text(1.85, 2.8, "Data Protection\nAct", ha="center", va="top",
            fontsize=14, weight="bold", color=INK)

    # Document 2: "NDA Contract"
    doc2 = patches.FancyBboxPatch((3.3, 3.2), 2.1, 2.5, boxstyle="round,pad=0.1",
                                 facecolor="#FFFFFF", edgecolor=DEEP["blue"], lw=2)
    ax.add_patch(doc2)
    ax.plot([5.1, 5.4, 5.1, 5.1], [5.7, 5.4, 5.4, 5.7], color=DEEP["blue"], lw=1.5)
    seal = patches.Circle((4.35, 4.7), 0.45, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5)
    ax.add_patch(seal)
    ax.text(4.35, 4.7, "NDA", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["pink"])
    for ly in [4.0, 3.6]:
        ax.plot([3.6, 5.1], [ly, ly], color=GREY, lw=2)
    ax.text(4.35, 2.8, "NDA Contract", ha="center", va="top",
            fontsize=14, weight="bold", color=INK)

    # Judge's Gavel (placed lower to avoid text overlaps)
    sb = patches.FancyBboxPatch((2.2, 0.7), 1.6, 0.3, boxstyle="round,pad=0.05",
                               facecolor=ORANGE, edgecolor=INK, lw=2)
    ax.add_patch(sb)
    gh = patches.FancyBboxPatch((2.5, 1.05), 1.0, 0.4, boxstyle="round,pad=0.05",
                               facecolor=DEEP["orange"], edgecolor=INK, lw=2)
    ax.add_patch(gh)
    gh_handle = patches.Rectangle((3.2, 1.15), 1.5, 0.2, angle=15,
                                  facecolor=ORANGE, edgecolor=INK, lw=2)
    ax.add_patch(gh_handle)

    # ------------------ RIGHT SIDE: ELECTRONICALLY ------------------
    # 1. Laptop with padlock on the screen
    screen_frame = patches.FancyBboxPatch((6.6, 3.5), 2.5, 1.8, boxstyle="round,pad=0.08",
                                         facecolor=INK, edgecolor=INK, lw=1.5)
    ax.add_patch(screen_frame)
    display = patches.Rectangle((6.75, 3.65), 2.2, 1.5, facecolor=BLUE, edgecolor="none")
    ax.add_patch(display)
    base = patches.Polygon([[6.3, 3.3], [9.4, 3.3], [9.1, 3.5], [6.6, 3.5]],
                           closed=True, facecolor=GREY, edgecolor=INK, lw=1.8)
    ax.add_patch(base)
    touchpad = patches.Rectangle((7.6, 3.35), 0.5, 0.12, facecolor="white", edgecolor=INK, lw=1)
    ax.add_patch(touchpad)

    # Padlock on the screen
    shackle = patches.Arc((7.85, 4.5), 0.5, 0.6, angle=0, theta1=0, theta2=180,
                          edgecolor=INK, lw=3)
    ax.add_patch(shackle)
    lock_body = patches.FancyBboxPatch((7.55, 3.95), 0.6, 0.5, boxstyle="round,pad=0.04",
                                       facecolor=ORANGE, edgecolor=INK, lw=2)
    ax.add_patch(lock_body)
    ax.plot([7.85, 7.85], [4.12, 4.25], color=INK, lw=2)

    # 2. VPN Shield
    shield_pts = [
        [10.6, 5.3],
        [11.4, 5.0],
        [11.2, 3.8],
        [10.6, 3.2],
        [10.0, 3.8],
        [9.8, 5.0],
    ]
    shield = patches.Polygon(shield_pts, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5)
    ax.add_patch(shield)
    ax.text(10.6, 4.35, "VPN", ha="center", va="center",
            fontsize=17, weight="bold", color=DEEP["green"])
    
    # Text labels for devices
    ax.text(7.85, 2.8, "Secure Device", ha="center", va="top",
            fontsize=14, weight="bold", color=INK)
    ax.text(10.6, 2.8, "VPN Shield", ha="center", va="top",
            fontsize=14, weight="bold", color=INK)

    # 3. Scrambled text (Encryption) box (sized safely to prevent border overlap)
    enc_box = patches.FancyBboxPatch((6.4, 0.7), 5.2, 1.4, boxstyle="round,pad=0.1",
                                    facecolor=LAV, edgecolor=DEEP["lav"], lw=2)
    ax.add_patch(enc_box)
    ax.text(9.0, 1.7, "Encryption", ha="center", va="center",
            fontsize=15, weight="bold", color=DEEP["lav"])
    ax.text(9.0, 1.2, "#7x!9$qL -> [PROTECTED]", ha="center", va="center",
            fontsize=14, family="monospace", weight="bold", color=INK)

    save(fig, out)
