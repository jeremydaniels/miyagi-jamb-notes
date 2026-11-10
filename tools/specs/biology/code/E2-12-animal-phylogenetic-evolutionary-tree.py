from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Background zones: Water below, Land above
    # Water zone: y in [0, 48], Land zone: y in [48, 100]
    ax.axhspan(0, 48, color=BLUE, alpha=0.25, zorder=0)
    ax.axhspan(48, 100, color=GREEN, alpha=0.15, zorder=0)

    # Dividing dashed transition line
    ax.axhline(48, color=DEEP["blue"], ls="--", lw=1.5, alpha=0.7, zorder=1)

    # Zone labels
    ax.text(6, 12, "AQUATIC ENVIRONMENT\n(Water)", color=DEEP["blue"], fontsize=12,
            fontweight="bold", ha="left", va="center", alpha=0.85)
    ax.text(6, 85, "TERRESTRIAL &\nAERIAL ENVIRONMENT\n(Land)", color=DEEP["green"], fontsize=12,
            fontweight="bold", ha="left", va="center", alpha=0.85)

    # Exact label: "water to land"
    ax.annotate("water to land", xy=(50, 48), xytext=(50, 51.5),
                fontsize=11.5, fontweight="bold", color=INK, ha="center", va="bottom",
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.0),
                zorder=10)

    # Macro-group banners: invertebrates vs vertebrates
    ax.text(20, 93, "invertebrates", fontsize=14, fontweight="bold", color=DEEP["pink"],
            ha="center", va="center", bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.4", lw=1.8),
            zorder=10)
    ax.text(78, 93, "vertebrates", fontsize=14, fontweight="bold", color=DEEP["blue"],
            ha="center", va="center", bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.4", lw=1.8),
            zorder=10)

    # Helper function to draw curved branches using cubic Bezier curves
    def draw_branch(p0, p1, p2, p3, lw=3.0, color=INK):
        t = np.linspace(0, 1, 100)
        x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
        ax.plot(x, y, color=color, lw=lw, solid_capstyle="round", zorder=3)

    tree_color = DEEP["green"]

    # Tree Nodes definition
    root = (50, 10)     # Amoeba / Protozoa / common ancestor
    n1 = (50, 19)       # Hydra branch
    n2 = (49, 27)       # Tapeworm branch
    n3 = (48, 35)       # Roundworm branch
    n4 = (47, 43)       # Earthworm & branch splitting to insect & snail

    n_invert_crown = (35, 52)  # Splits into insect (arthropod) and snail (mollusc)
    n_vert_start = (55, 47)    # Fish divergence
    n_amph = (64, 57)          # Frog divergence & continues to lizard
    n_lizard = (73, 69)        # Lizard (reptile) node, which splits into bird and mammal

    # Main basal trunk
    draw_branch(root, (50, 13), (50, 16), n1, lw=5.0, color=tree_color)
    draw_branch(n1, (50, 22), (49.5, 24), n2, lw=4.5, color=tree_color)
    draw_branch(n2, (49, 30), (48.5, 32), n3, lw=4.2, color=tree_color)
    draw_branch(n3, (48, 38), (47.5, 40), n4, lw=4.0, color=tree_color)

    # Invertebrate side branches rising in order
    hydra_tip = (31, 21)
    tapeworm_tip = (29, 29)
    roundworm_tip = (27, 37)
    earthworm_tip = (25, 45)

    draw_branch(n1, (43, 19.5), (37, 20.0), hydra_tip, lw=2.5, color=tree_color)
    draw_branch(n2, (42, 27.5), (35, 28.0), tapeworm_tip, lw=2.5, color=tree_color)
    draw_branch(n3, (41, 35.5), (34, 36.0), roundworm_tip, lw=2.5, color=tree_color)
    draw_branch(n4, (39, 43.5), (32, 44.0), earthworm_tip, lw=2.5, color=tree_color)

    # Branch splitting to an insect (arthropod) and a snail (mollusc)
    draw_branch(n4, (44, 46), (39, 49), n_invert_crown, lw=3.2, color=tree_color)
    insect_tip = (23, 72)
    snail_tip = (38, 72)
    draw_branch(n_invert_crown, (30, 58), (25, 64), insect_tip, lw=2.5, color=tree_color)
    draw_branch(n_invert_crown, (37, 58), (38, 64), snail_tip, lw=2.5, color=tree_color)

    # Main trunk continues to vertebrates:
    # 1. A fish
    draw_branch(n4, (51, 44.5), (53, 45.5), n_vert_start, lw=4.0, color=tree_color)
    fish_tip = (75, 42)
    draw_branch(n_vert_start, (62, 46), (68, 43), fish_tip, lw=2.5, color=tree_color)

    # 2. Frog (amphibian)
    draw_branch(n_vert_start, (57, 50), (61, 53), n_amph, lw=3.6, color=tree_color)
    frog_tip = (53, 67)
    draw_branch(n_amph, (58, 60), (55, 63), frog_tip, lw=2.5, color=tree_color)

    # 3. Trunk continues to lizard (reptile)
    draw_branch(n_amph, (67, 61), (70, 65), n_lizard, lw=3.2, color=tree_color)

    # Lizard splits into two branches ending in a bird and a mammal (goat)
    bird_tip = (64, 84)
    mammal_tip = (82, 84)
    draw_branch(n_lizard, (69, 74), (66, 78), bird_tip, lw=2.5, color=tree_color)
    draw_branch(n_lizard, (77, 74), (80, 78), mammal_tip, lw=2.5, color=tree_color)

    # Node markers
    for pt in [root, n1, n2, n3, n4, n_invert_crown, n_vert_start, n_amph, n_lizard]:
        ax.scatter(pt[0], pt[1], s=40, color=DEEP["green"], zorder=4)

    # Helper function to annotate taxons
    def annotate_taxon(xy, common_name, phylum_name, align="right", offset=(-2, 0)):
        tx = xy[0] + offset[0]
        ty = xy[1] + offset[1]
        text_str = f"{common_name}\n({phylum_name})"
        ax.scatter(xy[0], xy[1], s=55, color=INK, zorder=5)
        ax.text(tx, ty, text_str, fontsize=11, ha=align, va="center",
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
                zorder=6)

    # Base: Protozoa / Amoeba / common ancestor
    ax.scatter(root[0], root[1], s=70, color=INK, zorder=5)
    ax.text(root[0], root[1] - 4.2, "Amoeba\n(Protozoa)", fontsize=11.5, fontweight="bold",
            ha="center", va="center", bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1.2),
            zorder=6)
    ax.annotate("common ancestor", xy=(root[0], root[1] - 1), xytext=(root[0] + 17, root[1] - 4.5),
                fontsize=11, fontstyle="italic", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8),
                ha="center", va="center", zorder=7)

    # Lower branches: Hydra, tapeworm, roundworm, earthworm
    annotate_taxon(hydra_tip, "Hydra", "Coelenterata", align="right", offset=(-2.5, 0))
    annotate_taxon(tapeworm_tip, "tapeworm (flatworm)", "Platyhelminthes", align="right", offset=(-2.5, 0))
    annotate_taxon(roundworm_tip, "roundworm (nematode)", "Nematoda", align="right", offset=(-2.5, 0))
    annotate_taxon(earthworm_tip, "earthworm (annelid)", "Annelida", align="right", offset=(-2.5, 0))

    # Upper invertebrate branches: insect and snail
    annotate_taxon(insect_tip, "insect", "Arthropoda", align="center", offset=(0, 3.8))
    annotate_taxon(snail_tip, "snail", "Mollusca", align="center", offset=(0, 3.8))

    # Vertebrate branches: fish, frog, lizard, bird, mammal
    annotate_taxon(fish_tip, "fish", "Pisces", align="left", offset=(2.5, 0))
    annotate_taxon(frog_tip, "frog", "Amphibia", align="right", offset=(-2.5, 0))

    # Lizard at n_lizard where the branch splits into bird and mammal
    ax.scatter(n_lizard[0], n_lizard[1], s=65, color=INK, zorder=6)
    ax.text(n_lizard[0] + 2.5, n_lizard[1] - 1.0, "lizard (reptile)\n(Reptilia)", fontsize=11, ha="left", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=0.8),
            zorder=7)

    # Bird and Mammal tips
    annotate_taxon(bird_tip, "bird", "Aves", align="center", offset=(0, 3.8))
    annotate_taxon(mammal_tip, "mammal (goat)", "Mammalia", align="center", offset=(0, 3.8))

    # Title
    ax.text(50, 97.5, "Evolutionary Tree of Animals", fontsize=15, fontweight="bold",
            ha="center", va="center", color=INK)

    save(fig, out)
