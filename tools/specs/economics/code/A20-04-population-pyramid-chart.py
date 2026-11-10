from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 8.5)
    
    # Age groups
    age_groups = [
        "0-4", "5-9", "10-14", "15-19", "20-24", "25-29",
        "30-34", "35-39", "40-44", "45-49", "50-54", "55-59",
        "60-64", "65-69", "70-74", "75-79", "80+"
    ]
    n_groups = len(age_groups)
    y_pos = np.arange(n_groups)
    
    # Typical developing country (broad base, tapering sharply)
    # Values in percent of total population
    male_pct = np.array([8.8, 7.8, 6.9, 5.9, 5.0, 4.2, 3.4, 2.7, 2.1, 1.6, 1.2, 0.9, 0.6, 0.4, 0.25, 0.15, 0.08])
    female_pct = np.array([8.5, 7.6, 6.7, 5.7, 4.8, 4.0, 3.3, 2.6, 2.0, 1.5, 1.2, 0.9, 0.6, 0.4, 0.28, 0.18, 0.12])
    
    # Two subplots side by side with gap for age labels
    ax_male = fig.add_axes([0.10, 0.12, 0.36, 0.76])
    ax_fem = fig.add_axes([0.54, 0.12, 0.36, 0.76])
    
    # Male bars (left side, going backwards from 0)
    ax_male.barh(y_pos, male_pct, height=0.75, color=BLUE, edgecolor=DEEP["blue"], linewidth=1.5, align='center')
    ax_male.set_xlim(10, 0)  # Inverted so 0 is at the centre
    ax_male.set_ylim(-0.7, n_groups - 0.3)
    ax_male.set_xticks([10, 8, 6, 4, 2, 0])
    ax_male.set_xticklabels(["10%", "8%", "6%", "4%", "2%", "0%"], fontsize=14, color=INK)
    ax_male.set_yticks([])  # Hide y-ticks on male axis
    ax_male.spines['top'].set_visible(False)
    ax_male.spines['left'].set_visible(False)
    ax_male.spines['right'].set_color(INK)
    ax_male.spines['right'].set_linewidth(1.5)
    ax_male.spines['bottom'].set_color(INK)
    ax_male.spines['bottom'].set_linewidth(1.5)
    ax_male.grid(axis='x', linestyle='--', alpha=0.4, color=GREY)
    
    # Female bars (right side, going forward from 0)
    ax_fem.barh(y_pos, female_pct, height=0.75, color=PINK, edgecolor=DEEP["pink"], linewidth=1.5, align='center')
    ax_fem.set_xlim(0, 10)
    ax_fem.set_ylim(-0.7, n_groups - 0.3)
    ax_fem.set_xticks([0, 2, 4, 6, 8, 10])
    ax_fem.set_xticklabels(["0%", "2%", "4%", "6%", "8%", "10%"], fontsize=14, color=INK)
    ax_fem.set_yticks([])  # Hide y-ticks on female axis
    ax_fem.spines['top'].set_visible(False)
    ax_fem.spines['right'].set_visible(False)
    ax_fem.spines['left'].set_color(INK)
    ax_fem.spines['left'].set_linewidth(1.5)
    ax_fem.spines['bottom'].set_color(INK)
    ax_fem.spines['bottom'].set_linewidth(1.5)
    ax_fem.grid(axis='x', linestyle='--', alpha=0.4, color=GREY)
    
    # Centre age labels between the two axes
    for idx, age in enumerate(age_groups):
        fig.text(0.50, 0.12 + (idx + 0.5) * (0.76 / n_groups), age,
                 ha='center', va='center', fontsize=14, color=INK, fontweight='medium')
    
    # Age column title
    fig.text(0.50, 0.90, "Age group", ha='center', va='center', fontsize=15, fontweight='bold', color=INK)
    
    # Subplot titles (Males / Females)
    ax_male.set_title("Males", fontsize=16, fontweight='bold', color=DEEP["blue"], pad=14)
    ax_fem.set_title("Females", fontsize=16, fontweight='bold', color=DEEP["pink"], pad=14)
    
    # X axis label across the bottom
    fig.text(0.50, 0.04, "Percentage of total population (%)", ha='center', va='center', fontsize=15, color=INK)
    
    # Main title
    fig.text(0.50, 0.96, "Population Pyramid: Typical Developing Country (e.g. Nigeria)",
             ha='center', va='center', fontsize=17, fontweight='bold', color=INK)
    
    # Explanatory annotations
    # Top annotation (elderly)
    ax_fem.annotate("Narrow apex:\nlow life expectancy,\nfew elderly",
                    xy=(0.6, 15.5), xytext=(4.0, 14.5),
                    fontsize=14, color=INK,
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                    bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    
    # Bottom annotation (young dependents)
    ax_male.annotate("Broad base:\nhigh birth rate,\nmany young dependents",
                     xy=(6.5, 1.2), xytext=(9.2, 4.5),
                     fontsize=14, color=INK, ha='center',
                     arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                     bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    
    save(fig, out)
