import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from style import *

def draw(out):
    fig = canvas(10, 8)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title
    ax.text(
        5, 7.5, "Sources of Tafsīr (Order of Priority)",
        fontsize=18, fontweight="bold", color=INK, ha="center", va="center"
    )

    # 6 levels: bottom (index 0) to top (index 5)
    labels = [
        "1. The Qur'ān itself",
        "2. The Sunnah (Hadīth)",
        "3. Statements of the Sahābah",
        "4. Statements of the Tābi'ūn",
        "5. Classical Arabic Language",
        "6. Ijtihād\n(Reasoning)"
    ]

    colors = [
        GREEN,
        BLUE,
        LAV,
        CREAM,
        ORANGE,
        PINK
    ]
    edge_colors = [
        DEEP["green"],
        DEEP["blue"],
        DEEP["lav"],
        DEEP["orange"],
        DEEP["orange"],
        DEEP["pink"]
    ]

    y_bottom = 0.8
    y_top = 6.9
    h_total = y_top - y_bottom
    n_levels = 6
    dh = h_total / n_levels
    
    half_w_base = 4.5
    half_w_top = 1.0 # Make the top wide enough for the text
    center_x = 5.0

    for i in range(n_levels):
        y0 = y_bottom + i * dh
        y1 = y_bottom + (i + 1) * dh
        
        # Width linearly decreases
        w0 = half_w_base - (half_w_base - half_w_top) * ((y0 - y_bottom) / h_total)
        w1 = half_w_base - (half_w_base - half_w_top) * ((y1 - y_bottom) / h_total)
        
        pts = np.array([
            [center_x - w0, y0],
            [center_x + w0, y0],
            [center_x + w1, y1],
            [center_x - w1, y1]
        ])
            
        poly = Polygon(
            pts,
            closed=True,
            facecolor=colors[i],
            edgecolor=edge_colors[i],
            linewidth=2,
            zorder=2
        )
        ax.add_patch(poly)
        
        y_text = 0.5 * (y0 + y1)
            
        ax.text(
            center_x, y_text, labels[i],
            fontsize=14.5, fontweight="semibold", color=INK,
            ha="center", va="center", zorder=3
        )

    # Optional side indicator showing priority direction
    arrow_x = 0.4
    ax.annotate(
        "",
        xy=(arrow_x, y_bottom + 0.1),
        xytext=(arrow_x, y_top - 0.1),
        arrowprops=dict(arrowstyle="->", color=INK, lw=2, mutation_scale=18)
    )
    ax.text(
        arrow_x + 0.15, (y_bottom + y_top) / 2, "Lower Priority / Interpretive",
        fontsize=14, color=INK, ha="left", va="center", rotation=90,
        bbox=dict(fc="white", ec="none", pad=3)
    )
    ax.text(
        arrow_x + 0.15, y_bottom + 0.5, "Highest Priority",
        fontsize=14, color=INK, ha="left", va="center", rotation=90,
        bbox=dict(fc="white", ec="none", pad=3)
    )

    save(fig, out)
