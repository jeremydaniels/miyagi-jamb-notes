from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrow

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    
    # Coordinate frame
    ax.set_xlim(3.0, 16.0)
    ax.set_ylim(7.0, 15.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Sokoto Caliphate polygon (West & Central Northern Nigeria)
    sokoto_coords = [
        (3.5, 11.5), (4.2, 13.8), (6.0, 14.0), (8.5, 13.5), (9.8, 12.8),
        (10.2, 11.5), (10.0, 10.0), (11.5, 8.5), (10.5, 8.0), (8.0, 8.2),
        (6.0, 8.6), (4.5, 9.5), (3.8, 10.5)
    ]
    sokoto_poly = Polygon(sokoto_coords, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5, zorder=2)
    ax.add_patch(sokoto_poly)

    # Kanem-Borno polygon (Northeast, surrounding / west and south of Lake Chad)
    # Shaded in soft yellow/cream
    borno_coords = [
        (10.5, 13.5), (12.5, 14.5), (15.5, 14.5), (15.5, 11.5), (14.5, 10.0),
        (13.0, 9.8), (11.0, 10.2), (10.5, 11.5), (10.2, 12.8)
    ]
    borno_poly = Polygon(borno_coords, closed=True, facecolor=CREAM, edgecolor='#B8860B', lw=2.5, zorder=2)
    ax.add_patch(borno_poly)

    # Lake Chad polygon
    lake_chad_coords = [
        (13.7, 12.6), (14.2, 13.8), (15.2, 13.8), (15.3, 12.8),
        (14.8, 12.3), (14.0, 12.3)
    ]
    lake_poly = Polygon(lake_chad_coords, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(lake_poly)

    # Lake Chad label placed clearly inside or distinctly above with safe background
    ax.text(
        14.5, 13.0, "Lake Chad", 
        fontsize=14, color=DEEP["blue"], weight='bold', ha='center', va='center',
        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1),
        zorder=6
    )

    # Red arrow from Sokoto Caliphate eastwards into Borno (Fulani attacks)
    # Using FancyArrow to guarantee a prominent, clear, crisp arrowhead
    arrow = FancyArrow(
        8.8, 11.8, 2.2, 0.0,
        width=0.18, length_includes_head=True,
        head_width=0.6, head_length=0.6,
        facecolor=DEEP["pink"], edgecolor=INK, lw=1.2,
        zorder=5
    )
    ax.add_patch(arrow)

    # Label for Fulani attacks - positioned clearly above arrow, outside collision
    ax.text(
        9.9, 12.3, "Fulani attacks", 
        fontsize=15, color=DEEP["pink"], weight='bold', ha='center', va='bottom',
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.2),
        zorder=6
    )

    # Star markers for Ngazargamu and Kukawa
    ngazargamu_pt = (12.2, 12.8)
    kukawa_pt = (13.5, 11.8)

    # Ngazargamu star and connected/adjacent clear label
    ax.scatter(*ngazargamu_pt, marker='*', s=350, color=DEEP["orange"], edgecolor=INK, lw=1.2, zorder=7)
    ax.text(
        ngazargamu_pt[0], ngazargamu_pt[1] + 0.45, "Ngazargamu",
        fontsize=14, color=INK, ha='center', va='bottom', weight='bold',
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"),
        zorder=8
    )

    # Kukawa star and clear label
    ax.scatter(*kukawa_pt, marker='*', s=350, color=DEEP["orange"], edgecolor=INK, lw=1.2, zorder=7)
    ax.text(
        kukawa_pt[0] + 0.25, kukawa_pt[1] - 0.45, "Kukawa",
        fontsize=14, color=INK, ha='left', va='top', weight='bold',
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"),
        zorder=8
    )

    # Main Area Labels
    ax.text(
        6.8, 11.0, "Sokoto Caliphate", 
        fontsize=18, color=INK, weight='bold', ha='center', va='center',
        bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.4", lw=1.5),
        zorder=6
    )

    ax.text(
        12.6, 10.6, "Kanem-Borno", 
        fontsize=18, color=INK, weight='bold', ha='center', va='center',
        bbox=dict(fc="white", ec='#B8860B', boxstyle="round,pad=0.4", lw=1.5),
        zorder=6
    )

    # Schematic note placed at the bottom completely clear of map polygons
    ax.text(
        3.2, 7.2, "Sketch map: zones are approximate", 
        fontsize=14, color=GREY, style='italic', ha='left', va='bottom',
        bbox=dict(fc="white", ec="none", pad=0.2),
        zorder=6
    )

    save(fig, out)
