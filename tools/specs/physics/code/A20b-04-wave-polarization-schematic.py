from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-3.2, 3.2)
    ax.axis('off')

    # Positions of polarizers
    x_p1 = 3.6
    x_p2 = 8.0

    # Draw Polarizer A (Vertical Slit)
    # Outer plate
    w_plate, h_plate = 0.5, 3.8
    rect_a = plt.Rectangle((x_p1 - w_plate/2, -h_plate/2), w_plate, h_plate, 
                           facecolor=LAV, edgecolor=DEEP["lav"], lw=2.2, zorder=4)
    ax.add_patch(rect_a)
    # Slit opening
    slit_w, slit_h = 0.12, 2.6
    slit_a = plt.Rectangle((x_p1 - slit_w/2, -slit_h/2), slit_w, slit_h, 
                           facecolor="white", edgecolor=DEEP["lav"], lw=1.8, zorder=5)
    ax.add_patch(slit_a)

    # Draw Polarizer B (Horizontal Slit)
    rect_b = plt.Rectangle((x_p2 - w_plate/2, -h_plate/2), w_plate, h_plate, 
                           facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.2, zorder=4)
    ax.add_patch(rect_b)
    # Slit opening (horizontal)
    slit_bw, slit_bh = 0.38, 0.14
    slit_b = plt.Rectangle((x_p2 - slit_bw/2, -slit_bh/2), slit_bw, slit_bh, 
                           facecolor="white", edgecolor=DEEP["orange"], lw=1.8, zorder=5)
    ax.add_patch(slit_b)

    # Section 1: Unpolarized Wave (0 to x_p1)
    # A 3D-projected transverse wave vibrating in multiple planes
    x1 = np.linspace(0.4, x_p1, 250)
    k1 = 2 * np.pi / 1.8
    # Vertical component
    y1_v = 0.9 * np.sin(k1 * x1)
    # Horizontal/oblique component represented by second wave
    y1_h = 0.55 * np.cos(k1 * x1 * 0.95)
    
    # Draw faint reference/dashed line through center
    ax.plot([0.2, 10.8], [0, 0], color=GREY, lw=1.2, ls="--", zorder=1)

    # Waves in section 1
    ax.plot(x1, y1_h, color=DEEP["pink"], lw=2.2, alpha=0.6, zorder=2)
    ax.plot(x1, y1_v, color=DEEP["blue"], lw=3.2, zorder=3)

    # Starburst arrows near start of unpolarized section
    star_x = 1.0
    star_y = 0.0
    r_arr = 0.75
    angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    for ang in angles:
        dx = r_arr * np.cos(ang) * 0.45  # scaled horizontally for aspect ratio
        dy = r_arr * np.sin(ang)
        ax.annotate("", xy=(star_x + dx, star_y + dy), xytext=(star_x, star_y),
                    arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8, mutation_scale=12),
                    zorder=6)

    # Section 2: Plane-polarized wave (x_p1 to x_p2)
    x2 = np.linspace(x_p1, x_p2, 250)
    y2 = 0.9 * np.sin(k1 * x2)
    ax.plot(x2, y2, color=DEEP["blue"], lw=3.2, zorder=3)

    # Vertical double-headed arrow showing vertical vibration
    mid_x2 = (x_p1 + x_p2) / 2
    ax.annotate("", xy=(mid_x2, 0.95), xytext=(mid_x2, -0.95),
                arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=2.0, mutation_scale=14),
                zorder=6)

    # Section 3: Wave blocked (after x_p2)
    x3 = np.linspace(x_p2, 10.6, 100)
    ax.plot(x3, np.zeros_like(x3), color=DEEP["blue"], lw=3.2, zorder=3)

    # Labels and Annotations (Textbook typography, size >= 14, no overlap)
    # Polarizer titles
    ax.text(x_p1, 2.35, "Vertical polarizer", ha="center", va="bottom", fontsize=15, 
            weight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1))
    ax.text(x_p1, -2.35, "(Polarizer A)", ha="center", va="top", fontsize=14, 
            color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    ax.text(x_p2, 2.35, "Horizontal analyzer", ha="center", va="bottom", fontsize=15, 
            weight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1))
    ax.text(x_p2, -2.35, "(Polarizer B)", ha="center", va="top", fontsize=14, 
            color=INK, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # State labels
    ax.text(1.8, 1.45, "Unpolarized wave", ha="center", va="bottom", fontsize=15,
            weight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1))
    
    ax.text(mid_x2, 1.45, "Plane-polarized wave", ha="center", va="bottom", fontsize=15,
            weight="bold", color=INK, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=1))

    ax.text(9.5, 0.65, "Wave blocked", ha="center", va="bottom", fontsize=15,
            weight="bold", color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["orange"], lw=1.2))
    
    # Descriptive caption below wave blocked
    ax.text(9.5, -0.7, "(completely\nblocked)", ha="center", va="top", fontsize=14, color=INK)

    save(fig, out)
