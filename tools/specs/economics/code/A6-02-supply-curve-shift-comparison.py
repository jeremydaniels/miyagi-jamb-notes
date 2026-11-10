from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 7)
    
    # Subplot 1: Movement along the supply curve
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "Quantity (Q)", "Price (P)", 10, 10)
    ax1.set_title("Movement along the curve\n(Change in Quantity Supplied)", fontsize=15, pad=15, weight='bold', color=INK)
    
    # Supply curve 1
    x_s = np.linspace(1.5, 8.5, 100)
    y_s = 1.0 + 0.9 * x_s
    ax1.plot(x_s, y_s, color=DEEP["blue"], lw=3)
    ax1.text(8.7, y_s[-1], "S", fontsize=16, color=DEEP["blue"], weight='bold', va='center')
    
    # Points A and B
    q1, p1 = 3.5, 1.0 + 0.9 * 3.5
    q2, p2 = 6.5, 1.0 + 0.9 * 6.5
    
    # Dashed reference lines
    ax1.plot([0, q1, q1], [p1, p1, 0], color=GREY, ls="--", lw=1.5)
    ax1.plot([0, q2, q2], [p2, p2, 0], color=GREY, ls="--", lw=1.5)
    
    # Points
    ax1.scatter([q1, q2], [p1, p2], color=DEEP["blue"], s=60, zorder=5)
    ax1.text(q1 - 0.4, p1 + 0.4, "A", fontsize=15, weight='bold', color=INK)
    ax1.text(q2 - 0.4, p2 + 0.4, "B", fontsize=15, weight='bold', color=INK)
    
    # Movement arrow along the curve
    ax1.annotate("", xy=(q2 - 0.4, p2 - 0.36), xytext=(q1 + 0.4, p1 + 0.36),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, shrinkA=5, shrinkB=5))
    
    # Axis labels for points
    ax1.text(-0.3, p1, "P₁", fontsize=15, ha='right', va='center', color=INK)
    ax1.text(-0.3, p2, "P₂", fontsize=15, ha='right', va='center', color=INK)
    ax1.text(q1, -0.6, "Q₁", fontsize=15, ha='center', va='top', color=INK)
    ax1.text(q2, -0.6, "Q₂", fontsize=15, ha='center', va='top', color=INK)
    
    # Subplot 2: Shift of the supply curve
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "Quantity (Q)", "Price (P)", 10, 10)
    ax2.set_title("Shift of the curve\n(Change in Supply)", fontsize=15, pad=15, weight='bold', color=INK)
    
    # Three supply curves
    x = np.linspace(0.8, 9.2, 100)
    # Original S1
    ax2.plot(x_s, y_s, color=DEEP["blue"], lw=3)
    ax2.text(8.7, y_s[-1], "S₁", fontsize=16, color=DEEP["blue"], weight='bold', va='center')
    
    # Right shift S2
    ax2.plot(x_s + 1.8, y_s, color=DEEP["green"], lw=3)
    ax2.text(8.7 + 1.2, y_s[-1] - 1.08, "S₂", fontsize=16, color=DEEP["green"], weight='bold', va='center')
    
    # Left shift S3
    ax2.plot(x_s - 1.8, y_s, color=DEEP["pink"], lw=3)
    ax2.text(8.7 - 2.0, y_s[-1], "S₃", fontsize=16, color=DEEP["pink"], weight='bold', va='center')
    
    # Price level P1 constant
    p_const = 5.0
    q_orig = (p_const - 1.0) / 0.9
    q_right = q_orig + 1.8
    q_left = q_orig - 1.8
    
    # Dashed line across to curves
    ax2.plot([0, q_right + 0.8], [p_const, p_const], color=GREY, ls="--", lw=1.5)
    ax2.plot([q_left, q_left], [0, p_const], color=GREY, ls="--", lw=1.5)
    ax2.plot([q_orig, q_orig], [0, p_const], color=GREY, ls="--", lw=1.5)
    ax2.plot([q_right, q_right], [0, p_const], color=GREY, ls="--", lw=1.5)
    
    # Points on curves
    ax2.scatter([q_left, q_orig, q_right], [p_const, p_const, p_const], color=INK, s=40, zorder=5)
    
    # Arrows indicating shifts
    ax2.annotate("", xy=(q_right - 0.2, p_const), xytext=(q_orig + 0.2, p_const),
                 arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5))
    ax2.annotate("", xy=(q_left + 0.2, p_const), xytext=(q_orig - 0.2, p_const),
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5))
    
    # Labels
    ax2.text(-0.3, p_const, "P₁", fontsize=15, ha='right', va='center', color=INK)
    ax2.text(q_left, -0.6, "Q₃", fontsize=15, ha='center', va='top', color=INK)
    ax2.text(q_orig, -0.6, "Q₁", fontsize=15, ha='center', va='top', color=INK)
    ax2.text(q_right, -0.6, "Q₂", fontsize=15, ha='center', va='top', color=INK)
    
    # Annotations for shift meanings
    ax2.text(q_right + 0.1, p_const + 0.8, "Increase\nin supply", fontsize=14, color=DEEP["green"], weight='bold', ha='center',
             bbox=dict(fc="white", ec="none", pad=1))
    ax2.text(q_left - 0.1, p_const + 0.8, "Decrease\nin supply", fontsize=14, color=DEEP["pink"], weight='bold', ha='center',
             bbox=dict(fc="white", ec="none", pad=1))
    
    plt.subplots_adjust(wspace=0.25, bottom=0.15, top=0.88, left=0.08, right=0.95)
    save(fig, out)
