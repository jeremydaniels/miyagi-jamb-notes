from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    
    # Set up axes
    axes_clean(ax, "Quantity (Q)", "Price (P)", 10, 10)
    
    # Define curves:
    # Supply curve S: upward sloping: P = 1.0 + 0.8 * Q
    # Demand curve D1: downward sloping: P = 8.5 - 0.9 * Q
    # Demand curve D2: shifted right: P = 11.2 - 0.9 * Q
    
    qs = np.linspace(1.2, 8.8, 100)
    supply = 1.0 + 0.8 * qs
    
    qd1 = np.linspace(1.2, 8.2, 100)
    demand1 = 8.5 - 0.9 * qd1
    
    qd2 = np.linspace(2.5, 9.5, 100)
    demand2 = 11.2 - 0.9 * qd2
    
    # Equilibrium points:
    # E1: 1.0 + 0.8 * Q = 8.5 - 0.9 * Q  => 1.7 * Q = 7.5 => Q1 = 7.5 / 1.7 ≈ 4.412
    q1 = 7.5 / 1.7
    p1 = 1.0 + 0.8 * q1
    
    # E2: 1.0 + 0.8 * Q = 11.2 - 0.9 * Q => 1.7 * Q = 10.2 => Q2 = 6.0
    q2 = 10.2 / 1.7
    p2 = 1.0 + 0.8 * q2
    
    # Plot curves
    ax.plot(qs, supply, color=DEEP["green"], lw=3.5, label="Supply (S)")
    ax.plot(qd1, demand1, color=DEEP["blue"], lw=3.5, label="Demand (D1)")
    ax.plot(qd2, demand2, color=DEEP["orange"], lw=3.5, label="Demand (D2)")
    
    # Curve labels
    ax.text(qs[-1] + 0.15, supply[-1], "S", fontsize=16, color=DEEP["green"], fontweight="bold", va="center")
    ax.text(qd1[-1] + 0.15, demand1[-1], "D₁", fontsize=16, color=DEEP["blue"], fontweight="bold", va="center")
    ax.text(qd2[-1] + 0.15, demand2[-1], "D₂", fontsize=16, color=DEEP["orange"], fontweight="bold", va="center")
    
    # Dashed guidelines for E1
    ax.plot([0, q1], [p1, p1], color=GREY, lw=1.5, ls="--")
    ax.plot([q1, q1], [0, p1], color=GREY, lw=1.5, ls="--")
    
    # Dashed guidelines for E2
    ax.plot([0, q2], [p2, p2], color=GREY, lw=1.5, ls="--")
    ax.plot([q2, q2], [0, p2], color=GREY, lw=1.5, ls="--")
    
    # Equilibrium dots and labels
    ax.plot(q1, p1, marker="o", color=INK, markersize=7)
    ax.text(q1 - 0.45, p1 + 0.35, "E₁", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    ax.plot(q2, p2, marker="o", color=INK, markersize=7)
    ax.text(q2 + 0.35, p2 + 0.2, "E₂", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Axis labels for P1, P2, Q1, Q2
    ax.text(-0.3, p1, "P₁", fontsize=15, fontweight="bold", color=INK, ha="right", va="center")
    ax.text(-0.3, p2, "P₂", fontsize=15, fontweight="bold", color=INK, ha="right", va="center")
    
    ax.text(q1, -0.45, "Q₁", fontsize=15, fontweight="bold", color=INK, ha="center", va="top")
    ax.text(q2, -0.45, "Q₂", fontsize=15, fontweight="bold", color=INK, ha="center", va="top")
    
    # Arrow for rightward demand shift between D1 and D2
    shift_y = 6.8
    x_d1 = (8.5 - shift_y) / 0.9
    x_d2 = (11.2 - shift_y) / 0.9
    ax.annotate("", xy=(x_d2 - 0.15, shift_y), xytext=(x_d1 + 0.15, shift_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18))
    ax.text((x_d1 + x_d2) / 2, shift_y + 0.45, "Shift in Demand", fontsize=14, color=DEEP["pink"],
            fontweight="bold", ha="center", bbox=dict(fc="white", ec="none", pad=2))
    
    # Arrow for upward movement from P1 to P2
    ax.annotate("", xy=(-0.3, p2 - 0.15), xytext=(-0.3, p1 + 0.15),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.2, mutation_scale=15),
                annotation_clip=False)
    
    # Arrow for rightward movement from Q1 to Q2
    ax.annotate("", xy=(q2 - 0.15, -0.45), xytext=(q1 + 0.15, -0.45),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.2, mutation_scale=15),
                annotation_clip=False)
    
    # Title
    ax.set_title("Rightward Shift in Demand", fontsize=17, fontweight="bold", pad=20, color=INK)
    
    save(fig, out)
