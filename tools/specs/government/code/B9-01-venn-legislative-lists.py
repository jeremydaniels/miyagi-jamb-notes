from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Circles
    r = 2.4
    y_c = 2.9
    c_left = patches.Circle((3.7, y_c), r, facecolor=BLUE, edgecolor=DEEP["blue"], linewidth=2.5, alpha=0.45)
    c_right = patches.Circle((6.3, y_c), r, facecolor=GREEN, edgecolor=DEEP["green"], linewidth=2.5, alpha=0.45)
    ax.add_patch(c_left)
    ax.add_patch(c_right)

    # Title
    ax.text(5.0, 5.9, "The Three Legislative Lists", fontsize=18, weight="bold", color=INK, ha="center", va="center")

    # Headers for circles
    ax.text(2.6, 5.15, "Federal Government", fontsize=16, weight="bold", color=DEEP["blue"], ha="center", va="center")
    ax.text(7.4, 5.15, "State Government", fontsize=16, weight="bold", color=DEEP["green"], ha="center", va="center")

    # Left content: Exclusive List
    ax.text(2.5, 3.1, "Exclusive List\n(e.g., Defence,\nCurrency)", fontsize=14, color=INK, ha="center", va="center", linespacing=1.3)

    # Middle overlapping content: Concurrent List
    middle_text = "Concurrent List\n(e.g., Education,\nHealth)\n\nwhere both\ncan make laws"
    ax.text(5.0, 2.9, middle_text, fontsize=14, color=INK, ha="center", va="center", linespacing=1.2)

    # Right content: Residual List
    ax.text(7.5, 3.1, "Residual List\n(e.g., Chieftaincy)", fontsize=14, color=INK, ha="center", va="center", linespacing=1.3)

    save(fig, out)
