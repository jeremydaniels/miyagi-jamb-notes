from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 7.5)
    
    # Left subplot: Demand-Pull Inflation
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "Real Output (Y)", "Price Level (P)", 10, 10)
    ax1.set_title("Demand-Pull Inflation", fontsize=16, pad=15, weight='bold', color=INK)
    
    # Curves for Demand-Pull
    # AS curve: upward sloping, steepening slightly at higher output
    x_as = np.linspace(1.5, 8.5, 100)
    y_as = 1.0 + 0.5 * x_as + 0.05 * (x_as**2)
    
    # AD curves: downward sloping straight lines
    # AD1: y = -0.9 * x + 8.5
    # AD2 shifted right: y = -0.9 * (x - 2.0) + 8.5 = -0.9 * x + 10.3
    x_ad = np.linspace(1.5, 9.0, 100)
    y_ad1 = 8.5 - 0.85 * x_ad
    y_ad2 = 10.3 - 0.85 * x_ad
    
    ax1.plot(x_as, y_as, color=DEEP["blue"], lw=3)
    ax1.plot(x_ad, y_ad1, color=DEEP["orange"], lw=3)
    ax1.plot(x_ad, y_ad2, color=DEEP["pink"], lw=3, linestyle='--')
    
    # Labels for curves
    ax1.text(8.6, y_as[-1], "AS", fontsize=15, weight='bold', color=DEEP["blue"], va='center')
    ax1.text(8.8, y_ad1[-5], r"$\mathrm{AD}_1$", fontsize=15, weight='bold', color=DEEP["orange"], va='center')
    ax1.text(8.8, y_ad2[-5], r"$\mathrm{AD}_2$", fontsize=15, weight='bold', color=DEEP["pink"], va='center')
    
    # Intersections
    # P1, Y1 intersection of AS and AD1:
    # 1.0 + 0.5x + 0.05x^2 = 8.5 - 0.85x  => 0.05x^2 + 1.35x - 7.5 = 0
    # x = (-1.35 + sqrt(1.35^2 + 4*0.05*7.5)) / 0.1 = (-1.35 + sqrt(1.8225 + 1.5)) / 0.1 = (-1.35 + 1.8227) / 0.1 = 4.73
    y1_val = 4.73
    p1_val = 8.5 - 0.85 * y1_val  # 4.48
    
    # P2, Y2 intersection of AS and AD2:
    # 0.05x^2 + 1.35x - 9.3 = 0
    # x = (-1.35 + sqrt(1.8225 + 1.86)) / 0.1 = (-1.35 + 1.9189) / 0.1 = 5.69
    y2_val = 5.69
    p2_val = 10.3 - 0.85 * y2_val # 5.46
    
    # Dashed lines to axes
    ax1.plot([y1_val, y1_val], [0, p1_val], color=GREY, lw=1.5, linestyle=':')
    ax1.plot([0, y1_val], [p1_val, p1_val], color=GREY, lw=1.5, linestyle=':')
    ax1.plot([y2_val, y2_val], [0, p2_val], color=GREY, lw=1.5, linestyle=':')
    ax1.plot([0, y2_val], [p2_val, p2_val], color=GREY, lw=1.5, linestyle=':')
    
    # Points
    ax1.plot([y1_val, y2_val], [p1_val, p2_val], 'o', color=INK, markersize=6)
    
    # Axis labels for equilibrium points
    ax1.text(y1_val, -0.6, r"$Y_1$", fontsize=14, ha='center', va='top')
    ax1.text(y2_val, -0.6, r"$Y_2$", fontsize=14, ha='center', va='top')
    ax1.text(-0.6, p1_val, r"$P_1$", fontsize=14, ha='right', va='center')
    ax1.text(-0.6, p2_val, r"$P_2$", fontsize=14, ha='right', va='center')
    
    # Shift arrows
    ax1.annotate("", xy=(6.5, 5.7), xytext=(5.3, 4.7),
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5))
    ax1.text(6.0, 4.8, "AD shifts\nright", fontsize=14, color=DEEP["pink"],
             bbox=dict(fc="white", ec="none", pad=2))

    # Right subplot: Cost-Push Inflation
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "Real Output (Y)", "Price Level (P)", 10, 10)
    ax2.set_title("Cost-Push Inflation", fontsize=16, pad=15, weight='bold', color=INK)
    
    # Curves for Cost-Push
    # Single AD curve
    x_ad_cp = np.linspace(1.5, 9.0, 100)
    y_ad_cp = 9.5 - 0.85 * x_ad_cp
    
    # AS curves: AS1 and AS2 shifted left (upwards)
    x_as_cp = np.linspace(1.0, 8.5, 100)
    y_as1 = 0.5 + 0.5 * x_as_cp + 0.05 * (x_as_cp**2)
    y_as2 = 2.4 + 0.5 * x_as_cp + 0.05 * (x_as_cp**2)
    
    ax2.plot(x_ad_cp, y_ad_cp, color=DEEP["orange"], lw=3)
    ax2.plot(x_as_cp, y_as1, color=DEEP["blue"], lw=3)
    ax2.plot(x_as_cp, y_as2, color=DEEP["green"], lw=3, linestyle='--')
    
    # Labels for curves
    ax2.text(8.8, y_ad_cp[-5], "AD", fontsize=15, weight='bold', color=DEEP["orange"], va='center')
    ax2.text(8.6, y_as1[-1], r"$\mathrm{AS}_1$", fontsize=15, weight='bold', color=DEEP["blue"], va='center')
    ax2.text(8.6, y_as2[-1], r"$\mathrm{AS}_2$", fontsize=15, weight='bold', color=DEEP["green"], va='center')
    
    # Intersections
    # AS1 and AD: 0.05x^2 + 1.35x - 9.0 = 0
    # x = (-1.35 + sqrt(1.8225 + 1.8)) / 0.1 = (-1.35 + 1.9033) / 0.1 = 5.53
    y1_cp = 5.53
    p1_cp = 9.5 - 0.85 * y1_cp  # 4.80
    
    # AS2 and AD: 0.05x^2 + 1.35x - 7.1 = 0
    # x = (-1.35 + sqrt(1.8225 + 1.42)) / 0.1 = (-1.35 + 1.8007) / 0.1 = 4.51
    y2_cp = 4.51
    p2_cp = 9.5 - 0.85 * y2_cp  # 5.67
    
    # Dashed lines to axes
    ax2.plot([y1_cp, y1_cp], [0, p1_cp], color=GREY, lw=1.5, linestyle=':')
    ax2.plot([0, y1_cp], [p1_cp, p1_cp], color=GREY, lw=1.5, linestyle=':')
    ax2.plot([y2_cp, y2_cp], [0, p2_cp], color=GREY, lw=1.5, linestyle=':')
    ax2.plot([0, y2_cp], [p2_cp, p2_cp], color=GREY, lw=1.5, linestyle=':')
    
    # Points
    ax2.plot([y1_cp, y2_cp], [p1_cp, p2_cp], 'o', color=INK, markersize=6)
    
    # Axis labels for equilibrium points
    ax2.text(y1_cp, -0.6, r"$Y_1$", fontsize=14, ha='center', va='top')
    ax2.text(y2_cp, -0.6, r"$Y_2$", fontsize=14, ha='center', va='top')
    ax2.text(-0.6, p1_cp, r"$P_1$", fontsize=14, ha='right', va='center')
    ax2.text(-0.6, p2_cp, r"$P_2$", fontsize=14, ha='right', va='center')
    
    # Shift arrows
    ax2.annotate("", xy=(3.0, 5.8), xytext=(4.3, 4.4),
                 arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5))
    ax2.text(2.6, 4.3, "AS shifts\nleft", fontsize=14, color=DEEP["green"],
             bbox=dict(fc="white", ec="none", pad=2))
    
    save(fig, out)
