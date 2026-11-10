from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 6)
    
    # Left subplot: P vs V
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "Volume (V)", "Pressure (P)", 10, 10)
    
    v = np.linspace(1.0, 9.5, 200)
    # P * V = constant -> P = k / V
    k1 = 8.0
    p1 = k1 / v
    
    ax1.plot(v, p1, color=DEEP["blue"], lw=3.5)
    ax1.set_title("Boyle's Law: $P$ vs $V$", fontsize=16, color=INK, pad=12)
    
    # Annotation / description for the curve
    ax1.text(5.5, 4.5, r"$P \propto \frac{1}{V}$" + "\n(constant $T$)", 
             fontsize=15, color=INK, ha="center", va="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    
    # Right subplot: P vs 1/V
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "1 / Volume (1/V)", "Pressure (P)", 10, 10)
    
    inv_v = np.linspace(0, 9.0, 200)
    slope = 0.95
    p2 = slope * inv_v
    
    ax2.plot(inv_v, p2, color=DEEP["orange"], lw=3.5)
    ax2.set_title(r"Boyle's Law: $P$ vs $1/V$", fontsize=16, color=INK, pad=12)
    
    # Annotation / description for the straight line
    ax2.text(3.5, 6.5, r"$P \propto \frac{1}{V}$" + "\n(linear relationship)", 
             fontsize=15, color=INK, ha="center", va="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    
    plt.subplots_adjust(wspace=0.3, top=0.88, bottom=0.15, left=0.08, right=0.95)
    save(fig, out)
