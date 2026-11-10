from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Magnet geometry
    magnet_h = 1.0
    magnet_half_w = 1.6
    d = 1.35  # Effective pole locations inside the magnet

    def get_field(x, y):
        # North (+q) at (-d, 0), South (-q) at (+d, 0)
        r1_sq = (x + d)**2 + y**2
        r2_sq = (x - d)**2 + y**2
        r1 = np.maximum(np.sqrt(r1_sq), 0.05)
        r2 = np.maximum(np.sqrt(r2_sq), 0.05)
        
        Bx = (x + d) / (r1**3) - (x - d) / (r2**3)
        By = y / (r1**3) - y / (r2**3)
        b_mag = np.hypot(Bx, By)
        return Bx / b_mag, By / b_mag

    dt = 0.02

    def trace_line(x0, y0, max_steps=1500, target_x=d):
        pts = [(x0, y0)]
        curr_x, curr_y = x0, y0
        for _ in range(max_steps):
            bx, by = get_field(curr_x, curr_y)
            curr_x += bx * dt
            curr_y += by * dt
            pts.append((curr_x, curr_y))
            
            # Reached target pole (South)
            if np.hypot(curr_x - target_x, curr_y) < 0.28:
                break
            # Out of bounds
            if abs(curr_x) > 6.0 or abs(curr_y) > 4.0:
                break
        return np.array(pts)

    def add_arrow(pts, t_fraction=0.5):
        if len(pts) < 25:
            return
        idx = int(len(pts) * t_fraction)
        idx = max(2, min(len(pts) - 3, idx))
        dx = pts[idx + 2, 0] - pts[idx - 2, 0]
        dy = pts[idx + 2, 1] - pts[idx - 2, 1]
        mag = np.hypot(dx, dy)
        if mag > 0:
            ax.annotate('',
                        xy=(pts[idx, 0] + dx/mag * 0.08, pts[idx, 1] + dy/mag * 0.08),
                        xytext=(pts[idx, 0] - dx/mag * 0.08, pts[idx, 1] - dy/mag * 0.08),
                        arrowprops=dict(arrowstyle="->,head_length=0.45,head_width=0.3",
                                        color=DEEP["blue"], lw=2.2),
                        zorder=3)

    # Angles for closed loops (connecting N to S) and open lines (leaving N)
    loop_angles = [12, 24, 38, 54, 70]
    open_angles = [88, 110, 135, 160]

    # 1. Closed loop field lines
    for ang in loop_angles:
        rad = np.radians(ang)
        x0 = -d + 0.25 * np.cos(rad)
        y0 = 0.25 * np.sin(rad)
        pts_top = trace_line(x0, y0)
        pts_bot = pts_top.copy()
        pts_bot[:, 1] = -pts_bot[:, 1]
        
        for pts in [pts_top, pts_bot]:
            ax.plot(pts[:, 0], pts[:, 1], color=DEEP["blue"], lw=2.0, zorder=2)
            add_arrow(pts, t_fraction=0.5)

    # 2. Open lines
    for ang in open_angles:
        rad = np.radians(ang)
        x0 = -d + 0.25 * np.cos(rad)
        y0 = 0.25 * np.sin(rad)
        pts_n_top = trace_line(x0, y0)
        
        # Mirror for bottom North open lines
        pts_n_bot = pts_n_top.copy()
        pts_n_bot[:, 1] = -pts_n_bot[:, 1]
        
        # Mirror and reverse for South open lines (coming from infinity to S)
        pts_s_top = pts_n_top.copy()[::-1]
        pts_s_top[:, 0] = -pts_s_top[:, 0]
        
        pts_s_bot = pts_n_bot.copy()[::-1]
        pts_s_bot[:, 0] = -pts_s_bot[:, 0]
        
        for pts in [pts_n_top, pts_n_bot, pts_s_top, pts_s_bot]:
            ax.plot(pts[:, 0], pts[:, 1], color=DEEP["blue"], lw=2.0, zorder=2)
            add_arrow(pts, t_fraction=0.45)

    # 3. Straight horizontal axis lines
    # Left: pointing LEFT (away from N)
    ax.plot([-5.5, -magnet_half_w], [0, 0], color=DEEP["blue"], lw=2.0, zorder=2)
    ax.annotate('', xy=(-3.8, 0), xytext=(-3.4, 0),
                arrowprops=dict(arrowstyle="->,head_length=0.45,head_width=0.3",
                                color=DEEP["blue"], lw=2.2), zorder=3)
    
    # Right: pointing LEFT (towards S)
    ax.plot([magnet_half_w, 5.5], [0, 0], color=DEEP["blue"], lw=2.0, zorder=2)
    ax.annotate('', xy=(3.4, 0), xytext=(3.8, 0),
                arrowprops=dict(arrowstyle="->,head_length=0.45,head_width=0.3",
                                color=DEEP["blue"], lw=2.2), zorder=3)

    # Draw Bar Magnet
    rect_n = patches.Rectangle((-magnet_half_w, -magnet_h/2), magnet_half_w, magnet_h,
                               facecolor=PINK, edgecolor=INK, linewidth=2.5, zorder=4)
    ax.add_patch(rect_n)
    
    rect_s = patches.Rectangle((0, -magnet_h/2), magnet_half_w, magnet_h,
                               facecolor=BLUE, edgecolor=INK, linewidth=2.5, zorder=4)
    ax.add_patch(rect_s)

    # Labels inside the magnet
    ax.text(-magnet_half_w / 2, 0, 'N', fontsize=22, fontweight='bold', color=INK,
            ha='center', va='center', zorder=5)
    ax.text(magnet_half_w / 2, 0, 'S', fontsize=22, fontweight='bold', color=INK,
            ha='center', va='center', zorder=5)

    # Title
    ax.text(0, 3.15, "Magnetic Field of a Bar Magnet", fontsize=18, fontweight='bold',
            color=INK, ha='center', va='center',
            bbox=dict(fc="white", ec="none", pad=4))

    save(fig, out)
