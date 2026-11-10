from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 9.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9.0)
    ax.axis('off')

    # Overall diagram title
    ax.text(7.5, 8.6, "Capture–Recapture Method (Lincoln–Petersen Index)",
            ha="center", va="center", fontsize=16, weight="bold", color=INK)

    # Helper function to draw a Tilapia-like fish
    def draw_fish(x, y, scale=0.32, angle=0, marked=False, mark_color=DEEP["orange"]):
        rad = np.radians(angle)
        rot = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

        # Body outline (oval)
        t = np.linspace(0, 2 * np.pi, 30)
        bx = 0.8 * np.cos(t)
        by = 0.42 * np.sin(t)
        pts_body = np.vstack([bx, by])
        pts_body_rot = rot @ pts_body

        # Tail vertices
        tail = np.array([[-0.7, -1.2, -1.2, -0.7], [0, 0.35, -0.35, 0]])
        tail_rot = rot @ tail

        body_poly = patches.Polygon(np.column_stack([pts_body_rot[0] * scale + x, pts_body_rot[1] * scale + y]),
                                    closed=True, fc=CREAM if not marked else "#FFF0E0",
                                    ec=DEEP["blue"], lw=1.2, zorder=5)
        tail_poly = patches.Polygon(np.column_stack([tail_rot[0] * scale + x, tail_rot[1] * scale + y]),
                                    closed=True, fc=CREAM if not marked else "#FFF0E0",
                                    ec=DEEP["blue"], lw=1.2, zorder=5)
        ax.add_patch(body_poly)
        ax.add_patch(tail_poly)

        # Eye
        eye_pos = rot @ np.array([[0.45], [0.1]]) * scale + np.array([[x], [y]])
        ax.plot(eye_pos[0], eye_pos[1], 'o', color=INK, markersize=2.5, zorder=6)

        # Fin mark if marked (coloured dot on fin / back)
        if marked:
            fin_pos = rot @ np.array([[0.0], [0.35]]) * scale + np.array([[x], [y]])
            mark_circle = patches.Circle((fin_pos[0][0], fin_pos[1][0]), 0.13 * scale * 2.5,
                                         fc=mark_color, ec=DEEP["orange"], lw=1.2, zorder=7)
            ax.add_patch(mark_circle)

    # Step panel geometry
    # Pond panels: y from 3.3 to 7.5 (height 4.2), titles placed at y = 7.95 (above panel)
    step_centers = [2.6, 7.5, 12.4]
    box_w, box_h = 4.3, 4.2
    box_y = 3.3

    for cx in step_centers:
        pond = patches.FancyBboxPatch((cx - box_w / 2, box_y), box_w, box_h,
                                      boxstyle="Round,pad=0.15,rounding_size=0.35",
                                      fc=BLUE, ec=DEEP["blue"], lw=1.5, alpha=0.25, zorder=1)
        ax.add_patch(pond)
        # Gentle surface ripple
        w_x = np.linspace(cx - box_w / 2 + 0.1, cx + box_w / 2 - 0.1, 40)
        w_y = box_y + box_h - 0.25 + 0.04 * np.sin(np.linspace(0, 4 * np.pi, 40))
        ax.plot(w_x, w_y, color=DEEP["blue"], lw=1.2, alpha=0.5, zorder=2)

    # Transition arrows between steps (placed in gaps at x=4.95 and x=9.85)
    ax.annotate("", xy=(5.05, 5.4), xytext=(4.55, 5.4),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=GREY))
    ax.annotate("", xy=(9.95, 5.4), xytext=(9.45, 5.4),
                arrowprops=dict(arrowstyle="->", lw=2.5, color=GREY))

    # Helper function to draw an attached dip-net
    def draw_net(rim_center_x, rim_center_y, rim_rx=1.2, rim_ry=1.0):
        # Dip-net rim (ellipse)
        t_ang = np.linspace(0, 2 * np.pi, 60)
        rx = rim_center_x + rim_rx * np.cos(t_ang)
        ry = rim_center_y + rim_ry * np.sin(t_ang)
        ax.plot(rx, ry, color=DEEP["green"], lw=2.2, zorder=4)

        # Net mesh / pouch (lines criss-crossing inside rim)
        for offset in np.linspace(-0.6, 0.6, 4):
            mx = np.linspace(rim_center_x - 0.7, rim_center_x + 0.7, 20)
            my = rim_center_y + offset + 0.15 * np.cos((mx - rim_center_x) * 2)
            ax.plot(mx, my, color=GREEN, lw=0.9, ls="--", alpha=0.8, zorder=3)
        for offset in np.linspace(-0.8, 0.8, 5):
            my = np.linspace(rim_center_y - 0.7, rim_center_y + 0.7, 20)
            mx = rim_center_x + offset + 0.15 * np.sin((my - rim_center_y) * 2)
            ax.plot(mx, my, color=GREEN, lw=0.9, ls="--", alpha=0.8, zorder=3)

        # Net handle firmly attached to the upper-right edge of rim
        rim_attach_x = rim_center_x + rim_rx * np.cos(np.pi / 4)
        rim_attach_y = rim_center_y + rim_ry * np.sin(np.pi / 4)
        handle_end_x = rim_attach_x + 0.75
        handle_end_y = rim_attach_y + 0.95
        ax.plot([rim_attach_x, handle_end_x], [rim_attach_y, handle_end_y],
                color=DEEP["green"], lw=4.0, solid_capstyle="round", zorder=4)

    # ================= STEP 1 =================
    # Step title above panel border
    ax.text(2.6, 8.0, "1. capture and count (n1)", ha="center", va="center",
            fontsize=13, weight="bold", color=INK)

    # Net positioned comfortably in upper-middle of panel
    draw_net(2.5, 5.6, rim_rx=1.1, rim_ry=0.95)

    # Fish inside net (n1 = 5)
    fish_step1_net = [
        (2.1, 5.8, 15), (2.8, 5.9, -12),
        (2.4, 5.4, 8),
        (2.0, 5.0, -18), (2.8, 4.9, 10)
    ]
    for x, y, ang in fish_step1_net:
        draw_fish(x, y, scale=0.28, angle=ang, marked=False)

    # Free fish outside net in lower pond (well clear of counter)
    draw_fish(1.1, 4.2, scale=0.28, angle=-10, marked=False)
    draw_fish(3.9, 4.3, scale=0.28, angle=15, marked=False)
    draw_fish(1.3, 6.7, scale=0.28, angle=20, marked=False)

    # Counter box in clear lower area of panel (y=3.45 to 3.95)
    c_box1 = patches.FancyBboxPatch((1.35, 3.45), 2.5, 0.52,
                                    boxstyle="Round,pad=0.08,rounding_size=0.15",
                                    fc="white", ec=DEEP["blue"], lw=1.3, zorder=6)
    ax.add_patch(c_box1)
    ax.text(2.6, 3.71, "Sample 1: n1 = 5", ha="center", va="center",
            fontsize=11.5, weight="bold", color=INK, zorder=7)

    # ================= STEP 2 =================
    ax.text(7.5, 8.0, "2. mark and release", ha="center", va="center",
            fontsize=13, weight="bold", color=INK)

    # Marked fish released and swimming throughout pond
    marked_step2 = [
        (6.5, 6.6, 15), (8.4, 6.4, -20),
        (7.5, 5.5, 10),
        (6.4, 4.7, -15), (8.3, 4.5, 25)
    ]
    for x, y, ang in marked_step2:
        draw_fish(x, y, scale=0.28, angle=ang, marked=True)

    # Unmarked fish mixing in pond
    unmarked_step2 = [
        (5.9, 5.9, -10), (7.4, 6.8, 5), (8.7, 5.4, 30),
        (6.0, 3.9, 12), (7.4, 4.3, -30), (8.7, 3.8, -15)
    ]
    for x, y, ang in unmarked_step2:
        draw_fish(x, y, scale=0.28, angle=ang, marked=False)

    # Explanatory annotation box
    ax.text(7.5, 3.65, "marked fish mix with population", ha="center", va="center",
            fontsize=11.5, style="italic", color=INK, zorder=7,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.9))

    # ================= STEP 3 =================
    ax.text(12.4, 8.0, "3. recapture: count total (n2) and marked (m)",
            ha="center", va="center", fontsize=11.5, weight="bold", color=INK)

    # Second net
    draw_net(12.3, 5.6, rim_rx=1.1, rim_ry=0.95)

    # Recaptured sample (total n2 = 6, marked m = 2)
    # Marked ones clearly visible
    draw_fish(11.9, 5.9, scale=0.28, angle=15, marked=True)
    draw_fish(12.7, 5.1, scale=0.28, angle=-12, marked=True)
    # Unmarked ones in net
    draw_fish(12.6, 6.0, scale=0.28, angle=-10, marked=False)
    draw_fish(11.8, 5.2, scale=0.28, angle=25, marked=False)
    draw_fish(12.2, 4.7, scale=0.28, angle=5, marked=False)
    draw_fish(12.8, 4.5, scale=0.28, angle=-25, marked=False)

    # Other fish remaining in pond
    draw_fish(10.9, 6.7, scale=0.28, angle=10, marked=False)
    draw_fish(11.0, 4.3, scale=0.28, angle=-15, marked=True)
    draw_fish(13.8, 4.3, scale=0.28, angle=20, marked=False)

    # Counter box for step 3 in clear lower area (y=3.45 to 3.95)
    c_box2 = patches.FancyBboxPatch((10.75, 3.45), 3.3, 0.52,
                                    boxstyle="Round,pad=0.08,rounding_size=0.15",
                                    fc="white", ec=DEEP["blue"], lw=1.3, zorder=6)
    ax.add_patch(c_box2)
    ax.text(12.4, 3.71, "Sample 2: total n2 = 6, marked (m) = 2", ha="center", va="center",
            fontsize=10.5, weight="bold", color=INK, zorder=7)

    # ================= KEY / LEGEND =================
    draw_fish(4.3, 2.45, scale=0.28, angle=0, marked=True)
    ax.text(4.9, 2.45, "marked fish", va="center", fontsize=12, color=INK)

    draw_fish(9.3, 2.45, scale=0.28, angle=0, marked=False)
    ax.text(9.9, 2.45, "unmarked fish", va="center", fontsize=12, color=INK)

    # ================= FORMULA BOX =================
    f_box = patches.FancyBboxPatch((3.5, 0.45), 8.0, 1.4,
                                   boxstyle="Round,pad=0.18,rounding_size=0.3",
                                   fc=CREAM, ec=DEEP["orange"], lw=2.0, zorder=2)
    ax.add_patch(f_box)
    ax.text(7.5, 1.4, "Lincoln Index: Estimated Population Size (N)", ha="center", va="center",
            fontsize=12.5, color=INK, weight="bold")
    ax.text(7.5, 0.9, "N = (n1 × n2) ÷ m", ha="center", va="center",
            fontsize=16, weight="bold", color=DEEP["orange"])

    save(fig, out)
