from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Color palette
    proton_col = DEEP["pink"]      # red/pink for protons
    neutron_col = DEEP["blue"]     # blue for neutrons
    electron_col = ORANGE          # warm yellow/orange for electrons
    orbit_col = GREY

    # Draw Electron Shells (Orbits)
    r1, r2 = 2.0, 3.4
    orbit1 = patches.Circle((0, 0), r1, fill=False, edgecolor=orbit_col, lw=2.0, ls='--')
    orbit2 = patches.Circle((0, 0), r2, fill=False, edgecolor=orbit_col, lw=2.0, ls='--')
    ax.add_patch(orbit1)
    ax.add_patch(orbit2)

    # Nucleus: cluster of protons and neutrons (carbon-like: 6 protons, 6 neutrons)
    p_positions = [
        (-0.35, 0.3), (0.35, 0.35), (-0.4, -0.3),
        (0.2, -0.45), (0.0, 0.0), (0.5, -0.05)
    ]
    n_positions = [
        (-0.15, 0.45), (0.45, 0.15), (-0.45, 0.05),
        (-0.1, -0.4), (0.35, -0.35), (0.05, 0.25)
    ]

    r_nuc = 0.28  # radius of nucleons

    # Draw neutrons (blank blue spheres)
    for (x, y) in n_positions:
        circ = patches.Circle((x, y), r_nuc, facecolor=neutron_col, edgecolor='white', lw=1.5, zorder=3)
        ax.add_patch(circ)

    # Draw protons (red spheres with '+')
    for (x, y) in p_positions:
        circ = patches.Circle((x, y), r_nuc, facecolor=proton_col, edgecolor='white', lw=1.5, zorder=4)
        ax.add_patch(circ)
        ax.text(x, y, '+', ha='center', va='center', fontsize=15, color='white', weight='bold', zorder=5)

    # Electrons on orbits (Bohr model: 2 on shell 1, 4 on shell 2)
    e_r = 0.22
    # Shell 1 angles (2 electrons: top and bottom)
    angles_s1 = [np.pi / 2, 3 * np.pi / 2]
    # Shell 2 angles (4 electrons: 45, 135, 225, 315 degrees)
    angles_s2 = [np.pi / 4, 3 * np.pi / 4, 5 * np.pi / 4, 7 * np.pi / 4]

    electron_coords = []
    for ang in angles_s1:
        electron_coords.append((r1 * np.cos(ang), r1 * np.sin(ang)))
    for ang in angles_s2:
        electron_coords.append((r2 * np.cos(ang), r2 * np.sin(ang)))

    for (ex, ey) in electron_coords:
        e_circ = patches.Circle((ex, ey), e_r, facecolor=electron_col, edgecolor=INK, lw=1.5, zorder=6)
        ax.add_patch(e_circ)
        # Using a standard hyphen '-' centered vertically and horizontally
        ax.text(ex, ey, '-', ha='center', va='center', fontsize=18, color=INK, weight='bold', zorder=7)

    # Annotations / Labels
    bbox_style = dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2)
    arrow_style = dict(arrowstyle="->", color=INK, lw=1.5, shrinkA=4, shrinkB=4)

    # Nucleus label
    ax.annotate(
        "Nucleus (protons + neutrons)",
        xy=(-0.25, 0.35), xytext=(-2.3, 2.0),
        fontsize=15, color=INK, weight='bold',
        arrowprops=arrow_style, bbox=bbox_style,
        ha='center', va='center', zorder=10
    )

    # Electron shell (orbit) label
    # Targeting shell 2 at an angle clearly away from electrons (e.g. 105 degrees)
    shell_angle = np.radians(105)
    shell_point_x = r2 * np.cos(shell_angle)
    shell_point_y = r2 * np.sin(shell_angle)
    ax.annotate(
        "Electron shell (orbit)",
        xy=(shell_point_x, shell_point_y), xytext=(-2.0, 4.3),
        fontsize=15, color=INK, weight='bold',
        arrowprops=arrow_style, bbox=bbox_style,
        ha='center', va='center', zorder=10
    )

    # Electron label pointing to the top-right outer shell electron
    target_e = (r2 * np.cos(np.pi / 4), r2 * np.sin(np.pi / 4))
    ax.annotate(
        "Electron",
        xy=target_e, xytext=(3.6, 3.6),
        fontsize=15, color=INK, weight='bold',
        arrowprops=arrow_style, bbox=bbox_style,
        ha='center', va='center', zorder=10
    )

    save(fig, out)
