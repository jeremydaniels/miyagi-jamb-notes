from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(10, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Helper function to draw a battery
    def draw_battery(cx, cy, long_left=True):
        # long plate: length 1.0, thin; short plate: length 0.5, thick
        dx = 0.18
        if long_left:
            # Long plate on left (+), short on right (-)
            ax.plot([cx - dx, cx - dx], [cy - 0.5, cy + 0.5], color=INK, lw=2.5)
            ax.plot([cx + dx, cx + dx], [cy - 0.28, cy + 0.28], color=INK, lw=5)
            ax.text(cx - dx - 0.35, cy, '+', fontsize=16, ha='center', va='center', color=INK, fontweight='bold')
            ax.text(cx + dx + 0.35, cy, '−', fontsize=16, ha='center', va='center', color=INK, fontweight='bold')
        else:
            # Short plate on left (-), long on right (+)
            ax.plot([cx - dx, cx - dx], [cy - 0.28, cy + 0.28], color=INK, lw=5)
            ax.plot([cx + dx, cx + dx], [cy - 0.5, cy + 0.5], color=INK, lw=2.5)
            ax.text(cx - dx - 0.35, cy, '−', fontsize=16, ha='center', va='center', color=INK, fontweight='bold')
            ax.text(cx + dx + 0.35, cy, '+', fontsize=16, ha='center', va='center', color=INK, fontweight='bold')

    # Diagram coordinates
    # Top diagram center y: 8.2 (diode: 8.7, battery: 6.7)
    # Bottom diagram center y: 3.2 (diode: 3.7, battery: 1.7)

    def draw_diode_setup(y_diode, y_batt, is_forward):
        # Diode block bounds
        x_left = 3.0
        x_right = 7.0
        w = x_right - x_left
        h = 1.4
        y_bot = y_diode - h / 2.0
        mid_x = (x_left + x_right) / 2.0

        # Depletion layer width
        d_w = 0.35 if is_forward else 1.5
        d_left = mid_x - d_w / 2.0
        d_right = mid_x + d_w / 2.0

        # p-region (left)
        p_rect = patches.Rectangle((x_left, y_bot), d_left - x_left, h,
                                   facecolor=LAV, edgecolor='none')
        # n-region (right)
        n_rect = patches.Rectangle((d_right, y_bot), x_right - d_right, h,
                                   facecolor=CREAM, edgecolor='none')
        # depletion layer
        dep_rect = patches.Rectangle((d_left, y_bot), d_w, h,
                                     facecolor=GREY, edgecolor='none', alpha=0.5)

        ax.add_patch(p_rect)
        ax.add_patch(n_rect)
        ax.add_patch(dep_rect)

        # Diode border and junction dashed line
        ax.plot([x_left, x_right, x_right, x_left, x_left],
                [y_bot, y_bot, y_bot + h, y_bot + h, y_bot],
                color=INK, lw=2)
        ax.plot([mid_x, mid_x], [y_bot, y_bot + h], color=INK, lw=1.2, ls='--')

        # Depletion boundaries
        ax.plot([d_left, d_left], [y_bot, y_bot + h], color=INK, lw=1.2, ls=':')
        ax.plot([d_right, d_right], [y_bot, y_bot + h], color=INK, lw=1.2, ls=':')

        # Labels for p and n
        ax.text((x_left + d_left) / 2.0, y_diode, 'p-type', fontsize=15,
                ha='center', va='center', fontweight='bold', color=INK)
        ax.text((d_right + x_right) / 2.0, y_diode, 'n-type', fontsize=15,
                ha='center', va='center', fontweight='bold', color=INK)

        # Depletion layer annotation
        dep_text = 'Narrow Depletion Layer' if is_forward else 'Wide Depletion Layer'
        ax.annotate(dep_text, xy=(mid_x, y_bot + h), xytext=(mid_x, y_bot + h + 0.45),
                    fontsize=14, ha='center', va='bottom', color=INK,
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

        # Circuit wiring
        wire_left = 1.8
        wire_right = 8.2

        # Left loop
        ax.plot([x_left, wire_left, wire_left, 4.4],
                [y_diode, y_diode, y_batt, y_batt], color=INK, lw=2)
        # Right loop
        ax.plot([5.6, wire_right, wire_right, x_right],
                [y_batt, y_batt, y_diode, y_diode], color=INK, lw=2)

        # Battery
        draw_battery(5.0, y_batt, long_left=is_forward)

        # Current flow indication
        if is_forward:
            # Flowing current arrows (clockwise: left up, top right, right down)
            # Arrow on top wire entering p-region
            ax.annotate('', xy=(2.7, y_diode), xytext=(2.0, y_diode),
                        arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=3, mutation_scale=18))
            ax.text(2.35, y_diode + 0.28, 'Current', fontsize=14, ha='center', va='bottom',
                    color=DEEP['green'], fontweight='bold')

            # Arrow on bottom wire returning to battery
            ax.annotate('', xy=(3.0, y_batt), xytext=(3.8, y_batt),
                        arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=3, mutation_scale=18))
            
            # Label near circuit
            ax.text(wire_right + 0.3, (y_diode + y_batt) / 2.0, 'Current\nFlows',
                    fontsize=14, ha='left', va='center', color=DEEP['green'], fontweight='bold')
        else:
            # Crossed out arrow indicating no current
            ax.annotate('', xy=(2.0, y_diode), xytext=(2.7, y_diode),
                        arrowprops=dict(arrowstyle="->", color=GREY, lw=2.5, mutation_scale=18))
            # Red cross over arrow
            cx_ar, cy_ar = 2.35, y_diode
            ax.plot([cx_ar - 0.2, cx_ar + 0.2], [cy_ar - 0.2, cy_ar + 0.2], color=DEEP['pink'], lw=3)
            ax.plot([cx_ar - 0.2, cx_ar + 0.2], [cy_ar + 0.2, cy_ar - 0.2], color=DEEP['pink'], lw=3)
            ax.text(cx_ar, y_diode + 0.28, 'No Current', fontsize=14, ha='center', va='bottom',
                    color=DEEP['pink'], fontweight='bold')

            ax.text(wire_right + 0.3, (y_diode + y_batt) / 2.0, 'No Current\nFlow',
                    fontsize=14, ha='left', va='center', color=DEEP['pink'], fontweight='bold')

    # Draw Section Titles
    ax.text(5.0, 10.3, "Forward Bias", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    draw_diode_setup(8.5, 6.7, is_forward=True)

    # Dividing separator
    ax.plot([1.0, 9.0], [5.6, 5.6], color=GREY, lw=1.2, ls=':')

    ax.text(5.0, 5.0, "Reverse Bias", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    draw_diode_setup(3.3, 1.5, is_forward=False)

    save(fig, out)
