from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_computer(ax, cx, cy, w=1.2, h=0.8):
    # Monitor screen
    screen = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                    boxstyle="round,pad=0.05,rounding_size=0.08",
                                    facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(screen)
    # Inner display
    inner = patches.Rectangle((cx - w/2 + 0.12, cy - h/2 + 0.12), w - 0.24, h - 0.24,
                              facecolor="white", edgecolor=DEEP["blue"], lw=1.2, zorder=4)
    ax.add_patch(inner)
    # Lines on screen (ledger lines)
    ax.plot([cx - w/2 + 0.25, cx + w/2 - 0.25], [cy + 0.1, cy + 0.1], color=GREY, lw=1.5, zorder=5)
    ax.plot([cx - w/2 + 0.25, cx + w/2 - 0.25], [cy - 0.05, cy - 0.05], color=GREY, lw=1.5, zorder=5)
    # Stand neck
    ax.plot([cx, cx], [cy - h/2, cy - h/2 - 0.2], color=DEEP["blue"], lw=3, zorder=2)
    # Stand base
    ax.plot([cx - 0.35, cx + 0.35], [cy - h/2 - 0.2, cy - h/2 - 0.2], color=DEEP["blue"], lw=3, solid_capstyle="round", zorder=2)

def draw_lock(ax, cx, cy, s=0.32):
    # Shackle
    shackle = patches.Arc((cx, cy + s*0.4), s*0.75, s*0.85, theta1=0, theta2=180,
                          edgecolor=DEEP["orange"], lw=2.5, zorder=5)
    ax.add_patch(shackle)
    # Body
    body = patches.Rectangle((cx - s*0.45, cy - s*0.45), s*0.9, s*0.75,
                             facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2, zorder=6)
    ax.add_patch(body)
    # Keyhole
    ax.plot([cx, cx], [cy - s*0.2, cy - 0.02], color="white", lw=2, zorder=7)

def draw_magnifier(ax, cx, cy, r=0.45):
    # Glass circle
    circle = patches.Circle((cx, cy), r, facecolor=LAV, edgecolor=DEEP["lav"], lw=3, zorder=6)
    ax.add_patch(circle)
    # Inner reflection arc
    inner_arc = patches.Arc((cx, cy), r*1.4, r*1.4, angle=45, theta1=50, theta2=110,
                            edgecolor="white", lw=2.5, zorder=7)
    ax.add_patch(inner_arc)
    # Handle pointing down-right
    hx1 = cx + r * np.cos(-np.pi/4)
    hy1 = cy + r * np.sin(-np.pi/4)
    hx2 = hx1 + 0.5 * np.cos(-np.pi/4)
    hy2 = hy1 + 0.5 * np.sin(-np.pi/4)
    ax.plot([hx1, hx2], [hy1, hy2], color=DEEP["lav"], lw=5, solid_capstyle="round", zorder=5)

def draw(out):
    fig = canvas(11, 7.8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.8)
    ax.axis("off")

    # Title
    ax.text(5.5, 7.3, "Blockchain in Accounting", fontsize=18, fontweight="bold",
            color=INK, ha="center", va="center")

    # Top Section: Shared Distributed Ledger
    pc_xs = [2.2, 5.5, 8.8]
    pc_y = 5.8
    for x in pc_xs:
        draw_computer(ax, x, pc_y)

    # Network connections between computers
    ax.plot([pc_xs[0] + 0.7, pc_xs[1] - 0.7], [pc_y, pc_y], color=DEEP["blue"], lw=2, ls="--", zorder=1)
    ax.plot([pc_xs[1] + 0.7, pc_xs[2] - 0.7], [pc_y, pc_y], color=DEEP["blue"], lw=2, ls="--", zorder=1)
    
    # Label for distributed ledger
    ax.text(5.5, 6.6, "Shared Distributed Ledger", fontsize=15, fontweight="bold",
            color=DEEP["blue"], ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=2))

    # Network connectors down to blockchain
    for x in pc_xs:
        ax.annotate("", xy=(x, 4.15), xytext=(x, 4.7),
                    arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=1.8, ls=":"))

    # Horizontal chain of three square blocks
    block_xs = [2.2, 5.5, 8.8]
    block_y = 3.1
    side = 1.9

    block_data = [
        {"title": "Block 1", "tx": "Transaction A", "has_lock": True},
        {"title": "Block 2", "tx": "Transaction B", "has_lock": True},
        {"title": "Block 3", "tx": "Transaction C", "has_lock": True}
    ]

    for x, data in zip(block_xs, block_data):
        rect = patches.FancyBboxPatch((x - side/2, block_y - side/2), side, side,
                                      boxstyle="round,pad=0.05,rounding_size=0.1",
                                      facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5, zorder=3)
        ax.add_patch(rect)
        
        # Block title
        ax.text(x, block_y + 0.58, data["title"], fontsize=15, fontweight="bold",
                color=INK, ha="center", va="center", zorder=4)
        
        # Lock icon
        if data["has_lock"]:
            draw_lock(ax, x, block_y + 0.12, s=0.34)
        
        # Transaction label
        ax.text(x, block_y - 0.48, data["tx"], fontsize=14,
                color=INK, ha="center", va="center", zorder=4)

    # Horizontal arrows linking the blocks
    for i in range(len(block_xs) - 1):
        x_start = block_xs[i] + side/2 + 0.05
        x_end = block_xs[i+1] - side/2 - 0.05
        ax.annotate("", xy=(x_end, block_y), xytext=(x_start, block_y),
                    arrowprops=dict(arrowstyle="-|>", mutation_scale=20, color=DEEP["green"], lw=3.5))

    # Auditor section: completely clear of text box
    aud_center_x = 2.0
    aud_center_y = 0.95
    draw_magnifier(ax, aud_center_x, aud_center_y, r=0.42)

    # Text label "Auditor" next to magnifier
    ax.text(aud_center_x + 0.85, aud_center_y, "Auditor", fontsize=16, fontweight="bold",
            color=DEEP["lav"], ha="left", va="center")

    # Sight arrow from magnifier pointing up toward the chain
    ax.annotate("", xy=(3.0, 2.0), xytext=(aud_center_x + 0.35, aud_center_y + 0.45),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=2.2, ls="--"))

    # Verification / Immutable audit trail box clearly placed to the right
    ax.text(7.2, 0.95, "Real-time Verification & Immutable Audit Trail",
            fontsize=14.5, style="italic", color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.5", lw=1.5))

    save(fig, out)
