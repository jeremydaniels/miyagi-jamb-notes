import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(15, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6)
    ax.set_aspect('equal')
    ax.axis('off')

    def draw_computer(cx, cy, label=""):
        # Monitor outer frame
        w, h = 0.8, 0.6
        rect = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                      boxstyle="round,pad=0.04,rounding_size=0.08",
                                      facecolor=BLUE, edgecolor=INK, lw=2, zorder=4)
        ax.add_patch(rect)
        # Screen inner
        sw, sh = 0.62, 0.42
        s_rect = patches.Rectangle((cx - sw/2, cy - sh/2 + 0.04), sw, sh,
                                   facecolor="white", edgecolor=INK, lw=1.2, zorder=5)
        ax.add_patch(s_rect)
        # Stand
        stand_w, stand_h = 0.28, 0.12
        stand = patches.Rectangle((cx - stand_w/2, cy - h/2 - stand_h), stand_w, stand_h,
                                  facecolor=GREY, edgecolor=INK, lw=1.5, zorder=3)
        ax.add_patch(stand)
        base = patches.Rectangle((cx - 0.35, cy - h/2 - stand_h), 0.7, 0.04,
                                 facecolor=INK, edgecolor=INK, lw=1, zorder=3)
        ax.add_patch(base)
        if label:
            ax.text(cx, cy - h/2 - stand_h - 0.25, label, ha="center", va="top",
                    fontsize=14, color=INK)

    # ---------------- 1) STAR TOPOLOGY ----------------
    ax.text(2.5, 5.4, "Star Topology", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    star_center = (2.5, 2.7)
    
    # 4 outer computers
    dist = 1.6
    angles = [45, 135, 225, 315]
    for ang in angles:
        rad = np.radians(ang)
        pc_x = star_center[0] + dist * np.cos(rad)
        pc_y = star_center[1] + dist * np.sin(rad)
        # Radiating line
        ax.plot([star_center[0], pc_x], [star_center[1], pc_y], color=DEEP["blue"], lw=3, zorder=1)
        draw_computer(pc_x, pc_y)

    # Central switch
    sw_w, sw_h = 1.0, 0.65
    switch_box = patches.FancyBboxPatch((star_center[0] - sw_w/2, star_center[1] - sw_h/2), sw_w, sw_h,
                                       boxstyle="round,pad=0.05,rounding_size=0.1",
                                       facecolor=ORANGE, edgecolor=INK, lw=2.2, zorder=6)
    ax.add_patch(switch_box)
    ax.text(star_center[0], star_center[1], "Switch", ha="center", va="center",
            fontsize=14, weight="bold", color=INK, zorder=7)

    # ---------------- 2) BUS TOPOLOGY ----------------
    ax.text(7.5, 5.4, "Bus Topology", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    bus_y = 2.7
    bus_x_start = 5.6
    bus_x_end = 9.4

    # Backbone cable
    ax.plot([bus_x_start, bus_x_end], [bus_y, bus_y], color=DEEP["green"], lw=4, zorder=2)

    # Terminators at both ends
    for tx in [bus_x_start, bus_x_end]:
        term = patches.Rectangle((tx - 0.08, bus_y - 0.35), 0.16, 0.7,
                                 facecolor=DEEP["orange"], edgecolor=INK, lw=2, zorder=5)
        ax.add_patch(term)
    ax.text(bus_x_start - 0.15, bus_y + 0.48, "Terminator", ha="center", va="bottom",
            fontsize=14, color=INK, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(bus_x_end + 0.15, bus_y + 0.48, "Terminator", ha="center", va="bottom",
            fontsize=14, color=INK, bbox=dict(fc="white", ec="none", pad=1))

    # 4 Computers attached via drop lines (2 above, 2 below)
    bus_pcs = [
        (6.3, bus_y + 1.35, bus_y),
        (7.1, bus_y - 1.35, bus_y),
        (7.9, bus_y + 1.35, bus_y),
        (8.7, bus_y - 1.35, bus_y),
    ]
    for pc_x, pc_y, by in bus_pcs:
        # Drop line
        ax.plot([pc_x, pc_x], [by, pc_y], color=INK, lw=2.2, zorder=1)
        # Tap / connection dot on the backbone
        ax.plot(pc_x, by, marker='o', markersize=8, color=INK, zorder=4)
        draw_computer(pc_x, pc_y)

    # Backbone label
    ax.text(7.5, bus_y + 0.15, "Backbone", ha="center", va="bottom",
            fontsize=14, color=INK, bbox=dict(fc="white", ec="none", pad=1), zorder=3)

    # ---------------- 3) RING TOPOLOGY ----------------
    ax.text(12.5, 5.4, "Ring Topology", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    ring_center = (12.5, 2.7)
    r = 1.35

    # Circular connection ring
    ring_circle = patches.Circle(ring_center, r, fill=False, edgecolor=DEEP["lav"], lw=3.5, zorder=1)
    ax.add_patch(ring_circle)

    # 4 Computers positioned in the ring (N, E, S, W)
    ring_angles = [0, 90, 180, 270]
    for ang in ring_angles:
        rad = np.radians(ang)
        pc_x = ring_center[0] + r * np.cos(rad)
        pc_y = ring_center[1] + r * np.sin(rad)
        draw_computer(pc_x, pc_y)

    # Subtle directional arrows to emphasize closed loop / ring flow
    arrow_angles = [45, 135, 225, 315]
    for ang in arrow_angles:
        rad = np.radians(ang)
        ax_pos = ring_center[0] + r * np.cos(rad)
        ay_pos = ring_center[1] + r * np.sin(rad)
        dx = -0.15 * np.sin(rad)
        dy = 0.15 * np.cos(rad)
        ax.annotate('', xy=(ax_pos + dx, ay_pos + dy), xytext=(ax_pos - dx, ay_pos - dy),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["lav"], lw=2.5, mutation_scale=15),
                    zorder=2)

    save(fig, out)
