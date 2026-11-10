from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title & Equation Header
    ax.text(5.5, 7.0, "THE ACCOUNTING EQUATION", ha="center", va="center", 
            fontsize=18, weight="bold", color=INK)
    ax.text(5.5, 6.35, "ASSETS  =  CAPITAL  +  LIABILITIES", ha="center", va="center", 
            fontsize=16, weight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.4", fc=CREAM, ec=DEEP["blue"], lw=1.5))

    # Scale Geometry
    cx, base_y, pivot_y = 5.5, 1.0, 5.0
    beam_w = 3.6  # half width
    left_x, right_x = cx - beam_w, cx + beam_w
    pan_y = 1.8   # pans at equal level (balanced)

    # Base & Central Pillar
    base = patches.Polygon([[cx - 1.5, base_y], [cx + 1.5, base_y], 
                            [cx + 0.8, base_y + 0.35], [cx - 0.8, base_y + 0.35]], 
                           closed=True, fc=GREY, ec=INK, lw=1.8)
    ax.add_patch(base)
    ax.plot([cx, cx], [base_y + 0.35, pivot_y], color=INK, lw=4, solid_capstyle="round")

    # Fulcrum & Pointer
    fulcrum = patches.Polygon([[cx - 0.35, pivot_y - 0.3], [cx + 0.35, pivot_y - 0.3], 
                              [cx, pivot_y + 0.1]], closed=True, fc=INK, ec=INK)
    ax.add_patch(fulcrum)
    # Balanced vertical pointer
    ax.plot([cx, cx], [pivot_y, pivot_y + 0.7], color=DEEP["orange"], lw=2.5)

    # Horizontal Beam
    ax.plot([left_x, right_x], [pivot_y, pivot_y], color=INK, lw=4, solid_capstyle="round")
    ax.plot(cx, pivot_y, "o", color=INK, markersize=8)

    # Block dimensions (substantially wider and taller so 14pt text fits comfortably)
    w_block = 2.6
    h_sub = 1.05
    h_assets = 2 * h_sub  # 2.10

    # Strings/Chains holding pans (spread wide enough to clear the block)
    pan_span = 1.5
    for px in [left_x, right_x]:
        ax.plot([px, px - pan_span], [pivot_y, pan_y + 0.25], color=INK, lw=1.5)
        ax.plot([px, px + pan_span], [pivot_y, pan_y + 0.25], color=INK, lw=1.5)
        # Pan structure
        pan_arc = patches.Arc((px, pan_y + 0.25), pan_span * 2, 0.75, angle=0, theta1=180, theta2=360, color=INK, lw=2.2)
        ax.add_patch(pan_arc)
        ax.plot([px - pan_span, px + pan_span], [pan_y + 0.25, pan_y + 0.25], color=INK, lw=2.2)

    # Left Pan: Large Gold Block (ASSETS)
    left_box = patches.Rectangle((left_x - w_block/2, pan_y + 0.25), w_block, h_assets,
                                 facecolor=CREAM, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(left_box)

    ax.text(left_x, pan_y + 0.25 + h_assets * 0.65, "ASSETS", ha="center", va="center", 
            fontsize=16, weight="bold", color=INK, zorder=4)
    ax.text(left_x, pan_y + 0.25 + h_assets * 0.35, "(What the business\nowns)", 
            ha="center", va="center", fontsize=14, color=INK, zorder=4)

    # Right Pan: Bottom block (LIABILITIES)
    liab_box = patches.Rectangle((right_x - w_block/2, pan_y + 0.25), w_block, h_sub,
                                 facecolor=PINK, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(liab_box)
    ax.text(right_x, pan_y + 0.25 + h_sub * 0.68, "LIABILITIES", ha="center", va="center", 
            fontsize=15, weight="bold", color=INK, zorder=4)
    ax.text(right_x, pan_y + 0.25 + h_sub * 0.28, "(Outsiders' claims)", ha="center", va="center", 
            fontsize=14, color=INK, zorder=4)

    # Right Pan: Top block (CAPITAL)
    cap_box = patches.Rectangle((right_x - w_block/2, pan_y + 0.25 + h_sub), w_block, h_sub,
                                facecolor=BLUE, edgecolor=INK, lw=2, zorder=3)
    ax.add_patch(cap_box)
    ax.text(right_x, pan_y + 0.25 + h_sub + h_sub * 0.68, "CAPITAL", ha="center", va="center", 
            fontsize=15, weight="bold", color=INK, zorder=4)
    ax.text(right_x, pan_y + 0.25 + h_sub + h_sub * 0.28, "(Owner's claim)", ha="center", va="center", 
            fontsize=14, color=INK, zorder=4)

    # Subtitle / Footer Note
    ax.text(5.5, 0.45, "The scale is perfectly balanced: Total Resources = Total Claims", 
            ha="center", va="center", fontsize=14, style="italic", color=INK)

    save(fig, out)
