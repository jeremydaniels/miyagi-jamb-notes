from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # Title / Summary formula banner at top
    ax.text(6.0, 7.45, "Genotype + environment = phenotype", 
            fontsize=16, fontweight="bold", color=INK, ha="center", va="center")

    # Box coordinates and sizes
    # Central box (Phenotype) - slightly wider to give ample room inside
    cx, cy, cw, ch = 4.4, 1.2, 3.2, 5.2
    # Left box (Genetic)
    lx, ly, lw, lh = 0.6, 1.2, 3.0, 5.2
    # Top-right box (Environment)
    trx, try_, trw, trh = 8.4, 4.0, 3.1, 2.4
    # Bottom-right box (Habitat)
    brx, bry, brw, brh = 8.4, 1.2, 3.1, 2.4

    # Draw rounded boxes
    box_defs = [
        (lx, ly, lw, lh, GREEN, DEEP["green"]),
        (trx, try_, trw, trh, ORANGE, DEEP["orange"]),
        (brx, bry, brw, brh, BLUE, DEEP["blue"]),
        (cx, cy, cw, ch, CREAM, INK)
    ]
    for bx, by, bw, bh, fc, ec in box_defs:
        rect = patches.FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.08,rounding_size=0.25",
                                      facecolor=fc, edgecolor=ec, lw=2.0)
        ax.add_patch(rect)

    # Connecting Arrows pointing to Central Box
    # From Left to Center (enters mid-left)
    ax.annotate("", xy=(cx, cy + ch * 0.5), xytext=(lx + lw, cy + ch * 0.5),
                arrowprops=dict(facecolor=DEEP["green"], edgecolor=DEEP["green"], width=3, headwidth=9, headlength=9))
    
    # From Top-right to Center (enters upper-right, safely above pupil figures)
    ax.annotate("", xy=(cx + cw, cy + ch * 0.82), xytext=(trx, try_ + trh * 0.5),
                arrowprops=dict(facecolor=DEEP["orange"], edgecolor=DEEP["orange"], width=3, headwidth=9, headlength=9))
    
    # From Bottom-right to Center (enters lower-right, along floor level)
    ax.annotate("", xy=(cx + cw, cy + ch * 0.22), xytext=(brx, bry + brh * 0.5),
                arrowprops=dict(facecolor=DEEP["blue"], edgecolor=DEEP["blue"], width=3, headwidth=9, headlength=9))

    # ================= LEFT BOX (Genetics) =================
    ax.text(lx + lw/2, ly + lh - 0.35, "Genetic constitution\n(genes)", fontsize=12, fontweight="bold",
            color=INK, ha="center", va="top")
    
    # DNA double helix (vertical)
    dna_y = np.linspace(ly + 0.6, ly + 3.3, 80)
    dna_x_center = lx + 0.75
    amp = 0.32
    x1 = dna_x_center + amp * np.sin(dna_y * 4.2)
    x2 = dna_x_center - amp * np.sin(dna_y * 4.2)
    ax.plot(x1, dna_y, color=DEEP["green"], lw=2.5)
    ax.plot(x2, dna_y, color=DEEP["green"], lw=2.5)
    for y_val in np.linspace(ly + 0.75, ly + 3.15, 12):
        x_a = dna_x_center + amp * np.sin(y_val * 4.2)
        x_b = dna_x_center - amp * np.sin(y_val * 4.2)
        ax.plot([x_a, x_b], [y_val, y_val], color=DEEP["green"], lw=1.5, alpha=0.85)

    # Chromosome pair (X shapes with centromere)
    def draw_chromosome(x_c, y_c, s=0.38):
        ax.plot([x_c - s*0.8, x_c + s*0.8], [y_c - s*1.3, y_c + s*1.3], color=DEEP["green"], lw=4.5, solid_capstyle='round')
        ax.plot([x_c + s*0.8, x_c - s*0.8], [y_c - s*1.3, y_c + s*1.3], color=DEEP["green"], lw=4.5, solid_capstyle='round')
        circ = patches.Circle((x_c, y_c), 0.08, facecolor="white", edgecolor=DEEP["green"], lw=1.5)
        ax.add_patch(circ)

    draw_chromosome(lx + 2.15, ly + 2.6, 0.42)
    draw_chromosome(lx + 2.15, ly + 1.25, 0.42)
    ax.text(dna_x_center, ly + 3.65, "DNA helix", fontsize=11, ha="center", color=INK)
    ax.text(lx + 2.15, ly + 3.65, "Chromosomes", fontsize=11, ha="center", color=INK)

    # ================= TOP-RIGHT BOX (Environment) =================
    ax.text(trx + trw/2, try_ + trh - 0.22, "Environmental conditions\n(food, light, temperature, disease)",
            fontsize=11, fontweight="bold", color=INK, ha="center", va="top")
    
    # Sun (light)
    sun_x, sun_y = trx + 0.55, try_ + 0.8
    sun_c = patches.Circle((sun_x, sun_y), 0.22, facecolor="#FDD835", edgecolor=DEEP["orange"], lw=1.5)
    ax.add_patch(sun_c)
    for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax.plot([sun_x + 0.26*np.cos(ang), sun_x + 0.4*np.cos(ang)],
                [sun_y + 0.26*np.sin(ang), sun_y + 0.4*np.sin(ang)], color=DEEP["orange"], lw=1.4)
    ax.text(sun_x, try_ + 0.25, "Sunlight", fontsize=11, ha="center", color=INK)

    # Plate of food (nutrition)
    px, py = trx + 1.55, try_ + 0.75
    plate = patches.Ellipse((px, py), 0.75, 0.32, facecolor="white", edgecolor=GREY, lw=1.5)
    ax.add_patch(plate)
    food1 = patches.Circle((px - 0.12, py + 0.04), 0.11, facecolor=DEEP["orange"], edgecolor=INK, lw=1)
    food2 = patches.Circle((px + 0.12, py + 0.04), 0.12, facecolor=DEEP["green"], edgecolor=INK, lw=1)
    ax.add_patch(food1)
    ax.add_patch(food2)
    ax.text(px, try_ + 0.25, "Nutrition", fontsize=11, ha="center", color=INK)

    # Thermometer (temperature)
    tx, ty = trx + 2.55, try_ + 0.55
    ax.plot([tx, tx], [ty, ty + 0.7], color=GREY, lw=3.5, solid_capstyle='round')
    ax.plot([tx, tx], [ty, ty + 0.45], color=DEEP["pink"], lw=2.0, solid_capstyle='round')
    t_bulb = patches.Circle((tx, ty), 0.11, facecolor=DEEP["pink"], edgecolor=GREY, lw=1)
    ax.add_patch(t_bulb)
    for dy in [0.25, 0.45, 0.62]:
        ax.plot([tx + 0.07, tx + 0.14], [ty + dy, ty + dy], color=GREY, lw=1)
    ax.text(tx, try_ + 0.25, "Temp.", fontsize=11, ha="center", color=INK)

    # ================= BOTTOM-RIGHT BOX (Habitat) =================
    ax.text(brx + brw/2, bry + brh - 0.22, "Habitat\n(where the organism lives)",
            fontsize=11, fontweight="bold", color=INK, ha="center", va="top")
    
    # Ground line
    g_line_y = bry + 0.55
    ax.plot([brx + 0.3, brx + brw - 0.3], [g_line_y, g_line_y], color=GREY, lw=1.5)

    # Shaded forest plant (under canopy)
    tree_canopy = patches.Ellipse((brx + 0.85, bry + 1.45), 1.05, 0.38, facecolor="#B0BEC5", edgecolor=GREY, lw=1.2, alpha=0.6)
    ax.add_patch(tree_canopy)
    ax.text(brx + 0.85, bry + 1.45, "Canopy shade", fontsize=9.5, ha="center", va="center", color=INK)
    ax.plot([brx + 0.85, brx + 0.85], [g_line_y, bry + 1.05], color=DEEP["green"], lw=2)
    lf1 = patches.Ellipse((brx + 0.72, bry + 0.85), 0.26, 0.11, angle=25, facecolor=GREEN, edgecolor=DEEP["green"])
    lf2 = patches.Ellipse((brx + 0.98, bry + 0.95), 0.26, 0.11, angle=-25, facecolor=GREEN, edgecolor=DEEP["green"])
    ax.add_patch(lf1); ax.add_patch(lf2)
    ax.text(brx + 0.85, bry + 0.25, "Dense forest\n(low light)", fontsize=11, ha="center", color=INK)

    # Plant in open sun (taller, thriving)
    ax.plot([brx + 2.25, brx + 2.25], [g_line_y, bry + 1.3], color=DEEP["green"], lw=2.5)
    for ly_pos, l_angle in [(0.75, 30), (0.92, -30), (1.1, 25), (1.23, -20)]:
        dx = 0.13 if l_angle > 0 else -0.13
        lf = patches.Ellipse((brx + 2.25 + dx, bry + ly_pos), 0.3, 0.12, angle=-l_angle,
                             facecolor=GREEN, edgecolor=DEEP["green"])
        ax.add_patch(lf)
    m_sun = patches.Circle((brx + 2.25, bry + 1.48), 0.12, facecolor="#FDD835", edgecolor=DEEP["orange"], lw=1)
    ax.add_patch(m_sun)
    ax.text(brx + 2.25, bry + 0.25, "Open sun\n(high light)", fontsize=11, ha="center", color=INK)

    # ================= CENTRAL BOX (Phenotype) =================
    ax.text(cx + cw/2, cy + ch - 0.35, "Phenotype\n(observable characteristics)",
            fontsize=12, fontweight="bold", color=INK, ha="center", va="top")

    # Pupil drawing function
    def draw_pupil(px, ground_y, total_h, col_shirt, label):
        head_r = total_h * 0.12
        head_y = ground_y + total_h - head_r
        # Head
        ax.add_patch(patches.Circle((px, head_y), head_r, facecolor=CREAM, edgecolor=INK, lw=1.5))
        # Torso
        torso_top = head_y - head_r
        torso_bot = ground_y + total_h * 0.42
        ax.plot([px, px], [torso_top, torso_bot], color=col_shirt, lw=4, solid_capstyle='round')
        # Arms
        ax.plot([px - 0.22, px, px + 0.22], [torso_top - 0.3, torso_top - 0.08, torso_top - 0.3],
                color=col_shirt, lw=2.5, solid_capstyle='round')
        # Legs
        ax.plot([px, px - 0.16], [torso_bot, ground_y], color=INK, lw=2.5, solid_capstyle='round')
        ax.plot([px, px + 0.16], [torso_bot, ground_y], color=INK, lw=2.5, solid_capstyle='round')
        ax.text(px, ground_y - 0.28, label, fontsize=11, ha="center", va="top", color=INK)

    c_ground = cy + 0.95
    # Ground floor line inside central box
    ax.plot([cx + 0.35, cx + cw - 0.35], [c_ground, c_ground], color=GREY, lw=1.5)

    # Heights of Pupil 1 & Pupil 2
    h1 = 1.85
    h2 = 2.50
    p1_x = cx + 0.85
    p2_x = cx + 2.35

    draw_pupil(p1_x, c_ground, h1, DEEP["blue"], "Pupil A\n(age 14)")
    draw_pupil(p2_x, c_ground, h2, DEEP["orange"], "Pupil B\n(age 14)")

    # Height comparison indicator placed cleanly BETWEEN the pupils
    ax.plot([p1_x, p2_x - 0.35], [c_ground + h1, c_ground + h1], color=GREY, ls="--", lw=1.4)
    mid_x = (p1_x + p2_x) / 2.0  # 1.6 relative to cx
    # Vertical dimension bracket between the two heights
    ax.plot([mid_x, mid_x], [c_ground + h1, c_ground + h2], color=DEEP["pink"], lw=2.0)
    ax.plot([mid_x - 0.08, mid_x + 0.08], [c_ground + h1, c_ground + h1], color=DEEP["pink"], lw=1.5)
    ax.plot([mid_x - 0.08, mid_x + 0.08], [c_ground + h2, c_ground + h2], color=DEEP["pink"], lw=1.5)
    # Centered annotation safely between pupils with no border collisions
    ax.text(mid_x, c_ground + (h1 + h2)/2, "Height\ndiff.",
            fontsize=11, fontweight="bold", ha="center", va="center", color=INK,
            bbox=dict(facecolor=CREAM, edgecolor="none", pad=1.5))

    save(fig, out)
