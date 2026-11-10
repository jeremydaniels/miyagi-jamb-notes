from style import *
import numpy as np
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_subplot(111)

    # Coordinate extents for Nigeria map with generous margins for labels
    ax.set_xlim(2.0, 15.6)
    ax.set_ylim(3.6, 15.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Realistic generalized outer outline of Nigeria
    nigeria_outline = np.array([
        [2.7, 6.4], [2.7, 7.5], [3.0, 8.5], [3.6, 9.5], [3.7, 10.3],
        [4.2, 11.5], [3.6, 11.7], [4.5, 12.0], [4.8, 13.0], [5.2, 13.8],
        [6.0, 13.8], [7.0, 13.3], [8.0, 13.3], [9.0, 13.0], [10.0, 13.5],
        [12.0, 13.4], [13.2, 13.7], [13.7, 13.7], [14.3, 13.0], [14.6, 12.5],
        [14.2, 11.8], [13.5, 11.0], [13.8, 10.5], [13.3, 9.5], [12.0, 9.0],
        [12.2, 8.0], [11.5, 7.0], [11.2, 6.7], [10.0, 6.5], [9.2, 6.0],
        [8.5, 4.7], [7.5, 4.4], [6.5, 4.4], [5.5, 5.0], [5.0, 5.7],
        [4.0, 6.2], [3.0, 6.3], [2.7, 6.4]
    ])

    poly_country = Polygon(nigeria_outline, closed=True, facecolor='#FAF9F5', edgecolor=INK, lw=1.8, zorder=1)
    ax.add_patch(poly_country)

    # Schematic state boundaries inside Nigeria (faint)
    state_lines = [
        [[3.6, 6.5], [4.0, 7.5], [3.5, 8.5]],
        [[3.5, 8.5], [5.0, 8.0], [5.2, 7.0], [4.5, 6.4]],
        [[4.5, 6.4], [5.5, 6.4], [6.0, 7.2], [5.0, 8.0]],
        [[3.6, 9.5], [5.5, 9.0], [6.8, 9.0]],
        [[5.5, 9.0], [5.8, 8.0], [7.0, 8.0]],
        [[6.0, 10.0], [7.5, 10.0], [8.5, 9.5]],
        [[4.5, 12.0], [6.0, 11.5], [6.5, 10.0]],
        [[6.5, 10.0], [7.5, 10.5], [8.8, 10.5]],
        [[7.0, 13.3], [7.5, 11.8], [9.0, 11.8]],
        [[9.0, 13.0], [9.5, 11.5], [10.5, 11.5]],
        [[9.5, 11.5], [10.0, 9.5], [11.2, 9.5]],
        [[10.5, 11.5], [11.5, 11.5], [12.5, 12.0]],
        [[11.5, 11.5], [11.8, 10.0], [13.0, 10.0]],
        [[8.5, 9.5], [9.0, 8.5], [10.0, 8.0], [11.5, 7.0]],
        [[7.0, 8.0], [8.0, 7.5], [9.0, 7.5]],
        [[8.0, 7.5], [7.5, 6.0], [7.0, 5.0]],
        [[7.5, 6.0], [8.5, 6.0], [8.5, 5.0]],
        [[8.5, 6.0], [9.5, 6.8]],
        [[6.0, 7.2], [6.8, 6.5], [6.5, 5.2]],
        [[6.8, 6.5], [7.5, 6.5]]
    ]
    for sl in state_lines:
        pts = np.array(sl)
        ax.plot(pts[:, 0], pts[:, 1], color=GREY, lw=0.9, ls='--', alpha=0.7, zorder=2)

    # Lake Chad (north-east corner)
    lake_chad = np.array([
        [13.5, 13.5], [14.0, 13.8], [14.7, 13.5], [14.6, 12.8],
        [14.0, 12.7], [13.6, 13.0], [13.5, 13.5]
    ])
    ax.add_patch(Polygon(lake_chad, closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.3, alpha=0.9, zorder=3))

    # Rivers: Niger & Benue (confluence near Lokoja ~ 6.7°E, 7.8°N)
    river_niger_upper = np.array([
        [3.8, 11.7], [4.2, 11.0], [4.4, 10.4], [4.5, 9.8],
        [4.8, 9.2], [5.3, 8.9], [6.0, 8.6], [6.7, 7.8]
    ])
    river_niger_lower = np.array([
        [6.7, 7.8], [6.8, 7.0], [6.6, 6.0], [6.2, 5.4], [5.8, 4.7]
    ])
    river_benue = np.array([
        [12.1, 9.0], [11.5, 9.2], [10.5, 8.8], [9.5, 8.4],
        [8.5, 8.0], [7.6, 7.9], [6.7, 7.8]
    ])
    ax.plot(river_niger_upper[:, 0], river_niger_upper[:, 1], color=DEEP['blue'], lw=2.4, zorder=3)
    ax.plot(river_niger_lower[:, 0], river_niger_lower[:, 1], color=DEEP['blue'], lw=2.4, zorder=3)
    ax.plot(river_benue[:, 0], river_benue[:, 1], color=DEEP['blue'], lw=2.4, zorder=3)

    # Niger Delta mouth splits
    ax.plot([6.2, 5.3], [5.4, 5.2], color=DEEP['blue'], lw=1.5, zorder=3)
    ax.plot([6.6, 7.0], [6.0, 4.6], color=DEEP['blue'], lw=1.5, zorder=3)

    # Kainji Lake (on River Niger in Niger / Kwara states)
    kainji_lake = np.array([
        [4.4, 10.2], [4.6, 10.4], [4.7, 10.0], [4.6, 9.6],
        [4.4, 9.6], [4.3, 9.9], [4.4, 10.2]
    ])
    ax.add_patch(Polygon(kainji_lake, closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.4, zorder=4))

    # National Parks (green shaded polygons)
    # 1. Kainji Lake NP (Borgu & Zugurma sectors flanking Kainji Lake)
    kainji_p1 = np.array([[3.7, 9.7], [4.2, 10.3], [4.3, 9.8], [3.9, 9.4]])
    kainji_p2 = np.array([[4.8, 9.7], [5.2, 9.6], [5.1, 9.2], [4.7, 9.3]])
    ax.add_patch(Polygon(kainji_p1, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))
    ax.add_patch(Polygon(kainji_p2, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 2. Old Oyo NP (south-west, Oyo State)
    old_oyo = np.array([[3.6, 8.4], [4.2, 8.9], [4.4, 8.5], [3.9, 8.1]])
    ax.add_patch(Polygon(old_oyo, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 3. Kamuku NP (north-central, Kaduna State)
    kamuku = np.array([[6.3, 10.6], [6.8, 10.8], [6.7, 10.3], [6.2, 10.3]])
    ax.add_patch(Polygon(kamuku, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 4. Okomu NP (south, Edo State)
    okomu = np.array([[5.1, 6.4], [5.6, 6.6], [5.5, 6.1], [5.0, 6.1]])
    ax.add_patch(Polygon(okomu, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 5. Cross River NP (two sections: Oban and Okwangwo)
    cross_river_1 = np.array([[8.3, 5.3], [8.8, 5.7], [8.7, 5.2], [8.2, 5.0]])
    cross_river_2 = np.array([[8.8, 6.1], [9.3, 6.4], [9.2, 6.0], [8.7, 5.8]])
    ax.add_patch(Polygon(cross_river_1, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))
    ax.add_patch(Polygon(cross_river_2, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 6. Gashaka-Gumti NP (east, Taraba and Adamawa on Cameroon border)
    gashaka = np.array([
        [11.2, 7.0], [11.8, 7.2], [12.1, 7.8], [11.7, 8.0],
        [11.3, 7.6], [11.1, 7.2]
    ])
    ax.add_patch(Polygon(gashaka, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))

    # 7. Chad Basin NP (north-east, in Borno and Yobe: Bade-Nguru & Sambisa/Chingurmi)
    cb_sec1 = np.array([[10.3, 12.5], [10.9, 12.7], [10.8, 12.2], [10.2, 12.2]])
    cb_sec2 = np.array([[13.3, 11.6], [13.8, 11.8], [13.9, 11.3], [13.4, 11.2]])
    ax.add_patch(Polygon(cb_sec1, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))
    ax.add_patch(Polygon(cb_sec2, closed=True, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.5, zorder=5))
    # Dashed linkage between Chad Basin sectors to show they belong together
    ax.plot([10.9, 13.3], [12.4, 11.5], color=DEEP['green'], lw=1.0, ls=':', zorder=4)

    # 8. Yankari Game Reserve (north-east, Bauchi State) - Orange marker
    yankari_coord = (9.8, 9.7)
    ax.scatter([yankari_coord[0]], [yankari_coord[1]], s=250, color=ORANGE, edgecolors=DEEP['orange'], lw=2, zorder=6)

    # River & Lake Labels (placed clearly alongside features with opaque white backgrounds)
    box_river = dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP['blue'], lw=0.8, alpha=0.95)
    
    # Corrected placement for River Niger, positioned directly over the main upper section
    ax.text(5.5, 8.8, "River Niger", fontsize=12, color=DEEP['blue'], fontstyle='italic',
            rotation=-26, bbox=box_river, ha='center', va='center', zorder=7)

    # Benue placed cleanly to the south of the river line to prevent overlap
    ax.text(9.5, 7.8, "River Benue", fontsize=12, color=DEEP['blue'], fontstyle='italic',
            rotation=12, bbox=box_river, ha='center', va='center', zorder=7)

    ax.text(14.0, 14.1, "Lake Chad", fontsize=12.5, color=DEEP['blue'], fontweight='semibold',
            ha='center', va='center', bbox=box_river, zorder=7)

    # Park Annotations with pointers (positioned cleanly around periphery)
    park_labels = [
        ("Kainji Lake NP", (4.0, 9.9), (2.4, 10.6)),
        ("Old Oyo NP", (4.0, 8.5), (2.5, 8.8)),
        ("Kamuku NP", (6.5, 10.6), (6.5, 11.8)),
        ("Okomu NP", (5.3, 6.3), (5.0, 5.0)),
        ("Cross River NP", (8.9, 5.7), (9.8, 5.2)),
        ("Gashaka-Gumti NP", (11.6, 7.5), (13.5, 7.3)),
        ("Yankari Game Reserve", (9.8, 9.7), (10.9, 9.0)),
        ("Chad Basin NP", (10.6, 12.4), (10.6, 13.5))
    ]

    for name, target, label_pos in park_labels:
        ax.annotate(
            name,
            xy=target, xytext=label_pos,
            fontsize=11.5, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY, lw=0.9, alpha=0.95),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2, shrinkA=3, shrinkB=4),
            ha='center', va='center', zorder=8
        )

    # Title & Subtitle (top left, moved higher to avoid overlap with map borders)
    ax.text(2.2, 15.0, "National Parks & Game Reserves of Nigeria", fontsize=15, fontweight='bold', color=INK, ha='left')
    ax.text(2.2, 14.6, "Sketch map: zones are approximate", fontsize=11, fontstyle='italic', color=GREY, ha='left')

    # Legend box (bottom left, comfortably away from Okomu NP label)
    leg_x, leg_y = 2.2, 3.8
    ax.add_patch(plt.Rectangle((leg_x, leg_y), 4.2, 1.25, fc="white", ec=GREY, lw=1, zorder=6))

    # Legend entries
    ax.add_patch(plt.Rectangle((leg_x + 0.3, leg_y + 0.72), 0.55, 0.32, fc=GREEN, ec=DEEP['green'], lw=1.2, zorder=7))
    ax.text(leg_x + 1.1, leg_y + 0.88, "National Park", fontsize=11.5, color=INK, va='center', zorder=7)

    ax.scatter([leg_x + 0.58], [leg_y + 0.38], s=140, color=ORANGE, edgecolors=DEEP['orange'], lw=1.5, zorder=7)
    ax.text(leg_x + 1.1, leg_y + 0.38, "Game Reserve", fontsize=11.5, color=INK, va='center', zorder=7)

    save(fig, out)
