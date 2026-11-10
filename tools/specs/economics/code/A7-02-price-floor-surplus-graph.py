from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    
    # Clean axes with Price and Quantity
    axes_clean(ax, "Quantity (Q)", "Price (P)", 10, 10)
    
    # Linear supply and demand curves
    # Demand: P = 9 - 0.8*Q => Q = (9 - P)/0.8
    # Supply: P = 1 + 0.8*Q => Q = (P - 1)/0.8
    # Intersection: 9 - 0.8*Q = 1 + 0.8*Q => 1.6*Q = 8 => Q_e = 5, P_e = 5
    q = np.linspace(0.8, 9.2, 100)
    p_demand = 9.0 - 0.8 * q
    p_supply = 1.0 + 0.8 * q
    
    ax.plot(q, p_demand, color=DEEP["blue"], lw=3.5)
    ax.plot(q, p_supply, color=DEEP["orange"], lw=3.5)
    
    # Curve labels
    ax.text(9.3, 1.6, "Demand (D)", color=DEEP["blue"], fontsize=15, va="center", weight="bold")
    ax.text(9.3, 8.4, "Supply (S)", color=DEEP["orange"], fontsize=15, va="center", weight="bold")
    
    # Equilibrium point
    q_e, p_e = 5.0, 5.0
    ax.plot([0, q_e], [p_e, p_e], color=GREY, ls="--", lw=1.5)
    ax.plot([q_e, q_e], [0, p_e], color=GREY, ls="--", lw=1.5)
    ax.scatter([q_e], [p_e], color=INK, s=40, zorder=5)
    
    # Minimum Price (Price Floor) above P_e
    p_min = 7.0
    # Q_d at p_min: (9 - 7)/0.8 = 2.5
    # Q_s at p_min: (7 - 1)/0.8 = 7.5
    q_d = 2.5
    q_s = 7.5
    
    # Minimum price line across graph
    ax.axhline(p_min, color=DEEP["pink"], lw=2.5, ls="-")
    ax.text(9.3, p_min, "Minimum Price\n(Price Floor)", color=DEEP["pink"], fontsize=14, va="center", weight="bold")
    
    # Dashed drop lines for Q_d and Q_s
    ax.plot([q_d, q_d], [0, p_min], color=GREY, ls="--", lw=1.5)
    ax.plot([q_s, q_s], [0, p_min], color=GREY, ls="--", lw=1.5)
    ax.scatter([q_d, q_s], [p_min, p_min], color=DEEP["pink"], s=45, zorder=5)
    
    # Axis tick labels (custom clean positions)
    ax.text(-0.3, p_e, r"$P_e$", fontsize=16, ha="right", va="center", color=INK)
    ax.text(-0.3, p_min, r"$P_{min}$", fontsize=16, ha="right", va="center", color=DEEP["pink"], weight="bold")
    
    ax.text(q_e, -0.4, r"$Q_e$", fontsize=16, ha="center", va="top", color=INK)
    ax.text(q_d, -0.4, r"$Q_d$", fontsize=16, ha="center", va="top", color=INK)
    ax.text(q_s, -0.4, r"$Q_s$", fontsize=16, ha="center", va="top", color=INK)
    
    # Double-headed arrow / bracket indicating Surplus (Excess Supply)
    arrow_y = 7.4
    ax.annotate(
        "", xy=(q_d, arrow_y), xytext=(q_s, arrow_y),
        arrowprops=dict(arrowstyle="<->", color=INK, lw=2, shrinkA=0, shrinkB=0)
    )
    ax.text((q_d + q_s) / 2, arrow_y + 0.35, "Surplus (Excess Supply)",
            fontsize=15, ha="center", va="bottom", color=INK, weight="bold",
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Shading the surplus area lightly between Qd and Qs along the min price
    ax.fill_between([q_d, q_e, q_s], [p_min, p_e, p_min], [p_min, p_min, p_min],
                    color=CREAM, alpha=0.6, zorder=1)
    
    save(fig, out)
