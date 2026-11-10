from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Circle, Rectangle

def draw(out):
    fig = canvas(15, 7.5)
    
    # 4 side-by-side panels
    axes = [fig.add_axes([0.03 + i * 0.24, 0.08, 0.22, 0.82]) for i in range(4)]
    
    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
    CELLULOSE_BG = '#E8F5E9'
    CELLULOSE_WALL = '#A5D6A7' 
    CORNER_GREEN = '#81C784'   # bright pale green for corner thickening
    LIGNIN_FILL = '#F8BBD0'    # pale pink-red
    LIGNIN_WALL = DEEP['pink'] # pink-red wall
    
    # -------------------------------------------------------------
    # PANEL 1: COLLENCHYMA
    # -------------------------------------------------------------
    ax1 = axes[0]
    ax1.text(5, 11.3, "Collenchyma", ha='center', va='center', fontsize=15, weight='bold', color=INK)
    ax1.text(5, 10.4, "Transverse view (T.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    
    centers = [
        (3.5, 8.8), (6.5, 8.8),
        (2.0, 7.2), (5.0, 7.2), (8.0, 7.2),
        (3.5, 5.6), (6.5, 5.6)
    ]
    r = 1.3
    angles = np.linspace(0, 2*np.pi, 7)[:-1]
    
    # Draw corners first so they sit behind cell outlines but form thick blobs
    corners = set()
    for cx, cy in centers:
        for a in angles:
            corners.add((round(cx + r * np.cos(a), 2), round(cy + r * np.sin(a), 2)))
            
    for kx, ky in corners:
        if 1.0 <= kx <= 9.0 and 4.8 <= ky <= 9.6:
            ax1.add_patch(Circle((kx, ky), 0.5, fc=CORNER_GREEN, ec='none'))

    # Cell outlines and bodies
    for cx, cy in centers:
        poly_pts = [[cx + r * np.cos(a), cy + r * np.sin(a)] for a in angles]
        poly = Polygon(poly_pts, closed=True, fc=CELLULOSE_BG, ec=CELLULOSE_WALL, lw=1.5)
        ax1.add_patch(poly)
        ax1.add_patch(Circle((cx + 0.2, cy + 0.2), 0.22, fc=DEEP['green'], ec=INK, lw=1.0))
    
    ax1.text(5, 4.4, "Longitudinal view (L.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    ls_xs = [2.2, 3.8, 5.4, 7.0]
    for lx in ls_xs:
        rect = Rectangle((lx, 0.8), 1.6, 3.2, fc=CELLULOSE_BG, ec=CELLULOSE_WALL, lw=1.5)
        ax1.add_patch(rect)
        ax1.plot([lx, lx], [0.8, 4.0], color=CORNER_GREEN, lw=4.5)
        ax1.add_patch(Circle((lx + 0.8, 2.4), 0.25, fc=DEEP['green'], ec=INK, lw=1.0))
    ax1.plot([ls_xs[-1]+1.6, ls_xs[-1]+1.6], [0.8, 4.0], color=CORNER_GREEN, lw=4.5)
    
    ax1.annotate("thickened corner", xy=(4.9, 8.5), xytext=(2.0, 9.8),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax1.annotate("nucleus", xy=(5.2, 7.4), xytext=(7.5, 8.4),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))

    # -------------------------------------------------------------
    # PANEL 2: SCLERENCHYMA
    # -------------------------------------------------------------
    ax2 = axes[1]
    ax2.text(5, 11.3, "Sclerenchyma", ha='center', va='center', fontsize=15, weight='bold', color=INK)
    ax2.text(5, 10.4, "Transverse view (T.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    
    s_centers = [(3.2, 8.6), (6.2, 8.6), (2.0, 7.0), (4.8, 7.0), (7.6, 7.0), (3.5, 5.5), (6.3, 5.5)]
    for cx, cy in s_centers:
        poly_pts = [[cx + 1.25 * np.cos(a + 0.2), cy + 1.25 * np.sin(a + 0.2)] for a in angles]
        poly = Polygon(poly_pts, closed=True, fc=LIGNIN_FILL, ec=LIGNIN_WALL, lw=2.0)
        ax2.add_patch(poly)
        lumen = Circle((cx, cy), 0.28, fc='white', ec=LIGNIN_WALL, lw=1.2)
        ax2.add_patch(lumen)
        for pa in np.linspace(0, 2*np.pi, 5)[:-1]:
            dx, dy = np.cos(pa), np.sin(pa)
            ax2.plot([cx + 0.28 * dx, cx + 1.05 * dx], [cy + 0.28 * dy, cy + 1.05 * dy], color=LIGNIN_WALL, lw=1.0, ls=':')

    ax2.text(5, 3.8, "Fibre & Sclereid (L.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    
    fibre_paths = [
        [(2.0, 0.4), (2.4, 2.0), (2.0, 3.4), (1.6, 2.0)],
        [(2.6, 0.2), (3.0, 1.7), (2.6, 3.1), (2.2, 1.7)],
        [(3.2, 0.5), (3.6, 2.1), (3.2, 3.5), (2.8, 2.1)]
    ]
    for pts in fibre_paths:
        poly = Polygon(pts, closed=True, fc=LIGNIN_FILL, ec=LIGNIN_WALL, lw=1.5)
        ax2.add_patch(poly)
        cx_mid = (pts[1][0] + pts[3][0]) / 2
        ax2.plot([cx_mid, cx_mid], [pts[0][1] + 0.4, pts[2][1] - 0.4], color='white', lw=1.2)
        
    sc_cx, sc_cy = 7.2, 1.8
    sc_poly = Polygon([[sc_cx + 1.5*np.cos(a), sc_cy + 1.5*np.sin(a)] for a in np.linspace(0, 2*np.pi, 9)[:-1]],
                      closed=True, fc=LIGNIN_FILL, ec=LIGNIN_WALL, lw=2.0)
    ax2.add_patch(sc_poly)
    ax2.add_patch(Circle((sc_cx, sc_cy), 0.35, fc='white', ec=LIGNIN_WALL, lw=1.2))
    for pa in np.linspace(0, 2*np.pi, 7)[:-1]:
        dx, dy = np.cos(pa), np.sin(pa)
        ax2.plot([sc_cx + 0.35*dx, sc_cx + 1.3*dx], [sc_cy + 0.35*dy, sc_cy + 1.3*dy], color=LIGNIN_WALL, lw=1.2, ls=':')
        
    ax2.annotate("lumen", xy=(4.8, 7.0), xytext=(4.8, 8.3),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, ha='center', bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax2.annotate("pit", xy=(5.4, 7.3), xytext=(7.5, 8.2),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax2.annotate("sclerenchyma fibre", xy=(2.7, 2.7), xytext=(0.4, 2.5),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax2.annotate("sclereid", xy=(7.2, 3.0), xytext=(7.2, 4.4),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, ha='center', bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))

    # -------------------------------------------------------------
    # PANEL 3: XYLEM
    # -------------------------------------------------------------
    ax3 = axes[2]
    ax3.text(5, 11.3, "Xylem", ha='center', va='center', fontsize=15, weight='bold', color=INK)
    ax3.text(5, 10.4, "Four vessel types (L.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    
    v_xs = [0.8, 3.1, 5.4, 7.7]
    w = 1.6
    y_b, y_t = 1.0, 9.8
    
    for vx in v_xs:
        ax3.add_patch(Rectangle((vx, y_b), w, y_t - y_b, fc='#FFF0F5', ec=LIGNIN_WALL, lw=2.0))
        
    v1_x = v_xs[0]
    for ry in np.linspace(y_b + 0.7, y_t - 0.7, 8):
        ax3.add_patch(patches.Ellipse((v1_x + w/2, ry), w*0.9, 0.45, fc='none', ec=LIGNIN_WALL, lw=3.0))
        
    v2_x = v_xs[1]
    sy = np.linspace(y_b + 0.4, y_t - 0.4, 150)
    for i in range(len(sy) - 1):
        phase = (sy[i] - y_b) * 3.5
        sx = v2_x + w/2 + (w * 0.42) * np.sin(phase)
        sx_next = v2_x + w/2 + (w * 0.42) * np.sin((sy[i+1] - y_b) * 3.5)
        lw = 3.5 if np.cos(phase) > 0 else 1.5
        ax3.plot([sx, sx_next], [sy[i], sy[i+1]], color=LIGNIN_WALL, lw=lw)
        
    v3_x = v_xs[2]
    for ly in np.linspace(y_b + 0.6, y_t - 0.6, 12):
        ax3.plot([v3_x + 0.15, v3_x + w - 0.15], [ly, ly], color=LIGNIN_WALL, lw=3.5)
        
    v4_x = v_xs[3]
    ax3.add_patch(Rectangle((v4_x, y_b), w, y_t - y_b, fc=LIGNIN_FILL, ec=LIGNIN_WALL, lw=2.0))
    for py in np.linspace(y_b + 0.8, y_t - 0.8, 7):
        for px_off in [0.45, w - 0.45]:
            ax3.add_patch(Circle((v4_x + px_off, py), 0.26, fc='white', ec=LIGNIN_WALL, lw=1.8))
            ax3.add_patch(Circle((v4_x + px_off, py), 0.08, fc=INK, ec='none'))
            
    labels = ["annular", "spiral", "scalariform", "pitted"]
    for vx, lbl in zip(v_xs, labels):
        ax3.text(vx + w/2, 0.4, lbl, ha='center', va='center', fontsize=11, color=INK,
                 bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
        
    ax3.annotate("xylem vessel", xy=(v1_x + w/2, 8.4), xytext=(v1_x - 0.4, 9.0),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))

    # -------------------------------------------------------------
    # PANEL 4: PHLOEM
    # -------------------------------------------------------------
    ax4 = axes[3]
    ax4.text(5, 11.3, "Phloem", ha='center', va='center', fontsize=15, weight='bold', color=INK)
    ax4.text(5, 10.4, "Longitudinal view (L.S.)", ha='center', va='center', fontsize=11, style='italic', color=GREY)
    
    cc_x, cc_w = 0.8, 1.6
    for c_idx, cy_start in enumerate([1.0, 5.4]):
        ax4.add_patch(Rectangle((cc_x, cy_start), cc_w, 4.3, fc='#C8E6C9', ec=CELLULOSE_WALL, lw=2.0))
        ax4.add_patch(Circle((cc_x + cc_w/2, cy_start + 2.15), 0.42, fc=DEEP['green'], ec=INK, lw=1.2))
        ax4.text(cc_x + cc_w/2, cy_start + 2.15, "N", ha='center', va='center', fontsize=8, color='white', weight='bold')

    st_x, st_w = 2.5, 3.2
    ax4.add_patch(Rectangle((st_x, 1.0), st_w, 8.7, fc=CELLULOSE_BG, ec=CELLULOSE_WALL, lw=2.0))
    for plate_y in [1.0, 5.35, 9.7]:
        ax4.plot([st_x, st_x + st_w], [plate_y, plate_y], color=DEEP['green'], lw=3.0)
        for pore_x in np.linspace(st_x + 0.4, st_x + st_w - 0.4, 5):
            ax4.add_patch(Circle((pore_x, plate_y), 0.12, fc='white', ec=DEEP['green'], lw=1.2))
            
    for strand_x in np.linspace(st_x + 0.6, st_x + st_w - 0.6, 4):
        ax4.plot([strand_x, strand_x], [1.3, 5.1], color='#A5D6A7', lw=1.2, ls='--')
        ax4.plot([strand_x, strand_x], [5.6, 9.4], color='#A5D6A7', lw=1.2, ls='--')

    f_x_base = 6.4
    fibre_specs = [
        [(f_x_base, 1.0), (f_x_base + 0.9, 5.0), (f_x_base, 9.0), (f_x_base - 0.5, 5.0)],
        [(f_x_base + 0.9, 2.0), (f_x_base + 1.8, 6.0), (f_x_base + 0.9, 9.7), (f_x_base + 0.4, 6.0)],
        [(f_x_base + 1.8, 0.5), (f_x_base + 2.6, 4.5), (f_x_base + 1.8, 8.5), (f_x_base + 1.3, 4.5)]
    ]
    for f_pts in fibre_specs:
        poly = Polygon(f_pts, closed=True, fc=LIGNIN_FILL, ec=LIGNIN_WALL, lw=1.8)
        ax4.add_patch(poly)
        
    ax4.annotate("companion cell", xy=(cc_x + cc_w/2, 7.8), xytext=(cc_x - 0.5, 9.5),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax4.annotate("sieve plate", xy=(st_x + st_w/2, 5.35), xytext=(st_x - 1.2, 4.3),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax4.annotate("sieve tube", xy=(st_x + st_w/2, 7.5), xytext=(st_x + 0.4, 8.4),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))
    ax4.annotate("phloem fibre", xy=(f_x_base + 1.2, 5.5), xytext=(f_x_base + 0.2, 3.2),
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                 fontsize=11, color=INK, bbox=dict(fc="white", ec=GREY, pad=0.2, boxstyle="round"))

    save(fig, out)
