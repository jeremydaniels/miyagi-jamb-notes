from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(11, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-6.8, 2.2)

    # Ceiling / Pivot mount
    ax.plot([-3.0, 3.0], [1.2, 1.2], color=INK, lw=2.5)
    # Hatch lines for ceiling
    for x in np.linspace(-2.8, 2.8, 15):
        ax.plot([x, x + 0.3], [1.2, 1.5], color=GREY, lw=1.5)

    pivot = (0, 1.2)
    L = 4.8
    # Use wider swing angle (40 deg) so extremes spread well apart (x = +/- 3.08)
    theta_deg = 40
    theta = np.radians(theta_deg)

    # Positions
    x_left = -L * np.sin(theta)
    y_left = pivot[1] - L * np.cos(theta)

    x_mid = 0.0
    y_mid = pivot[1] - L

    x_right = L * np.sin(theta)
    y_right = pivot[1] - L * np.cos(theta)

    # Trajectory arc (dashed)
    arc_angles = np.linspace(-theta - 0.08, theta + 0.08, 100)
    arc_x = pivot[0] + L * np.sin(arc_angles)
    arc_y = pivot[1] - L * np.cos(arc_angles)
    ax.plot(arc_x, arc_y, ls="--", color=GREY, lw=1.8, zorder=1)

    # Reference vertical dashed line for center equilibrium
    ax.plot([0, 0], [pivot[1], y_mid], ls=":", color=GREY, lw=1.2, zorder=1)

    # Strings
    ax.plot([pivot[0], x_left], [pivot[1], y_left], color=DEEP["blue"], lw=2, zorder=2)
    ax.plot([pivot[0], x_mid], [pivot[1], y_mid], color=DEEP["orange"], lw=2.2, zorder=2)
    ax.plot([pivot[0], x_right], [pivot[1], y_right], color=DEEP["blue"], lw=2, zorder=2)

    # Pivot point
    pivot_circle = plt.Circle(pivot, 0.12, fc=INK, ec=INK, zorder=6)
    ax.add_patch(pivot_circle)

    # Bobs
    r_bob = 0.42
    bob_left = plt.Circle((x_left, y_left), r_bob, fc=BLUE, ec=DEEP["blue"], lw=2.5, zorder=5)
    bob_mid = plt.Circle((x_mid, y_mid), r_bob, fc=ORANGE, ec=DEEP["orange"], lw=2.5, zorder=5)
    bob_right = plt.Circle((x_right, y_right), r_bob, fc=BLUE, ec=DEEP["blue"], lw=2.5, zorder=5)
    ax.add_patch(bob_left)
    ax.add_patch(bob_mid)
    ax.add_patch(bob_right)

    # Labels for extremes and center (placed with plenty of horizontal space and staggered slightly vertically)
    bbox_style = dict(boxstyle="round,pad=0.4", fc="white", ec=GREY, lw=1.2)

    # Left extreme
    ax.text(x_left - 0.6, y_left - 0.75, "Left extreme\nMax PE, KE = 0", 
            ha="center", va="top", fontsize=14.5, color=INK, bbox=bbox_style)

    # Center (lowest point) - placed beneath the lowest bob
    ax.text(x_mid, y_mid - 0.85, "Center (lowest point)\nMax KE, PE = 0", 
            ha="center", va="top", fontsize=14.5, color=INK, bbox=bbox_style)

    # Right extreme
    ax.text(x_right + 0.6, y_right - 0.75, "Right extreme\nMax PE, KE = 0", 
            ha="center", va="top", fontsize=14.5, color=INK, bbox=bbox_style)

    # Diagram title
    ax.text(0, 1.85, "Conservation of Energy in a Simple Pendulum", 
            ha="center", va="center", fontsize=17, weight="bold", color=INK)

    save(fig, out)
