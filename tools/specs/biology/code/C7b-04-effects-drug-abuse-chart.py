from style import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as mpath

def draw(out):
    fig = canvas(12, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(-6.8, 6.8)
    ax.set_ylim(-6.8, 6.8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0, 6.1, "The Effects of Substance Abuse", ha='center', va='center',
            fontsize=18, fontweight='bold', color=INK)

    # 9 items specified in prompt
    effects = [
        {"label": "Mental illness", "type": "brain", "color": LAV, "line_col": DEEP["lav"]},
        {"label": "Lung disease", "type": "lungs", "color": BLUE, "line_col": DEEP["blue"]},
        {"label": "Heart attack", "type": "heart", "color": PINK, "line_col": DEEP["pink"]},
        {"label": "Liver damage", "type": "liver", "color": ORANGE, "line_col": DEEP["orange"]},
        {"label": "HIV and hepatitis", "type": "syringe", "color": GREEN, "line_col": DEEP["green"]},
        {"label": "Road accidents", "type": "car", "color": PINK, "line_col": DEEP["pink"]},
        {"label": "Family breakdown", "type": "house", "color": ORANGE, "line_col": DEEP["orange"]},
        {"label": "School dropout", "type": "school", "color": BLUE, "line_col": DEEP["blue"]},
        {"label": "Crime", "type": "crime", "color": LAV, "line_col": DEEP["lav"]}
    ]

    N = len(effects)
    R_outer = 4.1
    node_r = 0.85

    # Center Circle
    center_r = 1.35
    c_bg = patches.Circle((0, 0), center_r, facecolor=CREAM, edgecolor=GREY, lw=2, zorder=2)
    ax.add_patch(c_bg)

    # Central Icons: Young person silhouette & pill / medicine bottle
    p_head = patches.Circle((-0.3, 0.45), 0.22, facecolor=INK, edgecolor='none', zorder=3)
    ax.add_patch(p_head)
    torso_path = mpath.Path([
        (-0.6, -0.2), (-0.6, 0.15), (-0.45, 0.25), (-0.15, 0.25), (0.0, 0.15), (0.0, -0.2)
    ], [mpath.Path.MOVETO, mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.LINETO, mpath.Path.CURVE3, mpath.Path.CURVE3])
    torso = patches.PathPatch(torso_path, facecolor=INK, edgecolor='none', zorder=3)
    ax.add_patch(torso)

    # Medicine bottle
    b_body = patches.Rectangle((0.2, -0.35), 0.45, 0.6, facecolor=BLUE, edgecolor=INK, lw=1.5, zorder=3)
    b_neck = patches.Rectangle((0.28, 0.25), 0.29, 0.1, facecolor=BLUE, edgecolor=INK, lw=1.5, zorder=3)
    b_cap = patches.Rectangle((0.24, 0.35), 0.37, 0.1, facecolor=GREY, edgecolor=INK, lw=1.5, zorder=3)
    ax.add_patch(b_body)
    ax.add_patch(b_neck)
    ax.add_patch(b_cap)
    ax.plot([0.425, 0.425], [-0.15, 0.05], color=INK, lw=2, zorder=4)
    ax.plot([0.325, 0.525], [-0.05, -0.05], color=INK, lw=2, zorder=4)

    # Pill / capsule
    pill_patch1 = patches.Wedge((-0.15, -0.55), 0.14, 45, 225, facecolor=PINK, edgecolor=INK, lw=1.5, zorder=4)
    pill_patch2 = patches.Wedge((-0.05, -0.45), 0.14, 225, 45, facecolor=LAV, edgecolor=INK, lw=1.5, zorder=4)
    ax.add_patch(pill_patch1)
    ax.add_patch(pill_patch2)

    ax.text(0, -0.95, "Substance\nAbuse", ha='center', va='center', fontsize=11, fontweight='bold', color=INK, zorder=4)

    # Helper functions for icons
    def draw_brain(cx, cy):
        # Recognizable brain: cerebral hemispheres with gyri curves + jagged crack
        # Left hemisphere
        l_path = mpath.Path([
            (cx - 0.04, cy + 0.32),
            (cx - 0.25, cy + 0.35), (cx - 0.42, cy + 0.18), (cx - 0.40, cy),
            (cx - 0.42, cy - 0.15), (cx - 0.32, cy - 0.30), (cx - 0.15, cy - 0.28),
            (cx - 0.08, cy - 0.22), (cx - 0.04, cy - 0.15), (cx - 0.04, cy - 0.15)
        ], [mpath.Path.MOVETO,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.LINETO])
        # Right hemisphere
        r_path = mpath.Path([
            (cx + 0.04, cy + 0.32),
            (cx + 0.25, cy + 0.35), (cx + 0.42, cy + 0.18), (cx + 0.40, cy),
            (cx + 0.42, cy - 0.15), (cx + 0.32, cy - 0.30), (cx + 0.15, cy - 0.28),
            (cx + 0.08, cy - 0.22), (cx + 0.04, cy - 0.15), (cx + 0.04, cy - 0.15)
        ], [mpath.Path.MOVETO,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.LINETO])
        ax.add_patch(patches.PathPatch(l_path, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4))
        ax.add_patch(patches.PathPatch(r_path, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4))
        # Internal sulci curves
        ax.plot([cx - 0.32, cx - 0.2, cx - 0.22], [cy + 0.12, cy + 0.15, cy + 0.02], color=INK, lw=1.4, zorder=5)
        ax.plot([cx - 0.28, cx - 0.15, cx - 0.1], [cy - 0.12, cy - 0.08, cy - 0.18], color=INK, lw=1.4, zorder=5)
        ax.plot([cx + 0.32, cx + 0.2, cx + 0.22], [cy + 0.12, cy + 0.15, cy + 0.02], color=INK, lw=1.4, zorder=5)
        ax.plot([cx + 0.28, cx + 0.15, cx + 0.1], [cy - 0.12, cy - 0.08, cy - 0.18], color=INK, lw=1.4, zorder=5)
        # Prominent crack dividing the brain
        crack_x = [cx, cx - 0.08, cx + 0.07, cx - 0.05, cx + 0.06, cx - 0.02, cx]
        crack_y = [cy + 0.35, cy + 0.23, cy + 0.11, cy - 0.02, cy - 0.14, cy - 0.24, cy - 0.32]
        ax.plot(crack_x, crack_y, color=DEEP["pink"], lw=2.6, zorder=6)

    def draw_lungs(cx, cy):
        # Trachea and main bronchi
        ax.plot([cx, cx], [cy + 0.32, cy + 0.12], color=INK, lw=2.4, zorder=4)
        ax.plot([cx, cx - 0.14], [cy + 0.12, cy + 0.02], color=INK, lw=2.0, zorder=4)
        ax.plot([cx, cx + 0.14], [cy + 0.12, cy + 0.02], color=INK, lw=2.0, zorder=4)
        # Recognizable anatomical lung lobes
        left_lung = patches.PathPatch(mpath.Path([
            (cx - 0.05, cy + 0.15),
            (cx - 0.25, cy + 0.25), (cx - 0.38, cy + 0.05), (cx - 0.38, cy - 0.18),
            (cx - 0.32, cy - 0.30), (cx - 0.18, cy - 0.28), (cx - 0.06, cy - 0.12),
            (cx - 0.05, cy + 0.15)
        ], [mpath.Path.MOVETO,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.LINETO]), facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4)
        right_lung = patches.PathPatch(mpath.Path([
            (cx + 0.05, cy + 0.15),
            (cx + 0.25, cy + 0.25), (cx + 0.38, cy + 0.05), (cx + 0.38, cy - 0.18),
            (cx + 0.32, cy - 0.30), (cx + 0.18, cy - 0.28), (cx + 0.06, cy - 0.12),
            (cx + 0.05, cy + 0.15)
        ], [mpath.Path.MOVETO,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.LINETO]), facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4)
        ax.add_patch(left_lung)
        ax.add_patch(right_lung)
        # Prominent dark disease patches
        dark_patches = [
            (cx - 0.22, cy + 0.04, 0.075),
            (cx - 0.16, cy - 0.14, 0.065),
            (cx - 0.28, cy - 0.12, 0.055),
            (cx + 0.22, cy + 0.02, 0.08),
            (cx + 0.18, cy - 0.15, 0.06),
            (cx + 0.27, cy - 0.10, 0.05)
        ]
        for px, py, pr in dark_patches:
            ax.add_patch(patches.Circle((px, py), pr, facecolor=INK, edgecolor='none', alpha=0.88, zorder=5))

    def draw_heart(cx, cy):
        t = np.linspace(0, 2*np.pi, 100)
        hx = 0.022 * (16 * np.sin(t)**3)
        hy = 0.022 * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
        ax.fill(cx + hx, cy + hy + 0.05, color=PINK, zorder=4)
        ax.plot(cx + hx, cy + hy + 0.05, color=INK, lw=1.8, zorder=4)
        ecg_x = [cx-0.34, cx-0.18, cx-0.10, cx-0.03, cx+0.06, cx+0.14, cx+0.34]
        ecg_y = [cy+0.04, cy+0.04, cy+0.25, cy-0.20, cy+0.20, cy+0.04, cy+0.04]
        ax.plot(ecg_x, ecg_y, color=DEEP["pink"], lw=2.6, zorder=5)

    def draw_liver(cx, cy):
        # Anatomically recognizable liver: large right lobe, tapered left lobe, smooth superior dome, gallbladder
        liver_outline = mpath.Path([
            (cx - 0.38, cy - 0.04),
            (cx - 0.32, cy + 0.14), (cx - 0.10, cy + 0.22), (cx + 0.12, cy + 0.24),
            (cx + 0.35, cy + 0.20), (cx + 0.40, cy + 0.08), (cx + 0.38, cy - 0.10),
            (cx + 0.30, cy - 0.24), (cx + 0.08, cy - 0.22), (cx - 0.06, cy - 0.16),
            (cx - 0.24, cy - 0.12), (cx - 0.38, cy - 0.04)
        ], [mpath.Path.MOVETO,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.CURVE3, mpath.Path.CURVE3,
            mpath.Path.CURVE3, mpath.Path.LINETO])
        ax.add_patch(patches.PathPatch(liver_outline, facecolor=CREAM, edgecolor=INK, lw=2.0, zorder=4))
        # Gallbladder notch/sac underneath
        gb = patches.Ellipse((cx + 0.05, cy - 0.22), 0.11, 0.16, angle=15, facecolor=GREEN, edgecolor=INK, lw=1.5, zorder=3)
        ax.add_patch(gb)
        # Falciform ligament dividing line
        ax.plot([cx + 0.05, cx + 0.02], [cy + 0.23, cy - 0.05], color=INK, lw=1.5, ls='--', zorder=5)
        # Cirrhosis/damage scars and spots
        ax.plot([cx + 0.12, cx + 0.25], [cy + 0.10, cy - 0.02], color=DEEP["orange"], lw=2.2, zorder=5)
        ax.plot([cx + 0.25, cx + 0.18], [cy - 0.02, cy - 0.12], color=DEEP["orange"], lw=2.2, zorder=5)
        ax.plot([cx - 0.16, cx - 0.04], [cy + 0.04, cy - 0.04], color=DEEP["orange"], lw=2.0, zorder=5)
        ax.add_patch(patches.Circle((cx + 0.24, cy + 0.08), 0.035, facecolor=DEEP["orange"], edgecolor='none', zorder=5))
        ax.add_patch(patches.Circle((cx - 0.12, cy - 0.02), 0.03, facecolor=DEEP["orange"], edgecolor='none', zorder=5))

    def draw_syringe(cx, cy):
        ax.plot([cx-0.2, cx+0.1], [cy-0.2, cy+0.1], color=INK, lw=6, solid_capstyle='butt', zorder=4)
        ax.plot([cx-0.2, cx+0.1], [cy-0.2, cy+0.1], color=GREEN, lw=3.5, solid_capstyle='butt', zorder=5)
        ax.plot([cx+0.1, cx+0.28], [cy+0.1, cy+0.28], color=INK, lw=1.8, zorder=4)
        ax.plot([cx-0.2, cx-0.3], [cy-0.2, cy-0.3], color=INK, lw=2.5, zorder=4)
        ax.plot([cx-0.35, cx-0.25], [cy-0.25, cy-0.35], color=INK, lw=2.5, zorder=4)
        vx, vy = cx - 0.15, cy + 0.18
        ax.add_patch(patches.Circle((vx, vy), 0.08, facecolor=LAV, edgecolor=INK, lw=1.5, zorder=6))
        for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
            ax.plot([vx + 0.08*np.cos(ang), vx + 0.14*np.cos(ang)],
                    [vy + 0.08*np.sin(ang), vy + 0.14*np.sin(ang)], color=INK, lw=1.5, zorder=6)

    def draw_car(cx, cy):
        ax.plot([cx-0.32, cx-0.28, cx-0.15, cx, cx+0.15, cx+0.28, cx+0.28, cx-0.32, cx-0.32],
                [cy-0.05, cy+0.1, cy+0.12, cy+0.22, cy+0.05, cy+0.05, cy-0.12, cy-0.12, cy-0.05],
                color=INK, lw=2, zorder=4)
        ax.add_patch(patches.Circle((cx-0.2, cy-0.14), 0.07, facecolor=GREY, edgecolor=INK, lw=1.8, zorder=5))
        ax.add_patch(patches.Circle((cx+0.16, cy-0.14), 0.07, facecolor=GREY, edgecolor=INK, lw=1.8, zorder=5))
        ax.plot([cx+0.28, cx+0.38], [cy+0.05, cy+0.12], color=DEEP["pink"], lw=2, zorder=5)
        ax.plot([cx+0.3, cx+0.42], [cy-0.02, cy-0.02], color=DEEP["pink"], lw=2, zorder=5)
        ax.plot([cx+0.28, cx+0.36], [cy-0.08, cy-0.16], color=DEEP["pink"], lw=2, zorder=5)

    def draw_house(cx, cy):
        left_wall = patches.Polygon([[cx-0.28, cy-0.2], [cx-0.28, cy+0.05], [cx-0.04, cy+0.26], [cx-0.02, cy+0.15], [cx-0.06, cy+0.02], [cx-0.02, cy-0.08], [cx-0.05, cy-0.2]], closed=True, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4)
        right_wall = patches.Polygon([[cx+0.28, cy-0.2], [cx+0.28, cy+0.05], [cx+0.06, cy+0.24], [cx+0.08, cy+0.15], [cx+0.04, cy+0.02], [cx+0.08, cy-0.08], [cx+0.05, cy-0.2]], closed=True, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4)
        ax.add_patch(left_wall)
        ax.add_patch(right_wall)

    def draw_school(cx, cy):
        base = patches.Rectangle((cx-0.28, cy-0.22), 0.42, 0.32, facecolor=BLUE, edgecolor=INK, lw=1.8, zorder=4)
        roof = patches.Polygon([[cx-0.32, cy+0.1], [cx-0.07, cy+0.28], [cx+0.18, cy+0.1]], closed=True, facecolor=CREAM, edgecolor=INK, lw=1.8, zorder=4)
        door = patches.Rectangle((cx-0.12, cy-0.22), 0.1, 0.18, facecolor=INK, edgecolor='none', zorder=5)
        ax.add_patch(base)
        ax.add_patch(roof)
        ax.add_patch(door)
        ax.annotate("", xy=(cx+0.36, cy-0.08), xytext=(cx+0.02, cy-0.08),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.5), zorder=6)

    def draw_crime(cx, cy):
        r1 = patches.Circle((cx-0.16, cy), 0.13, facecolor='none', edgecolor=INK, lw=2.5, zorder=4)
        r2 = patches.Circle((cx+0.16, cy), 0.13, facecolor='none', edgecolor=INK, lw=2.5, zorder=4)
        ax.add_patch(r1)
        ax.add_patch(r2)
        ax.plot([cx-0.16, cx-0.16], [cy-0.04, cy+0.04], color=INK, lw=2, zorder=5)
        ax.plot([cx+0.16, cx+0.16], [cy-0.04, cy+0.04], color=INK, lw=2, zorder=5)
        ax.plot([cx-0.03, cx+0.03], [cy, cy], color=INK, lw=3, zorder=5)

    icon_drawers = {
        "brain": draw_brain,
        "lungs": draw_lungs,
        "heart": draw_heart,
        "liver": draw_liver,
        "syringe": draw_syringe,
        "car": draw_car,
        "house": draw_house,
        "school": draw_school,
        "crime": draw_crime
    }

    angles = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, N, endpoint=False)

    for i, item in enumerate(effects):
        theta = angles[i]
        ox = R_outer * np.cos(theta)
        oy = R_outer * np.sin(theta)

        start_x = (center_r + 0.05) * np.cos(theta)
        start_y = (center_r + 0.05) * np.sin(theta)
        end_x = (R_outer - node_r - 0.08) * np.cos(theta)
        end_y = (R_outer - node_r - 0.08) * np.sin(theta)

        ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0, mutation_scale=16), zorder=1)

        node_bg = patches.Circle((ox, oy), node_r, facecolor=item["color"], edgecolor=item["line_col"], lw=2.2, zorder=3)
        ax.add_patch(node_bg)

        icon_drawers[item["type"]](ox, oy)

        label_r = R_outer + node_r + 0.42
        lx = label_r * np.cos(theta)
        ly = label_r * np.sin(theta)

        if abs(np.cos(theta)) < 0.2:
            ha = 'center'
        elif np.cos(theta) > 0:
            ha = 'left'
        else:
            ha = 'right'

        if abs(np.sin(theta)) < 0.2:
            va = 'center'
        elif np.sin(theta) > 0:
            va = 'bottom'
        else:
            va = 'top'

        ax.text(lx, ly, item["label"], ha=ha, va=va, fontsize=12.5, fontweight='bold', color=INK,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9), zorder=7)

    save(fig, out)
