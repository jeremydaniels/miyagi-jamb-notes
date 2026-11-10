from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 9.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Color definitions matching specifications
    c_parenchyma = CREAM
    c_sclerenchyma = DEEP["pink"]  # darker pink
    c_sclerenchyma_fill = PINK      # lighter pink fill for sheath/hypodermis band
    c_xylem = "#FFD1D1"            # pale red
    c_xylem_edge = DEEP["orange"]
    c_phloem = BLUE                # pale blue
    c_phloem_edge = DEEP["blue"]
    c_lacuna = "#FFFFFF"           # white air space
    
    # -------------------------------------------------------------
    # Title
    # -------------------------------------------------------------
    ax.text(7.5, 9.0, "Transverse Section of a Young Monocotyledonous Stem (Maize)",
            ha="center", va="center", fontsize=15, weight="bold", color=INK)

    # -------------------------------------------------------------
    # LEFT: Whole Stem Section (Circle)
    # -------------------------------------------------------------
    stem_center = (4.0, 4.5)
    r_outer = 3.6
    r_hypo = 3.35

    # 1. Epidermis (outer edge circle) & Hypodermis ring
    # Outer circle filled with hypodermis pink
    hypo_circle = patches.Circle(stem_center, r_outer, facecolor="#F8D7DA", edgecolor=INK, lw=1.5)
    ax.add_patch(hypo_circle)

    # Inner ground tissue (parenchyma pale cream)
    ground_circle = patches.Circle(stem_center, r_hypo, facecolor=c_parenchyma, edgecolor=c_sclerenchyma, lw=1.2)
    ax.add_patch(ground_circle)

    # Scatter vascular bundles (crowded near periphery, larger and sparser towards centre)
    np.random.seed(42)
    
    # Generate bundles systematically to look realistic
    bundles = []
    # Peripheral rings (small, crowded)
    for r in np.linspace(2.2, 3.15, 4):
        n_bundles = int(2 * np.pi * r / 0.45)
        angles = np.linspace(0, 2 * np.pi, n_bundles, endpoint=False) + np.random.uniform(-0.1, 0.1, n_bundles)
        for a in angles:
            bx = stem_center[0] + r * np.cos(a) + np.random.uniform(-0.04, 0.04)
            by = stem_center[1] + r * np.sin(a) + np.random.uniform(-0.04, 0.04)
            bundles.append((bx, by, 0.11, 0.15, np.degrees(a) - 90))

    # Intermediate zone (medium, less crowded)
    for r in [1.3, 1.7]:
        n_bundles = int(2 * np.pi * r / 0.65)
        angles = np.linspace(0, 2 * np.pi, n_bundles, endpoint=False) + np.random.uniform(-0.15, 0.15, n_bundles)
        for a in angles:
            bx = stem_center[0] + r * np.cos(a) + np.random.uniform(-0.06, 0.06)
            by = stem_center[1] + r * np.sin(a) + np.random.uniform(-0.06, 0.06)
            bundles.append((bx, by, 0.15, 0.20, np.degrees(a) - 90))

    # Center zone (larger, sparse)
    for r in [0.4, 0.8]:
        n_bundles = int(2 * np.pi * r / 0.75) + 1
        angles = np.linspace(0, 2 * np.pi, n_bundles, endpoint=False) + np.random.uniform(-0.2, 0.2, n_bundles)
        for a in angles:
            bx = stem_center[0] + r * np.cos(a) + np.random.uniform(-0.05, 0.05)
            by = stem_center[1] + r * np.sin(a) + np.random.uniform(-0.05, 0.05)
            bundles.append((bx, by, 0.18, 0.24, np.degrees(a) - 90))
    # One near absolute center
    bundles.append((stem_center[0] + 0.05, stem_center[1] - 0.05, 0.19, 0.25, 10))

    for bx, by, bw, bh, ang in bundles:
        ell = patches.Ellipse((bx, by), bw, bh, angle=ang, facecolor="#F8B4B4", edgecolor=DEEP["pink"], lw=0.7)
        ax.add_patch(ell)

    # Target bundle to enlarge (highlighted with an indicator box)
    target_bx, target_by = stem_center[0] + 1.7 * np.cos(0.2), stem_center[1] + 1.7 * np.sin(0.2)
    hl_rect = patches.Rectangle((target_bx - 0.28, target_by - 0.32), 0.56, 0.64,
                                fill=False, edgecolor=DEEP["blue"], lw=1.8, linestyle="--")
    ax.add_patch(hl_rect)

    # Subtitle for left
    ax.text(4.0, 0.5, "Whole stem cross-section", ha="center", va="center", fontsize=13, weight="bold", color=INK)

    # -------------------------------------------------------------
    # RIGHT: Enlarged Vascular Bundle
    # -------------------------------------------------------------
    box_x, box_y, box_w, box_h = 8.5, 0.9, 6.0, 7.5
    bg_box = patches.Rectangle((box_x, box_y), box_w, box_h, facecolor="white", edgecolor=GREY, lw=1.5, zorder=0)
    ax.add_patch(bg_box)
    ax.text(box_x + box_w/2, box_y + box_h - 0.4, "Enlarged Vascular Bundle", ha="center", va="center", fontsize=13, weight="bold", color=INK)

    # Connecting zoom lines from target rect to enlarged box
    ax.plot([target_bx + 0.28, box_x], [target_by + 0.32, box_y + box_h - 0.2], color=GREY, lw=1.2, linestyle=":")
    ax.plot([target_bx + 0.28, box_x], [target_by - 0.32, box_y + 0.2], color=GREY, lw=1.2, linestyle=":")

    b_center = (box_x + 3.0, box_y + 3.5)

    # 1. Sclerenchymatous bundle sheath (outer thick oval boundary)
    sheath_outer = patches.Ellipse(b_center, 3.6, 4.8, facecolor=PINK, edgecolor=DEEP["pink"], lw=2.5, zorder=1)
    ax.add_patch(sheath_outer)

    # Sheath inner area (ground of the bundle)
    sheath_inner = patches.Ellipse(b_center, 3.0, 4.1, facecolor="#FFF9F5", edgecolor=DEEP["pink"], lw=1.2, linestyle="--", zorder=2)
    ax.add_patch(sheath_inner)

    # 2. Phloem at the top (outer side)
    phloem_poly = patches.Ellipse((b_center[0], b_center[1] + 1.15), 1.7, 1.25,
                                  facecolor=c_phloem, edgecolor=c_phloem_edge, lw=1.8, zorder=3)
    ax.add_patch(phloem_poly)

    # Cellular pattern inside phloem (sieve tubes & companion cells)
    for p_dx in np.linspace(-0.55, 0.55, 5):
        for p_dy in np.linspace(-0.35, 0.35, 3):
            if (p_dx/0.75)**2 + (p_dy/0.5)**2 < 0.9:
                sieve_c = patches.Circle((b_center[0] + p_dx, b_center[1] + 1.15 + p_dy), 0.08,
                                         facecolor="white", edgecolor=c_phloem_edge, lw=0.8, zorder=4)
                ax.add_patch(sieve_c)

    # 3. Metaxylem vessels (two large lateral vessels side by side)
    mx_left = patches.Circle((b_center[0] - 0.75, b_center[1] + 0.05), 0.58,
                             facecolor=c_xylem, edgecolor=c_xylem_edge, lw=2.2, zorder=5)
    mx_right = patches.Circle((b_center[0] + 0.75, b_center[1] + 0.05), 0.58,
                              facecolor=c_xylem, edgecolor=c_xylem_edge, lw=2.2, zorder=5)
    ax.add_patch(mx_left)
    ax.add_patch(mx_right)

    # Concentric lumen rings for metaxylem
    for center in [(b_center[0] - 0.75, b_center[1] + 0.05), (b_center[0] + 0.75, b_center[1] + 0.05)]:
        inner_c = patches.Circle(center, 0.46, facecolor="white", edgecolor=c_xylem_edge, lw=1.2, zorder=6)
        ax.add_patch(inner_c)

    # 4. Protoxylem vessel(s) (one or two smaller vessels below metaxylem)
    px1 = patches.Circle((b_center[0], b_center[1] - 0.35), 0.28,
                         facecolor=c_xylem, edgecolor=c_xylem_edge, lw=1.8, zorder=5)
    px1_in = patches.Circle((b_center[0], b_center[1] - 0.35), 0.20,
                            facecolor="white", edgecolor=c_xylem_edge, lw=1.0, zorder=6)
    ax.add_patch(px1)
    ax.add_patch(px1_in)

    # 5. Protoxylem lacuna (large round air space at the bottom)
    lacuna = patches.Circle((b_center[0], b_center[1] - 1.1), 0.52,
                            facecolor=c_lacuna, edgecolor=INK, lw=2.0, zorder=5)
    ax.add_patch(lacuna)

    # -------------------------------------------------------------
    # ANNOTATIONS & LABELS
    # -------------------------------------------------------------
    # Helper function for label with pointer
    def label_pointer(text, xy, xytext, ha="left", va="center"):
        ax.annotate(text, xy=xy, xytext=xytext,
                    fontsize=12, color=INK, weight="medium",
                    ha=ha, va=va,
                    bbox=dict(fc="white", ec="none", pad=2),
                    arrowprops=dict(arrowstyle="-", color=INK, lw=1.2),
                    zorder=10)

    # Labels on Whole Stem View
    label_pointer("epidermis", (stem_center[0] - r_outer * np.cos(np.pi/4), stem_center[1] + r_outer * np.sin(np.pi/4)),
                  (0.6, 7.8), ha="left")
    label_pointer("sclerenchyma hypodermis", (stem_center[0] - 3.48 * np.cos(np.pi/6), stem_center[1] + 3.48 * np.sin(np.pi/6)),
                  (0.3, 6.6), ha="left")
    label_pointer("ground tissue (parenchyma)", (stem_center[0] - 1.6, stem_center[1] + 0.8),
                  (0.3, 3.8), ha="left")
    label_pointer("vascular bundle", (stem_center[0] - 2.6, stem_center[1] - 1.2),
                  (0.5, 2.2), ha="left")

    # Labels on Enlarged Bundle
    label_pointer("bundle sheath", (b_center[0] - 1.65, b_center[1] + 1.2),
                  (box_x - 0.3, 6.2), ha="right")
    label_pointer("phloem", (b_center[0] + 0.8, b_center[1] + 1.45),
                  (box_x + box_w - 0.2, 5.8), ha="right")
    label_pointer("metaxylem vessel", (b_center[0] + 1.25, b_center[1] + 0.15),
                  (box_x + box_w - 0.2, 4.4), ha="right")
    label_pointer("protoxylem", (b_center[0] + 0.3, b_center[1] - 0.35),
                  (box_x + box_w - 0.2, 3.2), ha="right")
    label_pointer("protoxylem lacuna", (b_center[0] + 0.52, b_center[1] - 1.1),
                  (box_x + box_w - 0.2, 2.0), ha="right")

    save(fig, out)
