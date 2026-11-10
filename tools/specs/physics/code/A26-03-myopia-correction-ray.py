from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1.5, 11.5)
    ax.axis('off')

    def draw_eyeball(cy):
        R = 2.5
        # Eyeball main circular arc (excluding front where cornea is)
        t = np.linspace(0.48, 2 * np.pi - 0.48, 200)
        ex = 10 + R * np.cos(t)
        ey = cy + R * np.sin(t)
        
        # Cornea bulge on left
        tc = np.linspace(-np.pi / 3, np.pi / 3, 50)
        cx = 7.5 + 0.8 * (1 - np.cos(tc))
        cy_pts = cy + 1.2 * np.sin(tc)
        
        eye_poly_x = np.concatenate([ex, [cx[-1]], cx[::-1], [ex[0]]])
        eye_poly_y = np.concatenate([ey, [cy_pts[-1]], cy_pts[::-1], [ey[0]]])
        ax.fill(eye_poly_x, eye_poly_y, color=CREAM, alpha=0.4, zorder=1)
        ax.plot(ex, ey, color=GREY, lw=2.5, zorder=2)
        
        # Retina highlight along the back curved surface (around x=12.5)
        t_ret = np.linspace(-np.pi / 3, np.pi / 3, 100)
        ax.plot(10 + R * np.cos(t_ret), cy + R * np.sin(t_ret), color=DEEP["orange"], lw=5, zorder=3)

        # Eye natural biconvex lens at x=8.2
        lens_h = 1.3
        lens_w = 0.35
        lens = patches.Ellipse((8.2, cy), lens_w * 2, lens_h * 2,
                               facecolor=BLUE, edgecolor=DEEP["blue"], lw=2, alpha=0.7, zorder=4)
        ax.add_patch(lens)
        
        # Optic axis
        ax.plot([0.5, 12.8], [cy, cy], color=GREY, linestyle='--', lw=1.2, zorder=1)

    # ==========================
    # --- TOP: UNCORRECTED ---
    # ==========================
    y_top = 7.8
    draw_eyeball(y_top)

    r_in = 1.0
    f_x = 10.6    # Focal point before retina
    ret_x = 12.5  # Retina position
    slope = r_in / (f_x - 8.2)
    blur_h = slope * (ret_x - f_x)

    # Ray bundle fill (shaded light beam)
    ray_x_top = [0.8, 8.2, f_x, ret_x, ret_x, f_x, 8.2, 0.8]
    ray_y_top = [y_top + r_in, y_top + r_in, y_top, y_top - blur_h,
                 y_top + blur_h, y_top, y_top - r_in, y_top - r_in]
    ax.fill(ray_x_top, ray_y_top, color=PINK, alpha=0.25, zorder=4)

    # Top boundary rays
    ax.plot([0.8, 8.2], [y_top + r_in, y_top + r_in], color=DEEP["pink"], lw=2.5, zorder=5)
    ax.plot([8.2, f_x, ret_x], [y_top + r_in, y_top, y_top - blur_h], color=DEEP["pink"], lw=2.5, zorder=5)

    ax.plot([0.8, 8.2], [y_top - r_in, y_top - r_in], color=DEEP["pink"], lw=2.5, zorder=5)
    ax.plot([8.2, f_x, ret_x], [y_top - r_in, y_top, y_top + blur_h], color=DEEP["pink"], lw=2.5, zorder=5)

    # Blur circle on retina
    ax.plot([ret_x, ret_x], [y_top - blur_h, y_top + blur_h], color=DEEP["pink"], lw=5.5, solid_capstyle='round', zorder=6)

    # Focus point marker
    ax.scatter([f_x], [y_top], color=DEEP["pink"], s=45, zorder=6)

    # Annotations - Top
    ax.text(0.5, y_top + 2.5, "Uncorrected Myopia (Short-sightedness)", fontsize=17, fontweight='bold', color=INK)
    ax.text(1.3, y_top + 1.4, "Parallel rays\nfrom infinity", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec="none", pad=2))

    ax.annotate("Focal point\nin front of retina", xy=(f_x, y_top), xytext=(f_x - 1.2, y_top + 1.8),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Blurred circle\non retina", xy=(ret_x, y_top - blur_h / 2), xytext=(ret_x + 0.5, y_top - 1.4),
                fontsize=14, color=INK, ha='left',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.text(12.7, y_top + 1.2, "Retina", fontsize=14, color=DEEP["orange"], fontweight='bold')

    # ==========================
    # --- BOTTOM: CORRECTED ---
    # ==========================
    y_bot = 2.0
    draw_eyeball(y_bot)

    # Concave lens parameters: thinner at center, thicker at edges
    # Left surface curves inward (bulges rightward at center, or indented at x=5.5)
    # Right surface curves inward (indented leftward at center)
    lx = 5.2
    lh = 1.6
    yc = np.linspace(-lh, lh, 60)
    # At center (y=0), width is minimum (~0.12); at edges (|y|=lh), width is larger (~0.44)
    curve_in = 0.16 * (1.0 - (yc / lh)**2)
    x_left = (lx - 0.22) + curve_in
    x_right = (lx + 0.22) - curve_in

    concave_x = np.concatenate([x_left, x_right[::-1]])
    concave_y = y_bot + np.concatenate([yc, yc[::-1]])
    ax.fill(concave_x, concave_y, color=LAV, alpha=0.75, zorder=5)
    ax.plot(concave_x, concave_y, color=DEEP["lav"], lw=2, zorder=5)

    # Rays for Bottom diagram
    # Parallel rays arrive at concave lens x=5.2 with height r_lens_in = 1.0
    # Diverge slightly on passing through concave lens: height at eye lens (x=8.2) is r_div = 1.25
    # Eye lens converges them exactly to retina at x=12.5, y=y_bot
    r_lens_in = 1.0
    r_div = 1.25

    # Ray bundle fill (shaded light beam matching the green boundary rays)
    ray_x_bot = [0.8, lx, 8.2, ret_x, 8.2, lx, 0.8]
    ray_y_bot = [y_bot + r_lens_in, y_bot + r_lens_in, y_bot + r_div, y_bot,
                 y_bot - r_div, y_bot - r_lens_in, y_bot - r_lens_in]
    ax.fill(ray_x_bot, ray_y_bot, color=GREEN, alpha=0.25, zorder=4)

    # Green ray lines
    ax.plot([0.8, lx], [y_bot + r_lens_in, y_bot + r_lens_in], color=DEEP["green"], lw=2.5, zorder=6)
    ax.plot([lx, 8.2], [y_bot + r_lens_in, y_bot + r_div], color=DEEP["green"], lw=2.5, zorder=6)
    ax.plot([8.2, ret_x], [y_bot + r_div, y_bot], color=DEEP["green"], lw=2.5, zorder=6)

    ax.plot([0.8, lx], [y_bot - r_lens_in, y_bot - r_lens_in], color=DEEP["green"], lw=2.5, zorder=6)
    ax.plot([lx, 8.2], [y_bot - r_lens_in, y_bot - r_div], color=DEEP["green"], lw=2.5, zorder=6)
    ax.plot([8.2, ret_x], [y_bot - r_div, y_bot], color=DEEP["green"], lw=2.5, zorder=6)

    # Sharp focus point marker exactly on retina
    ax.scatter([ret_x], [y_bot], color=DEEP["green"], s=55, zorder=7)

    # Annotations - Bottom
    ax.text(0.5, y_bot + 2.5, "Corrected Myopia (Using Concave Lens)", fontsize=17, fontweight='bold', color=INK)

    ax.annotate("Concave lens\n(diverging lens)", xy=(lx, y_bot - lh), xytext=(lx - 1.1, y_bot - 2.5),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Rays diverge\nslightly", xy=(6.7, y_bot + 1.13), xytext=(6.4, y_bot + 2.0),
                fontsize=14, color=INK, ha='center',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.annotate("Sharp focus\non retina", xy=(ret_x, y_bot), xytext=(ret_x + 0.5, y_bot - 1.4),
                fontsize=14, color=INK, ha='left',
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))

    ax.text(12.7, y_bot + 1.2, "Retina", fontsize=14, color=DEEP["orange"], fontweight='bold')

    save(fig, out)
