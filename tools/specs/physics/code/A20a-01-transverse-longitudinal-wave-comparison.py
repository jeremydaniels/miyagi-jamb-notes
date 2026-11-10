from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 7.5)
    
    # Left subplot: Transverse Wave
    ax1 = fig.add_axes([0.05, 0.08, 0.42, 0.82])
    ax1.set_xlim(-0.5, 8.5)
    ax1.set_ylim(-3.5, 3.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Title
    ax1.text(4.0, 3.1, "Transverse Wave", fontsize=18, fontweight='bold', color=INK, ha='center')
    
    # Equilibrium line
    ax1.plot([-0.2, 8.2], [0, 0], color=GREY, lw=1.5, linestyle='--', zorder=1)
    
    # Sine wave (rope)
    x = np.linspace(0, 8, 500)
    y = 1.6 * np.sin(2 * np.pi * x / 4.0)
    ax1.plot(x, y, color=DEEP["blue"], lw=4.0, zorder=2)
    
    # Labels for Crest and Trough
    # Crest at x = 1.0, y = 1.6
    ax1.annotate("Crest", xy=(1.0, 1.6), xytext=(1.0, 2.4),
                 fontsize=15, color=INK, ha='center', va='bottom',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=1))
    
    # Trough at x = 3.0, y = -1.6
    ax1.annotate("Trough", xy=(3.0, -1.6), xytext=(3.0, -2.4),
                 fontsize=15, color=INK, ha='center', va='top',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=1))
    
    # Particle Vibration (Up-Down double arrow)
    ax1.annotate('', xy=(5.0, 1.3), xytext=(5.0, -1.3),
                 arrowprops=dict(arrowstyle='<->', color=DEEP["pink"], lw=2.5))
    ax1.text(5.2, 0, "Particle\nVibration", fontsize=14, color=DEEP["pink"],
             va='center', ha='left', fontweight='semibold',
             bbox=dict(fc="white", ec="none", pad=2))
    
    # Wave Direction (Arrow pointing right)
    ax1.annotate('', xy=(7.8, -2.6), xytext=(4.2, -2.6),
                 arrowprops=dict(arrowstyle='->', color=DEEP["green"], lw=3.0))
    ax1.text(6.0, -3.1, "Wave Direction", fontsize=14, color=DEEP["green"],
             va='center', ha='center', fontweight='semibold')

    # Right subplot: Longitudinal Wave
    ax2 = fig.add_axes([0.53, 0.08, 0.42, 0.82])
    ax2.set_xlim(-0.5, 8.5)
    ax2.set_ylim(-3.5, 3.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    # Title
    ax2.text(4.0, 3.1, "Longitudinal Wave", fontsize=18, fontweight='bold', color=INK, ha='center')
    
    # Draw slinky spring with alternating compression and rarefaction
    # Phase phi from 0 to 2*pi*2 (2 complete wavelengths across L=8)
    # x(phi) = (8/(4*pi)) * (phi - 0.55 * sin(phi))
    phi = np.linspace(0, 4 * np.pi, 900)
    x_center = (8.0 / (4 * np.pi)) * (phi - 0.58 * np.sin(phi))
    
    # Slinky loops
    num_loops = 32
    theta = np.linspace(0, num_loops * 2 * np.pi, 1200)
    # Map theta to phi
    phi_theta = theta / num_loops * (4 * np.pi)
    x_slinky = (8.0 / (4 * np.pi)) * (phi_theta - 0.58 * np.sin(phi_theta)) + 0.18 * np.cos(theta)
    y_slinky = 1.0 * np.sin(theta)
    
    ax2.plot(x_slinky, y_slinky, color=DEEP["orange"], lw=2.5, zorder=2)
    
    # Labels for Compression and Rarefaction
    # Compressions occur where d(phi)/dx is large, near phi = 0, 2*pi, 4*pi
    # x approx: phi=0 -> 0; phi=2*pi -> 4.0; phi=pi -> 2.0 (Rarefaction)
    ax2.annotate("Compression", xy=(4.0, 1.05), xytext=(4.0, 2.4),
                 fontsize=15, color=INK, ha='center', va='bottom',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=1))
                 
    ax2.annotate("Rarefaction", xy=(2.0, 1.05), xytext=(2.0, 2.4),
                 fontsize=15, color=INK, ha='center', va='bottom',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec="none", pad=1))
    
    # Particle Vibration (Left-Right double arrow)
    ax2.annotate('', xy=(5.2, -1.6), xytext=(2.8, -1.6),
                 arrowprops=dict(arrowstyle='<->', color=DEEP["pink"], lw=2.5))
    ax2.text(4.0, -2.0, "Particle Vibration", fontsize=14, color=DEEP["pink"],
             va='top', ha='center', fontweight='semibold',
             bbox=dict(fc="white", ec="none", pad=1))
    
    # Wave Direction (Arrow pointing right)
    ax2.annotate('', xy=(7.8, -2.6), xytext=(4.2, -2.6),
                 arrowprops=dict(arrowstyle='->', color=DEEP["green"], lw=3.0))
    ax2.text(6.0, -3.1, "Wave Direction", fontsize=14, color=DEEP["green"],
             va='center', ha='center', fontweight='semibold')
    
    save(fig, out)
