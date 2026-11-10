from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Draw Nigeria boundary
    poly_pts = nigeria_poly()
    # If nigeria_poly returns a list of polygons or list of points
    if isinstance(poly_pts, list) and len(poly_pts) > 0:
        if isinstance(poly_pts[0], (list, np.ndarray)) and len(poly_pts[0]) > 2:
            for p in poly_pts:
                patch = Polygon(p, closed=True, facecolor=CREAM, edgecolor=GREY, linewidth=2, zorder=1)
                ax.add_patch(patch)
        else:
            patch = Polygon(poly_pts, closed=True, facecolor=CREAM, edgecolor=GREY, linewidth=2, zorder=1)
            ax.add_patch(patch)
    else:
        # Fallback simplified shape if needed
        pass

    # Approximate coordinates (lon, lat) of stations
    # Lagos: (3.4, 6.45)
    # Ibadan: (3.9, 7.4)
    # Ilorin: (4.55, 8.5)
    # Minna: (6.55, 9.6)
    # Kaduna: (7.43, 10.5)
    # Kano: (8.53, 12.0)
    # Port Harcourt: (7.0, 4.8)
    # Enugu: (7.5, 6.44)
    # Makurdi: (8.54, 7.73)
    # Jos / branch / feeder roads

    stations = {
        "Lagos": (3.4, 6.45),
        "Ibadan": (3.9, 7.4),
        "Ilorin": (4.55, 8.5),
        "Minna": (6.55, 9.6),
        "Kaduna": (7.43, 10.5),
        "Kano": (8.53, 12.0),
        "Port Harcourt": (7.0, 4.8),
        "Enugu": (7.5, 6.44),
        "Makurdi": (8.54, 7.73)
    }

    # Western Line: Lagos -> Ibadan -> Ilorin -> Minna -> Kaduna -> Kano
    west_pts = np.array([
        stations["Lagos"],
        stations["Ibadan"],
        stations["Ilorin"],
        stations["Minna"],
        stations["Kaduna"],
        stations["Kano"]
    ])

    # Eastern Line: Port Harcourt -> Enugu -> Makurdi -> Kaduna
    east_pts = np.array([
        stations["Port Harcourt"],
        stations["Enugu"],
        stations["Makurdi"],
        (8.1, 9.2), # intermediate curve towards Kaduna
        stations["Kaduna"]
    ])

    # Feeder roads (dotted lines branching off into surrounding areas)
    feeders = [
        # Off Kano
        (stations["Kano"], (10.0, 12.5)),
        (stations["Kano"], (7.2, 12.8)),
        (stations["Kano"], (9.8, 11.2)),
        # Off Kaduna
        (stations["Kaduna"], (8.9, 9.9)), # towards Jos
        (stations["Kaduna"], (6.0, 11.0)),
        # Off Minna
        (stations["Minna"], (5.2, 10.0)),
        (stations["Minna"], (6.8, 8.8)),
        # Off Ilorin
        (stations["Ilorin"], (5.8, 8.2)),
        (stations["Ilorin"], (3.5, 8.8)),
        # Off Ibadan
        (stations["Ibadan"], (4.8, 7.0)),
        (stations["Ibadan"], (2.8, 7.5)),
        # Off Makurdi
        (stations["Makurdi"], (10.0, 7.3)),
        (stations["Makurdi"], (8.8, 6.8)),
        # Off Enugu
        (stations["Enugu"], (8.8, 6.0)),
        (stations["Enugu"], (6.3, 6.3)),
        # Off Port Harcourt
        (stations["Port Harcourt"], (6.0, 5.0)),
        (stations["Port Harcourt"], (7.8, 4.8))
    ]

    # Draw feeder roads
    for p1, p2 in feeders:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=DEEP["orange"], lw=2.2, ls=":", zorder=2)

    # Feeder road legend dummy
    ax.plot([], [], color=DEEP["orange"], lw=2.2, ls=":", label="Feeder roads")

    # Draw Railway Lines
    # Western Line
    ax.plot(west_pts[:, 0], west_pts[:, 1], color=DEEP["blue"], lw=4, solid_capstyle='round', zorder=3, label="Western Railway Line")
    # Eastern Line
    ax.plot(east_pts[:, 0], east_pts[:, 1], color=DEEP["green"], lw=4, solid_capstyle='round', zorder=3, label="Eastern Railway Line")

    # Draw stations
    for name, pt in stations.items():
        ax.scatter(pt[0], pt[1], color=INK, s=60, zorder=4)

    # Station labels and specific annotations required
    # "Lagos", "Port Harcourt", "Enugu (Coal)", "Kano (Groundnut)", "Western Railway Line", "Eastern Railway Line"
    ax.text(stations["Lagos"][0] - 0.2, stations["Lagos"][1] - 0.4, "Lagos", fontsize=15, fontweight="bold",
            ha="right", va="top", color=INK, bbox=dict(fc="white", ec="none", pad=1.5))
    
    ax.text(stations["Port Harcourt"][0] + 0.3, stations["Port Harcourt"][1] - 0.3, "Port Harcourt", fontsize=15, fontweight="bold",
            ha="left", va="top", color=INK, bbox=dict(fc="white", ec="none", pad=1.5))

    ax.text(stations["Enugu"][0] + 0.3, stations["Enugu"][1] - 0.1, "Enugu (Coal)", fontsize=15, fontweight="bold",
            ha="left", va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1.5))

    ax.text(stations["Kano"][0] + 0.3, stations["Kano"][1] + 0.3, "Kano (Groundnut)", fontsize=15, fontweight="bold",
            ha="left", va="bottom", color=INK, bbox=dict(fc="white", ec="none", pad=1.5))

    # Other station labels for geographical completeness
    ax.text(stations["Ibadan"][0] - 0.25, stations["Ibadan"][1] + 0.1, "Ibadan", fontsize=14,
            ha="right", va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(stations["Ilorin"][0] - 0.25, stations["Ilorin"][1] + 0.1, "Ilorin", fontsize=14,
            ha="right", va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(stations["Minna"][0] - 0.25, stations["Minna"][1] + 0.1, "Minna", fontsize=14,
            ha="right", va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(stations["Kaduna"][0] - 0.3, stations["Kaduna"][1] + 0.25, "Kaduna", fontsize=14,
            ha="right", va="bottom", color=INK, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(stations["Makurdi"][0] + 0.25, stations["Makurdi"][1] + 0.15, "Makurdi", fontsize=14,
            ha="left", va="center", color=INK, bbox=dict(fc="white", ec="none", pad=1))

    # Labels for Western & Eastern lines directly on the map
    ax.text(4.2, 9.6, "Western Railway Line", fontsize=14, color=DEEP["blue"], fontweight="bold",
            rotation=56, ha="center", va="center", bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.2", lw=1))
    
    ax.text(8.9, 7.8, "Eastern Railway Line", fontsize=14, color=DEEP["green"], fontweight="bold",
            rotation=58, ha="center", va="center", bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.2", lw=1))

    # Title & Legend / Notes
    ax.set_title("Colonial Nigerian Railway Network", fontsize=18, fontweight="bold", pad=15, color=INK)
    ax.text(8.5, 3.8, "Sketch map: routes & zones are approximate", fontsize=14, fontstyle="italic", color=INK, ha="center")

    # Set map limits
    ax.set_xlim(2.2, 14.8)
    ax.set_ylim(3.5, 14.2)

    save(fig, out)
