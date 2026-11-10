from style import *
import numpy as np

def draw(out):
    # Two-panel vertically aligned canvas: top for TP, bottom for AP and MP
    fig = canvas(10, 11)
    
    # Grid layout with shared x-axis
    gs = fig.add_gridspec(2, 1, height_ratios=[1.1, 1], hspace=0.18, left=0.12, right=0.92, top=0.92, bottom=0.08)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharex=ax1)

    # Mathematical formulation for classical cubic production function:
    # TP = a * L^2 - b * L^3 = L^2 * (a - b*L)
    # AP = TP / L = a * L - b * L^2
    # MP = d(TP)/dL = 2 * a * L - 3 * b * L^2
    # Let max AP occur at L = 4.5. Then d(AP)/dL = a - 2*b*L = 0 => a = 2 * b * 4.5 = 9 * b.
    # Set b = 1, so a = 9.
    # TP(L) = 9*L^2 - L^3
    # AP(L) = 9*L - L^2
    # MP(L) = 18*L - 3*L^2 = 3*L*(6 - L)
    # Peak MP at L = 3, MP(3) = 27
    # MP = AP at L = 4.5: AP(4.5) = 40.5 - 20.25 = 20.25; MP(4.5) = 81 - 60.75 = 20.25 (Stage I boundary)
    # MP = 0 at L = 6: TP is maximum at L = 6, TP(6) = 9*36 - 216 = 108 (Stage II boundary)
    # Stage III: L > 6, where MP < 0 and TP is falling.
    
    L = np.linspace(0, 7.5, 300)
    tp = 9 * L**2 - L**3
    # Avoid divide-by-zero for AP at 0
    L_safe = np.where(L == 0, 1e-6, L)
    ap = 9 * L_safe - L_safe**2
    mp = 18 * L - 3 * L**2

    # Boundaries
    L_stage1 = 4.5
    L_stage2 = 6.0
    TP_max = 108.0
    AP_max = 20.25

    # Top Panel: Total Product
    ax1.plot(L, tp, color=DEEP["blue"], lw=3.5, label="Total Product (TP)")
    ax1.set_xlim(0, 7.8)
    ax1.set_ylim(-5, 125)
    ax1.set_ylabel("Product (Output)", fontsize=15, color=INK)
    
    # Hide top and right spines
    for ax in [ax1, ax2]:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(INK)
        ax.spines["left"].set_linewidth(1.5)
        ax.spines["bottom"].set_color(INK)
        ax.spines["bottom"].set_linewidth(1.5)
        ax.set_facecolor("white")
        ax.tick_params(colors=INK, labelsize=14)

    ax1.tick_params(labelbottom=False, bottom=False)

    # Bottom Panel: AP and MP
    ax2.plot(L, ap, color=DEEP["green"], lw=3.5, label="Average Product (AP)")
    ax2.plot(L, mp, color=DEEP["orange"], lw=3.5, label="Marginal Product (MP)")
    ax2.axhline(0, color=GREY, lw=1.2, ls="-")
    ax2.set_xlim(0, 7.8)
    ax2.set_ylim(-35, 35)
    ax2.set_xlabel("Variable Input (e.g., Labour)", fontsize=15, color=INK)
    ax2.set_ylabel("Product (Output)", fontsize=15, color=INK)

    # Stage shading / division lines across both axes
    for boundary in [L_stage1, L_stage2]:
        ax1.axvline(boundary, color=GREY, lw=1.8, ls="--", zorder=1)
        ax2.axvline(boundary, color=GREY, lw=1.8, ls="--", zorder=1)

    # Stage Background Tints
    ax1.axvspan(0, L_stage1, color=CREAM, alpha=0.3, zorder=0)
    ax1.axvspan(L_stage1, L_stage2, color=BLUE, alpha=0.08, zorder=0)
    ax1.axvspan(L_stage2, 7.8, color=PINK, alpha=0.15, zorder=0)

    ax2.axvspan(0, L_stage1, color=CREAM, alpha=0.3, zorder=0)
    ax2.axvspan(L_stage1, L_stage2, color=BLUE, alpha=0.08, zorder=0)
    ax2.axvspan(L_stage2, 7.8, color=PINK, alpha=0.15, zorder=0)

    # Stage Labels at the top of ax1
    bbox_stage = dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=1)
    ax1.text(L_stage1 / 2, 116, "Stage I", ha="center", va="center", fontsize=15, weight="bold", color=INK, bbox=bbox_stage)
    ax1.text((L_stage1 + L_stage2) / 2, 116, "Stage II (Rational Zone)", ha="center", va="center", fontsize=14, weight="bold", color=INK, bbox=bbox_stage)
    ax1.text((L_stage2 + 7.8) / 2, 116, "Stage III", ha="center", va="center", fontsize=15, weight="bold", color=INK, bbox=bbox_stage)

    # Point of maximum TP annotation on ax1
    ax1.plot(L_stage2, TP_max, marker="o", markersize=7, color=DEEP["blue"], zorder=5)
    ax1.annotate("Point of maximum TP (MP=0)",
                 xy=(L_stage2, TP_max), xytext=(L_stage2 - 2.8, TP_max - 5),
                 fontsize=14, color=INK, weight="medium",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=2))

    # Curve label on ax1
    ax1.text(3.0, 62, "Total Product (TP)", color=DEEP["blue"], fontsize=15, weight="bold",
             bbox=dict(fc="white", ec="none", pad=2))

    # Point of maximum AP annotation on ax2
    ax2.plot(L_stage1, AP_max, marker="o", markersize=7, color=DEEP["green"], zorder=5)
    ax2.annotate("Point of maximum AP",
                 xy=(L_stage1, AP_max), xytext=(L_stage1 - 3.2, AP_max + 7),
                 fontsize=14, color=INK, weight="medium",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=2))

    # Point where MP = 0 annotation on ax2
    ax2.plot(L_stage2, 0, marker="o", markersize=7, color=DEEP["orange"], zorder=5)

    # Curve labels on ax2
    ax2.text(2.0, 26, "Marginal Product (MP)", color=DEEP["orange"], fontsize=14, weight="bold",
             bbox=dict(fc="white", ec="none", pad=2))
    ax2.text(5.5, 16, "Average Product (AP)", color=DEEP["green"], fontsize=14, weight="bold",
             bbox=dict(fc="white", ec="none", pad=2))

    # Stage descriptions / notes along bottom
    ax2.text(1.2, -26, "MP > AP\nAP rising", ha="center", fontsize=14, color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="square,pad=0.3", lw=0.8))
    ax2.text(5.25, -26, "MP < AP\nMP > 0", ha="center", fontsize=14, color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="square,pad=0.3", lw=0.8))
    ax2.text(6.9, -26, "MP < 0\nTP falls", ha="center", fontsize=14, color=INK,
             bbox=dict(fc="white", ec=GREY, boxstyle="square,pad=0.3", lw=0.8))

    save(fig, out)
