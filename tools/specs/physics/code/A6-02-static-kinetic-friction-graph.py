from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6)
    ax = fig.add_subplot(111)
    
    # Set up axes
    axes_clean(ax, "Applied Force", "Frictional Force", 10, 8)
    
    # Data points
    # Static friction line: from (0,0) to (5, 6)
    # Peak at (5, 6) - Limiting friction
    # Drop to (5.6, 4.5) then flat dynamic friction to (9.5, 4.5)
    x_static = np.array([0, 5.0])
    y_static = np.array([0, 6.0])
    
    # Smooth drop after peak to kinetic friction
    x_trans = np.linspace(5.0, 5.6, 20)
    # Cosine drop from 6.0 to 4.5
    y_trans = 4.5 + 1.5 * 0.5 * (1 + np.cos(np.pi * (x_trans - 5.0) / 0.6))
    
    x_kinetic = np.array([5.6, 9.5])
    y_kinetic = np.array([4.5, 4.5])
    
    # Combined curve
    x_full = np.concatenate([x_static, x_trans[1:], x_kinetic[1:]])
    y_full = np.concatenate([y_static, y_trans[1:], y_kinetic[1:]])
    
    # Shading regions for clarity (Static vs Kinetic)
    ax.axvspan(0, 5.0, color=BLUE, alpha=0.12)
    ax.axvspan(5.0, 9.8, color=ORANGE, alpha=0.12)
    
    # Plot dashed vertical dividing line at peak
    ax.plot([5.0, 5.0], [0, 6.0], color=GREY, linestyle="--", lw=1.5)
    
    # Plot curve
    ax.plot(x_full, y_full, color=DEEP["blue"], lw=3.5)
    
    # Peak dot
    ax.plot(5.0, 6.0, marker="o", color=DEEP["pink"], markersize=8, zorder=5)
    
    # Label for Static Friction (along the slope)
    ax.text(2.3, 3.4, "Static Friction: F = Applied Force", 
            fontsize=14, color=INK, rotation=38, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2, alpha=0.85))
    
    # Label for Limiting Friction at the peak
    ax.annotate("Limiting Friction", xy=(5.0, 6.0), xytext=(5.0, 7.2),
                fontsize=15, color=INK, ha="center", va="center", weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Label for Dynamic (Kinetic) Friction
    ax.text(7.5, 4.9, "Dynamic (Kinetic) Friction", 
            fontsize=14, color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2, alpha=0.85))
    
    # Region indicators at bottom
    ax.text(2.5, 0.4, "Static Region\n(Object at rest)", 
            fontsize=14, color=INK, ha="center", va="bottom", style="italic")
    ax.text(7.5, 0.4, "Kinetic Region\n(Object in motion)", 
            fontsize=14, color=INK, ha="center", va="bottom", style="italic")

    save(fig, out)
