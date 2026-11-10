from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw(out):
    fig = canvas(9, 6.2)
    ax = fig.add_subplot(111)
    
    # Range and max height geometry
    R = 10.0
    H = 4.0
    
    # Parabolic trajectory: y = 4*H/(R^2) * x * (R - x)
    x = np.linspace(0, R, 200)
    y = 4 * H / (R**2) * x * (R - x)
    
    # Plot ground line
    ax.plot([-0.8, R + 1.2], [0, 0], color=INK, lw=2, zorder=2)
    
    # Trajectory
    ax.plot(x, y, color=DEEP["blue"], lw=3.5, zorder=3)
    
    # Launch angle theta: dy/dx at x=0 is 4*H/R = 1.6
    # Angle theta approx 58 degrees
    theta_deg = np.degrees(np.arctan(4 * H / R))
    u_len = 3.2
    ux = u_len * np.cos(np.radians(theta_deg))
    uy = u_len * np.sin(np.radians(theta_deg))
    
    # Initial velocity vector u
    ax.annotate("", xy=(ux, uy), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18), zorder=4)
    ax.text(ux * 0.7, uy + 0.25, r"$u$", fontsize=16, color=DEEP["orange"], fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=1))
    
    # Components of initial velocity: dashed arrows
    ax.annotate("", xy=(ux, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2, ls="--", mutation_scale=15), zorder=4)
    ax.annotate("", xy=(ux, uy), xytext=(ux, 0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2, ls="--", mutation_scale=15), zorder=4)
    
    ax.text(ux / 2, -0.5, r"$u \cos \theta$", fontsize=14, color=DEEP["orange"], ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(ux + 0.2, uy / 2, r"$u \sin \theta$", fontsize=14, color=DEEP["orange"], ha="left", va="center",
            bbox=dict(fc="white", ec="none", pad=1))
    
    # Angle arc for \theta
    arc_radius = 1.6
    arc = Arc((0, 0), arc_radius * 2, arc_radius * 2, angle=0, theta1=0, theta2=theta_deg,
              color=INK, lw=1.5, zorder=3)
    ax.add_patch(arc)
    ax.text(1.2, 0.45, r"$\theta$", fontsize=15, color=INK, ha="center", va="center")
    
    # Peak of the curve: maximum height H
    x_peak, y_peak = R / 2, H
    ax.plot(x_peak, y_peak, marker="o", markersize=7, color=DEEP["pink"], zorder=5)
    
    # Velocity at peak (purely horizontal)
    v_peak_len = ux
    ax.annotate("", xy=(x_peak + v_peak_len, y_peak), xytext=(x_peak, y_peak),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5, mutation_scale=18), zorder=4)
    ax.text(x_peak + v_peak_len / 2, y_peak + 0.35, r"$u \cos \theta$", fontsize=14, color=DEEP["orange"],
            ha="center", bbox=dict(fc="white", ec="none", pad=1))
    
    # Maximum height H measurement line
    ax.plot([x_peak, x_peak], [0, y_peak], color=GREY, lw=1.5, ls=":", zorder=2)
    # Double-headed arrow for H
    ax.annotate("", xy=(x_peak, y_peak), xytext=(x_peak, 0),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.5, mutation_scale=12), zorder=4)
    ax.text(x_peak - 0.25, y_peak / 2, r"$H$", fontsize=16, color=INK, ha="right", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Bracket for total range R
    y_b = -1.2
    ax.plot([0, R], [y_b, y_b], color=INK, lw=1.5)
    ax.plot([0, 0], [y_b - 0.15, y_b + 0.15], color=INK, lw=1.5)
    ax.plot([R, R], [y_b - 0.15, y_b + 0.15], color=INK, lw=1.5)
    # Dashed drop lines from ground to bracket
    ax.plot([0, 0], [0, y_b], color=GREY, lw=1, ls=":")
    ax.plot([R, R], [0, y_b], color=GREY, lw=1, ls=":")
    ax.text(R / 2, y_b - 0.25, r"Range, $R$", fontsize=15, color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Origin label
    ax.text(0, -0.3, r"$(0,0)$", fontsize=14, color=INK, ha="center", va="top")
    
    # Set display limits & turn off standard frame/spines
    ax.set_xlim(-1.2, R + 1.8)
    ax.set_ylim(-2.0, H + 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    
    save(fig, out)
