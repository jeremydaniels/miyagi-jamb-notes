from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')

    # Regional boundaries roughly: lon 18 to 55, lat 8 to 42
    ax.set_xlim(18, 52)
    ax.set_ylim(10, 42)

    # Base land masses using country_polys or continent_polys if available
    # style.py provides country_polys(*names) and continent_polys(...)
    try:
        # Load surrounding / regional countries
        land_polys = country_polys(
            "Egypt", "Sudan", "South Sudan", "Saudi Arabia", "Yemen", "Oman",
            "Syria", "Jordan", "Israel", "Lebanon", "Iraq", "Turkey", "Libya",
            "Chad", "Cyprus", "Greece", "Iran"
        )
        for poly in land_polys:
            ax.add_patch(plt.Polygon(poly, facecolor=CREAM, edgecolor=GREY, lw=0.8, zorder=1))
        
        # Egypt highlighted specifically
        egypt_poly = country_polys("Egypt")
        for poly in egypt_poly:
            ax.add_patch(plt.Polygon(poly, facecolor=DEEP["green"], edgecolor=INK, lw=1.5, zorder=2))
    except Exception:
        # Fallback simplified outlines if polygon data name differs
        pass

    # Military expansion arrows from Egypt under Muhammad Ali
    # 1. South into Sudan (1820-1824)
    ax.annotate(
        "", xy=(31.5, 16.5), xytext=(31.0, 24.5),
        arrowprops=dict(arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["orange"], lw=3.5),
        zorder=5
    )

    # 2. East across Red Sea into Arabia / Hejaz (1811-1818)
    ax.annotate(
        "", xy=(39.5, 23.0), xytext=(32.5, 26.0),
        arrowprops=dict(
            arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["orange"], lw=3.5,
            connectionstyle="arc3,rad=-0.15"
        ),
        zorder=5
    )

    # 3. Northeast into Syria / Levant (1831-1833)
    ax.annotate(
        "", xy=(36.5, 34.5), xytext=(32.5, 30.5),
        arrowprops=dict(
            arrowstyle="->,head_width=0.6,head_length=0.8", color=DEEP["orange"], lw=3.5,
            connectionstyle="arc3,rad=0.1"
        ),
        zorder=5
    )

    # Labels with clear white bounding boxes
    bbox_style = dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85)
    bbox_egypt = dict(boxstyle="round,pad=0.3", fc=DEEP["green"], ec="none")

    # Sea labels (blue text or ink text)
    ax.text(26.5, 33.5, "Mediterranean Sea", fontsize=15, fontstyle="italic", color=DEEP["blue"], ha="center", bbox=bbox_style, zorder=6)
    ax.text(37.5, 20.0, "Red Sea", fontsize=14, fontstyle="italic", color=DEEP["blue"], ha="center", rotation=-48, bbox=bbox_style, zorder=6)

    # Region / Country labels
    ax.text(29.8, 26.8, "Egypt", fontsize=16, fontweight="bold", color="white", ha="center", bbox=bbox_egypt, zorder=6)
    ax.text(30.0, 15.0, "Sudan", fontsize=16, fontweight="bold", color=INK, ha="center", bbox=bbox_style, zorder=6)
    ax.text(42.5, 23.5, "Arabia", fontsize=16, fontweight="bold", color=INK, ha="center", bbox=bbox_style, zorder=6)
    ax.text(38.0, 35.0, "Syria", fontsize=15, fontweight="bold", color=INK, ha="center", bbox=bbox_style, zorder=6)
    ax.text(35.0, 39.0, "Ottoman Empire", fontsize=16, fontweight="bold", color=INK, ha="center", bbox=bbox_style, zorder=6)

    # Title & Caption
    ax.text(
        0.5, 0.96, "Egyptian Expansion in the Early 19th Century",
        transform=ax.transAxes, fontsize=17, fontweight="bold", color=INK, ha="center"
    )
    ax.text(
        0.5, 0.03, "Sketch map: zones are approximate",
        transform=ax.transAxes, fontsize=14, fontstyle="italic", color=GREY, ha="center"
    )

    save(fig, out)
