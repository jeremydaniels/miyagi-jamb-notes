import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Circle, Wedge, Rectangle
from style import *

def draw(out):
    fig = canvas(14, 8.5)
    
    # Left subplot: Whole transverse section (overview)
    # Right subplot: Enlarged sector showing detailed cellular layers
    ax_whole = fig.add_axes([0.03, 0.1, 0.38, 0.8])
    ax_detail = fig.add_axes([0.46, 0.08, 0.51, 0.84])
    
    for ax in [ax_whole, ax_detail]:
        ax.set_aspect("equal")
        ax.axis("off")
        
    # --- WHOLE TS VIEW (Left) ---
    ax_whole.set_xlim(-1.25, 1.25)
    ax_whole.set_ylim(-1.25, 1.35)
    ax_whole.set_title("Plan of T.S. of Sunflower Stem", fontsize=14, weight="bold", color=INK, pad=15)
    
    r_stem = 1.0
    r_cortex_in = 0.84
    r_pith = 0.55
    
    # Pith & Cortex ground tissue
    stem_bg = Circle((0, 0), r_stem, facecolor=CREAM, edgecolor=INK, lw=1.5, zorder=1)
    ax_whole.add_patch(stem_bg)
    
    # Vascular bundles (8 wedge-shaped bundles arranged in a ring)
    n_bundles = 8
    angles = np.linspace(0, 2*np.pi, n_bundles, endpoint=False)
    
    bundle_r_in = 0.52
    bundle_dtheta = 0.16
    
    c_xylem = PINK         
    c_phloem = BLUE        
    c_cambium = GREEN      
    c_scler = DEEP["pink"] 
    
    for ang in angles:
        t_pts = np.linspace(ang - bundle_dtheta, ang + bundle_dtheta, 15)
        # Sclerenchyma cap
        r0, r1 = 0.77, 0.83
        p_cap = Polygon(np.vstack([
            np.stack([r1 * np.cos(t_pts), r1 * np.sin(t_pts)], axis=1),
            np.stack([r0 * np.cos(t_pts[::-1]), r0 * np.sin(t_pts[::-1])], axis=1)
        ]), facecolor=c_scler, edgecolor=INK, lw=0.8, zorder=3)
        ax_whole.add_patch(p_cap)
        
        # Phloem
        r0, r1 = 0.70, 0.77
        p_ph = Polygon(np.vstack([
            np.stack([r1 * np.cos(t_pts), r1 * np.sin(t_pts)], axis=1),
            np.stack([r0 * np.cos(t_pts[::-1]), r0 * np.sin(t_pts[::-1])], axis=1)
        ]), facecolor=c_phloem, edgecolor=INK, lw=0.8, zorder=3)
        ax_whole.add_patch(p_ph)
        
        # Cambium line
        t_line = np.linspace(ang - bundle_dtheta*0.9, ang + bundle_dtheta*0.9, 10)
        ax_whole.plot(0.70 * np.cos(t_line), 0.70 * np.sin(t_line), color=DEEP["green"], lw=1.5, zorder=4)
        
        # Xylem
        t_in = np.linspace(ang - bundle_dtheta*0.4, ang + bundle_dtheta*0.4, 10)
        p_xy = Polygon(np.vstack([
            np.stack([0.70 * np.cos(t_pts), 0.70 * np.sin(t_pts)], axis=1),
            np.stack([bundle_r_in * np.cos(t_in[::-1]), bundle_r_in * np.sin(t_in[::-1])], axis=1)
        ]), facecolor=c_xylem, edgecolor=INK, lw=0.8, zorder=3)
        ax_whole.add_patch(p_xy)

    # Highlight sector wedge (around angle = pi/2 to avoid pith label at 0,0)
    sector_center = np.pi / 2
    sector_angle = np.pi / 8
    sector_arc = Wedge((0, 0), 1.05, np.degrees(sector_center - sector_angle), np.degrees(sector_center + sector_angle),
                       fill=False, edgecolor=DEEP["blue"], lw=1.8, linestyle="--", zorder=5)
    ax_whole.add_patch(sector_arc)
    ax_whole.plot([0, 1.05 * np.cos(sector_center - sector_angle)], [0, 1.05 * np.sin(sector_center - sector_angle)],
                  color=DEEP["blue"], lw=1.5, ls="--", zorder=5)
    ax_whole.plot([0, 1.05 * np.cos(sector_center + sector_angle)], [0, 1.05 * np.sin(sector_center + sector_angle)],
                  color=DEEP["blue"], lw=1.5, ls="--", zorder=5)
    
    con1 = patches.ConnectionPatch(xyA=(1.05 * np.cos(sector_center - sector_angle), 1.05 * np.sin(sector_center - sector_angle)), coordsA=ax_whole.transData,
                                  xyB=(5.0, 10.0), coordsB=ax_detail.transData,
                                  color=DEEP["blue"], lw=1.2, ls=":")
    con2 = patches.ConnectionPatch(xyA=(1.05 * np.cos(sector_center + sector_angle), 1.05 * np.sin(sector_center + sector_angle)), coordsA=ax_whole.transData,
                                  xyB=(0.0, 10.0), coordsB=ax_detail.transData,
                                  color=DEEP["blue"], lw=1.2, ls=":")
    fig.add_artist(con1)
    fig.add_artist(con2)

    ax_whole.text(0, 0, "pith", ha="center", va="center", fontsize=11, color=INK,
                  bbox=dict(fc="white", ec="none", pad=1), zorder=6)
    
    ray_ang = np.pi / 4
    rx, ry = 0.65 * np.cos(ray_ang), 0.65 * np.sin(ray_ang)
    ax_whole.annotate("medullary ray", xy=(rx, ry), xytext=(0.7, 0.95),
                     fontsize=11.5, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK, lw=1.0),
                     bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    ax_whole.annotate("epidermis", xy=(-0.707, 0.707), xytext=(-1.15, 0.9),
                     fontsize=11.5, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK, lw=1.0),
                     bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    ax_whole.annotate("cortex", xy=(-0.88, 0.1), xytext=(-1.2, 0.25),
                     fontsize=11.5, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK, lw=1.0),
                     bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))
    
    ax_whole.annotate("vascular\nbundle", xy=(-0.65, -0.2), xytext=(-1.18, -0.4),
                     fontsize=11.5, color=INK,
                     arrowprops=dict(arrowstyle="-", color=INK, lw=1.0),
                     bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # --- ENLARGED SECTOR VIEW (Right) ---
    ax_detail.set_xlim(-0.5, 9.8)
    ax_detail.set_ylim(-0.5, 11.2)
    ax_detail.set_title("Enlarged Sector: Cellular Organisation", fontsize=14, weight="bold", color=INK, pad=15)
    
    bg_poly = Polygon([[0.5, 0], [4.5, 0], [5.0, 10.0], [0.0, 10.0]], 
                      facecolor=CREAM, edgecolor="none", zorder=0)
    ax_detail.add_patch(bg_poly)
    
    ax_detail.plot([0.0, 0.5], [10.0, 0.0], color=GREY, lw=1, ls="--", zorder=2)
    ax_detail.plot([5.0, 4.5], [10.0, 0.0], color=GREY, lw=1, ls="--", zorder=2)
    
    # 1. Epidermis and Cuticle
    ax_detail.plot([0.0, 5.0], [10.05, 10.05], color=DEEP["orange"], lw=2.5, zorder=6)
    n_epi = 14
    xs_epi = np.linspace(0.0, 5.0, n_epi + 1)
    for i in range(n_epi):
        rec = Rectangle((xs_epi[i], 9.65), xs_epi[i+1]-xs_epi[i], 0.4,
                        facecolor="white", edgecolor=INK, lw=0.9, zorder=5)
        ax_detail.add_patch(rec)
        
    # Multicellular Hair
    hair_poly = Polygon([[2.25, 10.05], [2.32, 10.35], [2.40, 10.7], [2.5, 11.0], 
                         [2.60, 10.7], [2.68, 10.35], [2.75, 10.05]],
                        facecolor="white", edgecolor=INK, lw=1.2, zorder=6)
    ax_detail.add_patch(hair_poly)
    ax_detail.plot([2.32, 2.68], [10.35, 10.35], color=INK, lw=1.0, zorder=7)
    ax_detail.plot([2.40, 2.60], [10.70, 10.70], color=INK, lw=1.0, zorder=7)
    
    # 2. Collenchyma (hypodermis)
    y_coll_bounds = [9.65, 9.35, 9.03, 8.7]
    for row in range(3):
        y_bot = y_coll_bounds[row+1]
        y_top = y_coll_bounds[row]
        n_c = 11 + row
        xs = np.linspace(0.1 + row*0.05, 4.9 - row*0.05, n_c + 1)
        for j in range(n_c):
            cell = Rectangle((xs[j], y_bot), xs[j+1]-xs[j], y_top-y_bot,
                             facecolor="#f9fff5", edgecolor=GREY, lw=0.7, zorder=4)
            ax_detail.add_patch(cell)
            ax_detail.scatter([xs[j], xs[j+1]], [y_bot, y_bot], s=14, color=DEEP["green"], zorder=5)
            ax_detail.scatter([xs[j], xs[j+1]], [y_top, y_top], s=14, color=DEEP["green"], zorder=5)

    # 3. Parenchyma Cortex
    for cy in [8.4, 8.0]:
        for cx in np.arange(0.5, 4.6, 0.55):
            c_par = Circle((cx + (0.1 if cy==8.0 else 0), cy), 0.22,
                           facecolor=CREAM, edgecolor=GREY, lw=0.8, zorder=4)
            ax_detail.add_patch(c_par)
            
    # 4. Endodermis
    x_endo = np.linspace(0.3, 4.7, 100)
    y_endo = 7.55 + 0.08 * np.sin(x_endo * 10)
    ax_detail.plot(x_endo, y_endo, color=DEEP["orange"], lw=1.3, zorder=5)
    ax_detail.plot(x_endo, y_endo - 0.2, color=DEEP["orange"], lw=1.0, zorder=5)
    for sx in np.linspace(0.45, 4.55, 14):
        sy = 7.45 + 0.08 * np.sin(sx * 10)
        sg = Circle((sx, sy), 0.05, facecolor=DEEP["blue"], edgecolor=INK, lw=0.5, zorder=6)
        ax_detail.add_patch(sg)
        
    # 5. Sclerenchyma Cap
    scler_box = Rectangle((0.6, 6.3), 3.8, 0.95, facecolor=c_scler, edgecolor="none", zorder=3)
    ax_detail.add_patch(scler_box)
    for sy in np.linspace(6.4, 7.15, 5):
        for sx in np.linspace(0.8, 4.2, 16):
            c_sc = Circle((sx + ((sy*10)%2)*0.08, sy), 0.08, facecolor=c_scler, edgecolor="#8a1834", lw=0.8, zorder=4)
            ax_detail.add_patch(c_sc)
            ax_detail.plot(sx + ((sy*10)%2)*0.08, sy, '.', color="#ffccd5", ms=2, zorder=5)

    # 6. Phloem
    phloem_box = Rectangle((0.8, 5.3), 3.4, 1.0, facecolor=c_phloem, edgecolor="none", zorder=3)
    ax_detail.add_patch(phloem_box)
    for py in np.linspace(5.45, 6.15, 4):
        for px in np.linspace(1.0, 4.0, 10):
            st = Circle((px, py), 0.12, facecolor="#e1f0fc", edgecolor=DEEP["blue"], lw=0.7, zorder=4)
            ax_detail.add_patch(st)
            cc = Rectangle((px+0.12, py-0.08), 0.08, 0.16, facecolor=DEEP["blue"], edgecolor=INK, lw=0.5, zorder=5)
            ax_detail.add_patch(cc)

    # 7. Cambium
    camb_box = Rectangle((0.8, 5.0), 3.4, 0.3, facecolor=c_cambium, edgecolor="none", zorder=3)
    ax_detail.add_patch(camb_box)
    for c_row in [5.08, 5.22]:
        for cx in np.linspace(0.85, 4.15, 16):
            rec_c = Rectangle((cx, c_row-0.06), 0.18, 0.12, facecolor=c_cambium, edgecolor=DEEP["green"], lw=0.6, zorder=4)
            ax_detail.add_patch(rec_c)

    # 8. Xylem
    xy_poly = Polygon([[0.8, 5.0], [4.2, 5.0], [3.2, 2.2], [1.8, 2.2]], facecolor=c_xylem, edgecolor="none", zorder=3)
    ax_detail.add_patch(xy_poly)
    
    large_vessels = [
        (1.5, 4.5, 0.28), (2.2, 4.6, 0.32), (2.9, 4.5, 0.30), (3.6, 4.4, 0.27),
        (1.8, 3.9, 0.25), (2.5, 4.0, 0.28), (3.2, 3.8, 0.26),
        (2.1, 3.3, 0.22), (2.8, 3.2, 0.22)
    ]
    for vx, vy, vr in large_vessels:
        vessel = Circle((vx, vy), vr, facecolor="white", edgecolor=DEEP["pink"], lw=1.8, zorder=4)
        ax_detail.add_patch(vessel)
        v_in = Circle((vx, vy), vr-0.04, facecolor="white", edgecolor=DEEP["pink"], lw=0.6, zorder=4)
        ax_detail.add_patch(v_in)
        
    small_vessels = [
        (2.3, 2.8, 0.14), (2.7, 2.7, 0.13),
        (2.4, 2.45, 0.10), (2.6, 2.35, 0.09)
    ]
    for vx, vy, vr in small_vessels:
        vessel = Circle((vx, vy), vr, facecolor="white", edgecolor=DEEP["pink"], lw=1.4, zorder=4)
        ax_detail.add_patch(vessel)
        
    for xx, xy in [(1.3, 3.8), (1.6, 3.3), (3.4, 3.3), (2.0, 2.8), (3.0, 2.6), (2.2, 2.2)]:
        xp = Circle((xx, xy), 0.1, facecolor=PINK, edgecolor="#cc7a88", lw=0.5, zorder=3)
        ax_detail.add_patch(xp)

    # 9. Medullary ray
    for my in np.linspace(2.5, 6.0, 8):
        r_l = Circle((0.45, my), 0.20, facecolor=CREAM, edgecolor=GREY, lw=0.7, zorder=3)
        ax_detail.add_patch(r_l)
        r_r = Circle((4.55, my), 0.20, facecolor=CREAM, edgecolor=GREY, lw=0.7, zorder=3)
        ax_detail.add_patch(r_r)

    # 10. Pith
    pith_coords = [
        (2.0, 1.8, 0.28), (2.7, 1.7, 0.30), (3.3, 1.8, 0.26), (1.4, 1.6, 0.24),
        (1.8, 1.2, 0.33), (2.5, 1.1, 0.35), (3.2, 1.2, 0.32),
        (1.5, 0.6, 0.32), (2.2, 0.5, 0.36), (3.0, 0.6, 0.34), (2.6, 0.1, 0.32)
    ]
    for px, py, pr in pith_coords:
        pith_c = Circle((px, py), pr, facecolor=CREAM, edgecolor=GREY, lw=0.9, zorder=3)
        ax_detail.add_patch(pith_c)

    # --- DETAILED LABELS AND ANNOTATIONS ---
    label_style = dict(fontsize=11.5, color=INK, va="center")
    arrow_style = dict(arrowstyle="-", color=INK, lw=1.1)
    
    ax_detail.annotate("hair", xy=(2.55, 10.8), xytext=(6.2, 10.8),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("cuticle", xy=(4.2, 10.05), xytext=(6.2, 10.15),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("epidermis", xy=(4.2, 9.8), xytext=(6.2, 9.6),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("collenchyma (hypodermis)", xy=(3.8, 9.1), xytext=(6.2, 9.0),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("cortex", xy=(3.9, 8.2), xytext=(6.2, 8.35),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("endodermis (starch sheath)", xy=(3.6, 7.5), xytext=(6.2, 7.6),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("pericycle fibres (bundle cap)", xy=(3.6, 6.75), xytext=(6.2, 6.85),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("phloem", xy=(3.4, 5.8), xytext=(6.2, 5.95),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("cambium", xy=(3.5, 5.15), xytext=(6.2, 5.2),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("xylem", xy=(3.2, 4.3), xytext=(6.2, 4.35),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("protoxylem", xy=(2.65, 2.45), xytext=(6.2, 3.2),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("medullary ray", xy=(4.55, 4.0), xytext=(6.2, 2.2),
                       arrowprops=arrow_style, **label_style)
    ax_detail.annotate("pith", xy=(3.1, 0.8), xytext=(6.2, 0.8),
                       arrowprops=arrow_style, **label_style)

    save(fig, out)
    plt.close(fig)
