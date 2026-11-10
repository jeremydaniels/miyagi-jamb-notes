from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    # Canvas size: wide enough for the horizontal row of officials
    fig = canvas(17, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    # Title
    ax.text(8.5, 9.8, "Fulani Emirate System", ha='center', va='center',
            fontsize=18, weight='bold', color=INK)

    # Box styling helper
    def draw_box(x, y, w, h, title, subtitle=None, bg_color=CREAM, edge_color=INK):
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.12,rounding_size=0.15",
            facecolor=bg_color, edgecolor=edge_color, lw=1.8, zorder=3
        )
        ax.add_patch(rect)
        if subtitle:
            # Shift up and down slightly more to accommodate multiline subtitles
            ax.text(x, y + 0.25, title, ha='center', va='center',
                    fontsize=14.5, weight='bold', color=INK, zorder=4)
            ax.text(x, y - 0.2, subtitle, ha='center', va='center',
                    fontsize=13.5, style='italic', color=INK, zorder=4)
        else:
            ax.text(x, y, title, ha='center', va='center',
                    fontsize=16, weight='bold', color=INK, zorder=4)

    # Coordinates
    emir_x, emir_y = 8.5, 8.5
    emir_w, emir_h = 2.4, 0.9
    draw_box(emir_x, emir_y, emir_w, emir_h, "Emir", bg_color=GREEN, edge_color=DEEP["green"])

    # Council / Key Officials (Row of 7)
    officials = [
        ("Waziri", "(Prime\nMinister)"),
        ("Madawaki", "(Army\nCommander)"),
        ("Galadima", "(Capital\nAdministrator)"),
        ("Maaji", "(Treasurer)"),
        ("Sarkin Fada", "(Head of\nPalace Workers)"),
        ("Sarkin\nYan Doka", "(Police Chief)"),
        ("Alkali", "(Judge)")
    ]

    xs = np.linspace(1.4, 15.6, 7)
    officials_y = 5.6
    off_w, off_h = 2.2, 1.4

    # Connect Emir down to horizontal distribution bar for officials
    t_y = 7.1  # horizontal bar level
    ax.plot([emir_x, emir_x], [emir_y - emir_h / 2, t_y], color=DEEP["blue"], lw=2.0, zorder=2)
    ax.plot([xs[0], xs[-1]], [t_y, t_y], color=DEEP["blue"], lw=2.0, zorder=2)

    for i, (title, sub) in enumerate(officials):
        x = xs[i]
        # Line from bar to each official box
        ax.annotate('', xy=(x, officials_y + off_h / 2), xytext=(x, t_y),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.8, mutation_scale=14),
                    zorder=2)
        draw_box(x, officials_y, off_w, off_h, title, sub, bg_color=LAV, edge_color=DEEP["lav"])

    # Territorial / Local Administration hierarchy (Emir -> Hakimi -> Dagaci)
    hakimi_y = 3.0
    dagaci_y = 1.2
    admin_w, admin_h = 4.0, 0.85

    ax.annotate('', xy=(8.5, hakimi_y + admin_h / 2), xytext=(8.5, officials_y - off_h / 2),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=16),
                zorder=2)

    # Label on territorial branch
    ax.text(8.5, (officials_y - off_h / 2 + hakimi_y + admin_h / 2) / 2, "Territorial Administration",
            ha='center', va='center', fontsize=12.5, color=INK, style='italic',
            bbox=dict(fc="white", ec="none", pad=2.0), zorder=5)

    draw_box(8.5, hakimi_y, admin_w, admin_h, "Hakimi", "(District Head)", bg_color=ORANGE, edge_color=DEEP["orange"])

    # Arrow from Hakimi to Dagaci
    ax.annotate('', xy=(8.5, dagaci_y + admin_h / 2), xytext=(8.5, hakimi_y - admin_h / 2),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2, mutation_scale=16),
                zorder=2)

    draw_box(8.5, dagaci_y, admin_w, admin_h, "Dagaci", "(Village Head)", bg_color=CREAM, edge_color=DEEP["orange"])

    save(fig, out)
