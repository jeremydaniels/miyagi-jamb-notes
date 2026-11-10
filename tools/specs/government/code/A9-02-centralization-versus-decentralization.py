from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Titles
    ax.text(3.0, 5.9, "Centralization", fontsize=18, fontweight="bold", color=INK, ha="center")
    ax.text(9.0, 5.9, "Decentralization", fontsize=18, fontweight="bold", color=INK, ha="center")

    # Divider line
    ax.plot([6.0, 6.0], [0.8, 5.8], color=GREY, lw=1.5, linestyle="--")

    # --- LEFT: Centralization ---
    # Center (National Government)
    c_x, c_y = 3.0, 3.2
    c_r = 0.75
    center_circle_left = patches.Circle((c_x, c_y), c_r, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(center_circle_left)
    ax.text(c_x, c_y, "National\nGovernment", fontsize=14, fontweight="bold", color=INK, ha="center", va="center", zorder=4)

    # Surrounding small dots pointing inwards
    n_periph = 7
    periph_r = 2.1
    dot_r = 0.22
    for i in range(n_periph):
        angle = 2 * np.pi * i / n_periph + np.pi / 7
        px = c_x + periph_r * np.cos(angle)
        py = c_y + periph_r * np.sin(angle)
        
        # Outer dot
        p_circle = patches.Circle((px, py), dot_r, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2, zorder=3)
        ax.add_patch(p_circle)
        
        # Arrow pointing inward
        # From edge of dot to edge of center circle
        dx = c_x - px
        dy = c_y - py
        dist = np.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        
        start_x = px + ux * (dot_r + 0.08)
        start_y = py + uy * (dot_r + 0.08)
        end_x = c_x - ux * (c_r + 0.08)
        end_y = c_y - uy * (c_r + 0.08)
        
        ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["orange"], lw=2.0, mutation_scale=14),
                    zorder=2)

    # --- RIGHT: Decentralization ---
    # Center (National Government)
    d_x, d_y = 9.0, 3.2
    center_circle_right = patches.Circle((d_x, d_y), c_r, facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
    ax.add_patch(center_circle_right)
    ax.text(d_x, d_y, "National\nGovernment", fontsize=14, fontweight="bold", color=INK, ha="center", va="center", zorder=4)

    # Intermediate regional/local circles
    n_mid = 4
    mid_dist = 1.6
    mid_r = 0.38
    
    # Angles for 4 intermediate nodes
    mid_angles = [np.pi * 0.25, np.pi * 0.75, np.pi * 1.25, np.pi * 1.75]
    
    for idx, angle in enumerate(mid_angles):
        mx = d_x + mid_dist * np.cos(angle)
        my = d_y + mid_dist * np.sin(angle)
        
        # Intermediate circle
        m_circle = patches.Circle((mx, my), mid_r, facecolor=GREEN, edgecolor=DEEP["green"], lw=2, zorder=3)
        ax.add_patch(m_circle)
        
        # Arrow from center outward to intermediate circle
        dx = mx - d_x
        dy = my - d_y
        dist = np.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        
        start_x = d_x + ux * (c_r + 0.08)
        start_y = d_y + uy * (c_r + 0.08)
        end_x = mx - ux * (mid_r + 0.08)
        end_y = my - uy * (mid_r + 0.08)
        
        ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="-|>", color=DEEP["blue"], lw=2.0, mutation_scale=14),
                    zorder=2)
        
        # Sub-dots branching outward from each intermediate circle
        sub_angles = [angle - 0.38, angle, angle + 0.38]
        sub_dist = 0.95
        sub_r = 0.12
        for s_angle in sub_angles:
            sx = mx + sub_dist * np.cos(s_angle)
            sy = my + sub_dist * np.sin(s_angle)
            
            s_circle = patches.Circle((sx, sy), sub_r, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5, zorder=3)
            ax.add_patch(s_circle)
            
            # Arrow from intermediate circle to sub-dot
            sdx = sx - mx
            sdy = sy - my
            sdist = np.hypot(sdx, sdy)
            sux, suy = sdx / sdist, sdy / sdist
            
            s_start_x = mx + sux * (mid_r + 0.05)
            s_start_y = my + suy * (mid_r + 0.05)
            s_end_x = sx - sux * (sub_r + 0.05)
            s_end_y = sy - suy * (sub_r + 0.05)
            
            ax.annotate("", xy=(s_end_x, s_end_y), xytext=(s_start_x, s_start_y),
                        arrowprops=dict(arrowstyle="-|>", color=DEEP["green"], lw=1.5, mutation_scale=11),
                        zorder=2)

    # Label for Local Units (Left side)
    ax.annotate("Local Units", xy=(1.5, 4.4), xytext=(0.5, 5.2),
                fontsize=14, color=INK, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=5)

    # Label for Local Units (Right side intermediate / terminal)
    ax.annotate("Local Units", xy=(10.5, 4.1), xytext=(10.5, 5.2),
                fontsize=14, color=INK, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=5)

    # Bottom explanations / key notes
    ax.text(3.0, 0.4, "Power and authority flow inward to the center",
            fontsize=14, color=INK, ha="center", style="italic")
    ax.text(9.0, 0.4, "Power and authority disperse outward to local levels",
            fontsize=14, color=INK, ha="center", style="italic")

    save(fig, out)
