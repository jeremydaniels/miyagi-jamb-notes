from style import *
import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(14, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Header / Context
    ax.text(7.0, 7.0, "Third Republic Political Parties (Nigeria, 1989–1993)",
            ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Panels
    # Left Panel: SDP
    sdp_box = patches.FancyBboxPatch((0.8, 0.8), 5.8, 5.8, boxstyle="round,pad=0.2",
                                     fc="white", ec=GREY, lw=2)
    ax.add_patch(sdp_box)

    # Right Panel: NRC
    nrc_box = patches.FancyBboxPatch((7.4, 0.8), 5.8, 5.8, boxstyle="round,pad=0.2",
                                     fc="white", ec=GREY, lw=2)
    ax.add_patch(nrc_box)

    # Left content: SDP Horse Emblem circular badge
    sdp_circle = patches.Circle((3.7, 4.3), 1.9, fc=CREAM, ec=DEEP["green"], lw=3)
    ax.add_patch(sdp_circle)

    # Stylized rearing horse outline / silhouette for SDP
    # Path for a simplified heraldic/rampant horse
    horse_verts = [
        (3.0, 3.2),  # hind hoof
        (3.2, 3.7),  # hock
        (3.1, 4.2),  # rump / flank
        (2.7, 4.1),  # tail base
        (2.3, 3.6),  # tail tip
        (2.6, 4.3),  # tail arch
        (3.3, 4.7),  # croup / back
        (3.5, 5.0),  # withers
        (3.7, 5.5),  # crest / neck
        (3.6, 5.7),  # ears
        (4.0, 5.6),  # forehead
        (4.4, 5.3),  # muzzle
        (4.2, 5.0),  # jaw / chin
        (3.9, 4.8),  # throat
        (4.1, 4.4),  # chest
        (4.7, 4.8),  # raised foreleg 1 knee
        (5.0, 5.1),  # raised foreleg 1 hoof
        (4.8, 4.7),
        (4.3, 4.2),  # shoulder
        (4.8, 4.3),  # foreleg 2 knee
        (4.9, 4.1),  # foreleg 2 hoof
        (4.4, 3.9),  # lower chest
        (3.8, 3.8),  # belly
        (3.6, 3.3),  # hindleg 2
        (3.4, 3.1),  # ground hindleg
        (3.0, 3.2)   # close
    ]
    horse_codes = [Path.MOVETO] + [Path.LINETO] * (len(horse_verts) - 2) + [Path.CLOSEPOLY]
    horse_path = Path(horse_verts, horse_codes)
    horse_patch = patches.PathPatch(horse_path, fc=DEEP["green"], ec=DEEP["green"], lw=1.5)
    ax.add_patch(horse_patch)

    # Right content: NRC Eagle Emblem circular badge
    nrc_circle = patches.Circle((10.3, 4.3), 1.9, fc=CREAM, ec=DEEP["green"], lw=3)
    ax.add_patch(nrc_circle)

    # Stylized eagle with spread wings for NRC
    eagle_verts = [
        (10.3, 5.6),  # eagle head top
        (10.6, 5.5),  # beak curve
        (10.7, 5.3),  # beak tip
        (10.5, 5.25), # beak base
        (10.5, 5.0),  # neck right
        (11.2, 5.5),  # right wing top
        (11.9, 5.7),  # right wing tip primary
        (11.7, 5.1),  # primary feather 2
        (11.5, 4.7),  # secondary feather
        (11.2, 4.3),  # wing base right
        (10.8, 4.1),  # right thigh
        (10.9, 3.4),  # right talon
        (10.6, 3.5),
        (10.7, 3.0),  # tail right
        (10.3, 2.8),  # tail center
        (9.9, 3.0),   # tail left
        (10.0, 3.5),
        (9.7, 3.4),   # left talon
        (9.8, 4.1),   # left thigh
        (9.4, 4.3),   # wing base left
        (9.1, 4.7),   # secondary feather left
        (8.9, 5.1),   # primary feather 2 left
        (8.7, 5.7),   # left wing tip primary
        (9.4, 5.5),   # left wing top
        (10.1, 5.0),  # neck left
        (10.1, 5.5),  # head left
        (10.3, 5.6)   # close
    ]
    eagle_codes = [Path.MOVETO] + [Path.LINETO] * (len(eagle_verts) - 2) + [Path.CLOSEPOLY]
    eagle_path = Path(eagle_verts, eagle_codes)
    eagle_patch = patches.PathPatch(eagle_path, fc=DEEP["green"], ec=DEEP["green"], lw=1.5)
    ax.add_patch(eagle_patch)

    # Text descriptions strictly as requested
    # Left party texts
    ax.text(3.7, 1.9, "Social Democratic Party (SDP)",
            ha="center", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(3.7, 1.35, "“A little to the left”",
            ha="center", va="center", fontsize=14, style="italic", color=DEEP["green"])

    # Right party texts
    ax.text(10.3, 1.9, "National Republican Convention (NRC)",
            ha="center", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(10.3, 1.35, "“A little to the right”",
            ha="center", va="center", fontsize=14, style="italic", color=DEEP["green"])

    save(fig, out)
