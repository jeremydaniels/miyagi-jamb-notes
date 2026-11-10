from style import *
import numpy as np
import matplotlib.patches as patches

def draw_eyeball(ax, cx, cy, rx, ry):
    # Short eyeball: ellipse
    theta = np.linspace(-np.pi, np.pi, 200)
    x = cx + rx * np.cos(theta)
    y = cy + ry * np.sin(theta)
    
    # Outer white/cream sclera fill
    ax.fill(x, y, color=CREAM, zorder=1)
    ax.plot(x, y, color=INK, lw=2, zorder=2)
    
    # Cornea bulge on the left (around theta = pi)
    cornea_theta = np.linspace(np.pi - 0.7, np.pi + 0.7, 50)
    xc = cx + rx * np.cos(cornea_theta) - 0.25 * np.cos((cornea_theta - np.pi) * (np.pi / 1.4))
    yc = cy + ry * np.sin(cornea_theta)
    ax.fill(xc, yc, color=CREAM, zorder=1)
    ax.plot(xc, yc, color=INK, lw=2, zorder=2)
    
    # Eye lens (crystalline lens)
    lens_x = cx - rx + 0.45
    lens = patches.Ellipse((lens_x, cy), 0.35, 1.4, color=BLUE, alpha=0.35, ec=DEEP["blue"], lw=1.8, zorder=3)
    ax.add_patch(lens)
    
    # Retina line at the back (arc around theta = 0)
    retina_theta = np.linspace(-0.9, 0.9, 60)
    xr = cx + rx * np.cos(retina_theta)
    yr = cy + ry * np.sin(retina_theta)
    ax.plot(xr, yr, color=DEEP["pink"], lw=3.5, zorder=3)
    
    return lens_x

