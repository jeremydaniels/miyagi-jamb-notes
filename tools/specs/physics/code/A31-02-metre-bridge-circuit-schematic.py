from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas size: wide layout with plenty of vertical breathing room
    fig = canvas(13, 9.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-1.5, 8.8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Wooden board background
    board = patches.Rectangle((0.5, 1.6), 11.0, 5.2, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
    ax.add_patch(board)
    ax.text(0.7, 6.5, "Wooden baseboard", fontsize=14, color=GREY, style='italic', zorder=2)

    # Brass strips (copper / brass warm tone)
    strip_color = '#E6C280'
    strip_edge = '#9C6644'

    # Left L-strip: vertical part x in [1.0, 1.8], horizontal arm to x=3.0
    left_strip_pts = [
        (1.0, 2.7), (1.8, 2.7), (1.8, 5.6), (3.0, 5.6),
        (3.0, 6.2), (1.0, 6.2)
    ]
    left_strip = patches.Polygon(left_strip_pts, closed=True, facecolor=strip_color, edgecolor=strip_edge, lw=1.5, zorder=2)
    ax.add_patch(left_strip)

    # Central strip: x in [4.5, 7.5], y in [5.6, 6.2]
    mid_strip = patches.Rectangle((4.5, 5.6), 3.0, 0.6, facecolor=strip_color, edgecolor=strip_edge, lw=1.5, zorder=2)
    ax.add_patch(mid_strip)

    # Right L-strip: vertical part x in [10.2, 11.0], horizontal arm to x=9.0
    right_strip_pts = [
        (11.0, 2.7), (10.2, 2.7), (10.2, 5.6), (9.0, 5.6),
        (9.0, 6.2), (11.0, 6.2)
    ]
    right_strip = patches.Polygon(right_strip_pts, closed=True, facecolor=strip_color, edgecolor=strip_edge, lw=1.5, zorder=2)
    ax.add_patch(right_strip)

    # Terminals (binding screws) on brass strips
    terminals = [
        (1.4, 3.0),   # Terminal A
        (2.6, 5.9),   # Left gap terminal 1
        (4.9, 5.9),   # Left gap terminal 2
        (6.0, 5.9),   # Galvanometer terminal on central strip
        (7.1, 5.9),   # Right gap terminal 1
        (9.4, 5.9),   # Right gap terminal 2
        (10.6, 3.0)   # Terminal B
    ]
    for pt in terminals:
        ax.plot(pt[0], pt[1], marker='o', markersize=6, color=INK, zorder=5)

    # Metre Scale (alongside the wire AB)
    scale_y = 2.4
    scale = patches.Rectangle((1.4, scale_y - 0.35), 9.2, 0.35, facecolor='white', edgecolor=GREY, lw=1.0, zorder=2)
    ax.add_patch(scale)
    for val in range(0, 101, 5):
        tx = 1.4 + (val / 100.0) * 9.2
        ty_top = scale_y
        ty_bottom = scale_y - (0.22 if val % 10 == 0 else 0.12)
        ax.plot([tx, tx], [ty_bottom, ty_top], color=INK, lw=0.8, zorder=3)
        if val % 20 == 0:
            ax.text(tx, scale_y - 0.52, str(val), fontsize=14, ha='center', va='top', color=INK, zorder=3)
    ax.text(6.0, scale_y - 0.75, "Metre rule", fontsize=14, ha='center', va='top', color=INK)

    # Wire AB (stretched tightly across terminals A and B)
    xA, yA = 1.4, 3.0
    xB, yB = 10.6, 3.0
    ax.plot([xA, xB], [yA, yB], color=INK, lw=2.5, zorder=4)

    # Labels A and B
    ax.text(xA - 0.25, yA, "A", fontsize=17, fontweight='bold', ha='right', va='center', color=INK)
    ax.text(xB + 0.25, yB, "B", fontsize=17, fontweight='bold', ha='left', va='center', color=INK)

    # Left Gap Resistor R1 (Unknown Resistor)
    # Wires lead strictly up to resistor box placed high in left gap
    y_res = 7.3
    ax.plot([2.6, 2.6, 3.3], [5.9, y_res, y_res], color=INK, lw=1.5, zorder=3)
    r1_box = patches.Rectangle((3.3, y_res - 0.25), 1.0, 0.5, facecolor='white', edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(r1_box)
    ax.plot([4.3, 4.9, 4.9], [y_res, y_res, 5.9], color=INK, lw=1.5, zorder=3)
    ax.text(3.8, y_res + 0.45, "Unknown resistor\n$R_1$", fontsize=15, ha='center', va='bottom', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # Right Gap Resistor R2 (Known Standard Resistor)
    ax.plot([7.1, 7.1, 7.7], [5.9, y_res, y_res], color=INK, lw=1.5, zorder=3)
    r2_box = patches.Rectangle((7.7, y_res - 0.25), 1.0, 0.5, facecolor='white', edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(r2_box)
    ax.plot([8.7, 9.4, 9.4], [y_res, y_res, 5.9], color=INK, lw=1.5, zorder=3)
    ax.text(8.2, y_res + 0.45, "Standard resistor\n$R_2$", fontsize=15, ha='center', va='bottom', color=INK,
            bbox=dict(fc='white', ec='none', pad=2))

    # Central brass strip label with arrow pointing clearly into strip (no wire overlaps)
    ax.annotate("Central brass strip", xy=(6.0, 6.2), xytext=(6.0, 7.5),
                ha='center', va='bottom', fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc='white', ec='none', pad=2), zorder=6)

    # Jockey Position J on wire AB (balance point at 40 cm)
    l1_frac = 0.40
    xJ = xA + l1_frac * (xB - xA)   # 1.4 + 0.40 * 9.2 = 5.08
    yJ = yA

    # Galvanometer G on central strip
    xMid, yMid = 6.0, 5.9
    yGalv = 4.7
    # Wire from terminal to top of galvanometer
    ax.plot([xMid, xMid], [yMid, yGalv + 0.38], color=INK, lw=1.5, zorder=3)
    # Galvanometer circle
    galv = patches.Circle((xMid, yGalv), 0.38, facecolor='white', edgecolor=INK, lw=1.5, zorder=5)
    ax.add_patch(galv)
    ax.text(xMid, yGalv, "G", fontsize=16, fontweight='bold', ha='center', va='center', color=INK, zorder=6)
    ax.text(xMid + 0.55, yGalv, "Galvanometer", fontsize=15, ha='left', va='center', color=INK)

    # Wire from galvanometer bottom down and across to jockey J
    # Route wire at y = 3.8, then straight down to J at (xJ, yJ)
    y_wire_route = 3.8
    ax.plot([xMid, xMid, xJ], [yGalv - 0.38, y_wire_route, y_wire_route], color=INK, lw=1.5, zorder=3)
    ax.plot([xJ, xJ], [y_wire_route, yJ], color=INK, lw=1.5, zorder=3)

    # Jockey indicator knife edge / arrow pointing to J
    ax.annotate('', xy=(xJ, yJ), xytext=(xJ, yJ + 0.65),
                arrowprops=dict(arrowstyle="-|>", facecolor=DEEP["blue"], edgecolor=DEEP["blue"], lw=2.0),
                zorder=6)
    ax.plot(xJ, yJ, marker='o', markersize=5, color=DEEP["blue"], zorder=7)

    # Jockey label placed to the LEFT of the vertical wire to prevent overlap
    ax.text(xJ - 0.25, 3.4, "Jockey (J)", fontsize=15, fontweight='bold', ha='right', va='center',
            color=DEEP["blue"], bbox=dict(fc='white', ec='none', pad=2), zorder=7)

    # Wire AB descriptive label (in right quadrant, with arrow to wire)
    ax.annotate("100 cm uniform wire AB", xy=(8.6, 3.0), xytext=(8.6, 4.2),
                ha='center', va='bottom', fontsize=15, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc='white', ec='none', pad=2), zorder=6)

    # Dimension lines for l1 and l2 below the scale
    dim_y = 1.0
    # Dashed extension lines down to dimension bar
    ax.plot([xA, xA], [yA - 0.2, dim_y - 0.2], color=GREY, ls='--', lw=1.2)
    ax.plot([xJ, xJ], [yA - 0.2, dim_y - 0.2], color=GREY, ls='--', lw=1.2)
    ax.plot([xB, xB], [yA - 0.2, dim_y - 0.2], color=GREY, ls='--', lw=1.2)

    # Double-headed arrows for l1 and l2
    ax.annotate('', xy=(xA, dim_y), xytext=(xJ, dim_y),
                arrowprops=dict(arrowstyle="<->", color=DEEP["blue"], lw=1.8))
    ax.text((xA + xJ)/2, dim_y - 0.35, "$l_1$", fontsize=16, fontweight='bold', ha='center', va='top', color=DEEP["blue"])

    ax.annotate('', xy=(xJ, dim_y), xytext=(xB, dim_y),
                arrowprops=dict(arrowstyle="<->", color=DEEP["green"], lw=1.8))
    ax.text((xJ + xB)/2, dim_y - 0.35, "$l_2 = (100 - l_1)$", fontsize=16, fontweight='bold', ha='center', va='top', color=DEEP["green"])

    # Cell and Switch circuit loop connected across ends A and B
    circ_y = -0.7
    # Vertical drop from A
    ax.plot([xA, xA, 3.8], [yA, circ_y, circ_y], color=INK, lw=1.5)

    # Cell: long thin line (+), short thick line (-)
    cell_plus_x = 4.2
    cell_minus_x = 4.6
    ax.plot([3.8, cell_plus_x], [circ_y, circ_y], color=INK, lw=1.5)
    ax.plot([cell_plus_x, cell_plus_x], [circ_y - 0.35, circ_y + 0.35], color=INK, lw=2.0)
    ax.plot([cell_minus_x, cell_minus_x], [circ_y - 0.20, circ_y + 0.20], color=INK, lw=4.0)
    ax.text(cell_plus_x - 0.2, circ_y + 0.38, "+", fontsize=16, ha='center', va='bottom', color=INK)
    ax.text(cell_minus_x + 0.2, circ_y + 0.38, "–", fontsize=16, ha='center', va='bottom', color=INK)
    ax.text((cell_plus_x + cell_minus_x)/2, circ_y - 0.5, "Cell", fontsize=15, ha='center', va='top', color=INK)

    # Wire from cell to switch
    ax.plot([cell_minus_x, 6.8], [circ_y, circ_y], color=INK, lw=1.5)

    # Switch (Key)
    sw_x1, sw_x2 = 6.8, 7.6
    ax.plot([sw_x1], [circ_y], marker='o', markersize=5, color=INK)
    ax.plot([sw_x2], [circ_y], marker='o', markersize=5, color=INK)
    ax.plot([sw_x1, sw_x2 - 0.1], [circ_y, circ_y + 0.35], color=INK, lw=2.0)  # tilted switch blade
    ax.plot([sw_x2, xB], [circ_y, circ_y], color=INK, lw=1.5)
    ax.plot([xB, xB], [circ_y, yB], color=INK, lw=1.5)
    ax.text((sw_x1 + sw_x2)/2, circ_y - 0.5, "Switch", fontsize=15, ha='center', va='top', color=INK)

    save(fig, out)
