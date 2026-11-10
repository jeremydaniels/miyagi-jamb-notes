from style import *
import numpy as np

def draw(out):
    fig = canvas(9, 9)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)

    # Simulation grid for wave interference background
    x = np.linspace(-5.2, 5.2, 450)
    y = np.linspace(-5.2, 5.2, 450)
    X, Y = np.meshgrid(x, y)

    # Sources: separation d = 3.0 (at x = -1.5 and x = +1.5)
    d = 1.5
    wavelength = 0.8
    k = 2 * np.pi / wavelength

    r1 = np.sqrt((X + d)**2 + Y**2)
    r2 = np.sqrt((X - d)**2 + Y**2)

    # Superposition of two coherent point sources
    # Damping slightly with distance to mimic ripples
    amp1 = np.cos(k * r1) / np.sqrt(np.maximum(r1, 0.4))
    amp2 = np.cos(k * r2) / np.sqrt(np.maximum(r2, 0.4))
    Z = amp1 + amp2

    # Draw continuous ripple field with soft colormap
    ax.imshow(
        Z,
        extent=[-5.2, 5.2, -5.2, 5.2],
        origin="lower",
        cmap="Blues",
        alpha=0.28,
        interpolation="bicubic"
    )

    # Draw expanding wavefronts (crests) around each source
    max_radius = 6.0
    radii = np.arange(wavelength, max_radius, wavelength)
    theta = np.linspace(0, 2 * np.pi, 200)

    for r in radii:
        ax.plot(-d + r * np.cos(theta), r * np.sin(theta), color=DEEP["blue"], lw=1.0, alpha=0.35, zorder=2)
        ax.plot(d + r * np.cos(theta), r * np.sin(theta), color=DEEP["blue"], lw=1.0, alpha=0.35, zorder=2)

    # Plot nodal and antinodal hyperbolae: |r1 - r2| = path_diff
    # Antinodal lines (constructive): path_diff = n * wavelength
    # Nodal lines (destructive): path_diff = (n + 0.5) * wavelength
    t = np.linspace(-4.5, 4.5, 300)

    # Antinodal: n = 0 (central line x = 0)
    ax.plot([0, 0], [-4.8, 4.8], color=DEEP["blue"], lw=3.0, linestyle="-", label="Antinodal line (constructive)", zorder=5)

    # Antinodal: n = 1 -> path_diff = wavelength
    # Hyperbola: x^2 / a^2 - y^2 / b^2 = 1 with 2a = wavelength => a = 0.4, c = 1.5, b = sqrt(c^2 - a^2)
    a_anti = wavelength / 2.0
    if a_anti < d:
        b_anti = np.sqrt(d**2 - a_anti**2)
        x_anti = a_anti * np.cosh(t / b_anti)
        y_anti = t
        # Both branches
        ax.plot(x_anti, y_anti, color=DEEP["blue"], lw=2.5, linestyle="-", zorder=5)
        ax.plot(-x_anti, y_anti, color=DEEP["blue"], lw=2.5, linestyle="-", zorder=5)

    # Nodal lines: n = 0 -> path_diff = 0.5 * wavelength
    a_node1 = 0.5 * wavelength / 2.0
    b_node1 = np.sqrt(d**2 - a_node1**2)
    x_node1 = a_node1 * np.cosh(t / b_node1)
    y_node1 = t
    ax.plot(x_node1, y_node1, color=DEEP["pink"], lw=2.5, linestyle="--", dashes=(5, 4), label="Nodal line (destructive)", zorder=5)
    ax.plot(-x_node1, y_node1, color=DEEP["pink"], lw=2.5, linestyle="--", dashes=(5, 4), zorder=5)

    # Nodal lines: n = 1 -> path_diff = 1.5 * wavelength
    a_node2 = 1.5 * wavelength / 2.0
    if a_node2 < d:
        b_node2 = np.sqrt(d**2 - a_node2**2)
        x_node2 = a_node2 * np.cosh(t / b_node2)
        y_node2 = t
        ax.plot(x_node2, y_node2, color=DEEP["pink"], lw=2.5, linestyle="--", dashes=(5, 4), zorder=5)
        ax.plot(-x_node2, y_node2, color=DEEP["pink"], lw=2.5, linestyle="--", dashes=(5, 4), zorder=5)

    # Mark the two point source dippers
    ax.scatter([-d, d], [0, 0], s=140, color=DEEP["orange"], edgecolors=INK, linewidth=2.0, zorder=10)
    ax.annotate(
        "Source $S_1$\n(dipper)",
        xy=(-d, 0),
        xytext=(-d - 0.2, -1.3),
        fontsize=14,
        color=INK,
        ha="center",
        va="top",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        zorder=12
    )
    ax.annotate(
        "Source $S_2$\n(dipper)",
        xy=(d, 0),
        xytext=(d + 0.2, -1.3),
        fontsize=14,
        color=INK,
        ha="center",
        va="top",
        bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"),
        arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
        zorder=12
    )

    # Explanatory annotations
    ax.annotate(
        "Antinode (maximum wave height)",
        xy=(0, 3.6),
        xytext=(0, 4.8),
        fontsize=14,
        color=DEEP["blue"],
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3"),
        arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
        zorder=12
    )

    # Node label pointing to first nodal line
    node_pt_x = a_node1 * np.cosh(2.5 / b_node1)
    node_pt_y = 2.5
    ax.annotate(
        "Node (calm water)",
        xy=(node_pt_x, node_pt_y),
        xytext=(3.2, 3.8),
        fontsize=14,
        color=DEEP["pink"],
        fontweight="bold",
        ha="left",
        va="center",
        bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3"),
        arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5),
        zorder=12
    )

    # Title & Legend
    ax.set_title("Ripple Tank Interference Pattern", fontsize=18, pad=12, color=INK, fontweight="bold")
    ax.legend(
        loc="lower center",
        frameon=True,
        facecolor="white",
        edgecolor=GREY,
        fontsize=14,
        bbox_to_anchor=(0.5, 0.02)
    )

    save(fig, out)
