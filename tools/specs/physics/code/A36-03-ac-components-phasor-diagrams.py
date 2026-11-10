from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 4.5)
    
    # 3 subplots side by side
    axes = [fig.add_subplot(1, 3, i + 1) for i in range(3)]
    
    titles = [
        "Resistor",
        "Capacitor",
        "Inductor"
    ]
    
    for ax, title in zip(axes, titles):
        ax.set_aspect("equal")
        ax.set_xlim(-1.2, 3.2)
        ax.set_ylim(-2.5, 2.5)
        ax.axis("off")
        ax.set_title(title, fontsize=17, color=INK, pad=12, weight="bold")
    
    # Common arrow properties
    arrow_kw = dict(angles='xy', scale_units='xy', scale=1, width=0.035)
    
    # --- Panel 1: Resistor ---
    ax1 = axes[0]
    # Dashed origin axes for reference
    ax1.axhline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    ax1.axvline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    
    # Two horizontal arrows pointing right: I and V_R
    # Offset slightly or draw different lengths so both are distinct and clear
    ax1.quiver(0, 0.15, 2.2, 0, color=DEEP["blue"], **arrow_kw)
    ax1.text(2.35, 0.15, r"$V_R$", color=DEEP["blue"], fontsize=16, va="center", weight="bold")
    
    ax1.quiver(0, -0.15, 1.6, 0, color=DEEP["pink"], **arrow_kw)
    ax1.text(1.75, -0.15, r"$I$", color=DEEP["pink"], fontsize=16, va="center", weight="bold")
    
    ax1.text(0, -1.8, "In phase\n" + r"($\Delta\phi = 0^\circ$)", color=INK, fontsize=14, ha="left")

    # --- Panel 2: Capacitor ---
    ax2 = axes[1]
    ax2.axhline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    ax2.axvline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    
    # Horizontal arrow I
    ax2.quiver(0, 0, 1.8, 0, color=DEEP["pink"], **arrow_kw)
    ax2.text(1.95, 0, r"$I$", color=DEEP["pink"], fontsize=16, va="center", weight="bold")
    
    # Vertical arrow pointing down V_C
    ax2.quiver(0, 0, 0, -1.8, color=DEEP["blue"], **arrow_kw)
    ax2.text(0.15, -1.95, r"$V_C$", color=DEEP["blue"], fontsize=16, va="top", weight="bold")
    
    # 90 degree angle indicator
    sq_size = 0.35
    ax2.plot([sq_size, sq_size, 0], [0, -sq_size, -sq_size], color=INK, lw=1.5)
    ax2.text(0.45, -0.45, r"$90^\circ$", color=INK, fontsize=14, va="center", ha="left")
    
    ax2.text(0, -2.4, r"$I$ leads $V_C$ by $90^\circ$", color=INK, fontsize=14, ha="left")

    # --- Panel 3: Inductor ---
    ax3 = axes[2]
    ax3.axhline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    ax3.axvline(0, color=GREY, lw=1, ls="--", alpha=0.7)
    
    # Horizontal arrow I
    ax3.quiver(0, 0, 1.8, 0, color=DEEP["pink"], **arrow_kw)
    ax3.text(1.95, 0, r"$I$", color=DEEP["pink"], fontsize=16, va="center", weight="bold")
    
    # Vertical arrow pointing up V_L
    ax3.quiver(0, 0, 0, 1.8, color=DEEP["blue"], **arrow_kw)
    ax3.text(0.15, 1.95, r"$V_L$", color=DEEP["blue"], fontsize=16, va="bottom", weight="bold")
    
    # 90 degree angle indicator
    ax3.plot([sq_size, sq_size, 0], [0, sq_size, sq_size], color=INK, lw=1.5)
    ax3.text(0.45, 0.45, r"$90^\circ$", color=INK, fontsize=14, va="center", ha="left")
    
    ax3.text(0, -2.4, r"$V_L$ leads $I$ by $90^\circ$", color=INK, fontsize=14, ha="left")

    plt.subplots_adjust(left=0.04, right=0.96, top=0.85, bottom=0.1)
    save(fig, out)
