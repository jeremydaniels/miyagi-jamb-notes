from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(15, 6.5)
    
    # Left subplot: Tetravalency (Methane)
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_xlim(-2.8, 2.8)
    ax1.set_ylim(-2.8, 2.6)
    ax1.set_aspect('equal')
    ax1.axis('off')
    
    # Middle subplot: Catenation: Straight chain (Pentane)
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_xlim(-1.1, 5.1)
    ax2.set_ylim(-2.8, 2.6)
    ax2.set_aspect('equal')
    ax2.axis('off')
    
    # Right subplot: Catenation: Ring structure (Cyclohexane)
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_xlim(-2.8, 2.8)
    ax3.set_ylim(-2.8, 2.6)
    ax3.set_aspect('equal')
    ax3.axis('off')
    
    atom_kwargs = dict(ha='center', va='center', zorder=4)
    c_bbox = dict(boxstyle='circle,pad=0.25', fc=CREAM, ec=DEEP['orange'], lw=2)
    h_bbox = dict(boxstyle='circle,pad=0.2', fc='white', ec=DEEP['blue'], lw=1.5)
    
    label_y = -2.5
    
    # --- 1. Methane (Tetrahedral representation) ---
    c_pos = np.array([0.0, 0.1])
    h_top = np.array([0.0, 1.6])
    h_left = np.array([-1.4, -0.6])
    h_right_wedge = np.array([1.2, -0.7])
    h_right_dash = np.array([1.4, 0.5])
    
    # Top bond (normal)
    ax1.plot([c_pos[0], h_top[0]], [c_pos[1], h_top[1]], color=INK, lw=2.5, zorder=2)
    # Left bond (normal)
    ax1.plot([c_pos[0], h_left[0]], [c_pos[1], h_left[1]], color=INK, lw=2.5, zorder=2)
    # Wedge bond (solid triangle)
    wedge_x = [c_pos[0], h_right_wedge[0] - 0.15, h_right_wedge[0] + 0.15]
    wedge_y = [c_pos[1], h_right_wedge[1] + 0.1, h_right_wedge[1] - 0.1]
    ax1.fill(wedge_x, wedge_y, color=INK, zorder=2)
    # Dash bond (dashed line)
    ax1.plot([c_pos[0], h_right_dash[0]], [c_pos[1], h_right_dash[1]], color=INK, lw=3, ls=(0, (3, 3)), zorder=2)
    
    # Draw C and H atoms
    ax1.text(c_pos[0], c_pos[1], 'C', fontsize=18, fontweight='bold', color=INK, bbox=c_bbox, **atom_kwargs)
    for hx, hy in [h_top, h_left, h_right_wedge, h_right_dash]:
        ax1.text(hx, hy, 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
        
    ax1.text(0.0, label_y, "Tetravalency (4 bonds)", fontsize=15, ha='center', va='center', fontweight='bold', color=INK)

    # --- 2. Straight chain (5 carbons: Pentane) ---
    c_x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    c_y = 0.1
    
    # Draw C-C bonds
    for i in range(4):
        ax2.plot([c_x[i], c_x[i+1]], [c_y, c_y], color=INK, lw=2.5, zorder=2)
        
    # Draw C-H bonds
    for x in c_x:
        ax2.plot([x, x], [c_y, c_y + 1.25], color=INK, lw=2, zorder=2)
        ax2.plot([x, x], [c_y, c_y - 1.25], color=INK, lw=2, zorder=2)
        ax2.text(x, c_y + 1.25, 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
        ax2.text(x, c_y - 1.25, 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
        
    # End hydrogens
    ax2.plot([c_x[0], c_x[0] - 0.9], [c_y, c_y], color=INK, lw=2, zorder=2)
    ax2.text(c_x[0] - 0.9, c_y, 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
    ax2.plot([c_x[-1], c_x[-1] + 0.9], [c_y, c_y], color=INK, lw=2, zorder=2)
    ax2.text(c_x[-1] + 0.9, c_y, 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
    
    # Draw C atoms
    for x in c_x:
        ax2.text(x, c_y, 'C', fontsize=18, fontweight='bold', color=INK, bbox=c_bbox, **atom_kwargs)
        
    ax2.text(2.0, label_y, "Catenation: Straight chain", fontsize=15, ha='center', va='center', fontweight='bold', color=INK)

    # --- 3. Ring structure (6 carbons) ---
    # Shift center slightly upwards to provide ample clearance below for label
    center_y = 0.2
    r_c = 1.05
    angles_c = np.linspace(np.pi/6, 2*np.pi + np.pi/6, 6, endpoint=False)
    ring_c_x = r_c * np.cos(angles_c)
    ring_c_y = center_y + r_c * np.sin(angles_c)
    
    # C-C ring bonds
    for i in range(6):
        next_i = (i + 1) % 6
        ax3.plot([ring_c_x[i], ring_c_x[next_i]], [ring_c_y[i], ring_c_y[next_i]], color=INK, lw=2.5, zorder=2)
        
    # Hydrogens pointing outward (two per carbon for cyclohexane)
    r_h = 1.75
    for i in range(6):
        a1 = angles_c[i] - 0.22
        a2 = angles_c[i] + 0.22
        h1 = [r_h * np.cos(a1), center_y + r_h * np.sin(a1)]
        h2 = [r_h * np.cos(a2), center_y + r_h * np.sin(a2)]
        
        ax3.plot([ring_c_x[i], h1[0]], [ring_c_y[i], h1[1]], color=INK, lw=1.8, zorder=2)
        ax3.plot([ring_c_x[i], h2[0]], [ring_c_y[i], h2[1]], color=INK, lw=1.8, zorder=2)
        
        ax3.text(h1[0], h1[1], 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
        ax3.text(h2[0], h2[1], 'H', fontsize=14, fontweight='bold', color=INK, bbox=h_bbox, **atom_kwargs)
        
    # Draw ring C atoms
    for i in range(6):
        ax3.text(ring_c_x[i], ring_c_y[i], 'C', fontsize=18, fontweight='bold', color=INK, bbox=c_bbox, **atom_kwargs)
        
    ax3.text(0.0, label_y, "Catenation: Ring structure", fontsize=15, ha='center', va='center', fontweight='bold', color=INK)
    
    save(fig, out)
