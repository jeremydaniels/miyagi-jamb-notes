from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(18, 9)
    
    # Age brackets from bottom (0-4) to top (80+)
    age_labels = [
        "0–4", "5–9", "10–14", "15–19", "20–24", "25–29",
        "30–34", "35–39", "40–44", "45–49", "50–54", "55–59",
        "60–64", "65–69", "70–74", "75–79", "80+"
    ]
    n_ages = len(age_labels)
    y_pos = np.arange(n_ages)
    
    # 1. Expanding (e.g. Nigeria): broad base, tapering sharply
    exp_m = np.array([8.8, 7.8, 6.8, 5.8, 4.9, 4.1, 3.4, 2.8, 2.2, 1.7, 1.3, 0.9, 0.6, 0.4, 0.3, 0.2, 0.1])
    exp_f = exp_m * 0.98

    # 2. Stable: column-like, nearly vertical sides, narrowing at top
    stb_m = np.array([3.4, 3.4, 3.5, 3.5, 3.5, 3.4, 3.4, 3.4, 3.3, 3.3, 3.2, 3.1, 2.8, 2.3, 1.8, 1.2, 0.8])
    stb_f = stb_m * 1.02

    # 3. Contracting (e.g. Japan): narrow base, bulge in middle (45-59)
    cnt_m = np.array([2.0, 2.2, 2.4, 2.7, 3.1, 3.3, 3.5, 3.8, 4.0, 4.2, 4.0, 3.8, 3.6, 3.4, 3.0, 2.2, 1.5])
    cnt_f = cnt_m * 1.04

    datasets = [
        (exp_m, exp_f, "expanding (e.g. Nigeria)", "high birth rate"),
        (stb_m, stb_f, "stable", None),
        (cnt_m, cnt_f, "contracting (e.g. Japan)", "low birth rate")
    ]
    
    axes = [fig.add_subplot(1, 3, i + 1) for i in range(3)]
    bar_height = 0.8
    
    for i, (ax, (m_vals, f_vals, title, br_label)) in enumerate(zip(axes, datasets)):
        ax.set_facecolor("white")
        
        # Bars: males to left (negative x), females to right (positive x)
        ax.barh(y_pos, -m_vals, height=bar_height, color=BLUE, edgecolor=DEEP["blue"], linewidth=1.2, zorder=2)
        ax.barh(y_pos, f_vals, height=bar_height, color=PINK, edgecolor=DEEP["pink"], linewidth=1.2, zorder=2)
        
        # Central spine
        ax.axvline(0, color=INK, linewidth=1.5, zorder=1)
        
        # Age group labels in the middle with an opaque white bbox to hide the spine
        for y, lab in zip(y_pos, age_labels):
            ax.text(0, y, lab, ha="center", va="center", fontsize=14, color=INK, zorder=4,
                    bbox=dict(boxstyle="square,pad=0.15", facecolor="white", edgecolor="none", alpha=1.0))
            
        ax.set_ylim(-0.8, n_ages + 0.8)
        ax.set_xlim(-10.5, 10.5)
        
        # Remove default ticks/spines
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ["top", "right", "left", "bottom"]:
            ax.spines[spine].set_visible(False)
            
        # Title of the pyramid
        ax.text(0, n_ages + 0.6, title, ha="center", va="bottom", fontsize=16, weight="bold", color=INK)
        
        # Sub-labels: "males" and "females"
        ax.text(-5.5, n_ages - 0.2, "males", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["blue"])
        ax.text(5.5, n_ages - 0.2, "females", ha="center", va="center", fontsize=14, weight="bold", color=DEEP["pink"])
        
        # Birth rate annotations
        if br_label:
            ax.text(0, -0.7, br_label, ha="center", va="top", fontsize=14, color=INK,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=CREAM, edgecolor=GREY, lw=1))
            
    # "age group" label on the center plot
    axes[1].text(0, -0.7, "age group", ha="center", va="top", fontsize=14, weight="bold", color=INK, zorder=4,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="none"))
    
    # Annotations for "old people" and "young people" spanning context
    axes[0].annotate("old people", xy=(-1.5, 15.5), xytext=(-6.8, 15.2),
                     arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                     fontsize=14, ha="right", va="center", color=INK,
                     bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY))
                     
    axes[0].annotate("young people", xy=(-8.0, 0.5), xytext=(-8.8, 3.2),
                     arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                     fontsize=14, ha="center", va="bottom", color=INK,
                     bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=GREY))
    
    plt.subplots_adjust(left=0.04, right=0.96, top=0.88, bottom=0.10, wspace=0.18)
    save(fig, out)
