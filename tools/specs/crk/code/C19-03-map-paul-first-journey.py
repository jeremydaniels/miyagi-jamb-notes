from style import *
import numpy as np

def draw(out):
    fig = canvas(12, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Coordinate bounds (Eastern Mediterranean)
    ax.set_xlim(29.5, 37.5)
    ax.set_ylim(33.8, 39.5)

    # Sea background
    ax.fill([29.0, 38.0, 38.0, 29.0], [33.5, 33.5, 40.0, 40.0], color="#EBF4F6", zorder=0)

    # Southern Anatolia / Asia Minor Landmass
    anatolia_x = [29.0, 30.5, 30.6, 31.5, 32.5, 34.0, 35.5, 36.0, 38.0, 38.0, 29.0]
    anatolia_y = [36.8, 36.8, 36.2, 36.8, 36.0, 36.2, 36.7, 36.0, 36.0, 40.0, 40.0]
    ax.fill(anatolia_x, anatolia_y, color=CREAM, ec=GREY, lw=1.2, zorder=1)

    # Levant / Syria Landmass
    levant_x = [35.5, 35.8, 35.7, 35.9, 38.0, 38.0]
    levant_y = [36.7, 36.0, 33.5, 33.5, 33.5, 36.7]
    ax.fill(levant_x, levant_y, color=CREAM, ec=GREY, lw=1.2, zorder=1)

    # Cyprus Island
    cyprus_x = [32.3, 32.8, 33.9, 34.6, 33.9, 33.0, 32.2]
    cyprus_y = [35.1, 35.2, 35.4, 35.7, 34.9, 34.6, 34.8]
    ax.fill(cyprus_x, cyprus_y, color=CREAM, ec=GREY, lw=1.2, zorder=1)

    # Regional labels placed away from route lines and legend
    ax.text(33.5, 34.2, "MEDITERRANEAN SEA", fontsize=15, color=DEEP["blue"],
            fontstyle='italic', alpha=0.7, ha="center", zorder=2)
    ax.text(33.5, 34.95, "CYPRUS", fontsize=14, color=INK, fontweight='bold', ha="center",
            bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.7), zorder=2)
    ax.text(34.8, 38.6, "ASIA MINOR (ANATOLIA)", fontsize=14, color=GREY, ha="center", zorder=2)
    ax.text(37.0, 35.0, "SYRIA", fontsize=14, color=GREY, ha="center", zorder=2)

    # Locations (Lon, Lat)
    cities = {
        "Antioch (Syria)": (36.16, 36.20),
        "Salamis": (33.90, 35.17),
        "Paphos": (32.41, 34.76),
        "Perga": (30.85, 36.96),
        "Antioch in Pisidia": (31.18, 38.30),
        "Iconium": (32.49, 37.87),
        "Lystra": (32.22, 37.56),
        "Derbe": (33.05, 37.35)
    }

    # Plot city markers
    for name, (x, y) in cities.items():
        ax.plot(x, y, 'o', color=INK, ms=5, zorder=5)

    # Offsets for city labels to avoid overlap
    label_offsets = {
        "Antioch (Syria)": (0.2, 0.15, "left"),
        "Salamis": (0.2, 0.15, "left"),
        "Paphos": (-0.18, -0.22, "right"),
        "Perga": (-0.18, 0.15, "right"),
        "Antioch in Pisidia": (-0.15, 0.22, "right"),
        "Iconium": (0.2, 0.18, "left"),
        "Lystra": (-0.2, -0.2, "right"),
        "Derbe": (0.2, -0.18, "left")
    }

    for name, (dx, dy, align) in label_offsets.items():
        x, y = cities[name]
        ax.text(x + dx, y + dy, name, fontsize=14, color=INK, ha=align, va="center",
                bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85), zorder=6)

    # Route arrows helper
    arrow_col = "#D62728"  # distinct red for visibility

    def draw_route(p1, p2, rad=0.0, ls='-'):
        ax.annotate('', xy=p2, xytext=p1,
                    arrowprops=dict(arrowstyle="->,head_length=0.6,head_width=0.35",
                                    color=arrow_col, lw=2.2, linestyle=ls,
                                    shrinkA=4, shrinkB=4,
                                    connectionstyle=f"arc3,rad={rad}"),
                    zorder=4)

    # Outbound Journey (explicitly linking via Perga):
    draw_route(cities["Antioch (Syria)"], cities["Salamis"], rad=-0.08)
    draw_route(cities["Salamis"], cities["Paphos"], rad=0.08)
    draw_route(cities["Paphos"], cities["Perga"], rad=-0.08)
    draw_route(cities["Perga"], cities["Antioch in Pisidia"], rad=-0.05)
    draw_route(cities["Antioch in Pisidia"], cities["Iconium"], rad=-0.05)
    draw_route(cities["Iconium"], cities["Lystra"], rad=0.05)
    draw_route(cities["Lystra"], cities["Derbe"], rad=-0.05)

    # Return Journey:
    draw_route(cities["Derbe"], cities["Lystra"], rad=0.15, ls='--')
    draw_route(cities["Lystra"], cities["Iconium"], rad=-0.15, ls='--')
    draw_route(cities["Iconium"], cities["Antioch in Pisidia"], rad=0.15, ls='--')
    draw_route(cities["Antioch in Pisidia"], cities["Perga"], rad=0.1, ls='--')

    # Sailing straight back from the coast (Perga) via Mediterranean sea to Antioch (Syria)
    sea_midpoint = (33.5, 35.85)
    ax.annotate('', xy=sea_midpoint, xytext=cities["Perga"],
                arrowprops=dict(arrowstyle="-",
                                color=arrow_col, lw=2.2, linestyle='--',
                                shrinkA=4, shrinkB=0,
                                connectionstyle="arc3,rad=-0.1"),
                zorder=4)
    ax.annotate('', xy=cities["Antioch (Syria)"], xytext=sea_midpoint,
                arrowprops=dict(arrowstyle="->,head_length=0.6,head_width=0.35",
                                color=arrow_col, lw=2.2, linestyle='--',
                                shrinkA=0, shrinkB=4,
                                connectionstyle="arc3,rad=-0.05"),
                zorder=4)

    # Legend / Key (moved to top-left to avoid bottom-left overlaps)
    ax.plot([], [], color=arrow_col, lw=2.2, label="Outbound journey")
    ax.plot([], [], color=arrow_col, lw=2.2, ls='--', label="Return journey")
    ax.legend(loc="upper left", frameon=True, fontsize=14, edgecolor=GREY, facecolor="white")

    # Titles & notes
    ax.text(33.5, 39.15, "Paul's First Missionary Journey", fontsize=18, fontweight='bold',
            color=INK, ha='center', bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.4"))
    ax.text(37.3, 34.0, "Sketch map: zones are approximate", fontsize=14,
            fontstyle='italic', color=GREY, ha='right')

    save(fig, out)
