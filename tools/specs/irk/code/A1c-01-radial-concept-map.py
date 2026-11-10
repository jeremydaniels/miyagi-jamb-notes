from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6.2, 5.8)
    ax.axis('off')

    # Title
    ax.text(0, 5.2, "The Qur'an: A Complete Guide to Life", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # 5 Surrounding Categories
    categories = [
        {"title": "Spiritual", "sub": "(Worship & Belief)", "color": GREEN, "deep": DEEP["green"]},
        {"title": "Moral", "sub": "(Character & Ethics)", "color": PINK, "deep": DEEP["pink"]},
        {"title": "Economic", "sub": "(Wealth & Trade)", "color": ORANGE, "deep": DEEP["orange"]},
        {"title": "Political", "sub": "(Governance & Justice)", "color": BLUE, "deep": DEEP["blue"]},
        {"title": "Socio-Cultural", "sub": "(Family & Community)", "color": LAV, "deep": DEEP["lav"]}
    ]

    # Angles for the 5 categories (distributed symmetrically around center)
    # 90 is top, distribute cleanly
    angles_deg = [90, 18, -54, -126, 162]
    r_nodes = 3.8

    # Draw arrows and nodes
    for i, cat in enumerate(categories):
        rad = np.radians(angles_deg[i])
        nx = r_nodes * np.cos(rad)
        ny = r_nodes * np.sin(rad) - 0.2  # slight offset down for balance

        # Arrow from center towards node
        arrow_start_r = 1.35
        arrow_end_r = 2.45
        sx = arrow_start_r * np.cos(rad)
        sy = arrow_start_r * np.sin(rad) - 0.2
        ex = arrow_end_r * np.cos(rad)
        ey = arrow_end_r * np.sin(rad) - 0.2

        ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                    arrowprops=dict(arrowstyle="-|>", color=cat["deep"], lw=2.5,
                                    mutation_scale=18, shrinkA=0, shrinkB=0))

        # Node Circle / Ellipse
        node_box = patches.FancyBboxPatch((nx - 1.6, ny - 0.65), 3.2, 1.3,
                                          boxstyle="round,pad=0.15,rounding_size=0.6",
                                          fc=cat["color"], ec=cat["deep"], lw=2, zorder=3)
        ax.add_patch(node_box)

        # Labels
        ax.text(nx, ny + 0.16, cat["title"], ha='center', va='center',
                fontsize=15, fontweight='bold', color=INK, zorder=4)
        ax.text(nx, ny - 0.22, cat["sub"], ha='center', va='center',
                fontsize=14, color=INK, zorder=4)

    # Center drawing: Open Qur'an on a wooden stand (Rihal)
    cx, cy = 0.0, -0.2

    # Stand (Rihal) legs crossing
    # Left foot to top right rest
    leg1 = np.array([[-0.75, -0.85], [-0.5, -0.85], [0.55, 0.0], [0.35, 0.0]])
    # Right foot to top left rest
    leg2 = np.array([[0.75, -0.85], [0.5, -0.85], [-0.55, 0.0], [-0.35, 0.0]])

    rihal_color = '#B8860B'  # dark golden / wooden
    rihal_edge = '#7A5200'

    # Draw X-legs
    ax.fill(leg1[:, 0] + cx, leg1[:, 1] + cy, color=CREAM, ec=INK, lw=1.8, zorder=2)
    ax.fill(leg2[:, 0] + cx, leg2[:, 1] + cy, color=ORANGE, ec=INK, lw=1.8, zorder=2)

    # Base cutout details of stand
    ax.plot([-0.7, 0.7], [-0.85 + cy, -0.85 + cy], color=INK, lw=2, zorder=2)

    # Open book pages
    # Left page
    left_page = np.array([
        [-0.03, -0.15],
        [-1.0, 0.35],
        [-0.95, 0.95],
        [-0.03, 0.45]
    ])
    # Right page
    right_page = np.array([
        [0.03, -0.15],
        [1.0, 0.35],
        [0.95, 0.95],
        [0.03, 0.45]
    ])

    # Left lower thickness (book cover edge)
    cover_left = np.array([
        [-0.03, -0.2],
        [-1.04, 0.3],
        [-1.0, 0.35],
        [-0.03, -0.15]
    ])
    cover_right = np.array([
        [0.03, -0.2],
        [1.04, 0.3],
        [1.0, 0.35],
        [0.03, -0.15]
    ])

    ax.fill(cover_left[:, 0] + cx, cover_left[:, 1] + cy, color=DEEP["green"], ec=INK, lw=1.5, zorder=3)
    ax.fill(cover_right[:, 0] + cx, cover_right[:, 1] + cy, color=DEEP["green"], ec=INK, lw=1.5, zorder=3)

    # Book pages
    ax.fill(left_page[:, 0] + cx, left_page[:, 1] + cy, color='white', ec=INK, lw=2, zorder=4)
    ax.fill(right_page[:, 0] + cx, right_page[:, 1] + cy, color='white', ec=INK, lw=2, zorder=4)

    # Spine fold
    ax.plot([cx, cx], [-0.15 + cy, 0.45 + cy], color=INK, lw=2, zorder=5)

    # Text lines on Qur'an pages
    for dy in [0.25, 0.4, 0.55, 0.7]:
        # Left page lines
        lx1, ly1 = -0.82, 0.4 + (dy - 0.25) * 0.7
        lx2, ly2 = -0.18, 0.0 + (dy - 0.25) * 0.7
        ax.plot([lx1 + cx, lx2 + cx], [ly1 + cy, ly2 + cy], color=GREY, lw=1.4, zorder=5)

        # Right page lines
        rx1, ry1 = 0.18, 0.0 + (dy - 0.25) * 0.7
        rx2, ry2 = 0.82, 0.4 + (dy - 0.25) * 0.7
        ax.plot([rx1 + cx, rx2 + cx], [ry1 + cy, ry2 + cy], color=GREY, lw=1.4, zorder=5)

    # Central label for Qur'an
    ax.text(cx, cy - 1.15, "Holy Qur'an\n(on Rihal stand)", ha='center', va='top',
            fontsize=15, fontweight='bold', color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc='white', ec=GREY, lw=1.2))

    save(fig, out)
