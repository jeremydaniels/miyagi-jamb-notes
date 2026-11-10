import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Background panels
    left_bg = patches.FancyBboxPatch((0.5, 0.5), 6.2, 7.8, boxstyle="round,pad=0.2",
                                    fc="#F2F9F3", ec=DEEP["green"], lw=2.5)
    right_bg = patches.FancyBboxPatch((7.3, 0.5), 6.2, 7.8, boxstyle="round,pad=0.2",
                                     fc="#FAF4F0", ec=DEEP["orange"], lw=2.5)
    ax.add_patch(left_bg)
    ax.add_patch(right_bg)

    # Dividing dashed line in the center
    ax.plot([7.0, 7.0], [0.8, 8.2], color=GREY, lw=2, linestyle="--")

    # Titles
    ax.text(3.6, 7.8, "Renewable Resources", color=DEEP["green"], fontsize=18,
            fontweight="bold", ha="center", va="center")
    ax.text(3.6, 7.35, "Naturally replenished over short periods", color=INK,
            fontsize=14, ha="center", va="center", style="italic")

    ax.text(10.4, 7.8, "Non-Renewable Resources", color=DEEP["orange"], fontsize=18,
            fontweight="bold", ha="center", va="center")
    ax.text(10.4, 7.35, "Finite supply; depleted faster than formed", color=INK,
            fontsize=14, ha="center", va="center", style="italic")

    # ================= LEFT SIDE ICONS (RENEWABLE) =================
    # 1. Sun (x=1.8, y=5.8)
    cx, cy = 1.8, 5.8
    sun_circ = patches.Circle((cx, cy), 0.35, fc=ORANGE, ec=DEEP["orange"], lw=1.8)
    ax.add_patch(sun_circ)
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        dx, dy = np.cos(angle), np.sin(angle)
        ax.plot([cx + 0.42*dx, cx + 0.58*dx], [cy + 0.42*dy, cy + 0.58*dy],
                color=DEEP["orange"], lw=2)
    ax.text(cx, cy - 0.75, "Solar", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 2. Wind Turbine (x=3.6, y=5.8)
    tx, ty = 3.6, 5.5
    ax.plot([tx, tx], [ty - 0.4, ty + 0.4], color=INK, lw=3)  # pole
    # Turbine blades
    for angle in [0, 2*np.pi/3, 4*np.pi/3]:
        bx = tx + 0.45 * np.sin(angle)
        by = (ty + 0.4) + 0.45 * np.cos(angle)
        ax.plot([tx, bx], [ty + 0.4, by], color=DEEP["blue"], lw=2.5)
    ax.scatter([tx], [ty + 0.4], color=INK, s=30, zorder=4)
    ax.text(tx, 5.05, "Wind", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 3. Flowing River (x=5.4, y=5.8)
    rx, ry = 5.4, 5.8
    # Waves
    w_x = np.linspace(rx - 0.5, rx + 0.5, 50)
    for dy_offset in [0.12, -0.08, -0.28]:
        w_y = ry + dy_offset + 0.05 * np.sin(w_x * 12)
        ax.plot(w_x, w_y, color=DEEP["blue"], lw=2.5)
    ax.text(rx, 5.05, "Water", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 4. Green Tree (x=2.5, y=3.7)
    trx, tr_y = 2.5, 3.6
    ax.plot([trx, trx], [tr_y - 0.4, tr_y + 0.1], color="#8B5A2B", lw=4) # trunk
    # Foliage circles
    fol1 = patches.Circle((trx, tr_y + 0.25), 0.35, fc=GREEN, ec=DEEP["green"], lw=2)
    fol2 = patches.Circle((trx - 0.2, tr_y + 0.1), 0.25, fc=GREEN, ec=DEEP["green"], lw=2)
    fol3 = patches.Circle((trx + 0.2, tr_y + 0.1), 0.25, fc=GREEN, ec=DEEP["green"], lw=2)
    ax.add_patch(fol2)
    ax.add_patch(fol3)
    ax.add_patch(fol1)
    ax.text(trx, tr_y - 0.6, "Biomass", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 5. Fish (x=4.7, y=3.7)
    fx, fy = 4.7, 3.7
    fish_body = patches.Ellipse((fx, fy), 0.6, 0.32, fc=BLUE, ec=DEEP["blue"], lw=2)
    ax.add_patch(fish_body)
    # Tail
    fish_tail = patches.Polygon([[fx + 0.28, fy], [fx + 0.48, fy + 0.2], [fx + 0.48, fy - 0.2]],
                                fc=BLUE, ec=DEEP["blue"], lw=2)
    ax.add_patch(fish_tail)
    ax.scatter([fx - 0.18], [fy + 0.05], color=INK, s=15, zorder=5) # eye
    ax.text(fx, fy - 0.6, "Wildlife", color=INK, fontsize=14, ha="center", fontweight="bold")

    # Loop arrow showing infinite replenishment
    loop_box = patches.FancyBboxPatch((1.0, 1.0), 5.2, 1.4, boxstyle="round,pad=0.2",
                                      fc="white", ec=DEEP["green"], lw=1.5)
    ax.add_patch(loop_box)
    # Draw circular looping arrow
    circ_center = (1.9, 1.7)
    arc = patches.Arc(circ_center, 1.0, 0.9, angle=0, theta1=40, theta2=330,
                      color=DEEP["green"], lw=3)
    ax.add_patch(arc)
    ax.annotate("", xy=(circ_center[0] + 0.48, circ_center[1] + 0.1),
                xytext=(circ_center[0] + 0.48, circ_center[1] - 0.1),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=3, mutation_scale=15))
    ax.text(2.6, 1.85, "Infinite Replenishment", color=DEEP["green"], fontsize=15, fontweight="bold")
    ax.text(2.6, 1.45, "Naturally regrows and regenerates", color=INK, fontsize=14)

    # ================= RIGHT SIDE ICONS (NON-RENEWABLE) =================
    # 1. Oil Rig (x=8.9, y=5.8)
    ox, oy = 8.9, 5.7
    rig_pts = [[ox - 0.35, oy - 0.4], [ox, oy + 0.45], [ox + 0.35, oy - 0.4]]
    ax.plot([ox - 0.35, ox, ox + 0.35], [oy - 0.4, oy + 0.45, oy - 0.4], color=INK, lw=2.5)
    ax.plot([ox - 0.2, ox + 0.2], [oy, oy], color=INK, lw=2)
    ax.plot([ox - 0.28, ox + 0.28], [oy - 0.2, oy - 0.2], color=INK, lw=2)
    # Pump arm / dark oil drops
    ax.plot([ox, ox + 0.4], [oy + 0.45, oy + 0.3], color=GREY, lw=2.5)
    ax.scatter([ox, ox - 0.05, ox + 0.05], [oy - 0.48, oy - 0.53, oy - 0.51],
               color=INK, s=28, zorder=5) # dark oil
    ax.text(ox, 4.95, "Petroleum", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 2. Lump of Coal (x=11.9, y=5.8)
    cx, cy = 11.9, 5.7
    coal_poly = patches.Polygon([[cx - 0.38, cy - 0.25], [cx - 0.42, cy + 0.05],
                                 [cx - 0.15, cy + 0.35], [cx + 0.25, cy + 0.3],
                                 [cx + 0.42, cy + 0.0], [cx + 0.3, cy - 0.3],
                                 [cx - 0.1, cy - 0.35]],
                                 fc="#3D3D3D", ec=INK, lw=2)
    ax.add_patch(coal_poly)
    ax.text(cx, 4.95, "Coal", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 3. Gold Bar (x=8.9, y=3.7)
    gx, gy = 8.9, 3.65
    bar1 = patches.Polygon([[gx - 0.4, gy - 0.2], [gx - 0.25, gy + 0.15],
                            [gx + 0.35, gy + 0.15], [gx + 0.2, gy - 0.2]],
                            fc="#FFD700", ec=DEEP["orange"], lw=2)
    bar2 = patches.Polygon([[gx - 0.25, gy + 0.15], [gx - 0.15, gy + 0.3],
                            [gx + 0.45, gy + 0.3], [gx + 0.35, gy + 0.15]],
                            fc="#FFE866", ec=DEEP["orange"], lw=2)
    ax.add_patch(bar1)
    ax.add_patch(bar2)
    ax.text(gx, 3.0, "Minerals / Gold", color=INK, fontsize=14, ha="center", fontweight="bold")

    # 4. Excavator digging a quarry (x=11.9, y=3.7)
    ex, ey = 11.9, 3.65
    # Tracks
    track = patches.FancyBboxPatch((ex - 0.35, ey - 0.25), 0.65, 0.18,
                                   boxstyle="round,pad=0.03", fc=GREY, ec=INK, lw=2)
    ax.add_patch(track)
    # Cab
    cab = patches.Rectangle((ex - 0.28, ey - 0.07), 0.35, 0.25, fc=ORANGE, ec=INK, lw=2)
    ax.add_patch(cab)
    # Boom arm & bucket
    ax.plot([ex + 0.05, ex + 0.35, ex + 0.55], [ey + 0.15, ey + 0.32, ey + 0.05],
            color=INK, lw=2.5)
    bucket = patches.Polygon([[ex + 0.55, ey + 0.05], [ex + 0.68, ey + 0.03],
                              [ex + 0.6, ey - 0.1]], fc=GREY, ec=INK, lw=2)
    ax.add_patch(bucket)
    # Quarry ground
    ax.plot([ex - 0.5, ex + 0.7], [ey - 0.28, ey - 0.28], color=INK, lw=2)
    ax.text(ex, 3.0, "Quarried Stone", color=INK, fontsize=14, ha="center", fontweight="bold")

    # Downward arrow to empty gauge
    gauge_box = patches.FancyBboxPatch((7.8, 1.0), 5.2, 1.4, boxstyle="round,pad=0.2",
                                       fc="white", ec=DEEP["orange"], lw=1.5)
    ax.add_patch(gauge_box)

    # Empty Gauge illustration
    gx_c, gy_c = 8.6, 1.55
    gauge_bg = patches.Wedge((gx_c, gy_c), 0.45, 0, 180, fc="#EEEEEE", ec=INK, lw=2)
    ax.add_patch(gauge_bg)
    # Empty zone mark (reddish/orange on the left)
    gauge_empty = patches.Wedge((gx_c, gy_c), 0.45, 140, 180, fc=PINK, ec=INK, lw=1)
    ax.add_patch(gauge_empty)
    # Gauge needle pointing to 'E' (left)
    ax.plot([gx_c, gx_c - 0.36], [gy_c, gy_c + 0.15], color=DEEP["pink"], lw=2.5)
    ax.scatter([gx_c], [gy_c], color=INK, s=20, zorder=5)
    ax.text(gx_c - 0.4, gy_c + 0.28, "E", color=DEEP["pink"], fontsize=12, fontweight="bold")
    ax.text(gx_c + 0.35, gy_c + 0.28, "F", color=GREY, fontsize=12, fontweight="bold")

    # Downward arrow next to gauge
    ax.annotate("", xy=(9.3, 1.3), xytext=(9.3, 1.9),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=3.5, mutation_scale=18))

    ax.text(9.5, 1.85, "Limited Supply (Depletion)", color=DEEP["orange"], fontsize=15, fontweight="bold", ha="left")
    ax.text(9.5, 1.45, "Permanent exhaustion\nwith consumption", color=INK, fontsize=14, ha="left")

    save(fig, out)
