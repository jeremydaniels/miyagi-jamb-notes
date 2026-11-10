from style import *
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.path import Path

def draw(out):
    fig = canvas(10, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)

    stages = [
        "1. Preliminary Study",
        "2. Feasibility",
        "3. Analysis",
        "4. Design",
        "5. Implementation",
        "6. Maintenance",
        "7. Review"
    ]

    # Professional palette cycling between blues, teals, and greens
    arrow_colors = [
        DEEP["blue"],
        "#0284c7",       # Sky blue
        "#0d9488",       # Teal
        DEEP["green"],
        "#16a34a",       # Bright green
        "#2563eb",       # Royal blue
        "#0f766e"        # Deep teal
    ]

    n = 7
    # Increased thickness of arrows to comfortably fit long words like Implementation and Maintenance
    r_in = 2.5
    r_out = 5.1
    r_mid = (r_in + r_out) / 2.0
    r_head_in = 2.2
    r_head_out = 5.4

    deg_per_seg = 360.0 / n
    gap = 3.5  # gap between arrows in degrees
    head_len_deg = 8.5  # angular length of arrow head

    # Clockwise: angles decrease from top (90 degrees)
    start_top = 90.0 + deg_per_seg / 2.0

    for i in range(n):
        theta_tail = start_top - i * deg_per_seg - gap / 2.0
        theta_tip = start_top - (i + 1) * deg_per_seg + gap / 2.0
        theta_body_end = theta_tip + head_len_deg

        angles_outer = np.linspace(np.radians(theta_tail), np.radians(theta_body_end), 25)
        angles_inner = np.linspace(np.radians(theta_body_end), np.radians(theta_tail), 25)

        verts = []
        codes = []

        # Start outer tail
        x_tail_out = r_out * np.cos(angles_outer[0])
        y_tail_out = r_out * np.sin(angles_outer[0])
        verts.append((x_tail_out, y_tail_out))
        codes.append(Path.MOVETO)

        # Outer arc
        for a in angles_outer[1:]:
            verts.append((r_out * np.cos(a), r_out * np.sin(a)))
            codes.append(Path.LINETO)

        # Outer head barb
        rad_body_end = np.radians(theta_body_end)
        verts.append((r_head_out * np.cos(rad_body_end), r_head_out * np.sin(rad_body_end)))
        codes.append(Path.LINETO)

        # Arrow tip
        rad_tip = np.radians(theta_tip)
        verts.append((r_mid * np.cos(rad_tip), r_mid * np.sin(rad_tip)))
        codes.append(Path.LINETO)

        # Inner head barb
        verts.append((r_head_in * np.cos(rad_body_end), r_head_in * np.sin(rad_body_end)))
        codes.append(Path.LINETO)

        # Base of inner body
        verts.append((r_in * np.cos(rad_body_end), r_in * np.sin(rad_body_end)))
        codes.append(Path.LINETO)

        # Inner arc
        for a in angles_inner[1:]:
            verts.append((r_in * np.cos(a), r_in * np.sin(a)))
            codes.append(Path.LINETO)

        # Close back to outer tail
        verts.append((x_tail_out, y_tail_out))
        codes.append(Path.CLOSEPOLY)

        path = Path(verts, codes)
        patch = mpatches.PathPatch(path, facecolor=arrow_colors[i], edgecolor='white', lw=1.5, zorder=2)
        ax.add_patch(patch)

        # Label position
        theta_center = (theta_tail + theta_tip) / 2.0
        rad_center = np.radians(theta_center)
        x_lbl = r_mid * np.cos(rad_center)
        y_lbl = r_mid * np.sin(rad_center)

        # Replace first space with newline
        label_text = stages[i].replace(" ", "\n", 1)

        ax.text(x_lbl, y_lbl, label_text, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white', zorder=4)

    # Central title / label
    ax.text(0, 0.45, "SYSTEM DEVELOPMENT\nLIFE CYCLE",
            ha='center', va='center', fontsize=18, fontweight='bold', color=INK, zorder=4)
    ax.text(0, -0.4, "(SDLC)",
            ha='center', va='center', fontsize=16, color=DEEP["blue"], fontweight='bold', zorder=4)
    ax.text(0, -0.9, "Continuous Flow",
            ha='center', va='center', fontsize=14, fontstyle='italic', color=GREY, zorder=4)

    # Subtle decorative circular guideline in the center
    inner_guide = mpatches.Circle((0, 0), 2.0, fill=True, color=CREAM, alpha=0.35, zorder=1)
    ax.add_patch(inner_guide)

    save(fig, out)
