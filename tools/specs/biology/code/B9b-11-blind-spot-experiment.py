from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 8.5)
    ax.axis('off')

    # Card dimensions and location (top section)
    card_x, card_y = 1.0, 5.2
    card_w, card_h = 8.0, 2.4

    # Draw card (pure white card with crisp grey border)
    card_rect = patches.FancyBboxPatch(
        (card_x, card_y), card_w, card_h,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor='white', edgecolor=GREY, linewidth=1.5
    )
    ax.add_patch(card_rect)

    # Cross on the left of the card
    cross_cx, cross_cy = 3.0, 6.4
    d = 0.35
    ax.plot([cross_cx - d, cross_cx + d], [cross_cy, cross_cy], color=INK, lw=4, solid_capstyle='round')
    ax.plot([cross_cx, cross_cx], [cross_cy - d, cross_cy + d], color=INK, lw=4, solid_capstyle='round')

    # Dot on the right of the card
    dot_cx, dot_cy = 7.0, 6.4
    dot_circle = patches.Circle((dot_cx, dot_cy), 0.32, facecolor=INK, edgecolor=INK)
    ax.add_patch(dot_circle)

    # Card label & element labels
    ax.text(1.3, 7.25, "card", fontsize=13, fontweight='bold', color=INK)
    ax.text(cross_cx, 7.15, "cross", fontsize=12, ha='center', color=INK,
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.9))
    ax.text(dot_cx, 7.15, "dot", fontsize=12, ha='center', color=INK,
            bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.9))

    # Top-view diagram of head and eyes
    head_cx, head_cy = 5.0, 1.2
    
    # Head outline (top view: ellipse + nose)
    head_ellipse = patches.Ellipse((head_cx, head_cy), 4.2, 2.6, facecolor='white', edgecolor=GREY, lw=1.5)
    ax.add_patch(head_ellipse)

    # Nose pointing up
    nose_x = [4.85, 5.0, 5.15]
    nose_y = [2.4, 2.7, 2.4]
    ax.plot(nose_x, nose_y, color=GREY, lw=1.5)

    # Left eye: Closed (simple curved arc or slit)
    left_x, left_y = 4.0, 2.2
    arc_theta = np.linspace(np.pi * 0.1, np.pi * 0.9, 50)
    ax.plot(left_x + 0.35 * np.cos(arc_theta), left_y + 0.15 * np.sin(arc_theta), color=INK, lw=2.2)
    # Eyelashes
    ax.plot([left_x - 0.2, left_x - 0.28], [left_y + 0.08, left_y + 0.2], color=INK, lw=1.5)
    ax.plot([left_x, left_x], [left_y + 0.15, left_y + 0.3], color=INK, lw=1.5)
    ax.plot([left_x + 0.2, left_x + 0.28], [left_y + 0.08, left_y + 0.2], color=INK, lw=1.5)

    # Label for left eye closed
    ax.text(left_x - 0.6, 2.6, "left eye closed", fontsize=12, color=INK, ha='right',
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8))
    ax.annotate("", xy=(left_x, left_y + 0.15), xytext=(left_x - 0.5, 2.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Right eye: Detailed schematic circle / eyeball
    right_x, right_y = 6.0, 2.2
    r_eye = 0.65
    
    # Eyeball circle
    eye_circle = patches.Circle((right_x, right_y), r_eye, facecolor='white', edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(eye_circle)

    # Lens / cornea at top of right eye
    lens_arc = patches.Arc((right_x, right_y + r_eye * 0.75), 0.5, 0.3, angle=0, theta1=0, theta2=180,
                           color=DEEP["blue"], lw=2, zorder=3)
    ax.add_patch(lens_arc)
    pupil = patches.Ellipse((right_x, right_y + r_eye - 0.05), 0.3, 0.12, facecolor=DEEP["blue"], edgecolor=None, zorder=3)
    ax.add_patch(pupil)

    # Optic nerve exit: on the nasal side (medial / left side of right eyeball)
    optic_ang = np.radians(225)
    optic_x = right_x + r_eye * np.cos(optic_ang)
    optic_y = right_y + r_eye * np.sin(optic_ang)

    # Draw optic nerve canal heading backwards / medially
    nerve_w = 0.12
    p1_x, p1_y = optic_x + nerve_w * 0.7, optic_y - nerve_w * 0.7
    p2_x, p2_y = optic_x - nerve_w * 0.7, optic_y + nerve_w * 0.7
    nerve_poly = patches.Polygon([
        (p2_x, p2_y), (p2_x - 0.45, p2_y - 0.7),
        (p1_x - 0.45, p1_y - 0.7), (p1_x, p1_y)
    ], closed=True, facecolor='white', edgecolor=INK, lw=1.8, zorder=1)
    ax.add_patch(nerve_poly)

    # Fovea: located on the temporal side (lateral / right side of posterior retina)
    lens_center = np.array([right_x, right_y + r_eye * 0.85])
    dir_cross = lens_center - np.array([cross_cx, cross_cy])
    dir_cross = dir_cross / np.linalg.norm(dir_cross)
    fovea_pos = lens_center + dir_cross * (r_eye * 1.8)
    fovea_x, fovea_y = fovea_pos[0], fovea_pos[1]

    # Draw light rays
    # Ray 1: from cross to fovea
    ax.plot([cross_cx, lens_center[0]], [cross_cy, lens_center[1]], color=DEEP["blue"], lw=1.8, linestyle='--', zorder=4)
    ax.plot([lens_center[0], fovea_x], [lens_center[1], fovea_y], color=DEEP["blue"], lw=1.8, linestyle='--', zorder=4)
    fovea_dot = patches.Circle((fovea_x, fovea_y), 0.06, facecolor=DEEP["pink"], edgecolor=DEEP["pink"], zorder=5)
    ax.add_patch(fovea_dot)

    # Ray 2: from dot through lens to blind spot (optic nerve exit)
    ax.plot([dot_cx, lens_center[0]], [dot_cy, lens_center[1]], color=DEEP["orange"], lw=1.8, linestyle='--', zorder=4)
    ax.plot([lens_center[0], optic_x], [lens_center[1], optic_y], color=DEEP["orange"], lw=1.8, linestyle='--', zorder=4)
    blind_spot_dot = patches.Circle((optic_x, optic_y), 0.06, facecolor=DEEP["orange"], edgecolor=DEEP["orange"], zorder=5)
    ax.add_patch(blind_spot_dot)

    # Annotations and Labels
    # Fovea label
    ax.text(fovea_x + 0.8, fovea_y - 0.25, "fovea", fontsize=12, color=INK,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8), zorder=6)
    ax.annotate("", xy=(fovea_x, fovea_y), xytext=(fovea_x + 0.75, fovea_y - 0.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), zorder=6)

    # Blind spot label
    ax.text(optic_x - 1.6, optic_y + 0.35, "blind spot", fontsize=12, color=INK, ha='right',
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8), zorder=6)
    ax.annotate("", xy=(optic_x, optic_y), xytext=(optic_x - 1.55, optic_y + 0.35),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), zorder=6)

    # Optic nerve label
    ax.text(optic_x - 1.6, optic_y - 0.5, "optic nerve", fontsize=12, color=INK, ha='right',
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY, lw=0.8), zorder=6)
    ax.annotate("", xy=(optic_x - 0.25, optic_y - 0.4), xytext=(optic_x - 1.55, optic_y - 0.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2), zorder=6)

    save(fig, out)
