from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Column centers shifted slightly right to give ample left margin
    col_x = [2.5, 5.1, 7.7, 10.3]
    titles = ["Group A", "Group B", "Group AB", "Group O"]
    
    # Title row
    for x, title in zip(col_x, titles):
        ax.text(x, 7.05, title, ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # Row headers / side labels placed safely in the left margin (x=0.15 to x=1.1)
    ax.text(0.15, 4.9, "Red blood cell\n& surface\nantigens", ha="left", va="center", 
            fontsize=11.5, color=INK, weight="bold", linespacing=1.2)
    ax.text(0.15, 1.8, "Plasma &\nantibodies", ha="left", va="center", 
            fontsize=11.5, color=INK, weight="bold", linespacing=1.2)

    # RBC parameters
    rbc_y = 4.9
    r_outer = 1.02
    for x in col_x:
        # Outer membrane / rim
        c_outer = patches.Circle((x, rbc_y), r_outer, fc="#E85D5D", ec=DEEP["pink"], lw=2.5, zorder=2)
        ax.add_patch(c_outer)
        # Inner biconcave depression
        c_inner = patches.Circle((x, rbc_y), 0.50, fc="#F6A8A8", ec="#E85D5D", lw=1.5, zorder=3)
        ax.add_patch(c_inner)

    # Helper: draw Antigen A (Blue Triangle)
    def draw_antigen_a(cx, cy, angle_rad):
        tip_r = 0.25
        base_w = 0.16
        tip_x = cx + tip_r * np.cos(angle_rad)
        tip_y = cy + tip_r * np.sin(angle_rad)
        perp_rad = angle_rad + np.pi / 2
        b1_x = cx + (base_w / 2) * np.cos(perp_rad)
        b1_y = cy + (base_w / 2) * np.sin(perp_rad)
        b2_x = cx - (base_w / 2) * np.cos(perp_rad)
        b2_y = cy - (base_w / 2) * np.sin(perp_rad)
        poly = patches.Polygon([[b1_x, b1_y], [tip_x, tip_y], [b2_x, b2_y]], closed=True,
                               fc=BLUE, ec=DEEP["blue"], lw=1.5, zorder=4)
        ax.add_patch(poly)

    # Helper: draw Antigen B (Green Square)
    def draw_antigen_b(cx, cy, angle_rad):
        side = 0.20
        sq_cx = cx + (side / 2) * np.cos(angle_rad)
        sq_cy = cy + (side / 2) * np.sin(angle_rad)
        perp = angle_rad + np.pi / 2
        p1 = [sq_cx - side/2*np.cos(angle_rad) - side/2*np.cos(perp), sq_cy - side/2*np.sin(angle_rad) - side/2*np.sin(perp)]
        p2 = [sq_cx + side/2*np.cos(angle_rad) - side/2*np.cos(perp), sq_cy + side/2*np.sin(angle_rad) - side/2*np.sin(perp)]
        p3 = [sq_cx + side/2*np.cos(angle_rad) + side/2*np.cos(perp), sq_cy + side/2*np.sin(angle_rad) + side/2*np.sin(perp)]
        p4 = [sq_cx - side/2*np.cos(angle_rad) + side/2*np.cos(perp), sq_cy - side/2*np.sin(angle_rad) + side/2*np.sin(perp)]
        poly = patches.Polygon([p1, p2, p3, p4], closed=True, fc=GREEN, ec=DEEP["green"], lw=1.5, zorder=4)
        ax.add_patch(poly)

    # Antigens on cells
    angles_12 = np.linspace(0, 2*np.pi, 12, endpoint=False) + 0.15
    # Group A: 12 triangles
    for a in angles_12:
        cx = col_x[0] + r_outer * np.cos(a)
        cy = rbc_y + r_outer * np.sin(a)
        draw_antigen_a(cx, cy, a)

    # Group B: 12 squares
    for a in angles_12:
        cx = col_x[1] + r_outer * np.cos(a)
        cy = rbc_y + r_outer * np.sin(a)
        draw_antigen_b(cx, cy, a)

    # Group AB: alternating triangles and squares
    for i, a in enumerate(angles_12):
        cx = col_x[2] + r_outer * np.cos(a)
        cy = rbc_y + r_outer * np.sin(a)
        if i % 2 == 0:
            draw_antigen_a(cx, cy, a)
        else:
            draw_antigen_b(cx, cy, a)

    # Group O: "no antigens"
    ax.text(col_x[3], rbc_y, "no antigens", ha="center", va="center", fontsize=12.5, color=INK, style="italic", zorder=5)

    # Plasma boxes
    box_w = 2.15
    box_h = 2.3
    plasma_y = 0.65
    for x in col_x:
        rect = patches.FancyBboxPatch((x - box_w/2, plasma_y), box_w, box_h,
                                      boxstyle="round,pad=0.06,rounding_size=0.15",
                                      fc="#FFFBEA", ec="#D4C89A", lw=1.5, zorder=1)
        ax.add_patch(rect)

    # Helper: draw Y-shaped Antibody with proper scale to avoid collision
    def draw_antibody(cx, cy, ab_type, rot_deg=0, scale=0.85):
        rad = np.radians(rot_deg)
        cos_r, sin_r = np.cos(rad), np.sin(rad)
        def rot(px, py):
            return [cx + (px * cos_r - py * sin_r) * scale, cy + (px * sin_r + py * cos_r) * scale]

        ec_col = DEEP["blue"] if ab_type == 'anti-A' else DEEP["green"]

        # Stem & Arms
        p_base = rot(0, -0.32)
        p_center = rot(0, 0.0)
        p_arm_l = rot(-0.25, 0.28)
        p_arm_r = rot(0.25, 0.28)

        ax.plot([p_base[0], p_center[0]], [p_base[1], p_center[1]], color=ec_col, lw=3.0, solid_capstyle='round', zorder=3)
        ax.plot([p_center[0], p_arm_l[0]], [p_center[1], p_arm_l[1]], color=ec_col, lw=3.0, solid_capstyle='round', zorder=3)
        ax.plot([p_center[0], p_arm_r[0]], [p_center[1], p_arm_r[1]], color=ec_col, lw=3.0, solid_capstyle='round', zorder=3)

        # Binding tips at the ends of arms
        for arm_x, arm_y, tip_ang in [(-0.25, 0.28, rot_deg + 40), (0.25, 0.28, rot_deg - 40)]:
            t_rad = np.radians(tip_ang)
            t_cos, t_sin = np.cos(t_rad), np.sin(t_rad)
            def t_rot(bx, by):
                return rot(arm_x + bx * t_cos - by * t_sin, arm_y + bx * t_sin + by * t_cos)

            if ab_type == 'anti-A':
                # Triangle notch / V-cleft
                pts = [t_rot(-0.09, 0.1), t_rot(0, 0), t_rot(0.09, 0.1)]
                ax.plot([p[0] for p in pts], [p[1] for p in pts], color=ec_col, lw=2.2, zorder=4)
            else:
                # Square notch / U-cup
                pts = [t_rot(-0.08, 0.09), t_rot(-0.08, 0), t_rot(0.08, 0), t_rot(0.08, 0.09)]
                ax.plot([p[0] for p in pts], [p[1] for p in pts], color=ec_col, lw=2.2, zorder=4)

    # Plasma contents
    # Group A: anti-B only (spaced sufficiently apart, no overlap)
    draw_antibody(col_x[0] - 0.52, 1.85, 'anti-B', 10)
    draw_antibody(col_x[0] + 0.52, 1.85, 'anti-B', -10)
    ax.text(col_x[0], 0.95, "anti-B", ha="center", va="center", fontsize=12, color=INK, weight="bold")

    # Group B: anti-A only (spaced sufficiently apart, no overlap)
    draw_antibody(col_x[1] - 0.52, 1.85, 'anti-A', 10)
    draw_antibody(col_x[1] + 0.52, 1.85, 'anti-A', -10)
    ax.text(col_x[1], 0.95, "anti-A", ha="center", va="center", fontsize=12, color=INK, weight="bold")

    # Group AB: none
    ax.text(col_x[2], 1.80, "no antibodies", ha="center", va="center", fontsize=12.5, color=INK, style="italic")

    # Group O: both anti-A and anti-B (spaced apart, no overlap)
    draw_antibody(col_x[3] - 0.54, 1.85, 'anti-A', 10)
    draw_antibody(col_x[3] + 0.54, 1.85, 'anti-B', -10)
    ax.text(col_x[3] - 0.54, 0.95, "anti-A", ha="center", va="center", fontsize=11.5, color=INK, weight="bold")
    ax.text(col_x[3] + 0.54, 0.95, "anti-B", ha="center", va="center", fontsize=11.5, color=INK, weight="bold")

    # Annotations and Labels
    # Label: "red blood cell" pointing to Group A RBC
    ax.annotate("red blood cell", xy=(col_x[0] - 0.72, 5.6), xytext=(col_x[0] - 1.5, 6.45),
                fontsize=11.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Label: "antigen A" pointing to an antigen on Group A cell
    ang_a_pt = angles_12[2]
    ax.annotate("antigen A", xy=(col_x[0] + (r_outer+0.22)*np.cos(ang_a_pt), rbc_y + (r_outer+0.22)*np.sin(ang_a_pt)),
                xytext=(col_x[0] + 0.65, 6.45), fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Label: "antigen B" pointing to an antigen on Group B cell
    ang_b_pt = angles_12[1]
    ax.annotate("antigen B", xy=(col_x[1] + (r_outer+0.22)*np.cos(ang_b_pt), rbc_y + (r_outer+0.22)*np.sin(ang_b_pt)),
                xytext=(col_x[1] + 0.65, 6.45), fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Label: "plasma" pointing to Group A plasma box
    ax.annotate("plasma", xy=(col_x[0] - 0.98, 2.4), xytext=(col_x[0] - 1.55, 2.65),
                fontsize=11.5, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    save(fig, out)
