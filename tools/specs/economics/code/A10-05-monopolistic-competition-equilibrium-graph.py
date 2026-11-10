from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes limits
    xmax, ymax = 10, 10
    axes_clean(ax, "Quantity (Q)", "Price / Cost (P, C)", xmax, ymax)
    
    # Mathematical setup for exact tangency and intersection:
    # Demand (AR): linear downward sloping
    # Let AR(Q) = a - b * Q
    # MR(Q) = a - 2 * b * Q
    # Let equilibrium be at Q_e = 4.0, P_e = 5.2
    # Slope of AR: -b. Choose b = 0.8 => a = 5.2 + 0.8 * 4.0 = 8.4
    # AR = 8.4 - 0.8 * Q
    # MR = 8.4 - 1.6 * Q
    # At Q_e = 4.0:
    # AR(4.0) = 5.2
    # MR(4.0) = 8.4 - 6.4 = 2.0
    #
    # LAC curve: U-shaped, must have LAC(4.0) = 5.2 and LAC'(4.0) = -0.8 (tangent to AR)
    # Quadratic LAC: LAC(Q) = c * (Q - Q_min)^2 + LAC_min
    # LAC'(Q) = 2 * c * (Q - Q_min)
    # At Q=4: 2 * c * (4 - Q_min) = -0.8 => c * (4 - Q_min) = -0.4
    # Let minimum of LAC be at Q_min = 6.0
    # Then 4 - 6.0 = -2.0 => c * (-2.0) = -0.4 => c = 0.2
    # LAC(4.0) = 0.2 * (4 - 6)^2 + LAC_min = 0.2 * 4 + LAC_min = 0.8 + LAC_min = 5.2
    # => LAC_min = 4.4
    # LAC(Q) = 0.2 * (Q - 6)^2 + 4.4
    # Total Cost LTC(Q) = Q * LAC(Q) = 0.2 * Q * (Q - 6)^2 + 4.4 * Q
    # LMC(Q) = d(LTC)/dQ = LAC(Q) + Q * LAC'(Q)
    # LMC(Q) = [0.2 * (Q - 6)^2 + 4.4] + Q * [0.4 * (Q - 6)]
    # At Q = 4.0:
    # LMC(4.0) = 5.2 + 4.0 * (-0.8) = 5.2 - 3.2 = 2.0
    
    Q = np.linspace(0.8, 8.5, 200)
    
    ar = 8.4 - 0.8 * Q
    # Stop MR earlier so the label doesn't overlap the x-axis
    mr_q = np.linspace(0.5, 4.9, 150)
    mr = 8.4 - 1.6 * mr_q
    
    lac = 0.2 * (Q - 6.0)**2 + 4.4
    lmc = lac + Q * (0.4 * (Q - 6.0))
    
    # Filter LMC within reasonable plot bounds
    mask_lmc = (lmc >= 0.5) & (lmc <= 9.2) & (Q <= 8.5)
    
    # Plot curves
    ax.plot(Q, ar, color=DEEP["blue"], lw=3.0, label="AR = D")
    ax.plot(mr_q, mr, color=DEEP["pink"], lw=3.0, label="MR")
    ax.plot(Q, lac, color=DEEP["green"], lw=3.0, label="LAC")
    ax.plot(Q[mask_lmc], lmc[mask_lmc], color=DEEP["orange"], lw=3.0, label="LMC")
    
    # Equilibrium point coordinates
    Q_e = 4.0
    P_e = 5.2
    MC_e = 2.0
    
    # Dashed guide lines
    ax.plot([Q_e, Q_e], [0, P_e], color=GREY, lw=1.8, linestyle="--")
    ax.plot([0, Q_e], [P_e, P_e], color=GREY, lw=1.8, linestyle="--")
    ax.plot([0, Q_e], [MC_e, MC_e], color=GREY, lw=1.8, linestyle=":")
    
    # Mark points
    ax.plot(Q_e, P_e, marker="o", markersize=7, color=DEEP["blue"], zorder=5)
    ax.plot(Q_e, MC_e, marker="o", markersize=7, color=DEEP["orange"], zorder=5)
    
    # Annotate curves at their ends
    ax.text(8.6, ar[-1], "AR", fontsize=15, color=DEEP["blue"], va="center", weight="bold")
    ax.text(mr_q[-1] + 0.1, mr[-1], "MR", fontsize=15, color=DEEP["pink"], va="center", weight="bold")
    ax.text(8.6, lac[-1], "LAC", fontsize=15, color=DEEP["green"], va="center", weight="bold")
    ax.text(Q[mask_lmc][-1] + 0.1, lmc[mask_lmc][-1], "LMC", fontsize=15, color=DEEP["orange"], va="center", weight="bold")
    
    # Key annotations
    ax.annotate("Tangency point\n(P = LAC, Normal profit)",
                xy=(Q_e, P_e), xytext=(Q_e + 1.2, P_e + 1.8),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax.annotate("LMC = MR",
                xy=(Q_e, MC_e), xytext=(Q_e + 1.4, MC_e - 0.7),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Axis ticks / labels for equilibrium
    ax.set_xticks([Q_e])
    ax.set_xticklabels([r"$Q_e$"], fontsize=16)
    ax.set_yticks([MC_e, P_e])
    ax.set_yticklabels([r"$MR_e$", r"$P_e$"], fontsize=16)
    
    # Diagram title
    ax.set_title("Long-Run Equilibrium in Monopolistic Competition", fontsize=16, color=INK, pad=15)
    
    save(fig, out)
