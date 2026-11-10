from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 14.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14.5)
    ax.axis("off")

    # Overall diagram title
    ax.text(6, 14.0, "Blood Clotting Cascade", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK)

    # ==================== TOP PANEL: CUT BLOOD VESSEL ====================
    # Section header
    ax.text(6, 13.4, "1. Vessel Injury and Platelet Plug", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=DEEP["blue"])

    # Upper vessel wall (pink border, broken in middle: gap 4.5 to 6.8)
    rect_u1 = patches.Rectangle((1.5, 12.0), 3.0, 0.35, fc=PINK, ec=DEEP["pink"], lw=2)
    rect_u2 = patches.Rectangle((6.8, 12.0), 3.7, 0.35, fc=PINK, ec=DEEP["pink"], lw=2)
    # Lower vessel wall (continuous)
    rect_lower = patches.Rectangle((1.5, 10.7), 9.0, 0.35, fc=PINK, ec=DEEP["pink"], lw=2)

    ax.add_patch(rect_u1)
    ax.add_patch(rect_u2)
    ax.add_patch(rect_lower)

    # Vessel lumen background
    vessel_bg = patches.Rectangle((1.5, 11.05), 9.0, 0.95, fc=CREAM, ec="none", alpha=0.55)
    ax.add_patch(vessel_bg)

    # Red blood cells escaping through the cut and within vessel
    rbc_coords = [
        (2.3, 11.5), (3.1, 11.2), (3.9, 11.6), (2.8, 11.2),
        (5.0, 11.4), (5.9, 11.6), (5.3, 12.3), (6.1, 12.5), (4.8, 12.6),
        (7.5, 11.3), (8.4, 11.5), (9.3, 11.2), (8.2, 11.2)
    ]
    for (rx, ry) in rbc_coords:
        rbc = patches.Ellipse((rx, ry), 0.52, 0.30,
                              angle=np.random.RandomState(int(rx * 100)).randint(-25, 25),
                              fc=DEEP["pink"], ec=INK, lw=1.2, zorder=3)
        ax.add_patch(rbc)

    # Platelets adhering to damaged edges (x ~ 4.5 and 6.8) and bridging
    edge_platelets = [
        (4.4, 12.0), (4.6, 12.2), (4.5, 11.8), (4.7, 11.9),
        (6.7, 12.0), (6.9, 12.2), (6.6, 11.8), (6.8, 11.9),
        (5.3, 12.1), (5.8, 12.2), (5.5, 12.0)
    ]
    for (px, py) in edge_platelets:
        plat = patches.Circle((px, py), 0.11, fc=LAV, ec=DEEP["lav"], lw=1.2, zorder=4)
        ax.add_patch(plat)

    # Labels for top panel
    ax.annotate("damaged blood vessel", xy=(4.5, 12.35), xytext=(2.2, 12.75),
                fontsize=11.5, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1))

    ax.annotate("platelets", xy=(4.65, 11.8), xytext=(2.3, 10.25),
                fontsize=11.5, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1))

    # Clean transition arrow between Section 1 and Section 2
    ax.annotate("", xy=(6.0, 9.9), xytext=(6.0, 10.6),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2, mutation_scale=16))

    # ==================== MIDDLE PANEL: CLOTTING CASCADE ====================
    # Section header placed safely between connecting arrows
    ax.text(6, 9.6, "2. Coagulation Cascade", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=DEEP["blue"])

    # Arrow from Section 2 title down into Box 1
    ax.annotate("", xy=(6.0, 8.9), xytext=(6.0, 9.35),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2, mutation_scale=16))

    # Box 1: Damaged tissue and platelets release thromboplastin
    b1 = patches.FancyBboxPatch((1.6, 8.2), 8.8, 0.65, boxstyle="round,pad=0.15",
                                fc=CREAM, ec=DEEP["orange"], lw=2)
    ax.add_patch(b1)
    ax.text(6.0, 8.525, "Damaged tissue and platelets release thromboplastin",
            ha="center", va="center", fontsize=12, fontweight="bold", color=INK)

    # Down arrow from Box 1 with "thromboplastin" label
    ax.annotate("", xy=(6.0, 7.35), xytext=(6.0, 8.15),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2, mutation_scale=16))
    ax.text(6.15, 7.75, "thromboplastin", ha="left", va="center",
            fontsize=11.5, fontweight="bold", color=DEEP["orange"],
            bbox=dict(fc="white", ec="none", pad=1))

    # --- Step: Prothrombin changes to Thrombin ---
    # Prothrombin box (left: x 1.2 to 4.1, width = 2.9)
    bp = patches.FancyBboxPatch((1.2, 6.45), 2.9, 0.70, boxstyle="round,pad=0.15",
                                fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(bp)
    ax.text(2.65, 6.8, "prothrombin", ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=INK)

    # Thrombin box (right: x 7.9 to 10.8, width = 2.9)
    bt = patches.FancyBboxPatch((7.9, 6.45), 2.9, 0.70, boxstyle="round,pad=0.15",
                                fc=LAV, ec=DEEP["lav"], lw=2)
    ax.add_patch(bt)
    ax.text(9.35, 6.8, "thrombin", ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=INK)

    # Conversion arrow from Prothrombin to Thrombin (gap is x=4.1 to 7.9, span = 3.8)
    ax.annotate("", xy=(7.85, 6.8), xytext=(4.15, 6.8),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=18))

    # Helper icon: calcium ions and vitamin K (positioned strictly between boxes at x=4.7 to 7.3)
    helper_box = patches.FancyBboxPatch((4.75, 5.65), 2.5, 0.65, boxstyle="round,pad=0.1",
                                       fc=GREEN, ec=DEEP["green"], lw=1.5)
    ax.add_patch(helper_box)
    ax.text(6.0, 5.975, "calcium ions\n+ vitamin K", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=DEEP["green"])
    # Arrow from helper box pointing to the conversion arrow
    ax.annotate("", xy=(6.0, 6.75), xytext=(6.0, 6.35),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2, mutation_scale=14))

    # --- Step: Fibrinogen changes to Fibrin ---
    # Box Fibrinogen (soluble) (left: x 1.2 to 4.5)
    bfg = patches.FancyBboxPatch((1.2, 4.45), 3.3, 0.75, boxstyle="round,pad=0.15",
                                 fc=BLUE, ec=DEEP["blue"], lw=2)
    ax.add_patch(bfg)
    ax.text(2.85, 4.825, "fibrinogen (soluble)", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=INK)

    # Box Fibrin threads (insoluble) (right: x 7.5 to 11.0)
    bfb = patches.FancyBboxPatch((7.5, 4.45), 3.5, 0.75, boxstyle="round,pad=0.15",
                                 fc=ORANGE, ec=DEEP["orange"], lw=2)
    ax.add_patch(bfb)
    ax.text(9.25, 4.825, "fibrin threads (insoluble)", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=INK)

    # Conversion arrow Fibrinogen -> Fibrin
    ax.annotate("", xy=(7.45, 4.825), xytext=(4.55, 4.825),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.5, mutation_scale=18))

    # Catalytic action arrow from Thrombin down to conversion arrow
    ax.annotate("", xy=(6.0, 4.9), xytext=(8.8, 6.45),
                arrowprops=dict(arrowstyle="->", color=DEEP["lav"], lw=2,
                                connectionstyle="arc3,rad=0.18", mutation_scale=15))
    ax.text(8.1, 5.75, "catalyses", ha="center", va="center",
            fontsize=11, fontstyle="italic", color=DEEP["lav"],
            bbox=dict(fc="white", ec="none", pad=1))

    # Down arrow leading cleanly into Section 3 header area
    ax.annotate("", xy=(6.0, 3.85), xytext=(6.0, 4.35),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.2, mutation_scale=16))

    # ==================== BOTTOM PANEL: FIBRIN MESH & CLOT ====================
    # Section header
    ax.text(6, 3.6, "3. Fibrin Mesh and Clot Formation", ha="center", va="center",
            fontsize=13.5, fontweight="bold", color=DEEP["blue"])

    # Arrow from Section 3 title into the mesh box
    ax.annotate("", xy=(6.0, 2.95), xytext=(6.0, 3.35),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2.0, mutation_scale=14))

    # Outer container for the close-up view (y from 0.4 to 2.9)
    clot_box = patches.FancyBboxPatch((1.5, 0.35), 9.0, 2.55, boxstyle="round,pad=0.15",
                                     fc="#FCFDFD", ec=GREY, lw=1.5)
    ax.add_patch(clot_box)

    # Mesh of fibrin threads
    mesh_lines = [
        (2.0, 1.0, 9.8, 2.4),
        (2.2, 2.3, 9.5, 0.7),
        (2.5, 0.5, 8.8, 2.6),
        (1.8, 1.7, 10.0, 1.4),
        (3.0, 2.7, 7.5, 0.5),
        (4.5, 0.5, 9.2, 2.5),
        (2.8, 2.5, 8.2, 0.6),
        (5.5, 2.7, 10.2, 1.0),
        (1.7, 1.4, 6.5, 2.7),
        (3.8, 0.5, 6.2, 2.7),
        (6.8, 0.5, 9.8, 2.2),
        (2.2, 0.8, 5.8, 2.5)
    ]
    for (x1, y1, x2, y2) in mesh_lines:
        ax.plot([x1, x2], [y1, y2], color=DEEP["orange"], lw=2.0, alpha=0.85, zorder=2)

    # Trapped red blood cells inside the mesh
    trapped_rbcs = [
        (3.2, 1.6), (4.2, 2.0), (4.0, 1.0),
        (5.2, 1.5), (5.0, 2.2), (6.0, 1.1),
        (6.3, 2.1), (7.2, 1.6), (7.0, 2.3),
        (8.1, 1.3), (8.0, 2.0), (5.8, 1.8)
    ]
    for (rx, ry) in trapped_rbcs:
        rbc = patches.Ellipse((rx, ry), 0.56, 0.34,
                              angle=np.random.RandomState(int(rx * 73)).randint(-35, 35),
                              fc=DEEP["pink"], ec=INK, lw=1.3, zorder=3)
        ax.add_patch(rbc)

    # Additional platelets trapped in the clot
    trapped_platelets = [
        (3.6, 1.8), (4.7, 1.3), (5.6, 2.1), (6.7, 1.3), (7.5, 1.9)
    ]
    for (px, py) in trapped_platelets:
        plat = patches.Circle((px, py), 0.11, fc=LAV, ec=DEEP["lav"], lw=1.2, zorder=4)
        ax.add_patch(plat)

    # Annotations inside bottom panel
    ax.annotate("fibrin threads (insoluble)", xy=(3.0, 2.15), xytext=(1.8, 2.65),
                fontsize=11.5, fontweight="bold", color=DEEP["orange"],
                arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1), zorder=5)

    ax.annotate("trapped red blood cells", xy=(6.3, 2.1), xytext=(7.5, 2.65),
                fontsize=11.5, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                bbox=dict(fc="white", ec="none", pad=1), zorder=5)

    # Prominent clot badge
    ax.text(6.0, 0.65, "clot", ha="center", va="center",
            fontsize=15, fontweight="bold", color=DEEP["pink"],
            bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.35", lw=2), zorder=6)

    save(fig, out)
