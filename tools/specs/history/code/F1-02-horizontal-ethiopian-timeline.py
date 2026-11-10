from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 7.5)
    ax = fig.add_subplot(111)
    
    # Hide standard axes
    ax.set_xlim(1850, 1900)
    ax.set_ylim(-3.5, 3.5)
    ax.axis('off')

    # Title
    ax.text(1875, 3.0, "19th-Century Ethiopia: Key Historical Milestones", 
            fontsize=18, fontweight='bold', ha='center', va='center', color=INK)

    # Central timeline axis
    ax.annotate('', xy=(1898.5, 0), xytext=(1851.5, 0),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.8", lw=3, color=INK))

    # Events data: (year, text, is_above, color_key, fill_color)
    events = [
        (1855, "Kassa Hailu crowned\nEmperor Theodore II", True, "blue", BLUE),
        (1868, "British expedition and\ndeath of Theodore at Magdala", False, "pink", PINK),
        (1889, "Menelik II crowned;\nTreaty of Wuchale\nsigned with Italy", True, "green", GREEN),
        (1893, "Menelik denounces the\nTreaty of Wuchale", False, "orange", ORANGE),
        (1896, "Ethiopian victory at the\nBattle of Adwa", True, "lav", LAV)
    ]

    for year, text, above, col_key, c_fill in events:
        c_line = DEEP[col_key]
        
        # Central marker
        ax.plot(year, 0, marker='o', markersize=10, color=c_line, zorder=5)
        ax.plot(year, 0, marker='o', markersize=6, color='white', zorder=6)

        # Offsets
        y_label = 0.5 if above else -0.5
        va_label = 'bottom' if above else 'top'
        
        y_callout = 1.3 if above else -1.3
        y_text = 1.5 if above else -1.5
        
        # Date label near line
        ax.text(year, y_label, str(year), fontsize=15, fontweight='bold',
                ha='center', va=va_label, color=c_line,
                bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none"))

        # Vertical connecting line to annotation box
        ax.plot([year, year], [0.8 if above else -0.8, y_callout],
                color=c_line, lw=1.5, ls='--')

        # Annotation box
        ax.text(year, y_text, text, fontsize=14, ha='center', va=va_label, color=INK,
                bbox=dict(boxstyle="round,pad=0.5", fc=c_fill, ec=c_line, lw=1.5))

    save(fig, out)
