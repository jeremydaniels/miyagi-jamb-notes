from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 6.5)
    
    # Left subplot: Temperature
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "temperature (°C)", "rate of reaction", 75, 105)
    
    # Temperature curve
    # Gradual rise up to ~37 °C, steep fall to 0 by ~60 °C
    t1 = np.linspace(0, 37, 150)
    # Q10 approx rise
    r1 = 95.0 * (t1 / 37.0) ** 2.2
    
    t2 = np.linspace(37, 60, 100)
    # Steep denaturation curve
    r2 = 95.0 * (1.0 - ((t2 - 37.0) / 23.0) ** 1.8)
    
    t3 = np.linspace(60, 70, 30)
    r3 = np.zeros_like(t3)
    
    temp_x = np.concatenate([t1, t2, t3])
    temp_y = np.concatenate([r1, r2, r3])
    
    ax1.plot(temp_x, temp_y, color=DEEP["blue"], lw=3.5)
    
    # Dotted guideline at optimum temperature
    ax1.plot([37, 37], [0, 95], color=GREY, linestyle="--", lw=1.8)
    ax1.scatter([37], [95], color=DEEP["blue"], s=50, zorder=5)
    
    # Annotations for Left Graph
    ax1.annotate("optimum temperature (37 °C)",
                 xy=(37, 95), xytext=(37, 102),
                 ha="center", va="bottom", fontsize=12, color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax1.annotate("enzyme denatured",
                 xy=(48, 55), xytext=(52, 70),
                 fontsize=12, color=INK, ha="left",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax1.set_xticks([0, 10, 20, 30, 40, 50, 60, 70])
    ax1.set_yticks([])
    
    # Right subplot: pH
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "pH", "rate of reaction", 12, 105)
    
    ph_x = np.linspace(0.5, 11.5, 400)
    
    # Three bell-shaped curves: pepsin (pH 2), salivary amylase (pH 7), trypsin (pH 8)
    def bell(x, mu, sigma, height=90.0):
        return height * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    pepsin = bell(ph_x, 2.0, 0.8, 90.0)
    amylase = bell(ph_x, 7.0, 1.1, 90.0)
    trypsin = bell(ph_x, 8.0, 1.0, 90.0)
    
    ax2.plot(ph_x, pepsin, color=DEEP["pink"], lw=3.5)
    ax2.plot(ph_x, amylase, color=DEEP["green"], lw=3.5)
    ax2.plot(ph_x, trypsin, color=DEEP["orange"], lw=3.5)
    
    # Annotations for Right Graph
    ax2.annotate("pepsin (pH 2)",
                 xy=(2.0, 90.0), xytext=(2.0, 97.0),
                 ha="center", va="bottom", fontsize=12, color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax2.annotate("salivary amylase (pH 7)",
                 xy=(7.0, 90.0), xytext=(5.6, 97.0),
                 ha="center", va="bottom", fontsize=12, color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax2.annotate("trypsin (pH 8)",
                 xy=(8.0, 90.0), xytext=(9.2, 97.0),
                 ha="center", va="bottom", fontsize=12, color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax2.set_xticks(range(1, 12))
    ax2.set_yticks([])

    plt.subplots_adjust(wspace=0.25, left=0.08, right=0.95, top=0.90, bottom=0.15)
    save(fig, out)
