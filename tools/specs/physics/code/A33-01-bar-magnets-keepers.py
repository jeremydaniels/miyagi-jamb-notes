from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Geometry coordinates
    # Top magnet: y from 4.6 to 5.6, x from 2.2 to 7.8
    # Bottom magnet: y from 1.6 to 2.6, x from 2.2 to 7.8
    # Left keeper: x from 1.4 to 2.2, y from 1.6 to 5.6
    # Right keeper: x from 7.8 to 8.6, y from 1.6 to 5.6

    # Draw continuous magnetic field lines circulating inside
    # Inside magnets:
    # Top magnet (N on left, S on right): Magnetization is S -> N, so lines travel Right to Left (towards N).
    # Outside/through keeper: From N (left of top) down left keeper to S (left of bottom).
    # Bottom magnet (S on left, N on right): Inside magnet lines travel Left to Right (towards N).
    # Right keeper: From N (right of bottom) up right keeper to S (right of top).
    # This forms a complete clockwise magnetic loop!

    # Draw loop lines with varying offsets (radii of rectangular tracks)
    offsets = [-0.25, 0.0, 0.25]
    for dy in offsets:
        # Loop coordinates:
        # y_top = 5.1 + dy, y_bot = 2.1 - dy
        # x_left = 1.8 - dy, x_right = 8.2 + dy
        yt = 5.1 + dy
        yb = 2.1 - dy
        xl = 1.8 - dy
        xr = 8.2 + dy
        r = 0.4 + abs(dy) * 0.2

        # Rounded rectangle loop
        # We can construct path vertices or draw four segments with arcs
        # Top segment: xr -> xl (right to left)
        # Left segment: yt -> yb (downwards)
        # Bottom segment: xl -> xr (left to right)
        # Right segment: yb -> yt (upwards)
        path_x = [xr - r, xl + r, xl, xl, xl + r, xr - r, xr, xr, xr - r]
        path_y = [yt, yt, yt - r, yb + r, yb, yb, yb + r, yt - r, yt]
        
        # Smooth rounded corners
        t = np.linspace(0, np.pi/2, 10)
        c_tl_x = xl + r - r * np.sin(t)
        c_tl_y = yt - r + r * np.cos(t)
        
        c_bl_x = xl + r - r * np.cos(t)
        c_bl_y = yb + r - r * np.sin(t)

        c_br_x = xr - r + r * np.sin(t)
        c_br_y = yb + r - r * np.cos(t)

        c_tr_x = xr - r + r * np.cos(t)
        c_tr_y = yt - r + r * np.sin(t)

        xs = np.concatenate([
            np.linspace(xr - r, xl + r, 20),
            c_tl_x,
            np.linspace(xl, xl, 10),
            c_bl_x,
            np.linspace(xl + r, xr - r, 20),
            c_br_x,
            np.linspace(xr, xr, 10),
            c_tr_x
        ])
        ys = np.concatenate([
            np.full(20, yt),
            c_tl_y,
            np.linspace(yt - r, yb + r, 10),
            c_bl_y,
            np.full(20, yb),
            c_br_y,
            np.linspace(yb + r, yt - r, 10),
            c_tr_y
        ])
        ax.plot(xs, ys, color=DEEP["blue"], lw=2.0, linestyle="--", alpha=0.9, zorder=3)

    # Add arrows to indicate circulation direction (clockwise)
    arrow_kw = dict(arrowstyle="-|>", mutation_scale=16, color=DEEP["blue"], lw=2.0, zorder=4)
    # Top moving left
    ax.annotate("", xy=(4.6, 5.1), xytext=(5.4, 5.1), arrowprops=arrow_kw)
    # Bottom moving right
    ax.annotate("", xy=(5.4, 2.1), xytext=(4.6, 2.1), arrowprops=arrow_kw)
    # Left moving down
    ax.annotate("", xy=(1.8, 3.2), xytext=(1.8, 4.0), arrowprops=arrow_kw)
    # Right moving up
    ax.annotate("", xy=(8.2, 4.0), xytext=(8.2, 3.2), arrowprops=arrow_kw)

    # Draw Magnets (shaded translucent or with distinct border so field lines inside are visible)
    # Top Magnet: N (left, PINK/reddish) and S (right, BLUE)
    # Half width = (7.8 - 2.2)/2 = 2.8, mid = 5.0
    top_n = patches.Rectangle((2.2, 4.6), 2.8, 1.0, facecolor=PINK, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    top_s = patches.Rectangle((5.0, 4.6), 2.8, 1.0, facecolor=BLUE, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    ax.add_patch(top_n)
    ax.add_patch(top_s)

    # Bottom Magnet: S (left, BLUE) and N (right, PINK)
    bot_s = patches.Rectangle((2.2, 1.6), 2.8, 1.0, facecolor=BLUE, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    bot_n = patches.Rectangle((5.0, 1.6), 2.8, 1.0, facecolor=PINK, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    ax.add_patch(bot_s)
    ax.add_patch(bot_n)

    # Keepers: Soft iron bars on left and right
    keeper_l = patches.Rectangle((1.4, 1.6), 0.8, 4.0, facecolor=GREY, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    keeper_r = patches.Rectangle((7.8, 1.6), 0.8, 4.0, facecolor=GREY, edgecolor=INK, lw=2, alpha=0.7, zorder=2)
    ax.add_patch(keeper_l)
    ax.add_patch(keeper_r)

    # Pole labels (N and S)
    label_kw = dict(fontsize=18, fontweight="bold", color=INK, ha="center", va="center", zorder=5)
    # Top magnet poles
    ax.text(2.8, 5.1, "N", **label_kw)
    ax.text(7.2, 5.1, "S", **label_kw)
    # Bottom magnet poles
    ax.text(2.8, 2.1, "S", **label_kw)
    ax.text(7.2, 2.1, "N", **label_kw)

    # Magnet body labels
    ax.text(5.0, 5.9, "Bar Magnet", fontsize=15, color=INK, ha="center", va="bottom",
            bbox=dict(fc="white", ec="none", pad=2))
    ax.text(5.0, 1.3, "Bar Magnet", fontsize=15, color=INK, ha="center", va="top",
            bbox=dict(fc="white", ec="none", pad=2))

    # Keepers annotations
    ax.annotate("Keeper\n(soft iron)", xy=(1.4, 3.6), xytext=(0.3, 3.6),
                fontsize=14, color=INK, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.annotate("Keeper\n(soft iron)", xy=(8.6, 3.6), xytext=(9.7, 3.6),
                fontsize=14, color=INK, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    # Magnetic field lines annotation
    ax.annotate("Continuous magnetic\nfield loop", xy=(5.0, 4.85), xytext=(5.0, 3.6),
                fontsize=14, color=DEEP["blue"], ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.5),
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3"))

    # Overall diagram title
    ax.text(5.0, 6.9, "Storing Bar Magnets with Soft Iron Keepers",
            fontsize=17, fontweight="bold", color=INK, ha="center", va="top")

    save(fig, out)
