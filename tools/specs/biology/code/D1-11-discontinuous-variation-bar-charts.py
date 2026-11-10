from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 5.5)
    
    # 3 subplots side by side
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)
    
    axes = [ax1, ax2, ax3]
    
    # Common y-axis configuration
    for ax in axes:
        ax.set_ylim(0, 32)
        ax.set_yticks(np.arange(0, 31, 5))
        ax.set_ylabel("Number of pupils", fontsize=12, color=INK)
        ax.tick_params(colors=INK, labelsize=11)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['bottom'].set_color(INK)
        ax.grid(axis='y', linestyle='--', alpha=0.4, color=GREY)
        ax.set_axisbelow(True)

    # Chart 1: Tongue rolling
    bars1 = ["Rollers", "Non-rollers"]
    vals1 = [28, 12]
    colors1 = [BLUE, PINK]
    edgecolors1 = [DEEP["blue"], DEEP["pink"]]
    x1 = np.arange(len(bars1))
    
    ax1.bar(x1, vals1, width=0.55, color=colors1, edgecolor=edgecolors1, linewidth=1.5)
    ax1.set_xticks(x1)
    ax1.set_xticklabels(bars1, fontsize=11, color=INK)
    ax1.set_title("Tongue rolling", fontsize=14, color=INK, pad=12, weight="bold")
    
    for i, v in enumerate(vals1):
        ax1.text(x1[i], v + 0.8, str(v), ha='center', va='bottom', fontsize=11, color=INK)

    # Chart 2: PTC tasting
    bars2 = ["Tasters", "Non-tasters"]
    vals2 = [29, 11]
    colors2 = [GREEN, ORANGE]
    edgecolors2 = [DEEP["green"], DEEP["orange"]]
    x2 = np.arange(len(bars2))
    
    ax2.bar(x2, vals2, width=0.55, color=colors2, edgecolor=edgecolors2, linewidth=1.5)
    ax2.set_xticks(x2)
    ax2.set_xticklabels(bars2, fontsize=11, color=INK)
    ax2.set_title("PTC tasting", fontsize=14, color=INK, pad=12, weight="bold")
    
    for i, v in enumerate(vals2):
        ax2.text(x2[i], v + 0.8, str(v), ha='center', va='bottom', fontsize=11, color=INK)

    # Chart 3: ABO blood groups
    bars3 = ["O", "A", "B", "AB"]
    vals3 = [21, 9, 8, 2]
    colors3 = [LAV, BLUE, GREEN, PINK]
    edgecolors3 = [DEEP["lav"], DEEP["blue"], DEEP["green"], DEEP["pink"]]
    x3 = np.arange(len(bars3))
    
    ax3.bar(x3, vals3, width=0.6, color=colors3, edgecolor=edgecolors3, linewidth=1.5)
    ax3.set_xticks(x3)
    ax3.set_xticklabels(bars3, fontsize=11, color=INK)
    ax3.set_title("ABO blood groups", fontsize=14, color=INK, pad=12, weight="bold")
    
    for i, v in enumerate(vals3):
        ax3.text(x3[i], v + 0.8, str(v), ha='center', va='bottom', fontsize=11, color=INK)

    # Caption at the bottom
    fig.text(0.5, 0.04, "Invented sample data for 40 pupils", ha="center", fontsize=12, style="italic", color=INK)
    
    plt.subplots_adjust(bottom=0.18, top=0.85, wspace=0.35, left=0.08, right=0.96)
    save(fig, out)
