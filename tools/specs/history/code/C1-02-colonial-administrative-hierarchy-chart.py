from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw(out):
    # Canvas setup
    fig = canvas(11, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(5.5, 7.0, "Administrative Set-up of the Northern Protectorate",
            ha="center", va="center", fontsize=17, weight="bold", color=INK)

    # Box styling helper
    def draw_box(x, y, text, bg_color=CREAM, border_color=DEEP["blue"]):
        ax.text(x, y, text, ha="center", va="center",
                fontsize=14, color=INK, zorder=4, weight="medium",
                bbox=dict(boxstyle="round,pad=0.8", fc=bg_color, ec=border_color, lw=2.0))

    # Node positions
    # British line (left column)
    x_brit = 3.2
    y_high = 5.8
    y_res = 4.3
    y_do = 2.8

    # Emir / Native Authority (right of DO)
    x_emir = 8.2
    y_emir = 2.8

    # Native institutions (below Emir)
    x_courts = 6.9
    x_treas = 9.5
    y_inst = 1.2

    # Draw connection lines first (zorder=2)
    # High Commissioner -> Resident
    ax.annotate("", xy=(x_brit, y_res + 0.5), xytext=(x_brit, y_high - 0.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2, shrinkA=0, shrinkB=0))

    # Resident -> District Officer
    ax.annotate("", xy=(x_brit, y_do + 0.5), xytext=(x_brit, y_res - 0.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2, shrinkA=0, shrinkB=0))

    # District Officer <-> Emir / Native Authority (Indirect Rule link)
    ax.annotate("", xy=(x_emir - 1.8, y_emir), xytext=(x_brit + 1.8, y_do),
                arrowprops=dict(arrowstyle="-", color=DEEP["orange"], lw=2.2, ls="--", shrinkA=0, shrinkB=0))

    # Emir branching to Native Courts and Treasuries
    # Branch stem down, then split horizontally
    stem_bottom = 2.0
    ax.plot([x_emir, x_emir], [y_emir - 0.5, stem_bottom],
            color=INK, lw=2, zorder=2)
    ax.plot([x_courts, x_treas], [stem_bottom, stem_bottom],
            color=INK, lw=2, zorder=2)

    # Down to Native Courts
    ax.annotate("", xy=(x_courts, y_inst + 0.45), xytext=(x_courts, stem_bottom),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2, shrinkA=0, shrinkB=0))

    # Down to Native Treasuries
    ax.annotate("", xy=(x_treas, y_inst + 0.45), xytext=(x_treas, stem_bottom),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2, shrinkA=0, shrinkB=0))

    # Draw Boxes
    # Top box: High Commissioner (British)
    draw_box(x_brit, y_high,
             "High Commissioner\n(British)",
             bg_color=BLUE, border_color=DEEP["blue"])

    # Resident box
    draw_box(x_brit, y_res,
             "Resident\n(British, in charge of a Province)",
             bg_color=BLUE, border_color=DEEP["blue"])

    # District Officer box
    draw_box(x_brit, y_do,
             "District Officer\n(British)",
             bg_color=BLUE, border_color=DEEP["blue"])

    # Emir / Native Authority box
    draw_box(x_emir, y_emir,
             "Emir / Native Authority\n(Traditional Ruler)",
             bg_color=GREEN, border_color=DEEP["green"])

    # Native Courts
    draw_box(x_courts, y_inst,
             "Native\nCourts",
             bg_color=CREAM, border_color=DEEP["green"])

    # Native Treasuries
    draw_box(x_treas, y_inst,
             "Native\nTreasuries",
             bg_color=CREAM, border_color=DEEP["green"])

    save(fig, out)
