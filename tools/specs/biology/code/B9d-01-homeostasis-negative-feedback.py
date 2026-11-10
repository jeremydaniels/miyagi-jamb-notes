from style import *
import numpy as np
import matplotlib.patches as patches
import math

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Center band: Normal Range / Set Point
    band_y0 = 5.0
    band_h = 1.0
    band_rect = patches.FancyBboxPatch((1.0, band_y0), 10.0, band_h,
                                      boxstyle="round,pad=0.08,rounding_size=0.2",
                                      fc=CREAM, ec=DEEP["green"], lw=2.5, zorder=2)
    ax.add_patch(band_rect)

    # Wavy set point line inside the band
    x_wave = np.linspace(1.5, 10.5, 200)
    y_wave = band_y0 + band_h/2.0 + 0.12 * np.sin(2 * np.pi * (x_wave - 1.5) / 2.2)
    ax.plot(x_wave, y_wave, color=DEEP["green"], lw=2.0, alpha=0.7, linestyle="--", zorder=3)

    ax.text(6.0, band_y0 + band_h/2.0, "Normal value (set point) / Normal range",
            ha="center", va="center", fontsize=15, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["green"], lw=1.5), zorder=4)

    # Helpers for icons
    def draw_sensor_icon(cx, cy, col):
        # Eye-like sensor
        t = np.linspace(0, np.pi, 50)
        x_eye = cx + 0.3 * np.cos(t)
        y_top = cy + 0.2 * np.sin(t)
        y_bot = cy - 0.2 * np.sin(t)
        ax.plot(x_eye, y_top, color=col, lw=2, zorder=5)
        ax.plot(x_eye, y_bot, color=col, lw=2, zorder=5)
        ax.add_patch(patches.Circle((cx, cy), 0.08, color=col, zorder=5))

    def draw_brain_icon(cx, cy, col):
        # Simplified brain
        c1 = patches.Circle((cx - 0.15, cy), 0.2, fill=False, ec=col, lw=2, zorder=5)
        c2 = patches.Circle((cx + 0.15, cy), 0.2, fill=False, ec=col, lw=2, zorder=5)
        ax.add_patch(c1); ax.add_patch(c2)
        ax.plot([cx-0.15, cx+0.15], [cy-0.1, cy-0.1], color=col, lw=2, zorder=5)

    def draw_effector_icon(cx, cy, col):
        # Muscle / droplet gland
        ax.plot([cx - 0.2, cx + 0.2], [cy - 0.1, cy - 0.1], color=col, lw=2, zorder=5)
        ax.add_patch(patches.Circle((cx, cy + 0.05), 0.15, fill=False, ec=col, lw=2, zorder=5))

    # Helper for boxes
    def draw_box(cx, cy, title, subtitle, col_bg, col_edge, icon_type):
        w, h = 3.0, 1.25
        box = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                    boxstyle="round,pad=0.05,rounding_size=0.15",
                                    fc=col_bg, ec=col_edge, lw=2.0, zorder=3)
        ax.add_patch(box)
        if icon_type == "sensor":
            draw_sensor_icon(cx, cy + 0.35, col_edge)
        elif icon_type == "brain":
            draw_brain_icon(cx, cy + 0.35, col_edge)
        elif icon_type == "effector":
            draw_effector_icon(cx, cy + 0.35, col_edge)
        
        ax.text(cx, cy - 0.05, title, ha="center", va="center", fontsize=14, weight="bold", color=INK, zorder=6)
        if subtitle:
            ax.text(cx, cy - 0.35, subtitle, ha="center", va="center", fontsize=14, color=INK, zorder=6)

    # Helper for curved flow arrows
    def draw_arrow(start, end, rad, col):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.8,
                                    mutation_scale=20,
                                    connectionstyle=f"arc3,rad={rad}"),
                    zorder=2)

    # ------------------ TOP LOOP (RISE - ORANGE) ------------------
    # Rise out of the band
    x_rise = np.linspace(1.5, 2.5, 50)
    y_rise = band_y0 + band_h/2.0 + 0.12 * np.sin(2 * np.pi * (x_rise - 1.5) / 2.2) + 1.2 * (x_rise - 1.5)
    ax.plot(x_rise, y_rise, color=DEEP["orange"], lw=2.5, zorder=3)

    # Arrow from normal to rise
    draw_arrow((2.5, 7.3), (2.8, 8.5), -0.1, DEEP["orange"])

    ax.text(1.8, 7.5, "Rise above normal",
            fontsize=14, weight="bold", color=DEEP["orange"], ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["orange"], lw=1.2), zorder=4)

    # Top boxes:
    b1_x, b1_y = 3.2, 9.4
    draw_box(b1_x, b1_y, "Receptors", "detect change", ORANGE, DEEP["orange"], "sensor")
    
    b2_x, b2_y = 6.2, 9.8
    draw_box(b2_x, b2_y, "Control centre", "", ORANGE, DEEP["orange"], "brain")
    
    b3_x, b3_y = 9.2, 9.4
    draw_box(b3_x, b3_y, "Effectors", "", ORANGE, DEEP["orange"], "effector")

    # Arrows for Top Loop
    draw_arrow((b1_x + 1.5, b1_y + 0.1), (b2_x - 1.5, b2_y + 0.1), -0.15, DEEP["orange"])
    draw_arrow((b2_x + 1.5, b2_y + 0.1), (b3_x - 1.5, b3_y + 0.1), -0.15, DEEP["orange"])
    draw_arrow((b3_x + 0.5, b3_y - 0.7), (9.5, band_y0 + band_h + 0.1), -0.25, DEEP["orange"])

    ax.text(10.6, 7.8, "Corrective\nresponse", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["orange"],
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["orange"], lw=1.2), zorder=4)
    ax.text(9.5, 6.5, "Return to normal", ha="center", va="center", fontsize=14, color=DEEP["orange"],
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=4)

    # ------------------ BOTTOM LOOP (FALL - BLUE) ------------------
    # Fall out of the band
    x_fall = np.linspace(1.5, 2.5, 50)
    y_fall = band_y0 + band_h/2.0 + 0.12 * np.sin(2 * np.pi * (x_fall - 1.5) / 2.2) - 1.2 * (x_fall - 1.5)
    ax.plot(x_fall, y_fall, color=DEEP["blue"], lw=2.5, zorder=3)

    # Arrow from normal to fall
    draw_arrow((2.5, 3.7), (2.8, 2.5), 0.1, DEEP["blue"])

    ax.text(1.8, 3.5, "Fall below normal",
            fontsize=14, weight="bold", color=DEEP["blue"], ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["blue"], lw=1.2), zorder=4)

    # Bottom boxes:
    bb1_x, bb1_y = 3.2, 1.6
    draw_box(bb1_x, bb1_y, "Receptors", "detect change", BLUE, DEEP["blue"], "sensor")
    
    bb2_x, bb2_y = 6.2, 1.2
    draw_box(bb2_x, bb2_y, "Control centre", "", BLUE, DEEP["blue"], "brain")
    
    bb3_x, bb3_y = 9.2, 1.6
    draw_box(bb3_x, bb3_y, "Effectors", "", BLUE, DEEP["blue"], "effector")

    # Arrows for Bottom Loop
    draw_arrow((bb1_x + 1.5, bb1_y - 0.1), (bb2_x - 1.5, bb2_y - 0.1), 0.15, DEEP["blue"])
    draw_arrow((bb2_x + 1.5, bb2_y - 0.1), (bb3_x - 1.5, bb3_y - 0.1), 0.15, DEEP["blue"])
    draw_arrow((bb3_x + 0.5, bb3_y + 0.7), (9.5, band_y0 - 0.1), 0.25, DEEP["blue"])

    ax.text(10.6, 3.2, "Corrective\nresponse", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["blue"], lw=1.2), zorder=4)
    ax.text(9.5, 4.5, "Return to normal", ha="center", va="center", fontsize=14, color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"), zorder=4)

    save(fig, out)
