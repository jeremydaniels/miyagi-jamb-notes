from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9.5)
    ax.axis("off")

    # Titles and Section Headings
    ax.text(6, 9.0, "Astigmatism and Corneal Curvature", ha="center", va="center", 
            fontsize=16, weight="bold", color=INK)

    # Coordinates for top charts
    cx_left, cy_left = 3.2, 5.0
    cx_right, cy_right = 8.8, 5.0
    r_inner, r_outer = 0.25, 1.85
    angles_deg = np.linspace(0, 180, 13)  # 13 radial spokes from 0 to 180 degrees

    # 1. Left Chart: Normal Vision
    # Top of spoke ends at cy_left + r_outer = 5.0 + 1.85 = 6.85. Place label comfortably above at 7.6.
    ax.text(cx_left, 7.6, "normal vision", ha="center", va="center", 
            fontsize=14, weight="bold", color=INK)
    
    # Outer semicircular arc for reference
    theta_arc = np.linspace(0, np.pi, 100)
    ax.plot(cx_left + r_outer * np.cos(theta_arc), cy_left + r_outer * np.sin(theta_arc), 
            color=GREY, lw=1.5, ls="--", alpha=0.5)
    ax.plot([cx_left - r_outer, cx_left + r_outer], [cy_left, cy_left], 
            color=GREY, lw=1.5, ls="--", alpha=0.5)

    for deg in angles_deg:
        rad = np.radians(deg)
        x0 = cx_left + r_inner * np.cos(rad)
        y0 = cy_left + r_inner * np.sin(rad)
        x1 = cx_left + r_outer * np.cos(rad)
        y1 = cy_left + r_outer * np.sin(rad)
        ax.plot([x0, x1], [y0, y1], color=INK, lw=2.5, solid_capstyle="round")

    # Center dot
    ax.plot(cx_left, cy_left, 'o', color=INK, markersize=5)
    ax.text(cx_left, 4.4, "All lines appear equally\nsharp and black", ha="center", va="top",
            fontsize=11.5, color=INK, style="italic")

    # 2. Right Chart: Astigmatism
    ax.text(cx_right, 7.6, "astigmatism", ha="center", va="center", 
            fontsize=14, weight="bold", color=INK)

    ax.plot(cx_right + r_outer * np.cos(theta_arc), cy_right + r_outer * np.sin(theta_arc), 
            color=GREY, lw=1.5, ls="--", alpha=0.5)
    ax.plot([cx_right - r_outer, cx_right + r_outer], [cy_right, cy_right], 
            color=GREY, lw=1.5, ls="--", alpha=0.5)

    for deg in angles_deg:
        rad = np.radians(deg)
        x0 = cx_right + r_inner * np.cos(rad)
        y0 = cy_right + r_inner * np.sin(rad)
        x1 = cx_right + r_outer * np.cos(rad)
        y1 = cy_right + r_outer * np.sin(rad)

        # Vertical is 90 deg: sharp and black.
        # Deviation towards horizontal (0 or 180) becomes blurred and grey.
        dev = abs(deg - 90) / 90.0
        
        if dev < 0.1:
            # Vertical line: sharp and black
            ax.plot([x0, x1], [y0, y1], color=INK, lw=2.8, solid_capstyle="round")
        else:
            # Blurred and grey
            blur_w = 2.0 + dev * 5.5
            blur_alpha = max(0.2, 0.85 - 0.65 * dev)
            ax.plot([x0, x1], [y0, y1], color=GREY, lw=blur_w, alpha=blur_alpha, solid_capstyle="round")
            ax.plot([x0, x1], [y0, y1], color=INK, lw=1.0, alpha=0.25 * (1 - dev), solid_capstyle="round")

    ax.plot(cx_right, cy_right, 'o', color=INK, markersize=5)
    ax.text(cx_right, 4.4, "Vertical lines sharp;\nhorizontal and slanting lines blurred", 
            ha="center", va="top", fontsize=11.5, color=INK, style="italic")

    # Divider line
    ax.plot([1.2, 10.8], [3.4, 3.4], color=GREY, lw=1, ls=":")

    # 3. Bottom Section: Cornea Shapes Comparison
    # Perfectly round cornea (left)
    cx_c1, cy_c1 = 3.2, 1.8
    circle_cornea = patches.Circle((cx_c1, cy_c1), 0.8, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5)
    ax.add_patch(circle_cornea)
    
    # Curvature grid lines on sphere (football)
    arc_theta = np.linspace(-np.pi/2, np.pi/2, 50)
    ax.plot(cx_c1 + 0.4 * np.cos(arc_theta), cy_c1 + 0.8 * np.sin(arc_theta), color=DEEP["blue"], lw=1.2, ls="--")
    ax.plot([cx_c1 - 0.8, cx_c1 + 0.8], [cy_c1, cy_c1], color=DEEP["blue"], lw=1.2, ls="--")

    ax.text(cx_c1, 0.7, "evenly curved cornea", ha="center", va="top", 
            fontsize=13, weight="bold", color=INK)
    ax.text(cx_c1, 0.35, "(like a football)", ha="center", va="top", 
            fontsize=11.5, color=INK)

    # Unevenly curved cornea (right)
    cx_c2, cy_c2 = 8.8, 1.8
    ellipse_cornea = patches.Ellipse((cx_c2, cy_c2), width=1.1, height=1.7, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5)
    ax.add_patch(ellipse_cornea)
    
    # Curvature grid lines on ellipse (rugby ball)
    ax.plot(cx_c2 + 0.25 * np.cos(arc_theta), cy_c2 + 0.85 * np.sin(arc_theta), color=DEEP["orange"], lw=1.2, ls="--")
    ax.plot([cx_c2 - 0.55, cx_c2 + 0.55], [cy_c2, cy_c2], color=DEEP["orange"], lw=1.2, ls="--")

    ax.text(cx_c2, 0.7, "unevenly curved cornea", ha="center", va="top", 
            fontsize=13, weight="bold", color=INK)
    ax.text(cx_c2, 0.35, "(like a rugby ball)", ha="center", va="top", 
            fontsize=11.5, color=INK)

    save(fig, out)
