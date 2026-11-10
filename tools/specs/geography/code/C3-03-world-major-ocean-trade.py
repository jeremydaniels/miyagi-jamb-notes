from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyArrowPatch
import matplotlib.patches as mpatches

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_axes([0.05, 0.08, 0.9, 0.82])
    
    # Configure axes for world map (approx -140 to 155 lon, -55 to 75 lat)
    ax.set_xlim(-140, 155)
    ax.set_ylim(-55, 75)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw world continents
    continents = continent_polys('World')
    for poly in continents:
        patch = Polygon(poly, facecolor='#EAEFF2', edgecolor=GREY, linewidth=1.2, zorder=1)
        ax.add_patch(patch)
        
    def plot_route(points, color, lw=3.0, ls='-', zorder=3):
        pts = np.array(points)
        ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, ls=ls, zorder=zorder)

    # 1. North Atlantic Route (NE USA to Western Europe) - Bold line
    pts_na = [
        (-74, 41), (-65, 43), (-55, 45), (-45, 47), 
        (-30, 50), (-15, 51), (-5, 50.5), (0, 50)
    ]
    plot_route(pts_na, DEEP["blue"], lw=4.5)
    ax.text(-35, 54, "North Atlantic Route", fontsize=14, fontweight="bold",
            color=INK, ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=GREY, alpha=0.9))

    # 2. Suez Canal Route
    # Carefully plotted to stay in the Mediterranean and Red Sea
    pts_suez = [
        (-9.0, 39.0),   # Off Portugal
        (-6.0, 35.8),   # Strait of Gibraltar
        (-2.0, 36.0),   # Alboran Sea
        (4.0, 37.5),    # North of Algeria
        (10.0, 38.0),   # North of Tunisia
        (15.0, 36.0),   # Ionian Sea
        (20.0, 34.5),   # South of Greece
        (25.0, 33.5),   # South of Crete
        (30.0, 32.5),   # Approaching Egypt
        (32.4, 31.5),   # Port Said
        (32.5, 29.5),   # Gulf of Suez
        (34.0, 27.5),   # Northern Red Sea
        (37.0, 22.0),   # Central Red Sea
        (40.0, 18.0),   # Southern Red Sea
        (43.0, 13.0),   # Bab-el-Mandeb
        (45.0, 12.0),   # Gulf of Aden
        (50.0, 13.0),   # Arabian Sea
        (60.0, 13.0),   # Indian Ocean
        (72.0, 8.0),    # South of India
        (88.0, 5.0),    # Bay of Bengal
        (98.0, 4.0),    # Malacca entrance
        (104.0, 1.5)    # Singapore
    ]
    plot_route(pts_suez, DEEP["orange"], lw=3.5)
    ax.text(62, 16, "Suez Canal Route", fontsize=14, fontweight="bold",
            color=INK, ha='left', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=GREY, alpha=0.9))

    # 3. Cape Route
    pts_cape = [
        (-12.0, 48.0),  # Atlantic off Western Europe
        (-15.0, 35.0),  # West of Gibraltar
        (-20.0, 22.0),  # West of Western Sahara
        (-22.0, 12.0),  # West of Cap-Vert
        (-18.0, 0.0),   # Equatorial Atlantic
        (-5.0, -15.0),  # South Atlantic
        (10.0, -32.0),  # Approaching South Africa
        (18.5, -36.5),  # South of Cape of Good Hope
        (30.0, -36.0),  # Rounding into Indian Ocean
        (48.0, -25.0),  # South Indian Ocean
        (68.0, -10.0),  # Mid Indian Ocean
        (90.0, 0.0),    # East Indian Ocean
        (100.0, 1.0)    # Approaching SE Asia
    ]
    plot_route(pts_cape, DEEP["green"], lw=3.5)
    ax.text(22, -43, "Cape Route", fontsize=14, fontweight="bold",
            color=INK, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=GREY, alpha=0.9))

    # 4. Trans-Pacific Route (Across the Pacific Ocean)
    pts_tp_asia = [(122, 31), (130, 33), (140, 36), (150, 39.5), (155, 41)]
    pts_tp_usa = [(-140, 42), (-135, 41), (-130, 39.5), (-123, 38)]
    plot_route(pts_tp_asia, DEEP["pink"], lw=3.5)
    plot_route(pts_tp_usa, DEEP["pink"], lw=3.5)
    ax.text(140, 46, "Trans-Pacific Route", fontsize=14, fontweight="bold",
            color=INK, ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=GREY, alpha=0.9))
    ax.text(-130, 46, "Trans-Pacific Route", fontsize=14, fontweight="bold",
            color=INK, ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=GREY, alpha=0.9))

    # Commodity Icons & Arrows
    # (a) Cocoa pod in West Africa (~lon -2, lat 7)
    def draw_cocoa(x, y):
        circle = mpatches.Ellipse((x, y), 5.5, 8.5, angle=-25, facecolor='#A0522D', edgecolor=INK, lw=1.5, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y - 7, "Cocoa", fontsize=14, fontweight="bold", color=INK, ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85))

    draw_cocoa(-2, 7)
    arrow_cocoa = FancyArrowPatch((-4, 11), (-8, 40),
                                  connectionstyle="arc3,rad=-0.15",
                                  arrowstyle='-|>', mutation_scale=16,
                                  color=DEEP["lav"], lw=2.5, zorder=4)
    ax.add_patch(arrow_cocoa)

    # (b) Oil barrel in Middle East (~lon 48, lat 25)
    def draw_oil_barrel(x, y):
        rect = Rectangle((x - 2.5, y - 3.5), 5, 7, facecolor='#333333', edgecolor=INK, lw=1.5, zorder=5)
        ax.add_patch(rect)
        top = mpatches.Ellipse((x, y + 3.5), 5, 1.8, facecolor='#555555', edgecolor=INK, lw=1.2, zorder=6)
        ax.add_patch(top)
        ax.text(x, y - 6, "Oil", fontsize=14, fontweight="bold", color=INK, ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85))

    draw_oil_barrel(48, 25)
    arrow_oil = FancyArrowPatch((44, 27), (12, 38),
                                connectionstyle="arc3,rad=0.18",
                                arrowstyle='-|>', mutation_scale=16,
                                color=DEEP["lav"], lw=2.5, zorder=4)
    ax.add_patch(arrow_oil)

    # (c) Car icon in Japan / China (~lon 116, lat 33)
    def draw_car(x, y):
        body = Rectangle((x - 4, y - 1.5), 8, 3, facecolor='#E74C3C', edgecolor=INK, lw=1.2, zorder=5)
        top = Rectangle((x - 2, y + 1.5), 4, 2, facecolor='#E74C3C', edgecolor=INK, lw=1.2, zorder=5)
        w1 = Circle((x - 2.2, y - 1.8), 1.1, facecolor='#222', edgecolor=INK, lw=1, zorder=6)
        w2 = Circle((x + 2.2, y - 1.8), 1.1, facecolor='#222', edgecolor=INK, lw=1, zorder=6)
        ax.add_patch(body)
        ax.add_patch(top)
        ax.add_patch(w1)
        ax.add_patch(w2)
        ax.text(x, y - 5, "Cars", fontsize=14, fontweight="bold", color=INK, ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85))

    draw_car(116, 33)
    arrow_car = FancyArrowPatch((122, 35), (145, 38),
                                connectionstyle="arc3,rad=-0.1",
                                arrowstyle='-|>', mutation_scale=16,
                                color=DEEP["lav"], lw=2.5, zorder=4)
    ax.add_patch(arrow_car)

    # Title & Caption
    fig.suptitle("Major Ocean Trade Routes and Commodity Flows", fontsize=18, fontweight="bold", color=INK, y=0.96)
    ax.text(0.5, -0.02, "Sketch map: zones are approximate",
            transform=ax.transAxes, fontsize=14, color=GREY, ha='center', va='top', style='italic')

    save(fig, out)
