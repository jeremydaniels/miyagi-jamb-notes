import numpy as np
import matplotlib.pyplot as plt
from style import *

def draw(out):
    fig = canvas(12, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 19)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.axis("off")

    # Styling
    ray_color = DEEP["orange"]
    ray_lw = 2.2
    lens_edge = DEEP["blue"]
    lens_face = BLUE

    # -------------------------------------------------------------
    # LEFT: Concave (Diverging) Lens
    # -------------------------------------------------------------
    xc = 4.0
    h_lens = 2.5
    y_vals = np.linspace(-h_lens, h_lens, 100)

    # Concave profile: thin at middle, thick at edges
    d_x = 0.12 + 0.35 * (y_vals / h_lens) ** 2
    left_x = xc - d_x
    right_x = xc + d_x

    lens_pts_x = np.concatenate([left_x, right_x[::-1]])
    lens_pts_y = np.concatenate([y_vals, y_vals[::-1]])
    ax.fill(lens_pts_x, lens_pts_y, color=lens_face, alpha=0.35, zorder=2)
    ax.plot(lens_pts_x, lens_pts_y, color=lens_edge, lw=2, zorder=3)

    # Optical axis (dashed)
    ax.plot([0.5, 8.5], [0, 0], color=GREY, lw=1.2, ls="--", zorder=1)

    # 3 incoming rays: y = +1.4, 0, -1.4
    f_concave = 2.8
    ray_ys = [1.4, 0.0, -1.4]
    for y0 in ray_ys:
        # Incoming ray
        ax.plot([0.6, xc], [y0, y0], color=ray_color, lw=ray_lw, zorder=4)
        # Arrow on incoming ray
        ax.annotate("", xy=(2.4, y0), xytext=(2.1, y0),
                    arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))

        if abs(y0) > 1e-5:
            # Diverging ray trajectory
            slope = y0 / f_concave
            x_end = 8.5
            y_end = y0 + slope * (x_end - xc)
            # Virtual trace (dashed) back to virtual focus
            ax.plot([xc - f_concave, xc], [0, y0], color=ray_color, lw=1.2, ls=":", zorder=2)
            # Diverged ray
            ax.plot([xc, x_end], [y0, y_end], color=ray_color, lw=ray_lw, zorder=4)
            # Arrow on diverged ray
            x_arr = xc + 1.8
            y_arr = y0 + slope * 1.8
            x_arr0 = xc + 1.5
            y_arr0 = y0 + slope * 1.5
            ax.annotate("", xy=(x_arr, y_arr), xytext=(x_arr0, y_arr0),
                        arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))
        else:
            # Center ray passes straight through
            ax.plot([xc, 8.5], [0, 0], color=ray_color, lw=ray_lw, zorder=4)
            ax.annotate("", xy=(6.5, 0), xytext=(6.2, 0),
                        arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))

    # -------------------------------------------------------------
    # RIGHT: Convex (Converging) Lens
    # -------------------------------------------------------------
    xv = 13.5
    # Convex profile: thick at middle, thin at edges
    d_xv = 0.45 - 0.38 * (y_vals / h_lens) ** 2
    left_xv = xv - d_xv
    right_xv = xv + d_xv

    lens_v_x = np.concatenate([left_xv, right_xv[::-1]])
    lens_v_y = np.concatenate([y_vals, y_vals[::-1]])
    ax.fill(lens_v_x, lens_v_y, color=lens_face, alpha=0.35, zorder=2)
    ax.plot(lens_v_x, lens_v_y, color=lens_edge, lw=2, zorder=3)

    # Optical axis (dashed)
    ax.plot([10.0, 18.0], [0, 0], color=GREY, lw=1.2, ls="--", zorder=1)

    f_convex = 3.2
    f_focus_x = xv + f_convex

    for y0 in ray_ys:
        # Incoming ray
        ax.plot([10.2, xv], [y0, y0], color=ray_color, lw=ray_lw, zorder=4)
        # Arrow on incoming ray
        ax.annotate("", xy=(11.9, y0), xytext=(11.6, y0),
                    arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))

        # Refracted ray towards focus
        slope = -y0 / f_convex
        x_end = xv + f_convex + 1.2
        y_end = slope * (x_end - xv) + y0
        ax.plot([xv, x_end], [y0, y_end], color=ray_color, lw=ray_lw, zorder=4)

        if abs(y0) > 1e-5:
            # Arrow on converging ray before focus
            x_mid = xv + 1.6
            y_mid = y0 + slope * 1.6
            x_mid0 = xv + 1.3
            y_mid0 = y0 + slope * 1.3
            ax.annotate("", xy=(x_mid, y_mid), xytext=(x_mid0, y_mid0),
                        arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))
        else:
            ax.annotate("", xy=(15.3, 0), xytext=(15.0, 0),
                        arrowprops=dict(arrowstyle="->", color=ray_color, lw=ray_lw))

    # Focal point marker
    ax.scatter([f_focus_x], [0], color=DEEP["pink"], s=50, zorder=6)

    # -------------------------------------------------------------
    # LABELS & ANNOTATIONS
    # -------------------------------------------------------------
    # Lens titles (top)
    ax.text(xc, 3.2, "concave lens", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(xv, 3.2, "convex lens", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2))

    # Ray action descriptions: placed to avoid ray intersection
    # Concave diverging label moved slightly to avoid intersection
    ax.annotate("rays spread out\n(diverge)",
                xy=(6.3, 2.1), xytext=(7.4, 0.9),
                fontsize=12, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"),
                zorder=7)

    # Convex converging label
    ax.annotate("rays meet\n(converge)",
                xy=(15.2, -0.65), xytext=(14.2, -2.5),
                fontsize=12, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"),
                zorder=7)

    # Focal point annotation
    ax.annotate("focal point",
                xy=(f_focus_x, 0), xytext=(f_focus_x + 0.2, 1.8),
                fontsize=12, color=INK, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"),
                zorder=7)

    save(fig, out)
