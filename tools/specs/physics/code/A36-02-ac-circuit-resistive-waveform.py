from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Subplot 1: Circuit Diagram
    ax1 = fig.add_axes([0.05, 0.1, 0.4, 0.8])
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 5.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Coordinates for circuit:
    # Top wire
    ax1.plot([1.0, 3.5], [4.5, 4.5], color=INK, lw=2.5)
    # Bottom wire
    ax1.plot([1.0, 3.5], [0.5, 0.5], color=INK, lw=2.5)
    
    # Left branch (AC source)
    src_center = (1.0, 2.5)
    radius = 0.6
    ax1.plot([1.0, 1.0], [4.5, 2.5 + radius], color=INK, lw=2.5)
    ax1.plot([1.0, 1.0], [2.5 - radius, 0.5], color=INK, lw=2.5)
    
    circle = plt.Circle(src_center, radius, edgecolor=INK, facecolor='white', lw=2.5, zorder=3)
    ax1.add_patch(circle)
    
    # Sine wave inside source
    t_s = np.linspace(-0.35, 0.35, 100)
    wave_s = 0.22 * np.sin(2 * np.pi * t_s / 0.7)
    ax1.plot(src_center[0] + t_s, src_center[1] + wave_s, color=INK, lw=2, zorder=4)
    
    ax1.text(0.1, 2.5, "a.c. source\n$v = V_0 \\sin(\\omega t)$", fontsize=14, color=INK, 
             va='center', ha='right', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
    
    # Right branch (Resistor zigzag)
    ax1.plot([3.5, 3.5], [4.5, 3.5], color=INK, lw=2.5)
    ax1.plot([3.5, 3.5], [1.5, 0.5], color=INK, lw=2.5)
    
    # Zig-zag: 6 segments between y=1.5 and y=3.5
    rz_y = np.linspace(3.5, 1.5, 9)
    rz_x = np.array([3.5, 3.8, 3.2, 3.8, 3.2, 3.8, 3.2, 3.8, 3.5])
    ax1.plot(rz_x, rz_y, color=INK, lw=2.5, solid_capstyle='round')
    
    ax1.text(4.1, 2.5, "Resistor\n($R$)", fontsize=15, color=INK, va='center', ha='left')
    ax1.set_title("Purely Resistive a.c. Circuit", fontsize=16, color=INK, pad=15)
    
    # Subplot 2: Graph of V and I in phase
    ax2 = fig.add_axes([0.55, 0.15, 0.4, 0.65])
    
    t = np.linspace(0, 2 * np.pi, 300)
    v = 1.0 * np.sin(t)
    i = 0.6 * np.sin(t)
    
    # Clean axes
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_position('zero')
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['left'].set_color(GREY)
    ax2.spines['bottom'].set_color(GREY)
    ax2.spines['left'].set_linewidth(1.5)
    ax2.spines['bottom'].set_linewidth(1.5)
    
    ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax2.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=14, color=INK)
    ax2.set_yticks([-1.0, -0.6, 0.6, 1.0])
    ax2.set_yticklabels(['$-V_0$', '$-I_0$', '$I_0$', '$V_0$'], fontsize=14, color=INK)
    ax2.tick_params(colors=GREY)
    
    # Plot voltage and current curves
    line_v, = ax2.plot(t, v, color=DEEP["blue"], lw=3.0, label="Voltage ($v$)")
    line_i, = ax2.plot(t, i, color=DEEP["pink"], lw=3.0, linestyle="--", label="Current ($i$)")
    
    # Labels & annotations
    ax2.set_xlabel(r"$\omega t$ (rad)", fontsize=15, color=INK, loc='right', labelpad=5)
    ax2.text(-0.35, 1.35, "Signal Amplitude", fontsize=15, color=INK, ha='left')
    
    ax2.annotate("In phase:\npeaks & zeroes coincide", 
                 xy=(np.pi/2, 1.0), xytext=(np.pi/2 + 0.8, 1.15),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax2.set_xlim(-0.2, 2 * np.pi + 0.4)
    ax2.set_ylim(-1.3, 1.5)
    ax2.legend(loc="lower right", frameon=True, fontsize=14, edgecolor=GREY)
    ax2.set_title("Voltage and Current in Phase", fontsize=16, color=INK, pad=25)
    
    save(fig, out)
