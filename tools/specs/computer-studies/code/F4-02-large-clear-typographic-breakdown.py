from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 6)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.3, "Structure of an E-mail Address", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # Main email address components display
    # Position: around y = 3.2
    # "xyz" in PINK/DEEP['pink'], "@" in ORANGE/DEEP['orange'], "jamb.org.ng" in BLUE/DEEP['blue']
    
    # Render three visually distinct boxes/blocks for the components
    # 1. "xyz"
    box_xyz = patches.FancyBboxPatch((1.0, 2.7), 1.8, 1.1,
                                     boxstyle="round,pad=0.1,rounding_size=0.15",
                                     linewidth=2, edgecolor=DEEP['pink'],
                                     facecolor=PINK)
    ax.add_patch(box_xyz)
    ax.text(1.9, 3.25, "xyz", ha="center", va="center",
            fontsize=26, fontweight="bold", color=INK, fontfamily="monospace")

    # 2. "@"
    box_at = patches.FancyBboxPatch((3.2, 2.7), 1.0, 1.1,
                                    boxstyle="round,pad=0.1,rounding_size=0.15",
                                    linewidth=2, edgecolor=DEEP['orange'],
                                    facecolor=ORANGE)
    ax.add_patch(box_at)
    ax.text(3.7, 3.25, "@", ha="center", va="center",
            fontsize=26, fontweight="bold", color=INK, fontfamily="monospace")

    # 3. "jamb.org.ng"
    box_domain = patches.FancyBboxPatch((4.6, 2.7), 4.4, 1.1,
                                        boxstyle="round,pad=0.1,rounding_size=0.15",
                                        linewidth=2, edgecolor=DEEP['blue'],
                                        facecolor=BLUE)
    ax.add_patch(box_domain)
    ax.text(6.8, 3.25, "jamb.org.ng", ha="center", va="center",
            fontsize=26, fontweight="bold", color=INK, fontfamily="monospace")

    # Arrows and Labels
    # Label 1: "xyz" -> Username / Local part
    # Put label below on the left
    ax.annotate("Username / Local part",
                xy=(1.9, 2.7), xytext=(1.9, 1.2),
                ha="center", va="top", fontsize=15, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=2.2, shrinkA=5, shrinkB=5),
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP['pink'], lw=1.5))

    # Label 2: "@" -> 'At' symbol, separates user from domain
    # Put label above
    ax.annotate("'At' symbol\n(separates user from domain)",
                xy=(3.7, 3.8), xytext=(3.7, 4.5),
                ha="center", va="bottom", fontsize=14, color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=2.2, shrinkA=5, shrinkB=5),
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP['orange'], lw=1.5))

    # Label 3: "jamb.org.ng" -> Domain name
    # Put label below on the right
    ax.annotate("Domain name",
                xy=(6.8, 2.7), xytext=(6.8, 1.2),
                ha="center", va="top", fontsize=15, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2.2, shrinkA=5, shrinkB=5),
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=DEEP['blue'], lw=1.5))

    save(fig, out)
