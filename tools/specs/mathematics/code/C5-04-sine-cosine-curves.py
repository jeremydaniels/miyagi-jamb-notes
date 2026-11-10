from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_subplot(111)
    
    # Domain 0 to 360 degrees
    x_deg = np.linspace(0, 360, 500)
    x_rad = np.radians(x_deg)
    
    y_sin = np.sin(x_rad)
    y_cos = np.cos(x_rad)
    
    # Reference gridlines at y = -1, 0, 1
    ax.axhline(1.0, color=GREY, linestyle=":", linewidth=1.2, zorder=1)
    ax.axhline(0.0, color=GREY, linestyle="-", linewidth=1.0, zorder=1)
    ax.axhline(-1.0, color=GREY, linestyle=":", linewidth=1.2, zorder=1)
    
    # Plot sine and cosine
    ax.plot(x_deg, y_sin, color=DEEP["pink"], lw=3.0, label="y = sin(x)", zorder=3)
    ax.plot(x_deg, y_cos, color=DEEP["blue"], lw=3.0, linestyle="--", label="y = cos(x)", zorder=3)
    
    # Key points for sine
    sin_pts_x = [0, 90, 180, 270, 360]
    sin_pts_y = [0, 1, 0, -1, 0]
    ax.scatter(sin_pts_x, sin_pts_y, color=DEEP["pink"], s=40, zorder=4)
    
    # Key points for cosine
    cos_pts_x = [0, 90, 180, 270, 360]
    cos_pts_y = [1, 0, -1, 0, 1]
    ax.scatter(cos_pts_x, cos_pts_y, color=DEEP["blue"], s=40, zorder=4)
    
    # Axis configuration
    ax.set_xlim(-15, 375)
    ax.set_ylim(-1.5, 1.5)
    
    ax.set_xticks([0, 90, 180, 270, 360])
    ax.set_xticklabels(["0°", "90°", "180°", "270°", "360°"], fontsize=14, color=INK)
    ax.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
    ax.set_yticklabels(["-1.5", "-1", "-0.5", "0", "0.5", "1", "1.5"], fontsize=14, color=INK)
    
    ax.set_xlabel("x", fontsize=16, color=INK, labelpad=8)
    ax.set_ylabel("y", fontsize=16, color=INK, labelpad=8)
    
    # Clean spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK, width=1.2)
    
    # Legend
    ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor=GREY, fontsize=14)
    
    save(fig, out)
