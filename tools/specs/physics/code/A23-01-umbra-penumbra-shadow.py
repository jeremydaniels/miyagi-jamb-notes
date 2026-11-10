from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 7.5)

    # Two side-by-side subplots: Left = Point Source, Right = Extended Source
    ax1 = fig.add_axes([0.03, 0.08, 0.45, 0.82])
    ax2 = fig.add_axes([0.52, 0.08, 0.45, 0.82])

    for ax in (ax1, ax2):
        ax.set_xlim(-0.5, 11.2)
        ax.set_ylim(-4.0, 4.0)
        ax.set_aspect("equal")
        ax.axis("off")

    # ================= LEFT DIAGRAM: POINT SOURCE =================
    ax1.set_title("Point Source: Umbra Only", fontsize=16, color=INK, pad=15, weight='bold')

    x_src1 = 0.5
    y_src1 = 0.0

    x_sph1 = 4.0
    y_sph1 = 0.0
    r_sph1 = 0.85

    x_scr1 = 7.5  # Screen plane x position

    # Geometry for point source tangents
    d1 = x_sph1 - x_src1
    sin1 = r_sph1 / d1
    cos1 = np.sqrt(1 - sin1**2)
    tan1 = sin1 / cos1

    # Tangent contact points on sphere
    xt1_top = x_sph1 - r_sph1 * sin1
    yt1_top = y_sph1 + r_sph1 * cos1
    xt1_bot = x_sph1 - r_sph1 * sin1
    yt1_bot = y_sph1 - r_sph1 * cos1

    # Screen intersection of rays
    y_scr1_top = (x_scr1 - x_src1) * tan1
    y_scr1_bot = -y_scr1_top

    # Light cone from source (illuminated region)
    ax1.fill([x_src1, x_scr1, x_scr1], [y_src1, 3.2, -3.2],
             color=CREAM, alpha=0.45, zorder=1)

    # Shadow cone behind sphere (fully blocked, Umbra cone)
    ax1.fill([xt1_top, x_scr1, x_scr1, xt1_bot],
             [yt1_top, y_scr1_top, y_scr1_bot, yt1_bot],
             color=GREY, alpha=0.35, zorder=2)

    # Boundary rays
    ax1.plot([x_src1, x_scr1], [y_src1, y_scr1_top], color=DEEP["orange"], lw=2.2, zorder=3)
    ax1.plot([x_src1, x_scr1], [y_src1, y_scr1_bot], color=DEEP["orange"], lw=2.2, zorder=3)

    # Point source
    ax1.plot(x_src1, y_src1, marker='o', markersize=10, color=DEEP["orange"],
             markeredgecolor=INK, markeredgewidth=1.2, zorder=8)
    # Radiating small glow rays
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax1.plot([x_src1 + 0.18*np.cos(angle), x_src1 + 0.35*np.cos(angle)],
                 [y_src1 + 0.18*np.sin(angle), y_src1 + 0.35*np.sin(angle)],
                 color=DEEP["orange"], lw=1.5, zorder=7)

    # Solid sphere
    sph1 = patches.Circle((x_sph1, y_sph1), r_sph1, facecolor=INK, edgecolor=INK, zorder=6)
    ax1.add_patch(sph1)

    # Oblique Screen showing circular shadow
    # Screen corners in oblique perspective:
    scr_w = 2.0
    scr_h = 7.0
    scr_skew = 1.0
    scr_pts1 = np.array([
        [x_scr1, -scr_h/2],
        [x_scr1 + scr_w, -scr_h/2 + scr_skew],
        [x_scr1 + scr_w, scr_h/2 + scr_skew],
        [x_scr1, scr_h/2]
    ])
    screen_patch1 = patches.Polygon(scr_pts1, facecolor="white", edgecolor=INK, lw=2, zorder=4)
    ax1.add_patch(screen_patch1)

    # Center of screen in perspective:
    cx_scr1 = x_scr1 + scr_w / 2
    cy_scr1 = scr_skew / 2
    r_umb1_y = y_scr1_top
    r_umb1_x = r_umb1_y * 0.45  # squashed ellipse for circle viewed at angle
    ellipse_angle = np.degrees(np.arctan2(scr_skew, scr_w))

    # Single sharp black circular shadow on screen
    umbra_ellipse1 = patches.Ellipse((cx_scr1, cy_scr1), 2*r_umb1_x, 2*r_umb1_y,
                                     angle=ellipse_angle, facecolor=INK, edgecolor=INK, zorder=5)
    ax1.add_patch(umbra_ellipse1)

    # Labels Ax1
    ax1.text(x_src1, -1.2, "Point\nsource", fontsize=15, ha="center", va="top", color=INK,
             bbox=dict(fc="white", ec="none", pad=2))
    ax1.text(x_sph1, -1.4, "Solid black\nsphere", fontsize=15, ha="center", va="top", color=INK,
             bbox=dict(fc="white", ec="none", pad=2))
    ax1.text(x_scr1 + scr_w/2, scr_h/2 + scr_skew + 0.3, "Screen", fontsize=15, ha="center", va="bottom",
             color=INK, weight="bold")

    # Annotation to Umbra
    ax1.annotate("Umbra\n(sharp shadow)",
                 xy=(cx_scr1, cy_scr1),
                 xytext=(cx_scr1 + 1.4, -2.4),
                 fontsize=14, color=INK, fontweight='bold', ha="left", va="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", zorder=10))


    # ================= RIGHT DIAGRAM: EXTENDED SOURCE =================
    ax2.set_title("Extended Source: Umbra and Penumbra", fontsize=16, color=INK, pad=15, weight='bold')

    x_src2 = 0.6
    r_bulb = 0.9  # semi-height of extended source
    y_bulb_top = r_bulb
    y_bulb_bot = -r_bulb

    x_sph2 = 4.2
    y_sph2 = 0.0
    r_sph2 = 0.8

    x_scr2 = 7.5

    # Helper function to compute tangent angles from a point to a circle
    def get_tangents(x0, y0, xc, yc, r):
        dx = xc - x0
        dy = yc - y0
        dist = np.hypot(dx, dy)
        base = np.arctan2(dy, dx)
        da = np.arcsin(r / dist)
        return base + da, base - da

    # Direct rays (bulb top to top of sphere, bulb bot to bot of sphere) -> define Umbra
    a_top_dir, a_top_trans = get_tangents(x_src2, y_bulb_top, x_sph2, y_sph2, r_sph2)
    a_bot_trans, a_bot_dir = get_tangents(x_src2, y_bulb_bot, x_sph2, y_sph2, r_sph2)

    # Intersections at screen plane:
    y_umb_top2 = y_bulb_top + (x_scr2 - x_src2) * np.tan(a_top_dir)
    y_umb_bot2 = y_bulb_bot + (x_scr2 - x_src2) * np.tan(a_bot_dir)

    y_pen_top2 = y_bulb_bot + (x_scr2 - x_src2) * np.tan(a_bot_trans)
    y_pen_bot2 = y_bulb_top + (x_scr2 - x_src2) * np.tan(a_top_trans)

    # Tangent contact points on sphere
    xt_td = x_sph2 - r_sph2 * np.sin(a_top_dir)
    yt_td = y_sph2 + r_sph2 * np.cos(a_top_dir)
    xt_bd = x_sph2 + r_sph2 * np.sin(a_bot_dir)
    yt_bd = y_sph2 - r_sph2 * np.cos(a_bot_dir)

    # Main illuminated light beam
    ax2.fill([x_src2, x_scr2, x_scr2, x_src2],
             [y_bulb_top, y_pen_top2 + 0.3, y_pen_bot2 - 0.3, y_bulb_bot],
             color=CREAM, alpha=0.45, zorder=1)

    # Penumbra shading region behind sphere
    ax2.fill([x_sph2, x_scr2, x_scr2, x_sph2],
             [r_sph2, y_pen_top2, y_pen_bot2, -r_sph2],
             color=GREY, alpha=0.22, zorder=2)

    # Umbra cone (core shadow)
    ax2.fill([xt_td, x_scr2, x_scr2, xt_bd],
             [yt_td, y_umb_top2, y_umb_bot2, yt_bd],
             color=GREY, alpha=0.45, zorder=2)

    # Rays
    # Direct rays (solid line)
    ax2.plot([x_src2, x_scr2], [y_bulb_top, y_umb_top2], color=DEEP["orange"], lw=2.0, zorder=3)
    ax2.plot([x_src2, x_scr2], [y_bulb_bot, y_umb_bot2], color=DEEP["orange"], lw=2.0, zorder=3)

    # Transverse rays (dashed lines forming outer penumbra boundary)
    ax2.plot([x_src2, x_scr2], [y_bulb_bot, y_pen_top2], color=DEEP["orange"], lw=1.6, ls="--", zorder=3)
    ax2.plot([x_src2, x_scr2], [y_bulb_top, y_pen_bot2], color=DEEP["orange"], lw=1.6, ls="--", zorder=3)

    # Wide light bulb (extended source)
    bulb_w = 0.55
    bulb_h = 2 * r_bulb
    bulb = patches.FancyBboxPatch((x_src2 - bulb_w/2, -r_bulb), bulb_w, bulb_h,
                                  boxstyle="round,pad=0.15", facecolor=ORANGE,
                                  edgecolor=DEEP["orange"], lw=2.2, zorder=8)
    ax2.add_patch(bulb)
    # Filament inside bulb
    ax2.plot([x_src2, x_src2], [-r_bulb + 0.3, r_bulb - 0.3], color="white", lw=2.5, zorder=9)

    # Solid sphere
    sph2 = patches.Circle((x_sph2, y_sph2), r_sph2, facecolor=INK, edgecolor=INK, zorder=6)
    ax2.add_patch(sph2)

    # Oblique Screen showing Umbra and Penumbra rings
    scr_pts2 = np.array([
        [x_scr2, -scr_h/2],
        [x_scr2 + scr_w, -scr_h/2 + scr_skew],
        [x_scr2 + scr_w, scr_h/2 + scr_skew],
        [x_scr2, scr_h/2]
    ])
    screen_patch2 = patches.Polygon(scr_pts2, facecolor="white", edgecolor=INK, lw=2, zorder=4)
    ax2.add_patch(screen_patch2)

    cx_scr2 = x_scr2 + scr_w / 2
    cy_scr2 = scr_skew / 2

    # Penumbra outer ellipse (lighter grey ring)
    r_pen2_y = (y_pen_top2 - y_pen_bot2) / 2
    r_pen2_x = r_pen2_y * 0.45
    penumbra_ellipse = patches.Ellipse((cx_scr2, cy_scr2), 2*r_pen2_x, 2*r_pen2_y,
                                       angle=ellipse_angle, facecolor=GREY, edgecolor=DEEP["lav"], lw=1.2, zorder=5)
    ax2.add_patch(penumbra_ellipse)

    # Umbra central ellipse (dark central circle)
    r_umb2_y = (y_umb_top2 - y_umb_bot2) / 2
    r_umb2_x = r_umb2_y * 0.45
    umbra_ellipse2 = patches.Ellipse((cx_scr2, cy_scr2), 2*r_umb2_x, 2*r_umb2_y,
                                     angle=ellipse_angle, facecolor=INK, edgecolor=INK, zorder=6)
    ax2.add_patch(umbra_ellipse2)

    # Labels Ax2
    ax2.text(x_src2, -2.1, "Extended source\n(light bulb)", fontsize=15, ha="center", va="top",
             color=INK, bbox=dict(fc="white", ec="none", pad=2))
    ax2.text(x_sph2, -1.4, "Solid black\nsphere", fontsize=15, ha="center", va="top",
             color=INK, bbox=dict(fc="white", ec="none", pad=2))
    ax2.text(x_scr2 + scr_w/2, scr_h/2 + scr_skew + 0.3, "Screen", fontsize=15, ha="center", va="bottom",
             color=INK, weight="bold")

    # Annotations for Umbra and Penumbra
    ax2.annotate("Penumbra\n(lighter grey ring)",
                 xy=(cx_scr2 + r_pen2_x*0.65, cy_scr2 + r_pen2_y*0.6),
                 xytext=(cx_scr2 + 1.4, 2.3),
                 fontsize=14, color=INK, ha="left", va="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", zorder=10))

    ax2.annotate("Umbra\n(dark central circle)",
                 xy=(cx_scr2, cy_scr2),
                 xytext=(cx_scr2 + 1.4, -2.4),
                 fontsize=14, color=INK, fontweight='bold', ha="left", va="center",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.6),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", zorder=10))

    save(fig, out)
