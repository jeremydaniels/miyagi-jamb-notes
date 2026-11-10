from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 10.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10.5)
    ax.axis("off")

    # Titles & Column Headers
    ax.text(6.0, 10.0, "Sickle-Cell Mutation: Molecular to Cellular Effects", 
            fontsize=16, fontweight="bold", color=INK, ha="center", va="center")
    
    ax.text(3.5, 9.4, "Normal (HbA)", fontsize=14, fontweight="bold", color=DEEP["blue"], ha="center")
    ax.text(8.8, 9.4, "Sickle-cell (HbS)", fontsize=14, fontweight="bold", color=DEEP["pink"], ha="center")

    # Vertical dividing line between left and right columns
    ax.plot([6.15, 6.15], [0.5, 9.2], color=GREY, lw=1.2, ls="--", alpha=0.7)

    # Level indicator banners on far left
    ax.text(0.3, 8.4, "DNA\nLevel", fontsize=11.5, fontweight="bold", color=INK, va="center", ha="left")
    ax.text(0.3, 5.8, "Protein\nLevel", fontsize=11.5, fontweight="bold", color=INK, va="center", ha="left")
    ax.text(0.3, 2.3, "Cellular\nLevel", fontsize=11.5, fontweight="bold", color=INK, va="center", ha="left")

    # -------------------------------------------------------------
    # ROW 1: DNA Sequences (y ~ 7.6 - 8.9)
    # -------------------------------------------------------------
    normal_seq = ["C", "T", "G", "A", "G", "G"]
    sickle_seq = ["C", "T", "G", "T", "G", "G"]
    
    x_norm_start = 1.95
    x_sick_start = 7.25
    box_w = 0.48
    box_h = 0.52
    spacing = 0.52
    
    # Normal DNA boxes
    for i, base in enumerate(normal_seq):
        bx = x_norm_start + i * spacing
        by = 8.15
        is_mut = (i == 3)
        fc = CREAM if is_mut else BLUE
        ec = DEEP["pink"] if is_mut else DEEP["blue"]
        lw = 2.0 if is_mut else 1.2
        rect = patches.FancyBboxPatch((bx, by), box_w, box_h, boxstyle="round,pad=0.03",
                                      fc=fc, ec=ec, lw=lw)
        ax.add_patch(rect)
        ax.text(bx + box_w/2, by + box_h/2, base, fontsize=12.5, fontweight="bold",
                ha="center", va="center", color=DEEP["pink"] if is_mut else INK)

    # Sickle DNA boxes
    for i, base in enumerate(sickle_seq):
        bx = x_sick_start + i * spacing
        by = 8.15
        is_mut = (i == 3)
        fc = PINK if is_mut else BLUE
        ec = DEEP["pink"] if is_mut else DEEP["blue"]
        lw = 2.2 if is_mut else 1.2
        rect = patches.FancyBboxPatch((bx, by), box_w, box_h, boxstyle="round,pad=0.03",
                                      fc=fc, ec=ec, lw=lw)
        ax.add_patch(rect)
        ax.text(bx + box_w/2, by + box_h/2, base, fontsize=12.5, fontweight="bold",
                ha="center", va="center", color=DEEP["pink"] if is_mut else INK)

    # Labels for DNA
    ax.text(3.5, 7.6, "normal DNA: GAG", fontsize=11.5, ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1.2))
    ax.text(8.8, 7.6, "mutated DNA: GTG", fontsize=11.5, ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.25", lw=1.2))

    # Base substitution arrow linking the normal 'A' to mutated 'T'
    ax.annotate("base substitution (A → T)", 
                xy=(x_sick_start + 3 * spacing + box_w/2, 8.75), 
                xytext=(6.15, 8.9),
                fontsize=11.5, fontweight="bold", color=DEEP["pink"], ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5,
                                connectionstyle="arc3,rad=-0.12"))

    # Connecting arrows DNA -> Protein
    ax.annotate("", xy=(3.5, 6.75), xytext=(3.5, 7.25),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    ax.annotate("", xy=(8.8, 6.75), xytext=(8.8, 7.25),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    ax.text(3.65, 7.0, "transcription\n& translation", fontsize=9.0, color=GREY, va="center")
    ax.text(8.95, 7.0, "transcription\n& translation", fontsize=9.0, color=GREY, va="center")

    # -------------------------------------------------------------
    # ROW 2: Amino Acid Chains (y ~ 4.7 - 6.6)
    # -------------------------------------------------------------
    aa_names_norm = ["Val", "His", "Leu", "Thr", "Pro", "Glu", "Glu"]
    aa_names_sick = ["Val", "His", "Leu", "Thr", "Pro", "Val", "Glu"]
    
    r_bead = 0.25
    start_x_norm = 1.7
    start_x_sick = 7.0
    spacing_aa = 0.60
    y_aa = 5.8

    # Backbone lines
    ax.plot([start_x_norm, start_x_norm + 6 * spacing_aa], [y_aa, y_aa], color=GREY, lw=2, zorder=1)
    ax.plot([start_x_sick, start_x_sick + 6 * spacing_aa], [y_aa, y_aa], color=GREY, lw=2, zorder=1)

    for i in range(7):
        # Normal chain
        bx = start_x_norm + i * spacing_aa
        is_target = (i == 5)  # 6th bead
        fc = BLUE if is_target else CREAM
        ec = DEEP["blue"] if is_target else GREY
        circle = patches.Circle((bx, y_aa), r_bead, fc=fc, ec=ec, lw=2.0 if is_target else 1.2, zorder=2)
        ax.add_patch(circle)
        ax.text(bx, y_aa, aa_names_norm[i], fontsize=9.0, ha="center", va="center", 
                fontweight="bold" if is_target else "normal", color=INK, zorder=3)
        
        # Sickle chain
        bx_s = start_x_sick + i * spacing_aa
        fc_s = PINK if is_target else CREAM
        ec_s = DEEP["pink"] if is_target else GREY
        circle_s = patches.Circle((bx_s, y_aa), r_bead, fc=fc_s, ec=ec_s, lw=2.0 if is_target else 1.2, zorder=2)
        ax.add_patch(circle_s)
        ax.text(bx_s, y_aa, aa_names_sick[i], fontsize=9.0, ha="center", va="center",
                fontweight="bold" if is_target else "normal", color=INK, zorder=3)

    # Amino acid 6th position callouts
    ax.annotate("glutamic acid", xy=(start_x_norm + 5 * spacing_aa, y_aa + r_bead), 
                xytext=(start_x_norm + 5 * spacing_aa, y_aa + 0.65),
                fontsize=11.5, fontweight="bold", color=DEEP["blue"], ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.4),
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1))
    
    ax.annotate("valine", xy=(start_x_sick + 5 * spacing_aa, y_aa + r_bead), 
                xytext=(start_x_sick + 5 * spacing_aa, y_aa + 0.65),
                fontsize=11.5, fontweight="bold", color=DEEP["pink"], ha="center",
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.4),
                bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.25", lw=1))

    # Haemoglobin labels
    ax.text(3.5, 4.95, "normal haemoglobin (HbA)", fontsize=11.5, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))
    ax.text(8.8, 4.95, "sickle haemoglobin (HbS)", fontsize=11.5, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Connecting arrows Protein -> Cell
    ax.annotate("", xy=(3.5, 3.85), xytext=(3.5, 4.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    ax.annotate("", xy=(8.8, 3.85), xytext=(8.8, 4.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # -------------------------------------------------------------
    # ROW 3: Red Blood Cells (y ~ 0.5 - 3.8)
    # -------------------------------------------------------------
    # Normal biconcave red blood cell
    cx_norm, cy_norm = 3.5, 2.3
    outer_rbc = patches.Circle((cx_norm, cy_norm), 1.25, fc=PINK, ec=DEEP["pink"], lw=2.2)
    ax.add_patch(outer_rbc)
    inner_rbc = patches.Ellipse((cx_norm, cy_norm), 1.2, 0.9, fc="#FAD2D8", ec=DEEP["pink"], lw=1.2, ls="--")
    ax.add_patch(inner_rbc)
    ax.text(cx_norm, cy_norm, "biconcave\ndisc", fontsize=10.0, ha="center", va="center", color=INK)

    # Sickle-shaped red blood cell (smooth crescent)
    t = np.linspace(-np.pi * 0.72, np.pi * 0.72, 100)
    x_outer = 8.6 + 1.35 * np.cos(t)
    y_outer = 2.3 + 1.45 * np.sin(t)
    x_inner = 8.6 + 0.65 * np.cos(t[::-1]) + 0.38
    y_inner = 2.3 + 1.22 * np.sin(t[::-1])
    sickle_x = np.concatenate([x_outer, x_inner])
    sickle_y = np.concatenate([y_outer, y_inner])

    sickle_cell = patches.Polygon(np.column_stack([sickle_x, sickle_y]), closed=True,
                                  fc=PINK, ec=DEEP["pink"], lw=2.2)
    ax.add_patch(sickle_cell)
    ax.text(9.15, 2.3, "sickle\nshape", fontsize=10.0, ha="center", va="center", color=INK)

    # Cell labels at the bottom
    ax.text(3.5, 0.65, "normal red cell", fontsize=12.5, fontweight="bold", ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1.2))
    ax.text(8.8, 0.65, "sickled red cell", fontsize=12.5, fontweight="bold", ha="center", va="center",
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.3", lw=1.2))

    save(fig, out)
