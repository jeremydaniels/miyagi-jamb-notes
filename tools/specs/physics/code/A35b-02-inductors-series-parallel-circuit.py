from style import *
import numpy as np

def inductor_path(x_start, y_center, n_loops=4, loop_radius=0.22):
    """Generates (x, y) coordinates for an inductor symbol with series of arcs."""
    x_pts = []
    y_pts = []
    for i in range(n_loops):
        theta = np.linspace(np.pi, 0, 30)
        cx = x_start + (2 * i + 1) * loop_radius
        cy = y_center
        x_pts.extend(cx + loop_radius * np.cos(theta))
        y_pts.extend(cy + loop_radius * np.sin(theta))
    return np.array(x_pts), np.array(y_pts)

def draw_inductor(ax, x_start, y_center, n_loops=4, r=0.22, color=DEEP["blue"], lw=2.5):
    xs, ys = inductor_path(x_start, y_center, n_loops, r)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle='round')
    total_len = 2 * n_loops * r
    return x_start + total_len

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 8.5)
    ax.axis('off')

    # Helper for circuit junction/terminal nodes
    def node(x, y):
        ax.plot(x, y, 'o', color=INK, markersize=6, zorder=5)

    # ---------------- Top Diagram: Series ----------------
    y_series = 6.4
    r = 0.22
    n_loops = 4

    # Title
    ax.text(0.5, 7.8, "Series Connection", fontsize=17, fontweight='bold', color=INK, va='center')

    # Terminal A
    ax.plot([0.6, 1.6], [y_series, y_series], color=INK, lw=2.5)
    node(0.6, y_series)
    ax.text(0.3, y_series, "A", fontsize=15, color=INK, ha='right', va='center')

    # Inductor L1
    x_curr = 1.6
    x_end1 = draw_inductor(ax, x_curr, y_series, n_loops=n_loops, r=r, color=DEEP["blue"])
    ax.text((x_curr + x_end1) / 2, y_series + 0.42, r"$L_1$", fontsize=16, color=INK, ha='center', va='bottom')

    # Wire between L1 and L2
    ax.plot([x_end1, x_end1 + 1.0], [y_series, y_series], color=INK, lw=2.5)
    x_curr = x_end1 + 1.0

    # Inductor L2
    x_end2 = draw_inductor(ax, x_curr, y_series, n_loops=n_loops, r=r, color=DEEP["blue"])
    ax.text((x_curr + x_end2) / 2, y_series + 0.42, r"$L_2$", fontsize=16, color=INK, ha='center', va='bottom')

    # Wire between L2 and L3
    ax.plot([x_end2, x_end2 + 1.0], [y_series, y_series], color=INK, lw=2.5)
    x_curr = x_end2 + 1.0

    # Inductor L3
    x_end3 = draw_inductor(ax, x_curr, y_series, n_loops=n_loops, r=r, color=DEEP["blue"])
    ax.text((x_curr + x_end3) / 2, y_series + 0.42, r"$L_3$", fontsize=16, color=INK, ha='center', va='bottom')

    # Terminal B
    ax.plot([x_end3, 9.4], [y_series, y_series], color=INK, lw=2.5)
    node(9.4, y_series)
    ax.text(9.7, y_series, "B", fontsize=15, color=INK, ha='left', va='center')

    # Divider line between diagrams
    ax.plot([0.5, 9.5], [4.9, 4.9], color=GREY, lw=1.2, linestyle='--')

    # ---------------- Bottom Diagram: Parallel ----------------
    # Title
    ax.text(0.5, 4.3, "Parallel Connection", fontsize=17, fontweight='bold', color=INK, va='center')

    y_top = 3.3
    y_mid = 2.1
    y_bot = 0.9

    x_left_junction = 3.0
    x_right_junction = 7.0

    # External leads to common junctions
    ax.plot([1.0, x_left_junction], [y_mid, y_mid], color=INK, lw=2.5)
    node(1.0, y_mid)
    ax.text(0.7, y_mid, "A", fontsize=15, color=INK, ha='right', va='center')

    ax.plot([x_right_junction, 9.0], [y_mid, y_mid], color=INK, lw=2.5)
    node(9.0, y_mid)
    ax.text(9.3, y_mid, "B", fontsize=15, color=INK, ha='left', va='center')

    # Common junction vertical buses
    ax.plot([x_left_junction, x_left_junction], [y_bot, y_top], color=INK, lw=2.5)
    ax.plot([x_right_junction, x_right_junction], [y_bot, y_top], color=INK, lw=2.5)

    # Junction dots
    node(x_left_junction, y_top)
    node(x_left_junction, y_mid)
    node(x_left_junction, y_bot)
    node(x_right_junction, y_top)
    node(x_right_junction, y_mid)
    node(x_right_junction, y_bot)

    # Parallel branches
    ind_width = 2 * n_loops * r
    x_ind_start = 5.0 - ind_width / 2.0
    x_ind_end = x_ind_start + ind_width

    branches = [
        (y_top, r"$L_1$"),
        (y_mid, r"$L_2$"),
        (y_bot, r"$L_3$")
    ]

    for y_pos, label in branches:
        # Wire from left junction to inductor
        ax.plot([x_left_junction, x_ind_start], [y_pos, y_pos], color=INK, lw=2.5)
        # Inductor
        draw_inductor(ax, x_ind_start, y_pos, n_loops=n_loops, r=r, color=DEEP["green"])
        # Wire from inductor to right junction
        ax.plot([x_ind_end, x_right_junction], [y_pos, y_pos], color=INK, lw=2.5)
        # Label
        ax.text(5.0, y_pos + 0.38, label, fontsize=16, color=INK, ha='center', va='bottom')

    save(fig, out)
