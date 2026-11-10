from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6, 6.9, "Economic Systems Spectrum", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    # Spectrum gradient arrow line in the background
    ax.annotate("", xy=(11.2, 6.2), xytext=(0.8, 6.2),
                arrowprops=dict(arrowstyle="<->", lw=3, color=GREY))
    ax.text(0.8, 6.5, "Market Forces", ha="left", va="center", fontsize=14, color=DEEP["blue"], weight="bold")
    ax.text(11.2, 6.5, "Government Control", ha="right", va="center", fontsize=14, color=DEEP["pink"], weight="bold")

    # Three main cards / zones
    # Left: Free Enterprise / Capitalism (Blue)
    # Middle: Mixed Economy (LAV / Purple)
    # Right: Centrally Planned / Command Economy (Pink / Red)

    centers = [2.3, 6.0, 9.7]
    box_w, box_h = 3.2, 4.8
    y_box = 0.8

    colors_face = [BLUE, LAV, PINK]
    colors_deep = [DEEP["blue"], DEEP["lav"], DEEP["pink"]]

    titles = [
        "Free Enterprise /\nCapitalism",
        "Mixed\nEconomy",
        "Centrally Planned /\nCommand Economy"
    ]

    ownerships = [
        "Private ownership",
        "Joint ownership",
        "State ownership"
    ]

    # Draw rounded boxes for each system
    for i in range(3):
        xc = centers[i]
        rect = patches.FancyBboxPatch((xc - box_w/2, y_box), box_w, box_h,
                                      boxstyle="round,pad=0.15,rounding_size=0.3",
                                      facecolor=colors_face[i], edgecolor=colors_deep[i],
                                      linewidth=2.5)
        ax.add_patch(rect)

        # Title
        ax.text(xc, 5.0, titles[i], ha="center", va="center",
                fontsize=15, weight="bold", color=INK)

        # Bottom ownership label
        ax.text(xc, 1.3, ownerships[i], ha="center", va="center",
                fontsize=14, weight="bold", color=colors_deep[i],
                bbox=dict(fc="white", ec=colors_deep[i], boxstyle="round,pad=0.3", lw=1.5))

    # --- Left Icons: Dollar sign & Factory ---
    # Dollar Sign (circular badge)
    c_dollar = patches.Circle((1.5, 3.4), 0.55, facecolor="white", edgecolor=DEEP["blue"], lw=2)
    ax.add_patch(c_dollar)
    ax.text(1.5, 3.4, "$", ha="center", va="center", fontsize=18, weight="bold", color=DEEP["blue"])

    # Factory outline
    fx, fy = 2.4, 2.9
    # Base
    ax.add_patch(patches.Rectangle((fx, fy), 0.9, 0.5, facecolor="white", edgecolor=DEEP["blue"], lw=2))
    # Sawtooth roofs
    roof_pts = np.array([
        [fx, fy + 0.5],
        [fx + 0.45, fy + 0.85],
        [fx + 0.45, fy + 0.5],
        [fx + 0.9, fy + 0.85],
        [fx + 0.9, fy + 0.5]
    ])
    ax.plot(roof_pts[:, 0], roof_pts[:, 1], color=DEEP["blue"], lw=2)
    # Chimney stack
    ax.add_patch(patches.Rectangle((fx + 0.65, fy + 0.85), 0.18, 0.35, facecolor="white", edgecolor=DEEP["blue"], lw=2))
    # Small door
    ax.add_patch(patches.Rectangle((fx + 0.15, fy), 0.2, 0.3, facecolor=DEEP["blue"], edgecolor="none"))

    # --- Middle Icons: Handshake between Businessperson & Official ---
    # Handshake circular badge shifted up to leave plenty of room for label below
    handshake_center_y = 3.5
    c_mid = patches.Circle((6.0, handshake_center_y), 0.9, facecolor="white", edgecolor=DEEP["lav"], lw=2)
    ax.add_patch(c_mid)

    # Handshake illustration inside badge
    # Left cuff (Business suit: blue), Right cuff (Uniform/State: pink)
    ax.add_patch(patches.Rectangle((5.35, handshake_center_y - 0.2), 0.22, 0.38, facecolor=DEEP["blue"], edgecolor=INK, lw=1.5))
    ax.add_patch(patches.Rectangle((6.43, handshake_center_y - 0.2), 0.22, 0.38, facecolor=DEEP["pink"], edgecolor=INK, lw=1.5))
    # Hands meeting: simplified clasp
    hand_l = patches.Polygon([[5.57, handshake_center_y - 0.1], [5.92, handshake_center_y - 0.1],
                             [6.10, handshake_center_y + 0.12], [5.82, handshake_center_y + 0.17],
                             [5.57, handshake_center_y + 0.08]],
                             facecolor=CREAM, edgecolor=INK, lw=1.5)
    hand_r = patches.Polygon([[6.43, handshake_center_y - 0.1], [6.08, handshake_center_y - 0.1],
                             [5.90, handshake_center_y + 0.04], [6.18, handshake_center_y + 0.17],
                             [6.43, handshake_center_y + 0.08]],
                             facecolor=CREAM, edgecolor=INK, lw=1.5)
    ax.add_patch(hand_l)
    ax.add_patch(hand_r)
    # Clear placement well below the circle border (circle bottom is at y = 2.6)
    ax.text(6.0, 2.15, "Public–Private\nPartnership", ha="center", va="center", fontsize=14, color=INK)

    # --- Right Icons: Government Building & Gears ---
    # Government building (Pantheon style)
    gx, gy = 8.5, 2.9
    # Base
    ax.add_patch(patches.Rectangle((gx, gy), 1.0, 0.1, facecolor="white", edgecolor=DEEP["pink"], lw=1.8))
    # Columns
    for cx_col in np.linspace(gx + 0.1, gx + 0.9 - 0.12, 3):
        ax.add_patch(patches.Rectangle((cx_col, gy + 0.1), 0.12, 0.5, facecolor="white", edgecolor=DEEP["pink"], lw=1.8))
    # Architrave / Frieze
    ax.add_patch(patches.Rectangle((gx, gy + 0.6), 1.0, 0.1, facecolor="white", edgecolor=DEEP["pink"], lw=1.8))
    # Pediment (triangle)
    pediment = patches.Polygon([[gx - 0.05, gy + 0.7], [gx + 0.5, gy + 1.0], [gx + 1.05, gy + 0.7]],
                               facecolor="white", edgecolor=DEEP["pink"], lw=1.8)
    ax.add_patch(pediment)

    # Gear icon (drawn next to building)
    gear_center = (10.4, 3.4)
    c_gear_outer = patches.Circle(gear_center, 0.45, facecolor="white", edgecolor=DEEP["pink"], lw=2)
    c_gear_inner = patches.Circle(gear_center, 0.18, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.8)
    ax.add_patch(c_gear_outer)
    # Gear teeth
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        tx = gear_center[0] + 0.45 * np.cos(angle)
        ty = gear_center[1] + 0.45 * np.sin(angle)
        ax.plot([tx, gear_center[0] + 0.55 * np.cos(angle)],
                [ty, gear_center[1] + 0.55 * np.sin(angle)],
                color=DEEP["pink"], lw=3.5, solid_capstyle="round")
    ax.add_patch(c_gear_inner)

    save(fig, out)
