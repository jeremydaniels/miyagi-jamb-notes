from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 5.5)
    
    # Left subplot: d.c. voltage
    ax1 = fig.add_axes([0.10, 0.18, 0.36, 0.68])
    # Right subplot: a.c. voltage
    ax2 = fig.add_axes([0.58, 0.18, 0.36, 0.68])
    
    # --- D.C. Voltage Plot ---
    t_dc = np.linspace(0, 10, 200)
    v_dc = np.full_like(t_dc, 3.0)
    
    ax1.plot(t_dc, v_dc, color=DEEP["blue"], lw=3.5)
    
    # Custom axes crossing at (0,0)
    ax1.spines["left"].set_position("zero")
    ax1.spines["bottom"].set_position("zero")
    ax1.spines["right"].set_visible(False)
    ax1.spines["top"].set_visible(False)
    
    ax1.set_xlim(-0.5, 11)
    ax1.set_ylim(-1.5, 4.5)
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    # Axis labels & Arrows
    ax1.plot(11, 0, marker=">", ms=8, color=INK, clip_on=False)
    ax1.plot(0, 4.5, marker="^", ms=8, color=INK, clip_on=False)
    ax1.text(11.2, 0, "Time", fontsize=15, va="center", ha="left", color=INK)
    ax1.text(0, 4.8, "Voltage", fontsize=15, va="bottom", ha="center", color=INK)
    
    ax1.text(5.5, 4.0, "d.c. Voltage", fontsize=16, weight="bold", ha="center", color=INK)
    ax1.text(5.5, 3.3, "Direct Current (steady)", fontsize=14, ha="center", color=GREY)
    
    # Dotted line to y-axis for d.c.
    ax1.plot([0, 0.5], [3.0, 3.0], color=GREY, ls="--", lw=1.5)
    ax1.text(-0.3, 3.0, "V", fontsize=15, va="center", ha="right", color=INK)
    
    # --- A.C. Voltage Plot ---
    t_ac = np.linspace(0, 4 * np.pi, 400)
    v_ac = 3.0 * np.sin(t_ac)
    
    ax2.plot(t_ac, v_ac, color=DEEP["orange"], lw=3.5)
    
    # Custom axes crossing at (0,0)
    ax2.spines["left"].set_position("zero")
    ax2.spines["bottom"].set_position("zero")
    ax2.spines["right"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    
    ax2.set_xlim(-0.6, 4 * np.pi + 1.2)
    ax2.set_ylim(-4.5, 4.5)
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    # Axis labels & Arrows
    ax2.plot(4 * np.pi + 1.2, 0, marker=">", ms=8, color=INK, clip_on=False)
    ax2.plot(0, 4.5, marker="^", ms=8, color=INK, clip_on=False)
    ax2.text(4 * np.pi + 1.4, 0, "Time", fontsize=15, va="center", ha="left", color=INK)
    ax2.text(0, 4.8, "Voltage", fontsize=15, va="bottom", ha="center", color=INK)
    
    ax2.text((4 * np.pi) / 2, 4.0, "a.c. Voltage", fontsize=16, weight="bold", ha="center", color=INK)
    
    # Peak Voltage annotation and marker
    peak_x = np.pi / 2
    peak_y = 3.0
    
    # Peak level dashed reference line
    ax2.plot([0, peak_x], [peak_y, peak_y], color=GREY, ls="--", lw=1.5)
    ax2.text(-0.3, peak_y, r"$V_0$", fontsize=15, va="center", ha="right", color=INK)
    
    # Annotation for Peak Voltage
    ax2.annotate(
        r"$V_0$ (Peak Voltage)",
        xy=(peak_x, peak_y),
        xytext=(peak_x + 1.8, peak_y + 0.6),
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )
    
    save(fig, out)
