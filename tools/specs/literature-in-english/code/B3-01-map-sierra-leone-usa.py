import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
from style import *

def draw(out):
    fig = canvas(10, 6.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-130, 25)
    ax.set_ylim(-5, 60)
    ax.axis('off')

    # Draw world continents as base
    continents = continent_polys('World')
    for poly in continents:
        coords = np.array(poly)
        patch = Polygon(coords, closed=True, facecolor=CREAM, edgecolor=GREY, linewidth=0.8, zorder=1)
        ax.add_patch(patch)

    # Highlight Sierra Leone
    sl_polys = country_polys('Sierra Leone')
    for poly in sl_polys:
        coords = np.array(poly)
        patch = Polygon(coords, closed=True, facecolor=ORANGE, edgecolor=DEEP['orange'], linewidth=1.5, zorder=3)
        ax.add_patch(patch)

    # Points inside Sierra Leone:
    # Freetown (~ -13.23, 8.48)
    # Koidu (~ -10.97, 8.64)
    # Village (e.g. Kenema/rural south-east ~ -11.8, 7.8)
    points = [
        (-13.23, 8.48),  # Freetown
        (-10.97, 8.64),  # Koidu
        (-11.83, 7.88)   # A village
    ]

    for pt in points:
        ax.plot(pt[0], pt[1], marker='o', markersize=5, color=DEEP['pink'], markeredgecolor=INK, markeredgewidth=1, zorder=5)

    # Dotted arrow from Sierra Leone to the United States (e.g. East Coast / central US ~ -77, 38)
    arrow = FancyArrowPatch(
        (-12.5, 8.5),
        (-77.0, 38.0),
        connectionstyle="arc3,rad=-0.25",
        color=INK,
        linestyle='dotted',
        linewidth=2.2,
        arrowstyle="-|>",
        mutation_scale=18,
        zorder=6
    )
    ax.add_patch(arrow)

    save(fig, out)
