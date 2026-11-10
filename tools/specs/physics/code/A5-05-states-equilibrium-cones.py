from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Ground line
    ground_y = 1.6
    ax.plot([0.5, 11.5], [ground_y, ground_y], color=INK, lw=2)

    # Sub-ground hatching / shading
    for x in np.linspace(0.8, 11.2, 45):
        ax.plot([x, x - 0.25], [ground_y, ground_y - 0.25], color=GREY, lw=1.2)

    # Parameters for cone: height H, base radius R
    H = 2.4
    R = 0.9

    # --- 1. Stable Equilibrium (Left, centered around x = 2.2) ---
    x1 = 2.2
    # Base is along ground_y: from x1 - R to x1 + R
    # Apex is at (x1, ground_y + H)
    cone1_pts = np.array([
        [x1 - R, ground_y],
        [x1 + R, ground_y],
        [x1, ground_y + H]
    ])
    cone1 = patches.Polygon(cone1_pts, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(cone1)

    # Center of gravity: 1/4 H from base
    cg1_y = ground_y + H / 4.0
    ax.plot(x1, cg1_y, marker='o', markersize=8, color=DEEP["pink"], zorder=5)
    ax.text(x1 + 0.25, cg1_y, "G", fontsize=15, color=INK, va='center', weight='bold')

    # Label 1
    ax.text(x1, 5.0, "Stable equilibrium", fontsize=16, color=INK, ha='center', weight='bold')
    ax.text(x1, 4.5, "Rests on flat base", fontsize=14, color=INK, ha='center', style='italic')

    # --- 2. Unstable Equilibrium (Middle, centered around x = 6.0) ---
    x2 = 6.0
    # Apex touches ground at (x2, ground_y)
    # Base is at top: y = ground_y + H, from x2 - R to x2 + R
    # Let's draw an ellipse top to show 3D base
    cone2_pts = np.array([
        [x2, ground_y],
        [x2 - R, ground_y + H],
        [x2 + R, ground_y + H]
    ])
    cone2 = patches.Polygon(cone2_pts, closed=True, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, zorder=3)
    ax.add_patch(cone2)
    ellipse2 = patches.Ellipse((x2, ground_y + H), 2 * R, 0.35, facecolor=CREAM, edgecolor=DEEP["orange"], lw=2.5, zorder=4)
    ax.add_patch(ellipse2)

    # Center of gravity: 3/4 H from ground tip
    cg2_y = ground_y + 3 * H / 4.0
    ax.plot(x2, cg2_y, marker='o', markersize=8, color=DEEP["pink"], zorder=5)
    ax.text(x2 + 0.25, cg2_y, "G", fontsize=15, color=INK, va='center', weight='bold')

    # Label 2
    ax.text(x2, 5.0, "Unstable equilibrium", fontsize=16, color=INK, ha='center', weight='bold')
    ax.text(x2, 4.5, "Balanced on sharp tip", fontsize=14, color=INK, ha='center', style='italic')

    # --- 3. Neutral Equilibrium (Right, centered around x = 9.8) ---
    x3 = 9.8
    # Cone lying horizontally on its side.
    # The slant line touches the ground: from x3 - H/2 to x3 + H/2 at ground_y
    # Slant length S = sqrt(H^2 + R^2), apex angle theta = arctan(R/H)
    # In 2D projection lying on side:
    # Contact edge is along the ground: x from x_tip to x_base
    x_tip = 8.6
    x_base_center = x_tip + H  # 11.0
    # Base is a line/ellipse tilted relative to vertical by apex semi-angle or purely drawn in profile:
    # A cone lying on its side has:
    # - Apex at (x_tip, ground_y)
    # - Bottom contact line: from (x_tip, ground_y) to (x_base_center, ground_y)
    # - Top generator line: from (x_tip, ground_y) to (x_base_center, ground_y + 2*R)
    # - Circular base (seen slanted as ellipse) connecting the ends
    y_top = ground_y + 2 * R
    cone3_pts = np.array([
        [x_tip, ground_y],
        [x_base_center, ground_y],
        [x_base_center, y_top]
    ])
    cone3 = patches.Polygon(cone3_pts, closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=2.5, zorder=3)
    ax.add_patch(cone3)
    ellipse3 = patches.Ellipse((x_base_center, ground_y + R), 0.35, 2 * R, facecolor=CREAM, edgecolor=DEEP["green"], lw=2.5, zorder=4)
    ax.add_patch(ellipse3)

    # Center of gravity: lies along the central axis at distance 3/4 H from apex
    # Central axis runs from (x_tip, ground_y) to (x_base_center, ground_y + R)
    cg3_x = x_tip + 0.75 * H
    cg3_y = ground_y + 0.75 * R
    ax.plot(cg3_x, cg3_y, marker='o', markersize=8, color=DEEP["pink"], zorder=5)
    ax.text(cg3_x + 0.25, cg3_y, "G", fontsize=15, color=INK, va='center', weight='bold')

    # Label 3
    ax.text(x3, 5.0, "Neutral equilibrium", fontsize=16, color=INK, ha='center', weight='bold')
    ax.text(x3, 4.5, "Lies on curved side", fontsize=14, color=INK, ha='center', style='italic')

    # Legend / Key for G
    ax.plot(0.9, 0.6, marker='o', markersize=8, color=DEEP["pink"])
    ax.text(1.2, 0.6, "G = Centre of gravity", fontsize=14, color=INK, va='center')

    save(fig, out)
