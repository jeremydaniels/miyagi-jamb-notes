from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 9.5)
    
    # Grid: ax1 top (axon schematic), ax2 bottom (action potential graph)
    ax1 = fig.add_axes([0.08, 0.56, 0.86, 0.38])
    ax2 = fig.add_axes([0.10, 0.08, 0.82, 0.38])
    
    # ================= TOP PANEL: AXON =================
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-1.6, 2.6)
    ax1.axis('off')
    
    # Axon tube geometry
    y_top = 0.9
    y_bot = -0.7
    axon_x0, axon_x1 = 0.5, 9.5
    
    # Fill axon interior
    ax1.fill_between([axon_x0, axon_x1], [y_bot, y_bot], [y_top, y_top],
                     color=CREAM, alpha=0.6, zorder=1)
    
    # Action potential active zone highlight
    # Action potential region ~ [5.2, 6.8], Repolarising zone ~ [3.6, 5.2]
    # Let AP be around 4.8 to 6.8
    ax1.fill_between([4.8, 6.6], [y_bot, y_bot], [y_top, y_top],
                     color=ORANGE, alpha=0.25, zorder=2)
    ax1.fill_between([3.2, 4.8], [y_bot, y_bot], [y_top, y_top],
                     color=BLUE, alpha=0.2, zorder=2)

    # Membrane bilayer lines
    d_m = 0.08
    for y_m in [y_top, y_bot]:
        ax1.plot([axon_x0, axon_x1], [y_m, y_m], color=DEEP["blue"], lw=3.5, zorder=3)
        ax1.plot([axon_x0, axon_x1], [y_m - (d_m if y_m>0 else -d_m), y_m - (d_m if y_m>0 else -d_m)],
                 color=DEEP["blue"], lw=1.2, linestyle='--', alpha=0.5, zorder=3)
        
    # Charges along membrane
    # Top outside (+/ -) and inside (-/ +)
    # Bottom inside (-/ +) and outside (+/ -)
    xs = np.linspace(0.8, 9.2, 29)
    for x in xs:
        # AP region: 5.0 <= x <= 6.4 (depolarisation)
        # Just behind AP: 3.4 <= x < 5.0 (repolarisation / returning)
        if 4.9 <= x <= 6.5:
            # Action potential: inside positive, outside negative
            top_out, top_in = "−", "+"
            bot_in, bot_out = "+", "−"
            col_out, col_in = DEEP["orange"], DEEP["orange"]
        else:
            # Resting: inside negative, outside positive
            top_out, top_in = "+", "−"
            bot_in, bot_out = "−", "+"
            col_out, col_in = DEEP["blue"], DEEP["blue"]
            
        # Top membrane charges
        ax1.text(x, y_top + 0.16, top_out, fontsize=12, ha='center', va='center',
                 fontweight='bold', color=col_out)
        ax1.text(x, y_top - 0.22, top_in, fontsize=12, ha='center', va='center',
                 fontweight='bold', color=col_in)
        # Bottom membrane charges
        ax1.text(x, y_bot + 0.22, bot_in, fontsize=12, ha='center', va='center',
                 fontweight='bold', color=col_in)
        ax1.text(x, y_bot - 0.16, bot_out, fontsize=12, ha='center', va='center',
                 fontweight='bold', color=col_out)

    # Ion flow arrows
    # Na+ entering at the action potential (~ 5.7)
    ax1.annotate("", xy=(5.7, y_top - 0.35), xytext=(5.7, y_top + 0.55),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=14))
    ax1.text(5.7, y_top + 0.72, "Na⁺ ions in", ha='center', va='bottom', fontsize=12,
             fontweight='bold', color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # K+ leaving just behind it (~ 4.0)
    ax1.annotate("", xy=(4.0, y_top + 0.55), xytext=(4.0, y_top - 0.35),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.2, mutation_scale=14))
    ax1.text(4.0, y_top + 0.72, "K⁺ ions out", ha='center', va='bottom', fontsize=12,
             fontweight='bold', color=DEEP["blue"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

    # Impulse propagation arrow (moving to the right)
    ax1.annotate("", xy=(8.2, 0.1), xytext=(2.2, 0.1),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=18))
    ax1.text(5.2, 0.26, "direction of impulse", ha='center', va='bottom',
             fontsize=12.5, fontweight='bold', color=INK,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))

    # Axon Labels
    ax1.text(0.5, y_top + 0.38, "axon membrane", fontsize=11.5, color=INK, ha='left',
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=0.8))
    ax1.plot([1.3, 1.8], [y_top + 0.35, y_top], color=INK, lw=1)

    # Label resting region
    ax1.annotate("resting region (inside negative)", xy=(8.1, y_bot - 0.4), xytext=(8.1, y_bot - 0.9),
                 ha='center', fontsize=11.5, color=INK,
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Label action potential
    ax1.annotate("action potential (inside positive)", xy=(5.7, y_bot - 0.4), xytext=(5.7, y_bot - 0.9),
                 ha='center', fontsize=11.5, color=INK,
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Section title
    ax1.text(0.1, 2.3, "A. Conduction of Action Potential Along Axon", fontsize=13, fontweight='bold', color=INK)

    # ================= BOTTOM PANEL: GRAPH =================
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color(INK)
    ax2.spines['bottom'].set_color(INK)
    ax2.spines['left'].set_linewidth(1.3)
    ax2.spines['bottom'].set_linewidth(1.3)
    
    ax2.set_xlim(0, 6.0)
    ax2.set_ylim(-90, 55)
    ax2.set_xlabel("Time (ms)", fontsize=13, color=INK, labelpad=6)
    ax2.set_ylabel("Membrane potential (mV)", fontsize=13, color=INK, labelpad=8)
    ax2.set_xticks(np.arange(0, 6.5, 1.0))
    ax2.set_yticks([-70, -55, 0, 40])
    ax2.tick_params(colors=INK, labelsize=11)
    
    # Action potential waveform
    t = np.linspace(0, 6.0, 500)
    # Piecewise realistic AP trace
    v = np.zeros_like(t)
    for i, ti in enumerate(t):
        if ti < 1.0:
            v[i] = -70.0
        elif ti < 1.4:
            # slow rise to threshold -55 mV
            v[i] = -70.0 + 15.0 * ((ti - 1.0) / 0.4)
        elif ti < 2.0:
            # sharp depolarisation up to +40 mV
            p = (ti - 1.4) / 0.6
            v[i] = -55.0 + 95.0 * np.sin(p * np.pi / 2)
        elif ti < 3.0:
            # repolarisation down to -80 mV (undershoot)
            p = (ti - 2.0) / 1.0
            v[i] = 40.0 - 120.0 * (1 - np.cos(p * np.pi)) / 2
        elif ti < 4.5:
            # refractory recovery back to -70 mV
            p = (ti - 3.0) / 1.5
            v[i] = -80.0 + 10.0 * (1 - np.exp(-3 * p)) / (1 - np.exp(-3))
        else:
            v[i] = -70.0

    # Reference gridlines (resting & threshold)
    ax2.axhline(-70, color=GREY, linestyle=':', lw=1.2, zorder=1)
    ax2.axhline(-55, color=GREY, linestyle='--', lw=1.1, zorder=1)
    ax2.axhline(0, color=GREY, linestyle='-', lw=0.6, alpha=0.5, zorder=1)

    # Plot AP curve
    ax2.plot(t, v, color=DEEP["orange"], lw=3.2, zorder=3)
    
    # Highlight depolarisation vs repolarisation sections
    t_dep = t[(t >= 1.4) & (t <= 2.0)]
    v_dep = v[(t >= 1.4) & (t <= 2.0)]
    ax2.plot(t_dep, v_dep, color=DEEP["orange"], lw=3.8, zorder=4)

    t_rep = t[(t >= 2.0) & (t <= 3.0)]
    v_rep = v[(t >= 2.0) & (t <= 3.0)]
    ax2.plot(t_rep, v_rep, color=DEEP["blue"], lw=3.8, zorder=4)

    # Graph annotations & labels
    # Resting potential (-70 mV)
    ax2.text(0.15, -67, "resting potential (−70 mV)", fontsize=11.5, color=INK,
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9))

    # Threshold
    ax2.text(0.15, -53, "threshold", fontsize=11.5, color=INK, fontstyle='italic',
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9))

    # Peak label (+40 mV)
    ax2.plot(2.0, 40, 'o', color=DEEP["orange"], markersize=5, zorder=5)

    # Depolarisation (Na+ in)
    ax2.annotate("depolarisation (Na⁺ in)", xy=(1.68, 5), xytext=(0.4, 25),
                 fontsize=12, fontweight='bold', color=DEEP["orange"],
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.4))

    # Repolarisation (K+ out)
    ax2.annotate("repolarisation (K⁺ out)", xy=(2.45, -15), xytext=(3.4, 18),
                 fontsize=12, fontweight='bold', color=DEEP["blue"],
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.4))

    # Refractory period
    ax2.annotate("refractory period", xy=(3.3, -79), xytext=(3.5, -45),
                 fontsize=11.5, color=INK,
                 bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Section title
    ax2.text(0.0, 58, "B. Changes in Membrane Potential During an Action Potential",
             fontsize=13, fontweight='bold', color=INK)

    save(fig, out)
