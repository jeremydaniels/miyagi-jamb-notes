from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Silicon wafer position: rectangular wafer from x=2.0 to x=6.2
    # Bottom layer: P-type silicon (y: 1.4 to 2.8)
    # Top layer: N-type silicon (y: 2.8 to 4.2)
    wx0, wx1 = 2.0, 6.2
    w_width = wx1 - wx0

    p_rect = patches.Rectangle((wx0, 1.4), w_width, 1.4, fc=LAV, ec=DEEP['lav'], lw=2, zorder=2)
    ax.add_patch(p_rect)

    n_rect = patches.Rectangle((wx0, 2.8), w_width, 1.4, fc=BLUE, ec=DEEP['blue'], lw=2, zorder=2)
    ax.add_patch(n_rect)

    # Junction line between P-type and N-type at y=2.8
    ax.plot([wx0, wx1], [2.8, 2.8], color=GREY, lw=2, linestyle='--', zorder=3)

    # Layer labels: placed cleanly to the left with arrows pointing into layers to avoid overlap
    ax.text(wx0 - 0.25, 3.5, "N-type silicon", fontsize=15, fontweight='bold', color=INK,
            va='center', ha='right', bbox=dict(fc='white', ec=BLUE, boxstyle='round,pad=0.25'))
    ax.annotate('', xy=(wx0 + 0.15, 3.5), xytext=(wx0 - 0.2, 3.5),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=1.8), zorder=5)

    ax.text(wx0 - 0.25, 2.1, "P-type silicon", fontsize=15, fontweight='bold', color=INK,
            va='center', ha='right', bbox=dict(fc='white', ec=LAV, boxstyle='round,pad=0.25'))
    ax.annotate('', xy=(wx0 + 0.15, 2.1), xytext=(wx0 - 0.2, 2.1),
                arrowprops=dict(arrowstyle="->", color=DEEP['lav'], lw=1.8), zorder=5)

    # Sunlight (wavy yellow/orange arrows pointing down) striking top layer
    # Placed on the right portion of the wafer (x = 3.8 to 5.6)
    sun_x_positions = [3.8, 4.4, 5.0, 5.6]
    for sx in sun_x_positions:
        sy = np.linspace(4.35, 6.1, 80)
        sw = sx + 0.10 * np.sin((sy - 4.35) * 4 * np.pi)
        ax.plot(sw, sy, color=DEEP['orange'], lw=2.5, zorder=3)
        # Downward arrowhead striking top of wafer
        ax.annotate('', xy=(sx, 4.25), xytext=(sw[5], sy[5]),
                    arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=2.5, mutation_scale=16),
                    zorder=4)

    ax.text(4.7, 6.55, "Sunlight (photons)", fontsize=15, fontweight='bold', color=DEEP['orange'],
            ha='center', va='center', bbox=dict(fc='white', ec=ORANGE, boxstyle='round,pad=0.3'))

    # Free electrons inside N-type layer knocked loose
    electron_coords = [(2.6, 3.5), (3.3, 3.2), (3.3, 3.8), (4.2, 3.5), (5.2, 3.4), (5.8, 3.7)]
    for ex, ey in electron_coords:
        c = patches.Circle((ex, ey), 0.15, fc=CREAM, ec=INK, lw=1.5, zorder=5)
        ax.add_patch(c)
        ax.text(ex, ey, "–", fontsize=15, ha='center', va='center', color=INK, fontweight='bold', zorder=6)

    # Annotation for "Free electrons" placed in the clear upper-left area (x=2.6, y=5.3)
    # Pointing down to electron at (2.6, 3.65) without crossing any wavy sunlight rays
    ax.text(2.6, 5.3, "Free electrons", fontsize=15, fontweight='bold', color=INK,
            ha='center', va='center', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25', zorder=7), zorder=8)
    ax.annotate('', xy=(2.6, 3.7), xytext=(2.6, 5.0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8), zorder=8)

    # External circuit / wire
    # Wire starts from top contact of N-type at (wx1, 3.8) -> (8.0, 3.8) -> down to lightbulb
    # Bottom wire from P-type at (wx1, 1.8) -> (8.0, 1.8) -> up to lightbulb
    bulb_x, bulb_y = 8.0, 2.8

    # Metal contact tabs on wafer edge
    ax.plot([wx1 - 0.2, wx1], [3.8, 3.8], lw=5, color=GREY, zorder=3)
    ax.plot([wx1 - 0.2, wx1], [1.8, 1.8], lw=5, color=GREY, zorder=3)

    # Wire paths
    ax.plot([wx1, 8.0, 8.0], [3.8, 3.8, bulb_y + 0.45], color=INK, lw=2.5, zorder=2)
    ax.plot([wx1, 8.0, 8.0], [1.8, 1.8, bulb_y - 0.45], color=INK, lw=2.5, zorder=2)

    # Current flow arrows & label
    ax.annotate('', xy=(7.3, 3.8), xytext=(6.7, 3.8),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2.5, mutation_scale=16), zorder=4)
    ax.annotate('', xy=(8.0, 3.4), xytext=(8.0, 3.7),
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2.5, mutation_scale=16), zorder=4)

    ax.text(7.0, 4.15, "Electric current", fontsize=14, color=DEEP['blue'], fontweight='bold', ha='center',
            bbox=dict(fc='white', ec=BLUE, boxstyle='round,pad=0.25'))

    # Glowing lightbulb at (bulb_x, bulb_y)
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        r_in = 0.55
        r_out = 0.85
        gx0 = bulb_x + r_in * np.cos(angle)
        gy0 = bulb_y + r_in * np.sin(angle)
        gx1 = bulb_x + r_out * np.cos(angle)
        gy1 = bulb_y + r_out * np.sin(angle)
        ax.plot([gx0, gx1], [gy0, gy1], color=DEEP['orange'], lw=2, zorder=1)

    bulb_glow = patches.Circle((bulb_x, bulb_y), 0.45, fc=CREAM, ec=DEEP['orange'], lw=2.5, zorder=4)
    ax.add_patch(bulb_glow)

    # Filament inside bulb
    fil_x = [bulb_x - 0.15, bulb_x - 0.08, bulb_x, bulb_x + 0.08, bulb_x + 0.15]
    fil_y = [bulb_y - 0.15, bulb_y + 0.12, bulb_y + 0.02, bulb_y + 0.12, bulb_y - 0.15]
    ax.plot(fil_x, fil_y, color=DEEP['orange'], lw=2, zorder=5)

    # Lightbulb label
    ax.text(bulb_x, bulb_y - 0.95, "Lightbulb", fontsize=15, fontweight='bold', color=INK,
            va='top', ha='center', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Title
    ax.text(5.0, 7.4, "Simple Photovoltaic Cell", fontsize=18, fontweight='bold', color=INK, ha='center')

    save(fig, out)
