from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 7)
    
    ax1 = fig.add_axes([0.05, 0.12, 0.42, 0.78])
    ax2 = fig.add_axes([0.53, 0.12, 0.42, 0.78])

    t = np.linspace(0, 2 * np.pi, 250)
    r = 3.6 + 0.45 * np.sin(2 * t) - 0.35 * np.cos(3 * t) + 0.2 * np.sin(5 * t)
    x_outer = r * np.cos(t)
    y_outer = r * np.sin(t)
    region_poly = list(zip(x_outer, y_outer))

    r_core = 1.35
    core_pts = [(r_core * np.cos(a), r_core * np.sin(a)) for a in np.linspace(0, 2 * np.pi, 120)]

    c_zone1 = "#2B303A"   # Central zone (very dark)
    c_zone2 = "#6C757D"   # Zone 2 (medium-dark grey)
    c_zone3 = "#ADB5BD"   # Zone 3 (medium-light grey)
    c_zone4 = "#E2E6EA"   # Zone 4 (light grey)

    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.set_xlim(-4.6, 4.6)
        ax.set_ylim(-5.0, 4.6)
        ax.axis("off")

    div_angles = [np.pi / 4, 5 * np.pi / 6, 3 * np.pi / 2]

    # --- LEFT MAP: Dot Map ---
    ax1.set_title("Dot Map", fontsize=18, color=INK, weight="bold", pad=14)

    base_patch1 = patches.Polygon(region_poly, closed=True, facecolor="#F8F9FA", edgecolor=INK, linewidth=2.0)
    ax1.add_patch(base_patch1)

    for ang in div_angles:
        x_ray = [r_core * np.cos(ang), 4.3 * np.cos(ang)]
        y_ray = [r_core * np.sin(ang), 4.3 * np.sin(ang)]
        line = patches.PathPatch(patches.Path([(x_ray[0], y_ray[0]), (x_ray[1], y_ray[1])]),
                                 color="#9AA0A6", linestyle="--", linewidth=1.2, zorder=2)
        line.set_clip_path(base_patch1)
        ax1.add_patch(line)

    core_circ1 = patches.Circle((0, 0), r_core, edgecolor="#9AA0A6", facecolor="none",
                                linestyle="--", linewidth=1.2, zorder=2)
    ax1.add_patch(core_circ1)

    np.random.seed(42)
    n_core = 340
    r_c = np.sqrt(np.random.uniform(0, r_core**2, n_core))
    theta_c = np.random.uniform(0, 2 * np.pi, n_core)
    x_c = r_c * np.cos(theta_c)
    y_c = r_c * np.sin(theta_c)

    n_mid = 130
    r_m = np.random.uniform(r_core, 2.7, n_mid)
    theta_m = np.random.uniform(0, 2 * np.pi, n_mid)
    x_m = r_m * np.cos(theta_m)
    y_m = r_m * np.sin(theta_m)

    n_outer = 50
    r_o = np.random.uniform(2.5, 3.6, n_outer)
    theta_o = np.random.uniform(0, 2 * np.pi, n_outer)
    x_o = r_o * np.cos(theta_o)
    y_o = r_o * np.sin(theta_o)

    all_x = np.concatenate([x_c, x_m, x_o])
    all_y = np.concatenate([y_c, y_m, y_o])

    outer_path = patches.Polygon(region_poly).get_path()
    valid_pts = [(px, py) for px, py in zip(all_x, all_y) if outer_path.contains_point((px, py))]
    valid_x, valid_y = zip(*valid_pts)

    ax1.scatter(valid_x, valid_y, s=14, color=INK, alpha=0.9, zorder=3, edgecolors="none")

    # Legend for Dot Map
    ax1.scatter([-3.4], [-4.4], s=14, color=INK, zorder=5)
    ax1.text(-3.05, -4.43, "1 dot = 100 people", fontsize=14, color=INK, va="center",
             bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="none"))

    # --- RIGHT MAP: Choropleth Map ---
    ax2.set_title("Choropleth Map", fontsize=18, color=INK, weight="bold", pad=14)

    base_patch2 = patches.Polygon(region_poly, closed=True, facecolor=c_zone4, edgecolor=INK, linewidth=2.0, zorder=1)
    ax2.add_patch(base_patch2)

    wedge_angles = [(np.pi / 4, 5 * np.pi / 6, c_zone2), (5 * np.pi / 6, 3 * np.pi / 2, c_zone3)]
    for start_a, end_a, col in wedge_angles:
        arc_angles = np.linspace(start_a, end_a, 60)
        wedge_pts = [(0, 0)] + [(5.5 * np.cos(a), 5.5 * np.sin(a)) for a in arc_angles]
        wedge_poly = patches.Polygon(wedge_pts, closed=True, facecolor=col, edgecolor="none", zorder=2)
        wedge_poly.set_clip_path(base_patch2)
        ax2.add_patch(wedge_poly)

    core_patch = patches.Polygon(core_pts, closed=True, facecolor=c_zone1, edgecolor=INK, linewidth=1.6, zorder=4)
    ax2.add_patch(core_patch)

    for ang in div_angles:
        p1 = (r_core * np.cos(ang), r_core * np.sin(ang))
        p2 = (5.0 * np.cos(ang), 5.0 * np.sin(ang))
        line = patches.PathPatch(patches.Path([p1, p2]), color=INK, linewidth=1.6, zorder=3)
        line.set_clip_path(base_patch2)
        ax2.add_patch(line)

    outer_outline = patches.Polygon(region_poly, closed=True, facecolor="none", edgecolor=INK, linewidth=2.0, zorder=5)
    ax2.add_patch(outer_outline)

    # Zone Labels
    zone_labels = [
        (0.0, 0.0, "Zone 1", "white"),
        (0.35, 2.3, "Zone 2", "white"),
        (-2.2, -0.6, "Zone 3", INK),
        (1.5, -2.0, "Zone 4", INK)
    ]
    for lx, ly, ltxt, lcol in zone_labels:
        ax2.text(lx, ly, ltxt, fontsize=14, color=lcol, weight="bold", ha="center", va="center", zorder=6)

    # Choropleth Legend
    legend_y = -4.35
    box_w = 0.58
    box_h = 0.32
    colors_legend = [c_zone1, c_zone2, c_zone3, c_zone4]
    start_x = -2.7

    for i, col in enumerate(colors_legend):
        bx = start_x + i * (box_w + 0.06)
        rect = patches.Rectangle((bx, legend_y), box_w, box_h, facecolor=col, edgecolor=INK, linewidth=1.2, zorder=5)
        ax2.add_patch(rect)

    ax2.text(start_x, legend_y + box_h + 0.16, "Darker shades = higher density",
             fontsize=14, color=INK, weight="bold", zorder=5)
    ax2.text(start_x, legend_y - 0.22, "High density", fontsize=14, color=INK, ha="left", va="top", zorder=5)
    ax2.text(start_x + 4 * (box_w + 0.06) - 0.06, legend_y - 0.22, "Low density",
             fontsize=14, color=INK, ha="right", va="top", zorder=5)

    save(fig, out)
