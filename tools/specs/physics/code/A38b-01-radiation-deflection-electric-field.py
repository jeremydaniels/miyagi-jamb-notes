from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-2, 11)
    ax.set_ylim(-3.5, 4.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # Lead block (cross-section)
    # Outer block: x from -1.5 to 0.5, y from -1.5 to 1.5
    lead_outer = patches.Rectangle((-1.5, -1.6), 2.2, 3.2, facecolor=GREY, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(lead_outer)

    # Cavity / hole inside lead block (collimator channel)
    lead_cavity = patches.Rectangle((-0.4, -0.3), 1.15, 0.6, facecolor="white", edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(lead_cavity)

    # Radioactive source inside the cavity
    source = patches.Circle((-0.1, 0), 0.22, facecolor=DEEP["orange"], edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(source)

    # Parallel Plates
    plate_x_start = 2.0
    plate_width = 5.0
    plate_thickness = 0.35

    # Positive Plate (top)
    pos_plate = patches.Rectangle((plate_x_start, 1.8), plate_width, plate_thickness,
                                  facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=2)
    ax.add_patch(pos_plate)
    # Positive plate charges
    for x_c in np.linspace(plate_x_start + 0.4, plate_x_start + plate_width - 0.4, 7):
        ax.text(x_c, 1.975, "+", color=DEEP["pink"], fontsize=16, fontweight="bold", ha="center", va="center", zorder=3)

    # Negative Plate (bottom)
    neg_plate = patches.Rectangle((plate_x_start, -2.15), plate_width, plate_thickness,
                                  facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=2)
    ax.add_patch(neg_plate)
    # Negative plate charges
    for x_c in np.linspace(plate_x_start + 0.4, plate_x_start + plate_width - 0.4, 7):
        ax.text(x_c, -1.975, "−", color=DEEP["blue"], fontsize=18, fontweight="bold", ha="center", va="center", zorder=3)

    # Electric field lines (subtle, pointing down from + to -)
    for x_e in np.linspace(plate_x_start + 0.6, plate_x_start + plate_width - 0.6, 6):
        ax.annotate("", xy=(x_e, -1.7), xytext=(x_e, 1.7),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=1, ls=":", mutation_scale=10), zorder=1)

    # Straight initial beam from source to entry of electric field
    ax.plot([-0.1, 2.2], [0, 0], color=INK, lw=2.5, zorder=5)

    # Radiation trajectories starting from x = 2.2, y = 0
    # 1. Gamma ray: completely undeflected
    x_gamma = np.linspace(2.2, 9.5, 100)
    y_gamma = np.zeros_like(x_gamma)
    ax.plot(x_gamma, y_gamma, color=DEEP["green"], lw=2.5, zorder=5)
    ax.annotate("", xy=(8.0, 0), xytext=(7.5, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5, mutation_scale=15), zorder=5)

    # 2. Beta ray: bends sharply upwards towards positive plate
    x_beta = np.linspace(2.2, 6.2, 100)
    # Parabolic deflection inside/leaving field
    y_beta = 0.12 * (x_beta - 2.2)**2 + 0.05 * (x_beta - 2.2)
    ax.plot(x_beta, y_beta, color=DEEP["blue"], lw=2.5, zorder=5)
    ax.annotate("", xy=(x_beta[60], y_beta[60]), xytext=(x_beta[55], y_beta[55]),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5, mutation_scale=15), zorder=5)

    # 3. Alpha ray: bends slightly downwards towards negative plate
    x_alpha = np.linspace(2.2, 8.5, 100)
    y_alpha = -0.028 * (x_alpha - 2.2)**2
    ax.plot(x_alpha, y_alpha, color=DEEP["pink"], lw=2.5, zorder=5)
    ax.annotate("", xy=(x_alpha[65], y_alpha[65]), xytext=(x_alpha[60], y_alpha[60]),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=15), zorder=5)

    # Text Labels with white bounding boxes to prevent overlapping lines
    bbox_style = dict(boxstyle="round,pad=0.25", fc="white", ec="none")

    # Plates
    ax.text(plate_x_start + plate_width / 2, 2.5, "+ Positive plate",
            fontsize=15, color=INK, ha="center", va="center", fontweight="bold", bbox=bbox_style)
    ax.text(plate_x_start + plate_width / 2, -2.6, "− Negative plate",
            fontsize=15, color=INK, ha="center", va="center", fontweight="bold", bbox=bbox_style)

    # Lead block & Radioactive source annotations
    ax.text(-0.4, -2.2, "Lead block", fontsize=14, color=INK, ha="center", va="center", bbox=bbox_style)
    ax.annotate("Radioactive source", xy=(-0.1, 0.25), xytext=(-0.5, 2.3),
                fontsize=14, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4), bbox=bbox_style)

    # Beam End Labels
    ax.text(6.4, y_beta[-1] + 0.1, r"Beta ($\beta$) particle",
            fontsize=15, color=DEEP["blue"], ha="left", va="center", fontweight="bold", bbox=bbox_style)
    ax.text(9.7, 0, r"Gamma ($\gamma$) ray",
            fontsize=15, color=DEEP["green"], ha="left", va="center", fontweight="bold", bbox=bbox_style)
    ax.text(8.7, y_alpha[-1] - 0.1, r"Alpha ($\alpha$) particle",
            fontsize=15, color=DEEP["pink"], ha="left", va="center", fontweight="bold", bbox=bbox_style)

    save(fig, out)
