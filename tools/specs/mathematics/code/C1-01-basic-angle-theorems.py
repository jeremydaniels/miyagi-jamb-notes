from style import *
import numpy as np
import matplotlib.patches as patches

def draw_arc(ax, center, r, theta1, theta2, color=INK, fill=None, alpha=0.3):
    cx, cy = center
    if fill:
        wedge = patches.Wedge(center, r, theta1, theta2, facecolor=fill, edgecolor=color, lw=1.5, alpha=alpha)
        ax.add_patch(wedge)
    arc = patches.Arc(center, 2*r, 2*r, angle=0, theta1=theta1, theta2=theta2, color=color, lw=1.5)
    ax.add_patch(arc)

def draw(out):
    fig = canvas(14, 5.2)
    
    # Diagram 1: Angles on a straight line
    ax1 = fig.add_axes([0.03, 0.1, 0.29, 0.8])
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-1.8, 2.5)
    
    # Horizontal line
    ax1.plot([-2.2, 2.2], [0, 0], color=INK, lw=2.5)
    # Diagonal line cutting it
    angle_deg = 60
    rad = np.deg2rad(angle_deg)
    ax1.plot([0, 1.8 * np.cos(rad)], [0, 1.8 * np.sin(rad)], color=DEEP['blue'], lw=2.5)
    
    # Arcs
    draw_arc(ax1, (0, 0), 0.7, 0, angle_deg, color=DEEP['blue'], fill=BLUE, alpha=0.35)
    draw_arc(ax1, (0, 0), 0.55, angle_deg, 180, color=DEEP['orange'], fill=ORANGE, alpha=0.35)
    
    # Labels a and b
    ax1.text(0.45 * np.cos(np.deg2rad(30)), 0.45 * np.sin(np.deg2rad(30)) + 0.05, "a", 
             fontsize=16, color=INK, ha='center', va='center', weight='bold')
    ax1.text(0.35 * np.cos(np.deg2rad(120)), 0.35 * np.sin(np.deg2rad(120)) + 0.05, "b", 
             fontsize=16, color=INK, ha='center', va='center', weight='bold')
    
    # Bottom label
    ax1.text(0, -1.0, "$a + b = 180^\\circ$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3', lw=1.2))

    # Diagram 2: Angles at a point
    ax2 = fig.add_axes([0.36, 0.1, 0.29, 0.8])
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-1.8, 2.5)
    
    # Central point and four rays
    angles = [20, 110, 200, 290, 380]
    labels = ['p', 'q', 'r', 's']
    colors = [BLUE, GREEN, ORANGE, PINK]
    deep_colors = [DEEP['blue'], DEEP['green'], DEEP['orange'], DEEP['pink']]
    
    for i in range(4):
        a1 = angles[i]
        a2 = angles[i+1]
        mid = (a1 + a2) / 2.0
        # Draw ray
        rx = 1.9 * np.cos(np.deg2rad(a1))
        ry = 1.9 * np.sin(np.deg2rad(a1))
        ax2.plot([0, rx], [0, ry], color=INK, lw=2.2)
        # Draw arc & fill
        draw_arc(ax2, (0, 0), 0.65, a1, a2, color=deep_colors[i], fill=colors[i], alpha=0.35)
        # Label
        lx = 0.95 * np.cos(np.deg2rad(mid))
        ly = 0.95 * np.sin(np.deg2rad(mid))
        ax2.text(lx, ly, labels[i], fontsize=16, color=INK, ha='center', va='center', weight='bold')
    
    # Center dot
    ax2.scatter([0], [0], color=INK, s=30, zorder=5)
    
    # Bottom label
    ax2.text(0, -1.0, "$p + q + r + s = 360^\\circ$", fontsize=16, color=INK, ha='center', va='center',
             bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3', lw=1.2))

    # Diagram 3: Vertically opposite angles
    ax3 = fig.add_axes([0.69, 0.1, 0.29, 0.8])
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_xlim(-2.5, 2.5)
    ax3.set_ylim(-1.8, 2.5)
    
    # X shape lines
    ang_x = 40
    rad_x = np.deg2rad(ang_x)
    L = 2.1
    ax3.plot([-L*np.cos(rad_x), L*np.cos(rad_x)], [-L*np.sin(rad_x), L*np.sin(rad_x)], color=INK, lw=2.2)
    ax3.plot([-L*np.cos(rad_x), L*np.cos(rad_x)], [L*np.sin(rad_x), -L*np.sin(rad_x)], color=INK, lw=2.2)
    
    # Arcs for top/bottom (x)
    draw_arc(ax3, (0, 0), 0.6, ang_x, 180 - ang_x, color=DEEP['green'], fill=GREEN, alpha=0.35)
    draw_arc(ax3, (0, 0), 0.6, 180 + ang_x, 360 - ang_x, color=DEEP['green'], fill=GREEN, alpha=0.35)
    
    # Arcs for left/right (y)
    draw_arc(ax3, (0, 0), 0.75, 360 - ang_x, 360 + ang_x, color=DEEP['pink'], fill=PINK, alpha=0.35)
    draw_arc(ax3, (0, 0), 0.75, 180 - ang_x, 180 + ang_x, color=DEEP['pink'], fill=PINK, alpha=0.35)
    
    # Labels
    ax3.text(0, 0.9, "x", fontsize=16, color=INK, ha='center', va='center', weight='bold')
    ax3.text(0, -0.9, "x", fontsize=16, color=INK, ha='center', va='center', weight='bold')
    ax3.text(1.1, 0, "y", fontsize=16, color=INK, ha='center', va='center', weight='bold')
    ax3.text(-1.1, 0, "y", fontsize=16, color=INK, ha='center', va='center', weight='bold')
    
    # Center dot
    ax3.scatter([0], [0], color=INK, s=25, zorder=5)
    
    # Bottom label
    ax3.text(0, -1.5, "Vertically opposite\nangles are equal", fontsize=14.5, color=INK, ha='center', va='center',
             bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3', lw=1.2))

    save(fig, out)
