from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 13)
    ax.set_ylim(-0.5, 9.5)
    ax.axis("off")

    # Base / Steps (Foundation)
    # Bottom step
    rect_base1 = patches.Rectangle((-0.5, 0.2), 13.0, 0.6, facecolor=CREAM, edgecolor=INK, linewidth=2, zorder=2)
    # Top step
    rect_base2 = patches.Rectangle((0.2, 0.8), 11.6, 0.5, facecolor=CREAM, edgecolor=INK, linewidth=2, zorder=2)
    ax.add_patch(rect_base1)
    ax.add_patch(rect_base2)

    # Entablature / Architrave beam resting on pillars
    rect_beam = patches.Rectangle((0.4, 4.7), 11.2, 0.7, facecolor=CREAM, edgecolor=INK, linewidth=2, zorder=2)
    ax.add_patch(rect_beam)

    # 5 pillars, labelled from right to left:
    # 1st from right: Shahadah (Faith)
    # 2nd from right: Salah (Prayer)
    # 3rd from right: Zakah (Charity)
    # 4th from right: Sawm (Fasting)
    # 5th from right (leftmost): Hajj (Pilgrimage)
    pillar_labels = [
        "Hajj\n(Pilgrimage)",
        "Sawm\n(Fasting)",
        "Zakah\n(Charity)",
        "Salah\n(Prayer)",
        "Shahadah\n(Faith)"
    ]

    col_x_centers = [1.5, 3.75, 6.0, 8.25, 10.5]
    pillar_width = 1.3
    pillar_bottom = 1.3
    pillar_height = 3.4

    for i, cx in enumerate(col_x_centers):
        # Capital base and top
        cap_b = patches.Rectangle((cx - pillar_width/2 - 0.15, pillar_bottom), pillar_width + 0.3, 0.25,
                                  facecolor=GREY, edgecolor=INK, linewidth=1.5, zorder=3)
        cap_t = patches.Rectangle((cx - pillar_width/2 - 0.15, pillar_bottom + pillar_height - 0.25), pillar_width + 0.3, 0.25,
                                  facecolor=GREY, edgecolor=INK, linewidth=1.5, zorder=3)
        # Pillar body
        body = patches.Rectangle((cx - pillar_width/2, pillar_bottom + 0.25), pillar_width, pillar_height - 0.5,
                                 facecolor=BLUE, edgecolor=INK, linewidth=1.8, zorder=3)
        ax.add_patch(cap_b)
        ax.add_patch(cap_t)
        ax.add_patch(body)

        # Label inside/on pillar
        ax.text(cx, pillar_bottom + pillar_height / 2, pillar_labels[i],
                ha="center", va="center", fontsize=14, weight="bold", color=INK,
                bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.9),
                zorder=4)

    # Dome resting securely on the entablature
    t = np.linspace(0, np.pi, 200)
    rx = 5.2
    ry = 2.8
    dome_x = 6.0 + rx * np.cos(np.pi - t)
    dome_y = 5.4 + ry * np.sin(np.pi - t)

    dome_poly = patches.Polygon(np.column_stack([dome_x, dome_y]), closed=True,
                                facecolor=GREEN, edgecolor=INK, linewidth=2.5, zorder=2)
    ax.add_patch(dome_poly)

    # Dome pinnacle / finial
    ax.plot([6.0, 6.0], [5.4 + ry, 5.4 + ry + 0.6], color=INK, lw=2.5, zorder=3)
    ax.plot([5.85, 6.15], [5.4 + ry + 0.3, 5.4 + ry + 0.3], color=INK, lw=2, zorder=3)
    crescent = patches.Circle((6.0, 5.4 + ry + 0.75), 0.25, facecolor=ORANGE, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(crescent)

    # Dome Label "Islam"
    ax.text(6.0, 6.6, "Islam", ha="center", va="center", fontsize=22, weight="bold", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=INK, lw=1.5), zorder=5)

    save(fig, out)
