from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 11)
    
    # Create two vertically stacked subplots
    ax1 = fig.add_axes([0.15, 0.54, 0.78, 0.38])
    ax2 = fig.add_axes([0.15, 0.08, 0.78, 0.38])
    
    # Mathematical formulation of TP, MP, AP
    # Let TP(L) = -a*L^3 + b*L^2 + c*L
    # Then AP(L) = -a*L^2 + b*L + c
    # MP(L) = -3a*L^2 + 2b*L + c
    # This ensures MP and AP start at c > 0, typical for textbook curves.
    
    a = 0.5
    b = 3.0
    c = 7.5
    
    # AP max occurs when dAP/dL = -2a*L + b = 0 => L = b / 2a = 3.0
    L1 = b / (2 * a)  # 3.0
    
    # TP max occurs when MP = 0 => -3a*L^2 + 2b*L + c = 0
    # For a=0.5, b=3.0, c=7.5, MP = -1.5*L^2 + 6*L + 7.5 = 0
    # Roots: L = 5.0 (and L = -1.0)
    L2 = 5.0
    
    L = np.linspace(0, 6.2, 400)
    
    tp = -a * L**3 + b * L**2 + c * L
    ap = -a * L**2 + b * L + c
    mp = -3 * a * L**2 + 2 * b * L + c
    
    tp_max = -a * L2**3 + b * L2**2 + c * L2   # 50.0
    ap_max = -a * L1**2 + b * L1 + c           # 12.0
    
    # Setup axes
    for ax in [ax1, ax2]:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['left'].set_linewidth(1.8)
        ax.spines['bottom'].set_color(INK)
        ax.spines['bottom'].set_linewidth(1.8)
        ax.set_xlim(0, 6.5)
    
    # Custom axes configuration
    ax1.set_ylim(0, 58)
    ax2.set_ylim(-15, 18)
    
    # Hide standard numeric ticks
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    # Labels as per description
    ax1.set_ylabel("Output", fontsize=15, color=INK, fontweight='bold', labelpad=10)
    ax2.set_ylabel("Output", fontsize=15, color=INK, fontweight='bold', labelpad=10)
    ax2.set_xlabel("Quantity of Labour (Variable Input)", fontsize=15, color=INK, fontweight='bold', labelpad=10)
    
    # Reference zero line on ax2
    ax2.axhline(0, color=GREY, lw=1.2, ls="-")
    
    # Vertical Stage dividing lines (dashed across both axes exactly aligning with coordinates)
    for l_val in [L1, L2]:
        ax1.axvline(l_val, color=GREY, lw=1.5, ls="--", zorder=0)
        ax2.axvline(l_val, color=GREY, lw=1.5, ls="--", zorder=0)
    
    # Draw curves
    ax1.plot(L, tp, color=DEEP["blue"], lw=3.5, label="Total Product (TP)", zorder=3)
    ax2.plot(L, ap, color=DEEP["green"], lw=3.5, label="Average Product (AP)", zorder=3)
    ax2.plot(L, mp, color=DEEP["orange"], lw=3.5, label="Marginal Product (MP)", zorder=3)
    
    # Points of interest
    # Peak TP
    ax1.plot(L2, tp_max, 'o', color=DEEP["blue"], markersize=8, zorder=4)
    ax1.annotate("Max TP", xy=(L2, tp_max), xytext=(L2 - 0.7, tp_max + 2.0),
                 fontsize=14, color=INK, fontweight='bold',
                 bbox=dict(fc="white", ec="none", pad=2))
                 
    # AP max = MP intersection
    ax2.plot(L1, ap_max, 'o', color=DEEP["green"], markersize=8, zorder=4)
    ax2.annotate("AP = MP\n(Max AP)", xy=(L1, ap_max), xytext=(L1 - 0.3, ap_max + 2.5),
                 fontsize=14, color=INK, fontweight='bold', ha='center',
                 bbox=dict(fc="white", ec="none", pad=2))
                 
    # MP = 0
    ax2.plot(L2, 0, 'o', color=DEEP["orange"], markersize=8, zorder=4)
    ax2.annotate("MP = 0", xy=(L2, 0), xytext=(L2 + 0.2, 1.5),
                 fontsize=14, color=INK, fontweight='bold',
                 bbox=dict(fc="white", ec="none", pad=2))
                 
    # Curve labels on curves (placed carefully to avoid overlap)
    ax1.text(L[-1] + 0.1, tp[-1], "TP", color=DEEP["blue"], fontsize=16, fontweight='bold', va='center', bbox=dict(fc="white", ec="none", pad=1))
    ax2.text(L[-1] + 0.1, ap[-1], "AP", color=DEEP["green"], fontsize=16, fontweight='bold', va='center', bbox=dict(fc="white", ec="none", pad=1))
    ax2.text(L[-1] + 0.1, mp[-1], "MP", color=DEEP["orange"], fontsize=16, fontweight='bold', va='center', bbox=dict(fc="white", ec="none", pad=1))

    # Stage labels at the top of ax1
    stage_y = 53
    ax1.text(L1 / 2.0, stage_y, "Stage 1", fontsize=15, fontweight='bold', color=INK, ha='center',
             bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3", lw=1.2))
    ax1.text((L1 + L2) / 2.0, stage_y, "Stage 2", fontsize=15, fontweight='bold', color=INK, ha='center',
             bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3", lw=1.2))
    ax1.text((L2 + 6.0) / 2.0, stage_y, "Stage 3", fontsize=15, fontweight='bold', color=INK, ha='center',
             bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3", lw=1.2))
             
    # Panel titles
    ax1.set_title("Total Product (TP) Curve", fontsize=16, color=INK, fontweight='bold', pad=12)
    ax2.set_title("Average Product (AP) & Marginal Product (MP) Curves", fontsize=16, color=INK, fontweight='bold', pad=12)
    
    save(fig, out)
