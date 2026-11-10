from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 7.5)
    ax = fig.add_subplot(111)
    
    # Configure axes limits and clean appearance
    ax.set_xlim(1918, 1964)
    ax.set_ylim(-3.5, 3.8)
    ax.axis('off')

    # Main timeline axis
    ax.plot([1920, 1962], [0, 0], color=INK, lw=3, zorder=2)
    # Arrowhead at the end of timeline
    ax.annotate('', xy=(1962.5, 0), xytext=(1961.5, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20))

    # Milestones data: (year, main title, subtitle, position above/below (+1/-1), box color, border color)
    milestones = [
        (1922, "1922", "Clifford Constitution", "(Elective Principle)", 1, CREAM, DEEP["orange"]),
        (1946, "1946", "Richards Constitution", "(Regionalism)", -1, BLUE, DEEP["blue"]),
        (1951, "1951", "Macpherson Constitution", "(Quasi-Federalism)", 1, GREEN, DEEP["green"]),
        (1954, "1954", "Lyttelton Constitution", "(True Federalism)", -1, LAV, DEEP["lav"]),
        (1957.5, "1957-1958", "Constitutional\nConferences", "", 1, CREAM, DEEP["orange"]),
        (1960, "1960", "Independence", "", -1, PINK, DEEP["pink"])
    ]

    for year, year_lbl, title, subtitle, direction, bg_col, edge_col in milestones:
        # Node on timeline
        ax.plot(year, 0, marker='o', markersize=10, color=edge_col, mec=INK, mew=2, zorder=4)
        
        # Stem and label positions
        y_text = 1.9 * direction
        
        # Connecting stem line
        ax.plot([year, year], [0, y_text], color=edge_col, lw=2, linestyle='--', zorder=3)
        
        # Combine text content
        if subtitle:
            content = f"{year_lbl}\n{title}\n{subtitle}"
        else:
            content = f"{year_lbl}\n{title}"
        
        # Text box
        ax.text(
            year, y_text, content,
            ha="center", va="center",
            fontsize=14, color=INK,
            fontweight='normal',
            bbox=dict(boxstyle="round,pad=0.5", fc=bg_col, ec=edge_col, lw=2),
            zorder=5
        )

    # Title
    ax.text(
        1941, 3.2,
        "Nigeria's Constitutional Development (1922-1960)",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK
    )

    save(fig, out)
