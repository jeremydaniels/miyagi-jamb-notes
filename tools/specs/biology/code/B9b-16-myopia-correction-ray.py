from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 9)
    
    # Two subplots (axes) with comfortable spacing
    ax1 = fig.add_axes([0.05, 0.52, 0.90, 0.42])
    ax2 = fig.add_axes([0.05, 0.05, 0.90, 0.42])

    for ax in (ax1, ax2):
        ax.set_xlim(-1, 14.5)
        ax.set_ylim(-3.5, 3.5)
        ax.set_aspect('equal')
        ax.axis('off')

    def draw_eyeball(ax, cx=7.5, cy=0.0, rx=3.2, ry=2.2):
        # Sclera outline (elongated eyeball)
        t = np.linspace(-np.pi * 0.82, np.pi * 0.82, 200)
        x_sclera = cx + rx * np.cos(t)
        y_sclera = cy + ry * np.sin(t)

        # Cornea arc bulging out to the left
        t_cornea = np.linspace(-np.pi * 0.42, np.pi * 0.42, 100)
        x_cornea = (cx - rx + 0.6) - 1.2 * np.cos(t_cornea)
        y_cornea = cy + 1.35 * np.sin(t_cornea)

        # Retina highlighted arc at the back
        t_retina = np.linspace(-np.pi * 0.35, np.pi * 0.35, 100)
        x_retina = cx + rx * np.cos(t_retina)
        y_retina = cy + ry * np.sin(t_retina)
        ax.plot(x_retina, y_retina, color=DEEP["pink"], lw=5.0, zorder=2)

        # Combine sclera and cornea outline
        ax.plot(x_sclera, y_sclera, color=INK, lw=2.2, zorder=3)
        ax.plot(x_cornea, y_cornea, color=INK, lw=2.2, zorder=3)

        # Crystalline lens inside eye
        lens_x = cx - rx + 1.4
        lens_ellipse = patches.Ellipse((lens_x, cy), 0.5, 2.0, color=LAV, ec=DEEP["lav"], lw=1.8, zorder=4)
        ax.add_patch(lens_ellipse)

        # Optic nerve stalk at the back
        ax.plot([cx + rx, cx + rx + 0.8], [cy + 0.3, cy + 0.4], color=INK, lw=2.0)
        ax.plot([cx + rx, cx + rx + 0.8], [cy - 0.3, cy - 0.4], color=INK, lw=2.0)

        # Optical axis dashed line
        ax.plot([-0.5, cx + rx + 0.6], [cy, cy], color=GREY, ls='--', lw=1.0, zorder=1)

        return lens_x

    # Common eyeball geometry parameters
    cx, rx = 7.5, 3.2
    retina_x = cx + rx  # 10.7
    y_rays = [1.0, 0.4, -0.4, -1.0]
    ray_color = DEEP["orange"]

    # =========================================================================
    # TOP PANEL: Uncorrected Myopia
    # =========================================================================
    lens_x1 = draw_eyeball(ax1, cx=cx, rx=rx)
    focal_x1 = 9.0  # inside eyeball, distinctly in front of retina (at 10.7)

    for yr in y_rays:
        # Incident parallel rays
        ax1.plot([0.0, lens_x1], [yr, yr], color=ray_color, lw=2.0, zorder=5)
        # Convergence towards focal point in front of retina
        ax1.plot([lens_x1, focal_x1], [yr, 0.0], color=ray_color, lw=2.0, zorder=5)
        # Spreading beyond focus towards retina
        slope = -yr / (focal_x1 - lens_x1)
        y_at_retina = slope * (retina_x - focal_x1)
        ax1.plot([focal_x1, retina_x], [0.0, y_at_retina], color=ray_color, lw=2.0, zorder=5)

    # Blurred patch on retina
    ax1.plot([retina_x, retina_x], [-0.55, 0.55], color=DEEP["pink"], lw=7.0, zorder=6, solid_capstyle='round')

    # Top Panel Title
    ax1.text(0.0, 3.0, "Uncorrected Myopia (Short-sightedness)", fontsize=14, weight='bold', color=INK)

    # Label: "rays from distant object"
    ax1.annotate("rays from distant object", xy=(1.5, 1.0), xytext=(0.5, 2.0),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: "long eyeball"
    ax1.annotate("long eyeball", xy=(cx + 0.8, 2.15), xytext=(cx + 1.2, 2.9),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: "focus in front of retina"
    ax1.annotate("focus in front of retina", xy=(focal_x1, 0.0), xytext=(focal_x1 - 2.2, -1.8),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: "blurred image"
    ax1.annotate("blurred image", xy=(retina_x, 0.0), xytext=(retina_x + 0.8, -1.2),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))


    # =========================================================================
    # BOTTOM PANEL: Corrected with Concave Lens
    # =========================================================================
    lens_x2 = draw_eyeball(ax2, cx=cx, rx=rx)
    concave_x = 2.4

    # Draw true biconcave lens: thin at center, thick at top and bottom ends
    lens_h = 2.6
    t_c = np.linspace(-lens_h/2, lens_h/2, 60)
    left_surface = concave_x - 0.08 - 0.20 * (t_c / (lens_h/2))**2
    right_surface = concave_x + 0.08 + 0.20 * (t_c / (lens_h/2))**2

    lens_poly_x = np.concatenate([left_surface, right_surface[::-1]])
    lens_poly_y = np.concatenate([t_c, t_c[::-1]])
    ax2.fill(lens_poly_x, lens_poly_y, color=BLUE, alpha=0.35, zorder=4)
    ax2.plot(left_surface, t_c, color=DEEP["blue"], lw=1.8, zorder=5)
    ax2.plot(right_surface, t_c, color=DEEP["blue"], lw=1.8, zorder=5)
    ax2.plot([left_surface[0], right_surface[0]], [t_c[0], t_c[0]], color=DEEP["blue"], lw=1.8, zorder=5)
    ax2.plot([left_surface[-1], right_surface[-1]], [t_c[-1], t_c[-1]], color=DEEP["blue"], lw=1.8, zorder=5)

    # Rays: concave lens spreads rays out slightly, then eye lens brings them to focus at retina
    focal_x2 = retina_x

    for yr in y_rays:
        # Parallel incident rays up to concave lens
        ax2.plot([0.0, concave_x], [yr, yr], color=ray_color, lw=2.0, zorder=5)
        # Spreading outwards after concave lens to eye lens
        div_yr = yr * 1.25
        ax2.plot([concave_x, lens_x2], [yr, div_yr], color=ray_color, lw=2.0, zorder=5)
        # Converging to meet exactly at retina
        ax2.plot([lens_x2, focal_x2], [div_yr, 0.0], color=ray_color, lw=2.0, zorder=5)

    # Sharp focus dot at retina
    ax2.plot(focal_x2, 0.0, 'o', color=DEEP["pink"], markersize=6, zorder=6)

    # Bottom Panel Title
    ax2.text(0.0, 3.0, "Corrected with Concave Lens", fontsize=14, weight='bold', color=INK)

    # Label: "concave lens"
    ax2.annotate("concave lens", xy=(concave_x, 1.2), xytext=(concave_x - 1.2, 2.0),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Label: "focus on retina"
    ax2.annotate("focus on retina", xy=(focal_x2, 0.0), xytext=(focal_x2 - 1.2, -1.8),
                 fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
