from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse

def draw(out):
    fig = canvas(12, 5.5)
    
    # 3 subplots for Cuboid, Cylinder, Cone
    ax1 = fig.add_axes([0.03, 0.08, 0.28, 0.82])
    ax2 = fig.add_axes([0.36, 0.08, 0.28, 0.82])
    ax3 = fig.add_axes([0.69, 0.08, 0.28, 0.82])
    
    for ax in [ax1, ax2, ax3]:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-0.2, 5.2)
        ax.set_ylim(-0.5, 6.5)

    # ------------------ 1. CUBOID ------------------
    ax1.set_title("Cuboid", fontsize=16, color=INK, pad=12, weight='bold')
    
    x0, y0 = 0.8, 1.2
    l_val, h_val = 2.6, 3.2
    dx, dy = 1.1, 0.9

    p_front = np.array([[x0, y0], [x0 + l_val, y0], [x0 + l_val, y0 + h_val], [x0, y0 + h_val]])
    p_top = np.array([[x0, y0 + h_val], [x0 + l_val, y0 + h_val], 
                      [x0 + l_val + dx, y0 + h_val + dy], [x0 + dx, y0 + h_val + dy]])
    p_side = np.array([[x0 + l_val, y0], [x0 + l_val + dx, y0 + dy], 
                       [x0 + l_val + dx, y0 + h_val + dy], [x0 + l_val, y0 + h_val]])

    # Hidden lines (dashed)
    p_back_bottom_left = np.array([x0 + dx, y0 + dy])
    ax1.plot([x0, p_back_bottom_left[0]], [y0, p_back_bottom_left[1]], ls='--', color=DEEP["blue"], lw=1.5, alpha=0.6)
    ax1.plot([p_back_bottom_left[0], x0 + l_val + dx], [p_back_bottom_left[1], y0 + dy], ls='--', color=DEEP["blue"], lw=1.5, alpha=0.6)
    ax1.plot([p_back_bottom_left[0], p_back_bottom_left[0]], [p_back_bottom_left[1], y0 + h_val + dy], ls='--', color=DEEP["blue"], lw=1.5, alpha=0.6)

    # Shaded faces
    ax1.add_patch(Polygon(p_front, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2, zorder=2))
    ax1.add_patch(Polygon(p_top, facecolor=LAV, edgecolor=DEEP["blue"], lw=2.2, zorder=2))
    ax1.add_patch(Polygon(p_side, facecolor=CREAM, edgecolor=DEEP["blue"], lw=2.2, zorder=2))

    # Length (l)
    dim_y = y0 - 0.45
    ax1.annotate("", xy=(x0, dim_y), xytext=(x0 + l_val, dim_y),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax1.text(x0 + l_val/2, dim_y - 0.35, "l", fontsize=16, ha='center', va='center', color=INK, weight='bold')

    # Height (h)
    dim_x = x0 - 0.45
    ax1.annotate("", xy=(dim_x, y0), xytext=(dim_x, y0 + h_val),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax1.text(dim_x - 0.35, y0 + h_val/2, "h", fontsize=16, ha='center', va='center', color=INK, weight='bold')

    # Breadth (b)
    ax1.annotate("", xy=(x0 + l_val + 0.25, y0 - 0.15), xytext=(x0 + l_val + dx + 0.25, y0 + dy - 0.15),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax1.text(x0 + l_val + dx/2 + 0.45, y0 + dy/2 - 0.35, "b", fontsize=16, ha='center', va='center', color=INK, weight='bold')


    # ------------------ 2. CYLINDER ------------------
    ax2.set_title("Cylinder", fontsize=16, color=INK, pad=12, weight='bold')
    
    cx, cy_b = 2.4, 1.3
    h_cyl = 3.3
    r_cyl = 1.4
    ry = 0.45

    # Cylinder body
    theta = np.linspace(np.pi, 2*np.pi, 100)
    x_bot = cx + r_cyl * np.cos(theta)
    y_bot = cy_b + ry * np.sin(theta)
    body_pts = np.vstack([
        np.array([cx - r_cyl, cy_b]),
        np.column_stack([x_bot, y_bot]),
        np.array([[cx + r_cyl, cy_b + h_cyl], [cx - r_cyl, cy_b + h_cyl]])
    ])
    ax2.add_patch(Polygon(body_pts, facecolor=GREEN, edgecolor='none', zorder=2))

    # Side profile lines
    ax2.plot([cx - r_cyl, cx - r_cyl], [cy_b, cy_b + h_cyl], color=DEEP["green"], lw=2.2, zorder=3)
    ax2.plot([cx + r_cyl, cx + r_cyl], [cy_b, cy_b + h_cyl], color=DEEP["green"], lw=2.2, zorder=3)

    # Bottom ellipse arcs
    t_top_half = np.linspace(0, np.pi, 100)
    t_bot_half = np.linspace(np.pi, 2*np.pi, 100)
    ax2.plot(cx + r_cyl * np.cos(t_top_half), cy_b + ry * np.sin(t_top_half),
             ls='--', color=DEEP["green"], lw=1.8, zorder=2)
    ax2.plot(cx + r_cyl * np.cos(t_bot_half), cy_b + ry * np.sin(t_bot_half),
             color=DEEP["green"], lw=2.2, zorder=3)

    # Top ellipse (filled)
    top_ellipse = Ellipse((cx, cy_b + h_cyl), 2*r_cyl, 2*ry,
                          facecolor=LAV, edgecolor=DEEP["green"], lw=2.2, zorder=4)
    ax2.add_patch(top_ellipse)

    # Top center point & radius arrow and label (r)
    y_top = cy_b + h_cyl
    ax2.plot([cx], [y_top], 'o', color=INK, markersize=4, zorder=5)
    ax2.annotate("", xy=(cx, y_top), xytext=(cx + r_cyl, y_top),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5), zorder=5)
    ax2.text(cx + r_cyl/2, y_top + 0.45, "r", fontsize=16, ha='center', va='center',
             color=INK, weight='bold', zorder=6)

    # Height (h) on the left
    dim_xc = cx - r_cyl - 0.45
    ax2.annotate("", xy=(dim_xc, cy_b), xytext=(dim_xc, cy_b + h_cyl),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5))
    ax2.text(dim_xc - 0.35, cy_b + h_cyl/2, "h", fontsize=16, ha='center', va='center', color=INK, weight='bold')


    # ------------------ 3. CONE ------------------
    ax3.set_title("Cone", fontsize=16, color=INK, pad=12, weight='bold')
    
    cx3, cy3 = 2.4, 1.3
    h_cone = 3.6
    r_cone = 1.5
    ry3 = 0.45
    apex = (cx3, cy3 + h_cone)

    # Cone body fill
    t_bot_cone = np.linspace(np.pi, 2*np.pi, 100)
    xb_cone = cx3 + r_cone * np.cos(t_bot_cone)
    yb_cone = cy3 + ry3 * np.sin(t_bot_cone)
    cone_pts = np.vstack([
        [apex[0], apex[1]],
        np.column_stack([xb_cone, yb_cone])
    ])
    ax3.add_patch(Polygon(cone_pts, facecolor=ORANGE, edgecolor='none', zorder=2))

    # Slant edges
    ax3.plot([cx3 - r_cone, apex[0]], [cy3, apex[1]], color=DEEP["orange"], lw=2.2, zorder=3)
    ax3.plot([cx3 + r_cone, apex[0]], [cy3, apex[1]], color=DEEP["orange"], lw=2.2, zorder=3)

    # Base ellipse arcs
    t_top_c = np.linspace(0, np.pi, 100)
    ax3.plot(cx3 + r_cone * np.cos(t_top_c), cy3 + ry3 * np.sin(t_top_c),
             ls='--', color=DEEP["orange"], lw=1.8, zorder=2)
    ax3.plot(xb_cone, yb_cone, color=DEEP["orange"], lw=2.2, zorder=3)

    # Axis (height h) inside cone
    ax3.plot([cx3, apex[0]], [cy3, apex[1]], ls='--', color=INK, lw=1.4, zorder=4)
    # Right-angle mark at base center
    rw = 0.22
    ax3.plot([cx3, cx3, cx3 + rw], [cy3 + rw, cy3 + rw, cy3], color=INK, lw=1.2, zorder=4)

    # Base center & radius (r)
    ax3.plot([cx3], [cy3], 'o', color=INK, markersize=4, zorder=5)
    ax3.annotate("", xy=(cx3, cy3), xytext=(cx3 + r_cone, cy3),
                 arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5), zorder=5)
    ax3.text(cx3 + r_cone/2, cy3 - 0.42, "r", fontsize=16, ha='center', va='center',
             color=INK, weight='bold', zorder=6)

    # Height label (h)
    ax3.text(cx3 - 0.35, cy3 + h_cone * 0.45, "h", fontsize=16, ha='center', va='center',
             color=INK, weight='bold', bbox=dict(fc='white', ec='none', pad=1), zorder=6)

    # Slant height label (l) along right side
    slant_mid_x = (cx3 + r_cone + apex[0]) / 2 + 0.32
    slant_mid_y = (cy3 + apex[1]) / 2 + 0.1
    ax3.text(slant_mid_x, slant_mid_y, "l", fontsize=16, ha='center', va='center',
             color=INK, weight='bold', bbox=dict(fc='white', ec='none', pad=1))

    save(fig, out)
