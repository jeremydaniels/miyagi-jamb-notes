from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    
    # Axes setup
    axes_clean(ax, "Temperature (°C)", "Solubility (mol dm⁻³)", 100, 10)
    ax.set_title("Solubility Curves", fontsize=18, pad=18, color=INK, weight="bold")
    
    # Temperature range from 0 to 95 °C
    T = np.linspace(0, 95, 200)
    
    # 1. KNO3: Steep upward curve (exponential-like increase)
    # Starts around 1.3 mol/dm3 at 0°C, reaches ~9.5 at 80°C
    kno3 = 1.3 * np.exp(0.025 * T)
    
    # 2. NaCl: Very flat, nearly horizontal line, barely changing with temperature
    # Around 5.2 to 5.6 mol/dm3
    nacl = 5.2 + 0.004 * T
    
    # 3. Gas / Ca(OH)2: Downward-sloping curve (exothermic dissolution, solubility decreases with T)
    # Starts around 2.5 mol/dm3 and slopes down towards ~0.4
    ce_gas = 2.5 * np.exp(-0.02 * T)
    
    # Plot the curves with DEEP colors
    ax.plot(T, kno3, color=DEEP["blue"], lw=3.5, label=r"$\mathrm{KNO_3}$ (solubility rises rapidly)")
    ax.plot(T, nacl, color=DEEP["orange"], lw=3.5, label=r"$\mathrm{NaCl}$ (solubility barely changes)")
    ax.plot(T, ce_gas, color=DEEP["pink"], lw=3.5, label=r"$\mathrm{Ca(OH)_2}$ / gas (solubility decreases)")
    
    # Direct annotations near curves with white bboxes
    ax.text(72, 8.8, r"$\mathbf{KNO_3}$", fontsize=15, color=DEEP["blue"],
            ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none"))
    
    ax.text(82, 5.9, r"$\mathbf{NaCl}$", fontsize=15, color=DEEP["orange"],
            ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none"))
    
    ax.text(68, 1.2, r"$\mathbf{Ca(OH)_2}$ (or gas)", fontsize=15, color=DEEP["pink"],
            ha="center", va="center", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none"))
    
    # Add legend
    ax.legend(loc="upper left", frameon=True, fontsize=14, edgecolor=GREY, facecolor="white", framealpha=0.95)
    
    # Set proper limits
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 10.5)
    
    save(fig, out)
