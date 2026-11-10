from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Color definitions
    HG_COLOR = "#B0B7BD"       # Mercury silvery-grey
    HG_DARK = "#7E8890"        # Darker mercury border/fill
    LIQUID_COLOR = "#6BA4B8"   # Liquid layer (blue-green tone)
    GLASS_BORDER = INK

    # Trough parameters
    trough_x = 1.0
    trough_y = 0.8
    trough_w = 10.0
    trough_h = 1.6
    hg_trough_level = 1.8

    # Trough mercury
    ax.fill_between([trough_x, trough_x + trough_w], trough_y, hg_trough_level, color=HG_COLOR, ec=None)
    
    # Trough outline
    ax.plot([trough_x, trough_x, trough_x + trough_w, trough_x + trough_w],
            [trough_y + trough_h, trough_y, trough_y, trough_y + trough_h],
            color=GLASS_BORDER, lw=2.5)

    # Tube parameters
    tube_w = 0.7
    tube_top = 7.5
    tube_bottom = 1.1
    tube_centers = [3.0, 6.0, 9.0]
    
    # Heights from trough mercury surface (y = 1.8)
    # Tube 1: full atmospheric height H (height = 4.8 -> y = 6.6)
    # Tube 2: slightly dropped (height = 4.0 -> y = 5.8)
    # Tube 3: saturated vapour, final height h (height = 3.2 -> y = 5.0)
    h_level1 = 6.6
    h_level2 = 5.8
    h_level3 = 5.0
    
    # Draw tubes
    for xc in tube_centers:
        x_left = xc - tube_w / 2
        x_right = xc + tube_w / 2
        
        # Tube rounded top
        arc = patches.Arc((xc, tube_top - tube_w/2), tube_w, tube_w, angle=0, theta1=0, theta2=180,
                          color=GLASS_BORDER, lw=2)
        ax.add_patch(arc)
        # Vertical walls
        ax.plot([x_left, x_left], [tube_bottom, tube_top - tube_w/2], color=GLASS_BORDER, lw=2)
        ax.plot([x_right, x_right], [tube_bottom, tube_top - tube_w/2], color=GLASS_BORDER, lw=2)

    # Mercury in tubes
    # Tube 1:
    x1_l, x1_r = tube_centers[0] - tube_w/2, tube_centers[0] + tube_w/2
    ax.fill_between([x1_l, x1_r], tube_bottom, h_level1, color=HG_COLOR)
    ax.plot([x1_l, x1_r], [h_level1, h_level1], color=HG_DARK, lw=2)

    # Tube 2:
    x2_l, x2_r = tube_centers[1] - tube_w/2, tube_centers[1] + tube_w/2
    ax.fill_between([x2_l, x2_r], tube_bottom, h_level2, color=HG_COLOR)
    ax.plot([x2_l, x2_r], [h_level2, h_level2], color=HG_DARK, lw=2)

    # Tube 3:
    x3_l, x3_r = tube_centers[2] - tube_w/2, tube_centers[2] + tube_w/2
    ax.fill_between([x3_l, x3_r], tube_bottom, h_level3, color=HG_COLOR)
    ax.plot([x3_l, x3_r], [h_level3, h_level3], color=HG_DARK, lw=2)

    # Tube 3: thin visible layer of liquid floating on top of mercury
    liq_thickness = 0.22
    liq_rect = patches.Rectangle((x3_l, h_level3), tube_w, liq_thickness,
                                 facecolor=LIQUID_COLOR, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(liq_rect)

    # Trough mercury surface line (drawn in front of tubes)
    ax.plot([trough_x, trough_x + trough_w], [hg_trough_level, hg_trough_level], color=HG_DARK, lw=2)

    # Dashed reference lines for heights
    ax.plot([tube_centers[0], 11.2], [h_level1, h_level1], color=GREY, ls='--', lw=1.3)
    ax.plot([tube_centers[2], 11.2], [h_level3, h_level3], color=GREY, ls='--', lw=1.3)
    ax.plot([0.8, tube_centers[0]], [hg_trough_level, hg_trough_level], color=GREY, ls='--', lw=1.3)

    # Tube identifiers
    ax.text(tube_centers[0], 0.4, "Tube 1", fontsize=15, ha='center', va='center', weight='bold', color=INK)
    ax.text(tube_centers[1], 0.4, "Tube 2", fontsize=15, ha='center', va='center', weight='bold', color=INK)
    ax.text(tube_centers[2], 0.4, "Tube 3", fontsize=15, ha='center', va='center', weight='bold', color=INK)

    # Labels and Annotations

    # 1. "Torricellian vacuum"
    ax.annotate("Torricellian vacuum",
                xy=(tube_centers[0], 7.0), xytext=(tube_centers[0] - 1.2, 7.8),
                fontsize=14, color=INK, ha='center', va='bottom',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=2))

    # 2. "Unsaturated vapour"
    ax.annotate("Unsaturated vapour",
                xy=(tube_centers[1], 6.5), xytext=(tube_centers[1], 7.8),
                fontsize=14, color=INK, ha='center', va='bottom',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=2))

    # 3. "Saturated vapour"
    ax.annotate("Saturated vapour",
                xy=(tube_centers[2], 6.3), xytext=(tube_centers[2] + 1.2, 7.8),
                fontsize=14, color=INK, ha='center', va='bottom',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=2))

    # 4. "Liquid layer"
    ax.annotate("Liquid layer",
                xy=(tube_centers[2] + tube_w/2, h_level3 + liq_thickness/2),
                xytext=(tube_centers[2] + 1.4, h_level3 + 0.8),
                fontsize=14, color=INK, ha='left', va='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=2))

    # 5. "Atmospheric pressure (H)" - double arrow from mercury trough level to Tube 1 mercury top
    dim_x1 = 1.8
    ax.annotate("", xy=(dim_x1, hg_trough_level), xytext=(dim_x1, h_level1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8))
    ax.plot([dim_x1, tube_centers[0] - tube_w/2], [h_level1, h_level1], color=GREY, ls='--', lw=1.3)
    ax.text(dim_x1 - 0.2, (hg_trough_level + h_level1) / 2, "Atmospheric pressure (H)",
            fontsize=14, color=INK, ha='right', va='center',
            rotation=90, bbox=dict(fc="white", ec="none", pad=2))

    # 6. "Final height (h)" - double arrow on Tube 3
    dim_x3 = 7.7
    ax.annotate("", xy=(dim_x3, hg_trough_level), xytext=(dim_x3, h_level3),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8))
    ax.text(dim_x3 - 0.2, (hg_trough_level + h_level3) / 2, "Final height (h)",
            fontsize=14, color=INK, ha='right', va='center',
            rotation=90, bbox=dict(fc="white", ec="none", pad=2))

    # 7. "S.V.P = H - h" - difference between level 1 and level 3
    dim_x_svp = 10.6
    ax.annotate("", xy=(dim_x_svp, h_level3), xytext=(dim_x_svp, h_level1),
                arrowprops=dict(arrowstyle="<->", color=DEEP["pink"], lw=2.0))
    ax.text(dim_x_svp + 0.3, (h_level1 + h_level3) / 2, "S.V.P = H - h",
            fontsize=15, color=DEEP["pink"], ha='left', va='center', weight='bold',
            bbox=dict(fc="white", ec="none", pad=2))

    save(fig, out)
