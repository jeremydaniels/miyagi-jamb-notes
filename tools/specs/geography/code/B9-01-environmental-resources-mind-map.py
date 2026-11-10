from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Title
    ax.text(0, 4.9, "Environmental Resources", fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Center circle
    center_circle = patches.Circle((0, 0), 1.35, facecolor=CREAM, edgecolor=INK, linewidth=2, zorder=3)
    ax.add_patch(center_circle)
    ax.text(0, 0, "Environmental\nResources", fontsize=15, fontweight="bold", ha="center", va="center", color=INK, zorder=4)

    # 5 branches
    # Branches order: Atmospheric (top), Vegetation (top-right), Soil (bottom-right), Minerals (bottom-left), Land (top-left)
    angles_deg = [90, 18, -54, -126, 162]
    categories = [
        {"name": "Atmospheric", "color": BLUE, "deep": DEEP["blue"]},
        {"name": "Vegetation", "color": GREEN, "deep": DEEP["green"]},
        {"name": "Soil", "color": ORANGE, "deep": DEEP["orange"]},
        {"name": "Minerals", "color": PINK, "deep": DEEP["pink"]},
        {"name": "Land", "color": LAV, "deep": DEEP["lav"]}
    ]
    r_node = 3.1
    node_rad = 0.95

    nodes_pos = []
    for deg in angles_deg:
        rad = np.deg2rad(deg)
        nodes_pos.append((r_node * np.cos(rad), r_node * np.sin(rad)))

    # Draw connecting branches
    for (nx, ny), cat in zip(nodes_pos, categories):
        ax.plot([0, nx], [0, ny], color=cat["deep"], lw=3.5, zorder=1)

    # Draw branch circles and labels
    for (nx, ny), cat in zip(nodes_pos, categories):
        c = patches.Circle((nx, ny), node_rad, facecolor=cat["color"], edgecolor=cat["deep"], lw=2.2, zorder=3)
        ax.add_patch(c)
        ax.text(nx, ny, cat["name"], fontsize=14, fontweight="bold", ha="center", va="center", color=INK, zorder=4)

    # Helper function to add icons
    # 1. Atmospheric: Sun and cloud (above node at (0, 3.1))
    # Sun
    sun_c = (0.55, 4.4)
    ax.add_patch(patches.Circle(sun_c, 0.22, facecolor="#FDD835", edgecolor=INK, lw=1.2, zorder=5))
    for a in np.linspace(0, 2*np.pi, 8, endpoint=False):
        dx, dy = np.cos(a), np.sin(a)
        ax.plot([sun_c[0] + 0.26*dx, sun_c[0] + 0.36*dx], [sun_c[1] + 0.26*dy, sun_c[1] + 0.36*dy], color=INK, lw=1.2, zorder=5)
    # Cloud
    cloud_pts = [(-0.6, 4.35), (-0.4, 4.45), (-0.2, 4.35), (-0.35, 4.25), (-0.55, 4.25)]
    for pt in [(-0.55, 4.35, 0.2), (-0.35, 4.45, 0.25), (-0.15, 4.35, 0.2)]:
        ax.add_patch(patches.Circle((pt[0], pt[1]), pt[2], facecolor="white", edgecolor=INK, lw=1.2, zorder=6))
    ax.add_patch(patches.Rectangle((-0.55, 4.15), 0.4, 0.2, facecolor="white", edgecolor="none", zorder=7))
    ax.plot([-0.65, -0.05], [4.15, 4.15], color=INK, lw=1.2, zorder=8)

    # 2. Vegetation: Tree (near (nx, ny) = (2.95, 0.96)) -> place around (4.3, 1.4)
    tx, ty = 4.3, 1.2
    # Trunk
    ax.add_patch(patches.Rectangle((tx - 0.08, ty - 0.4), 0.16, 0.45, facecolor="#8D6E63", edgecolor=INK, lw=1.2, zorder=4))
    # Foliage (triangles or cloud of green)
    ax.add_patch(patches.Polygon([[tx, ty + 0.55], [tx - 0.45, ty], [tx + 0.45, ty]], facecolor="#81C784", edgecolor=INK, lw=1.2, zorder=5))
    ax.add_patch(patches.Polygon([[tx, ty + 0.75], [tx - 0.35, ty + 0.25], [tx + 0.35, ty + 0.25]], facecolor="#A5D6A7", edgecolor=INK, lw=1.2, zorder=6))

    # 3. Soil: Sprouting plant in earth (near (nx, ny) = (1.82, -2.51)) -> place around (2.9, -3.8)
    sx, sy = 2.9, -3.7
    # Earth mound
    arc = patches.Arc((sx, sy - 0.05), 0.9, 0.45, theta1=0, theta2=180, edgecolor=INK, facecolor="#BCAAA4", lw=1.2, zorder=4)
    mound = patches.Polygon([[sx - 0.45, sy - 0.05], [sx - 0.3, sy + 0.15], [sx, sy + 0.2], [sx + 0.3, sy + 0.15], [sx + 0.45, sy - 0.05]], facecolor="#A1887F", edgecolor=INK, lw=1.2, zorder=4)
    ax.add_patch(mound)
    # Sprout stem
    stem_x = np.linspace(sx, sx + 0.05, 20)
    stem_y = np.linspace(sy + 0.2, sy + 0.55, 20)
    ax.plot(stem_x, stem_y, color=DEEP["green"], lw=2, zorder=5)
    # Leaves
    ax.add_patch(patches.Ellipse((sx - 0.12, sy + 0.52), 0.24, 0.12, angle=35, facecolor="#81C784", edgecolor=INK, lw=1.1, zorder=6))
    ax.add_patch(patches.Ellipse((sx + 0.18, sy + 0.56), 0.24, 0.12, angle=-25, facecolor="#81C784", edgecolor=INK, lw=1.1, zorder=6))

    # 4. Minerals: Diamond and oil drum (near (nx, ny) = (-1.82, -2.51)) -> place around (-3.0, -3.7)
    mx, my = -3.2, -3.7
    # Diamond
    dx, dy = mx - 0.4, my + 0.1
    diamond_pts = [[dx, dy + 0.3], [dx + 0.25, dy + 0.1], [dx, dy - 0.3], [dx - 0.25, dy + 0.1]]
    ax.add_patch(patches.Polygon(diamond_pts, facecolor="#E1BEE7", edgecolor=INK, lw=1.2, zorder=4))
    ax.plot([dx - 0.25, dx + 0.25], [dy + 0.1, dy + 0.1], color=INK, lw=1.0, zorder=5)
    ax.plot([dx, dx], [dy + 0.3, dy - 0.3], color=INK, lw=0.9, zorder=5)
    # Oil drum
    ox, oy = mx + 0.45, my - 0.15
    # Drum body
    ax.add_patch(patches.Rectangle((ox - 0.2, oy), 0.4, 0.5, facecolor="#B0BEC5", edgecolor=INK, lw=1.2, zorder=4))
    ax.add_patch(patches.Ellipse((ox, oy + 0.5), 0.4, 0.15, facecolor="#CFD8DC", edgecolor=INK, lw=1.2, zorder=5))
    ax.add_patch(patches.Ellipse((ox, oy), 0.4, 0.15, facecolor="#90A4AE", edgecolor=INK, lw=1.2, zorder=5))
    ax.plot([ox - 0.2, ox + 0.2], [oy + 0.25, oy + 0.25], color=INK, lw=1.0, zorder=5)

    # 5. Land: Mountain and building (near (nx, ny) = (-2.95, 0.96)) -> place around (-4.3, 1.3)
    lx, ly = -4.3, 1.2
    # Mountain
    mount_pts = [[lx - 0.55, ly - 0.3], [lx - 0.1, ly + 0.5], [lx + 0.3, ly - 0.3]]
    ax.add_patch(patches.Polygon(mount_pts, facecolor="#BDBDBD", edgecolor=INK, lw=1.2, zorder=4))
    snow_pts = [[lx - 0.1, ly + 0.5], [lx - 0.2, ly + 0.3], [lx - 0.1, ly + 0.25], [lx + 0.05, ly + 0.32], [lx + 0.1, ly + 0.28], [lx + 0.15, ly + 0.23]]
    # Building
    bx, by = lx + 0.15, ly - 0.3
    ax.add_patch(patches.Rectangle((bx, by), 0.38, 0.55, facecolor="#FFE082", edgecolor=INK, lw=1.2, zorder=5))
    # Windows
    for r in range(3):
        for c_idx in range(2):
            wx = bx + 0.07 + c_idx * 0.15
            wy = by + 0.08 + r * 0.15
            ax.add_patch(patches.Rectangle((wx, wy), 0.08, 0.09, facecolor="#424242", edgecolor="none", zorder=6))

    save(fig, out)
