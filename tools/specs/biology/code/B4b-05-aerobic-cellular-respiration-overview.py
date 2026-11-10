import numpy as np
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Title / Header
    ax.text(7, 8.7, "Aerobic Respiration Overview", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # 1. Cytoplasm container (left side)
    cyto_box = patches.FancyBboxPatch((0.5, 1.5), 4.2, 6.6,
                                      boxstyle="round,pad=0.2,rounding_size=0.4",
                                      facecolor=CREAM, edgecolor=GREY, lw=2)
    ax.add_patch(cyto_box)
    ax.text(2.6, 7.8, "Cytoplasm", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    # 2. Mitochondrion container (right side)
    mito_outer = patches.FancyBboxPatch((5.1, 1.5), 8.4, 6.6,
                                        boxstyle="round,pad=0.3,rounding_size=0.8",
                                        facecolor=LAV, edgecolor=DEEP["lav"], lw=2.5)
    ax.add_patch(mito_outer)
    ax.text(9.3, 7.8, "Mitochondrion", ha="center", va="center",
            fontsize=16, fontweight="bold", color=DEEP["lav"])

    # Inside Mitochondrion: Matrix area
    matrix_box = patches.FancyBboxPatch((5.4, 1.8), 4.7, 5.6,
                                        boxstyle="round,pad=0.2,rounding_size=0.5",
                                        facecolor="white", edgecolor=GREY, lw=1.5, ls="--")
    ax.add_patch(matrix_box)

    # Inside Mitochondrion: Cristae / ETC area
    etc_box = patches.FancyBboxPatch((10.4, 1.8), 2.8, 5.6,
                                     boxstyle="round,pad=0.2,rounding_size=0.5",
                                     facecolor="white", edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(etc_box)

    # --- GLYCOLYSIS (Cytoplasm) ---
    # Glucose input
    ax.text(2.6, 7.0, "glucose", ha="center", va="center", fontsize=15, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.8))
    
    # Arrow glucose -> glycolysis
    ax.annotate("", xy=(2.6, 6.15), xytext=(2.6, 6.65),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    # Glycolysis process box
    ax.text(2.6, 5.7, "glycolysis (cytoplasm)", ha="center", va="center", fontsize=14, fontweight="bold",
            bbox=dict(boxstyle="square,pad=0.4", fc=BLUE, ec=DEEP["blue"], lw=1.5))

    # Outputs of glycolysis: ATP & NADH
    # ATP out left
    ax.annotate("", xy=(0.8, 5.2), xytext=(1.6, 5.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.8))
    ax.text(0.8, 4.9, "2 ATP", ha="center", va="center", fontsize=14, fontweight="bold",
            color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["orange"], lw=1.5))

    # 2 pyruvic acid box
    ax.annotate("", xy=(2.6, 4.45), xytext=(2.6, 5.25),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))
    ax.text(2.6, 4.1, "2 pyruvic acid", ha="center", va="center", fontsize=15, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=INK, lw=1.8))

    # Arrow to mitochondrial link reaction
    ax.annotate("", xy=(6.0, 6.2), xytext=(3.7, 4.1),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.1", color=INK, lw=2.2))

    # --- LINK REACTION (Mitochondrial Matrix) ---
    ax.text(6.8, 6.3, "link reaction", ha="center", va="center", fontsize=14, fontweight="bold",
            bbox=dict(boxstyle="square,pad=0.35", fc=GREEN, ec=DEEP["green"], lw=1.5))
    
    # Link reaction releases CO2
    ax.annotate("", xy=(6.8, 7.3), xytext=(6.8, 6.7),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.text(6.8, 7.4, "carbon dioxide out", ha="center", va="bottom", fontsize=14,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1))

    # Link reaction arrow to acetyl CoA
    ax.annotate("", xy=(6.8, 5.5), xytext=(6.8, 5.9),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))
    ax.text(6.8, 5.2, "acetyl CoA", ha="center", va="center", fontsize=15, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=INK, lw=1.8))

    # Arrow from acetyl CoA into Krebs cycle
    ax.annotate("", xy=(6.8, 4.2), xytext=(6.8, 4.9),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    # --- KREBS CYCLE (Matrix) ---
    krebs_circle = patches.Circle((6.8, 3.2), 0.9, facecolor=PINK, edgecolor=DEEP["pink"], lw=2)
    ax.add_patch(krebs_circle)
    ax.text(6.8, 3.2, "Krebs cycle\n(matrix)", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    # Krebs outputs: CO2 out
    ax.annotate("", xy=(5.6, 2.3), xytext=(6.1, 2.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.text(5.5, 2.1, "carbon dioxide out", ha="center", va="top", fontsize=14,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=GREY, lw=1))

    # Krebs outputs: 2 ATP
    ax.annotate("", xy=(7.8, 2.2), xytext=(7.3, 2.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.8))
    ax.text(8.0, 2.1, "2 ATP", ha="center", va="top", fontsize=14, fontweight="bold",
            color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=DEEP["orange"], lw=1.5))

    # Krebs / Glycolysis outputs: NADH and FADH2 flowing to ETC
    ax.text(9.1, 4.4, "NADH and FADH₂", ha="center", va="center", fontsize=14, fontweight="bold",
            color=DEEP["blue"], bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["blue"], lw=1.5))

    # Arrows feeding into NADH/FADH2 from Cytoplasm & Krebs
    # From Krebs to NADH label
    ax.annotate("", xy=(8.2, 4.2), xytext=(7.6, 3.7),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))
    # From Cytoplasm glycolysis (NADH) over to ETC via curved arrow passing below acetyl CoA
    ax.annotate("", xy=(8.2, 4.5), xytext=(3.4, 5.6),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.3",
                                color=DEEP["blue"], lw=2, ls="--"))
    # From NADH/FADH2 label into ETC
    ax.annotate("", xy=(10.4, 4.4), xytext=(10.0, 4.4),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2.2))

    # --- ELECTRON TRANSPORT CHAIN (Cristae) ---
    ax.text(11.8, 6.0, "electron transport chain\n(cristae)", ha="center", va="center",
            fontsize=14, fontweight="bold", color=INK)

    # Oxygen in
    ax.text(11.8, 7.1, "oxygen in", ha="center", va="center", fontsize=14, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["blue"], lw=1.5))
    ax.annotate("", xy=(11.8, 6.5), xytext=(11.8, 6.85),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))

    # Water out
    ax.annotate("", xy=(11.8, 3.0), xytext=(11.8, 3.5),
                arrowprops=dict(arrowstyle="->", color=DEEP["blue"], lw=2))
    ax.text(11.8, 2.7, "water out", ha="center", va="center", fontsize=14, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=DEEP["blue"], lw=1.5))

    # 34 ATP produced from ETC
    ax.annotate("", xy=(12.8, 4.6), xytext=(12.2, 5.0),
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2))
    ax.text(12.7, 4.2, "34 ATP", ha="center", va="center", fontsize=15, fontweight="bold",
            color=DEEP["orange"], bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["orange"], lw=2))

    # --- TOTAL BOX AT BOTTOM ---
    total_box = patches.FancyBboxPatch((3.5, 0.2), 7.0, 0.9,
                                       boxstyle="round,pad=0.15,rounding_size=0.3",
                                       facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(total_box)
    ax.text(7.0, 0.65, "total: 38 ATP (traditional figure)", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)

    save(fig, out)
