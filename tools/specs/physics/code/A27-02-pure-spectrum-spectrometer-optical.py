import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from style import *

def draw(out):
    fig = canvas(15, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 15.2)
    ax.set_ylim(-1.6, 6.8)
    ax.set_aspect('equal')
    ax.axis('off')

    c_white = "#555555"
    c_red = DEEP["orange"]
    c_green = DEEP["green"]
    c_violet = DEEP["lav"]

    # 1. Light Source (left)
    source_x, source_y = 0.5, 3.2
    ax.scatter([source_x], [source_y], color=ORANGE, s=360, zorder=5, edgecolor=DEEP["orange"], lw=2)
    ax.plot([source_x, source_x], [source_y - 0.75, source_y - 0.28], color=INK, lw=3)
    ax.text(source_x, source_y - 1.15, "Light\nsource", ha="center", va="top", fontsize=15, color=INK)

    # 2. Narrow vertical slit
    slit_x = 1.9
    slit_w = 0.14
    slit_gap = 0.36
    ax.fill([slit_x - slit_w/2, slit_x + slit_w/2, slit_x + slit_w/2, slit_x - slit_w/2],
            [source_y + slit_gap/2, source_y + slit_gap/2, 5.2, 5.2], color=INK)
    ax.fill([slit_x - slit_w/2, slit_x + slit_w/2, slit_x + slit_w/2, slit_x - slit_w/2],
            [1.2, 1.2, source_y - slit_gap/2, source_y - slit_gap/2], color=INK)
    ax.text(slit_x, 5.4, "Narrow slit", ha="center", va="bottom", fontsize=14, color=INK)

    # Rays from source through slit to Collimator lens
    lens1_x = 3.6
    ax.plot([source_x, slit_x, lens1_x], [source_y, source_y + 0.12, source_y + 0.95], color=c_white, lw=1.5, ls="--")
    ax.plot([source_x, slit_x, lens1_x], [source_y, source_y, source_y], color=c_white, lw=1.5, ls="--")
    ax.plot([source_x, slit_x, lens1_x], [source_y, source_y - 0.12, source_y - 0.95], color=c_white, lw=1.5, ls="--")

    # 3. Collimator Lens (Converging L1)
    lens1_semi_h = 1.6
    lens_arc1 = np.linspace(-lens1_semi_h, lens1_semi_h, 50)
    thick1 = 0.22 * (1 - (lens_arc1 / lens1_semi_h)**2)
    ax.fill_betweenx(source_y + lens_arc1, lens1_x - thick1, lens1_x + thick1, color=BLUE, alpha=0.35, ec=DEEP["blue"], lw=1.6)
    ax.text(lens1_x, source_y - 2.0, "Collimating lens\n(L₁)", ha="center", va="top", fontsize=14, color=INK)

    # 4. Parallel beam of white light
    y_rays = [source_y + 0.7, source_y, source_y - 0.7]
    prism_entry_x = 5.5
    for y_ray in y_rays:
        ax.plot([lens1_x, prism_entry_x], [y_ray, y_ray], color=c_white, lw=2.2)
    ax.text((lens1_x + prism_entry_x) / 2, source_y + 1.1, "Parallel beam of\nwhite light",
            ha="center", va="bottom", fontsize=14, color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))

    # 5. Triangular Prism
    p_apex = [6.5, 5.2]
    p_base_l = [5.2, 1.0]
    p_base_r = [7.8, 1.0]
    prism = Polygon([p_apex, p_base_l, p_base_r], facecolor=LAV, edgecolor=DEEP["lav"], alpha=0.45, lw=2, zorder=2)
    ax.add_patch(prism)
    ax.text(6.5, 5.5, "Prism", ha="center", va="bottom", fontsize=15, color=INK, fontweight="bold")

    # Geometry of prism faces
    def left_face_x(y):
        return p_base_l[0] + (y - p_base_l[1]) * (p_apex[0] - p_base_l[0]) / (p_apex[1] - p_base_l[1])

    def right_face_x(y):
        return p_apex[0] + (p_apex[1] - y) * (p_base_r[0] - p_apex[0]) / (p_apex[1] - p_base_r[1])

    # Telescope lens L2 parameters (sufficiently tall and centered to capture all refracted rays)
    lens2_x = 10.2
    lens2_y = 2.4
    lens2_semi_h = 2.5
    lens_arc2 = np.linspace(-lens2_semi_h, lens2_semi_h, 60)
    thick2 = 0.26 * (1 - (lens_arc2 / lens2_semi_h)**2)
    ax.fill_betweenx(lens2_y + lens_arc2, lens2_x - thick2, lens2_x + thick2, color=BLUE, alpha=0.35, ec=DEEP["blue"], lw=1.6, zorder=3)
    ax.text(lens2_x, lens2_y - lens2_semi_h - 0.35, "Telescope lens\n(L₂)", ha="center", va="top", fontsize=14, color=INK)

    # Screen parameters
    screen_x = 13.0
    f_red_y = 3.3
    f_green_y = 2.4
    f_violet_y = 1.5

    # Angles of parallel bundles exiting the prism (in radians)
    theta_r = -6.0 * np.pi / 180
    theta_g = -13.0 * np.pi / 180
    theta_v = -20.0 * np.pi / 180

    # Ray tracing through prism to screen
    for yi in y_rays:
        x_ent = left_face_x(yi)
        # Inside prism
        y_exit_r = yi - 0.20
        y_exit_g = yi - 0.34
        y_exit_v = yi - 0.48

        x_exit_r = right_face_x(y_exit_r)
        x_exit_g = right_face_x(y_exit_g)
        x_exit_v = right_face_x(y_exit_v)

        ax.plot([x_ent, x_exit_r], [yi, y_exit_r], color=c_red, lw=1.6, alpha=0.85)
        ax.plot([x_ent, x_exit_g], [yi, y_exit_g], color=c_green, lw=1.6, alpha=0.85)
        ax.plot([x_ent, x_exit_v], [yi, y_exit_v], color=c_violet, lw=1.6, alpha=0.85)

        # Prism to Lens 2 (parallel beams)
        y_lens_r = y_exit_r + np.tan(theta_r) * (lens2_x - x_exit_r)
        y_lens_g = y_exit_g + np.tan(theta_g) * (lens2_x - x_exit_g)
        y_lens_v = y_exit_v + np.tan(theta_v) * (lens2_x - x_exit_v)

        ax.plot([x_exit_r, lens2_x], [y_exit_r, y_lens_r], color=c_red, lw=1.8)
        ax.plot([x_exit_g, lens2_x], [y_exit_g, y_lens_g], color=c_green, lw=1.8)
        ax.plot([x_exit_v, lens2_x], [y_exit_v, y_lens_v], color=c_violet, lw=1.8)

        # Lens 2 to focal points on screen
        ax.plot([lens2_x, screen_x], [y_lens_r, f_red_y], color=c_red, lw=1.8)
        ax.plot([lens2_x, screen_x], [y_lens_g, f_green_y], color=c_green, lw=1.8)
        ax.plot([lens2_x, screen_x], [y_lens_v, f_violet_y], color=c_violet, lw=1.8)

    # Parallel bundle labels with white bbox to prevent ray overlapping
    bbox_fmt = dict(fc="white", ec="none", pad=1.5)
    ax.text(8.7, 3.8, "Parallel bundle (Red)", ha="center", va="bottom",
            fontsize=14, color=c_red, fontweight="bold", bbox=bbox_fmt)
    ax.text(8.7, 2.7, "Parallel bundle (Green)", ha="center", va="center",
            fontsize=14, color=c_green, fontweight="bold", bbox=bbox_fmt)
    ax.text(8.7, 1.25, "Parallel bundle (Violet)", ha="center", va="top",
            fontsize=14, color=c_violet, fontweight="bold", bbox=bbox_fmt)

    # 6. Screen
    screen_w = 0.16
    screen_bot = 0.6
    screen_top = 4.3
    ax.fill([screen_x - screen_w/2, screen_x + screen_w/2, screen_x + screen_w/2, screen_x - screen_w/2],
            [screen_bot, screen_bot, screen_top, screen_top], color=GREY, ec=INK, lw=1.5, zorder=4)
    ax.text(screen_x, screen_top + 0.3, "White screen", ha="center", va="bottom", fontsize=15, color=INK, fontweight="bold")

    # Focused color spots on the screen
    ax.scatter([screen_x], [f_red_y], color=c_red, s=90, zorder=6)
    ax.scatter([screen_x], [f_green_y], color=c_green, s=90, zorder=6)
    ax.scatter([screen_x], [f_violet_y], color=c_violet, s=90, zorder=6)

    ax.text(screen_x + 0.35, f_red_y, "Red (R)", va="center", ha="left", fontsize=14, color=c_red, fontweight="bold")
    ax.text(screen_x + 0.35, f_green_y, "Green (G)", va="center", ha="left", fontsize=14, color=c_green, fontweight="bold")
    ax.text(screen_x + 0.35, f_violet_y, "Violet (V)", va="center", ha="left", fontsize=14, color=c_violet, fontweight="bold")

    # Pure spectrum bracket annotation
    ax.annotate("Pure\nspectrum", xy=(screen_x + 1.9, (f_red_y + f_violet_y) / 2),
                ha="center", va="center", fontsize=15, color=INK, fontweight="bold",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35"))

    # Diagram Title
    ax.text(7.2, 6.4, "Optical Setup for Producing a Pure Spectrum",
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

    save(fig, out)
