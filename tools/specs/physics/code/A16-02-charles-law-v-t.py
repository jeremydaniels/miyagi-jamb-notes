from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 6.5)
    
    # ----------------- Left Graph: V vs T in °C -----------------
    ax1 = fig.add_subplot(121)
    
    # Coordinate system for Celsius graph:
    # x goes from -300 to 200, y goes from -1 to 8
    ax1.set_xlim(-310, 180)
    ax1.set_ylim(-0.8, 6.5)
    
    # Remove top and right spines
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Position bottom spine at y=0
    ax1.spines['bottom'].set_position(('data', 0))
    ax1.spines['bottom'].set_color(INK)
    ax1.spines['bottom'].set_linewidth(1.5)
    
    # Position left spine at x=0
    ax1.spines['left'].set_position(('data', 0))
    ax1.spines['left'].set_color(INK)
    ax1.spines['left'].set_linewidth(1.5)
    
    # Arrow heads for axes
    ax1.plot(180, 0, ">", color=INK, markersize=8, clip_on=False)
    ax1.plot(0, 6.5, "^", color=INK, markersize=8, clip_on=False)
    
    # Custom ticks
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    # Axis labels
    ax1.text(180, -0.4, "Temperature (T) in °C", color=INK, fontsize=15, ha="right", va="top")
    ax1.text(-15, 6.5, "Volume (V)", color=INK, fontsize=15, ha="right", va="bottom")
    
    # Charles's law line: V = m * (T + 273)
    # Extrapolation (dashed): from -273 to -100
    x_extrap = np.linspace(-273, -100, 50)
    y_extrap = 0.015 * (x_extrap + 273)
    ax1.plot(x_extrap, y_extrap, linestyle="--", color=DEEP["blue"], lw=3)
    
    # Real / measured range (solid): from -100 to 140
    x_real = np.linspace(-100, 140, 100)
    y_real = 0.015 * (x_real + 273)
    ax1.plot(x_real, y_real, linestyle="-", color=DEEP["blue"], lw=3)
    
    # Tick mark and label at -273 °C
    ax1.plot([-273, -273], [-0.15, 0.15], color=INK, lw=1.5)
    ax1.text(-273, -0.4, "-273 °C\n(Absolute Zero)", color=INK, fontsize=14, ha="center", va="top")
    
    # Origin mark 0
    ax1.text(5, -0.35, "0", color=INK, fontsize=14, ha="left", va="top")
    
    ax1.set_title("Charles's Law (Celsius)", fontsize=16, color=INK, pad=20, weight="bold")
    
    # ----------------- Right Graph: V vs T in Kelvin -----------------
    ax2 = fig.add_subplot(122)
    
    ax2.set_xlim(-30, 450)
    ax2.set_ylim(-0.8, 6.5)
    
    # Remove top and right spines
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Bottom spine at y=0, left spine at x=0
    ax2.spines['bottom'].set_position(('data', 0))
    ax2.spines['bottom'].set_color(INK)
    ax2.spines['bottom'].set_linewidth(1.5)
    
    ax2.spines['left'].set_position(('data', 0))
    ax2.spines['left'].set_color(INK)
    ax2.spines['left'].set_linewidth(1.5)
    
    # Arrow heads
    ax2.plot(450, 0, ">", color=INK, markersize=8, clip_on=False)
    ax2.plot(0, 6.5, "^", color=INK, markersize=8, clip_on=False)
    
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    # Axis labels
    ax2.text(450, -0.4, "Temperature (T) in Kelvin (K)", color=INK, fontsize=15, ha="right", va="top")
    ax2.text(-15, 6.5, "Volume (V)", color=INK, fontsize=15, ha="right", va="bottom")
    
    # Direct proportionality line through (0,0)
    x_k_dashed = np.linspace(0, 60, 30)
    y_k_dashed = 0.015 * x_k_dashed
    ax2.plot(x_k_dashed, y_k_dashed, linestyle="--", color=DEEP["blue"], lw=3)
    
    x_k_solid = np.linspace(60, 400, 100)
    y_k_solid = 0.015 * x_k_solid
    ax2.plot(x_k_solid, y_k_solid, linestyle="-", color=DEEP["blue"], lw=3)
    
    # Origin label (0,0)
    ax2.plot([0, 0], [-0.15, 0.15], color=INK, lw=1.5)
    ax2.text(0, -0.4, "0 K\n(0,0)", color=INK, fontsize=14, ha="center", va="top")
    
    # Annotation V ∝ T
    ax2.text(250, 2.3, r"$V \propto T$", color=INK, fontsize=16, 
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax2.set_title("Charles's Law (Kelvin)", fontsize=16, color=INK, pad=20, weight="bold")
    
    plt.tight_layout()
    save(fig, out)
