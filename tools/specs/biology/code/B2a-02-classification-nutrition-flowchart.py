import sys
sys.path.insert(0, '/home/user/miyagi-jamb-notes/tools/codedraw')
from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(15, 10.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10.5)
    ax.axis('off')

    c_top = CREAM
    ec_top = GREY
    c_auto = GREEN
    ec_auto = DEEP["green"]
    c_hetero = ORANGE
    ec_hetero = DEEP["orange"]
    c_carn = LAV
    ec_carn = DEEP["lav"]

    def draw_box(x, y, w, h, text, title="", fc=CREAM, ec=GREY, title_color=INK, body_color=INK, lw=1.5):
        box = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                    boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
        ax.add_patch(box)
        if title and text:
            ax.text(x, y + h*0.18, title, ha='center', va='center', fontsize=12, fontweight='bold', color=title_color, zorder=4)
            ax.text(x, y - h*0.2, text, ha='center', va='center', fontsize=11, color=body_color, zorder=4)
        elif title:
            ax.text(x, y, title, ha='center', va='center', fontsize=13, fontweight='bold', color=title_color, zorder=4)
        else:
            ax.text(x, y, text, ha='center', va='center', fontsize=11.5, color=body_color, zorder=4)

    # Top Box: Nutrition
    draw_box(7.5, 9.7, 3.2, 0.8, "", title="Nutrition", fc=CREAM, ec=ec_top, title_color=INK, lw=2)

    # Main branches
    auto_x, auto_y = 3.5, 8.3
    hetero_x, hetero_y = 11.5, 8.3
    draw_box(auto_x, auto_y, 3.4, 0.9, "", title="Autotrophic", fc=c_auto, ec=ec_auto, title_color=DEEP["green"], lw=2)
    draw_box(hetero_x, hetero_y, 3.8, 0.9, "", title="Heterotrophic", fc=c_hetero, ec=ec_hetero, title_color=DEEP["orange"], lw=2)

    # Top connectors
    ax.plot([7.5, 7.5], [9.3, 8.9], color=INK, lw=1.8, zorder=1)
    ax.plot([auto_x, hetero_x], [8.9, 8.9], color=INK, lw=1.8, zorder=1)
    ax.plot([auto_x, auto_x], [8.9, 8.75], color=INK, lw=1.8, zorder=1)
    ax.plot([hetero_x, hetero_x], [8.9, 8.75], color=INK, lw=1.8, zorder=1)

    # Autotrophic children
    auto_sub_y = [6.7, 5.1]
    auto_w, auto_h = 5.2, 1.0
    draw_box(auto_x, auto_sub_y[0], auto_w, auto_h, "(green plants, algae)", title="Photosynthetic", fc="white", ec=ec_auto, title_color=DEEP["green"])
    draw_box(auto_x, auto_sub_y[1], auto_w, auto_h, "(nitrifying bacteria)", title="Chemosynthetic", fc="white", ec=ec_auto, title_color=DEEP["green"])
    
    # Auto tree lines
    ax.plot([auto_x, auto_x], [7.85, 7.2], color=ec_auto, lw=1.8, zorder=1)
    ax.plot([auto_x, auto_x], [6.2, 5.6], color=ec_auto, lw=1.8, zorder=1)

    # Heterotrophic children
    hetero_sub_y = [6.8, 5.3, 3.8, 2.3]
    hetero_w, hetero_h = 5.6, 1.0
    draw_box(hetero_x, hetero_sub_y[0], hetero_w, hetero_h, "(sheep, man)", title="Holozoic", fc="white", ec=ec_hetero, title_color=DEEP["orange"])
    draw_box(hetero_x, hetero_sub_y[1], hetero_w, hetero_h, "(roundworm, tapeworm, Loranthus)", title="Parasitic", fc="white", ec=ec_hetero, title_color=DEEP["orange"])
    draw_box(hetero_x, hetero_sub_y[2], hetero_w, hetero_h, "(Rhizopus, mushroom)", title="Saprophytic", fc="white", ec=ec_hetero, title_color=DEEP["orange"])
    draw_box(hetero_x, hetero_sub_y[3], hetero_w, hetero_h, "(Rhizobium and legumes, lichens)", title="Symbiotic", fc="white", ec=ec_hetero, title_color=DEEP["orange"])

    # Hetero tree lines
    ax.plot([hetero_x, hetero_x], [7.85, 7.3], color=ec_hetero, lw=1.8, zorder=1)
    ax.plot([hetero_x, hetero_x], [6.3, 5.8], color=ec_hetero, lw=1.8, zorder=1)
    ax.plot([hetero_x, hetero_x], [4.8, 4.3], color=ec_hetero, lw=1.8, zorder=1)
    ax.plot([hetero_x, hetero_x], [3.3, 2.8], color=ec_hetero, lw=1.8, zorder=1)

    # Carnivorous plants side box (moved down to avoid overlap)
    carn_x, carn_y = 3.5, 2.8
    carn_w, carn_h = 5.2, 1.3
    box_carn = patches.FancyBboxPatch((carn_x - carn_w/2, carn_y - carn_h/2), carn_w, carn_h,
                                     boxstyle="round,pad=0.1,rounding_size=0.2",
                                     facecolor=c_carn, edgecolor=ec_carn, linewidth=1.8, linestyle="--", zorder=3)
    ax.add_patch(box_carn)
    ax.text(carn_x, carn_y + 0.3, "Carnivorous plants", ha='center', va='center', fontsize=12, fontweight='bold', color=DEEP["lav"], zorder=4)
    ax.text(carn_x, carn_y, "(sundew, bladderwort):", ha='center', va='center', fontsize=11, color=INK, zorder=4)
    ax.text(carn_x, carn_y - 0.3, "photosynthesise and digest insects", ha='center', va='center', fontsize=10.5, style='italic', color=INK, zorder=4)

    # Dotted connections to both main branches
    ax.plot([auto_x, auto_x], [4.6, carn_y + carn_h/2], color=DEEP["lav"], lw=1.8, linestyle=":", zorder=1)
    ax.plot([carn_x + carn_w/2, 8.5], [carn_y, carn_y], color=DEEP["lav"], lw=1.8, linestyle=":", zorder=1)
    ax.plot([8.5, 8.5], [carn_y, 7.85], color=DEEP["lav"], lw=1.8, linestyle=":", zorder=1)
    ax.plot([8.5, hetero_x - hetero_w/2], [7.85, 7.85], color=DEEP["lav"], lw=1.8, linestyle=":", zorder=1)


    # Icons
    # Photosynthetic
    ix, iy = auto_x - auto_w/2 + 0.5, auto_sub_y[0]
    leaf = patches.Ellipse((ix, iy), 0.38, 0.22, angle=35, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2, zorder=5)
    ax.add_patch(leaf)
    ax.plot([ix - 0.15, ix + 0.15], [iy - 0.1, iy + 0.1], color=DEEP["green"], lw=1, zorder=5)

    # Chemosynthetic
    ix, iy = auto_x - auto_w/2 + 0.5, auto_sub_y[1]
    bac = patches.FancyBboxPatch((ix - 0.2, iy - 0.08), 0.4, 0.16, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor=CREAM, edgecolor=DEEP["green"], lw=1.2, zorder=5)
    ax.add_patch(bac)
    ax.plot([ix + 0.22, ix + 0.32, ix + 0.38], [iy, iy + 0.06, iy], color=DEEP["green"], lw=1, zorder=5)

    # Holozoic
    ix, iy = hetero_x - hetero_w/2 + 0.5, hetero_sub_y[0]
    ax.add_patch(patches.Ellipse((ix, iy - 0.05), 0.35, 0.24, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.2, zorder=5))
    ax.add_patch(patches.Circle((ix + 0.18, iy + 0.08), 0.1, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.2, zorder=5))
    ax.plot([ix - 0.1, ix - 0.1], [iy - 0.17, iy - 0.28], color=DEEP["orange"], lw=1.2, zorder=5)
    ax.plot([ix + 0.1, ix + 0.1], [iy - 0.17, iy - 0.28], color=DEEP["orange"], lw=1.2, zorder=5)

    # Parasitic
    ix, iy = hetero_x - hetero_w/2 + 0.5, hetero_sub_y[1]
    wx = np.linspace(ix - 0.25, ix + 0.25, 30)
    wy = iy + 0.1 * np.sin(np.linspace(0, 3*np.pi, 30))
    ax.plot(wx, wy, color=DEEP["orange"], lw=2, zorder=5)

    # Saprophytic
    ix, iy = hetero_x - hetero_w/2 + 0.5, hetero_sub_y[2]
    ax.add_patch(patches.Rectangle((ix - 0.05, iy - 0.22), 0.1, 0.18, facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.2, zorder=5))
    ax.add_patch(patches.Wedge((ix, iy - 0.06), 0.22, 0, 180, facecolor=PINK, edgecolor=DEEP["orange"], lw=1.2, zorder=5))

    # Symbiotic
    ix, iy = hetero_x - hetero_w/2 + 0.5, hetero_sub_y[3]
    ax.add_patch(patches.Circle((ix - 0.09, iy), 0.15, fill=False, edgecolor=DEEP["orange"], lw=1.5, zorder=5))
    ax.add_patch(patches.Circle((ix + 0.09, iy), 0.15, fill=False, edgecolor=DEEP["green"], lw=1.5, zorder=5))

    # Carnivorous
    ix, iy = carn_x - carn_w/2 + 0.45, carn_y
    ax.add_patch(patches.Ellipse((ix, iy - 0.05), 0.18, 0.32, facecolor=PINK, edgecolor=DEEP["lav"], lw=1.2, zorder=5))
    ax.plot([ix - 0.15, ix, ix + 0.15], [iy + 0.16, iy + 0.22, iy + 0.16], color=DEEP["lav"], lw=1.2, zorder=5)

    save(fig, out)

if __name__ == '__main__':
    draw(sys.argv[1])
