import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes setup
    axes_clean(ax, "Quantity", "Price", 10, 10)
    
    # Demand curves: P = -Q + intercept  =>  intercepts: D3=6.5, D1=9.0, D2=11.5
    # Let's plot lines over relevant ranges
    q = np.linspace(0.8, 9.2, 200)
    
    # D1 (middle)
    p_d1 = 9.0 - q
    # D3 (left)
    p_d3 = 6.5 - q
    # D2 (right)
    p_d2 = 11.5 - q
    
    # Clip to valid display range
    m1 = (p_d1 >= 0.8) & (p_d1 <= 8.5)
    m3 = (p_d3 >= 0.8) & (p_d3 <= 6.0)
    m2 = (p_d2 >= 2.5) & (p_d2 <= 8.5)
    
    ax.plot(q[m3], p_d3[m3], color=DEEP["pink"], lw=3.2)
    ax.plot(q[m1], p_d1[m1], color=DEEP["blue"], lw=3.5)
    ax.plot(q[m2], p_d2[m2], color=DEEP["green"], lw=3.2)
    
    # Fixed Price P
    P_val = 4.8
    # Intersection quantities
    q3 = 6.5 - P_val  # 1.7
    q1 = 9.0 - P_val  # 4.2
    q2 = 11.5 - P_val # 6.7
    
    # Horizontal dashed line for Price P
    ax.axhline(P_val, xmin=0, xmax=8.2/10, color=GREY, ls="--", lw=1.8, zorder=1)
    ax.text(-0.35, P_val, "P", fontsize=16, fontweight="bold", color=INK, va="center", ha="right")
    
    # Curve labels at the lower-right ends of each line
    ax.text(q[m3][-1] + 0.15, p_d3[m3][-1], r"$D_3$", fontsize=16, fontweight="bold", color=DEEP["pink"], va="top")
    ax.text(q[m1][-1] + 0.15, p_d1[m1][-1], r"$D_1$", fontsize=16, fontweight="bold", color=DEEP["blue"], va="top")
    ax.text(q[m2][-1] + 0.15, p_d2[m2][-1], r"$D_2$", fontsize=16, fontweight="bold", color=DEEP["green"], va="top")
    
    # Intersection points
    ax.scatter([q3, q1, q2], [P_val, P_val, P_val], color=[DEEP["pink"], DEEP["blue"], DEEP["green"]], s=55, zorder=4)
    
    # Vertical dashed lines down to quantity axis
    for q_pt, col, q_lbl in [(q3, DEEP["pink"], r"$Q_3$"), (q1, DEEP["blue"], r"$Q_1$"), (q2, DEEP["green"], r"$Q_2$")]:
        ax.plot([q_pt, q_pt], [0, P_val], color=col, ls=":", lw=1.5, alpha=0.8, zorder=1)
        ax.text(q_pt, -0.4, q_lbl, fontsize=15, color=INK, ha="center", va="top")
    
    # Shift arrows and annotations at P level or slightly above
    # Arrow D1 -> D2: Increase in Demand (Rightward Shift)
    arrow_y_inc = 6.2
    q_start_inc = 9.0 - arrow_y_inc
    q_end_inc = 11.5 - arrow_y_inc
    ax.annotate("", xy=(q_end_inc - 0.1, arrow_y_inc), xytext=(q_start_inc + 0.1, arrow_y_inc),
                arrowprops=dict(arrowstyle="->", lw=2.2, color=DEEP["green"]))
    ax.text((q_start_inc + q_end_inc) / 2, arrow_y_inc + 0.35, "Increase in Demand\n(Rightward Shift)",
            fontsize=14, color=DEEP["green"], ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Arrow D1 -> D3: Decrease in Demand (Leftward Shift)
    arrow_y_dec = 3.2
    q_start_dec = 9.0 - arrow_y_dec
    q_end_dec = 6.5 - arrow_y_dec
    ax.annotate("", xy=(q_end_dec + 0.1, arrow_y_dec), xytext=(q_start_dec - 0.1, arrow_y_dec),
                arrowprops=dict(arrowstyle="->", lw=2.2, color=DEEP["pink"]))
    ax.text((q_start_dec + q_end_dec) / 2, arrow_y_dec - 0.4, "Decrease in Demand\n(Leftward Shift)",
            fontsize=14, color=DEEP["pink"], ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=2))

    save(fig, out)
