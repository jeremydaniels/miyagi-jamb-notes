from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Title
    ax.text(6.0, 6.4, "Penetrating Power of Radiation", ha="center", va="center",
            fontsize=18, weight="bold", color=INK)

    # Coordinates and dimensions of barriers
    # Paper: x = 4.2 to 4.4
    # Aluminium: x = 6.8 to 7.1
    # Lead: x = 9.5 to 10.7
    paper_x = 4.2
    paper_w = 0.2
    al_x = 6.9
    al_w = 0.35
    lead_x = 9.6
    lead_w = 1.3
    barrier_y = 1.0
    barrier_h = 4.5

    # Draw Lead Box (Source) on the left
    # Outer box
    box_rect = patches.Rectangle((0.6, 2.0), 1.4, 3.0, linewidth=2, edgecolor=INK, facecolor=GREY)
    ax.add_patch(box_rect)
    # Cavity / Collimator opening to the right
    cavity = patches.Rectangle((1.3, 2.7), 0.75, 1.6, linewidth=1.5, edgecolor=INK, facecolor="white")
    ax.add_patch(cavity)
    # Radioactive source inside cavity
    source = patches.Circle((1.5, 3.5), 0.22, facecolor=DEEP["orange"], edgecolor=INK, linewidth=1.5, zorder=5)
    ax.add_patch(source)
    ax.text(1.3, 1.6, "Radioactive\nsource", ha="center", va="top", fontsize=14, color=INK)
    ax.text(1.3, 5.2, "Lead\ncollimator", ha="center", va="bottom", fontsize=14, color=INK)

    # Draw Barriers
    # 1. Paper
    paper_rect = patches.Rectangle((paper_x, barrier_y), paper_w, barrier_h,
                                   linewidth=1.8, edgecolor=INK, facecolor="#F8F9FA", zorder=3)
    ax.add_patch(paper_rect)
    ax.text(paper_x + paper_w / 2, barrier_y + barrier_h + 0.25, "Paper", ha="center", va="bottom",
            fontsize=15, weight="bold", color=INK)

    # 2. Aluminium
    al_rect = patches.Rectangle((al_x, barrier_y), al_w, barrier_h,
                                linewidth=1.8, edgecolor=INK, facecolor="#CBD3DC", zorder=3)
    ax.add_patch(al_rect)
    ax.text(al_x + al_w / 2, barrier_y + barrier_h + 0.25, "Aluminium", ha="center", va="bottom",
            fontsize=15, weight="bold", color=INK)

    # 3. Lead Block
    lead_rect = patches.Rectangle((lead_x, barrier_y), lead_w, barrier_h,
                                  linewidth=1.8, edgecolor=INK, facecolor="#828D99", zorder=3)
    ax.add_patch(lead_rect)
    ax.text(lead_x + lead_w / 2, barrier_y + barrier_h + 0.25, "Thick Lead", ha="center", va="bottom",
            fontsize=15, weight="bold", color=INK)

    # Ray trajectories
    start_x = 1.7
    y_alpha = 4.3
    y_beta = 3.5
    y_gamma = 2.7

    # 1. Alpha Ray (thick, red/orange, stopped by paper)
    ax.annotate("", xy=(paper_x, y_alpha), xytext=(start_x, y_alpha),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["orange"], lw=5.0, mutation_scale=20))
    ax.text(2.6, y_alpha + 0.25, r"$\alpha$ (alpha particles)", ha="center", va="bottom",
            fontsize=15, weight="bold", color=DEEP["orange"],
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # 2. Beta Ray (medium, blue, passes paper, stopped by aluminium)
    # Segment through paper to aluminium
    ax.plot([start_x, al_x], [y_beta, y_beta], color=DEEP["blue"], lw=2.8, zorder=2)
    # Arrow head at aluminium
    ax.annotate("", xy=(al_x, y_beta), xytext=(al_x - 0.2, y_beta),
                arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.8, mutation_scale=18), zorder=4)
    ax.text(2.6, y_beta + 0.25, r"$\beta$ (beta particles)", ha="center", va="bottom",
            fontsize=15, weight="bold", color=DEEP["blue"],
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # 3. Gamma Ray (wavy line, green/deep green, passes paper & al, absorbed in lead)
    # Create sine wave up to the middle of the lead block
    stop_gamma_x = lead_x + lead_w * 0.7
    x_wave = np.linspace(start_x, stop_gamma_x, 600)
    wavelength = 0.35
    amplitude = 0.12
    # Damp amplitude slightly inside lead block to show absorption
    damp = np.where(x_wave > lead_x, np.exp(-3.5 * (x_wave - lead_x)), 1.0)
    y_wave = y_gamma + amplitude * np.sin(2 * np.pi * (x_wave - start_x) / wavelength) * damp
    ax.plot(x_wave, y_wave, color=DEEP["green"], lw=2.5, zorder=4)

    # Add absorption marker (cross or dot) inside lead
    ax.plot(stop_gamma_x, y_gamma, marker="o", markersize=5, color=DEEP["green"], zorder=5)

    ax.text(2.6, y_gamma - 0.45, r"$\gamma$ (gamma rays)", ha="center", va="top",
            fontsize=15, weight="bold", color=DEEP["green"],
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Bottom notes / indicators
    ax.text(paper_x + paper_w / 2, barrier_y - 0.4, "Stopped by\npaper", ha="center", va="top",
            fontsize=14, color=INK)
    ax.text(al_x + al_w / 2, barrier_y - 0.4, "Stopped by\n~5 mm Al", ha="center", va="top",
            fontsize=14, color=INK)
    ax.text(lead_x + lead_w / 2, barrier_y - 0.4, "Absorbed by\nlead block", ha="center", va="top",
            fontsize=14, color=INK)

    save(fig, out)
