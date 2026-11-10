import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    # Canvas setup
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    # ----------------------------------------------------
    # Title & Subtitles
    # ----------------------------------------------------
    ax.text(6.0, 7.4, "Layered Defense System (Defense-in-Depth)", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # ----------------------------------------------------
    # LAYER 1: OUTER WALL (Firewall protecting network)
    # Left region: x in [0.8, 4.2], y in [1.2, 6.8]
    # ----------------------------------------------------
    # Wall background panel
    wall_bg = patches.Rectangle((0.8, 1.2), 3.4, 5.4, facecolor=CREAM, 
                                edgecolor=DEEP['orange'], lw=2.5, linestyle='--')
    ax.add_patch(wall_bg)

    # Brick pattern for the firewall
    brick_w, brick_h = 0.7, 0.32
    wall_x0, wall_y0 = 1.1, 1.5
    wall_cols, wall_rows = 4, 11
    
    for r in range(wall_rows):
        y = wall_y0 + r * brick_h
        shift = 0.35 if (r % 2 == 1) else 0.0
        for c in range(wall_cols + 1):
            x = wall_x0 + c * brick_w - shift
            # Clip brick boundaries to fit neatly
            bx = max(wall_x0, x)
            bw = min(wall_x0 + wall_cols * brick_w, x + brick_w) - bx
            if bw > 0.05:
                brick = patches.Rectangle((bx, y), bw, brick_h - 0.04, 
                                          facecolor=ORANGE, edgecolor=DEEP['orange'], lw=1.2)
                ax.add_patch(brick)

    # Flame icon / symbol at top of wall
    flame_pts = np.array([
        [2.5, 5.3], [2.2, 5.6], [2.1, 6.0], [2.3, 6.1], 
        [2.2, 6.4], [2.5, 6.2], [2.7, 6.45], [2.9, 6.1], 
        [3.0, 5.7], [2.8, 5.5], [2.5, 5.3]
    ])
    flame = patches.Polygon(flame_pts, closed=True, facecolor=PINK, edgecolor=DEEP['pink'], lw=2)
    ax.add_patch(flame)

    # Firewall Label & Description
    ax.text(2.5, 6.7, "Firewall", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(fc='white', ec=DEEP['orange'], boxstyle='round,pad=0.3', lw=1.5))
    ax.text(2.5, 0.7, "Outer Perimeter:\nNetwork Filtering", ha='center', va='center', 
            fontsize=14, color=INK)

    # Flow arrow from Firewall to Encryption Vault
    ax.annotate("", xy=(4.6, 3.8), xytext=(4.0, 3.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5))

    # ----------------------------------------------------
    # LAYER 2: VAULT (Encryption protecting data inside)
    # Middle region: x in [4.5, 7.7], y in [1.2, 6.8]
    # ----------------------------------------------------
    vault_bg = patches.Rectangle((4.5, 1.2), 3.2, 5.4, facecolor=CREAM,
                                 edgecolor=DEEP['blue'], lw=2.5, linestyle='--')
    ax.add_patch(vault_bg)

    # Vault outer steel frame
    vault_box = patches.FancyBboxPatch((4.9, 2.0), 2.4, 3.8, boxstyle="round,pad=0.1",
                                       facecolor=BLUE, edgecolor=DEEP['blue'], lw=2.5)
    ax.add_patch(vault_box)

    # Vault inner door
    vault_door = patches.Circle((6.1, 3.9), 1.2, facecolor=GREY, edgecolor=DEEP['blue'], lw=2.5)
    ax.add_patch(vault_door)
    vault_inner = patches.Circle((6.1, 3.9), 0.75, facecolor='white', edgecolor=DEEP['blue'], lw=1.8)
    ax.add_patch(vault_inner)

    # Vault dial & spokes
    ax.scatter([6.1], [3.9], s=80, color=DEEP['blue'], zorder=4)
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = np.deg2rad(angle)
        x1, y1 = 6.1 + 0.15 * np.cos(rad), 3.9 + 0.15 * np.sin(rad)
        x2, y2 = 6.1 + 0.55 * np.cos(rad), 3.9 + 0.55 * np.sin(rad)
        ax.plot([x1, x2], [y1, y2], color=DEEP['blue'], lw=2.5, zorder=3)

    # Data block inside vault (representation of protected data)
    data_badge = patches.Rectangle((5.35, 2.2), 1.5, 0.45, facecolor=GREEN, 
                                   edgecolor=DEEP['green'], lw=1.5, zorder=4)
    ax.add_patch(data_badge)
    ax.text(6.1, 2.42, "Encrypted Data", ha='center', va='center', 
            fontsize=14, color=INK, weight='bold', zorder=5)

    # Encryption Label & Description
    ax.text(6.1, 6.7, "Encryption", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(fc='white', ec=DEEP['blue'], boxstyle='round,pad=0.3', lw=1.5))
    ax.text(6.1, 0.7, "Storage / Transit:\nCryptographic Vault", ha='center', va='center', 
            fontsize=14, color=INK)

    # Flow arrow from Vault to Antivirus Endpoint
    ax.annotate("", xy=(8.1, 3.8), xytext=(7.5, 3.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5))

    # ----------------------------------------------------
    # LAYER 3: ANTIVIRUS & COMPUTER (Inspecting a file)
    # Right region: x in [8.0, 11.2], y in [1.2, 6.8]
    # ----------------------------------------------------
    endpoint_bg = patches.Rectangle((8.0, 1.2), 3.2, 5.4, facecolor=CREAM,
                                    edgecolor=DEEP['green'], lw=2.5, linestyle='--')
    ax.add_patch(endpoint_bg)

    # Computer Monitor Screen
    screen_frame = patches.FancyBboxPatch((8.4, 2.7), 2.4, 2.1, boxstyle="round,pad=0.08",
                                          facecolor=GREY, edgecolor=INK, lw=2.2)
    ax.add_patch(screen_frame)
    screen_display = patches.Rectangle((8.55, 2.95), 2.1, 1.65, facecolor='white',
                                       edgecolor=GREY, lw=1.2)
    ax.add_patch(screen_display)

    # Computer Stand & Base
    stand = patches.Rectangle((9.45, 2.3), 0.3, 0.4, facecolor=GREY, edgecolor=INK, lw=2)
    base = patches.FancyBboxPatch((9.1, 2.15), 1.0, 0.15, boxstyle="round,pad=0.05",
                                  facecolor=GREY, edgecolor=INK, lw=2)
    ax.add_patch(stand)
    ax.add_patch(base)

    # File on the screen
    file_doc = patches.Rectangle((8.8, 3.2), 0.9, 1.15, facecolor=CREAM, 
                                 edgecolor=INK, lw=1.5)
    ax.add_patch(file_doc)
    # File text lines
    ax.plot([8.95, 9.5], [4.1, 4.1], color=INK, lw=1.5)
    ax.plot([8.95, 9.4], [3.8, 3.8], color=INK, lw=1.5)
    ax.plot([8.95, 9.55], [3.5, 3.5], color=INK, lw=1.5)

    # Magnifying Glass inspecting the file
    mag_center_x, mag_center_y = 9.8, 4.2
    mag_r = 0.55
    # Magnifying lens glass
    mag_glass = patches.Circle((mag_center_x, mag_center_y), mag_r, 
                               facecolor=LAV, edgecolor=DEEP['lav'], lw=2.8, zorder=5)
    ax.add_patch(mag_glass)
    # Magnifying handle
    handle_len = 0.6
    hx = [mag_center_x + mag_r * np.cos(np.deg2rad(-45)), 
          mag_center_x + (mag_r + handle_len) * np.cos(np.deg2rad(-45))]
    hy = [mag_center_y + mag_r * np.sin(np.deg2rad(-45)), 
          mag_center_y + (mag_r + handle_len) * np.sin(np.deg2rad(-45))]
    ax.plot(hx, hy, color=INK, lw=4.5, solid_capstyle='round', zorder=6)

    # Antivirus checkmark inside lens
    check_x = [mag_center_x - 0.25, mag_center_x - 0.05, mag_center_x + 0.28]
    check_y = [mag_center_y, mag_center_y - 0.22, mag_center_y + 0.25]
    ax.plot(check_x, check_y, color=DEEP['green'], lw=3, zorder=7)

    # Antivirus Label & Description
    ax.text(9.6, 6.7, "Antivirus", ha='center', va='center', fontsize=16, weight='bold',
            color=INK, bbox=dict(fc='white', ec=DEEP['green'], boxstyle='round,pad=0.3', lw=1.5))
    ax.text(9.6, 0.7, "Endpoint Security:\nFile & System Scanning", ha='center', va='center', 
            fontsize=14, color=INK)

    # Save output
    save(fig, out)
