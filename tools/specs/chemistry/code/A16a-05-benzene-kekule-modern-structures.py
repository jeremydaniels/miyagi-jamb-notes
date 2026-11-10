from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 6.2)

    # Title
    ax.text(5, 5.5, "Evolution of the Benzene Structure", fontsize=18, weight="bold", color=INK, ha="center")

    # Geometry helper for regular hexagon
    # Benzene typically drawn with vertical sides or horizontal vertices.
    # Standard: vertices at 30, 90, 150, 210, 270, 330 deg (pointy top/bottom)
    angles = np.radians([90, 30, 330, 270, 210, 150, 90])
    r = 1.6

    # --- Left: Kekulé structure ---
    cx1, cy1 = 2.5, 2.6
    x1 = cx1 + r * np.cos(angles)
    y1 = cy1 + r * np.sin(angles)

    # Outer hexagon
    ax.plot(x1, y1, color=INK, lw=3.5, solid_capstyle="round")

    # Double bonds (alternating on sides 0-1, 2-3, 4-5)
    # Inner hexagon scaled down slightly for double bond segments
    inner_factor = 0.8
    for i in [0, 2, 4]:
        p1 = np.array([x1[i], y1[i]])
        p2 = np.array([x1[i+1], y1[i+1]])
        mid = (p1 + p2) / 2.0
        center = np.array([cx1, cy1])
        # Vector towards center
        inset = (center - mid) * (1 - inner_factor)
        ax.plot([p1[0] + inset[0], p2[0] + inset[0]], 
                [p1[1] + inset[1], p2[1] + inset[1]], 
                color=INK, lw=3, solid_capstyle="round")

    ax.text(cx1, 0.4, "Kekulé structure", fontsize=16, weight="bold", color=INK, ha="center")
    ax.text(cx1, -0.1, "Alternating single and\ndouble bonds", fontsize=14, color=GREY, ha="center")

    # --- Right: Modern structure ---
    cx2, cy2 = 7.5, 2.6
    x2 = cx2 + r * np.cos(angles)
    y2 = cy2 + r * np.sin(angles)

    # Outer hexagon
    ax.plot(x2, y2, color=INK, lw=3.5, solid_capstyle="round")

    # Delocalised circle inside
    circle_r = r * 0.58
    circle = plt.Circle((cx2, cy2), circle_r, fill=False, color=DEEP["blue"], lw=3.5)
    ax.add_patch(circle)

    # Light fill for delocalised cloud
    cloud_fill = plt.Circle((cx2, cy2), circle_r, fill=True, color=BLUE, alpha=0.35, zorder=1)
    ax.add_patch(cloud_fill)

    ax.text(cx2, 0.4, "Modern structure", fontsize=16, weight="bold", color=INK, ha="center")
    ax.text(cx2, -0.1, "Delocalised π-electron\ncloud (ring)", fontsize=14, color=GREY, ha="center")

    # Arrow transition in the middle
    ax.annotate("", xy=(5.5, cy1), xytext=(4.5, cy1),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3, mutation_scale=20))

    save(fig, out)
