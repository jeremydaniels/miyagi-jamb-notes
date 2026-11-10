from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1.5, 23.5)
    ax.set_ylim(-3.5, 4.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Geometry settings
    stem_y = 1.0
    stem_half_h = 0.55
    bulb_x = 0.2
    bulb_r = 1.15
    stem_left = 1.1
    stem_right = 21.8

    scale_start = 1.8   # 0 cm mark
    scale_end = 20.8    # 20 cm mark
    cm_len = (scale_end - scale_start) / 20.0
    meniscus_x = scale_start + 12.0 * cm_len  # 12 cm mark

    # 1. Outer Glass Tube (Stem)
    stem_box = patches.FancyBboxPatch(
        (stem_left, stem_y - stem_half_h),
        stem_right - stem_left,
        stem_half_h * 2,
        boxstyle="round,pad=0.04,rounding_size=0.4",
        facecolor=CREAM,
        edgecolor=INK,
        linewidth=2.0,
        zorder=1
    )
    ax.add_patch(stem_box)

    # Glass highlight inside stem
    ax.plot([stem_left + 0.4, stem_right - 0.4], [stem_y + 0.32, stem_y + 0.32],
            color='white', lw=2.5, alpha=0.9, zorder=2)

    # 2. Bulb at left end
    bulb_circle = patches.Circle(
        (bulb_x, stem_y),
        bulb_r,
        facecolor='#B0B7BD',  # Silver mercury color
        edgecolor=INK,
        linewidth=2.0,
        zorder=4
    )
    ax.add_patch(bulb_circle)

    # Bulb highlight
    bulb_hl = patches.Arc(
        (bulb_x - 0.2, stem_y + 0.2),
        1.2, 1.2,
        angle=45, theta1=60, theta2=150,
        color='white', lw=2.5, zorder=5
    )
    ax.add_patch(bulb_hl)

    # 3. Capillary Tube (bore)
    ax.plot([bulb_x + bulb_r * 0.7, stem_right - 0.3], [stem_y, stem_y],
            color=GREY, lw=1.2, linestyle='--', zorder=2)

    # Liquid thread inside capillary (red line ending at 12 cm mark)
    ax.plot([bulb_x + bulb_r * 0.5, meniscus_x], [stem_y, stem_y],
            color=DEEP["pink"], lw=4.5, solid_capstyle='round', zorder=3)

    # 4. Scale Markings ON the thermometer stem
    # Place ticks fully inside or cleanly along the stem with ample clearance to text below
    # Let ticks hang downward from bottom edge of stem, with scale baseline offset
    stem_bottom = stem_y - stem_half_h - 0.04
    tick_len_major = 0.35
    tick_len_minor = 0.20

    # Draw ticks extending downwards from the bottom edge of the glass tube
    for cm in range(21):
        x = scale_start + cm * cm_len
        ax.plot([x, x], [stem_bottom, stem_bottom - tick_len_major], color=INK, lw=1.6, zorder=3)

        # Numbers comfortably below tick ends
        if cm % 2 == 0:
            ax.text(x, stem_bottom - tick_len_major - 0.22, str(cm),
                    ha='center', va='top', fontsize=14, color=INK, zorder=6)

        # Half-cm minor ticks
        if cm < 20:
            x_mid = x + 0.5 * cm_len
            ax.plot([x_mid, x_mid], [stem_bottom, stem_bottom - tick_len_minor],
                    color=INK, lw=1.1, zorder=3)

    # Unit label "cm" well spaced at end of scale
    ax.text(scale_end + 0.65, stem_bottom - tick_len_major - 0.22, "cm",
            ha='left', va='top', fontsize=14, color=INK, fontweight='bold', zorder=6)

    # 5. Fixed points (0 °C and 100 °C)
    y_temp_label = stem_bottom - 1.65

    # 0 °C label below 0 cm mark
    ax.annotate("0 °C\n(ice point)",
                xy=(scale_start, stem_bottom - tick_len_major - 0.55),
                xytext=(scale_start, y_temp_label),
                ha='center', va='top', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    # 100 °C label below 20 cm mark
    ax.annotate("100 °C\n(steam point)",
                xy=(scale_end, stem_bottom - tick_len_major - 0.55),
                xytext=(scale_end, y_temp_label),
                ha='center', va='top', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    # 6. Meniscus at 12 cm callout
    ax.annotate("thread ends\nat 12 cm",
                xy=(meniscus_x, stem_y),
                xytext=(meniscus_x + 0.3, stem_y + 1.6),
                ha='center', va='bottom', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.6),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["pink"]))

    # 7. Labels for Bulb and Stem
    ax.annotate("silver bulb\n(mercury)",
                xy=(bulb_x, stem_y + bulb_r),
                xytext=(bulb_x - 0.2, stem_y + 1.8),
                ha='center', va='bottom', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    ax.annotate("capillary tube inside stem",
                xy=(scale_start + 4.5 * cm_len, stem_y + stem_half_h),
                xytext=(scale_start + 4.5 * cm_len, stem_y + 1.8),
                ha='center', va='bottom', fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY))

    save(fig, out)