def draw(out):
    fig = canvas(12, 8.5)
    
    # Top Panel: Uncorrected Hypermetropia
    ax1 = fig.add_axes([0.05, 0.52, 0.9, 0.44])
    ax1.set_xlim(-0.5, 11.5)
    ax1.set_ylim(-2.2, 2.2)
    ax1.axis('off')
    
    # Bottom Panel: Corrected Hypermetropia
    ax2 = fig.add_axes([0.05, 0.04, 0.9, 0.44])
    ax2.set_xlim(-0.5, 11.5)
    ax2.set_ylim(-2.2, 2.2)
    ax2.axis('off')
    
    # Common parameters
    obj_x = 0.5
    obj_y = 0.0
    cx = 7.0
    cy = 0.0
    rx = 2.0  # shortened eyeball
    ry = 1.8
    retina_x = cx + rx  # 9.0
    
    # ------------------ TOP PANEL ------------------
    ax1.text(0.2, 1.8, "Uncorrected Hypermetropia (Long-sightedness)", fontsize=14, fontweight='bold', color=INK)
    
    lx1 = draw_eyeball(ax1, cx, cy, rx, ry)
    
    # Object point
    ax1.plot(obj_x, obj_y, marker='o', color=DEEP["orange"], markersize=6, zorder=5)
    
    # Near object rays diverging to eye lens
    lens_top_y = 0.55
    lens_bot_y = -0.55
    
    ax1.plot([obj_x, lx1], [obj_y, lens_top_y], color=DEEP["orange"], lw=2, zorder=4)
    ax1.plot([obj_x, lx1], [obj_y, lens_bot_y], color=DEEP["orange"], lw=2, zorder=4)
    ax1.plot([obj_x, lx1], [obj_y, 0], color=DEEP["orange"], lw=2, zorder=4)
    
    # Behind retina focus point
    focus_x1 = 10.4
    focus_y1 = 0.0
    
    # Rays inside eye (refracted by eye lens, heading towards focus_x1)
    # Intersect with retina around x = retina_x = 9.0
    ret_y_top = lens_top_y + (focus_y1 - lens_top_y) * (retina_x - lx1) / (focus_x1 - lx1)
    ret_y_bot = lens_bot_y + (focus_y1 - lens_bot_y) * (retina_x - lx1) / (focus_x1 - lx1)
    
    ax1.plot([lx1, retina_x], [lens_top_y, ret_y_top], color=DEEP["orange"], lw=2, zorder=4)
    ax1.plot([lx1, retina_x], [lens_bot_y, ret_y_bot], color=DEEP["orange"], lw=2, zorder=4)
    ax1.plot([lx1, retina_x], [0, 0], color=DEEP["orange"], lw=2, zorder=4)
    
    # Dashed continuation to focus behind retina
    ax1.plot([retina_x, focus_x1], [ret_y_top, focus_y1], color=DEEP["orange"], lw=1.8, ls='--', zorder=4)
    ax1.plot([retina_x, focus_x1], [ret_y_bot, focus_y1], color=DEEP["orange"], lw=1.8, ls='--', zorder=4)
    ax1.plot([retina_x, focus_x1], [0, 0], color=DEEP["orange"], lw=1.8, ls='--', zorder=4)
    ax1.plot(focus_x1, focus_y1, marker='x', color=DEEP["orange"], markersize=8, mew=2, zorder=5)
    
    # Blurred patch on retina
    ax1.plot([retina_x, retina_x], [ret_y_bot, ret_y_top], color=DEEP["pink"], lw=4.5, zorder=5)
    
    # Labels Top Panel
    ax1.annotate("rays from near object", xy=(1.8, 0.25), xytext=(1.8, 1.2),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
                 
    ax1.annotate("short eyeball", xy=(cx, 1.8), xytext=(cx, 2.05),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))
                 
    ax1.annotate("blurred image", xy=(retina_x, (ret_y_top + ret_y_bot)/2), xytext=(8.0, 1.4),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
                 
    ax1.annotate("focus behind retina", xy=(focus_x1, focus_y1), xytext=(10.4, 0.9),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
                 

    # ------------------ BOTTOM PANEL ------------------
    ax2.text(0.2, 1.8, "Corrected with Convex Lens", fontsize=14, fontweight='bold', color=INK)
    
    lx2 = draw_eyeball(ax2, cx, cy, rx, ry)
    
    # Convex spectacle lens in front of eye
    glasses_x = 4.0
    convex_lens = patches.Ellipse((glasses_x, cy), 0.35, 1.6, color=LAV, alpha=0.45, ec=DEEP["lav"], lw=2, zorder=3)
    ax2.add_patch(convex_lens)
    
    # Object point
    ax2.plot(obj_x, obj_y, marker='o', color=DEEP["orange"], markersize=6, zorder=5)
    
    # Rays to convex lens
    g_top_y = 0.6
    g_bot_y = -0.6
    ax2.plot([obj_x, glasses_x], [obj_y, g_top_y], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([obj_x, glasses_x], [obj_y, g_bot_y], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([obj_x, glasses_x], [obj_y, 0], color=DEEP["orange"], lw=2, zorder=4)
    
    # Rays bent inwards from convex lens towards eye lens
    el_top_y = 0.42
    el_bot_y = -0.42
    ax2.plot([glasses_x, lx2], [g_top_y, el_top_y], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([glasses_x, lx2], [g_bot_y, el_bot_y], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([glasses_x, lx2], [0, 0], color=DEEP["orange"], lw=2, zorder=4)
    
    # Rays from eye lens converging exactly on retina
    ax2.plot([lx2, retina_x], [el_top_y, 0], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([lx2, retina_x], [el_bot_y, 0], color=DEEP["orange"], lw=2, zorder=4)
    ax2.plot([lx2, retina_x], [0, 0], color=DEEP["orange"], lw=2, zorder=4)
    
    ax2.plot(retina_x, 0, marker='o', color=DEEP["green"], markersize=6, zorder=5)
    
    # Labels Bottom Panel
    ax2.annotate("convex lens", xy=(glasses_x, 0.85), xytext=(glasses_x, 1.4),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
                 
    ax2.annotate("short eyeball", xy=(cx, 1.8), xytext=(cx, 2.05),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))
                 
    ax2.annotate("focus on retina", xy=(retina_x, 0), xytext=(10.4, 0.5),
                 fontsize=12, color=INK, ha='center',
                 bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    save(fig, out)
