from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(14, 7.5)
    
    # Left subplot: Diamond, Right subplot: Graphite
    ax_left = fig.add_axes([0.03, 0.08, 0.45, 0.82])
    ax_right = fig.add_axes([0.52, 0.08, 0.45, 0.82])
    
    for ax in [ax_left, ax_right]:
        ax.set_aspect("equal")
        ax.axis("off")
        
    # --- 1. DIAMOND LATTICE (Left) ---
    # Construct an intuitive perspective projection of diamond tetrahedral network
    # We can use a small set of diamond cubic coordinates (fcc + basis)
    # Basis: (0,0,0) and (1/4, 1/4, 1/4)
    diamond_nodes = []
    
    # Build a 2x2x2 block of diamond lattice nodes
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # FCC points
                diamond_nodes.append((i, j, k))
                diamond_nodes.append((i + 0.5, j + 0.5, k))
                diamond_nodes.append((i + 0.5, j, k + 0.5))
                diamond_nodes.append((i, j + 0.5, k + 0.5))
                # Basis shifted by (0.25, 0.25, 0.25)
                diamond_nodes.append((i + 0.25, j + 0.25, k + 0.25))
                diamond_nodes.append((i + 0.75, j + 0.75, k + 0.25))
                diamond_nodes.append((i + 0.75, j + 0.25, k + 0.75))
                diamond_nodes.append((i + 0.25, j + 0.75, k + 0.75))
                
    # Filter to a compact spherical or cuboid cluster
    diamond_nodes = np.array(list(set(diamond_nodes)))
    center = np.array([1.0, 1.0, 1.0])
    dists = np.linalg.norm(diamond_nodes - center, axis=1)
    diamond_nodes = diamond_nodes[dists <= 1.3]
    
    # Bonds: distance = sqrt(3)/4 ~ 0.433
    bonds = []
    num_nodes = len(diamond_nodes)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            d = np.linalg.norm(diamond_nodes[i] - diamond_nodes[j])
            if 0.40 < d < 0.46:
                bonds.append((i, j))
                
    # Perspective projection
    angle_x = np.radians(20)
    angle_y = np.radians(35)
    Rx = np.array([[1, 0, 0], [0, np.cos(angle_x), -np.sin(angle_x)], [0, np.sin(angle_x), np.cos(angle_x)]])
    Ry = np.array([[np.cos(angle_y), 0, np.sin(angle_y)], [0, 1, 0], [-np.sin(angle_y), 0, np.cos(angle_y)]])
    R = Ry @ Rx
    
    rot_nodes = (diamond_nodes - center) @ R.T
    
    # Sort bonds by average depth (Z)
    bond_depths = []
    for i, j in bonds:
        z_avg = (rot_nodes[i, 2] + rot_nodes[j, 2]) / 2.0
        bond_depths.append((z_avg, i, j))
    bond_depths.sort(key=lambda x: x[0])
    
    # Draw bonds
    for _, i, j in bond_depths:
        x1, y1 = rot_nodes[i, 0], rot_nodes[i, 1]
        x2, y2 = rot_nodes[j, 0], rot_nodes[j, 1]
        ax_left.plot([x1, x2], [y1, y2], color=DEEP["blue"], lw=3.5, solid_capstyle="round", zorder=2)
        
    # Draw atoms
    # Sort atoms by Z for correct occlusions
    atom_order = np.argsort(rot_nodes[:, 2])
    for idx in atom_order:
        x, y = rot_nodes[idx, 0], rot_nodes[idx, 1]
        ax_left.scatter(x, y, s=280, color=BLUE, edgecolor=DEEP["blue"], lw=2.5, zorder=3)
        
    ax_left.set_xlim(-1.5, 1.5)
    ax_left.set_ylim(-1.5, 1.5)
    
    ax_left.text(0, -1.4, "Diamond structure (tetrahedral)", ha="center", va="center",
                 fontsize=15, weight="bold", color=INK,
                 bbox=dict(fc="white", ec="none", pad=3))
    
    ax_left.text(0, 1.35, "Strong covalent bonds throughout\nrigid 3D tetrahedral network",
                 ha="center", va="center", fontsize=14, color=INK,
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # --- 2. GRAPHITE LATTICE (Right) ---
    # Construct 3 layers of honeycomb hexagons in oblique projection
    # Layer planes at different Y heights
    layers_y = [0.8, -0.05, -0.9]
    hex_centers_x = [-1.0, 0.0, 1.0]
    hex_centers_z = [-0.5, 0.4]
    
    # Oblique projection: x_proj = x + z * 0.4, y_proj = y + z * 0.25
    def project_layer(x, y_layer, z):
        xp = x + 0.45 * z
        yp = y_layer + 0.28 * z
        return xp, yp

    # Honeycomb unit generator
    layer_atoms = []
    r = 0.42  # C-C distance
    angles = np.linspace(0, 2 * np.pi, 7)[:-1] + np.pi / 6
    hx = r * np.cos(angles)
    hz = r * np.sin(angles)
    
    # Create a nice patch of interconnected hexagons for one layer
    base_hex_offsets = [
        (-0.72, 0.42), (0.0, 0.42), (0.72, 0.42),
        (-1.08, -0.21), (-0.36, -0.21), (0.36, -0.21), (1.08, -0.21),
        (-0.72, -0.84), (0.0, -0.84), (0.72, -0.84)
    ]
    
    unique_layer_points = []
    layer_bonds = []
    
    for ox, oz in base_hex_offsets:
        pts = [(ox + np.cos(a) * 0.42, oz + np.sin(a) * 0.42) for a in angles]
        for p in pts:
            # Check if exists
            exists = False
            for up in unique_layer_points:
                if (up[0] - p[0])**2 + (up[1] - p[1])**2 < 0.01:
                    exists = True
                    break
            if not exists:
                unique_layer_points.append(p)
                
    unique_layer_points = np.array(unique_layer_points)
    for i in range(len(unique_layer_points)):
        for j in range(i + 1, len(unique_layer_points)):
            d = np.linalg.norm(unique_layer_points[i] - unique_layer_points[j])
            if 0.38 < d < 0.46:
                layer_bonds.append((i, j))

    # Draw interlayer weak forces (dashed lines) between corresponding atoms in layer 0 & 1, 1 & 2
    for l_idx in range(len(layers_y) - 1):
        y_top = layers_y[l_idx]
        y_bot = layers_y[l_idx + 1]
        for p in unique_layer_points[::3]:  # sample atoms for dashed lines
            xt, yt = project_layer(p[0], y_top, p[1])
            xb, yb = project_layer(p[0], y_bot, p[1])
            ax_right.plot([xt, xb], [yt, yb], color=DEEP["pink"], lw=1.8, ls="--", dashes=(4, 4), zorder=1)

    # Draw each layer's bonds and atoms
    for y_l in layers_y:
        # Bonds
        for i, j in layer_bonds:
            x1, y1 = project_layer(unique_layer_points[i, 0], y_l, unique_layer_points[i, 1])
            x2, y2 = project_layer(unique_layer_points[j, 0], y_l, unique_layer_points[j, 1])
            ax_right.plot([x1, x2], [y1, y2], color=DEEP["green"], lw=3.0, solid_capstyle="round", zorder=2)
            
        # Atoms
        for p in unique_layer_points:
            x, y = project_layer(p[0], y_l, p[1])
            ax_right.scatter(x, y, s=140, color=GREEN, edgecolor=DEEP["green"], lw=2, zorder=3)
            
    # Annotations on Graphite
    ax_right.annotate("Weak forces between\nseparated layers",
                      xy=(0.7, 0.35), xytext=(1.45, 0.42),
                      fontsize=14, color=INK, ha="left", va="center",
                      arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    
    ax_right.annotate("Strong covalent bonds\nwithin hexagonal sheets",
                      xy=(-0.3, -0.05), xytext=(-1.7, 0.3),
                      fontsize=14, color=INK, ha="right", va="center",
                      arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax_right.set_xlim(-1.8, 2.2)
    ax_right.set_ylim(-1.5, 1.5)
    
    ax_right.text(0.1, -1.4, "Graphite structure (hexagonal layers)", ha="center", va="center",
                  fontsize=15, weight="bold", color=INK,
                  bbox=dict(fc="white", ec="none", pad=3))

    save(fig, out)
