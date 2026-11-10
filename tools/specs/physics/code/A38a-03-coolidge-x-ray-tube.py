from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-0.8, 14.8)
    ax.set_ylim(-0.8, 10.2)
    ax.axis('off')

    # Title
    ax.text(7.0, 9.6, "Coolidge X-ray Tube", ha='center', va='center',
            fontsize=18, weight='bold', color=INK)

    # Simplified glass envelope
    glass = patches.FancyBboxPatch((3.0, 3.6), 7.2, 4.0, boxstyle="round,pad=0.5",
                                  ec=DEEP["blue"], fc=CREAM, lw=2.2, alpha=0.35)
    ax.add_patch(glass)

    # Left & right tube necks
    ax.fill_between([1.4, 3.5], [4.8, 4.8], [6.4, 6.4], color=CREAM, alpha=0.35)
    ax.plot([1.4, 3.5], [4.8, 4.8], color=DEEP["blue"], lw=2.2)
    ax.plot([1.4, 3.5], [6.4, 6.4], color=DEEP["blue"], lw=2.2)

    ax.fill_between([9.8, 12.0], [4.8, 4.8], [6.4, 6.4], color=CREAM, alpha=0.35)
    ax.plot([9.8, 12.0], [4.8, 4.8], color=DEEP["blue"], lw=2.2)
    ax.plot([9.8, 12.0], [6.4, 6.4], color=DEEP["blue"], lw=2.2)

    # Evacuated tube annotation
    ax.text(3.8, 7.4, "Evacuated glass tube", fontsize=14, color=GREY, style='italic',
            bbox=dict(fc='white', ec='none', pad=2))

    # --- LEFT SIDE: CATHODE & FILAMENT ---
    # Focusing cup
    cup = patches.Polygon([[3.0, 6.2], [3.3, 6.2], [3.7, 6.0], [3.7, 5.2], [3.3, 5.0], [3.0, 5.0]],
                          closed=True, ec=INK, fc=GREY, lw=1.5)
    ax.add_patch(cup)

    # Filament coil sketch
    fil_x = [3.4, 3.5, 3.6, 3.5, 3.6, 3.5, 3.4]
    fil_y = [5.9, 5.8, 5.7, 5.6, 5.5, 5.4, 5.3]
    ax.plot(fil_x, fil_y, color=DEEP["orange"], lw=3)

    # Filament leads
    ax.plot([1.1, 3.4], [5.9, 5.9], color=INK, lw=2)
    ax.plot([1.1, 3.4], [5.3, 5.3], color=INK, lw=2)

    # Low voltage supply circuit
    ax.plot([1.1, 0.3, 0.3, 1.1], [5.9, 5.9, 5.3, 5.3], color=INK, lw=2)
    # Battery symbol on low voltage supply
    ax.plot([0.3, 0.3], [5.75, 5.45], color=INK, lw=2)
    ax.plot([0.0, 0.6], [5.75, 5.75], color=INK, lw=3)
    ax.plot([0.15, 0.45], [5.45, 5.45], color=INK, lw=2)
    ax.text(0.3, 4.7, "Low voltage\nfilament supply", ha='center', va='top',
            fontsize=14, color=INK, bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.2"))

    ax.annotate("Heated cathode\nfilament", xy=(3.5, 5.6), xytext=(2.2, 8.2),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.2"))

    # --- RIGHT SIDE: ANODE & TARGET ---
    # Copper block with angled face
    copper_poly = patches.Polygon([[8.2, 6.2], [11.2, 6.2], [11.2, 5.0], [7.6, 5.0]],
                                  closed=True, ec=INK, fc=ORANGE, lw=1.8)
    ax.add_patch(copper_poly)

    # Angled tungsten target embedded in copper
    tungsten_poly = patches.Polygon([[7.7, 5.2], [8.1, 6.0], [8.25, 5.9], [7.85, 5.1]],
                                    closed=True, ec=INK, fc=BLUE, lw=1.5)
    ax.add_patch(tungsten_poly)

    # Cooling fins attached to copper rod
    for fin_x in [11.4, 11.8, 12.2, 12.6]:
        ax.plot([fin_x, fin_x], [4.4, 6.8], color=INK, lw=2.5)
    ax.plot([11.2, 12.7], [5.6, 5.6], color=INK, lw=3)

    ax.annotate("Tungsten target", xy=(7.9, 5.6), xytext=(6.8, 8.4),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.2"))

    ax.annotate("Copper anode block", xy=(9.5, 6.2), xytext=(9.8, 8.0),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.2"))

    ax.annotate("Cooling fins", xy=(12.0, 6.8), xytext=(12.7, 8.2),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.2"))

    # --- ELECTRON BEAM ---
    beam = patches.FancyArrow(3.8, 5.6, 3.6, 0.0, width=0.18, length_includes_head=True,
                             head_width=0.45, head_length=0.4, fc=PINK, ec=DEEP["pink"], lw=1.5)
    ax.add_patch(beam)
    ax.text(5.5, 6.1, "accelerating electrons", ha='center', va='bottom',
            fontsize=15, color=DEEP["pink"], weight='bold',
            bbox=dict(fc='white', ec='none', pad=2))

    # --- EMITTED X-RAYS (Downwards & slightly rightwards to avoid HV box) ---
    def draw_wavy_ray(start_x, start_y, angle_deg, length, waves=4, amp=0.12):
        rad = np.deg2rad(angle_deg)
        t = np.linspace(0, length, 120)
        w = amp * np.sin(2 * np.pi * waves * t / length)
        x = start_x + t * np.cos(rad) - w * np.sin(rad)
        y = start_y + t * np.sin(rad) + w * np.cos(rad)
        ax.plot(x, y, color=DEEP["green"], lw=2.2)
        ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[-4], y[-4]),
                    arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.2))

    # Angled target normal points downwards and to the left/straight down
    # Route X-rays downwards and slightly rightwards: angles around -70 to -85 deg
    draw_wavy_ray(7.75, 5.15, -78, 2.6, waves=4.0)
    draw_wavy_ray(7.90, 5.30, -68, 2.7, waves=4.0)
    draw_wavy_ray(8.05, 5.45, -58, 2.8, waves=4.0)

    ax.text(8.8, 2.8, "X-rays", ha='center', va='center',
            fontsize=16, color=DEEP["green"], weight='bold',
            bbox=dict(fc='white', ec=GREY, boxstyle="round,pad=0.3"))

    # --- HIGH VOLTAGE POWER SUPPLY ---
    # Routed clearly below all X-rays with generous clearance
    # Cathode wire down
    ax.plot([2.3, 2.3, 4.4], [5.3, 0.8, 0.8], color=INK, lw=1.8)
    # Anode wire down
    ax.plot([10.5, 10.5, 7.2], [5.0, 0.8, 0.8], color=INK, lw=1.8)

    # High voltage supply box shifted left to x=[4.4, 7.2], y=[0.1, 1.5]
    hv_box = patches.FancyBboxPatch((4.4, 0.1), 2.8, 1.4, boxstyle="round,pad=0.15",
                                   ec=DEEP["blue"], fc='white', lw=2)
    ax.add_patch(hv_box)
    ax.text(5.8, 0.8, "High voltage\npower supply", ha='center', va='center',
            fontsize=14, color=INK, weight='bold')

    # Polarities on connection wires
    ax.text(3.9, 1.15, "−", fontsize=20, color=DEEP["blue"], weight='bold', ha='center')
    ax.text(7.6, 1.15, "+", fontsize=20, color=DEEP["orange"], weight='bold', ha='center')

    # Cathode and Anode main labels
    ax.text(2.3, 4.6, "Cathode (−)", fontsize=14, color=INK, ha='center',
            bbox=dict(fc='white', ec='none', pad=2))
    ax.text(10.5, 4.2, "Anode (+)", fontsize=14, color=INK, ha='center',
            bbox=dict(fc='white', ec='none', pad=2))

    save(fig, out)
