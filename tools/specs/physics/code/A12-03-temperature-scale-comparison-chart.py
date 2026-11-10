from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.8, 7.2)
    ax.axis('off')

    # Y-coordinates for the three reference points
    y_steam = 5.6
    y_ice = 3.6
    y_abs = 1.0

    # Thermometer positions (center X)
    thermo_x = [3.8, 6.5, 9.2]
    tube_w = 0.5
    bulb_r = 0.45
    tube_bottom = 0.6
    tube_top = 6.4

    # Reference levels info: (y, label, [C_val, K_val, F_val])
    levels = [
        (y_steam, "Steam point", ["100 °C", "373 K", "212 °F"]),
        (y_ice, "Ice point", ["0 °C", "273 K", "32 °F"]),
        (y_abs, "Absolute zero", ["-273 °C", "0 K", "-459.67 °F"])
    ]

    # Draw dashed reference lines across
    line_x_start = 1.6
    line_x_end = 11.2
    for y, label, vals in levels:
        ax.plot([line_x_start, line_x_end], [y, y], linestyle="--", color=GREY, lw=1.8, zorder=1)
        # Left label for reference line
        ax.text(line_x_start - 0.2, y, label, ha="right", va="center", fontsize=15, fontweight="bold", color=INK)

    # Draw thermometers
    for idx, cx in enumerate(thermo_x):
        # Outer tube background (CREAM)
        rect_bg = patches.Rectangle((cx - tube_w/2, tube_bottom), tube_w, tube_top - tube_bottom,
                                    fc=CREAM, ec="none", zorder=2)
        circle_bg = patches.Circle((cx, tube_bottom), bulb_r, fc=CREAM, ec="none", zorder=2)
        ax.add_patch(rect_bg)
        ax.add_patch(circle_bg)

        # Liquid column (PINK / DEEP["pink"])
        liq_w = 0.22
        liq_top = y_steam + 0.35
        liq_rect = patches.Rectangle((cx - liq_w/2, tube_bottom), liq_w, liq_top - tube_bottom,
                                     fc=PINK, ec="none", zorder=3)
        liq_bulb = patches.Circle((cx, tube_bottom), bulb_r * 0.75, fc=PINK, ec="none", zorder=3)
        ax.add_patch(liq_rect)
        ax.add_patch(liq_bulb)

        # Tube outline
        # Stem vertical lines
        ax.plot([cx - tube_w/2, cx - tube_w/2], [tube_bottom, tube_top], color=INK, lw=2, zorder=4)
        ax.plot([cx + tube_w/2, cx + tube_w/2], [tube_bottom, tube_top], color=INK, lw=2, zorder=4)
        # Rounded top cap
        arc_top = patches.Arc((cx, tube_top), tube_w, tube_w, angle=0, theta1=0, theta2=180,
                              ec=INK, lw=2, zorder=4)
        ax.add_patch(arc_top)

        # Bulb outline (connected at bottom)
        bulb_outer = patches.Circle((cx, tube_bottom), bulb_r, fill=False, ec=INK, lw=2, zorder=4)
        ax.add_patch(bulb_outer)

        # Tick marks and value annotations for each level
        for y, _, vals in levels:
            # Tick mark on right edge of tube
            ax.plot([cx + tube_w/2 - 0.05, cx + tube_w/2 + 0.15], [y, y], color=INK, lw=2, zorder=5)
            # Text value to the right of tick mark
            val_text = vals[idx]
            ax.text(cx + tube_w/2 + 0.25, y, val_text, ha="left", va="center", fontsize=15,
                    color=INK, bbox=dict(fc="white", ec="none", pad=1.5), zorder=6)

    # Column Titles
    titles = ["Celsius (°C)", "Kelvin (K)", "Fahrenheit (°F)"]
    for cx, title in zip(thermo_x, titles):
        ax.text(cx, tube_top + 0.45, title, ha="center", va="bottom", fontsize=16,
                fontweight="bold", color=INK)

    save(fig, out)
