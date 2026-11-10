from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Two-panel comparative diagram: Addition vs Condensation Polymerization
    fig = canvas(16, 9)
    
    # Left subplot: Addition Polymerization
    ax1 = fig.add_axes([0.03, 0.05, 0.45, 0.88])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Right subplot: Condensation Polymerization
    ax2 = fig.add_axes([0.52, 0.05, 0.45, 0.88])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    # Divider line
    fig.lines.extend([plt.Line2D([0.50, 0.50], [0.08, 0.92], color=GREY, linewidth=1.5, linestyle="--")])

    # ------------------ LEFT PANEL: ADDITION ------------------
    ax1.text(5, 9.4, "Addition Polymerization", fontsize=18, fontweight="bold", color=INK, ha="center")
    ax1.text(5, 8.7, "Monomers contain double bonds; no by-products", fontsize=14, color=GREY, ha="center", style="italic")
    
    # Monomers section
    ax1.text(5, 7.8, "Monomers (Ethene)", fontsize=15, fontweight="bold", color=DEEP["blue"], ha="center")
    
    def draw_ethene(ax, cx, cy):
        rect = patches.FancyBboxPatch((cx - 1.0, cy - 0.55), 2.0, 1.1, boxstyle="round,pad=0.1",
                                      fc=BLUE, ec=DEEP["blue"], lw=1.8)
        ax.add_patch(rect)
        # CH2=CH2
        ax.text(cx - 0.45, cy, "CH₂", fontsize=15, fontweight="bold", color=INK, ha="center", va="center")
        # Double bond
        ax.plot([cx - 0.15, cx + 0.15], [cy + 0.06, cy + 0.06], color=INK, lw=2.2)
        ax.plot([cx - 0.15, cx + 0.15], [cy - 0.06, cy - 0.06], color=INK, lw=2.2)
        ax.text(cx + 0.45, cy, "CH₂", fontsize=15, fontweight="bold", color=INK, ha="center", va="center")

    draw_ethene(ax1, 2.0, 6.7)
    ax1.text(3.5, 6.7, "+", fontsize=20, fontweight="bold", color=INK, ha="center", va="center")
    draw_ethene(ax1, 5.0, 6.7)
    ax1.text(6.5, 6.7, "+", fontsize=20, fontweight="bold", color=INK, ha="center", va="center")
    draw_ethene(ax1, 8.0, 6.7)
    
    # Downward arrow
    ax1.annotate("", xy=(5, 4.7), xytext=(5, 5.8),
                 arrowprops=dict(facecolor=INK, edgecolor=INK, width=3, headwidth=10))
    ax1.text(5.3, 5.25, "Polymerization", fontsize=14, color=INK, va="center")

    # Polymer chain section
    ax1.text(5, 4.3, "Polymer Chain (Polyethene)", fontsize=15, fontweight="bold", color=DEEP["blue"], ha="center")
    
    py = 3.2
    # Continuous polymer chain segment [...-CH2-CH2-CH2-CH2-CH2-CH2-...]
    chain_groups = ["CH₂", "CH₂", "CH₂", "CH₂", "CH₂", "CH₂"]
    xs = np.linspace(1.8, 8.2, 6)
    
    # Background card for polymer
    poly_box = patches.FancyBboxPatch((0.5, py - 0.8), 9.0, 1.6, boxstyle="round,pad=0.15",
                                      fc=CREAM, ec=DEEP["blue"], lw=1.5, ls="--")
    ax1.add_patch(poly_box)

    # Lead-in dashed bond
    ax1.plot([0.8, xs[0] - 0.5], [py, py], color=INK, lw=2.5, ls=":")
    ax1.text(0.65, py, "•••", fontsize=16, color=INK, ha="center", va="center")

    for i in range(len(xs)):
        ax1.text(xs[i], py, chain_groups[i], fontsize=15, fontweight="bold", color=INK, ha="center", va="center")
        if i < len(xs) - 1:
            ax1.plot([xs[i] + 0.5, xs[i+1] - 0.5], [py, py], color=INK, lw=2.5)

    # Lead-out dashed bond
    ax1.plot([xs[-1] + 0.5, 9.2], [py, py], color=INK, lw=2.5, ls=":")
    ax1.text(9.35, py, "•••", fontsize=16, color=INK, ha="center", va="center")

    # Note at bottom of panel 1
    ax1.text(5, 1.6, "• All atoms from monomers are retained\n• Double bonds open to form single bonds\n• Only one product formed", 
             fontsize=14, color=INK, ha="center", va="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.5"))

    # ------------------ RIGHT PANEL: CONDENSATION ------------------
    ax2.text(5, 9.4, "Condensation Polymerization", fontsize=18, fontweight="bold", color=INK, ha="center")
    ax2.text(5, 8.7, "Monomers with functional groups; small molecules eliminated", fontsize=14, color=GREY, ha="center", style="italic")
    
    ax2.text(5, 7.8, "Monomers (with Reactive Ends)", fontsize=15, fontweight="bold", color=DEEP["pink"], ha="center")

    # Square monomer with -OH groups
    sq_x, sq_y = 2.4, 6.7
    sq_patch = patches.Rectangle((sq_x - 0.6, sq_y - 0.5), 1.2, 1.0,
                                 fc=LAV, ec=DEEP["lav"], lw=2, zorder=3)
    ax2.add_patch(sq_patch)
    ax2.text(sq_x, sq_y, "A", fontsize=15, fontweight="bold", color=INK, ha="center", va="center", zorder=4)
    # Left OH
    ax2.plot([sq_x - 0.6, sq_x - 1.0], [sq_y, sq_y], color=INK, lw=2)
    ax2.text(sq_x - 1.1, sq_y, "HO", fontsize=14, fontweight="bold", color=DEEP["pink"], ha="right", va="center")
    # Right OH
    ax2.plot([sq_x + 0.6, sq_x + 1.0], [sq_y, sq_y], color=INK, lw=2)
    ax2.text(sq_x + 1.1, sq_y, "OH", fontsize=14, fontweight="bold", color=DEEP["pink"], ha="left", va="center")

    # Plus sign
    ax2.text(4.75, 6.7, "+", fontsize=20, fontweight="bold", color=INK, ha="center", va="center")

    # Round monomer with -H groups
    cir_x, cir_y = 7.1, 6.7
    cir_patch = patches.Circle((cir_x, cir_y), 0.55,
                               fc=PINK, ec=DEEP["pink"], lw=2, zorder=3)
    ax2.add_patch(cir_patch)
    ax2.text(cir_x, cir_y, "B", fontsize=15, fontweight="bold", color=INK, ha="center", va="center", zorder=4)
    # Left H
    ax2.plot([cir_x - 0.55, cir_x - 0.95], [cir_y, cir_y], color=INK, lw=2)
    ax2.text(cir_x - 1.05, cir_y, "H", fontsize=14, fontweight="bold", color=DEEP["blue"], ha="right", va="center")
    # Right H
    ax2.plot([cir_x + 0.55, cir_x + 0.95], [cir_y, cir_y], color=INK, lw=2)
    ax2.text(cir_x + 1.05, cir_y, "H", fontsize=14, fontweight="bold", color=DEEP["blue"], ha="left", va="center")

    # Downward arrow
    ax2.annotate("", xy=(5, 4.7), xytext=(5, 5.8),
                 arrowprops=dict(facecolor=INK, edgecolor=INK, width=3, headwidth=10))
    ax2.text(5.3, 5.25, "Polymerization", fontsize=14, color=INK, va="center")

    # Polymer chain section
    ax2.text(5, 4.3, "Alternating Polymer Chain + By-product", fontsize=15, fontweight="bold", color=DEEP["pink"], ha="center")

    # Alternating chain of square and round blocks
    b_types = ["sq", "round", "sq", "round"]
    b_xs = [2.0, 3.8, 5.6, 7.4]
    b_y = 3.2

    # Outer dashed box
    ax2.add_patch(patches.FancyBboxPatch((0.5, b_y - 0.8), 9.0, 1.6, boxstyle="round,pad=0.15",
                                         fc=CREAM, ec=DEEP["pink"], lw=1.5, ls="--"))

    # Lead in/out bonds
    ax2.plot([0.8, b_xs[0] - 0.5], [b_y, b_y], color=INK, lw=2.5, ls=":")
    ax2.text(0.65, b_y, "•••", fontsize=16, color=INK, ha="center", va="center")

    for i in range(len(b_types)):
        bx = b_xs[i]
        if b_types[i] == "sq":
            p = patches.Rectangle((bx - 0.45, b_y - 0.45), 0.9, 0.9, fc=LAV, ec=DEEP["lav"], lw=2, zorder=3)
            ax2.add_patch(p)
            ax2.text(bx, b_y, "A", fontsize=14, fontweight="bold", color=INK, ha="center", va="center", zorder=4)
        else:
            p = patches.Circle((bx, b_y), 0.45, fc=PINK, ec=DEEP["pink"], lw=2, zorder=3)
            ax2.add_patch(p)
            ax2.text(bx, b_y, "B", fontsize=14, fontweight="bold", color=INK, ha="center", va="center", zorder=4)

        if i < len(b_types) - 1:
            next_x = b_xs[i+1]
            ax2.plot([bx + 0.45, next_x - 0.45], [b_y, b_y], color=INK, lw=2.5)

    ax2.plot([b_xs[-1] + 0.45, 9.2], [b_y, b_y], color=INK, lw=2.5, ls=":")
    ax2.text(9.35, b_y, "•••", fontsize=16, color=INK, ha="center", va="center")

    # Small H2O molecules dropping out of the connections
    junctions = [(b_xs[i] + b_xs[i+1]) / 2 for i in range(len(b_xs) - 1)]
    for jx in junctions:
        ax2.annotate("", xy=(jx, b_y - 0.72), xytext=(jx, b_y - 0.08),
                     arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.8,
                                     connectionstyle="arc3,rad=-0.15"))
        h2o_badge = patches.FancyBboxPatch((jx - 0.48, b_y - 1.25), 0.96, 0.42, boxstyle="round,pad=0.08",
                                           fc=BLUE, ec=DEEP["blue"], lw=1.2)
        ax2.add_patch(h2o_badge)
        ax2.text(jx, b_y - 1.04, "+ H₂O", fontsize=14, fontweight="bold", color=INK, ha="center", va="center")

    # Note at bottom of panel 2
    ax2.text(5, 1.6, "• Two different functional groups react\n• Water (H₂O) eliminated at each junction\n• Two products: polymer + small molecule", 
             fontsize=14, color=INK, ha="center", va="center",
             bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.5"))

    save(fig, out)
