from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    
    # 2D Graph with clean axes
    # Max x = 10, max y = 1.05
    axes_clean(ax, "Kinetic Energy", "Number of particles", 10, 1.0)
    
    # Maxwell-Boltzmann kinetic energy distribution: f(E) ~ sqrt(E) * exp(-E / (kT))
    # E >= 0
    x = np.linspace(0, 9.6, 500)
    
    # Parametrize T1 (Lower Temperature) and T2 (Higher Temperature)
    # T1: kT = 1.2
    # T2: kT = 2.0
    kT1 = 1.25
    kT2 = 2.1
    
    # Distribution formula proportional to sqrt(E) * exp(-E/kT) / (kT)^1.5
    f1 = np.sqrt(x) * np.exp(-x / kT1) / (kT1**1.5)
    f2 = np.sqrt(x) * np.exp(-x / kT2) / (kT2**1.5)
    
    # Normalize heights for visual clarity and textbook appeal
    scale = 1.8
    y1 = f1 * scale
    y2 = f2 * scale
    
    # Activation Energy Ea
    Ea = 5.8
    mask = x >= Ea
    
    # Shading areas under curves to the right of Ea
    # T2 shaded area (larger)
    ax.fill_between(x[mask], y2[mask], color=BLUE, alpha=0.55, zorder=2)
    # T1 shaded area (smaller, nested/overlapping)
    ax.fill_between(x[mask], y1[mask], color=ORANGE, alpha=0.55, zorder=3)
    
    # Plot curves
    ax.plot(x, y1, color=DEEP["orange"], lw=3.2, zorder=4)
    ax.plot(x, y2, color=DEEP["blue"], lw=3.2, zorder=4)
    
    # Vertical dashed line for Activation Energy (E_a)
    y_max_ea = max(y1[x >= Ea].max(), y2[x >= Ea].max()) * 2.8
    ax.axvline(x=Ea, ymin=0, ymax=0.78, color=INK, linestyle="--", lw=2, zorder=5)
    
    # Labels for curves
    # T1 peak is around E = kT1/2 = 0.625, let's place label near upper part of curve
    ax.annotate(r"Lower Temperature ($T_1$)", 
                xy=(1.7, y1[np.argmin(np.abs(x - 1.7))]), 
                xytext=(2.4, 0.88),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=6)
                
    ax.annotate(r"Higher Temperature ($T_2$)", 
                xy=(3.2, y2[np.argmin(np.abs(x - 3.2))]), 
                xytext=(4.3, 0.68),
                fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=6)
                
    # Activation Energy label
    ax.text(Ea, 0.82, r"Activation Energy ($E_a$)", 
            fontsize=14, color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
            zorder=6)
            
    # Annotation pointing out particles with E >= Ea
    ax.annotate("Particles with\nenergy $\\geq E_a$",
                xy=(6.8, 0.12),
                xytext=(7.5, 0.38),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
                zorder=6)

    save(fig, out)
