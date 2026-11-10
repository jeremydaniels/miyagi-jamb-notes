from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect("equal")
    ax.axis("off")

    # Outer environment nodes definitions (PESTLE order roughly: Political, Economic, Social, Tech, Environmental, Legal)
    R = 3.6
    angles = np.linspace(90, 90 - 360, 6, endpoint=False)
    
    categories = [
        {"title": "Political", "color": BLUE, "deep": DEEP["blue"]},
        {"title": "Economic", "color": ORANGE, "deep": DEEP["orange"]},
        {"title": "Social/Cultural", "color": PINK, "deep": DEEP["pink"]},
        {"title": "Technological", "color": LAV, "deep": DEEP["lav"]},
        {"title": "Environmental", "color": GREEN, "deep": DEEP["green"]},
        {"title": "Legal", "color": CREAM, "deep": GREY}
    ]

    node_radius = 1.35

    # Connecting spokes/bridges from center to nodes
    for ang in angles:
        rad = np.radians(ang)
        x_end = R * np.cos(rad)
        y_end = R * np.sin(rad)
        ax.plot([0, x_end], [0, y_end], color=GREY, lw=4, zorder=1, linestyle="--")

    # Connecting ring among external factors
    ring = patches.Circle((0, 0), R, fill=False, edgecolor=GREY, lw=2.5, linestyle=":", zorder=1)
    ax.add_patch(ring)

    # Center: The Business
    center_r = 1.6
    center_circle = patches.Circle((0, 0), center_r, facecolor='white', edgecolor=INK, lw=3, zorder=5)
    ax.add_patch(center_circle)

    # Modern Corporate Building Icon in Center
    ax.add_patch(patches.Rectangle((-0.45, -0.6), 0.9, 1.2, facecolor=LAV, edgecolor=INK, lw=2, zorder=6))
    ax.add_patch(patches.Rectangle((-0.8, -0.6), 0.35, 0.8, facecolor=CREAM, edgecolor=INK, lw=2, zorder=6))
    ax.add_patch(patches.Rectangle((0.45, -0.6), 0.35, 0.6, facecolor=CREAM, edgecolor=INK, lw=2, zorder=6))
    
    for wy in [-0.3, 0.0, 0.3]:
        for wx in [-0.3, -0.05, 0.2]:
            ax.add_patch(patches.Rectangle((wx, wy), 0.15, 0.18, facecolor='white', edgecolor=INK, lw=1.2, zorder=7))
    ax.add_patch(patches.Rectangle((-0.68, -0.2), 0.12, 0.25, facecolor='white', edgecolor=INK, lw=1, zorder=7))
    ax.add_patch(patches.Rectangle((0.57, -0.3), 0.12, 0.2, facecolor='white', edgecolor=INK, lw=1, zorder=7))
    ax.add_patch(patches.Rectangle((-0.15, -0.6), 0.3, 0.2, facecolor=INK, zorder=7))

    ax.text(0, -1.0, "The Business", fontsize=16, fontweight="bold", ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.9), zorder=8)

    # Draw 6 External nodes with icons
    for i, (ang, cat) in enumerate(zip(angles, categories)):
        rad = np.radians(ang)
        cx = R * np.cos(rad)
        cy = R * np.sin(rad)

        circle = patches.Circle((cx, cy), node_radius, facecolor=cat["color"], edgecolor=cat["deep"], lw=3, zorder=3)
        ax.add_patch(circle)

        label_y = cy - 0.85
        ax.text(cx, label_y, cat["title"], fontsize=15, fontweight="bold", ha="center", va="center", color=INK,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=cat["deep"], lw=1.5), zorder=6)

        icx, icy = cx, cy + 0.22

        if i == 0:
            triangle = patches.Polygon([[icx - 0.6, icy + 0.15], [icx + 0.6, icy + 0.15], [icx, icy + 0.55]],
                                       closed=True, facecolor="white", edgecolor=INK, lw=2, zorder=5)
            ax.add_patch(triangle)
            ax.add_patch(patches.Rectangle((icx - 0.55, icy + 0.05), 1.1, 0.1, facecolor="white", edgecolor=INK, lw=1.5, zorder=5))
            for col_x in np.linspace(icx - 0.45, icx + 0.35, 4):
                ax.add_patch(patches.Rectangle((col_x, icy - 0.4), 0.1, 0.45, facecolor="white", edgecolor=INK, lw=1.5, zorder=5))
            ax.add_patch(patches.Rectangle((icx - 0.65, icy - 0.5), 1.3, 0.12, facecolor="white", edgecolor=INK, lw=2, zorder=5))

        elif i == 1:
            ax.plot([icx - 0.65, icx - 0.65, icx + 0.65], [icy + 0.45, icy - 0.45, icy - 0.45], color=INK, lw=2, zorder=5)
            gx = np.array([icx - 0.55, icx - 0.2, icx + 0.15, icx + 0.55])
            gy = np.array([icy - 0.35, icy - 0.1, icy - 0.2, icy + 0.35])
            ax.plot(gx, gy, color=cat["deep"], lw=3.5, zorder=5)
            ax.scatter(gx[-1], gy[-1], s=40, color=cat["deep"], zorder=6)
            ax.text(icx - 0.1, icy + 0.15, "₦", fontsize=20, fontweight="bold", color=INK,
                    ha="center", va="center", bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec=cat["deep"], lw=1.5), zorder=6)

        elif i == 2:
            people = [
                (icx, icy + 0.05, 0.18, 0.45),
                (icx - 0.42, icy - 0.1, 0.15, 0.38),
                (icx + 0.42, icy - 0.1, 0.15, 0.38)
            ]
            for px, py, hr, sw in people:
                ax.add_patch(patches.Circle((px, py + hr + 0.05), hr, facecolor="white", edgecolor=INK, lw=2, zorder=5))
                ax.add_patch(patches.Wedge((px, py - 0.15), sw/2, 0, 180, facecolor="white", edgecolor=INK, lw=2, zorder=5))

        elif i == 3:
            ax.add_patch(patches.Rectangle((icx - 0.55, icy - 0.45), 0.5, 0.9, facecolor="white", edgecolor=INK, lw=2, zorder=5))
            ax.add_patch(patches.Rectangle((icx - 0.5, icy - 0.33), 0.4, 0.65, facecolor=LAV, edgecolor=INK, lw=1.2, zorder=6))
            ax.add_patch(patches.Circle((icx - 0.3, icy - 0.39), 0.03, facecolor=INK, zorder=7))
            
            gear_cx, gear_cy = icx + 0.3, icy + 0.05
            ax.add_patch(patches.Circle((gear_cx, gear_cy), 0.32, facecolor="white", edgecolor=INK, lw=2, zorder=5))
            ax.add_patch(patches.Circle((gear_cx, gear_cy), 0.12, facecolor=LAV, edgecolor=INK, lw=1.5, zorder=7))
            for g_ang in np.linspace(0, 315, 8):
                grad = np.radians(g_ang)
                gx1 = gear_cx + 0.32 * np.cos(grad)
                gy1 = gear_cy + 0.32 * np.sin(grad)
                gx2 = gear_cx + 0.42 * np.cos(grad)
                gy2 = gear_cy + 0.42 * np.sin(grad)
                ax.plot([gx1, gx2], [gy1, gy2], color=INK, lw=4, solid_capstyle="round", zorder=6)

        elif i == 4:
            t = np.linspace(-0.4, 0.4, 100)
            leaf_x1 = icx + (0.4**2 - t**2) * 0.9
            leaf_y1 = icy + t
            leaf_x2 = icx - (0.4**2 - t**2) * 0.9
            leaf_y2 = icy + t
            leaf_xs = np.concatenate([leaf_x1, leaf_x2[::-1]])
            leaf_ys = np.concatenate([leaf_y1, leaf_y2[::-1]])
            leaf_poly = patches.Polygon(np.column_stack([leaf_xs, leaf_ys]), closed=True, facecolor="white", edgecolor=cat["deep"], lw=2.5, zorder=5)
            ax.add_patch(leaf_poly)
            ax.plot([icx, icx], [icy - 0.5, icy + 0.4], color=cat["deep"], lw=2.5, zorder=6)
            ax.plot([icx, icx + 0.18], [icy - 0.1, icy + 0.05], color=cat["deep"], lw=1.8, zorder=6)
            ax.plot([icx, icx - 0.18], [icy - 0.05, icy + 0.1], color=cat["deep"], lw=1.8, zorder=6)
            ax.plot([icx, icx + 0.15], [icy + 0.1, icy + 0.22], color=cat["deep"], lw=1.8, zorder=6)
            ax.plot([icx, icx - 0.15], [icy + 0.15, icy + 0.27], color=cat["deep"], lw=1.8, zorder=6)

        elif i == 5:
            ang_deg = 30
            ang_r = np.radians(ang_deg)
            cos_a, sin_a = np.cos(ang_r), np.sin(ang_r)
            
            gh_x, gh_y = icx + 0.1, icy + 0.15
            hx_end = gh_x - 0.65 * cos_a - (-0.65) * sin_a
            ax.plot([gh_x - 0.05 * sin_a, gh_x - 0.65 * cos_a], 
                    [gh_y + 0.05 * cos_a, gh_y - 0.65 * sin_a], color=INK, lw=4, solid_capstyle="round", zorder=5)
            head_rect = patches.Rectangle((gh_x - 0.35, gh_y - 0.15), 0.7, 0.3, angle=ang_deg, rotation_point=(gh_x, gh_y),
                                         facecolor="white", edgecolor=INK, lw=2, zorder=6)
            ax.add_patch(head_rect)
            ax.add_patch(patches.Ellipse((icx - 0.15, icy - 0.35), 0.8, 0.25, facecolor="white", edgecolor=INK, lw=2, zorder=5))
            ax.add_patch(patches.Rectangle((icx - 0.45, icy - 0.45), 0.6, 0.1, facecolor="white", edgecolor=INK, lw=1.5, zorder=5))

    ax.text(0, 5.5, "The External Business Environment", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    save(fig, out)
