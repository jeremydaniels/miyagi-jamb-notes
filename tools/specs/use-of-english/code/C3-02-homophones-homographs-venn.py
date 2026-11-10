from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.0, "Word Relationships", ha="center", va="center",
            fontsize=18, fontweight="bold", color=INK)

    # Circles setup
    # Left: Homophones (sound), Right: Homographs (spelling), Center overlap: Homonyms
    r = 2.7
    c1 = (4.3, 3.4)
    c2 = (7.7, 3.4)

    # Soft colors
    # Left circle: soft blue
    circle_left = patches.Circle(c1, r, facecolor=BLUE, edgecolor=DEEP["blue"],
                                 alpha=0.45, lw=2.5)
    # Right circle: soft green
    circle_right = patches.Circle(c2, r, facecolor=GREEN, edgecolor=DEEP["green"],
                                  alpha=0.45, lw=2.5)
    ax.add_patch(circle_left)
    ax.add_patch(circle_right)

    # Overlap tint (soft yellow / cream / orange tint)
    # We can clip or simply draw an intersection patch or soft cream/yellow polygon
    # An easy clean way in matplotlib is a clip path or an ellipse approximation for the lens
    lens = patches.Ellipse((6.0, 3.4), width=2.4, height=3.9,
                           facecolor="#FFF3B0", edgecolor="none", alpha=0.55)
    ax.add_patch(lens)

    # Re-draw clean boundaries around the circles so outline is crisp
    circle_left_line = patches.Circle(c1, r, fill=False, edgecolor=DEEP["blue"], lw=2.5)
    circle_right_line = patches.Circle(c2, r, fill=False, edgecolor=DEEP["green"], lw=2.5)
    ax.add_patch(circle_left_line)
    ax.add_patch(circle_right_line)

    # Icon: Ear (simple line drawing near left circle)
    ear_x, ear_y = 2.4, 5.6
    ear_t = np.linspace(-0.6, 2.2, 50)
    # Outer ear curve
    ex = ear_x + 0.22 * np.cos(ear_t)
    ey = ear_y + 0.32 * np.sin(ear_t)
    ax.plot(ex, ey, color=DEEP["blue"], lw=2.2, solid_capstyle="round")
    # Inner ear notch
    ax.plot([ear_x + 0.05, ear_x + 0.12, ear_x + 0.05],
            [ear_y + 0.08, ear_y, ear_y - 0.12],
            color=DEEP["blue"], lw=1.8, solid_capstyle="round")

    # Icon: Pencil (near right circle)
    px, py = 9.6, 5.6
    # Pencil shaft (angled rectangle/polygon)
    pencil_poly = np.array([
        [px - 0.2, py - 0.2],
        [px + 0.15, py + 0.15],
        [px + 0.25, py + 0.05],
        [px - 0.1, py - 0.3]
    ])
    ax.add_patch(patches.Polygon(pencil_poly, closed=True, facecolor=DEEP["green"], edgecolor=DEEP["green"], lw=1.5))
    # Pencil tip
    tip_poly = np.array([
        [px - 0.2, py - 0.2],
        [px - 0.1, py - 0.3],
        [px - 0.3, py - 0.35]
    ])
    ax.add_patch(patches.Polygon(tip_poly, closed=True, facecolor=INK, edgecolor=INK, lw=1))

    # --- Left Circle Content: Homophones ---
    ax.text(2.6, 4.9, "Homophones", ha="center", va="center",
            fontsize=16, fontweight="bold", color=DEEP["blue"])
    ax.text(2.6, 4.4, "same sound", ha="center", va="center",
            fontsize=14, fontstyle="italic", color=INK)

    box_kw = dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["blue"], alpha=0.9, lw=1.2)
    ax.text(2.6, 3.4, "sea  /  see", ha="center", va="center",
            fontsize=15, color=INK, bbox=box_kw)
    ax.text(2.6, 2.4, "right  /  write", ha="center", va="center",
            fontsize=15, color=INK, bbox=box_kw)

    # --- Right Circle Content: Homographs ---
    ax.text(9.4, 4.9, "Homographs", ha="center", va="center",
            fontsize=16, fontweight="bold", color=DEEP["green"])
    ax.text(9.4, 4.4, "same spelling", ha="center", va="center",
            fontsize=14, fontstyle="italic", color=INK)

    box_kw_g = dict(boxstyle="round,pad=0.35", fc="white", ec=DEEP["green"], alpha=0.9, lw=1.2)
    ax.text(9.4, 3.4, "lead (to guide)\nlead (metal)", ha="center", va="center",
            fontsize=14, color=INK, bbox=box_kw_g)
    ax.text(9.4, 2.2, "tear (from the eye)\ntear (to rip)", ha="center", va="center",
            fontsize=14, color=INK, bbox=box_kw_g)

    # --- Center Overlap Content: Homonyms ---
    ax.text(6.0, 5.0, "Homonyms", ha="center", va="center",
            fontsize=16, fontweight="bold", color=INK)
    ax.text(6.0, 4.5, "same sound\nAND\nsame spelling", ha="center", va="center",
            fontsize=14, fontstyle="italic", color=INK)

    box_kw_m = dict(boxstyle="round,pad=0.35", fc="white", ec="#D4A017", alpha=0.95, lw=1.2)
    ax.text(6.0, 3.4, "bank (money)\nbank (river)", ha="center", va="center",
            fontsize=14, color=INK, bbox=box_kw_m)
    ax.text(6.0, 2.2, "bat (animal)\nbat (sport)", ha="center", va="center",
            fontsize=14, color=INK, bbox=box_kw_m)

    save(fig, out)
