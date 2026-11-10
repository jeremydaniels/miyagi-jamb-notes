from style import *
import numpy as np

def draw(out):
    fig = canvas(8.5, 7.5)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-4, 6)
    ax.set_ylim(-4, 4)

    # Fluid representation (subtle container or streamlines)
    # Streamlines showing flow around the falling sphere
    sphere_center = np.array([-1.0, 0.0])
    radius = 1.0

    # Draw fluid streamlines (relative upward flow as sphere falls downwards)
    stream_x = np.linspace(-3.5, 1.5, 7)
    for sx in stream_x:
        if abs(sx - sphere_center[0]) < 0.2:
            continue
        y_pts = np.linspace(-3.2, 3.2, 100)
        # Simple potential flow deflection
        dx = sx - sphere_center[0]
        r_sq = dx**2 + (y_pts - sphere_center[1])**2
        # Avoid division issues
        r_sq = np.maximum(r_sq, 0.5)
        x_pts = sx + (radius**3 * dx / (2 * r_sq**1.5))
        ax.plot(x_pts, y_pts, color=BLUE, alpha=0.35, lw=1.5, ls="--")

    # Falling direction indicator (small motion arrow to the left)
    ax.annotate(
        "Motion\n(falling)",
        xy=(-3.0, -1.2),
        xytext=(-3.0, 0.2),
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        arrowprops=dict(arrowstyle="->", color=INK, lw=2, mutation_scale=15),
    )

    # Draw sphere
    circle = plt.Circle(sphere_center, radius, fc=CREAM, ec=INK, lw=2.5, zorder=3)
    ax.add_patch(circle)

    # Centre dot
    ax.plot(sphere_center[0], sphere_center[1], "o", color=INK, ms=6, zorder=4)

    # Force arrows:
    # 1. Weight (W) acting downwards from centre
    w_len = 2.4
    ax.annotate(
        "",
        xy=(sphere_center[0], sphere_center[1] - w_len),
        xytext=(sphere_center[0], sphere_center[1]),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["pink"],
            lw=3.5,
            mutation_scale=22,
        ),
        zorder=5,
    )
    ax.text(
        sphere_center[0] + 0.25,
        sphere_center[1] - w_len * 0.65,
        "Weight (W)",
        fontsize=15,
        color=DEEP["pink"],
        fontweight="bold",
        va="center",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6,
    )

    # 2. Upthrust (U) acting upwards from top of the sphere
    # Draw two parallel or slightly offset upward arrows from top
    top_pt = (sphere_center[0], sphere_center[1] + radius)

    # Upthrust (slightly offset to left)
    u_x = top_pt[0] - 0.35
    u_len = 1.2
    ax.annotate(
        "",
        xy=(u_x, top_pt[1] + u_len),
        xytext=(u_x, top_pt[1]),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["blue"],
            lw=3.2,
            mutation_scale=20,
        ),
        zorder=5,
    )
    ax.text(
        u_x - 0.15,
        top_pt[1] + u_len + 0.3,
        "Upthrust (U)",
        fontsize=14.5,
        color=DEEP["blue"],
        fontweight="bold",
        ha="center",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6,
    )

    # 3. Viscous Drag (F) acting upwards from top (slightly offset to right)
    f_x = top_pt[0] + 0.35
    f_len = 1.2
    ax.annotate(
        "",
        xy=(f_x, top_pt[1] + f_len),
        xytext=(f_x, top_pt[1]),
        arrowprops=dict(
            arrowstyle="-|>",
            color=DEEP["orange"],
            lw=3.2,
            mutation_scale=20,
        ),
        zorder=5,
    )
    ax.text(
        f_x + 0.15,
        top_pt[1] + f_len + 0.3,
        "Viscous Drag (F)",
        fontsize=14.5,
        color=DEEP["orange"],
        fontweight="bold",
        ha="center",
        va="bottom",
        bbox=dict(fc="white", ec="none", pad=2),
        zorder=6,
    )

    # Side note on terminal velocity
    note_text = (
        "At terminal velocity:\n\n"
        "W = U + F\n\n"
        "Acceleration = 0"
    )
    ax.text(
        3.5,
        0.0,
        note_text,
        fontsize=16,
        color=INK,
        ha="center",
        va="center",
        linespacing=1.2,
        bbox=dict(boxstyle="round,pad=0.8", fc="white", ec=DEEP["green"], lw=2),
        zorder=6,
    )

    save(fig, out)
