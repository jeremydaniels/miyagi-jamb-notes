from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 7.5)
    
    # Left subplot: S-shaped (sigmoid) curve
    ax1 = fig.add_axes([0.08, 0.14, 0.40, 0.70])
    # Right subplot: J-shaped curve
    ax2 = fig.add_axes([0.56, 0.14, 0.40, 0.70])
    
    axes_clean(ax1, "time", "number of individuals (population size)", 10, 10)
    axes_clean(ax2, "time", "number of individuals (population size)", 10, 10)
    
    # ------------------ LEFT: S-SHAPED CURVE ------------------
    # Define phase boundaries along x
    x_lag = 1.8
    x_exp = 4.2
    x_dec = 6.2
    x_stat = 8.5
    x_end = 10.0
    
    # Shading phase regions
    ax1.axvspan(0, x_lag, color=CREAM, alpha=0.6, zorder=0)
    ax1.axvspan(x_lag, x_exp, color=BLUE, alpha=0.25, zorder=0)
    ax1.axvspan(x_exp, x_dec, color=GREEN, alpha=0.25, zorder=0)
    ax1.axvspan(x_dec, x_stat, color=LAV, alpha=0.3, zorder=0)
    ax1.axvspan(x_stat, x_end, color=PINK, alpha=0.3, zorder=0)
    
    # Sigmoid curve with death phase
    x1 = np.linspace(0, 10, 300)
    # Logistic base
    K = 7.5
    r = 1.3
    x0 = 4.2
    logistic = K / (1 + np.exp(-r * (x1 - x0)))
    # Add gentle decline after x = 8.5
    death_factor = np.where(x1 > 8.5, 1.0 - 0.25 * ((x1 - 8.5) / 1.5)**1.2, 1.0)
    y1 = logistic * death_factor
    
    ax1.plot(x1, y1, color=DEEP["blue"], lw=3.5, zorder=3)
    
    # Carrying capacity line
    ax1.axhline(K, color=DEEP["orange"], lw=2.0, ls="--", zorder=2)
    ax1.text(0.3, K + 0.25, "carrying capacity (K)", fontsize=14, color=DEEP["orange"], weight="bold",
             bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Phase boundary dashed dividers
    for xv in [x_lag, x_exp, x_dec, x_stat]:
        ax1.axvline(xv, color=GREY, lw=1.2, ls=":", zorder=1)
        
    # Phase labels at top of zones
    ax1.text(x_lag / 2, 9.3, "lag\nphase", ha="center", va="top", fontsize=14, color=INK)
    ax1.text((x_lag + x_exp) / 2, 9.3, "exponential\n(log) phase", ha="center", va="top", fontsize=14, color=INK)
    ax1.text((x_exp + x_dec) / 2, 9.3, "deceleration\nphase", ha="center", va="top", fontsize=14, color=INK)
    ax1.text((x_dec + x_stat) / 2, 9.3, "stationary\nphase", ha="center", va="top", fontsize=14, color=INK)
    ax1.text((x_stat + x_end) / 2, 9.3, "death\nphase", ha="center", va="top", fontsize=14, color=INK)
    
    ax1.set_title("S-shaped (sigmoid) growth curve", fontsize=16, pad=30, color=INK, weight="bold")
    
    # ------------------ RIGHT: J-SHAPED CURVE ------------------
    # Rise exponentially until crash_x, then sharp drop
    crash_x = 7.0
    x_rise = np.linspace(0.2, crash_x, 200)
    # Exponential rise to ~8.5
    y_rise = 0.25 * np.exp(0.51 * x_rise)
    
    # Sharp crash from crash_x to 7.8 down to ~0.6, then low flat line to 10
    x_drop = np.linspace(crash_x, 7.8, 50)
    y_drop = y_rise[-1] - (y_rise[-1] - 0.7) * ((x_drop - crash_x) / 0.8)**0.8
    
    x_flat = np.linspace(7.8, 10.0, 50)
    y_flat = np.linspace(0.7, 0.5, 50)
    
    x2 = np.concatenate([x_rise, x_drop[1:], x_flat[1:]])
    y2 = np.concatenate([y_rise, y_drop[1:], y_flat[1:]])
    
    ax2.plot(x2, y2, color=DEEP["green"], lw=3.5, zorder=3)
    
    # Annotate exponential growth
    ax2.annotate("exponential growth", xy=(4.8, 2.8), xytext=(2.2, 5.5),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Annotate population crash
    ax2.annotate("population crash", xy=(7.4, 4.5), xytext=(7.5, 7.2),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 ha="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    # Carrying capacity line for context reference (dashed)
    ax2.axhline(K, color=GREY, lw=1.5, ls="--", zorder=1)
    ax2.text(0.3, K + 0.25, "carrying capacity (K)", fontsize=14, color=GREY,
             bbox=dict(fc="white", ec="none", pad=1.5))
    
    ax2.set_title("J-shaped growth curve", fontsize=16, pad=30, color=INK, weight="bold")
    
    save(fig, out)
