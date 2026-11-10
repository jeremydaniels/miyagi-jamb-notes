from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Title & Caption
    ax.text(6, 6.4, "Hajj Pilgrimage Route & Key Locations", fontsize=18, fontweight='bold', ha='center', color=INK)
    ax.text(6, 0.4, "Sketch map: zones and distances are approximate", fontsize=14, fontstyle='italic', ha='center', color=GREY)

    # Locations layout (west to east roughly: Makkah -> Mina -> Muzdalifah -> Arafat)
    # Coordinates for center of stations
    coords = {
        'Makkah': (1.8, 3.2),
        'Mina': (5.0, 3.2),
        'Muzdalifah': (7.8, 3.2),
        'Arafat': (10.4, 3.2)
    }

    # Draw shaded zones for each site
    zones = [
        ('Makkah', 1.8, 3.2, 1.8, 2.2, BLUE),
        ('Mina', 5.0, 3.2, 1.8, 2.2, GREEN),
        ('Muzdalifah', 7.8, 3.2, 1.8, 2.2, LAV),
        ('Arafah', 10.4, 3.2, 1.8, 2.2, ORANGE)
    ]

    for name, cx, cy, w, h, col in zones:
        rect = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                      boxstyle="round,pad=0.15",
                                      fc=col, ec=GREY, lw=1.5, alpha=0.35, zorder=1)
        ax.add_patch(rect)

    # Icons & Illustrations
    # 1. Makkah: Ka'bah icon
    kx, ky = 1.8, 3.2
    # Black cube with gold band
    kabah_base = patches.Rectangle((kx - 0.35, ky - 0.35), 0.7, 0.7, fc='#222222', ec=INK, lw=1.5, zorder=4)
    ax.add_patch(kabah_base)
    # Kiswa gold band
    ax.plot([kx - 0.35, kx + 0.35], [ky + 0.15, ky + 0.15], color='#D4AF37', lw=2.5, zorder=5)

    # 2. Mina: Cluster of tents
    def draw_tent(tx, ty, s=0.25):
        tent = patches.Polygon([[tx - s, ty - s], [tx, ty + s], [tx + s, ty - s]],
                               closed=True, fc='white', ec=DEEP['green'], lw=1.8, zorder=4)
        ax.add_patch(tent)
        # tent seam
        ax.plot([tx, tx], [ty - s, ty + s], color=DEEP['green'], lw=1.2, zorder=5)

    draw_tent(5.0 - 0.35, 3.2 - 0.15, 0.25)
    draw_tent(5.0 + 0.35, 3.2 - 0.15, 0.25)
    draw_tent(5.0, 3.2 + 0.2, 0.25)

    # 3. Muzdalifah: Open plain with small pebbles / under the night sky symbol
    mx, my = 7.8, 3.2
    pebbles = [(mx-0.3, my-0.2), (mx-0.1, my+0.1), (mx+0.25, my-0.15), (mx+0.1, my+0.25), (mx+0.35, my+0.1)]
    for px, py in pebbles:
        p_circ = patches.Circle((px, py), 0.08, fc=GREY, ec=INK, lw=1, zorder=4)
        ax.add_patch(p_circ)

    # 4. Arafah: Mount of Mercy (Jabal ar-Rahmah)
    ax_c, ay_c = 10.4, 3.1
    # Hill
    hill = patches.Arc((ax_c, ay_c - 0.4), 1.2, 1.2, angle=0, theta1=0, theta2=180, color=DEEP['orange'], lw=2, zorder=4)
    ax.add_patch(hill)
    hill_poly = patches.Polygon([[ax_c - 0.6, ay_c - 0.4],
                                 [ax_c - 0.4, ay_c + 0.05],
                                 [ax_c, ay_c + 0.2],
                                 [ax_c + 0.4, ay_c + 0.05],
                                 [ax_c + 0.6, ay_c - 0.4]],
                                closed=True, fc='#FFE5CC', ec=DEEP['orange'], lw=2, zorder=4)
    ax.add_patch(hill_poly)
    # Pillar on top of Mount of Mercy
    ax.plot([ax_c, ax_c], [ay_c + 0.2, ay_c + 0.45], color=INK, lw=2.5, zorder=5)

    # Site Labels
    ax.text(1.8, 4.6, "Makkah\n(Ka'bah)", fontsize=15, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(5.0, 4.6, "Mina\n(Tents)", fontsize=15, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(7.8, 4.6, "Muzdalifah\n(Open plain)", fontsize=15, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(10.4, 4.6, "Arafah\n(Mount of Mercy)", fontsize=15, fontweight='bold', ha='center', va='bottom', color=INK)

    # Dotted Pilgrimage Route Paths with Arrows
    arrow_kw = dict(arrowstyle="->,head_length=0.4,head_width=0.25", lw=2.2, linestyle=(0, (4, 3)), color=INK)

    # 1. Makkah -> Mina (Day 8: 8th Dhul-Hijjah)
    path1 = patches.FancyArrowPatch((2.7, 3.5), (4.1, 3.5),
                                    connectionstyle="arc3,rad=-0.15", **arrow_kw)
    ax.add_patch(path1)
    ax.text(3.4, 3.9, "1. 8th Dhul-Hijjah", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # 2. Mina -> Arafah (Day 9 morning, bypasses Muzdalifah directly to Arafah)
    path2 = patches.FancyArrowPatch((5.8, 3.7), (9.6, 3.7),
                                    connectionstyle="arc3,rad=-0.25", **arrow_kw)
    ax.add_patch(path2)
    ax.text(7.7, 5.7, "2. 9th Dhul-Hijjah (Day of Arafah)", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # 3. Arafah -> Muzdalifah (Day 9 sunset)
    path3 = patches.FancyArrowPatch((9.7, 2.7), (8.6, 2.7),
                                    connectionstyle="arc3,rad=-0.15", **arrow_kw)
    ax.add_patch(path3)
    ax.text(9.1, 2.1, "3. 9th Night", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # 4. Muzdalifah -> Mina (Day 10 morning)
    path4 = patches.FancyArrowPatch((7.0, 2.7), (5.8, 2.7),
                                    connectionstyle="arc3,rad=-0.15", **arrow_kw)
    ax.add_patch(path4)
    ax.text(6.4, 2.1, "4. 10th Morning", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # 5. Mina -> Makkah (Tawaf al-Ifadah & Final farewell)
    path5 = patches.FancyArrowPatch((4.2, 2.7), (2.7, 2.7),
                                    connectionstyle="arc3,rad=-0.2", **arrow_kw)
    ax.add_patch(path5)
    ax.text(3.45, 1.6, "5. Return to Makkah\n(Tawaf al-Ifadah)", fontsize=14, ha='center', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    save(fig, out)
