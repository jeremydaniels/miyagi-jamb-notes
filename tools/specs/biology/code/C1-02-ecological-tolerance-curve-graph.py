from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    
    # Range of x from 0 to 100
    x = np.linspace(0, 100, 500)
    # Bell-shaped curve (normal distribution curve)
    mu = 50.0
    sigma = 13.0
    y = np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    # Scale y so max is roughly 85-90
    y = y * 85.0
    
    # Boundary definitions
    # Intolerance zones: x < 15 and x > 85
    # Stress zones: 15 <= x < 35 and 65 < x <= 85
    # Optimum zone: 35 <= x <= 65
    x_low_limit = 18.0
    x_opt_low = 36.0
    x_opt_high = 64.0
    x_high_limit = 82.0
    
    # Pale colors
    c_intolerance = "#FFEAEA"  # pale red / reddish pink
    c_stress = "#FFF8D6"       # pale yellow
    c_optimum = "#E2F5E5"      # pale soft green

    # Shading regions under curve
    # 1. Left intolerance
    mask_intol_left = (x <= x_low_limit)
    ax.fill_between(x[mask_intol_left], 0, y[mask_intol_left], color=c_intolerance, alpha=0.9)
    # Fill also the flat area to the left
    ax.fill_between([0, x_low_limit], 0, [0, 0], color=c_intolerance, alpha=0.9)

    # 2. Left stress
    mask_stress_left = (x >= x_low_limit) & (x <= x_opt_low)
    ax.fill_between(x[mask_stress_left], 0, y[mask_stress_left], color=c_stress, alpha=0.9)

    # 3. Optimum
    mask_opt = (x >= x_opt_low) & (x <= x_opt_high)
    ax.fill_between(x[mask_opt], 0, y[mask_opt], color=c_optimum, alpha=0.9)

    # 4. Right stress
    mask_stress_right = (x >= x_opt_high) & (x <= x_high_limit)
    ax.fill_between(x[mask_stress_right], 0, y[mask_stress_right], color=c_stress, alpha=0.9)

    # 5. Right intolerance
    mask_intol_right = (x >= x_high_limit)
    ax.fill_between(x[mask_intol_right], 0, y[mask_intol_right], color=c_intolerance, alpha=0.9)

    # Draw the main bell-shaped curve
    ax.plot(x, y, color=DEEP["green"], lw=3.5)

    # Vertical dividing dashed lines
    div_y_max = 95
    for div_x in [x_low_limit, x_opt_low, x_opt_high, x_high_limit]:
        ax.plot([div_x, div_x], [0, div_y_max], color=GREY, ls="--", lw=1.5, zorder=3)

    # Clean axes
    axes_clean(ax, "environmental factor (e.g. temperature)", "number of organisms", 100, 105)
    
    # Annotate zones at the top
    # Zone of intolerance (left)
    ax.text(x_low_limit / 2.0, 98, "zone of\nintolerance", ha="center", va="center", 
            fontsize=11.5, color=INK, fontweight="bold")
    # Zone of stress (left)
    ax.text((x_low_limit + x_opt_low) / 2.0, 98, "zone of\nstress", ha="center", va="center", 
            fontsize=12, color=INK, fontweight="bold")
    # Optimum range (center)
    ax.text(50.0, 98, "optimum range", ha="center", va="center", 
            fontsize=13, color=INK, fontweight="bold")
    # Zone of stress (right)
    ax.text((x_opt_high + x_high_limit) / 2.0, 98, "zone of\nstress", ha="center", va="center", 
            fontsize=12, color=INK, fontweight="bold")
    # Zone of intolerance (right)
    ax.text((x_high_limit + 100) / 2.0, 98, "zone of\nintolerance", ha="center", va="center", 
            fontsize=11.5, color=INK, fontweight="bold")

    # Lower and upper limits of tolerance annotations
    ax.annotate("lower limit\nof tolerance", 
                xy=(x_low_limit, 8), 
                xytext=(x_low_limit - 4, 35),
                ha="right", va="center", fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9))

    ax.annotate("upper limit\nof tolerance", 
                xy=(x_high_limit, 8), 
                xytext=(x_high_limit + 4, 35),
                ha="left", va="center", fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", alpha=0.9))

    # Low to High indicator along x-axis
    ax.text(3, -7, "Low", ha="left", va="top", fontsize=11, color=GREY, fontstyle="italic")
    ax.text(97, -7, "High", ha="right", va="top", fontsize=11, color=GREY, fontstyle="italic")

    # Adjust layout and save
    plt.tight_layout()
    save(fig, out)
