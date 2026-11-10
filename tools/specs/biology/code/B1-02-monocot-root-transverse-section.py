import sys
sys.path.insert(0, '/home/user/miyagi-jamb-notes/tools/codedraw')
from style import *
import numpy as np
import matplotlib.patches as mpatches

def draw(out):
    fig = canvas(12, 10)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-6.5, 7.5)
    ax.set_ylim(-5.5, 5.5)

    # Coordinates and Radii
    r_epidermis = 4.2
    r_exodermis_out = 4.15
    r_exodermis_in = 3.65
    r_cortex_in = 2.45
    r_endodermis_in = 2.30
    r_pericycle_in = 2.15
    r_pith = 1.35

    # 1. Background / Layers
    cortex_poly = plt.Circle((0, 0), r_exodermis_in, fc=CREAM, ec="none", zorder=1)
    ax.add_patch(cortex_poly)

    exo_poly = mpatches.Wedge((0, 0), r_exodermis_out, 0, 360, width=r_exodermis_out - r_exodermis_in,
                              fc="#F0E5D0", ec=DEEP["orange"], lw=0.5, zorder=2)
    ax.add_patch(exo_poly)

    ax.plot(r_epidermis * np.cos(np.linspace(0, 2*np.pi, 300)),
            r_epidermis * np.sin(np.linspace(0, 2*np.pi, 300)),
            color=INK, lw=1.2, zorder=4)

    # Root hairs omitted at the very top to avoid title
    hair_angles = [10, 30, 50, 130, 150, 170, 195, 215, 240, 260, 285, 310, 335, 350]
    for ang in hair_angles:
        rad = np.radians(ang)
        r_vals = np.linspace(r_epidermis, r_epidermis + 0.9 + 0.2*np.sin(rad), 15)
        lat_wave = 0.08 * np.sin(np.linspace(0, 3*np.pi, 15))
        hx = r_vals * np.cos(rad) - lat_wave * np.sin(rad)
        hy = r_vals * np.sin(rad) + lat_wave * np.cos(rad)
        ax.plot(hx, hy, color=INK, lw=1.3, zorder=3)

    for r_mid in [(r_exodermis_out + r_exodermis_in)/2 + 0.12, (r_exodermis_out + r_exodermis_in)/2 - 0.12]:
        n_exo = 48
        d_th = 2 * np.pi / n_exo
        for i in range(n_exo):
            th = i * d_th + (0.02 if r_mid > 3.9 else 0)
            x_vals = np.array([r_mid - 0.12, r_mid + 0.12]) * np.cos(th)
            y_vals = np.array([r_mid - 0.12, r_mid + 0.12]) * np.sin(th)
            ax.plot(x_vals, y_vals, color=GREY, lw=0.6, zorder=3)
            
    ax.plot(r_exodermis_out * np.cos(np.linspace(0, 2*np.pi, 300)),
            r_exodermis_out * np.sin(np.linspace(0, 2*np.pi, 300)),
            color=DEEP["orange"], lw=1.0, zorder=3)
    ax.plot(r_exodermis_in * np.cos(np.linspace(0, 2*np.pi, 300)),
            r_exodermis_in * np.sin(np.linspace(0, 2*np.pi, 300)),
            color=GREY, lw=0.8, zorder=3)

    np.random.seed(42)
    for r_c in np.linspace(2.65, 3.45, 5):
        n_c = int(2 * np.pi * r_c / 0.32)
        d_th = 2 * np.pi / n_c
        for i in range(n_c):
            th = i * d_th + np.random.uniform(-0.03, 0.03)
            cx = r_c * np.cos(th)
            cy = r_c * np.sin(th)
            c_circ = plt.Circle((cx, cy), 0.14, fc=CREAM, ec="#C5BEAE", lw=0.7, zorder=2)
            ax.add_patch(c_circ)

    stele_poly = plt.Circle((0, 0), r_cortex_in, fc="#FCF9F2", ec="none", zorder=3)
    ax.add_patch(stele_poly)

    n_endo = 42
    d_th_endo = 2 * np.pi / n_endo
    passage_cell_indices = [6, 17, 27, 38] 

    for i in range(n_endo):
        th0 = i * d_th_endo
        th1 = (i + 1) * d_th_endo

        is_passage = i in passage_cell_indices

        if is_passage:
            endo_cell = mpatches.Wedge((0, 0), r_cortex_in, np.degrees(th0), np.degrees(th1),
                                       width=r_cortex_in - r_endodermis_in,
                                       fc="#FFFFFF", ec=INK, lw=0.8, zorder=5)
            ax.add_patch(endo_cell)
        else:
            endo_cell = mpatches.Wedge((0, 0), r_cortex_in, np.degrees(th0), np.degrees(th1),
                                       width=r_cortex_in - r_endodermis_in,
                                       fc="#F4E8D8", ec=GREY, lw=0.6, zorder=5)
            ax.add_patch(endo_cell)
            th_arc = np.linspace(th0, th1, 10)
            ax.plot(r_endodermis_in * np.cos(th_arc), r_endodermis_in * np.sin(th_arc),
                    color=DEEP["orange"], lw=2.2, zorder=6)
            
            x_vals = np.array([r_endodermis_in, r_endodermis_in + 0.1]) * np.cos(th0)
            y_vals = np.array([r_endodermis_in, r_endodermis_in + 0.1]) * np.sin(th0)
            ax.plot(x_vals, y_vals, color=DEEP["orange"], lw=1.8, zorder=6)

    ax.plot(r_cortex_in * np.cos(np.linspace(0, 2*np.pi, 300)),
            r_cortex_in * np.sin(np.linspace(0, 2*np.pi, 300)), color=INK, lw=0.8, zorder=6)

    peri_wedge = mpatches.Wedge((0, 0), r_endodermis_in, 0, 360,
                                width=r_endodermis_in - r_pericycle_in,
                                fc="#FAFAF5", ec=GREY, lw=0.5, zorder=4)
    ax.add_patch(peri_wedge)
    ax.plot(r_pericycle_in * np.cos(np.linspace(0, 2*np.pi, 300)),
            r_pericycle_in * np.sin(np.linspace(0, 2*np.pi, 300)),
            color=GREY, lw=0.7, ls=":", zorder=5)

    pith_circle = plt.Circle((0, 0), r_pith, fc="#F8F7F0", ec=GREY, lw=0.8, zorder=4)
    ax.add_patch(pith_circle)

    pith_pts = [(0, 0)]
    for pr in [0.35, 0.7, 1.05]:
        pn = int(2 * np.pi * pr / 0.35)
        for j in range(pn):
            pth = j * (2 * np.pi / pn) + 0.15 * pr
            pith_pts.append((pr * np.cos(pth), pr * np.sin(pth)))

    for px, py in pith_pts:
        p_cell = plt.Circle((px, py), 0.17, fc="#FDFBF7", ec="#CDC6B8", lw=0.8, zorder=5)
        ax.add_patch(p_cell)

    n_bundles = 14
    d_bundle = 2 * np.pi / n_bundles

    xylem_fc = PINK
    xylem_ec = DEEP["pink"]
    phloem_fc = BLUE
    phloem_ec = DEEP["blue"]

    xylem_sample_coord = None
    phloem_sample_coord = None

    for i in range(n_bundles):
        th_x = i * d_bundle
        th_p = th_x + d_bundle / 2

        r_meta = 1.62
        xm_x = r_meta * np.cos(th_x)
        xm_y = r_meta * np.sin(th_x)
        meta_circ = plt.Circle((xm_x, xm_y), 0.16, fc=xylem_fc, ec=xylem_ec, lw=1.5, zorder=7)
        ax.add_patch(meta_circ)

        r_proto1 = 1.88
        xp1_x = r_proto1 * np.cos(th_x)
        xp1_y = r_proto1 * np.sin(th_x)
        p1_circ = plt.Circle((xp1_x, xp1_y), 0.08, fc=xylem_fc, ec=xylem_ec, lw=1.2, zorder=7)
        ax.add_patch(p1_circ)

        r_proto2 = 2.05
        xp2_x = r_proto2 * np.cos(th_x)
        xp2_y = r_proto2 * np.sin(th_x)
        p2_circ = plt.Circle((xp2_x, xp2_y), 0.055, fc=xylem_fc, ec=xylem_ec, lw=1.0, zorder=7)
        ax.add_patch(p2_circ)

        if i == 6:  # Select a bundle on the left side to avoid lines crossing the root
            xylem_sample_coord = (xm_x, xm_y)

        r_phloem = 1.95
        ph_x = r_phloem * np.cos(th_p)
        ph_y = r_phloem * np.sin(th_p)
        ph_patch = plt.Circle((ph_x, ph_y), 0.11, fc=phloem_fc, ec=phloem_ec, lw=1.2, zorder=7)
        ax.add_patch(ph_patch)

        c1 = plt.Circle((ph_x + 0.05*np.cos(th_p+1), ph_y + 0.05*np.sin(th_p+1)), 0.035,
                        fc=phloem_fc, ec=phloem_ec, lw=0.8, zorder=8)
        ax.add_patch(c1)

        if i == 6:
            phloem_sample_coord = (ph_x, ph_y)

    pass_th = (6 + 0.5) * d_th_endo
    passage_sample_coord = (r_endodermis_in * np.cos(pass_th) + 0.08, r_endodermis_in * np.sin(pass_th) + 0.08)

    def annotate_feature(text, xy, xytext, ha="left"):
        ax.annotate(text, xy=xy, xytext=xytext,
                    fontsize=12.5, color=INK,
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.1),
                    ha=ha, va="center",
                    bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.9))

    annotate_feature("root hair", (4.8 * np.cos(np.radians(30)), 4.8 * np.sin(np.radians(30))), (5.4, 3.2))
    annotate_feature("piliferous layer", (r_epidermis * np.cos(np.radians(18)), r_epidermis * np.sin(np.radians(18))), (5.4, 2.3))
    annotate_feature("exodermis", (3.9 * np.cos(np.radians(5)), 3.9 * np.sin(np.radians(5))), (5.4, 1.3))
    annotate_feature("cortex", (3.0 * np.cos(np.radians(-15)), 3.0 * np.sin(np.radians(-15))), (5.4, 0.3))
    annotate_feature("endodermis", (r_cortex_in * np.cos(np.radians(-32)), r_cortex_in * np.sin(np.radians(-32))), (5.4, -0.7))
    annotate_feature("passage cell", passage_sample_coord, (5.4, -1.7))

    annotate_feature("pericycle", (r_pericycle_in * np.cos(np.radians(160)), r_pericycle_in * np.sin(np.radians(160))), (-5.4, 2.2), ha="right")
    annotate_feature("phloem", phloem_sample_coord, (-5.4, 1.2), ha="right")
    annotate_feature("xylem", xylem_sample_coord, (-5.4, 0.2), ha="right")
    annotate_feature("pith", (-0.6, -0.2), (-5.4, -1.0), ha="right")

    ax.text(0, 5.2, "T.S. of Young Monocotyledonous Root (Maize)",
            ha="center", va="center", fontsize=15, fontweight="bold", color=INK,
            bbox=dict(fc="white", ec="none", pad=2, alpha=0.8))

    save(fig, out)

if __name__ == '__main__':
    draw(sys.argv[1])
