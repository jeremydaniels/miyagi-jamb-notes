from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

def draw(out):
    fig = canvas(15, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Colors for cube faces
    c_front = BLUE
    c_top = "#E2EDF8"    # lighter soft blue
    c_side = "#BFD9F2"   # medium soft blue
    edge_col = DEEP["blue"]

    def draw_cube(x0, y0, s):
        # Oblique projection: dx = 0.4 * s, dy = 0.3 * s
        dx = 0.4 * s
        dy = 0.3 * s
        
        # Front face
        front = [[x0, y0], [x0 + s, y0], [x0 + s, y0 + s], [x0, y0 + s]]
        poly_f = Polygon(front, facecolor=c_front, edgecolor=edge_col, lw=1.6, zorder=2)
        ax.add_patch(poly_f)
        
        # Top face
        top = [[x0, y0 + s], [x0 + s, y0 + s], [x0 + s + dx, y0 + s + dy], [x0 + dx, y0 + s + dy]]
        poly_t = Polygon(top, facecolor=c_top, edgecolor=edge_col, lw=1.6, zorder=2)
        ax.add_patch(poly_t)
        
        # Right face
        side = [[x0 + s, y0], [x0 + s + dx, y0 + dy], [x0 + s + dx, y0 + s + dy], [x0 + s, y0 + s]]
        poly_s = Polygon(side, facecolor=c_side, edgecolor=edge_col, lw=1.6, zorder=2)
        ax.add_patch(poly_s)

    # 1. Cubes placed comfortably on the left half (X: 0.5 to 6.8)
    base_y = 2.7
    
    # Cube 1: side 0.65
    c1_x = 0.6
    s1 = 0.65
    draw_cube(c1_x, base_y, s1)
    
    # Cube 2: side 1.25
    c2_x = 1.8
    s2 = 1.25
    draw_cube(c2_x, base_y, s2)
    
    # Cube 3: side 2.4
    c3_x = 3.65
    s3 = 2.4
    draw_cube(c3_x, base_y, s3)

    # Labels and blank panels under cubes
    cube_data = [
        (c1_x + (s1 + 0.4 * s1) / 2, "1 cm cube", "SA:V 6:1"),
        (c2_x + (s2 + 0.4 * s2) / 2, "2 cm cube", "SA:V 3:1"),
        (c3_x + (s3 + 0.4 * s3) / 2, "4 cm cube", "SA:V 1.5:1")
    ]
    
    for cx, name_lbl, ratio_lbl in cube_data:
        # Title of cube
        ax.text(cx, 2.25, name_lbl, ha="center", va="center", fontsize=12.5, fontweight="bold", color=INK)
        
        # Blank panel
        p_w, p_h = 1.45, 0.7
        panel = FancyBboxPatch((cx - p_w / 2, 1.15), p_w, p_h,
                               boxstyle="round,pad=0.06,rounding_size=0.12",
                               facecolor=CREAM, edgecolor=GREY, lw=1.2)
        ax.add_patch(panel)
        
        # SA:V label inside panel
        ax.text(cx, 1.15 + p_h / 2, ratio_lbl, ha="center", va="center", fontsize=11.5, color=INK)

    # Vertical separator line between cubes and biological sketches
    ax.plot([6.85, 6.85], [0.8, 6.8], color=GREY, lw=1.2, ls="--")

    # Header / Key indicator for oxygen diffusion
    ax.text(10.9, 6.8, "Diffusion of oxygen into organisms", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=INK)

    # 2. Amoeba sketch (left side of organism panel, x ~ 8.4)
    amoeba_center = (8.4, 4.4)
    theta = np.linspace(0, 2 * np.pi, 150)
    # Pseudopod-like slight irregularities
    r_amoeba = 0.65 + 0.05 * np.sin(3 * theta) + 0.04 * np.cos(5 * theta)
    ax.fill(amoeba_center[0] + r_amoeba * np.cos(theta),
            amoeba_center[1] + r_amoeba * np.sin(theta),
            color=GREEN, alpha=0.35, ec=DEEP["green"], lw=2, zorder=2)
    # Nucleus
    ax.plot(amoeba_center[0], amoeba_center[1], 'o', color=DEEP["green"], ms=6, zorder=3)
    
    # Arrows diffusing in all around surface, penetrating right to center
    n_arrows = 8
    arrow_angles = np.linspace(0, 2 * np.pi, n_arrows, endpoint=False)
    for a in arrow_angles:
        x_start = amoeba_center[0] + 1.15 * np.cos(a)
        y_start = amoeba_center[1] + 1.15 * np.sin(a)
        x_end = amoeba_center[0] + 0.15 * np.cos(a)
        y_end = amoeba_center[1] + 0.15 * np.sin(a)
        ax.annotate("", xy=(x_end, y_end), xytext=(x_start, y_start),
                    arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8, mutation_scale=12),
                    zorder=4)

    # Amoeba label (stacked neatly below)
    ax.text(amoeba_center[0], 2.2, "Amoeba:\ndiffusion reaches\nall parts",
            ha="center", va="top", fontsize=11.5, fontweight="bold", color=INK)

    # 3. Large Organism sketch (right side of organism panel, x ~ 12.3)
    org_center = (12.3, 4.4)
    theta_blob = np.linspace(0, 2 * np.pi, 200)
    # Larger blob animal shape
    r_blob = 1.35 + 0.12 * np.sin(2 * theta_blob) + 0.08 * np.cos(4 * theta_blob)
    ax.fill(org_center[0] + r_blob * np.cos(theta_blob),
            org_center[1] + r_blob * np.sin(theta_blob),
            color=LAV, alpha=0.35, ec=DEEP["lav"], lw=2, zorder=2)

    # Inner cells at the core
    inner_offsets = [(0, 0), (-0.2, 0.18), (0.2, 0.18), (-0.18, -0.2), (0.18, -0.2), (0, 0.32), (0, -0.35)]
    for dx_c, dy_c in inner_offsets:
        ax.plot(org_center[0] + dx_c, org_center[1] + dy_c, 'o', color=DEEP["lav"], ms=4.5, zorder=3)
    ax.text(org_center[0], org_center[1] - 0.58, "inner cells",
            ha="center", va="center", fontsize=10, color=INK, style="italic", zorder=5)

    # Arrows from surface stopping short of deep centre cells
    n_blob_arrows = 10
    blob_angles = np.linspace(0, 2 * np.pi, n_blob_arrows, endpoint=False)
    for a in blob_angles:
        x_start = org_center[0] + 1.8 * np.cos(a)
        y_start = org_center[1] + 1.8 * np.sin(a)
        x_end = org_center[0] + 0.95 * np.cos(a)
        y_end = org_center[1] + 0.95 * np.sin(a)
        ax.annotate("", xy=(x_end, y_end), xytext=(x_start, y_start),
                    arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8, mutation_scale=12),
                    zorder=4)

    # Large organism label (stacked neatly below)
    ax.text(org_center[0], 2.2, "Large organism:\ndiffusion too slow\nto reach inner cells",
            ha="center", va="top", fontsize=11.5, fontweight="bold", color=INK)

    save(fig, out)
