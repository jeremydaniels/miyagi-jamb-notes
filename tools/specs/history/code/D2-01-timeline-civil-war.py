from style import *
import numpy as np

def draw(out):
    fig = canvas(18, 9)
    ax = fig.add_subplot(111)
    ax.set_facecolor('white')
    ax.axis('off')

    # Title
    ax.text(9, 8.4, "Timeline of Key Events: 1914 – 1967", 
            ha='center', va='center', fontsize=20, weight='bold', color=INK)

    # Main timeline axis
    y_axis = 4.3
    ax.plot([0.8, 17.2], [y_axis, y_axis], color=INK, lw=3, zorder=2)
    ax.annotate('', xy=(17.4, y_axis), xytext=(17.0, y_axis),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.5, mutation_scale=20),
                zorder=2)

    # 10 milestone events:
    # (x, date_text, title_text, side (+1 top, -1 bottom), stem_len, color_key)
    events = [
        (1.4, "1914", "Amalgamation", 1, 2.0, "blue"),
        (3.1, "1946–1951", "Regional\nConstitutions", -1, 2.0, "green"),
        (5.0, "1960", "Independence", 1, 2.4, "orange"),
        (6.9, "1962–65", "Census and\nElection Crises", -1, 2.2, "pink"),
        (8.8, "Jan 15, 1966", "First Military\nCoup", 1, 2.0, "lav"),
        (10.5, "May 1966", "Unification\nDecree", -1, 2.0, "blue"),
        (12.2, "July 29, 1966", "Counter-Coup", 1, 2.4, "pink"),
        (13.8, "Jan 1967", "Aburi Accord", -1, 2.2, "green"),
        (15.3, "May 27, 1967", "Creation of\n12 States", 1, 2.0, "orange"),
        (16.8, "May 30, 1967", "Declaration\nof Biafra", -1, 2.0, "pink")
    ]

    fill_colors = {
        "blue": BLUE,
        "green": GREEN,
        "orange": ORANGE,
        "pink": PINK,
        "lav": LAV
    }

    for x, date_lbl, title_lbl, side, stem_len, col_key in events:
        y_node = y_axis + side * stem_len
        edge_col = DEEP[col_key]
        bg_col = fill_colors[col_key]

        # Stem line
        ax.plot([x, x], [y_axis, y_node], color=edge_col, lw=2, linestyle='-', zorder=3)
        
        # Axis dot
        ax.plot(x, y_axis, marker='o', markersize=9, color=edge_col,
                markeredgecolor='white', markeredgewidth=1.8, zorder=5)

        # Content card layout
        if side == 1:
            # Date above node, title above date
            card_y = y_node + 0.35
            ax.text(x, card_y, f"{date_lbl}\n{title_lbl}",
                    ha='center', va='bottom', fontsize=14, color=INK,
                    linespacing=1.2,
                    bbox=dict(boxstyle="round,pad=0.5", facecolor=bg_col,
                              edgecolor=edge_col, lw=1.8, alpha=0.9),
                    zorder=6)
        else:
            # Date below node, title below date
            card_y = y_node - 0.35
            ax.text(x, card_y, f"{date_lbl}\n{title_lbl}",
                    ha='center', va='top', fontsize=14, color=INK,
                    linespacing=1.2,
                    bbox=dict(boxstyle="round,pad=0.5", facecolor=bg_col,
                              edgecolor=edge_col, lw=1.8, alpha=0.9),
                    zorder=6)

    ax.set_xlim(0.5, 17.8)
    ax.set_ylim(0.5, 9.0)

    save(fig, out)
