import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path
from style import *

def draw(out):
    fig = canvas(9, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-4.8, 4.8)
    ax.set_ylim(-3.8, 4.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0, 3.8, "The CIA Triad", fontsize=20, weight='bold', color=INK, ha='center', va='center')

    # Triangle vertices
    # Top: Confidentiality, Bottom-Left: Integrity, Bottom-Right: Availability
    v_top = np.array([0.0, 2.0])
    v_left = np.array([-2.8, -1.8])
    v_right = np.array([2.8, -1.8])

    # Draw shaded central background triangle
    tri_poly = patches.Polygon([v_top, v_right, v_left], closed=True,
                               facecolor=CREAM, edgecolor=GREY, linewidth=2.0, zorder=1)
    ax.add_patch(tri_poly)

    # Connecting side edges
    ax.plot([v_top[0], v_right[0]], [v_top[1], v_right[1]], color=DEEP["blue"], lw=4, zorder=2)
    ax.plot([v_right[0], v_left[0]], [v_right[1], v_left[1]], color=DEEP["green"], lw=4, zorder=2)
    ax.plot([v_left[0], v_top[0]], [v_left[1], v_top[1]], color=DEEP["orange"], lw=4, zorder=2)

    # Center shield icon representing Information Security
    # Standard shield polygon with explicit closed vertices to avoid Path/Bézier bugs
    cx, cy = 0.0, -0.15
    w, h = 0.85, 1.1

    # Generate smooth shield outline using numpy points
    t = np.linspace(0, np.pi / 2, 25)
    # Right curve from bottom point (cx, cy - h) to top-right corner
    # Right side: vertical line from top down to midway, then curve to bottom
    xr = cx + w * np.cos(t[::-1])
    yr = cy - h + h * 0.9 * (1 - np.sin(t[::-1]))

    # Clean shield contour points:
    # Top flat/slightly dipped edge, straight upper sides, tapering curved lower sides to bottom tip
    shield_pts = [
        [cx, cy + h * 0.65],
        [cx - w, cy + h * 0.75],
        [cx - w, cy + h * 0.1],
        [cx - w * 0.8, cy - h * 0.35],
        [cx - w * 0.45, cy - h * 0.7],
        [cx, cy - h],
        [cx + w * 0.45, cy - h * 0.7],
        [cx + w * 0.8, cy - h * 0.35],
        [cx + w, cy + h * 0.1],
        [cx + w, cy + h * 0.75],
    ]
    outer_shield = patches.Polygon(shield_pts, closed=True, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=4)
    ax.add_patch(outer_shield)

    # Inner shield (inset for textbook 3D/layering look)
    inner_pts = [[cx + (x - cx) * 0.78, cy + (y - cy) * 0.78] for x, y in shield_pts]
    inner_shield = patches.Polygon(inner_pts, closed=True, facecolor='white', edgecolor=DEEP["blue"], lw=1.5, zorder=5)
    ax.add_patch(inner_shield)

    # Padlock icon inside shield (representing Information Security)
    # Shackle
    shackle_arc = patches.Arc((cx, cy + 0.15), width=0.34, height=0.42, theta1=0, theta2=180,
                              color=DEEP["blue"], lw=3.0, zorder=6)
    ax.add_patch(shackle_arc)
    # Lock body
    lock_body = patches.FancyBboxPatch((cx - 0.24, cy - 0.22), 0.48, 0.38,
                                       boxstyle="round,pad=0.04,rounding_size=0.06",
                                       facecolor=DEEP["blue"], edgecolor='none', zorder=6)
    ax.add_patch(lock_body)
    # Keyhole
    key_circle = patches.Circle((cx, cy - 0.05), radius=0.06, facecolor='white', edgecolor='none', zorder=7)
    key_stem = patches.Polygon([[cx - 0.03, cy - 0.15], [cx + 0.03, cy - 0.15],
                                [cx + 0.02, cy - 0.06], [cx - 0.02, cy - 0.06]],
                               facecolor='white', edgecolor='none', zorder=7)
    ax.add_patch(key_circle)
    ax.add_patch(key_stem)

    # Label on/below shield: "Information Security"
    ax.text(0, -1.05, "Information\nSecurity", fontsize=14, weight='bold', color=INK,
            ha='center', va='top', zorder=7,
            bbox=dict(boxstyle="round,pad=0.25", facecolor='white', edgecolor=GREY, lw=1.2))

    # Node circles at vertices
    node_rad = 0.35
    for pt, col, fill in [(v_top, DEEP["orange"], ORANGE),
                          (v_left, DEEP["green"], GREEN),
                          (v_right, DEEP["blue"], BLUE)]:
        ax.add_patch(patches.Circle(pt, radius=node_rad, facecolor=fill, edgecolor=col, lw=2.5, zorder=5))

    # Letters C, I, A inside node circles
    ax.text(v_top[0], v_top[1], "C", fontsize=16, weight='bold', color=INK, ha='center', va='center', zorder=6)
    ax.text(v_left[0], v_left[1], "I", fontsize=16, weight='bold', color=INK, ha='center', va='center', zorder=6)
    ax.text(v_right[0], v_right[1], "A", fontsize=16, weight='bold', color=INK, ha='center', va='center', zorder=6)

    # Labels for three points
    # Top: Confidentiality (Secrecy)
    ax.text(v_top[0], v_top[1] + 0.5, "Confidentiality\n(Secrecy)", fontsize=15, weight='bold',
            color=INK, ha='center', va='bottom',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor=DEEP["orange"], lw=1.5))

    # Bottom Left: Integrity (Accuracy)
    ax.text(v_left[0] - 0.1, v_left[1] - 0.45, "Integrity\n(Accuracy)", fontsize=15, weight='bold',
            color=INK, ha='center', va='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor=DEEP["green"], lw=1.5))

    # Bottom Right: Availability (Accessibility)
    ax.text(v_right[0] + 0.1, v_right[1] - 0.45, "Availability\n(Accessibility)", fontsize=15, weight='bold',
            color=INK, ha='center', va='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor=DEEP["blue"], lw=1.5))

    save(fig, out)
