from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 8.5)
    ax = fig.add_subplot(111)
    
    # Towns and relative rainfall values (south to north)
    towns = ["Calabar", "Benin City", "Makurdi", "Kaduna", "Kano", "Maiduguri"]
    rainfall = [3000, 2100, 1300, 1050, 750, 500]  # Relative heights
    
    # 6 soft blue shades from deep to pale blue
    colors = [
        DEEP["blue"],
        "#3B7EA1",
        "#5D9CB8",
        BLUE,
        "#A8CEE0",
        "#CDE5F0"
    ]
    
    x_positions = np.arange(len(towns)) * 1.5 + 1.0
    bar_width = 0.8
    
    # Draw bars
    for i in range(len(towns)):
        rect = patches.Rectangle(
            (x_positions[i] - bar_width/2, 0), bar_width, rainfall[i],
            facecolor=colors[i],
            edgecolor=DEEP["blue"],
            linewidth=1.3
        )
        ax.add_patch(rect)
    
    # Baseline for bars
    ax.plot([0.2, 9.3], [0, 0], color=INK, lw=1.5)
    
    # Town labels above baseline / under bars
    for i, town in enumerate(towns):
        ax.text(x_positions[i], -130, town, ha="center", va="top", fontsize=12, fontweight="bold", color=INK)
    
    # Function to draw vegetation icons below labels
    def draw_icon(i, kind):
        cx = x_positions[i]
        cy = -560  # icon center y
        
        # Ground patch
        ax.plot([cx - 0.5, cx + 0.5], [cy - 100, cy - 100], color=GREY, lw=1.5)
        
        if kind == "mangrove":  # mangrove or rainforest tree
            # stilt roots
            ax.plot([cx, cx - 0.28], [cy - 40, cy - 100], color=DEEP["green"], lw=2)
            ax.plot([cx, cx + 0.28], [cy - 40, cy - 100], color=DEEP["green"], lw=2)
            ax.plot([cx, cx - 0.12], [cy - 40, cy - 100], color=DEEP["green"], lw=2)
            ax.plot([cx, cx + 0.12], [cy - 40, cy - 100], color=DEEP["green"], lw=2)
            # trunk
            ax.plot([cx, cx], [cy - 40, cy + 20], color=DEEP["green"], lw=3.5)
            # canopy
            c1 = patches.Circle((cx, cy + 45), 0.28, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            c2 = patches.Circle((cx - 0.18, cy + 25), 0.2, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            c3 = patches.Circle((cx + 0.18, cy + 25), 0.2, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c1)
            
        elif kind == "rainforest":  # rainforest tree
            # tall trunk with flared buttress
            ax.plot([cx, cx], [cy - 100, cy + 30], color=DEEP["green"], lw=4)
            ax.plot([cx - 0.18, cx], [cy - 100, cy - 60], color=DEEP["green"], lw=2)
            ax.plot([cx + 0.18, cx], [cy - 100, cy - 60], color=DEEP["green"], lw=2)
            # dense canopy
            c1 = patches.Circle((cx, cy + 55), 0.3, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            c2 = patches.Circle((cx - 0.2, cy + 30), 0.22, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            c3 = patches.Circle((cx + 0.2, cy + 30), 0.22, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
            ax.add_patch(c2); ax.add_patch(c3); ax.add_patch(c1)
            
        elif kind == "tall_grass":  # tall grass with trees
            # tree
            ax.plot([cx - 0.18, cx - 0.18], [cy - 100, cy + 15], color=DEEP["green"], lw=2.5)
            c1 = patches.Circle((cx - 0.18, cy + 35), 0.22, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2)
            ax.add_patch(c1)
            # tall grass tufts
            for gx in [cx + 0.08, cx + 0.22, cx + 0.35]:
                ax.plot([gx, gx - 0.06], [cy - 100, cy - 15], color=DEEP["green"], lw=1.8)
                ax.plot([gx, gx + 0.06], [cy - 100, cy - 5], color=DEEP["green"], lw=1.8)
                ax.plot([gx, gx], [cy - 100, cy + 5], color=DEEP["green"], lw=1.8)
                
        elif kind == "short_grass":  # shorter grass with trees
            # small tree
            ax.plot([cx - 0.16, cx - 0.16], [cy - 100, cy], color=DEEP["green"], lw=2)
            c1 = patches.Ellipse((cx - 0.16, cy + 18), 0.38, 50, facecolor="#BBE3C5", edgecolor=DEEP["green"], lw=1.2)
            ax.add_patch(c1)
            # shorter grass tufts
            for gx in [cx + 0.08, cx + 0.22, cx + 0.35]:
                ax.plot([gx, gx - 0.05], [cy - 100, cy - 50], color=DEEP["green"], lw=1.5)
                ax.plot([gx, gx + 0.05], [cy - 100, cy - 45], color=DEEP["green"], lw=1.5)
                
        elif kind == "baobab_acacia":  # baobab and Acacia
            # baobab
            ax.plot([cx - 0.22, cx - 0.22], [cy - 100, cy - 10], color="#967954", lw=5)
            ax.plot([cx - 0.22, cx - 0.35], [cy - 10, cy + 20], color="#967954", lw=2)
            ax.plot([cx - 0.22, cx - 0.1], [cy - 10, cy + 20], color="#967954", lw=2)
            c1 = patches.Circle((cx - 0.35, cy + 24), 0.14, facecolor="#CBE8D3", edgecolor=DEEP["green"], lw=1)
            c2 = patches.Circle((cx - 0.1, cy + 24), 0.14, facecolor="#CBE8D3", edgecolor=DEEP["green"], lw=1)
            ax.add_patch(c1); ax.add_patch(c2)
            # flat-topped acacia
            ax.plot([cx + 0.22, cx + 0.22], [cy - 100, cy - 5], color="#967954", lw=2)
            ax.plot([cx + 0.22, cx + 0.1], [cy - 5, cy + 20], color="#967954", lw=1.5)
            ax.plot([cx + 0.22, cx + 0.32], [cy - 5, cy + 20], color="#967954", lw=1.5)
            el = patches.Ellipse((cx + 0.22, cy + 22), 0.4, 25, facecolor="#BBE3C5", edgecolor=DEEP["green"], lw=1)
            ax.add_patch(el)
            
        elif kind == "shrub":  # sparse thorny shrub
            ax.plot([cx - 0.18, cx - 0.3], [cy - 100, cy - 45], color="#967954", lw=1.5)
            ax.plot([cx - 0.18, cx - 0.08], [cy - 100, cy - 35], color="#967954", lw=1.5)
            ax.plot([cx + 0.18, cx + 0.06], [cy - 100, cy - 50], color="#967954", lw=1.5)
            ax.plot([cx + 0.18, cx + 0.3], [cy - 100, cy - 40], color="#967954", lw=1.5)
            # small thorny shrub clumps
            c1 = patches.Circle((cx - 0.3, cy - 40), 0.11, facecolor="#D9EAD3", edgecolor=DEEP["green"], lw=1)
            c2 = patches.Circle((cx - 0.08, cy - 30), 0.11, facecolor="#D9EAD3", edgecolor=DEEP["green"], lw=1)
            c3 = patches.Circle((cx + 0.18, cy - 42), 0.11, facecolor="#D9EAD3", edgecolor=DEEP["green"], lw=1)
            ax.add_patch(c1); ax.add_patch(c2); ax.add_patch(c3)

    veg_types = ["mangrove", "rainforest", "tall_grass", "short_grass", "baobab_acacia", "shrub"]
    veg_labels = [
        "mangrove or\nrainforest tree",
        "rainforest tree",
        "tall grass\nwith trees",
        "shorter grass\nwith trees",
        "baobab and\nAcacia",
        "sparse thorny\nshrub"
    ]
    
    for i in range(len(towns)):
        draw_icon(i, veg_types[i])
        ax.text(x_positions[i], -770, veg_labels[i], ha="center", va="top", fontsize=11, color=INK)

    # South to north arrow and annotation under chart
    arrow_y = -1350
    ax.annotate(
        "",
        xy=(8.7, arrow_y),
        xytext=(0.8, arrow_y),
        arrowprops=dict(arrowstyle="->", lw=2, color=INK)
    )
    ax.text(0.8, arrow_y + 40, "south", ha="center", va="bottom", fontsize=12, fontweight="bold", color=INK)
    ax.text(8.7, arrow_y + 40, "north", ha="center", va="bottom", fontsize=12, fontweight="bold", color=INK)
    ax.text(4.75, arrow_y - 65, "rainfall decreases northwards", ha="center", va="top", fontsize=12.5, fontstyle="italic", color=INK)

    # Y-axis label
    ax.set_ylabel("annual rainfall (approximate)", fontsize=13, fontweight="bold", color=INK, labelpad=12)
    
    # Hide spines and ticks
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.set_yticks([])
    
    # Limits
    ax.set_xlim(0.0, 9.6)
    ax.set_ylim(-1600, 3200)
    
    save(fig, out)
