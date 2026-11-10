from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 6.5)
    
    # -------------------------------------------------------------
    # Left subplot: Human growth curve
    # -------------------------------------------------------------
    ax1 = fig.add_subplot(1, 2, 1)
    axes_clean(ax1, "time", "length", 22, 200)
    
    t = np.linspace(0, 20, 300)
    
    # Growth model:
    infancy = 45 * (1 - np.exp(-t / 1.1))
    childhood = 4.2 * t
    puberty = 28 / (1 + np.exp(-(t - 13.2) / 0.85))
    length_raw = 50 + infancy + childhood + puberty
    
    # Smooth asymptotic levelling off around 18-20 years to ~175 cm
    length_human = np.where(t < 17, length_raw, 175 - (175 - length_raw[np.abs(t - 17).argmin()]) * np.exp(-(t - 17) * 0.9))
    length_human = np.minimum(length_human, 175.0)

    ax1.plot(t, length_human, color=DEEP["blue"], lw=3.2)
    ax1.set_title("human growth curve", fontsize=15, pad=14, color=INK, fontweight="bold")
    
    ax1.set_xticks([0, 5, 10, 15, 20])
    ax1.set_xticklabels(["birth", "5", "10", "15", "20 years"], fontsize=11, color=INK)
    
    ax1.annotate("infancy growth", xy=(1.0, 75), 
                 xytext=(3.5, 55), fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    
    ax1.annotate("adolescent growth spurt", xy=(13.2, 145), 
                 xytext=(8.0, 168), fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
                 
    ax1.annotate("adult size", xy=(19.5, 175), 
                 xytext=(15.0, 190), fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # -------------------------------------------------------------
    # Right subplot: Insect (stepwise) growth curve
    # -------------------------------------------------------------
    ax2 = fig.add_subplot(1, 2, 2)
    axes_clean(ax2, "time", "length", 10, 100)
    
    t_insect = [0.0, 2.2, 2.2, 4.8, 4.8, 7.4, 7.4, 9.8]
    l_insect = [20.0, 20.0, 42.0, 42.0, 68.0, 68.0, 90.0, 90.0]
    
    ax2.plot(t_insect, l_insect, color=DEEP["green"], lw=3.2)
    ax2.set_title("insect (stepwise) growth curve", fontsize=15, pad=14, color=INK, fontweight="bold")
    
    ax2.annotate("moult (ecdysis)", xy=(2.2, 31), xytext=(0.6, 52),
                 fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
                 
    ax2.annotate("moult (ecdysis)", xy=(4.8, 55), xytext=(3.0, 78),
                 fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
                 
    ax2.annotate("moult (ecdysis)", xy=(7.4, 79), xytext=(5.6, 94),
                 fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    ax2.annotate("no increase in length\n(hard exoskeleton)", xy=(1.2, 20), xytext=(1.2, 6),
                 fontsize=10.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    ax2.annotate("no increase in length\n(hard exoskeleton)", xy=(3.5, 42), xytext=(4.2, 24),
                 fontsize=10.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    ax2.annotate("no increase in length\n(hard exoskeleton)", xy=(6.1, 68), xytext=(7.1, 48),
                 fontsize=10.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    ax2.annotate("no increase in length\n(hard exoskeleton)", xy=(8.6, 90), xytext=(9.0, 70),
                 fontsize=10.5, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    fig.tight_layout(w_pad=4.5)
    save(fig, out)
