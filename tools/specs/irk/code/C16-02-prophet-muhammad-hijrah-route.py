from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 10)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    
    # Coordinate boundaries (Hijaz region / Arabian Peninsula)
    lon_min, lon_max = 34.5, 43.5
    lat_min, lat_max = 19.5, 27.5
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)

    # Simplified smooth Red Sea coastline (Arabian / Hijaz shore)
    red_sea_coast = np.array([
        [34.8, 28.0],
        [35.4, 27.2],
        [36.2, 26.2],
        [37.0, 25.2],
        [37.8, 24.0],
        [38.6, 23.0],
        [39.0, 22.0],
        [39.4, 21.0],
        [40.2, 20.0],
        [41.0, 19.0]
    ])

    # Red Sea water polygon (West side)
    water_poly = np.vstack([
        [[33.0, 28.5]],
        red_sea_coast,
        [[41.0, 18.5], [33.0, 18.5]]
    ])
    
    # Land background polygon (East side)
    land_poly = np.vstack([
        [[33.0, 28.5], [45.0, 28.5], [45.0, 18.5]],
        red_sea_coast[::-1]
    ])

    # Draw Land & Water
    ax.fill(land_poly[:, 0], land_poly[:, 1], color=CREAM, alpha=0.55, zorder=1)
    ax.fill(water_poly[:, 0], water_poly[:, 1], color=BLUE, alpha=0.35, zorder=1)
    ax.plot(red_sea_coast[:, 0], red_sea_coast[:, 1], color=DEEP["blue"], lw=2.0, zorder=2)

    # Locations
    # Madinah and Quba (well inland, east of the coast which is around 37.8 - 38.6 E)
    madinah = np.array([39.61, 24.47])
    quba = np.array([39.61, 24.15])  # Visibly south of Madinah, clearly inland
    
    # Makkah and Cave of Thawr (spaced sufficiently to avoid marker overlap)
    makkah = np.array([39.82, 21.42])
    thawr = np.array([39.82, 20.95])   # Distinctly south of Makkah

    # Route: Starts at Makkah -> Cave of Thawr -> towards coast -> northwards along coast -> turns inland to Quba -> Madinah
    route = np.array([
        makkah,
        thawr,
        [39.40, 20.95],
        [39.15, 21.50],
        [38.80, 22.40],
        [38.60, 23.10],
        [38.75, 23.65],
        quba,
        madinah
    ])

    # Plot Route (single clean dotted line)
    ax.plot(route[:, 0], route[:, 1], color=DEEP["orange"], lw=3.5, ls=":", zorder=4)

    # Add small, neat direction arrows along route segments
    arrow_segs = [(2, 3), (3, 4), (4, 5), (6, 7)]
    for i, j in arrow_segs:
        p1 = route[i]
        p2 = route[j]
        mid = 0.55 * p1 + 0.45 * p2
        d = (p2 - p1)
        d_unit = d / np.hypot(d[0], d[1])
        ax.annotate('', xy=mid + d_unit * 0.16, xytext=mid - d_unit * 0.16,
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2), zorder=5)

    # Key places to plot and label
    places = [
        ("Madinah (Yathrib)", madinah, (14, 2), "left"),
        ("Quba", quba, (14, -2), "left"),
        ("Makkah", makkah, (14, 2), "left"),
        ("Cave of Thawr", thawr, (14, -2), "left")
    ]

    for name, pt, offset, align in places:
        ax.plot(pt[0], pt[1], 'o', color=DEEP["pink"], markersize=8.5, zorder=6, mec=INK, mew=1.5)
        ax.annotate(name, xy=pt, xytext=offset, textcoords="offset points",
                    fontsize=15, fontweight="bold", color=INK, ha=align, va="center",
                    bbox=dict(fc="white", ec="none", pad=2.5, alpha=0.9), zorder=7)

    # Red Sea Label
    ax.text(36.6, 21.8, "Red Sea", fontsize=18, fontstyle="italic", color=DEEP["blue"],
            rotation=-55, ha="center", va="center", zorder=3)

    # Title & Legend Box at upper-left
    ax.text(35.0, 26.7, "The Hijrah Route", fontsize=17, fontweight="bold", color=INK)
    ax.plot([35.0, 36.3], [26.2, 26.2], color=DEEP["orange"], lw=3.2, ls=":", zorder=4)
    ax.text(36.5, 26.2, "Hijrah Route", fontsize=15, color=INK, va="center")

    # Schematic note
    ax.text(35.0, 19.8, "Sketch map: zones are approximate", fontsize=14, fontstyle="italic", color=GREY)

    save(fig, out)
