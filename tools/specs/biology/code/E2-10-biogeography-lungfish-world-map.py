from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, ConnectionPatch

def draw(out):
    fig = canvas(14, 9.5)
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
    ax.set_xlim(-130, 160)
    ax.set_ylim(-60, 65)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw World Continents
    world_polys = continent_polys('World')
    for poly in world_polys:
        coords = np.array(poly)
        ax.fill(coords[:, 0], coords[:, 1], color=CREAM, ec=GREY, lw=1.2, zorder=1)

    # Highlight Nigeria specifically as noted in description
    try:
        nig_poly = nigeria_poly()
        coords = np.array(nig_poly)
        ax.fill(coords[:, 0], coords[:, 1], color=GREEN, alpha=0.35, ec=DEEP['green'], lw=1, zorder=2)
    except:
        pass

    # Helper icon drawers
    def draw_fish(x, y, scale=1.0, color=DEEP['blue']):
        t = np.linspace(0, 2*np.pi, 50)
        body_x = x + 3.0 * scale * np.cos(t)
        body_y = y + 1.2 * scale * np.sin(t)
        ax.fill(body_x, body_y, color=color, zorder=5)
        # Tail
        tail_x = [x - 2.8 * scale, x - 4.5 * scale, x - 4.5 * scale]
        tail_y = [y, y + 1.2 * scale, y - 1.2 * scale]
        ax.fill(tail_x, tail_y, color=color, zorder=5)
        # Eye
        ax.scatter([x + 2.0 * scale], [y + 0.3 * scale], s=10 * scale, color='white', zorder=6)

    def draw_marsupial(x, y, scale=1.0, color=DEEP['orange']):
        # Simple kangaroo / marsupial silhouette sketch
        body = FancyBboxPatch((x - 1.5*scale, y - 2*scale), 3*scale, 4*scale,
                              boxstyle="round,pad=0.3", fc=color, ec="none", zorder=5)
        ax.add_patch(body)
        # Ears
        ax.plot([x - 0.8*scale, x - 1.2*scale], [y + 2.2*scale, y + 3.8*scale], lw=2.5*scale, color=color, zorder=5)
        ax.plot([x + 0.2*scale, x + 0.6*scale], [y + 2.2*scale, y + 3.8*scale], lw=2.5*scale, color=color, zorder=5)
        # Tail
        ax.plot([x - 1.5*scale, x - 4.0*scale], [y - 1.5*scale, y - 1.0*scale], lw=3.0*scale, color=color, zorder=5)

    def draw_koala(x, y, scale=1.0, color=INK):
        # Round head and large ears
        circle = plt.Circle((x, y), 1.8*scale, color=color, zorder=5)
        ax.add_patch(circle)
        ear_l = plt.Circle((x - 1.6*scale, y + 1.4*scale), 0.9*scale, color=color, zorder=5)
        ear_r = plt.Circle((x + 1.6*scale, y + 1.4*scale), 0.9*scale, color=color, zorder=5)
        ax.add_patch(ear_l)
        ax.add_patch(ear_r)
        # Nose
        nose = plt.Circle((x, y - 0.2*scale), 0.5*scale, color='white', zorder=6)
        ax.add_patch(nose)

    def draw_finch(x, y, scale=1.0, color=DEEP['green']):
        # Bird body
        body_x = [x - 2.5*scale, x + 1.5*scale, x + 0.5*scale]
        body_y = [y - 0.8*scale, y, y + 1.5*scale]
        ax.fill([x-2*scale, x+1.5*scale, x, x-1.5*scale], [y-1*scale, y, y+1.5*scale, y], color=color, zorder=5)
        # Beak
        ax.fill([x + 1.5*scale, x + 3.2*scale, x + 1.3*scale], [y + 0.2*scale, y, y - 0.6*scale], color=INK, zorder=6)

    def draw_lemur(x, y, scale=1.0, color=DEEP['pink']):
        # Lemur head + striped tail
        head = plt.Circle((x, y), 1.5*scale, color=color, zorder=5)
        ax.add_patch(head)
        # Ears
        ax.fill([x-1.5*scale, x-1.0*scale, x-0.5*scale], [y+1.0*scale, y+2.5*scale, y+1.2*scale], color=color, zorder=5)
        ax.fill([x+0.5*scale, x+1.0*scale, x+1.5*scale], [y+1.2*scale, y+2.5*scale, y+1.0*scale], color=color, zorder=5)
        # Arched tail
        t_tail = np.linspace(0, np.pi * 0.9, 20)
        tail_x = x + 1.5*scale + 2.5*scale * np.sin(t_tail)
        tail_y = y - 1.5*scale + 4.0*scale * (1 - np.cos(t_tail))
        ax.plot(tail_x, tail_y, color=color, lw=3.5*scale, zorder=5)

    # 1. Lungfish locations: South America (-60, -10), Tropical Africa/Nigeria (10, 5), Australia (138, -25)
    sa_lf = (-60, -10)
    af_lf = (10, 5)
    au_lf = (136, -22)

    # Lungfish icons
    draw_fish(sa_lf[0], sa_lf[1], scale=1.2, color=DEEP['blue'])
    draw_fish(af_lf[0], af_lf[1], scale=1.2, color=DEEP['blue'])
    draw_fish(au_lf[0], au_lf[1], scale=1.2, color=DEEP['blue'])

    # Faint dashed lines connecting lungfish
    line1_x = np.linspace(sa_lf[0], af_lf[0], 50)
    line1_y = np.linspace(sa_lf[1], af_lf[1], 50) - 6 * np.sin(np.linspace(0, np.pi, 50))
    ax.plot(line1_x, line1_y, color=DEEP['blue'], lw=1.8, ls='--', alpha=0.7, zorder=3)

    line2_x = np.linspace(af_lf[0], au_lf[0], 50)
    line2_y = np.linspace(af_lf[1], au_lf[1], 50) - 16 * np.sin(np.linspace(0, np.pi, 50))
    ax.plot(line2_x, line2_y, color=DEEP['blue'], lw=1.8, ls='--', alpha=0.7, zorder=3)

    # Label for lungfish
    ax.text(35, -28, "lungfish (Africa, South America, Australia)", fontsize=14, color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['blue'], lw=1.2), zorder=10)

    # 2. Marsupials in Australia: Kangaroo & Koala
    draw_marsupial(123, -28, scale=1.2, color=DEEP['orange'])
    draw_koala(145, -32, scale=1.1, color=INK)
    ax.text(134, -43, "marsupials (Australia)", fontsize=14, color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['orange'], lw=1.2), zorder=10)

    # 3. Darwin's finches: Galápagos Islands (-90, -1) and arrow from South America (-72, -3)
    draw_finch(-92, -1, scale=1.1, color=DEEP['green'])
    ax.scatter([-91], [-0.5], s=40, color=DEEP['green'], zorder=4)
    # Arrow from South America to Galapagos
    ax.annotate("", xy=(-90, -1), xytext=(-73, -4),
                arrowprops=dict(arrowstyle="->", color=DEEP['green'], lw=2.0, mutation_scale=15), zorder=6)
    ax.text(-90, 10, "Darwin's finches (Galápagos)", fontsize=14, color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['green'], lw=1.2), zorder=10)

    # 4. Lemur on Madagascar (47, -20)
    draw_lemur(48, -20, scale=1.0, color=DEEP['pink'])
    ax.text(58, -3, "lemurs (Madagascar)", fontsize=14, color=INK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['pink'], lw=1.2), zorder=10)
    ax.annotate("", xy=(48, -17), xytext=(58, -5),
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=1.5), zorder=6)

    # Title & Caption
    ax.text(15, 58, "Biogeography & Continental Drift Evidence", fontsize=18, fontweight='bold',
            ha='center', va='center', color=INK)
    ax.text(-128, -56, "Sketch map: zones are approximate", fontsize=14, color=GREY, style='italic', ha='left')

    # Inset in lower-left corner: Supercontinent Gondwana
    inset_ax = fig.add_axes([0.05, 0.08, 0.32, 0.32])
    inset_ax.set_aspect('equal')
    inset_ax.set_xlim(-15, 15)
    inset_ax.set_ylim(-15, 15)
    inset_ax.axis('off')

    # Inset background card
    card = FancyBboxPatch((-14, -14), 28, 28, boxstyle="round,pad=0.5",
                          fc='white', ec=GREY, lw=1.5, zorder=1)
    inset_ax.add_patch(card)
    inset_ax.text(0, 11, "Gondwana (joined continents)", fontsize=14, fontweight='bold',
                  ha='center', va='center', color=INK, zorder=5)

    # Fitted jigsaw pieces for Gondwana: South America, Africa, Antarctica, India, Australia
    # Africa (center)
    af_g_poly = [(-2, 8), (4, 7), (5, 3), (3, -2), (1, -6), (-2, -5), (-3, 1), (-4, 5)]
    inset_ax.fill(*zip(*af_g_poly), color=CREAM, ec=INK, lw=1.3, zorder=2)
    inset_ax.text(0.5, 2, "Africa", fontsize=14, ha='center', va='center', color=INK, zorder=3)

    # South America (west of Africa, snugly touching)
    sa_g_poly = [(-4, 5), (-3, 1), (-2, -5), (-4, -8), (-7, -5), (-8, 0), (-6, 4)]
    inset_ax.fill(*zip(*sa_g_poly), color=CREAM, ec=INK, lw=1.3, zorder=2)
    inset_ax.text(-5.5, -1, "S. America", fontsize=14, ha='center', va='center', color=INK, zorder=3)

    # Antarctica (south of Africa & Australia)
    ant_g_poly = [(-4, -8), (1, -6), (6, -6), (8, -8), (5, -11), (-2, -11)]
    inset_ax.fill(*zip(*ant_g_poly), color=CREAM, ec=INK, lw=1.3, zorder=2)
    inset_ax.text(1.5, -9, "Antarctica", fontsize=14, ha='center', va='center', color=INK, zorder=3)

    # India (tucked against east Africa / Antarctica)
    ind_g_poly = [(3, -2), (5, 0), (7, -2), (6, -5), (3, -4)]
    inset_ax.fill(*zip(*ind_g_poly), color=CREAM, ec=INK, lw=1.3, zorder=2)
    inset_ax.text(5, -2.5, "India", fontsize=14, ha='center', va='center', color=INK, zorder=3)

    # Australia (east of Antarctica and India)
    au_g_poly = [(7, -2), (11, -1), (12, -5), (8, -8), (6, -5)]
    inset_ax.fill(*zip(*au_g_poly), color=CREAM, ec=INK, lw=1.3, zorder=2)
    inset_ax.text(9.2, -4.5, "Australia", fontsize=14, ha='center', va='center', color=INK, zorder=3)

    # Faint lungfish distribution band across Gondwana (connecting SA, AF, AU)
    band_x = [-6, -0.5, 4.5, 9.5]
    band_y = [-2.5, -0.5, -3.5, -4.5]
    inset_ax.plot(band_x, band_y, color=DEEP['blue'], lw=3, ls='--', alpha=0.8, zorder=4)

    save(fig, out)
