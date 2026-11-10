from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 6)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.82, bottom=0.15, wspace=0.25)
    
    # Data for 3 years
    years = ['Year 1', 'Year 2', 'Year 3']
    n_years = len(years)
    x = np.arange(n_years)
    
    # Sub-category values
    crop = np.array([4.5, 5.5, 6.5])
    livestock = np.array([3.0, 3.8, 4.2])
    fishery = np.array([2.0, 2.2, 2.8])
    total = crop + livestock + fishery
    
    # Colors
    c_crop = GREEN
    c_live = BLUE
    c_fish = ORANGE
    c_simple = BLUE
    
    ec_crop = DEEP['green']
    ec_live = DEEP['blue']
    ec_fish = DEEP['orange']
    ec_simple = DEEP['blue']
    
    ymax = 16
    
    # Panel 1: Simple Bar Chart
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_title("Simple Bar Chart", fontsize=16, color=INK, pad=15, weight='bold')
    ax1.bar(x, total, width=0.5, color=c_simple, edgecolor=ec_simple, linewidth=2, label="Total Output")
    ax1.set_ylabel("Agricultural Output", fontsize=14, color=INK)
    ax1.set_xlabel("Year", fontsize=14, color=INK)
    ax1.set_xticks(x)
    ax1.set_xticklabels(years, fontsize=14)
    ax1.set_yticks([])
    ax1.set_ylim(0, ymax)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(INK)
    ax1.spines['bottom'].set_color(INK)
    ax1.legend(loc="upper left", frameon=True, fontsize=14, edgecolor=GREY)
    
    # Panel 2: Component (Stacked) Bar Chart
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_title("Component Bar Chart\n(Stacked)", fontsize=16, color=INK, pad=15, weight='bold')
    ax2.bar(x, crop, width=0.5, color=c_crop, edgecolor=ec_crop, linewidth=2, label="Crop")
    ax2.bar(x, livestock, width=0.5, bottom=crop, color=c_live, edgecolor=ec_live, linewidth=2, label="Livestock")
    ax2.bar(x, fishery, width=0.5, bottom=crop+livestock, color=c_fish, edgecolor=ec_fish, linewidth=2, label="Fishery")
    ax2.set_ylabel("Agricultural Output", fontsize=14, color=INK)
    ax2.set_xlabel("Year", fontsize=14, color=INK)
    ax2.set_xticks(x)
    ax2.set_xticklabels(years, fontsize=14)
    ax2.set_yticks([])
    ax2.set_ylim(0, ymax)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color(INK)
    ax2.spines['bottom'].set_color(INK)
    ax2.legend(loc="upper left", frameon=True, fontsize=14, edgecolor=GREY)
    
    # Panel 3: Multiple (Grouped) Bar Chart
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_title("Multiple Bar Chart\n(Grouped)", fontsize=16, color=INK, pad=15, weight='bold')
    width = 0.22
    ax3.bar(x - width, crop, width=width, color=c_crop, edgecolor=ec_crop, linewidth=2, label="Crop")
    ax3.bar(x, livestock, width=width, color=c_live, edgecolor=ec_live, linewidth=2, label="Livestock")
    ax3.bar(x + width, fishery, width=width, color=c_fish, edgecolor=ec_fish, linewidth=2, label="Fishery")
    ax3.set_ylabel("Agricultural Output", fontsize=14, color=INK)
    ax3.set_xlabel("Year", fontsize=14, color=INK)
    ax3.set_xticks(x)
    ax3.set_xticklabels(years, fontsize=14)
    ax3.set_yticks([])
    ax3.set_ylim(0, ymax)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['left'].set_color(INK)
    ax3.spines['bottom'].set_color(INK)
    ax3.legend(loc="upper left", frameon=True, fontsize=14, edgecolor=GREY)
    
    save(fig, out)
