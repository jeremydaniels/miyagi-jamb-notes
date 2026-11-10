from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    cx, cy = 5.0, 6.0
    R = 2.8       # Wheel radius
    r = 1.2       # Axle radius
    shaft_r = 0.2 # Shaft radius

    # Title
    ax.text(5.0, 9.4, "Wheel and Axle Machine", fontsize=18, fontweight="bold",
            color=INK, ha="center")

    # --- Wheel (Large Cylinder, Front View) ---
    wheel = patches.Circle((cx, cy), R, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, alpha=0.3, zorder=2)
    ax.add_patch(wheel)
    wheel_edge = patches.Circle((cx, cy), R, fill=False, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(wheel_edge)

    # --- Axle (Small Cylinder, Front View) ---
    axle = patches.Circle((cx, cy), r, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2.5, alpha=0.8, zorder=4)
    ax.add_patch(axle)

    # --- Common Shaft (Cross-section) ---
    shaft = patches.Circle((cx, cy), shaft_r, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=5)
    ax.add_patch(shaft)
    ax.plot(cx, cy, marker='+', color=INK, markersize=8, zorder=6) # Center mark

    # --- Labels for Wheel and Axle ---
    ax.text(cx + R + 0.2, cy + R - 0.5, "Wheel\n(radius R)", fontsize=15, fontweight="bold",
            color=DEEP["blue"], ha="left", va="center", bbox=dict(fc="white", ec="none", pad=1))
    
    ax.text(cx - r - 0.2, cy + r + 0.8, "Axle\n(radius r)", fontsize=15, fontweight="bold",
            color=DEEP["orange"], ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1))

    # --- Radius 'R' Arrow ---
    theta_R = np.radians(35)
    rx_wheel = cx + R * np.cos(theta_R)
    ry_wheel = cy + R * np.sin(theta_R)
    ax.annotate("", xy=(rx_wheel, ry_wheel), xytext=(cx, cy),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2), zorder=6)
    ax.text(cx + 0.5 * R * np.cos(theta_R) - 0.1, cy + 0.5 * R * np.sin(theta_R) + 0.2,
            "R", fontsize=16, fontweight="bold", color=DEEP["blue"], zorder=7,
            bbox=dict(fc="white", ec="none", pad=1))

    # --- Radius 'r' Arrow ---
    theta_r = np.radians(145)
    rx_axle = cx + r * np.cos(theta_r)
    ry_axle = cy + r * np.sin(theta_r)
    ax.annotate("", xy=(rx_axle, ry_axle), xytext=(cx, cy),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2), zorder=6)
    ax.text(cx + 0.5 * r * np.cos(theta_r) - 0.2, cy + 0.5 * r * np.sin(theta_r) - 0.3,
            "r", fontsize=16, fontweight="bold", color=DEEP["orange"], zorder=7,
            bbox=dict(fc="white", ec="none", pad=1))

    # --- Effort Rope (Wrapped on Right) ---
    rope_wheel_x = cx + R
    ax.plot([rope_wheel_x, rope_wheel_x], [cy, 2.5], color=INK, lw=2.5, zorder=1)
    
    # Effort Arrow
    ax.annotate("", xy=(rope_wheel_x, 1.0), xytext=(rope_wheel_x, 2.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=3.5, mutation_scale=20), zorder=8)
    ax.text(rope_wheel_x + 0.3, 1.75, "Effort (E)", fontsize=16, fontweight="bold",
            color=DEEP["blue"], va="center", bbox=dict(fc="white", ec="none", pad=2))

    # --- Load Rope (Wrapped on Left) ---
    rope_axle_x = cx - r
    load_top_y = 3.2
    ax.plot([rope_axle_x, rope_axle_x], [cy, load_top_y], color=INK, lw=2.5, zorder=1)

    # Load Weight Box
    load_w, load_h = 1.8, 1.4
    load_rect = patches.Rectangle((rope_axle_x - load_w / 2, load_top_y - load_h), load_w, load_h,
                                  facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=8)
    ax.add_patch(load_rect)
    ax.text(rope_axle_x, load_top_y - load_h / 2, "Load (L)", fontsize=15, fontweight="bold",
            color=INK, ha="center", va="center", zorder=9)

    save(fig, out)
