from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 5.5)
    
    # Subplot 1: Temperature in Kelvin
    ax1 = fig.add_subplot(1, 2, 1)
    
    # Custom spines for textbook look
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(INK)
    ax1.spines['bottom'].set_color(INK)
    ax1.spines['left'].set_linewidth(1.5)
    ax1.spines['bottom'].set_linewidth(1.5)
    
    # Line for Graph 1
    T_k = np.linspace(0, 10, 100)
    V_k = 0.8 * T_k
    ax1.plot(T_k, V_k, color=DEEP["blue"], lw=3.5)
    
    ax1.set_xlim(0, 11)
    ax1.set_ylim(0, 9)
    ax1.set_xticks([0])
    ax1.set_xticklabels(["0"], fontsize=14, color=INK)
    ax1.set_yticks([0])
    ax1.set_yticklabels(["0"], fontsize=14, color=INK)
    ax1.set_xlabel("Temperature (K)", fontsize=16, color=INK, labelpad=10)
    ax1.set_ylabel("Volume (V)", fontsize=16, color=INK, labelpad=10)
    ax1.set_title("Volume vs. Absolute Temperature", fontsize=16, color=INK, pad=15)
    
    # Arrowheads for axes
    ax1.plot(11, 0, ">k", clip_on=False, markersize=8, color=INK)
    ax1.plot(0, 9, "^k", clip_on=False, markersize=8, color=INK)

    # Subplot 2: Temperature in Celsius
    ax2 = fig.add_subplot(1, 2, 2)
    
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_position(('data', 0))
    ax2.spines['bottom'].set_position(('data', 0))
    ax2.spines['left'].set_color(INK)
    ax2.spines['bottom'].set_color(INK)
    ax2.spines['left'].set_linewidth(1.5)
    ax2.spines['bottom'].set_linewidth(1.5)

    # Parameters: -273 is at x = -3, y-intercept at (0, 3)
    # y = slope * (x - x_intercept)
    # slope = 3 / 3 = 1
    x_dotted = np.linspace(-3, 0, 50)
    y_dotted = 1.0 * (x_dotted + 3)
    ax2.plot(x_dotted, y_dotted, color=DEEP["blue"], lw=2.5, linestyle="--")

    x_solid = np.linspace(0, 5, 50)
    y_solid = 1.0 * (x_solid + 3)
    ax2.plot(x_solid, y_solid, color=DEEP["blue"], lw=3.5)

    ax2.set_xlim(-4, 6)
    ax2.set_ylim(-0.5, 9)
    
    # Custom ticks
    ax2.set_xticks([-3, 0])
    ax2.set_xticklabels(["-273 °C", "0"], fontsize=14, color=INK)
    ax2.set_yticks([])

    # Mark -273 °C point
    ax2.plot(-3, 0, 'o', color=DEEP["pink"], markersize=6, zorder=5)

    # Axis labels
    ax2.set_xlabel("Temperature (°C)", fontsize=16, color=INK, labelpad=10)
    ax2.xaxis.set_label_coords(0.75, -0.08)
    
    ax2.text(-0.3, 8.8, "Volume (V)", fontsize=16, color=INK, ha='right', va='top')
    ax2.set_title("Volume vs. Celsius Temperature", fontsize=16, color=INK, pad=15)

    # Arrowheads for axes
    ax2.plot(6, 0, ">k", clip_on=False, markersize=8, color=INK)
    ax2.plot(0, 9, "^k", clip_on=False, markersize=8, color=INK)

    fig.tight_layout(w_pad=4.0)
    save(fig, out)
