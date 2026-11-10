from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 15.5)
    ax.set_ylim(-1.5, 7.5)
    ax.axis("off")

    # Title
    ax.text(7.5, 7.0, "Image Formation in the Human Eye", fontsize=16, weight="bold", color=INK, ha="center")

    # 1. Object: Upright Green Mango Tree (Left side)
    obj_x = 1.2
    obj_y_bot = 1.8
    obj_y_top = 4.4
    
    trunk = Polygon([[obj_x-0.1, obj_y_bot], [obj_x+0.1, obj_y_bot], [obj_x+0.07, 2.8], [obj_x-0.07, 2.8]], closed=True, fc="#8B5A2B", ec=INK, lw=1.5, zorder=3)
    ax.add_patch(trunk)
    crown_pts = [
        (obj_x, obj_y_top), (obj_x-0.45, 4.0), (obj_x-0.7, 3.4), (obj_x-0.5, 2.8), (obj_x-0.2, 2.7),
        (obj_x+0.2, 2.7), (obj_x+0.5, 2.8), (obj_x+0.7, 3.4), (obj_x+0.45, 4.0)
    ]
    crown = Polygon(crown_pts, closed=True, fc=GREEN, ec=DEEP["green"], lw=2, zorder=3)
    ax.add_patch(crown)
    ax.add_patch(Ellipse((0.85, 3.3), 0.15, 0.22, angle=-20, fc=ORANGE, ec=INK, lw=1, zorder=4))
    ax.add_patch(Ellipse((1.5, 3.1), 0.15, 0.22, angle=15, fc=ORANGE, ec=INK, lw=1, zorder=4))
    ax.add_patch(Ellipse((1.15, 3.7), 0.15, 0.22, angle=10, fc=ORANGE, ec=INK, lw=1, zorder=4))

    ax.text(obj_x, 1.1, "object", ha="center", va="top", fontsize=13, fontweight="bold", color=INK)

    obj_top = np.array([obj_x, obj_y_top])
    obj_bot = np.array([obj_x, obj_y_bot])

    # 2. Eye Geometry
    eye_cx, eye_cy = 9.0, 3.0
    R = 1.6

    thetas = np.linspace(-np.pi * 0.72, np.pi * 0.72, 150)
    eyeball_x = eye_cx + R * np.cos(thetas)
    eyeball_y = eye_cy + R * np.sin(thetas)

    cornea_t = np.linspace(np.pi * 0.72, np.pi * 1.28, 60)
    cornea_x = (eye_cx - 0.42) + (R * 0.92) * np.cos(cornea_t)
    cornea_y = eye_cy + (R * 0.92) * np.sin(cornea_t)

    ax.plot(eyeball_x, eyeball_y, color=INK, lw=2.5, zorder=2)
    ax.plot(cornea_x, cornea_y, color=DEEP["blue"], lw=2.5, zorder=2)

    retina_t = np.linspace(-np.pi * 0.58, np.pi * 0.58, 120)
    ret_R = R - 0.08
    ret_x = eye_cx + ret_R * np.cos(retina_t)
    ret_y = eye_cy + ret_R * np.sin(retina_t)
    ax.plot(ret_x, ret_y, color=DEEP["pink"], lw=4.5, zorder=2)

    lens_x, lens_y = 7.75, 3.0
    lens = Ellipse((lens_x, lens_y), 0.38, 1.4, fc=BLUE, ec=DEEP["blue"], lw=2, alpha=0.85, zorder=5)
    ax.add_patch(lens)

    c_top1 = np.array([7.18, 3.45])
    c_top2 = np.array([7.06, 3.16])
    c_bot1 = np.array([7.06, 2.84])
    c_bot2 = np.array([7.18, 2.55])

    l_top1 = np.array([7.75, 3.45])
    l_top2 = np.array([7.75, 3.15])
    l_bot1 = np.array([7.75, 2.85])
    l_bot2 = np.array([7.75, 2.55])

    # Ensure focus points are exactly on the retina curve
    focus_top_y = 2.45
    focus_top_x = eye_cx + np.sqrt(ret_R**2 - (focus_top_y - eye_cy)**2)
    focus_top = np.array([focus_top_x, focus_top_y])
    
    focus_bot_y = 3.55
    focus_bot_x = eye_cx + np.sqrt(ret_R**2 - (focus_bot_y - eye_cy)**2)
    focus_bot = np.array([focus_bot_x, focus_bot_y])

    # Draw straight rays from object to cornea, through lens, converging on retina
    ax.plot([obj_top[0], c_top1[0], l_top1[0], focus_top[0]],
            [obj_top[1], c_top1[1], l_top1[1], focus_top[1]],
            color=DEEP["pink"], lw=1.8, zorder=3)
    ax.plot([obj_top[0], c_top2[0], l_top2[0], focus_top[0]],
            [obj_top[1], c_top2[1], l_top2[1], focus_top[1]],
            color=DEEP["pink"], lw=1.8, zorder=3)

    ax.plot([obj_bot[0], c_bot1[0], l_bot1[0], focus_bot[0]],
            [obj_bot[1], c_bot1[1], l_bot1[1], focus_bot[1]],
            color=DEEP["blue"], lw=1.8, zorder=3)
    ax.plot([obj_bot[0], c_bot2[0], l_bot2[0], focus_bot[0]],
            [obj_bot[1], c_bot2[1], l_bot2[1], focus_bot[1]],
            color=DEEP["blue"], lw=1.8, zorder=3)

    def add_arrow(p1, p2, col):
        pm = 0.52 * p1 + 0.48 * p2
        d = p2 - p1
        d = d / np.hypot(*d) * 0.16
        ax.annotate("", xy=pm + d, xytext=pm - d,
                    arrowprops=dict(arrowstyle="->", color=col, lw=1.8, mutation_scale=12))

    add_arrow(obj_top, c_top1, DEEP["pink"])
    add_arrow(obj_top, c_top2, DEEP["pink"])
    add_arrow(obj_bot, c_bot1, DEEP["blue"])
    add_arrow(obj_bot, c_bot2, DEEP["blue"])

    # 3. Small Inverted Tree Image on Retina matching focal points exactly
    inv_x_bot = focus_bot[0]
    inv_y_bot = focus_bot[1]
    inv_x_top = focus_top[0]
    inv_y_top = focus_top[1]
    
    # Line up the inverted trunk and crown directly between focus_bot and focus_top
    mid_y = (inv_y_bot + inv_y_top) / 2 + 0.15 # Crown/trunk split
    
    inv_trunk = Polygon([[inv_x_bot-0.04, inv_y_bot], [inv_x_bot+0.04, inv_y_bot], 
                         [inv_x_bot+0.02, mid_y], [inv_x_bot-0.02, mid_y]],
                        closed=True, fc="#8B5A2B", ec=INK, lw=1.2, zorder=6)
    ax.add_patch(inv_trunk)

    inv_crown_pts = [
        (inv_x_top, inv_y_top), (inv_x_top-0.15, inv_y_top+0.2), (inv_x_top-0.25, inv_y_top+0.45), 
        (inv_x_bot-0.15, mid_y), (inv_x_bot+0.15, mid_y), 
        (inv_x_top+0.25, inv_y_top+0.45), (inv_x_top+0.15, inv_y_top+0.2)
    ]
    inv_crown = Polygon(inv_crown_pts, closed=True, fc=GREEN, ec=DEEP["green"], lw=1.5, zorder=6)
    ax.add_patch(inv_crown)

    ax.plot([inv_x_top-0.08], [inv_y_top+0.4], 'o', color=ORANGE, markersize=3.5, zorder=7)
    ax.plot([inv_x_top+0.08], [inv_y_top+0.3], 'o', color=ORANGE, markersize=3.5, zorder=7)

    # 4. Optic Nerve
    nerve_x = [10.58, 11.2, 11.9, 12.7]
    nerve_y1 = [2.88, 2.82, 2.92, 3.10]
    nerve_y2 = [2.68, 2.62, 2.72, 2.90]
    ax.fill_between(nerve_x, nerve_y1, nerve_y2, color="#FCD34D", ec=DEEP["orange"], lw=1.5, zorder=2)

    # 5. Brain outline
    brain_pts = [
        (12.7, 3.0), (12.7, 3.6), (13.0, 4.4), (13.5, 4.8),
        (14.2, 4.7), (14.7, 4.2), (14.9, 3.5), (14.7, 2.8),
        (14.3, 2.5), (13.9, 2.7), (13.5, 2.7), (13.1, 2.8)
    ]
    brain_poly = Polygon(brain_pts, closed=True, fc=CREAM, ec=INK, lw=2, zorder=2)
    ax.add_patch(brain_poly)

    occipital_pts = [
        (14.2, 4.7), (14.7, 4.2), (14.9, 3.5), (14.7, 2.8), (14.3, 2.5),
        (14.1, 3.1), (14.2, 4.0)
    ]
    occipital_poly = Polygon(occipital_pts, closed=True, fc=LAV, ec=DEEP["lav"], lw=1.5, zorder=3)
    ax.add_patch(occipital_poly)

    # 6. Labels
    bbox_style = dict(fc="white", ec=GREY, boxstyle="round,pad=0.25")

    ax.annotate("light rays", xy=(4.2, 3.3), xytext=(4.2, 5.2),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("cornea", xy=(7.05, 3.6), xytext=(6.2, 5.2),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("lens", xy=(7.75, 3.7), xytext=(7.75, 5.7),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("retina", xy=(10.15, 4.15), xytext=(9.9, 5.9),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("inverted image", xy=(10.45, 3.0), xytext=(9.2, 0.9),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("optic nerve", xy=(11.5, 2.76), xytext=(11.5, 1.2),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    ax.annotate("visual area of brain", xy=(14.5, 3.5), xytext=(13.9, 5.7),
                fontsize=13, fontweight="bold", color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4),
                bbox=bbox_style)

    save(fig, out)
    plt.close(fig)
