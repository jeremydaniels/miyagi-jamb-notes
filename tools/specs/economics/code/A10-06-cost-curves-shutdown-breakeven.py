from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    axes_clean(ax, "Quantity (Q)", "Cost / Price ($)", 9, 10)
    
    # TVC = a*q^3 + b*q^2 + c*q
    # AVC = a*q^2 + b*q + c
    # MC = 3a*q^2 + 2b*q + c
    # ATC = a*q^2 + b*q + c + FC/q
    # Min AVC at q=3.5: 2a(3.5) + b = 0 => b = -7a
    # Min ATC at q=6.0: 2a(6) + b - FC/6^2 = 0 => 12a - 7a = FC/36 => 5a = FC/36 => FC = 180a
    
    a = 0.08
    b = -0.56
    c = 3.5
    FC = 14.4
    
    q_vals = np.linspace(0.8, 8.5, 300)
    avc_vals = a * q_vals**2 + b * q_vals + c
    atc_vals = avc_vals + FC / q_vals
    mc_vals = 3 * a * q_vals**2 + 2 * b * q_vals + c
    
    # Clip values to avoid plotting too far outside the visible area
    mc_mask = mc_vals <= 11
    atc_mask = atc_vals <= 11
    
    ax.plot(q_vals[mc_mask], mc_vals[mc_mask], color=DEEP["orange"], lw=3.2, label="MC")
    ax.plot(q_vals[atc_mask], atc_vals[atc_mask], color=DEEP["blue"], lw=3.2, label="ATC")
    ax.plot(q_vals, avc_vals, color=DEEP["green"], lw=3.2, label="AVC")
    
    # Reference points
    q_avc_min = 3.5
    p_avc_min = a * q_avc_min**2 + b * q_avc_min + c
    
    q_atc_min = 6.0
    p_atc_min = a * q_atc_min**2 + b * q_atc_min + c + FC / q_atc_min
    
    # Points at minima
    ax.plot(q_avc_min, p_avc_min, 'o', color=DEEP["green"], markersize=7, zorder=5)
    ax.plot(q_atc_min, p_atc_min, 'o', color=DEEP["blue"], markersize=7, zorder=5)
    
    # Horizontal dashed lines
    ax.axhline(y=p_atc_min, xmin=0, xmax=q_atc_min/9.0, color=GREY, ls="--", lw=1.8)
    ax.axhline(y=p_avc_min, xmin=0, xmax=q_avc_min/9.0, color=GREY, ls="--", lw=1.8)
    
    # Text labels for Break-even and Shut-down points
    ax.text(0.3, p_atc_min + 0.3, "Break-even point", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(0.3, p_avc_min + 0.3, "Shut-down point", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    
    # Curve name annotations at the right ends
    q_end_mc = q_vals[mc_mask][-1]
    p_end_mc = mc_vals[mc_mask][-1]
    ax.text(q_end_mc + 0.15, p_end_mc, "MC", fontsize=15, weight="bold", color=DEEP["orange"], va="center")
    
    q_end_atc = q_vals[atc_mask][-1]
    p_end_atc = atc_vals[atc_mask][-1]
    ax.text(q_end_atc + 0.15, p_end_atc, "ATC", fontsize=15, weight="bold", color=DEEP["blue"], va="center")
    
    ax.text(q_vals[-1] + 0.15, avc_vals[-1], "AVC", fontsize=15, weight="bold", color=DEEP["green"], va="center")
    
    ax.plot([q_avc_min, q_avc_min], [0, p_avc_min], ls=":", color=GREY, lw=1.5)
    ax.plot([q_atc_min, q_atc_min], [0, p_atc_min], ls=":", color=GREY, lw=1.5)
    
    ax.set_title("Short-Run Cost Curves (ATC, AVC, MC)", fontsize=16, pad=12, color=INK)
    
    save(fig, out)
