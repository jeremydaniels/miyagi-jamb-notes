from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Quantity", "Price/Cost", 8, 16)

    # Calculate consistent textbook cost curves:
    # Let FC = 12.5, VC(q) = 0.25*q^3 - 2*q^2 + 6*q
    # This gives:
    # AVC(q) = 0.25*q^2 - 2*q + 6
    # MC(q) = 0.75*q^2 - 4*q + 6
    # AC(q) = 0.25*q^2 - 2*q + 6 + 12.5/q
    
    # Derivations:
    # Min AVC occurs where dAVC/dq = 0.5*q - 2 = 0 => q_sd = 4
    # At q=4, min AVC = 4 - 8 + 6 = 2. MC(4) = 12 - 16 + 6 = 2.
    # Min AC occurs where dAC/dq = 0.5*q - 2 - 12.5/q^2 = 0 => 0.5*q^3 - 2*q^2 - 12.5 = 0
    # Solving for q: q = 5.
    # At q=5, AC(5) = 6.25 - 10 + 6 + 2.5 = 4.75. MC(5) = 18.75 - 20 + 6 = 4.75.
    
    q_sd, p_sd = 4.0, 2.0
    q_be, p_be = 5.0, 4.75

    q = np.linspace(1.5, 7.5, 300)
    avc = 0.25 * q**2 - 2 * q + 6
    ac = avc + 12.5 / q

    q_below = np.linspace(1.5, q_sd, 100)
    mc_below = 0.75 * q_below**2 - 4 * q_below + 6

    q_above = np.linspace(q_sd, 7.5, 200)
    mc_above = 0.75 * q_above**2 - 4 * q_above + 6

    # Guide lines for break-even and shut-down points
    ax.plot([0, q_be], [p_be, p_be], color=GREY, linestyle="--", lw=1.5)
    ax.plot([0, q_sd], [p_sd, p_sd], color=GREY, linestyle="--", lw=1.5)

    # Plot AC and AVC curves
    ax.plot(q, ac, color=DEEP["blue"], lw=2.5, label="AC")
    ax.plot(q, avc, color=DEEP["green"], lw=2.5, label="AVC")

    # Plot MC portions
    ax.plot(q_below, mc_below, color=GREY, linestyle="--", lw=2.0)
    ax.plot(q_above, mc_above, color=DEEP["orange"], lw=4.5, solid_capstyle="round")

    # Intersection points
    ax.plot(q_sd, p_sd, 'o', color=DEEP["orange"], markersize=8, zorder=5)
    ax.plot(q_be, p_be, 'o', color=DEEP["blue"], markersize=8, zorder=5)

    # Curve labels
    ax.text(7.6, ac[-1], "AC", color=DEEP["blue"], fontsize=15, fontweight="bold", va="center")
    ax.text(7.6, avc[-1], "AVC", color=DEEP["green"], fontsize=15, fontweight="bold", va="center")
    ax.text(7.6, mc_above[-1], "MC", color=DEEP["orange"], fontsize=15, fontweight="bold", va="center")

    # Horizontal line labels
    ax.text(0.3, p_be + 0.4, "Break-even point", color=INK, fontsize=14,
            bbox=dict(fc="white", ec="none", pad=1.5))
    ax.text(0.3, p_sd + 0.4, "Shut-down point ($P = \\min AVC$)", color=INK, fontsize=14,
            bbox=dict(fc="white", ec="none", pad=1.5))

    # Supply curve annotation
    ax.annotate("Firm's Short-Run\nSupply Curve", 
                xy=(6.2, 0.75*(6.2)**2 - 4*6.2 + 6), 
                xytext=(3.5, 12),
                fontsize=15, fontweight="bold", color=DEEP["orange"],
                ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0),
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.4", lw=1.5))

    save(fig, out)
