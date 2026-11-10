from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Define vertical sections:
    # 1. ATMOSPHERE: y = 6.7 to 9.6
    # 2. HYDROSPHERE: y = 3.65 to 6.5
    # 3. LITHOSPHERE: y = 0.6 to 3.45

    # 1. ATMOSPHERE
    sky = Rectangle((0.8, 6.7), 10.4, 2.9, facecolor="#EBF4FA", edgecolor=DEEP["blue"], linewidth=2, zorder=1)
    ax.add_patch(sky)

    # Stylized clouds in atmosphere
    def draw_cloud(cx, cy, s=1.0):
        circles = [
            (cx - 0.4*s, cy, 0.3*s),
            (cx - 0.15*s, cy + 0.2*s, 0.4*s),
            (cx + 0.25*s, cy + 0.15*s, 0.35*s),
            (cx + 0.5*s, cy, 0.28*s),
            (cx, cy - 0.1*s, 0.35*s)
        ]
        for x, y, r in circles:
            c = Circle((x, y), r, facecolor="white", edgecolor="#D0E2EC", lw=1.5, zorder=2)
            ax.add_patch(c)

    draw_cloud(2.2, 8.2, 0.85)
    draw_cloud(4.5, 7.5, 0.65)

    # Title
    ax.text(1.2, 9.1, "Atmosphere (gaseous mixture)", fontsize=16, fontweight="bold", color=INK, zorder=4)

    # Atmosphere Pie Chart
    # Angles: start at 90 deg and go counterclockwise
    # N2: 78% = 280.8° -> 90° to 370.8° (equiv. 10.8°)
    # O2: 21% = 75.6°  -> 10.8° to 86.4°
    # Other: 1% = 3.6° -> 86.4° to 90.0°
    # Let's set it cleanly:
    # N2: 0° to 280.8° (facing right, bottom, left)
    # O2 (21%): 280.8° to 356.4° (in quadrant 4, pointing down-right / right)
    # Let's instead start O2 at 0° to 75.6° (upper right quadrant) for easy labeling!
    # O2 (21%): 0° to 75.6° (midpoint 37.8° -> top-right quadrant)
    # Other (1%): 75.6° to 79.2°
    # N2 (78%): 79.2° to 360.0° (midpoint 219.6° -> lower-left)
    pie1_cx, pie1_cy, pie1_r = 8.6, 8.15, 1.05
    w_o2 = Wedge((pie1_cx, pie1_cy), pie1_r, 0.0, 75.6, facecolor=PINK, edgecolor="white", lw=2, zorder=3)
    w_oth = Wedge((pie1_cx, pie1_cy), pie1_r, 75.6, 79.2, facecolor=GREY, edgecolor="white", lw=2, zorder=3)
    w_n2 = Wedge((pie1_cx, pie1_cy), pie1_r, 79.2, 360.0, facecolor=BLUE, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(w_n2)
    ax.add_patch(w_o2)
    ax.add_patch(w_oth)

    # N2 label inside the large blue sector (centroid around theta = 219.6°)
    ax.text(pie1_cx - 0.25, pie1_cy - 0.25, "78% N₂", fontsize=15, fontweight="bold", color=INK, ha="center", va="center", zorder=4)

    # O2 label clearly pointing to pink sector (midpoint angle = 37.8°)
    rad_o2 = np.radians(37.8)
    o2_pt_x = pie1_cx + 0.65 * pie1_r * np.cos(rad_o2)
    o2_pt_y = pie1_cy + 0.65 * pie1_r * np.sin(rad_o2)
    ax.annotate("21% O₂", xy=(o2_pt_x, o2_pt_y), xytext=(pie1_cx + 1.45, pie1_cy + 0.65),
                fontsize=15, fontweight="bold", color=INK, ha="left", va="center",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none"),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=4)

    # 2. HYDROSPHERE
    ocean = Rectangle((0.8, 3.65), 10.4, 2.85, facecolor="#D9EAF7", edgecolor=DEEP["blue"], linewidth=2, zorder=1)
    ax.add_patch(ocean)

    # Surface waves
    x_waves = np.linspace(0.8, 11.2, 200)
    y_waves = 6.4 + 0.07 * np.sin(x_waves * 8)
    ax.plot(x_waves, y_waves, color=DEEP["blue"], lw=2, zorder=2)

    # Deep water tint band
    ocean_deep = Rectangle((0.8, 3.65), 10.4, 1.8, facecolor="#C4DFFA", edgecolor="none", zorder=1)
    ax.add_patch(ocean_deep)

    # Subtle wave ripples
    for wy in [4.3, 5.2]:
        w_x = np.linspace(1.5, 6.0, 100)
        w_y = wy + 0.04 * np.sin(w_x * 6)
        ax.plot(w_x, w_y, color="#B3D4F5", lw=1.5, zorder=2)

    # Title
    ax.text(1.2, 5.9, "Hydrosphere (water and dissolved salts)", fontsize=16, fontweight="bold", color=INK, zorder=4)

    # Ocean chemical composition formula
    ax.text(4.2, 4.75, r"$\mathbf{H_2O\ +\ NaCl}$", fontsize=18, fontweight="bold", color=DEEP["blue"], zorder=4,
            ha="center", bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=DEEP["blue"], lw=1.5))
    ax.text(4.2, 4.1, "(Major components: water & dissolved salts)", fontsize=14, color=INK, ha="center", zorder=4)

    # 3. LITHOSPHERE
    litho = Rectangle((0.8, 0.6), 10.4, 2.85, facecolor="#F5EFEB", edgecolor="#8B5A2B", linewidth=2, zorder=1)
    ax.add_patch(litho)

    # Strata lines
    x_rock = np.linspace(0.8, 11.2, 150)
    y_rock1 = 2.4 + 0.06 * np.sin(x_rock * 4) + 0.03 * np.cos(x_rock * 9)
    y_rock2 = 1.4 + 0.05 * np.cos(x_rock * 5) + 0.04 * np.sin(x_rock * 7)
    ax.plot(x_rock, y_rock1, color="#D7C4B7", lw=2, zorder=2)
    ax.plot(x_rock, y_rock2, color="#D7C4B7", lw=2, zorder=2)

    # Small rock symbols
    for rx, ry, s in [(2.0, 1.8, 0.15), (3.2, 1.0, 0.2), (1.5, 0.9, 0.12), (4.5, 2.0, 0.18), (5.5, 1.2, 0.14)]:
        rect = Rectangle((rx, ry), s*2, s, facecolor="#C4AEA0", edgecolor="#8B5A2B", lw=1, zorder=2)
        ax.add_patch(rect)

    # Title
    ax.text(1.2, 2.9, "Lithosphere (solid silicate rocks)", fontsize=16, fontweight="bold", color=INK, zorder=4)

    # Lithosphere Pie Chart
    # 47% Oxygen, 28% Silicon, 25% Others
    pie2_cx, pie2_cy, pie2_r = 8.6, 2.0, 1.05
    # Oxygen wedge (47% = 169.2 deg, from 0 to 169.2)
    w_ox = Wedge((pie2_cx, pie2_cy), pie2_r, 0, 169.2, facecolor=PINK, edgecolor="white", lw=2, zorder=3)
    # Silicon wedge (28% = 100.8 deg, from 169.2 to 270 deg)
    w_si = Wedge((pie2_cx, pie2_cy), pie2_r, 169.2, 270.0, facecolor=ORANGE, edgecolor="white", lw=2, zorder=3)
    # Others wedge (25% = 90 deg, from 270 to 360 deg)
    w_oth2 = Wedge((pie2_cx, pie2_cy), pie2_r, 270.0, 360.0, facecolor=GREY, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(w_ox)
    ax.add_patch(w_si)
    ax.add_patch(w_oth2)

    # Labels for Lithosphere Pie
    ax.text(pie2_cx - 0.1, pie2_cy + 0.45, "47% Oxygen", fontsize=14, fontweight="bold", color=INK, ha="center", zorder=4)
    ax.text(pie2_cx - 0.6, pie2_cy - 0.45, "28% Silicon", fontsize=14, fontweight="bold", color=INK, ha="center", zorder=4)
    ax.text(pie2_cx + 0.5, pie2_cy - 0.45, "25% Other", fontsize=14, color=INK, ha="center", zorder=4)

    save(fig, out)
