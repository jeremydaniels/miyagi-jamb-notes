from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(18, 4.5)
    
    # 5 subplots side by side
    axes = [fig.add_subplot(1, 5, i+1) for i in range(5)]
    
    titles = [
        "Perfectly Inelastic\n(Ed = 0)",
        "Inelastic\n(Ed < 1)",
        "Unitary Elastic\n(Ed = 1)",
        "Elastic\n(Ed > 1)",
        "Perfectly Elastic\n(Ed = ∞)"
    ]
    
    colors = [
        DEEP["blue"],
        DEEP["green"],
        DEEP["orange"],
        DEEP["pink"],
        DEEP["lav"]
    ]
    
    for i, ax in enumerate(axes):
        # Clean axes setup: price (P) on y-axis, quantity (Q) on x-axis
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        
        # Draw clean arrows for axes
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(INK)
        ax.spines['bottom'].set_color(INK)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        ax.set_xlabel("Quantity (Q)", fontsize=14, color=INK, labelpad=8)
        ax.set_ylabel("Price (P)", fontsize=14, color=INK, labelpad=8)
        
        # Subplot Title
        ax.set_title(titles[i], fontsize=15, color=INK, weight="bold", pad=12)

    # 1: Perfectly Inelastic (Ed = 0) -> Vertical line
    axes[0].plot([5, 5], [1.5, 8.5], color=colors[0], lw=3.5)
    axes[0].text(5.4, 8.2, "D", color=colors[0], fontsize=16, weight="bold")

    # 2: Inelastic (Ed < 1) -> Steep downward line
    x2 = np.linspace(3, 7, 100)
    y2 = 8.5 - (8.5 - 1.5) / (7 - 3) * (x2 - 3)
    axes[1].plot(x2, y2, color=colors[1], lw=3.5)
    axes[1].text(7.2, 1.8, "D", color=colors[1], fontsize=16, weight="bold")

    # 3: Unitary Elastic (Ed = 1) -> Rectangular hyperbola (P * Q = constant)
    x3 = np.linspace(1.8, 8.2, 150)
    c = 16.0
    y3 = c / x3
    axes[2].plot(x3, y3, color=colors[2], lw=3.5)
    axes[2].text(8.3, c / 8.2, "D", color=colors[2], fontsize=16, weight="bold")

    # 4: Elastic (Ed > 1) -> Gentle/flat downward line
    x4 = np.linspace(1.5, 8.5, 100)
    y4 = 6.5 - (6.5 - 3.5) / (8.5 - 1.5) * (x4 - 1.5)
    axes[3].plot(x4, y4, color=colors[3], lw=3.5)
    axes[3].text(8.7, 3.5, "D", color=colors[3], fontsize=16, weight="bold")

    # 5: Perfectly Elastic (Ed = infinity) -> Horizontal line
    axes[4].plot([1.5, 8.5], [5, 5], color=colors[4], lw=3.5)
    axes[4].text(8.7, 5, "D", color=colors[4], fontsize=16, weight="bold", va="center")

    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.15, top=0.82, wspace=0.35)
    save(fig, out)
