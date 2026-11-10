from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Arc, Rectangle

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-4.6, 5.0)

    # Title
    ax.text(0, 4.4, "Geostationary Satellite Orbit", ha="center", va="center", 
            fontsize=17, weight="bold", color=INK)

    # Radii
    r_earth = 1.45
    r_orbit = 4.2
    orbit_squash = 0.35  # Perspective scaling for y-axis

    # Orbit path (elliptical to show it lies in the equatorial plane)
    orbit_ellipse = Ellipse((0, 0), 2*r_orbit, 2*r_orbit * orbit_squash, edgecolor=DEEP["blue"], 
                            facecolor="none", linestyle="--", lw=2.0, zorder=2)
    ax.add_patch(orbit_ellipse)

    # Earth body
    earth_circle = Circle((0, 0), r_earth, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(earth_circle)

    # Continents sketch (stylised patches on Earth)
    c1 = Circle((-0.45, 0.45), 0.5, facecolor=GREEN, edgecolor="none", alpha=0.7, zorder=4)
    c2 = Circle((0.55, 0.35), 0.45, facecolor=GREEN, edgecolor="none", alpha=0.7, zorder=4)
    c3 = Circle((0.1, -0.6), 0.5, facecolor=GREEN, edgecolor="none", alpha=0.7, zorder=4)
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.add_patch(c3)

    # Rotational axis (North Pole to South Pole)
    axis_len = r_earth + 0.6
    ax.plot([0, 0], [-axis_len, axis_len], color=GREY, lw=1.8, linestyle="-.", zorder=5)
    ax.text(0, axis_len + 0.22, "North Pole", ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1.0))
    ax.text(0, -axis_len - 0.22, "South Pole", ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1.0))

    # Equator line across the Earth's surface (ellipse arc)
    equator_front = Arc((0, 0), 2*r_earth, 2*r_earth * orbit_squash, angle=0, theta1=180, theta2=360, 
                        color=DEEP["orange"], lw=3.0, zorder=6)
    ax.add_patch(equator_front)
    equator_back = Arc((0, 0), 2*r_earth, 2*r_earth * orbit_squash, angle=0, theta1=0, theta2=180, 
                       color=DEEP["orange"], lw=1.5, linestyle=":", zorder=4)
    ax.add_patch(equator_back)
    
    # Equator plane line extended slightly outside Earth for clarity
    ax.plot([-r_orbit - 0.3, r_orbit + 0.3], [0, 0], color=GREY, lw=1.0, linestyle=":", zorder=1)
    
    # Equator text label
    ax.text(-2.8, 0.35, "Equatorial plane", ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"), zorder=12)

    # Earth rotation: curved arrow around Earth's equator
    rot_arc = Arc((0, 0), 2*r_earth + 0.4, 2*r_earth*orbit_squash + 0.4, angle=0, theta1=220, theta2=320, 
                  color=DEEP["orange"], lw=3.0, zorder=7)
    ax.add_patch(rot_arc)
    # Arrowhead
    tip_ang = np.radians(322)
    tail_ang = np.radians(318)
    r_rot_x, r_rot_y = r_earth + 0.2, (r_earth + 0.2)*orbit_squash
    tip_x, tip_y = r_rot_x * np.cos(tip_ang), r_rot_y * np.sin(tip_ang)
    tail_x, tail_y = r_rot_x * np.cos(tail_ang), r_rot_y * np.sin(tail_ang)
    ax.annotate("", xy=(tip_x, tip_y), xytext=(tail_x, tail_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.0, mutation_scale=18),
                zorder=8)
    
    # Earth rotation label
    ax.annotate("Earth rotates\nPeriod = 24 hours",
                xy=(0, -0.6), xytext=(-2.6, -1.8),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=12)

    # Satellite placed on the orbital path (at x = r_orbit, y = 0)
    sat_x = r_orbit
    sat_y = 0.0

    # Draw satellite: central bus + solar panels
    body_w, body_h = 0.40, 0.40
    panel_w, panel_h = 0.28, 0.65

    # Solar panels (oriented along y-axis perpendicular to equatorial line)
    rect_top = Rectangle((sat_x - panel_w/2, sat_y + body_h/2), panel_w, panel_h,
                         facecolor=LAV, edgecolor=DEEP["lav"], lw=1.5, zorder=9)
    rect_bottom = Rectangle((sat_x - panel_w/2, sat_y - body_h/2 - panel_h), panel_w, panel_h,
                            facecolor=LAV, edgecolor=DEEP["lav"], lw=1.5, zorder=9)
    # Central body
    rect_body = Rectangle((sat_x - body_w/2, sat_y - body_h/2), body_w, body_h,
                          facecolor=GREY, edgecolor=INK, lw=1.5, zorder=10)
    ax.add_patch(rect_top)
    ax.add_patch(rect_bottom)
    ax.add_patch(rect_body)

    # Satellite label placed on the right side
    ax.annotate("Geostationary satellite\nPeriod = 24 hours\n(directly above equator)",
                xy=(sat_x, sat_y + 0.3), xytext=(sat_x + 0.0, 2.2),
                fontsize=14, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=12)

    # Curved arrow showing satellite revolving in same direction
    rev_arc = Arc((0, 0), 2*r_orbit + 0.6, 2*r_orbit*orbit_squash + 0.6, angle=0, theta1=280, theta2=350,
                  color=DEEP["blue"], lw=3.5, zorder=4)
    ax.add_patch(rev_arc)
    # Arrowhead showing revolution
    rev_tip_ang = np.radians(352)
    rev_tail_ang = np.radians(348)
    rev_r_x, rev_r_y = r_orbit + 0.3, r_orbit*orbit_squash + 0.3
    rev_tip_x, rev_tip_y = rev_r_x * np.cos(rev_tip_ang), rev_r_y * np.sin(rev_tip_ang)
    rev_tail_x, rev_tail_y = rev_r_x * np.cos(rev_tail_ang), rev_r_y * np.sin(rev_tail_ang)
    ax.annotate("", xy=(rev_tip_x, rev_tip_y), xytext=(rev_tail_x, rev_tail_y),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.0, mutation_scale=20),
                zorder=10)

    # Label for satellite revolution arrow
    ax.text(2.8, -2.4, "Satellite revolves\nin same direction", ha="center", va="center",
            fontsize=14, color=INK, bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Bottom summary explanation banner
    ax.text(0, -3.9, "Both rotate in the same direction with a 24-hour period:\nSatellite stays stationary relative to Earth's surface",
            ha="center", va="center", fontsize=14, color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"), zorder=12)

    save(fig, out)
