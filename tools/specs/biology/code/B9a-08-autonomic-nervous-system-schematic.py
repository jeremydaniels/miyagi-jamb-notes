from style import *
import numpy as np

def draw(out):
    fig = canvas(15, 11)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Column Titles
    ax.text(3.4, 10.4, "sympathetic (fight or flight)", fontsize=13, fontweight="bold", 
            color=DEEP["orange"], ha="center", va="center")
    ax.text(11.6, 10.4, "parasympathetic (rest and digest)", fontsize=13, fontweight="bold", 
            color=DEEP["blue"], ha="center", va="center")

    # Central CNS (Brain & Spinal Cord)
    # Brain
    brain = plt.matplotlib.patches.FancyBboxPatch((7.0, 8.8), 1.0, 1.2,
                                                 boxstyle="round,pad=0.2,rounding_size=0.3",
                                                 fc=PINK, ec=DEEP["pink"], lw=2)
    ax.add_patch(brain)
    ax.text(7.5, 9.4, "brain", fontsize=12, fontweight="bold", color=INK, ha="center", va="center")

    # Spinal Cord: long vertical rounded bar
    cord = plt.matplotlib.patches.FancyBboxPatch((7.32, 1.2), 0.36, 7.4,
                                                boxstyle="round,pad=0.1,rounding_size=0.1",
                                                fc=PINK, ec=DEEP["pink"], lw=2)
    ax.add_patch(cord)
    ax.text(7.5, 0.95, "spinal cord", fontsize=12, fontweight="bold", color=INK, ha="center", va="center")

    # Spinal Cord Region annotations (on the cord)
    ax.text(7.5, 5.2, "thoracic and lumbar region", fontsize=10, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5), rotation=90)
    ax.text(7.5, 2.2, "sacral region", fontsize=10, color=INK, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5), rotation=90)

    # Organs and their vertical levels
    # Explicitly separate organs to match all required labels:
    # eye, salivary gland, lungs, heart, stomach, intestine, adrenal gland, bladder
    organs = [
        {"name": "eye", "y": 8.8, "symp": "dilated pupil", "para": "constricted pupil"},
        {"name": "salivary gland", "y": 7.8, "symp": "inhibited", "para": "stimulated"},
        {"name": "lungs", "y": 6.8, "symp": "bronchioles dilated", "para": "bronchioles constricted"},
        {"name": "heart", "y": 5.8, "symp": "faster", "para": "slower"},
        {"name": "stomach", "y": 4.8, "symp": "inhibited", "para": "stimulated"},
        {"name": "intestine", "y": 3.8, "symp": "inhibited", "para": "stimulated"},
        {"name": "adrenal gland", "y": 2.8, "symp": "adrenaline released", "para": None},
        {"name": "bladder", "y": 1.7, "symp": "relaxed", "para": "contracted"},
    ]

    # Sympathetic Chain Ganglia (left of spinal cord: x = 6.4)
    chain_x = 6.4
    # Chain vertical line spanning thoracic and lumbar origins
    ax.plot([chain_x, chain_x], [2.7, 7.6], color=DEEP["orange"], lw=2.5, linestyle="-", zorder=2)

    # Sympathetic chain ganglia label placed cleanly to the left, with white bbox so no fibres clash
    ax.text(chain_x - 0.15, 8.35, "sympathetic chain ganglia", fontsize=11, color=DEEP["orange"],
            ha="right", va="center", fontweight="bold",
            bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.25", lw=1))
    ax.annotate("", xy=(chain_x, 7.65), xytext=(chain_x - 0.45, 8.15),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.3))

    # Pre-ganglionic sympathetic roots leaving thoracic/lumbar
    symp_origins = [7.5, 7.0, 6.4, 5.7, 4.9, 4.1, 3.4, 2.8]
    for yo, org in zip(symp_origins, organs):
        # Bead on chain
        ax.plot(chain_x, yo, "o", color=DEEP["orange"], markersize=6, zorder=3)
        # short pre-ganglionic fibre from spinal cord to chain ganglion
        ax.plot([7.32, chain_x], [yo, yo], color=DEEP["orange"], lw=1.8, zorder=1)

        # post-ganglionic long fibre from chain to organ box (left side at x=4.7)
        yt = org["y"]
        # Route fibre clearly around the chain label
        ax.plot([chain_x, 5.0, 4.6], [yo, yt, yt], color=DEEP["orange"], lw=1.8, linestyle="--", zorder=1)

        # Left label (Sympathetic action & Organ name)
        symp_box_text = f"{org['name']}\n({org['symp']})"
        ax.text(2.6, yt, symp_box_text, fontsize=10.5, color=INK, ha="center", va="center",
                bbox=dict(fc=CREAM, ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.4))
        # Arrow pointing to the organ box
        ax.annotate("", xy=(3.8, yt), xytext=(4.6, yt),
                    arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.4))

    # Parasympathetic Side (Right side)
    vagus_drawn = False
    for org in organs:
        yt = org["y"]
        if org["para"] is None:
            # Adrenal gland has no parasympathetic innervation
            continue

        ganglion_x = 10.3
        # Determine origin on CNS
        if org["name"] in ["eye", "salivary gland"]:
            # Cranial nerves leaving brain
            yo = 9.2 if org["name"] == "eye" else 8.9
            ax.plot([7.9, 8.8, ganglion_x], [yo, yt, yt], color=DEEP["blue"], lw=1.8, zorder=1)
        elif org["name"] in ["lungs", "heart", "stomach", "intestine"]:
            # Vagus nerve from brainstem
            yo = 8.6
            ax.plot([7.9, 8.5, ganglion_x], [yo, yt, yt], color=DEEP["blue"], lw=1.8, zorder=1)
            if not vagus_drawn and org["name"] == "heart":
                vagus_drawn = True
                ax.text(8.7, 7.3, "vagus nerve", fontsize=11, color=DEEP["blue"],
                        ha="center", va="center", fontweight="bold",
                        bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.25", lw=1))
        elif org["name"] == "bladder":
            # Sacral spinal cord
            yo = 2.0
            ax.plot([7.68, 8.8, ganglion_x], [yo, yt, yt], color=DEEP["blue"], lw=1.8, zorder=1)

        # Parasympathetic ganglion near organ
        ax.plot(ganglion_x, yt, "o", color=DEEP["blue"], markersize=6, zorder=3)
        # short post-ganglionic fibre to organ box
        ax.plot([ganglion_x, 11.1], [yt, yt], color=DEEP["blue"], lw=1.8, linestyle="--", zorder=1)
        ax.annotate("", xy=(11.2, yt), xytext=(10.7, yt),
                    arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=1.4))

        # Right label (Parasympathetic action & Organ name)
        para_box_text = f"{org['name']}\n({org['para']})"
        ax.text(12.4, yt, para_box_text, fontsize=10.5, color=INK, ha="center", va="center",
                bbox=dict(fc=CREAM, ec=DEEP["blue"], boxstyle="round,pad=0.35", lw=1.4))

    # Fiber type key at the bottom
    leg_y = 0.45
    # Solid line = preganglionic
    ax.plot([2.4, 3.2], [leg_y, leg_y], color=INK, lw=1.8)
    ax.text(3.35, leg_y, "Preganglionic fibre", fontsize=11, color=INK, va="center")
    # Dashed line = postganglionic
    ax.plot([6.2, 7.0], [leg_y, leg_y], color=INK, lw=1.8, linestyle="--")
    ax.text(7.15, leg_y, "Postganglionic fibre", fontsize=11, color=INK, va="center")
    # Ganglion symbol
    ax.plot(10.2, leg_y, "o", color=INK, markersize=6)
    ax.text(10.45, leg_y, "Autonomic ganglion", fontsize=11, color=INK, va="center")

    save(fig, out)
