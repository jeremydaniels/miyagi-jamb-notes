from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 8.2)
    
    # 2 rows, 3 columns
    axes = [fig.add_subplot(2, 3, i + 1) for i in range(6)]
    
    # Grid coordinate helper
    x = np.linspace(-3, 3, 250)
    y = np.linspace(-3, 3, 250)
    X, Y = np.meshgrid(x, y)
    
    contour_kw = dict(colors=DEEP["orange"], linewidths=2.0)
    label_kw = dict(inline=True, fontsize=14, fmt='%d', colors=INK)
    
    # -------------------------------------------------------------
    # 1. Conical hill (concentric circular contours)
    # -------------------------------------------------------------
    ax1 = axes[0]
    Z1 = 100 + 400 * np.exp(-(X**2 + Y**2) / 3.2)
    levels1 = [150, 200, 250, 300, 350, 400]
    cs1 = ax1.contour(X, Y, Z1, levels=levels1, **contour_kw)
    ax1.clabel(cs1, levels=levels1[::2], **label_kw)
    ax1.set_title("1. Conical Hill", fontsize=16, color=INK, pad=10, weight="bold")
    
    # -------------------------------------------------------------
    # 2. Plateau (contours close at edges, wide empty top)
    # -------------------------------------------------------------
    ax2 = axes[1]
    r = np.sqrt(X**2 + Y**2)
    Z2 = 100 + 300 / (1 + np.exp(4.0 * (r - 1.9)))
    levels2 = [150, 200, 250, 300, 350]
    cs2 = ax2.contour(X, Y, Z2, levels=levels2, **contour_kw)
    ax2.clabel(cs2, levels=levels2, **label_kw)
    ax2.text(0, 0, "Flat top\n(400 m)", fontsize=14, color=INK, ha='center', va='center',
             bbox=dict(fc="white", ec="none", pad=1.5))
    ax2.set_title("2. Plateau", fontsize=16, color=INK, pad=10, weight="bold")
    
    # -------------------------------------------------------------
    # 3. Ridge (long oval contours)
    # -------------------------------------------------------------
    ax3 = axes[2]
    Z3 = 100 + 350 * np.exp(-(0.35 * X**2 + 2.2 * Y**2))
    levels3 = [150, 200, 250, 300, 350, 400]
    cs3 = ax3.contour(X, Y, Z3, levels=levels3, **contour_kw)
    ax3.clabel(cs3, levels=levels3[::2], **label_kw)
    ax3.set_title("3. Ridge", fontsize=16, color=INK, pad=10, weight="bold")
    
    # -------------------------------------------------------------
    # 4. Escarpment (gentle dip slope on one side, steep scarp on other)
    # -------------------------------------------------------------
    ax4 = axes[3]
    Z4 = 100 + 30 * (X + 2.6) + 300 / (1 + np.exp(-4.5 * (X - 0.6)))
    levels4 = [120, 160, 200, 250, 300, 350, 400]
    cs4 = ax4.contour(X, Y, Z4, levels=levels4, **contour_kw)
    labels4 = [120, 200, 300, 400]
    manual_locs4 = [(-2.0, 0), (-0.5, 0), (0.6, 1.5), (1.0, 1.5)]
    ax4.clabel(cs4, levels=labels4, manual=manual_locs4, **label_kw)
    ax4.text(-1.4, -2.2, "Gentle slope\n(dip slope)", fontsize=14, color=INK, ha='center',
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax4.text(1.3, -2.2, "Steep scarp", fontsize=14, color=INK, ha='center',
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax4.set_title("4. Escarpment", fontsize=16, color=INK, pad=10, weight="bold")
    
    # -------------------------------------------------------------
    # 5. Valley (V-shaped contours pointing towards higher values, with river)
    # -------------------------------------------------------------
    ax5 = axes[4]
    Z5 = 150 + 45 * Y - 55 * np.exp(-1.2 * np.abs(X))
    levels5 = [80, 120, 160, 200]
    cs5 = ax5.contour(X, Y, Z5, levels=levels5, **contour_kw)
    manual_locs5 = [(-1.5, -1.8), (-1.5, -0.9), (-1.5, 0.0), (-1.5, 0.9)]
    ax5.clabel(cs5, levels=levels5, manual=manual_locs5, **label_kw)
    # Stream in the valley axis (stops before hitting top text)
    ax5.plot([0, 0], [-2.6, 1.6], color=DEEP["blue"], lw=3.0, zorder=2)
    ax5.annotate("", xy=(0, -1.6), xytext=(0, -0.4),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5))
    ax5.text(0.2, 0.8, "River\n(flows downhill)", fontsize=14, color=DEEP["blue"], ha="left",
             bbox=dict(fc="white", ec="none", pad=1.5), zorder=10)
    ax5.text(0, 2.2, "Contours point uphill", fontsize=14, color=INK, ha="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"), zorder=10)
    ax5.set_title("5. Valley", fontsize=16, color=INK, pad=10, weight="bold")
    
    # -------------------------------------------------------------
    # 6. Spur (V-shaped contours pointing towards lower values)
    # -------------------------------------------------------------
    ax6 = axes[5]
    Z6 = 150 + 45 * Y + 55 * np.exp(-1.2 * np.abs(X))
    levels6 = [120, 160, 200, 240]
    cs6 = ax6.contour(X, Y, Z6, levels=levels6, **contour_kw)
    manual_locs6 = [(-1.5, -0.9), (-1.5, 0.0), (-1.5, 0.9), (-1.5, 1.8)]
    ax6.clabel(cs6, levels=levels6, manual=manual_locs6, **label_kw)
    ax6.annotate("Spur crest", xy=(0, -0.8), xytext=(0.4, -1.6),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"), zorder=10)
    ax6.text(0, -2.2, "Contours point downhill", fontsize=14, color=INK, ha="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"), zorder=10)
    ax6.set_title("6. Spur", fontsize=16, color=INK, pad=10, weight="bold")
    
    # Uniform styling across all panels
    for ax in axes:
        ax.set_xlim(-2.6, 2.6)
        ax.set_ylim(-2.6, 2.6)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_linewidth(1.2)
            
    fig.tight_layout(pad=2.2)
    save(fig, out)
