from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_xlim(-22, 55)
    ax.set_ylim(-38, 40)

    # 1914 colonial color mapping
    COL_BRITISH = PINK
    COL_FRENCH = BLUE
    COL_PORTUGUESE = GREEN
    COL_BELGIAN = CREAM
    COL_GERMAN = GREY
    COL_SPANISH = ORANGE
    COL_ITALIAN = LAV
    COL_INDEP = "#FFFFFF"

    # Variations in Natural Earth / shapefile naming
    british_names = [
        "Egypt", "Sudan", "S. Sudan", "South Sudan", "Uganda", "Kenya",
        "South Africa", "Lesotho", "Eswatini", "Swaziland", "Botswana",
        "Zimbabwe", "Zambia", "Malawi", "Nigeria", "Ghana", "Gold Coast",
        "Sierra Leone", "Gambia", "Somaliland", "N. Cyprus"
    ]

    french_names = [
        "Algeria", "Tunisia", "Morocco", "Mauritania", "Senegal",
        "Mali", "Guinea", "Côte d'Ivoire", "Ivory Coast", "Burkina Faso",
        "Niger", "Benin", "Chad", "Central African Rep.", "Central African Republic",
        "Congo", "Rep. Congo", "Republic of the Congo", "Gabon",
        "Madagascar", "Djibouti"
    ]

    portuguese_names = [
        "Angola", "Mozambique", "Guinea-Bissau"
    ]

    belgian_names = [
        "Dem. Rep. Congo", "Democratic Republic of the Congo", "DR Congo",
        "Zaire", "Congo, Dem. Rep.", "Rwanda", "Burundi"
    ]

    german_names = [
        "Togo", "Cameroon", "Tanzania", "United Republic of Tanzania",
        "Namibia"
    ]

    spanish_names = [
        "W. Sahara", "Western Sahara", "Eq. Guinea", "Equatorial Guinea"
    ]

    italian_names = [
        "Libya", "Eritrea", "Somalia"
    ]

    independent_names = [
        "Ethiopia", "Liberia"
    ]

    def plot_group(names, facecolor, edgecolor=INK, lw=0.8):
        polys = country_polys(*names)
        for poly in polys:
            ax.add_patch(plt.Polygon(poly, facecolor=facecolor, edgecolor=edgecolor, lw=lw, zorder=2))

    # Base background: continent outline
    try:
        cont_polys = continent_polys('Africa')
        for poly in cont_polys:
            ax.add_patch(plt.Polygon(poly, facecolor=COL_INDEP, edgecolor=INK, lw=1, zorder=1))
    except Exception:
        pass

    # Plot colonial territories
    plot_group(french_names, COL_FRENCH)
    plot_group(british_names, COL_BRITISH)
    plot_group(german_names, COL_GERMAN)
    plot_group(belgian_names, COL_BELGIAN)
    plot_group(portuguese_names, COL_PORTUGUESE)
    plot_group(italian_names, COL_ITALIAN)
    plot_group(spanish_names, COL_SPANISH)
    plot_group(independent_names, COL_INDEP)

    # Title
    ax.text(16, 37.5, "Africa in 1914", fontsize=18, fontweight="bold",
            ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="none"))

    # Caption
    ax.text(16, -36, "Sketch map: zones are approximate",
            fontsize=14, fontstyle="italic", ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none"))

    # Explicit, rock-solid legend drawn manually to guarantee perfect text/swatch alignment
    items = [
        ("British", COL_BRITISH),
        ("French", COL_FRENCH),
        ("Portuguese", COL_PORTUGUESE),
        ("Belgian", COL_BELGIAN),
        ("German", COL_GERMAN),
        ("Spanish", COL_SPANISH),
        ("Italian", COL_ITALIAN),
        ("Independent", COL_INDEP)
    ]

    # Legend box background
    box_x, box_y, box_w, box_h = -21, -34.5, 22.5, 27.5
    leg_box = Rectangle((box_x, box_y), box_w, box_h,
                        facecolor="white", edgecolor=GREY, lw=1.2, zorder=10)
    ax.add_patch(leg_box)

    # Legend Header
    ax.text(box_x + 1.5, box_y + box_h - 2.5, "Colonial Power",
            fontsize=15, fontweight="bold", color=INK, va="center", zorder=11)

    # Legend Items
    start_y = box_y + box_h - 6.0
    spacing = 2.8
    for i, (label, col) in enumerate(items):
        cur_y = start_y - i * spacing
        swatch = Rectangle((box_x + 1.5, cur_y - 1.0), 3.2, 2.0,
                           facecolor=col, edgecolor=INK, lw=1.0, zorder=11)
        ax.add_patch(swatch)
        ax.text(box_x + 6.0, cur_y, label,
                fontsize=14, color=INK, va="center", ha="left", zorder=11)

    save(fig, out)
