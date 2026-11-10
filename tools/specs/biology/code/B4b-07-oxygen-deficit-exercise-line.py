import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(11, 7)
    ax = fig.add_subplot(111)
    
    # Axes limits: time from 0 to 14, oxygen uptake 0 to 5.2
    axes_clean(ax, "time", "oxygen uptake", 14, 5.2)
    
    # Time points
    # 0 to 2: rest
    # 2 to 6.5: exercise
    # 6.5 to 13.5: recovery
    t_rest = np.linspace(0, 2, 60)
    t_ex = np.linspace(2, 6.5, 180)
    t_rec = np.linspace(6.5, 13.5, 200)
    
    y_rest_val = 0.8
    y_plateau = 3.6
    
    y_need_val = 4.2
    
    # Uptake curve during exercise: rises sharply to plateau
    k_rise = 2.0
    y_ex = y_rest_val + (y_plateau - y_rest_val) * (1 - np.exp(-k_rise * (t_ex - 2)))
    
    # Recovery curve: falls gradually back to resting level
    y_rec = y_rest_val + (y_plateau - y_rest_val) * np.exp(-0.65 * (t_rec - 6.5))
    
    # Combined curve
    t_full = np.concatenate([t_rest, t_ex, t_rec])
    y_full = np.concatenate([np.full_like(t_rest, y_rest_val), y_ex, y_rec])
    
    # Zone background shading
    ax.axvspan(0, 2, color=GREY, alpha=0.10)
    ax.axvspan(2, 6.5, color=ORANGE, alpha=0.08)
    ax.axvspan(6.5, 13.5, color=BLUE, alpha=0.08)
    
    # Deficit is at the start of exercise where uptake lags behind need.
    t_def = np.linspace(2, 4.0, 100)
    y_def_curve = y_rest_val + (y_plateau - y_rest_val) * (1 - np.exp(-k_rise * (t_def - 2)))
    ax.fill_between(t_def, y_def_curve, y_need_val, color=PINK, alpha=0.45)
    
    # Debt repaid: under the recovery curve above resting level
    ax.fill_between(t_rec, y_rest_val, y_rec, color=LAV, alpha=0.55)
    
    # Dashed line showing oxygen actually needed during exercise above the plateau
    ax.plot([2, 2], [y_rest_val, y_need_val], color=DEEP["pink"], linestyle="--", lw=2.2)
    ax.plot([2, 6.5], [y_need_val, y_need_val], color=DEEP["pink"], linestyle="--", lw=2.2)
    ax.plot([6.5, 6.5], [y_plateau, y_need_val], color=DEEP["pink"], linestyle="--", lw=2.2)
    
    # Resting level dotted line extending through the graph
    ax.axhline(y_rest_val, color=GREY, linestyle=":", lw=1.8)
    ax.text(0.3, y_rest_val + 0.12, "resting level", fontsize=11.5, color=INK, fontweight='medium')
    
    # Vertical boundary markers for zones
    ax.axvline(2, color=GREY, linestyle="--", lw=1.3, alpha=0.6)
    ax.axvline(6.5, color=GREY, linestyle="--", lw=1.3, alpha=0.6)
    
    # Main oxygen uptake curve
    ax.plot(t_full, y_full, color=DEEP["blue"], lw=3.5)
    
    # Zone labels at the top
    ax.text(1.0, 4.85, "rest", ha="center", va="center", fontsize=13.5, fontweight="bold", color=INK)
    ax.text(4.25, 4.85, "exercise", ha="center", va="center", fontsize=13.5, fontweight="bold", color=INK)
    ax.text(10.0, 4.85, "recovery", ha="center", va="center", fontsize=13.5, fontweight="bold", color=INK)
    
    # Label: "oxygen needed by muscles"
    ax.annotate("oxygen needed by muscles", 
                xy=(4.5, y_need_val), xytext=(4.5, 4.52),
                fontsize=11.5, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    
    # Label: "oxygen deficit (anaerobic respiration, lactic acid builds up)"
    # Positioned lower in the exercise zone to avoid overlapping the line and boundaries
    ax.annotate("oxygen deficit\n(anaerobic respiration,\nlactic acid builds up)",
                xy=(2.65, 3.5), xytext=(4.0, 1.8),
                fontsize=11, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.4),
                bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.2))
    
    # Label: "oxygen debt repaid (lactic acid removed)"
    ax.annotate("oxygen debt repaid\n(lactic acid removed)",
                xy=(7.8, 1.8), xytext=(10.2, 2.5),
                fontsize=11.5, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=1.4),
                bbox=dict(fc="white", ec=DEEP["lav"], boxstyle="round,pad=0.3", lw=1.2))
    
    # Label: "oxygen uptake"
    # Positioned clearly in the upper exercise area away from any lines
    ax.annotate("oxygen uptake",
                xy=(5.5, y_plateau), xytext=(5.3, 2.8),
                fontsize=12, color=DEEP["blue"], fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1.2))
    
    save(fig, out)
