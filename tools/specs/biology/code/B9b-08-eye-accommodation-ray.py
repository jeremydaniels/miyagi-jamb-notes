from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 11)
    
    # We will create two subplots: top for distant object, bottom for near object
    ax1 = fig.add_axes([0.05, 0.52, 0.9, 0.43])
    ax2 = fig.add_axes([0.05, 0.05, 0.9, 0.43])
    
    for ax in [ax1, ax2]:
        ax.set_xlim(-8, 9)
        ax.set_ylim(-4.2, 4.2)
        ax.set_aspect("equal")
        ax.axis("off")

    def draw_eye_base(ax):
        # Sclera / eye outline
        # Circular main body with corneal bulge at front (around x = 0 to 1.5)
        # Eye center roughly at (3.5, 0), radius ~ 3.2
        # Back retina arc: from top around x=1.5, y=2.8 to back x=6.7, y=0 to bottom x=1.5, y=-2.8
        theta = np.linspace(-np.pi * 0.72, np.pi * 0.72, 200)
        cx, cy, r = 3.5, 0.0, 3.2
        x_eye = cx + r * np.cos(theta)
        y_eye = cy + r * np.sin(theta)
        
        # Cornea bulge at the front
        theta_cornea = np.linspace(-np.pi * 0.42, np.pi * 0.42, 100)
        cx_c, cy_c, r_c = 0.4, 0.0, 2.5
        x_cornea = cx_c + r_c * np.cos(theta_cornea)
        y_cornea = cy_c + r_c * np.sin(theta_cornea)
        
        # Combine eye shell
        # Draw background fill for eyeball
        ax.fill(np.append(x_eye, x_cornea[::-1]), np.append(y_eye, y_cornea[::-1]), 
                color=CREAM, alpha=0.3, zorder=1)
        
        # Draw eye wall (sclera/outer)
        ax.plot(x_eye, y_eye, color=INK, lw=2.2, zorder=2)
        ax.plot(x_cornea, y_cornea, color=INK, lw=2.2, zorder=2)
        
        # Draw retina lining along the inner back wall
        r_retina = 3.05
        theta_ret = np.linspace(-np.pi * 0.65, np.pi * 0.65, 150)
        x_ret = cx + r_retina * np.cos(theta_ret)
        y_ret = cy + r_retina * np.sin(theta_ret)
        ax.plot(x_ret, y_ret, color=DEEP["pink"], lw=4.5, solid_capstyle='round', zorder=2)

    # ------------------ TOP PANEL: DISTANT OBJECT ------------------
    ax1.set_title("Distant object", fontsize=15, fontweight="bold", pad=12, color=INK, loc="left")
    draw_eye_base(ax1)
    
    # Lens parameters: thin and flat (rx = 0.28, ry = 1.6)
    lens_x = 2.0
    lens_rx = 0.28
    lens_ry = 1.65
    lens_top = patches.Ellipse((lens_x, 0), 2 * lens_rx, 2 * lens_ry, 
                               facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.0, zorder=4)
    ax1.add_patch(lens_top)
    
    # Ciliary muscles: relaxed (flatter against the wall, further out)
    # Suspensory ligaments: straight tight lines connecting muscle to lens
    # Upper ciliary body & muscle
    ciliary_top_rel = patches.Polygon([[1.5, 2.5], [2.7, 2.5], [2.6, 1.95], [1.6, 1.95]], 
                                      closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    ciliary_bot_rel = patches.Polygon([[1.5, -2.5], [2.7, -2.5], [2.6, -1.95], [1.6, -1.95]], 
                                      closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    ax1.add_patch(ciliary_top_rel)
    ax1.add_patch(ciliary_bot_rel)
    
    # Ligaments: tight, straight lines
    for offset in [-0.15, 0.0, 0.15]:
        ax1.plot([lens_x + offset, lens_x + offset], [1.55, 1.95], color=GREY, lw=2.0, zorder=3)
        ax1.plot([lens_x + offset, lens_x + offset], [-1.55, -1.95], color=GREY, lw=2.0, zorder=3)
        
    # Parallel light rays (distant object)
    ray_ys = [-1.1, 0.0, 1.1]
    focal_pt_x, focal_pt_y = 6.55, 0.0 # On retina
    for y in ray_ys:
        # Incoming parallel from left to cornea/lens
        ax1.plot([-7.5, lens_x], [y, y], color=DEEP["orange"], lw=2.2, zorder=5)
        # Refracted towards retina
        ax1.plot([lens_x, focal_pt_x], [y, focal_pt_y], color=DEEP["orange"], lw=2.2, zorder=5)
        # Arrow heads
        ax1.annotate('', xy=(-3.5, y), xytext=(-4.5, y),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2))
        ax1.annotate('', xy=(4.0, y * 0.55), xytext=(3.0, y * 0.78),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2))

    # Labels for top panel
    # Light rays
    ax1.text(-5.5, 1.6, "light rays", color=INK, fontsize=12.5, ha="center",
             bbox=dict(fc="white", ec="none", pad=1.5))
    # Ciliary muscle relaxed
    ax1.annotate("ciliary muscle relaxed", xy=(2.6, 2.25), xytext=(4.5, 3.2),
                 fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Suspensory ligaments tight
    ax1.annotate("suspensory ligaments tight", xy=(2.15, 1.75), xytext=(-2.0, 3.2),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Thin lens
    ax1.annotate("thin lens", xy=(2.0, -0.6), xytext=(-1.5, -1.8),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Retina
    ax1.annotate("retina", xy=(6.55, 0.4), xytext=(7.4, 1.5),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # ------------------ BOTTOM PANEL: NEAR OBJECT ------------------
    ax2.set_title("Near object", fontsize=15, fontweight="bold", pad=12, color=INK, loc="left")
    draw_eye_base(ax2)
    
    # Lens parameters: thick and rounded (rx = 0.55, ry = 1.45)
    lens_thick_rx = 0.58
    lens_thick_ry = 1.45
    lens_bot = patches.Ellipse((lens_x, 0), 2 * lens_thick_rx, 2 * lens_thick_ry, 
                               facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.0, zorder=4)
    ax2.add_patch(lens_bot)
    
    # Ciliary muscles: contracted and bulging inwards (thicker, closer to center)
    ciliary_top_con = patches.Polygon([[1.4, 2.5], [2.8, 2.5], [2.7, 1.6], [1.5, 1.6]], 
                                      closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    ciliary_bot_con = patches.Polygon([[1.4, -2.5], [2.8, -2.5], [2.7, -1.6], [1.5, -1.6]], 
                                      closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=2, zorder=3)
    ax2.add_patch(ciliary_top_con)
    ax2.add_patch(ciliary_bot_con)
    
    # Ligaments: slack, wavy lines
    for offset in [-0.15, 0.0, 0.15]:
        wy = np.linspace(1.35, 1.65, 30)
        wx = lens_x + offset + 0.05 * np.sin(4 * np.pi * (wy - 1.35) / 0.3)
        ax2.plot(wx, wy, color=GREY, lw=2.0, zorder=3)
        
        wy_b = np.linspace(-1.65, -1.35, 30)
        wx_b = lens_x + offset + 0.05 * np.sin(4 * np.pi * (wy_b + 1.65) / 0.3)
        ax2.plot(wx_b, wy_b, color=GREY, lw=2.0, zorder=3)
        
    # Near object source point
    obj_x, obj_y = -4.5, 0.0
    ax2.scatter([obj_x], [obj_y], color=DEEP["orange"], s=70, zorder=6)
    ax2.text(obj_x, -0.6, "near object", color=INK, fontsize=11, ha="center",
             bbox=dict(fc="white", ec="none", pad=1.5))
    
    # Diverging light rays from near object
    ray_targets_y = [-1.1, 0.0, 1.1]
    for ty in ray_targets_y:
        # Diverging ray from object to lens front
        ax2.plot([obj_x, lens_x], [obj_y, ty], color=DEEP["orange"], lw=2.2, zorder=5)
        # Refracted towards retina
        ax2.plot([lens_x, focal_pt_x], [ty, focal_pt_y], color=DEEP["orange"], lw=2.2, zorder=5)
        # Arrow heads
        ax2.annotate('', xy=(lens_x - 1.5, ty * (1 - 1.5 / (lens_x - obj_x))), 
                     xytext=(lens_x - 2.5, ty * (1 - 2.5 / (lens_x - obj_x))),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2))
        ax2.annotate('', xy=(4.0, ty * 0.55), xytext=(3.0, ty * 0.78),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.2))

    # Labels for bottom panel
    # Light rays
    ax2.text(-1.8, 1.3, "light rays", color=INK, fontsize=12.5, ha="center",
             bbox=dict(fc="white", ec="none", pad=1.5))
    # Ciliary muscle contracted
    ax2.annotate("ciliary muscle contracted", xy=(2.7, 2.0), xytext=(4.5, 3.2),
                 fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Suspensory ligaments slack
    ax2.annotate("suspensory ligaments slack", xy=(2.15, 1.5), xytext=(-2.0, 3.2),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Thick lens
    ax2.annotate("thick lens", xy=(2.0, -0.6), xytext=(-1.5, -1.8),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    # Retina
    ax2.annotate("retina", xy=(6.55, 0.4), xytext=(7.4, 1.5),
                 fontsize=12, color=INK, ha="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    save(fig, out)
