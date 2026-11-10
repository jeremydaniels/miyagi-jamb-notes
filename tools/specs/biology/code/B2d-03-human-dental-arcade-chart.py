from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle

def draw(out):
    fig = canvas(15, 8.5)
    
    # Left subplot: Child (milk teeth, 20)
    # Right subplot: Adult (permanent teeth, 32)
    ax_child = fig.add_axes([0.05, 0.18, 0.42, 0.72])
    ax_adult = fig.add_axes([0.53, 0.18, 0.42, 0.72])

    for ax in [ax_child, ax_adult]:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-5.2, 5.2)
        ax.set_ylim(-5.5, 5.5)

    # Color mapping
    c_incisor = BLUE
    c_canine = GREEN
    c_premolar = CREAM
    c_molar = ORANGE
    c_wisdom = "#FDEBD0" # lighter orange/cream for wisdom teeth

    edge_col = INK

    def draw_arch(ax, y_center, is_upper, teeth_types, radii_x, radii_y, y_stretch=1.0):
        n_half = len(teeth_types)
        t_vals = np.linspace(0.08, 0.95, n_half)
        sign = 1.0 if is_upper else -1.0

        for side in [-1, 1]:
            for i, (t, t_type) in enumerate(zip(t_vals, teeth_types)):
                x = side * (radii_x * np.sin(t * np.pi / 2))
                y = y_center + sign * (radii_y * np.cos(t * np.pi / 2) * y_stretch)

                if t_type == "incisor":
                    fc = c_incisor
                    w, h = 0.55, 0.38
                    angle = -side * (t * 55) if is_upper else side * (t * 55)
                elif t_type == "canine":
                    fc = c_canine
                    w, h = 0.52, 0.52
                    angle = -side * (t * 60)
                elif t_type == "premolar":
                    fc = c_premolar
                    w, h = 0.60, 0.55
                    angle = -side * (t * 40)
                elif t_type == "molar":
                    fc = c_molar
                    w, h = 0.78, 0.70
                    angle = 0
                elif t_type == "wisdom":
                    fc = c_wisdom
                    w, h = 0.72, 0.65
                    angle = 0

                patch = Ellipse((x, y), w, h, angle=angle, facecolor=fc, edgecolor=edge_col, lw=1.4, zorder=3)
                ax.add_patch(patch)

                if "molar" in t_type or t_type == "wisdom":
                    ax.plot([x - 0.15, x + 0.15], [y, y], color=GREY, lw=1.0, zorder=4)
                    ax.plot([x, x], [y - 0.15, y + 0.15], color=GREY, lw=1.0, zorder=4)
                elif t_type == "premolar":
                    ax.plot([x - 0.12, x + 0.12], [y, y], color=GREY, lw=1.0, zorder=4)

        t_bg = np.linspace(-np.pi/2 * 0.95, np.pi/2 * 0.95, 100)
        x_bg = radii_x * np.sin(t_bg)
        y_bg = y_center + sign * (radii_y * np.cos(t_bg) * y_stretch)
        ax.plot(x_bg, y_bg, color=PINK, lw=14, alpha=0.35, zorder=1, solid_capstyle='round')

    # Draw Child Jaws
    child_types = ["incisor", "incisor", "canine", "molar", "molar"]
    draw_arch(ax_child, y_center=0.4, is_upper=True, teeth_types=child_types, radii_x=2.9, radii_y=2.5)
    draw_arch(ax_child, y_center=-0.4, is_upper=False, teeth_types=child_types, radii_x=2.7, radii_y=2.4)

    # Draw Adult Jaws
    adult_types = ["incisor", "incisor", "canine", "premolar", "premolar", "molar", "molar", "wisdom"]
    draw_arch(ax_adult, y_center=0.4, is_upper=True, teeth_types=adult_types, radii_x=3.8, radii_y=3.2)
    draw_arch(ax_adult, y_center=-0.4, is_upper=False, teeth_types=adult_types, radii_x=3.6, radii_y=3.0)

    # Section Headers & Titles
    ax_child.text(0, 4.7, "milk teeth (20)", fontsize=16, weight="bold", color=INK, ha="center")
    ax_child.text(0, 3.8, "Upper jaw (maxilla)", fontsize=12, style="italic", color=INK, ha="center")
    ax_child.text(0, -3.8, "Lower jaw (mandible)", fontsize=12, style="italic", color=INK, ha="center")

    ax_adult.text(0, 4.7, "permanent teeth (32)", fontsize=16, weight="bold", color=INK, ha="center")
    ax_adult.text(0, 4.1, "Upper jaw (maxilla)", fontsize=12, style="italic", color=INK, ha="center")
    ax_adult.text(0, -4.1, "Lower jaw (mandible)", fontsize=12, style="italic", color=INK, ha="center")

    # Annotations & Pointers
    # Child annotations
    ax_child.annotate("incisors", xy=(-0.35, 2.8), xytext=(-2.8, 3.7),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8))
    
    ax_child.annotate("canines", xy=(-1.6, 2.45), xytext=(-3.8, 2.7),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8))

    ax_child.annotate("milk molars", xy=(-2.65, 1.2), xytext=(-4.8, -0.2),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8))

    # Adult annotations
    ax_adult.annotate("premolars", xy=(3.0, 2.3), xytext=(3.6, 3.4),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8))

    ax_adult.annotate("molars", xy=(3.5, 1.3), xytext=(3.8, 1.9),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8))

    ax_adult.annotate("wisdom tooth (third molar)", xy=(3.6, 0.4), xytext=(1.8, -0.1),
                      fontsize=12, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                      bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.8), ha="center")

    # Legend at the bottom
    legend_items = [
        ("incisors", c_incisor),
        ("canines", c_canine),
        ("premolars", c_premolar),
        ("molars / milk molars", c_molar),
        ("wisdom tooth (third molar)", c_wisdom)
    ]
    
    x_start = 0.12
    dx = 0.165
    y_leg = 0.06
    for i, (label, color) in enumerate(legend_items):
        cx = x_start + i * dx
        fig.patches.append(Rectangle((cx, y_leg), 0.022, 0.028, transform=fig.transFigure,
                                     facecolor=color, edgecolor=INK, lw=1.2, zorder=5))
        fig.text(cx + 0.028, y_leg + 0.007, label, fontsize=11.5, color=INK, verticalalignment='bottom')

    save(fig, out)
