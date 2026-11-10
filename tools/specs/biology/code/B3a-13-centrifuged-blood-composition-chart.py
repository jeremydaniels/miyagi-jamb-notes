from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Test tube geometry
    tube_left = 1.0
    tube_width = 1.4
    tube_right = tube_left + tube_width
    r = tube_width / 2.0
    cx = tube_left + r

    # Heights
    y_lip = 7.2
    y_straight_bottom = 2.0
    y_meniscus = 6.6
    y_buffy_top = 3.9
    y_buffy_bot = 3.75

    # Colors
    c_plasma = '#FFF2A8'       # pale yellow
    c_buffy = '#FFFFFF'        # whitish
    c_rbc = '#A61C1C'          # dark red
    tube_border = INK

    # Draw Red Blood Cells (bottom layer)
    # Start top-left, go top-right, down right, arc bottom, up left
    pts_rbc = [(tube_left, y_buffy_bot), (tube_right, y_buffy_bot), (tube_right, y_straight_bottom)]
    theta = np.linspace(0, -np.pi, 50)
    for a in theta:
        pts_rbc.append((cx + r * np.cos(a), y_straight_bottom + r * np.sin(a)))
    pts_rbc.append((tube_left, y_straight_bottom))
    
    poly_rbc = plt.Polygon(pts_rbc, facecolor=c_rbc, edgecolor='none')
    ax.add_patch(poly_rbc)

    # Draw Buffy Coat (thin middle band)
    rect_buffy = Rectangle((tube_left, y_buffy_bot), tube_width, y_buffy_top - y_buffy_bot,
                           facecolor=c_buffy, edgecolor=GREY, linewidth=0.5)
    ax.add_patch(rect_buffy)

    # Draw Plasma (upper layer)
    rect_plasma = Rectangle((tube_left, y_buffy_top), tube_width, y_meniscus - y_buffy_top,
                            facecolor=c_plasma, edgecolor='none')
    ax.add_patch(rect_plasma)

    # Draw Test Tube Outline (glass)
    tube_pts = [(tube_left - 0.1, y_lip), (tube_right + 0.1, y_lip),
                (tube_right + 0.1, y_lip - 0.2), (tube_right, y_lip - 0.2),
                (tube_right, y_straight_bottom)]
    for a in np.linspace(0, -np.pi, 50):
        tube_pts.append((cx + r * np.cos(a), y_straight_bottom + r * np.sin(a)))
    tube_pts.extend([(tube_left, y_straight_bottom), (tube_left, y_lip - 0.2),
                     (tube_left - 0.1, y_lip - 0.2)])
    poly_tube = plt.Polygon(tube_pts, facecolor='none', edgecolor=tube_border, linewidth=2.5, closed=True)
    ax.add_patch(poly_tube)

    # Meniscus line
    ax.plot([tube_left, tube_right], [y_meniscus, y_meniscus], color=DEEP['blue'], lw=1.5, alpha=0.6)

    # Labels and pointer lines to the layers
    text_x = tube_right + 1.2
    
    # Plasma label
    ax.annotate("plasma (about 55%)",
                xy=(tube_right, (y_meniscus + y_buffy_top) / 2),
                xytext=(text_x, 5.5),
                fontsize=15, fontweight='bold', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8),
                va='center', ha='left', bbox=dict(fc="white", ec="none", pad=2))

    # Buffy coat label
    ax.annotate("white blood cells and\nplatelets (buffy coat)",
                xy=(tube_right, (y_buffy_top + y_buffy_bot) / 2),
                xytext=(text_x, 3.82),
                fontsize=15, fontweight='bold', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8),
                va='center', ha='left', bbox=dict(fc="white", ec="none", pad=2))

    # RBC label
    ax.annotate("red blood cells (about 45%)",
                xy=(tube_right, 2.5),
                xytext=(text_x, 2.3),
                fontsize=15, fontweight='bold', color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8),
                va='center', ha='left', bbox=dict(fc="white", ec="none", pad=2))

    # Pie Chart on the right side
    pie_cx, pie_cy, pie_r = 9.8, 3.82, 1.4

    # Plasma slice (55% -> 198 deg, starting from 90 deg counter-clockwise)
    w_plasma = Wedge((pie_cx, pie_cy), pie_r, 90, 90 + 198, facecolor=c_plasma, edgecolor=INK, lw=1.8)
    # RBC + Buffy slice (~45%)
    w_cells = Wedge((pie_cx, pie_cy), pie_r, 90 + 198, 90 + 360, facecolor=c_rbc, edgecolor=INK, lw=1.8)
    ax.add_patch(w_plasma)
    ax.add_patch(w_cells)

    # Pie chart labels inside/beside slices
    ax.text(pie_cx - 0.6, pie_cy + 0.4, "55%\nplasma", fontsize=14, color=INK,
            ha='center', va='center', fontweight='bold')
    ax.text(pie_cx + 0.6, pie_cy - 0.4, "45%\ncells", fontsize=14, color='white',
            ha='center', va='center', fontweight='bold')

    # Bracket showing connection
    bracket_x = 7.7
    ax.plot([bracket_x, bracket_x + 0.3], [5.5, 5.5], color=GREY, lw=2)
    ax.plot([bracket_x, bracket_x + 0.3], [2.3, 2.3], color=GREY, lw=2)
    ax.plot([bracket_x + 0.3, bracket_x + 0.3], [2.3, 5.5], color=GREY, lw=2)
    ax.annotate("", xy=(pie_cx - pie_r - 0.1, pie_cy), xytext=(bracket_x + 0.3, pie_cy),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2))

    # Title
    ax.text(6.0, 7.5, "Composition of Centrifuged Whole Blood", fontsize=18, fontweight='bold',
            color=INK, ha='center', va='center')

    save(fig, out)
