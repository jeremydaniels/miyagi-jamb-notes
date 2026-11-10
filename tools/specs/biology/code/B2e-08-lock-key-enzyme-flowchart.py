from style import *
import numpy as np
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(15, 6)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6)
    ax.axis('off')

    def get_enzyme_path(cx, cy):
        verts = [
            (cx - 0.9, cy + 0.6),
            (cx - 0.45, cy + 0.6),
            (cx - 0.35, cy + 0.1),
            (cx + 0.35, cy + 0.1),
            (cx + 0.45, cy + 0.6),
            (cx + 0.9, cy + 0.6),
            (cx + 0.9, cy - 0.6),
            (cx - 0.9, cy - 0.6),
            (cx - 0.9, cy + 0.6),
        ]
        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]
        return Path(verts, codes)

    def get_substrate_path(cx, cy_offset):
        verts = [
            (cx - 0.42, 2.0 + cy_offset + 0.48),
            (cx + 0.42, 2.0 + cy_offset + 0.48),
            (cx + 0.33, 2.0 + cy_offset + 0.03),
            (cx - 0.33, 2.0 + cy_offset + 0.03),
            (cx - 0.42, 2.0 + cy_offset + 0.48),
        ]
        codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        return Path(verts, codes)

    def get_product1_path(cx, cy_offset):
        verts = [
            (cx - 0.42, 2.0 + cy_offset + 0.48),
            (cx - 0.05, 2.0 + cy_offset + 0.48),
            (cx - 0.05, 2.0 + cy_offset + 0.03),
            (cx - 0.33, 2.0 + cy_offset + 0.03),
            (cx - 0.42, 2.0 + cy_offset + 0.48),
        ]
        codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        return Path(verts, codes)

    def get_product2_path(cx, cy_offset):
        verts = [
            (cx + 0.05, 2.0 + cy_offset + 0.48),
            (cx + 0.42, 2.0 + cy_offset + 0.48),
            (cx + 0.33, 2.0 + cy_offset + 0.03),
            (cx + 0.05, 2.0 + cy_offset + 0.03),
            (cx + 0.05, 2.0 + cy_offset + 0.48),
        ]
        codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        return Path(verts, codes)

    def get_denatured_path(cx, cy):
        verts = [
            (cx - 0.85, cy + 0.55),
            (cx - 0.45, cy + 0.55),
            (cx - 0.2, cy + 0.3),
            (cx - 0.1, cy + 0.4),
            (cx + 0.1, cy + 0.2),
            (cx + 0.3, cy + 0.5),
            (cx + 0.85, cy + 0.55),
            (cx + 0.75, cy - 0.6),
            (cx - 0.8, cy - 0.55),
            (cx - 0.85, cy + 0.55),
        ]
        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]
        return Path(verts, codes)

    xs = [1.5, 4.3, 7.1, 9.9]
    ey = 2.0  

    p_enz1 = patches.PathPatch(get_enzyme_path(xs[0], ey), facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    p_sub1 = patches.PathPatch(get_substrate_path(xs[0], 1.2), facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(p_enz1)
    ax.add_patch(p_sub1)

    ax.annotate("", xy=(xs[0], 2.85), xytext=(xs[0], 3.15),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    p_enz2 = patches.PathPatch(get_enzyme_path(xs[1], ey), facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    p_sub2 = patches.PathPatch(get_substrate_path(xs[1], 0.07), facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(p_enz2)
    ax.add_patch(p_sub2)

    p_enz3 = patches.PathPatch(get_enzyme_path(xs[2], ey), facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    p_pr1_s3 = patches.PathPatch(get_product1_path(xs[2], 0.07), facecolor=PINK, edgecolor=DEEP["pink"], lw=2)
    p_pr2_s3 = patches.PathPatch(get_product2_path(xs[2], 0.07), facecolor=GREEN, edgecolor=DEEP["green"], lw=2)
    ax.add_patch(p_enz3)
    ax.add_patch(p_pr1_s3)
    ax.add_patch(p_pr2_s3)

    p_enz4 = patches.PathPatch(get_enzyme_path(xs[3], ey), facecolor=BLUE, edgecolor=DEEP["blue"], lw=2.2)
    p_pr1_s4 = patches.PathPatch(get_product1_path(xs[3] - 0.25, 1.25), facecolor=PINK, edgecolor=DEEP["pink"], lw=2)
    p_pr2_s4 = patches.PathPatch(get_product2_path(xs[3] + 0.25, 1.35), facecolor=GREEN, edgecolor=DEEP["green"], lw=2)
    ax.add_patch(p_enz4)
    ax.add_patch(p_pr1_s4)
    ax.add_patch(p_pr2_s4)

    ax.annotate("", xy=(xs[3] - 0.45, 3.8), xytext=(xs[3] - 0.25, 3.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.annotate("", xy=(xs[3] + 0.45, 3.9), xytext=(xs[3] + 0.25, 3.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    for i in range(3):
        x_start = xs[i] + 1.15
        x_end = xs[i+1] - 1.15
        ax.annotate("", xy=(x_end, ey), xytext=(x_start, ey),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=2.2))

    ax.annotate("substrate", xy=(xs[0], 3.4), xytext=(xs[0], 4.2),
                fontsize=13, color=INK, ha="center", weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    ax.annotate("active site", xy=(xs[0] + 0.2, 2.15), xytext=(xs[0] + 0.9, 3.2),
                fontsize=12, color=INK, ha="center",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    ax.text(xs[0], 1.2, "enzyme", fontsize=13, color=INK, ha="center", va="top", weight="bold")

    ax.text(xs[1], 1.2, "enzyme-substrate\ncomplex", fontsize=13, color=INK, ha="center", va="top", weight="bold")

    ax.text(xs[2], 1.2, "substrate split\ninto products", fontsize=12, color=INK, ha="center", va="top")

    ax.annotate("products", xy=(xs[3], 3.55), xytext=(xs[3], 4.3),
                fontsize=13, color=INK, ha="center", weight="bold",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(fc="white", ec="none", pad=1))

    ax.text(xs[3], 1.2, "enzyme unchanged", fontsize=13, color=INK, ha="center", va="top", weight="bold")

    ax.axvline(11.4, ymin=0.08, ymax=0.92, color=GREY, lw=1.5, ls="--")

    x5 = 13.2
    p_den = patches.PathPatch(get_denatured_path(x5, ey), facecolor=LAV, edgecolor=DEEP["lav"], lw=2.2)
    p_sub5 = patches.PathPatch(get_substrate_path(x5, 1.2), facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(p_den)
    ax.add_patch(p_sub5)

    ax.annotate("", xy=(x5, 2.7), xytext=(x5, 3.1),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.8, ls="--"))
    ax.text(x5 + 0.5, 2.9, "does not\nfit", fontsize=11, color=DEEP["pink"], ha="left", va="center", weight="bold")

    ax.text(x5, 1.2, "denatured enzyme\n(active site changed)", fontsize=12, color=INK, ha="center", va="top", weight="bold")

    ax.text(5.7, 5.4, "Lock-and-Key Model of Enzyme Action", fontsize=16, color=INK, ha="center", weight="bold")
    ax.text(13.2, 5.4, "Denaturation", fontsize=14, color=INK, ha="center", weight="bold")

    save(fig, out)
