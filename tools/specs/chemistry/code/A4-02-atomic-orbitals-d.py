from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw_axes_3d(ax, length=2.2):
    # Standard axonometric projection for 3D axes on 2D plane:
    # z: vertical (up)
    # y: horizontal (right)
    # x: coming forward/down-left (at 215 degrees)
    
    # x-axis (projected forward-left)
    angle_x = np.radians(215)
    dx = length * 0.9 * np.cos(angle_x)
    dy = length * 0.9 * np.sin(angle_x)
    ax.annotate('', xy=(dx, dy), xytext=(-dx * 0.45, -dy * 0.45),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5))
    ax.text(dx * 1.15, dy * 1.15, 'x', color=INK, fontsize=14, ha='center', va='center', weight='bold')
    
    # y-axis (horizontal right)
    ax.annotate('', xy=(length, 0), xytext=(-length * 0.45, 0),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5))
    ax.text(length * 1.15, 0, 'y', color=INK, fontsize=14, ha='center', va='center', weight='bold')
    
    # z-axis (vertical up)
    ax.annotate('', xy=(0, length), xytext=(0, -length * 0.45),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5))
    ax.text(0, length * 1.15, 'z', color=INK, fontsize=14, ha='center', va='center', weight='bold')

def draw_s_orbital(ax):
    # Shaded circle with soft radial appearance
    theta = np.linspace(0, 2 * np.pi, 200)
    r = 1.25
    for rad, alpha in zip(np.linspace(1.25, 0.2, 12), np.linspace(0.2, 0.8, 12)):
        ax.fill(rad * np.cos(theta), rad * np.sin(theta), color=BLUE, alpha=alpha, ec='none')
    ax.plot(r * np.cos(theta), r * np.sin(theta), color=DEEP["blue"], lw=2.2)

def draw_dumbbell(ax, angle_rad, length=1.45, max_w=0.62, col_pos=PINK, col_neg=LAV, edge_pos=DEEP["pink"], edge_neg=DEEP["lav"]):
    # Create parametric lobe shape along positive x-axis
    t = np.linspace(0, 1, 120)
    # Tear-drop / orbital lobe shape starting at origin (0, 0)
    w = max_w * np.sin(np.pi * t)**0.85 * (1.0 - 0.15 * t)
    
    x_pos = np.concatenate([length * t, length * t[::-1]])
    y_pos = np.concatenate([w, -w[::-1]])
    
    # Perfectly inverted negative lobe along negative x-axis
    x_neg = -x_pos
    y_neg = -y_pos
    
    # Rotation matrix to align along the desired axis angle
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    R = np.array([[c, -s], [s, c]])
    
    pts_pos = R @ np.vstack([x_pos, y_pos])
    pts_neg = R @ np.vstack([x_neg, y_neg])
    
    # Draw negative lobe then positive lobe
    ax.fill(pts_neg[0], pts_neg[1], color=col_neg, alpha=0.85, ec=edge_neg, lw=2, zorder=3)
    ax.fill(pts_pos[0], pts_pos[1], color=col_pos, alpha=0.85, ec=edge_pos, lw=2, zorder=3)
    
    # Add phase signs (+ and -) centered on each lobe
    pos_center = R @ np.array([length * 0.58, 0])
    neg_center = R @ np.array([-length * 0.58, 0])
    ax.text(pos_center[0], pos_center[1], '+', color=INK, fontsize=16, ha='center', va='center', weight='bold', zorder=4)
    ax.text(neg_center[0], neg_center[1], '–', color=INK, fontsize=16, ha='center', va='center', weight='bold', zorder=4)

def draw(out):
    fig = canvas(14, 4.8)
    
    # 4 subplots side by side
    axes = [fig.add_axes([0.02 + i * 0.245, 0.12, 0.22, 0.76]) for i in range(4)]
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.3, 2.5)
        ax.axis('off')
    
    # Subplot 0: s-orbital
    ax0 = axes[0]
    draw_axes_3d(ax0)
    draw_s_orbital(ax0)
    ax0.plot(0, 0, 'o', color=INK, markersize=4.5, zorder=5)
    ax0.text(0, -2.1, "s-orbital (spherical)", color=INK, fontsize=15, ha='center', va='top', weight='bold')
    
    # Subplot 1: px-orbital (along x-axis, 215 deg)
    ax1 = axes[1]
    draw_axes_3d(ax1)
    # The projected x-axis goes towards angle 215 deg
    draw_dumbbell(ax1, np.radians(215))
    ax1.plot(0, 0, 'o', color=INK, markersize=4.5, zorder=5)
    ax1.text(0, -2.1, "px-orbital", color=INK, fontsize=15, ha='center', va='top', weight='bold')
    
    # Subplot 2: py-orbital (along y-axis, 0 deg)
    ax2 = axes[2]
    draw_axes_3d(ax2)
    draw_dumbbell(ax2, 0)
    ax2.plot(0, 0, 'o', color=INK, markersize=4.5, zorder=5)
    ax2.text(0, -2.1, "py-orbital", color=INK, fontsize=15, ha='center', va='top', weight='bold')
    
    # Subplot 3: pz-orbital (along z-axis, 90 deg)
    ax3 = axes[3]
    draw_axes_3d(ax3)
    draw_dumbbell(ax3, np.pi / 2)
    ax3.plot(0, 0, 'o', color=INK, markersize=4.5, zorder=5)
    ax3.text(0, -2.1, "pz-orbital", color=INK, fontsize=15, ha='center', va='top', weight='bold')
    
    # Annotation for "node at the nucleus" on pz-orbital
    # Placed in the upper-left quadrant to clearly avoid overlapping either lobe
    ax3.annotate("node at the nucleus", xy=(0, 0), xytext=(-1.45, 1.35),
                 fontsize=14, color=INK, weight='medium', ha='center', va='center',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5, connectionstyle="arc3,rad=-0.15"),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", alpha=0.95),
                 zorder=6)
    
    save(fig, out)
