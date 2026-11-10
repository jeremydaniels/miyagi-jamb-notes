from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Title
    ax.text(6, 6.0, "Formation of a Dipeptide (Condensation Reaction)", 
            fontsize=18, fontweight="bold", ha="center", va="center", color=INK)

    # Helper function to draw an amino acid backbone
    # Amino acid 1
    # N - C(alpha) - C(=O) - OH
    # At (1.5, 3.5)
    # Positions of atoms in AA 1:
    # H2N at (1.0, 3.5), C_alpha at (2.2, 3.5), C=O at (3.4, 3.5)
    
    lw = 2.0
    
    # --- Amino Acid 1 ---
    # Central C
    ax.text(2.2, 3.5, r"$\mathbf{CH}$", fontsize=16, ha="center", va="center", color=INK)
    # R1 group (up)
    ax.plot([2.2, 2.2], [3.8, 4.4], color=INK, lw=lw)
    ax.text(2.2, 4.7, r"$\mathrm{R_1}$", fontsize=15, ha="center", va="center", color=DEEP["blue"], fontweight="bold")
    # H (down)
    ax.plot([2.2, 2.2], [3.2, 2.6], color=INK, lw=lw)
    ax.text(2.2, 2.3, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)
    
    # Left Amino group: H2N-
    ax.plot([1.9, 1.4], [3.5, 3.5], color=INK, lw=lw)
    ax.text(0.9, 3.5, r"$\mathrm{H_2N}$", fontsize=16, ha="center", va="center", color=INK)
    
    # Right Carboxyl group: -C(=O)-OH
    ax.plot([2.5, 3.1], [3.5, 3.5], color=INK, lw=lw)
    ax.text(3.3, 3.5, r"$\mathbf{C}$", fontsize=16, ha="center", va="center", color=INK)
    # =O (up)
    ax.plot([3.25, 3.25], [3.8, 4.4], color=INK, lw=lw)
    ax.plot([3.35, 3.35], [3.8, 4.4], color=INK, lw=lw)
    ax.text(3.3, 4.7, r"$\mathrm{O}$", fontsize=16, ha="center", va="center", color=INK)
    # -OH
    ax.plot([3.5, 3.9], [3.5, 3.5], color=INK, lw=lw)
    ax.text(4.25, 3.5, r"$\mathbf{OH}$", fontsize=16, ha="center", va="center", color=DEEP["pink"])

    # Label AA1
    ax.text(2.6, 1.5, "Amino acid 1", fontsize=15, ha="center", va="center", color=INK, style="italic")

    # Plus sign
    ax.text(4.75, 3.5, "+", fontsize=18, ha="center", va="center", color=GREY)

    # --- Amino Acid 2 ---
    # N(H) - C(alpha) - COOH
    ax.text(5.25, 3.5, r"$\mathbf{H}$", fontsize=16, ha="center", va="center", color=DEEP["pink"])
    ax.plot([5.45, 5.75], [3.5, 3.5], color=INK, lw=lw)
    ax.text(5.95, 3.5, r"$\mathrm{N}$", fontsize=16, ha="center", va="center", color=INK)
    # H on N pointing down
    ax.plot([5.95, 5.95], [3.2, 2.6], color=INK, lw=lw)
    ax.text(5.95, 2.3, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # C_alpha 2
    ax.plot([6.15, 6.6], [3.5, 3.5], color=INK, lw=lw)
    ax.text(6.9, 3.5, r"$\mathbf{CH}$", fontsize=16, ha="center", va="center", color=INK)
    # R2 group (up)
    ax.plot([6.9, 6.9], [3.8, 4.4], color=INK, lw=lw)
    ax.text(6.9, 4.7, r"$\mathrm{R_2}$", fontsize=15, ha="center", va="center", color=DEEP["orange"], fontweight="bold")
    # H (down)
    ax.plot([6.9, 6.9], [3.2, 2.6], color=INK, lw=lw)
    ax.text(6.9, 2.3, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # Carboxyl group 2: -COOH
    ax.plot([7.2, 7.65], [3.5, 3.5], color=INK, lw=lw)
    ax.text(8.1, 3.5, r"$\mathrm{COOH}$", fontsize=16, ha="center", va="center", color=INK)

    # Label AA2
    ax.text(6.7, 1.5, "Amino acid 2", fontsize=15, ha="center", va="center", color=INK, style="italic")

    # Dashed box enclosing OH and H (water removal)
    box = patches.FancyBboxPatch((3.95, 3.1), 1.5, 0.8, boxstyle="round,pad=0.1",
                                 ec=DEEP["pink"], fc=PINK, lw=1.8, linestyle="--", alpha=0.35)
    ax.add_patch(box)
    ax.text(4.7, 2.6, r"removal of $\mathrm{H_2O}$", fontsize=14, ha="center", va="center", color=DEEP["pink"])

    # Reaction arrow pointing right (with -H2O above/below or on dipeptide side)
    ax.annotate("", xy=(8.7, 3.5), xytext=(7.8 + 0.9, 3.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5))

    # --- Dipeptide Product ---
    # Centered around x = 9.8 to 11.5
    # Let's shift dipeptide to right side cleanly:
    # Dipeptide: H2N - CH(R1) - C(=O) - NH - CH(R2) - COOH
    # We can place it below or to the right. Since canvas is 12 wide, right side is good!
    # Wait, 8.7 to 12 is a bit tight for 6 atoms. Let's adjust scale or positions!
    # Let's adjust all x coordinates:
    pass

    # Clear and redraw with optimized x-spacing across 12-width:
    ax.clear()
    ax.axis("off")
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.8)

    ax.text(6.5, 6.2, "Formation of a Dipeptide (Condensation Reaction)", 
            fontsize=17, fontweight="bold", ha="center", va="center", color=INK)

    # --- LEFT SIDE: TWO AMINO ACIDS ---
    # AA1:
    # H2N at 0.8, CH(R1) at 1.7, C(=O) at 2.6, OH at 3.3
    ax.text(0.65, 3.8, r"$\mathbf{H_2N}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([1.05, 1.45], [3.8, 3.8], color=INK, lw=lw)
    
    # CH
    ax.text(1.7, 3.8, r"$\mathbf{CH}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([1.7, 1.7], [4.1, 4.65], color=INK, lw=lw)
    ax.text(1.7, 4.95, r"$\mathbf{R_1}$", fontsize=15, ha="center", va="center", color=DEEP["blue"])
    ax.plot([1.7, 1.7], [3.5, 2.95], color=INK, lw=lw)
    ax.text(1.7, 2.65, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # C=O
    ax.plot([1.95, 2.4], [3.8, 3.8], color=INK, lw=lw)
    ax.text(2.6, 3.8, r"$\mathbf{C}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([2.55, 2.55], [4.1, 4.65], color=INK, lw=lw)
    ax.plot([2.65, 2.65], [4.1, 4.65], color=INK, lw=lw)
    ax.text(2.6, 4.95, r"$\mathbf{O}$", fontsize=15, ha="center", va="center", color=INK)

    # -OH
    ax.plot([2.8, 3.1], [3.8, 3.8], color=INK, lw=lw)
    ax.text(3.35, 3.8, r"$\mathbf{OH}$", fontsize=15, ha="center", va="center", color=DEEP["pink"])

    # AA2:
    # H-N(H) at 4.1, 4.6, CH(R2) at 5.4, COOH at 6.3
    ax.text(4.15, 3.8, r"$\mathbf{H}$", fontsize=15, ha="center", va="center", color=DEEP["pink"])
    ax.plot([4.3, 4.5], [3.8, 3.8], color=INK, lw=lw)
    ax.text(4.7, 3.8, r"$\mathbf{N}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([4.7, 4.7], [3.5, 2.95], color=INK, lw=lw)
    ax.text(4.7, 2.65, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # CH
    ax.plot([4.9, 5.2], [3.8, 3.8], color=INK, lw=lw)
    ax.text(5.45, 3.8, r"$\mathbf{CH}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([5.45, 5.45], [4.1, 4.65], color=INK, lw=lw)
    ax.text(5.45, 4.95, r"$\mathbf{R_2}$", fontsize=15, ha="center", va="center", color=DEEP["orange"])
    ax.plot([5.45, 5.45], [3.5, 2.95], color=INK, lw=lw)
    ax.text(5.45, 2.65, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # COOH
    ax.plot([5.7, 6.05], [3.8, 3.8], color=INK, lw=lw)
    ax.text(6.45, 3.8, r"$\mathbf{COOH}$", fontsize=15, ha="center", va="center", color=INK)

    # Sub-labels for reactant amino acids
    ax.text(1.7, 1.8, "Amino acid 1", fontsize=14, ha="center", va="center", color=GREY, style="italic")
    ax.text(5.45, 1.8, "Amino acid 2", fontsize=14, ha="center", va="center", color=GREY, style="italic")

    # Water extraction dashed box
    box = patches.FancyBboxPatch((3.1, 3.35), 1.25, 0.9, boxstyle="round,pad=0.08",
                                 ec=DEEP["pink"], fc=PINK, lw=1.8, linestyle="--", alpha=0.45)
    ax.add_patch(box)
    ax.annotate("Water removed\n" + r"($\mathbf{-H_2O}$)", xy=(3.72, 3.35), xytext=(3.72, 2.1),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5),
                fontsize=14, ha="center", va="top", color=DEEP["pink"],
                bbox=dict(fc="white", ec=PINK, boxstyle="round,pad=0.2"))

    # Reaction arrow
    ax.annotate("", xy=(7.8, 3.8), xytext=(7.0, 3.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5))
    ax.text(7.4, 4.15, "Condensation", fontsize=14, ha="center", va="bottom", color=INK, style="italic")

    # --- RIGHT SIDE: DIPEPTIDE ---
    # Dipeptide starts at 8.2
    # H2N at 8.2, CH(R1) at 9.0, C(=O) at 9.75, NH at 10.5, CH(R2) at 11.25, COOH at 12.1
    ax.text(8.2, 3.8, r"$\mathbf{H_2N}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([8.5, 8.8], [3.8, 3.8], color=INK, lw=lw)

    # CH
    ax.text(9.0, 3.8, r"$\mathbf{CH}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([9.0, 9.0], [4.1, 4.65], color=INK, lw=lw)
    ax.text(9.0, 4.95, r"$\mathbf{R_1}$", fontsize=15, ha="center", va="center", color=DEEP["blue"])
    ax.plot([9.0, 9.0], [3.5, 2.95], color=INK, lw=lw)
    ax.text(9.0, 2.65, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # C=O
    ax.plot([9.2, 9.55], [3.8, 3.8], color=INK, lw=lw)
    ax.text(9.75, 3.8, r"$\mathbf{C}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([9.7, 9.7], [4.1, 4.65], color=INK, lw=lw)
    ax.plot([9.8, 9.8], [4.1, 4.65], color=INK, lw=lw)
    ax.text(9.75, 4.95, r"$\mathbf{O}$", fontsize=15, ha="center", va="center", color=INK)

    # PEPTIDE BOND: between C (9.75) and N (10.5)
    ax.plot([9.95, 10.3], [3.8, 3.8], color=DEEP["green"], lw=3.5)

    # NH
    ax.text(10.5, 3.8, r"$\mathbf{NH}$", fontsize=15, ha="center", va="center", color=INK)

    # CH
    ax.plot([10.75, 11.05], [3.8, 3.8], color=INK, lw=lw)
    ax.text(11.25, 3.8, r"$\mathbf{CH}$", fontsize=15, ha="center", va="center", color=INK)
    ax.plot([11.25, 11.25], [4.1, 4.65], color=INK, lw=lw)
    ax.text(11.25, 4.95, r"$\mathbf{R_2}$", fontsize=15, ha="center", va="center", color=DEEP["orange"])
    ax.plot([11.25, 11.25], [3.5, 2.95], color=INK, lw=lw)
    ax.text(11.25, 2.65, r"$\mathrm{H}$", fontsize=15, ha="center", va="center", color=INK)

    # COOH
    ax.plot([11.45, 11.75], [3.8, 3.8], color=INK, lw=lw)
    ax.text(12.2, 3.8, r"$\mathbf{COOH}$", fontsize=15, ha="center", va="center", color=INK)

    # Highlight box for the peptide bond (-CO-NH-)
    pb_box = patches.FancyBboxPatch((9.5, 3.25), 1.25, 1.95, boxstyle="round,pad=0.08",
                                     ec=DEEP["green"], fc=GREEN, lw=2.0, linestyle="-", alpha=0.35)
    ax.add_patch(pb_box)

    # Annotation pointing to peptide bond
    ax.annotate("Peptide bond\n(amide linkage)",
                xy=(10.12, 3.25), xytext=(10.12, 1.8),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.0),
                fontsize=14, ha="center", va="top", color=DEEP["green"], fontweight="bold",
                bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.25"))

    # Product Byproduct: + H2O
    ax.text(11.25, 1.1, r"$\mathbf{+\ H_2O}$", fontsize=16, ha="center", va="center", color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.3"))

    # Label dipeptide
    ax.text(10.12, 5.65, "Dipeptide", fontsize=16, fontweight="bold", ha="center", va="center", color=INK)

    save(fig, out)
