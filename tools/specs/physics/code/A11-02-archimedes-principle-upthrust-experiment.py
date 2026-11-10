import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    # Stand / ceiling support line
    ax.plot([0.8, 11.2], [8.0, 8.0], color=INK, lw=3)
    for x in np.linspace(1.0, 11.0, 25):
        ax.plot([x, x + 0.25], [8.0, 8.25], color=GREY, lw=1.5)

    def draw_spring_balance(cx, reading_val):
        # Top ring/hook
        ring = patches.Circle((cx, 7.7), 0.15, fill=False, edgecolor=INK, lw=2)
        ax.add_patch(ring)
        ax.plot([cx, cx], [8.0, 7.85], color=INK, lw=2)
        
        # Balance body
        body_w, body_h = 1.0, 2.4
        body = patches.Rectangle((cx - body_w/2, 5.15), body_w, body_h,
                                 facecolor=CREAM, edgecolor=INK, lw=2, zorder=3)
        ax.add_patch(body)
        
        # Balance scale slot
        slot = patches.Rectangle((cx - 0.2, 5.4), 0.4, 1.9,
                                 facecolor='white', edgecolor=GREY, lw=1.2, zorder=4)
        ax.add_patch(slot)
        
        # Scale tick marks
        for y in np.linspace(5.6, 7.0, 8):
            ax.plot([cx - 0.15, cx - 0.05], [y, y], color=GREY, lw=1, zorder=5)
            
        # Indicator line depending on reading
        # 50 N is lower down (more stretch), 30 N is higher
        indic_y = 5.85 if reading_val == 50 else 6.35
        ax.plot([cx - 0.18, cx + 0.18], [indic_y, indic_y], color=DEEP["pink"], lw=2.5, zorder=6)

        # Reading label beside scale
        ax.text(cx + 0.6, indic_y, f"{reading_val} N", fontsize=15, fontweight='bold',
                color=DEEP["pink"], va='center', ha='left',
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2', lw=1))

        # Bottom hook
        ax.plot([cx, cx], [5.15, 4.8], color=INK, lw=2)
        hook = patches.Arc((cx, 4.7), 0.2, 0.2, angle=0, theta1=90, theta2=330, edgecolor=INK, lw=2)
        ax.add_patch(hook)
        
        # String from hook to sphere
        ax.plot([cx, cx], [4.6, 3.4], color=INK, lw=1.5, ls='--')

    # === Scenario A: In Air (cx = 3.0) ===
    cx_a = 3.0
    cy_sphere_a = 2.7
    r_sphere = 0.7

    draw_spring_balance(cx_a, 50)
    
    # Sphere A
    sphere_a = patches.Circle((cx_a, cy_sphere_a), r_sphere,
                              facecolor=GREY, edgecolor=INK, lw=2.5, zorder=4)
    ax.add_patch(sphere_a)

    ax.text(cx_a, 0.7, "Scenario A: In Air\n(Reading = 50 N)", fontsize=16,
            fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.4', lw=1.2))

    # === Scenario B: In Liquid (cx = 8.8) ===
    cx_b = 8.8
    cy_sphere_b = 2.7

    # Beaker with liquid
    beaker_w, beaker_h = 3.0, 3.4
    beaker_x = cx_b - beaker_w/2
    beaker_y = 1.3
    
    # Liquid
    liquid = patches.Rectangle((beaker_x + 0.08, beaker_y), beaker_w - 0.16, 2.6,
                               facecolor=BLUE, alpha=0.45, edgecolor=None, zorder=2)
    ax.add_patch(liquid)
    
    # Liquid surface line
    ax.plot([beaker_x + 0.08, beaker_x + beaker_w - 0.08], [beaker_y + 2.6, beaker_y + 2.6],
            color=DEEP["blue"], lw=2.5, zorder=3)
    
    # Beaker glass outline
    ax.plot([beaker_x, beaker_x, beaker_x + beaker_w, beaker_x + beaker_w],
            [beaker_y + beaker_h, beaker_y, beaker_y, beaker_y + beaker_h],
            color=INK, lw=2.5, zorder=5)

    draw_spring_balance(cx_b, 30)

    # Sphere B (submerged)
    sphere_b = patches.Circle((cx_b, cy_sphere_b), r_sphere,
                              facecolor=GREY, edgecolor=INK, lw=2.5, zorder=4)
    ax.add_patch(sphere_b)

    # Force arrows on submerged sphere
    # Upthrust U = 20 N (upward arrow)
    ax.annotate('', xy=(cx_b, cy_sphere_b + 1.25), xytext=(cx_b, cy_sphere_b),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=3.0, mutation_scale=20),
                zorder=7)
    ax.text(cx_b - 0.15, cy_sphere_b + 0.85, "Upthrust (U) = 20 N", fontsize=14,
            fontweight='bold', color=DEEP["green"], ha='right', va='center',
            bbox=dict(fc='white', ec=DEEP["green"], boxstyle='round,pad=0.25', lw=1.2), zorder=8)

    # Real Weight W = 50 N (downward arrow)
    ax.annotate('', xy=(cx_b, cy_sphere_b - 1.5), xytext=(cx_b, cy_sphere_b),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["pink"], lw=3.0, mutation_scale=20),
                zorder=7)
    ax.text(cx_b + 0.2, cy_sphere_b - 1.1, "Real Weight (W) = 50 N", fontsize=14,
            fontweight='bold', color=DEEP["pink"], ha='left', va='center',
            bbox=dict(fc='white', ec=DEEP["pink"], boxstyle='round,pad=0.25', lw=1.2), zorder=8)

    ax.text(cx_b, 0.7, "Scenario B: Submerged in Liquid\n(Reading = 30 N)", fontsize=16,
            fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.4', lw=1.2))

    save(fig, out)
