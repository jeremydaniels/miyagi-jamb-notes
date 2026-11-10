from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    
    # Bounding box for Southern Africa tip: Lon 16 to 30.5, Lat -36.0 to -28.2
    ax.set_xlim(16.2, 30.8)
    ax.set_ylim(-36.2, -28.2)
    ax.axis("off")
    
    # Coastline of Southern Africa (schematic smooth coordinates)
    coast_lons = [16.5, 17.5, 18.0, 18.3, 18.4, 18.9, 20.0, 22.0, 24.0, 25.6, 26.5, 27.2, 28.5, 30.0, 30.8, 30.8, 16.5]
    coast_lats = [-28.5, -31.0, -32.5, -33.5, -34.3, -34.8, -34.8, -34.2, -34.0, -33.8, -33.6, -33.3, -32.0, -30.0, -28.5, -28.2, -28.2]
    land_poly = patches.Polygon(np.column_stack([coast_lons, coast_lats]), closed=True, 
                                facecolor="#F7F9FA", edgecolor=DEEP["blue"], lw=2.0, zorder=1)
    ax.add_patch(land_poly)

    # Cape Colony territory (South-West)
    cape_x = [17.5, 18.0, 18.3, 18.4, 18.9, 20.0, 23.5, 23.5, 20.0, 17.5]
    cape_y = [-31.0, -32.5, -33.5, -34.3, -34.8, -34.8, -34.0, -31.2, -31.0, -31.0]
    cape_poly = patches.Polygon(np.column_stack([cape_x, cape_y]), closed=True,
                                facecolor=ORANGE, alpha=0.35, edgecolor=DEEP["orange"], lw=2, linestyle="--", zorder=2)
    ax.add_patch(cape_poly)

    # Xhosa territory (South-East)
    xhosa_x = [27.2, 28.5, 30.0, 30.8, 30.8, 28.5, 27.2]
    xhosa_y = [-33.3, -32.0, -30.0, -28.5, -30.5, -31.5, -32.8]
    xhosa_poly = patches.Polygon(np.column_stack([xhosa_x, xhosa_y]), closed=True,
                                 facecolor=GREEN, alpha=0.35, edgecolor=DEEP["green"], lw=2, linestyle="--", zorder=2)
    ax.add_patch(xhosa_poly)

    # Great Fish River path (flowing south-east to coast around lon 27.1, lat -33.5)
    fish_river_x = [25.5, 25.8, 26.3, 26.8, 27.1]
    fish_river_y = [-31.5, -32.1, -32.7, -33.1, -33.5]
    ax.plot(fish_river_x, fish_river_y, color=DEEP["blue"], lw=3.0, zorder=4)

    # The Zuurveld region (between Sundays River ~25.6 and Great Fish River ~27.1 along coast)
    zuurveld_x = [25.6, 26.2, 27.1, 26.6, 25.6]
    zuurveld_y = [-33.8, -33.2, -33.5, -33.8, -33.8]
    zuurveld_poly = patches.Polygon(np.column_stack([zuurveld_x, zuurveld_y]), closed=True,
                                    facecolor=PINK, alpha=0.6, edgecolor=DEEP["pink"], hatch="//", lw=1.5, zorder=3)
    ax.add_patch(zuurveld_poly)

    # Ocean labels placed safely offshore away from river mouths
    ax.text(17.2, -35.2, "Atlantic\nOcean", fontsize=15, color=GREY, fontstyle="italic", ha="center")
    # Indian ocean shifted south-east off the Transkei / Natal coast, well away from Fish River (27.1, -33.5)
    ax.text(29.8, -33.8, "Indian Ocean", fontsize=15, color=GREY, fontstyle="italic", ha="center")

    # Settlement points
    ax.plot(18.42, -33.92, marker="o", color=INK, markersize=6, zorder=5)
    ax.text(18.55, -33.65, "Cape Town\n(est. 1652)", fontsize=14, color=INK, ha="left", va="bottom",
            bbox=dict(fc="white", ec="none", pad=1))

    # Territory labels
    ax.text(20.5, -32.3, "CAPE COLONY\n(Dutch / British)", fontsize=16, weight="bold", color=DEEP["orange"], ha="center",
            bbox=dict(fc="white", ec="none", pad=1, alpha=0.7), zorder=4)
    ax.text(29.2, -31.2, "XHOSA\nTERRITORY", fontsize=16, weight="bold", color=DEEP["green"], ha="center",
            bbox=dict(fc="white", ec="none", pad=1, alpha=0.8), zorder=4)

    # Trekboer Expansion Arrow (pointing eastwards)
    ax.annotate(
        "Trekboer Expansion",
        xy=(24.8, -33.3), xytext=(20.2, -33.7),
        fontsize=15, weight="bold", color=DEEP["orange"],
        arrowprops=dict(facecolor=DEEP["orange"], edgecolor=DEEP["orange"], width=3.5, headwidth=11, headlength=12),
        ha="center", va="center",
        bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.3", lw=1.2),
        zorder=5
    )

    # Xhosa Expansion Arrow (pointing westwards)
    ax.annotate(
        "Xhosa Expansion",
        xy=(27.5, -33.0), xytext=(29.8, -32.6),
        fontsize=15, weight="bold", color=DEEP["green"],
        arrowprops=dict(facecolor=DEEP["green"], edgecolor=DEEP["green"], width=3.5, headwidth=11, headlength=12),
        ha="center", va="center",
        bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.3", lw=1.2),
        zorder=5
    )

    # Great Fish River label (annotating the river inland)
    ax.annotate(
        "Great Fish River",
        xy=(26.4, -32.8), xytext=(24.8, -31.2),
        fontsize=14, weight="bold", color=DEEP["blue"],
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.0),
        ha="center", va="bottom",
        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1)
    )

    # The Zuurveld label (positioned directly south of Zuurveld with clear space)
    ax.annotate(
        "The Zuurveld\n(Contested Zone)",
        xy=(26.3, -33.6), xytext=(25.0, -35.2),
        fontsize=14, weight="bold", color=DEEP["pink"],
        arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.0),
        ha="center", va="top",
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.2),
        zorder=6
    )

    # Title and sketch note
    ax.text(23.5, -28.9, "Southern Africa: Eastern Frontier (Late 18th – Early 19th C.)", 
            fontsize=17, weight="bold", color=INK, ha="center")
    ax.text(30.6, -35.8, "Sketch map: zones are approximate", 
            fontsize=14, fontstyle="italic", color=GREY, ha="right", va="bottom")

    save(fig, out)
