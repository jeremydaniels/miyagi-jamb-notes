from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 7.5)
    ax = fig.add_axes([0.08, 0.05, 0.84, 0.90])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.6, "Energy Levels & Emission Spectra", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK)

    # 1. Top Section: Energy Levels Schematic
    # Energy level horizontal lines
    # Levels: n=1 at y=4.8, n=2 at y=6.4, n=3 at y=7.8
    y1, y2, y3 = 4.8, 6.4, 7.8
    x_start, x_end = 2.0, 8.5

    # Energy axis (vertical arrow) on the left
    ax.annotate('', xy=(1.2, 8.4), xytext=(1.2, 4.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.0))
    ax.text(0.9, 6.4, "Energy", rotation=90, ha="center", va="center",
            fontsize=15, fontweight="bold", color=INK)

    # Level lines
    levels = [(y1, "n = 1 (ground state)"), (y2, "n = 2"), (y3, "n = 3")]
    for y_pos, label in levels:
        ax.plot([x_start, x_end], [y_pos, y_pos], color=INK, lw=2.5)
        ax.text(x_end + 0.15, y_pos, label, ha="left", va="center",
                fontsize=14, fontweight="bold", color=INK)

    # Transition 1: n=3 -> n=2 (at x = 3.6)
    x_t1 = 3.6
    ax.annotate('', xy=(x_t1, y2 + 0.05), xytext=(x_t1, y3 - 0.05),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5))
    ax.plot(x_t1, y3, marker='o', markersize=6, color=DEEP["pink"])

    # Wavy photon from transition 1
    # Emit to the right between y3 and y2
    y_wave1_center = (y3 + y2) / 2
    x_w1 = np.linspace(x_t1 + 0.2, x_t1 + 1.6, 100)
    y_w1 = y_wave1_center + 0.12 * np.sin(2 * np.pi * 3.5 * (x_w1 - x_t1) / 1.4)
    ax.plot(x_w1, y_w1, color=DEEP["pink"], lw=2.0)
    ax.annotate('', xy=(x_t1 + 1.8, y_wave1_center), xytext=(x_t1 + 1.6, y_wave1_center),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.0))
    ax.text(x_t1 + 1.0, y_wave1_center + 0.35, "photon", ha="center", va="bottom",
            fontsize=14, color=DEEP["pink"], style="italic")

    # Transition 2: n=2 -> n=1 (at x = 6.2)
    x_t2 = 6.2
    ax.annotate('', xy=(x_t2, y1 + 0.05), xytext=(x_t2, y2 - 0.05),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5))
    ax.plot(x_t2, y2, marker='o', markersize=6, color=DEEP["blue"])

    # Wavy photon from transition 2
    y_wave2_center = (y2 + y1) / 2
    x_w2 = np.linspace(x_t2 + 0.2, x_t2 + 1.6, 100)
    y_w2 = y_wave2_center + 0.12 * np.sin(2 * np.pi * 4.5 * (x_w2 - x_t2) / 1.4)
    ax.plot(x_w2, y_w2, color=DEEP["blue"], lw=2.0)
    ax.annotate('', xy=(x_t2 + 1.8, y_wave2_center), xytext=(x_t2 + 1.6, y_wave2_center),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0))
    ax.text(x_t2 + 1.0, y_wave2_center + 0.35, "photon", ha="center", va="bottom",
            fontsize=14, color=DEEP["blue"], style="italic")

    # 2. Bottom Section: Spectra Rectangles
    spec_left = 1.8
    spec_right = 8.5
    w_spec = spec_right - spec_left

    # Continuous Spectrum
    y_cont_bottom = 2.4
    h_spec = 0.8
    ax.text(spec_left - 0.2, y_cont_bottom + h_spec / 2, "Continuous\nspectrum",
            ha="right", va="center", fontsize=14, color=INK, fontweight="bold")

    # Draw continuous spectrum gradient
    n_pts = 300
    spec_img = np.linspace(0, 1, n_pts).reshape(1, n_pts)
    ax.imshow(spec_img, cmap='turbo', aspect='auto',
              extent=[spec_left, spec_right, y_cont_bottom, y_cont_bottom + h_spec],
              origin='lower')
    # Border for continuous spectrum
    rect1 = plt.Rectangle((spec_left, y_cont_bottom), w_spec, h_spec,
                          edgecolor=INK, facecolor='none', lw=2.0)
    ax.add_patch(rect1)

    # Line Emission Spectrum
    y_line_bottom = 0.8
    ax.text(spec_left - 0.2, y_line_bottom + h_spec / 2, "Line emission\nspectrum",
            ha="right", va="center", fontsize=14, color=INK, fontweight="bold")

    # Black background rectangle
    rect2 = plt.Rectangle((spec_left, y_line_bottom), w_spec, h_spec,
                          edgecolor=INK, facecolor='#111111', lw=2.0)
    ax.add_patch(rect2)

    # Three thin vertical coloured lines
    # Using wavelengths corresponding visually across the visible range: red, aqua/cyan, violet/blue
    line_positions = [
        (spec_left + 0.22 * w_spec, '#3b82f6'),  # violet / blue line
        (spec_left + 0.50 * w_spec, '#10b981'),  # green / cyan line
        (spec_left + 0.82 * w_spec, '#ef4444')   # red line
    ]
    for x_pos, col in line_positions:
        ax.plot([x_pos, x_pos], [y_line_bottom, y_line_bottom + h_spec],
                color=col, lw=3.0)

    save(fig, out)
