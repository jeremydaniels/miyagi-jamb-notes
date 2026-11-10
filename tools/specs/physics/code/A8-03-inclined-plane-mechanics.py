from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-0.5, 9.8)
    ax.set_ylim(-0.5, 6.2)

    # Geometry of the inclined plane
    x0, y0 = 1.0, 1.0
    base_len = 6.2
    theta_deg = 28.0
    theta_rad = np.radians(theta_deg)
    h_len = base_len * np.tan(theta_rad)
    L_len = base_len / np.cos(theta_rad)

    x_right = x0 + base_len
    y_right = y0
    x_top = x_right
    y_top = y0 + h_len

    # Ground line
    ax.plot([x0 - 0.6, x_right + 1.2], [y0, y0], color=INK, lw=2.0, zorder=1)

    # Draw the wedge (inclined plane)
    wedge_coords = np.array([[x0, y0], [x_right, y_right], [x_top, y_top]])
    wedge_poly = patches.Polygon(wedge_coords, closed=True, facecolor=CREAM, edgecolor=INK, lw=2.5, zorder=2)
    ax.add_patch(wedge_poly)

    # Right-angle indicator at bottom-right corner
    ra_size = 0.45
    ra_coords = [
        [x_right - ra_size, y0],
        [x_right - ra_size, y0 + ra_size],
        [x_right, y0 + ra_size]
    ]
    ax.plot([c[0] for c in ra_coords], [c[1] for c in ra_coords], color=INK, lw=1.5, zorder=3)

    # Angle theta arc and label
    arc_radius = 1.4
    arc_angles = np.linspace(0, theta_rad, 40)
    ax.plot(x0 + arc_radius * np.cos(arc_angles), y0 + arc_radius * np.sin(arc_angles), color=INK, lw=1.8, zorder=3)
    ax.text(x0 + 1.75 * np.cos(theta_rad / 2), y0 + 1.75 * np.sin(theta_rad / 2), 'θ',
            fontsize=17, color=INK, ha='center', va='center')

    # Dimension lines: Height 'h'
    dim_x = x_right + 0.55
    ax.plot([x_right + 0.1, dim_x + 0.35], [y0, y0], color=GREY, lw=1.2)
    ax.plot([x_right + 0.1, dim_x + 0.35], [y_top, y_top], color=GREY, lw=1.2)
    ax.annotate('', xy=(dim_x, y_top), xytext=(dim_x, y0),
                arrowprops=dict(arrowstyle='<->', color=INK, lw=1.5, shrinkA=0, shrinkB=0))
    ax.text(dim_x + 0.25, (y0 + y_top) / 2, 'h', fontsize=16, color=INK, ha='left', va='center', fontweight='bold')

    # Dimension lines: Slanted length 'L' (placed below/along the incline, clearly offset)
    # Unit vectors parallel and perpendicular to the slope
    ux = np.cos(theta_rad)
    uy = np.sin(theta_rad)
    nx = -uy  # outward normal (perpendicular up-left)
    ny = ux

    offset_dist = 1.85
    p0_off = np.array([x0 + nx * offset_dist, y0 + ny * offset_dist])
    ptop_off = np.array([x_top + nx * offset_dist, y_top + ny * offset_dist])

    # Extension tick lines for L
    ax.plot([x0 + nx * 0.2, p0_off[0] + nx * 0.2], [y0 + ny * 0.2, p0_off[1] + ny * 0.2], color=GREY, lw=1.2)
    ax.plot([x_top + nx * 0.2, ptop_off[0] + nx * 0.2], [y_top + ny * 0.2, ptop_off[1] + ny * 0.2], color=GREY, lw=1.2)
    ax.annotate('', xy=(ptop_off[0], ptop_off[1]), xytext=(p0_off[0], p0_off[1]),
                arrowprops=dict(arrowstyle='<->', color=INK, lw=1.5, shrinkA=0, shrinkB=0))

    mid_L = (p0_off + ptop_off) / 2
    ax.text(mid_L[0] + nx * 0.25, mid_L[1] + ny * 0.25, 'L', fontsize=16, color=INK,
            ha='center', va='center', fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=2))

    # Square block resting on the incline
    s_mid = 0.46 * L_len
    bx_base = x0 + s_mid * ux
    by_base = y0 + s_mid * uy

    block_size = 1.35
    # Bottom-left of block along slope
    bl_x = bx_base - (block_size / 2) * ux
    bl_y = by_base - (block_size / 2) * uy

    block = patches.Rectangle((bl_x, bl_y), block_size, block_size,
                              angle=theta_deg, rotation_point=(bl_x, bl_y),
                              facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2, zorder=4)
    ax.add_patch(block)

    # Label on the block: 'Load (L) = mg' split into two clean lines to avoid crossing borders
    center_x = bx_base + nx * (block_size / 2)
    center_y = by_base + ny * (block_size / 2)
    ax.text(center_x, center_y, 'Load (L)\n= mg', fontsize=14, color=INK,
            ha='center', va='center', rotation=theta_deg, fontweight='bold', zorder=5,
            multialignment='center')

    # Effort arrow pointing parallel up the slope
    arrow_start_s = s_mid + (block_size / 2) + 0.1
    arrow_end_s = arrow_start_s + 1.45

    # Arrow level with the middle of the block
    arrow_h = block_size / 2
    as_x = x0 + arrow_start_s * ux + nx * arrow_h
    as_y = y0 + arrow_start_s * uy + ny * arrow_h
    ae_x = x0 + arrow_end_s * ux + nx * arrow_h
    ae_y = y0 + arrow_end_s * uy + ny * arrow_h

    ax.annotate('', xy=(ae_x, ae_y), xytext=(as_x, as_y),
                arrowprops=dict(arrowstyle='-|>', color=DEEP["orange"], lw=3.0,
                                mutation_scale=20), zorder=6)

    # Label for Effort (E) placed along the arrow direction
    label_s = arrow_end_s + 0.15
    al_x = x0 + label_s * ux + nx * arrow_h
    al_y = y0 + label_s * uy + ny * arrow_h
    ax.text(al_x, al_y, 'Effort (E)', fontsize=15, color=DEEP["orange"],
            ha='left', va='center', rotation=theta_deg, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=2), zorder=6)

    save(fig, out)
