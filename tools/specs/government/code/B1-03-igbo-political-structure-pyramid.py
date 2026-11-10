from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(5, 6.4, "Structure of the Igbo Political System", 
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK)
    ax.text(5, 5.95, "Bottom-up (segmentary lineage) political organisation", 
            ha='center', va='center', fontsize=14, fontstyle='italic', color=INK)

    # Pyramid geometry parameters
    # Apex at (5, 5.4), base line y = 1.0, half-width at base = 3.6
    y_apex = 5.4
    y_base = 1.0
    w_base = 3.6
    
    # Levels from bottom (0) to top (3)
    # y-cuts for 4 tiers:
    # Tier 0: 1.0 to 2.05 (Base)
    # Tier 1: 2.05 to 3.1
    # Tier 2: 3.1 to 4.15
    # Tier 3: 4.15 to 5.2 (Top)
    y_levels = [1.0, 2.05, 3.1, 4.15, 5.2]
    
    def get_x(y):
        # linear interpolation from apex (5, 5.4) down to base (5 ± w_base, 1.0)
        frac = (y_apex - y) / (y_apex - y_base)
        hw = frac * w_base
        return 5.0 - hw, 5.0 + hw

    colors = [CREAM, GREEN, BLUE, ORANGE]
    edge_colors = [DEEP['orange'], DEEP['green'], DEEP['blue'], DEEP['orange']]
    
    labels = [
        "Ezi / Ulo\n(The Nuclear Family)",
        "Umunna\n(The Extended Family / Lineage)",
        "Ogbe\n(The Village)",
        "Obodo\n(The Village Group / Town)"
    ]

    for i in range(4):
        y_bot = y_levels[i]
        y_top = y_levels[i+1]
        
        x_bl, x_br = get_x(y_bot)
        x_tl, x_tr = get_x(y_top)
        
        pts = np.array([
            [x_bl, y_bot],
            [x_br, y_bot],
            [x_tr, y_top],
            [x_tl, y_top]
        ])
        
        poly = Polygon(pts, closed=True, facecolor=colors[i], edgecolor=edge_colors[i], lw=2.5, zorder=2)
        ax.add_patch(poly)
        
        y_center = (y_bot + y_top) / 2
        ax.text(5.0, y_center, labels[i], ha='center', va='center', 
                fontsize=14.5, fontweight='bold', color=INK, zorder=3)

    # Bottom-up indication arrow
    ax.annotate(
        "", 
        xy=(1.0, 5.0), 
        xytext=(1.0, 1.2),
        arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=20)
    )
    
    # Label beside the arrow
    ax.text(
        0.75, 3.1, "Bottom-Up\nConsensus &\nAuthority", 
        ha='right', va='center', fontsize=14, fontweight='bold', color=INK,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.5)
    )

    save(fig, out)
