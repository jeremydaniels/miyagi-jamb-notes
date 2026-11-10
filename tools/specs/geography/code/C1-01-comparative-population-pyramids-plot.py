from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(15, 8.5)
    
    # Age groups
    age_groups = [
        "0–4", "5–9", "10–14", "15–19", "20–24", "25–29",
        "30–34", "35–39", "40–44", "45–49", "50–54", "55–59",
        "60–64", "65–69", "70–74", "75–79", "80+"
    ]
    n_groups = len(age_groups)
    y_pos = np.arange(n_groups)
    bar_height = 0.78
    
    # Developing Country (Nigeria-style): wide base, rapidly tapering
    # Percentages per cohort (male, female roughly symmetrical)
    dev_male = np.array([8.8, 7.8, 6.9, 6.0, 5.1, 4.3, 3.6, 3.0, 2.4, 1.9, 1.5, 1.2, 0.9, 0.6, 0.4, 0.3, 0.2])
    dev_female = np.array([8.5, 7.6, 6.7, 5.8, 5.0, 4.2, 3.5, 2.9, 2.4, 1.9, 1.6, 1.3, 1.0, 0.7, 0.5, 0.3, 0.3])
    
    # Developed Country (Japan-style): narrow base, bulging middle/older ages
    ind_male = np.array([2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.6, 4.0, 4.3, 4.2, 3.9, 3.8, 3.7, 3.2, 2.4, 2.2])
    ind_female = np.array([2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.5, 3.9, 4.2, 4.2, 4.0, 4.0, 4.1, 3.7, 3.1, 3.4])
    
    # Subplots: left for Developing, right for Developed
    # Leave room in center of each for age labels or on the y-axis
    ax1 = fig.add_axes([0.08, 0.12, 0.38, 0.74])
    ax2 = fig.add_axes([0.56, 0.12, 0.38, 0.74])
    
    # Plotting helper
    for ax, m_data, f_data, title, subtitle in [
        (ax1, dev_male, dev_female, "Developing Country", "(e.g., Nigeria)"),
        (ax2, ind_male, ind_female, "Developed Country", "(e.g., Japan)")
    ]:
        ax.set_facecolor("white")
        # Horizontal bars: Males negative, Females positive
        ax.barh(y_pos, -m_data, height=bar_height, color=BLUE, edgecolor=DEEP["blue"], linewidth=1.2, label="Male")
        ax.barh(y_pos, f_data, height=bar_height, color=PINK, edgecolor=DEEP["pink"], linewidth=1.2, label="Female")
        
        # Center line
        ax.axvline(0, color=GREY, linewidth=1.5)
        
        # Grid lines for percentage readability
        ax.grid(axis='x', linestyle='--', alpha=0.5, color=GREY)
        ax.set_axisbelow(True)
        
        # Limits and ticks
        ax.set_xlim(-10, 10)
        ax.set_ylim(-0.8, n_groups - 0.2)
        
        xticks = [-8, -6, -4, -2, 0, 2, 4, 6, 8]
        xticklabels = [f"{abs(x)}%" for x in xticks]
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, fontsize=14, color=INK)
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(age_groups, fontsize=14, color=INK)
        
        # Spines
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
        ax.spines["left"].set_color(GREY)
        ax.spines["bottom"].set_color(GREY)
        
        # Labels and title
        ax.set_xlabel("Percentage of population", fontsize=15, color=INK, labelpad=8)
        ax.set_title(f"{title}\n{subtitle}", fontsize=17, fontweight="bold", color=INK, pad=12)
        
        # Gender markers at top of pyramid
        ax.text(-5, n_groups - 0.1, "Male", fontsize=15, fontweight="bold", color=DEEP["blue"], ha="center")
        ax.text(5, n_groups - 0.1, "Female", fontsize=15, fontweight="bold", color=DEEP["pink"], ha="center")
        
    ax1.set_ylabel("Age group", fontsize=15, color=INK, labelpad=8)
    
    # Key structural annotations
    ax1.annotate(
        "Wide base:\nhigh birth rate",
        xy=(-7.5, 0.8), xytext=(-9.2, 3.8),
        fontsize=14, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )
    ax1.annotate(
        "Narrow top:\nhigh mortality\nin older ages",
        xy=(0.6, 14.5), xytext=(2.2, 13.5),
        fontsize=14, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )
    
    ax2.annotate(
        "Bulging middle &\naging population",
        xy=(4.2, 10.0), xytext=(4.5, 12.8),
        fontsize=14, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )
    ax2.annotate(
        "Narrow base:\nlow birth rate",
        xy=(-2.4, 0.8), xytext=(-8.8, 3.5),
        fontsize=14, color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3")
    )

    save(fig, out)
