from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Colors
    c_oxy = DEEP["pink"]      # Red/oxygenated
    c_deoxy = DEEP["blue"]    # Blue/deoxygenated
    bg_heart = CREAM
    bg_organ = LAV

    # Helper for boxes
    def draw_organ(cx, cy, w, h, label, bg=bg_organ):
        rect = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                      boxstyle="round,pad=0.15",
                                      facecolor=bg, edgecolor=INK, lw=2)
        ax.add_patch(rect)
        ax.text(cx, cy, label, ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

    # Helper for arrows
    def draw_arrow(start, end, color):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=3.5, mutation_scale=20))

    # ==========================================
    # LEFT: FISH SINGLE CIRCULATION
    # ==========================================
    # Centers:
    # Gills: (3.5, 7.5)
    # Body:  (3.5, 1.5)
    # Heart: (3.5, 4.5) -> Atrium at (3.5, 3.8), Ventricle at (3.5, 5.0)

    # Title
    ax.text(3.5, 8.5, "fish: single circulation", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    # Organs
    draw_organ(3.5, 7.2, 2.4, 0.9, "gills")
    draw_organ(3.5, 1.2, 2.4, 0.9, "body")

    # Heart outline container
    heart_left_rect = patches.FancyBboxPatch((2.2, 3.1), 2.6, 2.6,
                                             boxstyle="round,pad=0.2",
                                             facecolor="white", edgecolor=GREY, lw=2, linestyle="--")
    ax.add_patch(heart_left_rect)
    ax.text(1.8, 4.4, "heart", ha="right", va="center", fontsize=15, fontweight="bold", color=INK)

    # Chambers
    draw_organ(3.5, 3.7, 2.0, 0.75, "atrium", bg=bg_heart)
    draw_organ(3.5, 5.1, 2.0, 0.75, "ventricle", bg=bg_heart)

    # Connecting heart internally
    draw_arrow((3.5, 4.075), (3.5, 4.725), c_deoxy)

    # Loop pathways:
    # Ventricle to Gills (Deoxygenated - Blue)
    draw_arrow((3.5, 5.475), (3.5, 6.75), c_deoxy)

    # Gills to Body (Oxygenated - Red): down right side
    ax.plot([4.7, 5.7, 5.7, 4.7], [7.2, 7.2, 1.2, 1.2], color=c_oxy, lw=3.5)
    draw_arrow((5.7, 4.5), (5.7, 4.0), c_oxy)

    # Body to Atrium (Deoxygenated - Blue): up left side
    ax.plot([2.3, 1.3, 1.3, 2.5], [1.2, 1.2, 3.7, 3.7], color=c_deoxy, lw=3.5)
    draw_arrow((1.3, 2.2), (1.3, 2.8), c_deoxy)

    # ==========================================
    # RIGHT: MAMMAL DOUBLE CIRCULATION
    # ==========================================
    # Centers:
    # Lungs: (10.5, 7.2)
    # Body:  (10.5, 1.2)
    # Heart center: (10.5, 4.4)

    # Title
    ax.text(10.5, 8.5, "mammal: double circulation", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)

    # Organs
    draw_organ(10.5, 7.2, 2.4, 0.9, "lungs")
    draw_organ(10.5, 1.2, 2.4, 0.9, "body")

    # Heart outline container
    heart_right_rect = patches.FancyBboxPatch((8.7, 3.1), 3.6, 2.6,
                                              boxstyle="round,pad=0.2",
                                              facecolor="white", edgecolor=GREY, lw=2, linestyle="--")
    ax.add_patch(heart_right_rect)
    ax.text(12.7, 4.4, "heart", ha="left", va="center", fontsize=15, fontweight="bold", color=INK)

    # Chambers:
    # Right side of animal (anatomical right = diagram left): Right Atrium, Right Ventricle
    # Left side of animal (anatomical left = diagram right): Left Atrium, Left Ventricle
    draw_organ(9.6, 4.9, 1.4, 0.75, "atrium", bg=bg_heart)      # RA
    draw_organ(9.6, 3.7, 1.4, 0.75, "ventricle", bg=bg_heart)   # RV
    draw_organ(11.4, 4.9, 1.4, 0.75, "atrium", bg=bg_heart)     # LA
    draw_organ(11.4, 3.7, 1.4, 0.75, "ventricle", bg=bg_heart)  # LV

    # Inside heart:
    # RA -> RV (blue)
    draw_arrow((9.6, 4.525), (9.6, 4.075), c_deoxy)
    # LA -> LV (red)
    draw_arrow((11.4, 4.525), (11.4, 4.075), c_oxy)

    # Pulmonary circuit:
    # RV (9.6, 3.7) -> Lungs (10.5, 7.2) [blue]
    ax.plot([8.9, 8.1, 8.1, 9.3], [3.7, 3.7, 7.2, 7.2], color=c_deoxy, lw=3.5)
    draw_arrow((8.1, 5.2), (8.1, 5.8), c_deoxy)

    # Lungs (10.5, 7.2) -> LA (11.4, 4.9) [red]
    ax.plot([11.7, 12.1, 12.1], [7.2, 7.2, 4.9], color=c_oxy, lw=3.5)
    draw_arrow((12.1, 4.9), (12.1, 4.9), c_oxy)
    ax.plot([12.1, 12.1], [7.2, 4.9], color=c_oxy, lw=3.5)
    draw_arrow((12.1, 6.2), (12.1, 5.6), c_oxy)

    # Systemic circuit:
    # LV (11.4, 3.7) -> Body (10.5, 1.2) [red]
    ax.plot([12.1, 12.7, 12.7, 11.7], [3.7, 3.7, 1.2, 1.2], color=c_oxy, lw=3.5)
    draw_arrow((12.7, 2.8), (12.7, 2.2), c_oxy)

    # Body (10.5, 1.2) -> RA (9.6, 4.9) [blue]
    ax.plot([9.3, 7.5, 7.5, 8.9], [1.2, 1.2, 4.9, 4.9], color=c_deoxy, lw=3.5)
    draw_arrow((7.5, 2.8), (7.5, 3.5), c_deoxy)

    # Divider between fish and mammal
    ax.plot([7.0, 7.0], [0.8, 8.2], color=GREY, lw=1.5, linestyle=":")

    save(fig, out)
