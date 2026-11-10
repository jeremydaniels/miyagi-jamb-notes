from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(8, 9)
    
    # Create two vertically stacked subplots sharing x axis
    ax_top = fig.add_axes([0.15, 0.54, 0.78, 0.38])
    ax_bot = fig.add_axes([0.15, 0.10, 0.78, 0.38])
    
    # Mathematics for TU and MU
    q_max = 7.5
    q = np.linspace(0, q_max, 200)
    tu = 10 * q - q**2
    mu = 10 - 2 * q
    q_peak = 5.0
    tu_peak = 25.0

    # Plot Total Utility (TU)
    ax_top.plot(q, tu, color=DEEP["blue"], lw=3.5, label="Total Utility (TU)")
    ax_top.set_xlim(0, 7.5)
    ax_top.set_ylim(0, 30)
    ax_top.set_ylabel("Total Utility", fontsize=15, color=INK, labelpad=10)
    ax_top.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    for spine in ['top', 'right']:
        ax_top.spines[spine].set_visible(False)
    ax_top.spines['left'].set_color(INK)
    ax_top.spines['bottom'].set_color(INK)
    ax_top.spines['left'].set_linewidth(1.5)
    ax_top.spines['bottom'].set_linewidth(1.5)

    # Plot Marginal Utility (MU)
    ax_bot.plot(q, mu, color=DEEP["orange"], lw=3.5, label="Marginal Utility (MU)")
    ax_bot.set_xlim(0, 7.5)
    ax_bot.set_ylim(-6, 12)
    ax_bot.set_xlabel("Quantity", fontsize=15, color=INK, labelpad=10)
    ax_bot.set_ylabel("Marginal Utility", fontsize=15, color=INK, labelpad=10)
    ax_bot.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    for spine in ['top', 'right']:
        ax_bot.spines[spine].set_visible(False)
    ax_bot.spines['left'].set_color(INK)
    ax_bot.spines['bottom'].set_position(('data', 0))
    ax_bot.spines['bottom'].set_color(INK)
    ax_bot.spines['left'].set_linewidth(1.5)
    ax_bot.spines['bottom'].set_linewidth(1.5)

    # Dashed connection line through the saturation point
    ax_top.plot([q_peak, q_peak], [0, tu_peak], color=GREY, ls='--', lw=1.8, zorder=1)
    ax_bot.plot([q_peak, q_peak], [-6, 10], color=GREY, ls='--', lw=1.8, zorder=1)

    # Key points markers
    ax_top.plot(q_peak, tu_peak, 'o', color=DEEP["blue"], markersize=7, zorder=5)
    ax_bot.plot(q_peak, 0, 'o', color=DEEP["orange"], markersize=7, zorder=5)

    # Labels for Top Graph
    ax_top.text(2.5, 23, "Total Utility (TU)", fontsize=16, color=DEEP["blue"], weight='bold',
                bbox=dict(fc='white', ec='none', pad=2))
    ax_top.annotate("Maximum TU",
                    xy=(q_peak, tu_peak), xytext=(q_peak + 0.4, tu_peak + 1.8),
                    fontsize=14, color=INK, weight='bold',
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                    bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Labels for Bottom Graph
    ax_bot.text(1.2, 8.5, "Marginal Utility (MU)", fontsize=16, color=DEEP["orange"], weight='bold',
                bbox=dict(fc='white', ec='none', pad=2))
    
    # Point of Satiety annotation
    ax_bot.annotate("Zero MU (Point of Satiety)",
                    xy=(q_peak, 0), xytext=(q_peak + 0.3, 4.0),
                    fontsize=14, color=INK, weight='bold',
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                    bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Positive and Negative MU regions
    ax_bot.text(2.0, 2.0, "Positive MU", fontsize=14, color=DEEP["green"], weight='bold',
                bbox=dict(fc='white', ec='none', pad=2))
    
    # Place Negative MU label away from the line with an arrow to avoid overlap
    ax_bot.annotate("Negative MU (Disutility)",
                    xy=(6.3, -2.6), xytext=(1.5, -4.0),
                    fontsize=14, color=DEEP["pink"], weight='bold',
                    arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5, connectionstyle="arc3,rad=-0.1"),
                    bbox=dict(fc='white', ec='none', pad=2))

    save(fig, out)
