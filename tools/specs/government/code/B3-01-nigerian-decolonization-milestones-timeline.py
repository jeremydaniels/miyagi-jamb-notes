from style import *
import numpy as np

def draw(out):
    fig = canvas(14, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-2.8, 3.2)
    ax.axis("off")

    # Title
    ax.text(3.5, 2.7, "Key Milestones of Nigerian Decolonization", 
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Milestones data: (year, title, subtitle, color_fill, color_edge, is_above)
    events = [
        ("1922", "Clifford Constitution", "Elective principle introduced", CREAM, DEEP["orange"], True),
        ("1923", "NNDP formed", "First political party", BLUE, DEEP["blue"], False),
        ("1944", "NCNC formed", "Nationalist coalition", GREEN, DEEP["green"], True),
        ("1945", "General Strike", "Workers demand concessions", PINK, DEEP["pink"], False),
        ("1954", "Lyttelton Constitution", "Federalism introduced", LAV, DEEP["lav"], True),
        ("1957/1959", "Regional Self-Government", "East & West (1957), North (1959)", CREAM, DEEP["orange"], False),
        ("1960", "Independence", "Sovereign Federation of Nigeria", GREEN, DEEP["green"], True),
    ]

    # Main timeline axis
    ax.annotate("", xy=(7.2, 0), xytext=(-0.2, 0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=3, mutation_scale=20))

    # Plot events
    for idx, (year, title, desc, fill_c, edge_c, is_above) in enumerate(events):
        x = idx * 1.0 + 0.5
        y_node = 0

        # Node dot on the timeline
        ax.plot(x, y_node, marker="o", markersize=10, markerfacecolor="white",
                markeredgecolor=edge_c, markeredgewidth=3, zorder=5)

        if is_above:
            stem_y = 1.3
            text_y = 1.45
            box_va = "bottom"
            dy_sign = 1
        else:
            stem_y = -1.3
            text_y = -1.45
            box_va = "top"
            dy_sign = -1

        # Stem line connecting timeline to text/card
        ax.plot([x, x], [y_node, stem_y], color=edge_c, lw=2, linestyle="--", zorder=3)

        # Label content
        card_text = f"{year}\n{title}\n({desc})" if desc.startswith("Elective") or desc.startswith("Federalism") else f"{year}\n{title}\n{desc}"
        
        ax.text(x, text_y, card_text, ha="center", va=box_va, fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.5", facecolor=fill_c, edgecolor=edge_c, lw=2),
                zorder=6)

    save(fig, out)
