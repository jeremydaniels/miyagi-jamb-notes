from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-5.0, 5.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Elliptical orbit parameters
    a = 4.6  # semi-major axis (x)
    b = 2.4  # semi-minor axis (y)

    # Draw orbit path
    theta = np.linspace(0, 2 * np.pi, 300)
    orbit_x = a * np.cos(theta)
    orbit_y = b * np.sin(theta)
    ax.plot(orbit_x, orbit_y, color=GREY, linestyle='--', lw=2.0, zorder=1)

    # Counter-clockwise orbit direction arrows
    ax.annotate('', xy=(0.4, -b), xytext=(-0.4, -b),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.2, mutation_scale=18))
    ax.annotate('', xy=(-0.4, b), xytext=(0.4, b),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.2, mutation_scale=18))

    # Draw Sun at center
    sun_radius = 0.8
    sun_halo = patches.Circle((0, 0), sun_radius * 1.35, facecolor=CREAM, edgecolor='none', zorder=2)
    ax.add_patch(sun_halo)
    sun = patches.Circle((0, 0), sun_radius, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, zorder=3)
    ax.add_patch(sun)
    ax.text(0, 0, "Sun", color=INK, fontsize=17, weight='bold', ha='center', va='center', zorder=4)

    # Earth parameters
    earth_r = 0.45
    tilt_deg = 23.5  # axis tilted rightward (towards +x)
    tilt_rad = np.radians(tilt_deg)
    
    dx_axis = np.sin(tilt_rad)
    dy_axis = np.cos(tilt_rad)

    positions = {
        'summer': (-a, 0.0),
        'winter': (a, 0.0),
        'spring': (0.0, b),
        'autumn': (0.0, -b)
    }

    def draw_earth(cx, cy):
        earth_circle = patches.Circle((cx, cy), earth_r, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.0, zorder=5)
        ax.add_patch(earth_circle)

        sun_angle = np.arctan2(-cy, -cx)
        night_angle = sun_angle + np.pi
        wedge = patches.Wedge((cx, cy), earth_r, np.degrees(night_angle - np.pi/2), np.degrees(night_angle + np.pi/2),
                              facecolor=GREY, alpha=0.45, edgecolor='none', zorder=6)
        ax.add_patch(wedge)

        axis_len = 0.8
        x0 = cx - axis_len * dx_axis
        y0 = cy - axis_len * dy_axis
        x1 = cx + axis_len * dx_axis
        y1 = cy + axis_len * dy_axis
        ax.plot([x0, x1], [y0, y1], color=INK, lw=2.0, zorder=7)

        ax.text(x1 + 0.12 * dx_axis, y1 + 0.12 * dy_axis, 'N', fontsize=14, weight='bold',
                ha='center', va='center', color=INK, zorder=8)
        ax.text(x0 - 0.12 * dx_axis, y0 - 0.12 * dy_axis, 'S', fontsize=14, weight='bold',
                ha='center', va='center', color=INK, zorder=8)

        eq_len = earth_r * 0.95
        eq_dx = -dy_axis
        eq_dy = dx_axis
        ax.plot([cx - eq_len * eq_dx, cx + eq_len * eq_dx],
                [cy - eq_len * eq_dy, cy + eq_len * eq_dy],
                color='white', lw=1.5, linestyle=':', zorder=7)

    for pos_key, (px, py) in positions.items():
        draw_earth(px, py)

    bbox_style = dict(facecolor='white', edgecolor=GREY, boxstyle='round,pad=0.4', lw=1.2)

    ax.text(0.0, b + 1.25, "March 21: Spring Equinox",
            fontsize=15, weight='bold', ha='center', va='center', color=INK, bbox=bbox_style, zorder=10)

    ax.text(0.0, -b - 1.25, "September 23: Autumn Equinox",
            fontsize=15, weight='bold', ha='center', va='center', color=INK, bbox=bbox_style, zorder=10)

    ax.text(-a, 1.45, "June 21: Summer Solstice\n(Northern Hemisphere tilted towards sun)",
            fontsize=14.5, weight='bold', ha='center', va='bottom', color=INK, bbox=bbox_style, zorder=10)

    ax.text(a, 1.45, "December 22: Winter Solstice\n(Northern Hemisphere tilted away)",
            fontsize=14.5, weight='bold', ha='center', va='bottom', color=INK, bbox=bbox_style, zorder=10)

    ax.annotate("23.5° tilt", xy=(-a + 0.35, 0.75), xytext=(-a + 1.2, 1.05),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=dict(facecolor='white', edgecolor='none', pad=0.1), zorder=10)

    save(fig, out)
