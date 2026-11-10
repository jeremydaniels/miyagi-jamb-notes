from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 8.5)
    ax.axis('off')

    # Coordinates for the rectangle
    # Wall is at top: from x = 1.5 to 9.5, rectangle hangs down from y = 6.0
    x_left = 2.5
    x_right = 8.5
    y_wall = 5.8
    y_bottom = 2.2

    # Draw shaded area inside enclosure
    rect = patches.Rectangle((x_left, y_bottom), x_right - x_left, y_wall - y_bottom,
                             facecolor=CREAM, edgecolor='none', zorder=1)
    ax.add_patch(rect)

    # Draw existing wall (thicker, with hatching or hatched block)
    wall_left = 1.0
    wall_right = 10.0
    wall_height = 0.35
    wall_rect = patches.Rectangle((wall_left, y_wall), wall_right - wall_left, wall_height,
                                  facecolor=GREY, edgecolor=INK, lw=1.5, hatch='///', zorder=3)
    ax.add_patch(wall_rect)

    # Label for existing wall
    ax.text((wall_left + wall_right) / 2, y_wall + wall_height + 0.35, "Existing wall",
            ha='center', va='bottom', fontsize=16, color=INK, weight='bold')

    # Draw fence sides (left, bottom, right)
    fence_x = [x_left, x_left, x_right, x_right]
    fence_y = [y_wall, y_bottom, y_bottom, y_wall]
    ax.plot(fence_x, fence_y, color=DEEP['blue'], lw=3.5, solid_capstyle='round', zorder=4)

    # Labels for sides: 'x' on left, 'x' on right, 'y' on bottom
    ax.text(x_left - 0.45, (y_wall + y_bottom) / 2, "x",
            ha='right', va='center', fontsize=18, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    ax.text(x_right + 0.45, (y_wall + y_bottom) / 2, "x",
            ha='left', va='center', fontsize=18, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    ax.text((x_left + x_right) / 2, y_bottom - 0.45, "y",
            ha='center', va='top', fontsize=18, color=INK,
            bbox=dict(fc="white", ec="none", pad=0.2))

    # Main text annotation
    ax.text((x_left + x_right) / 2, 0.4, "Total length of fence = 2x + y",
            ha='center', va='center', fontsize=18, color=INK, weight='bold',
            bbox=dict(fc="white", ec=DEEP['blue'], boxstyle="round,pad=0.5", lw=1.5))

    save(fig, out)
