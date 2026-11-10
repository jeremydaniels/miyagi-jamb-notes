from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 10)
    
    # 2x2 grid for 4 steps of induction
    axes = [
        fig.add_axes([0.05, 0.53, 0.42, 0.40]), # Panel 1
        fig.add_axes([0.53, 0.53, 0.42, 0.40]), # Panel 2
        fig.add_axes([0.05, 0.05, 0.42, 0.40]), # Panel 3
        fig.add_axes([0.53, 0.05, 0.42, 0.40])  # Panel 4
    ]
    
    titles = [
        "Step 1: Charged rod brought near sphere",
        "Step 2: Sphere grounded (earthing)",
        "Step 3: Ground wire removed",
        "Step 4: Rod removed, net positive charge"
    ]
    
    sphere_center = (6.0, 5.0)
    sphere_radius = 2.0
    
    def draw_stand(ax):
        # Insulating stand
        stand_top_y = sphere_center[1] - sphere_radius
        stand_stem = patches.Rectangle((sphere_center[0] - 0.25, 0.8), 0.5, stand_top_y - 0.8,
                                       fc=GREY, ec=INK, lw=1.5)
        stand_base = patches.Rectangle((sphere_center[0] - 1.5, 0.5), 3.0, 0.3,
                                       fc=GREY, ec=INK, lw=1.5)
        ax.add_patch(stand_stem)
        ax.add_patch(stand_base)
        ax.text(sphere_center[0], 0.2, "Insulating stand", ha='center', va='center',
                fontsize=14, color=INK)

    def draw_sphere(ax):
        # Metal sphere
        sphere = patches.Circle(sphere_center, sphere_radius, fc=BLUE, ec=INK, lw=2, zorder=3)
        ax.add_patch(sphere)

    def draw_rod(ax):
        # Negatively charged rod
        rod = patches.FancyBboxPatch((0.4, 4.3), 2.2, 1.4, boxstyle="round,pad=0.2",
                                     fc=PINK, ec=DEEP["pink"], lw=2, zorder=4)
        ax.add_patch(rod)
        ax.text(1.5, 5.0, "–  –  –", color=INK, fontsize=18, fontweight='bold',
                ha='center', va='center', zorder=5)
        ax.text(1.5, 6.4, "Charged rod\n(negative)", ha='center', va='center',
                fontsize=14, color=INK, zorder=5)

    def draw_earth(ax, x, y):
        # Earth plates (fixed shapes: both x and y are 2-element lists)
        ax.plot([x - 0.7, x + 0.7], [y, y], color=INK, lw=2.5, zorder=4)
        ax.plot([x - 0.45, x + 0.45], [y - 0.2, y - 0.2], color=INK, lw=2.2, zorder=4)
        ax.plot([x - 0.2, x + 0.2], [y - 0.4, y - 0.4], color=INK, lw=1.8, zorder=4)
        ax.text(x, y - 0.75, "Earth", ha='center', va='center', fontsize=14, color=INK)

    for i, ax in enumerate(axes):
        ax.set_xlim(-0.5, 11)
        ax.set_ylim(-0.3, 8.5)
        ax.axis('off')
        
        # Panel frame
        rect = patches.FancyBboxPatch((0.0, 0.0), 10.8, 8.2, boxstyle="square,pad=0",
                                      fc="white", ec=GREY, lw=1.5, zorder=0)
        ax.add_patch(rect)
        
        # Title
        ax.text(5.4, 7.6, titles[i], ha='center', va='center', fontsize=15,
                fontweight='bold', color=INK, bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
        
        draw_stand(ax)
        draw_sphere(ax)

    # Panel 1: Rod near, + on left, - on right
    draw_rod(axes[0])
    axes[0].text(4.7, 5.7, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[0].text(4.4, 5.0, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[0].text(4.7, 4.3, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    
    axes[0].text(7.3, 5.7, "–", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[0].text(7.6, 5.0, "–", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[0].text(7.3, 4.3, "–", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)

    # Panel 2: Rod near, wire to earth, electrons flow to earth
    draw_rod(axes[1])
    axes[1].text(4.7, 5.7, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[1].text(4.4, 5.0, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[1].text(4.7, 4.3, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    
    # Ground wire connecting from far side of sphere (x=8, y=5) down to earth (x=9.5, y=2.5)
    axes[1].plot([8.0, 9.5, 9.5], [5.0, 5.0, 2.5], color=INK, lw=2, zorder=4)
    draw_earth(axes[1], 9.5, 2.5)
    # Electrons flowing down
    axes[1].annotate("", xy=(9.5, 3.3), xytext=(9.5, 4.5),
                     arrowprops=dict(arrowstyle="->", color=DEEP["orange"], lw=2.5), zorder=6)
    axes[1].text(9.7, 3.9, "e⁻", color=DEEP["orange"], fontsize=16, fontweight='bold', va='center')
    axes[1].text(9.2, 5.4, "Ground wire", color=INK, fontsize=14, ha='center')

    # Panel 3: Wire removed, rod still held near
    draw_rod(axes[2])
    axes[2].text(4.7, 5.7, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[2].text(4.4, 5.0, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[2].text(4.7, 4.3, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[2].text(8.5, 6.5, "Wire removed", fontsize=14, color=INK, ha='center',
                 bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY))

    # Panel 4: Rod removed, + charges distribute evenly
    r_pos = 1.2
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        px = sphere_center[0] + r_pos * np.cos(angle)
        py = sphere_center[1] + r_pos * np.sin(angle)
        axes[3].text(px, py, "+", fontsize=18, fontweight='bold', color=INK, ha='center', va='center', zorder=5)
    axes[3].text(2.5, 6.5, "Rod removed", fontsize=14, color=INK, ha='center',
                 bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=GREY))
    axes[3].text(8.5, 5.0, "Evenly distributed\npositive charge", fontsize=14,
                 color=INK, ha='center', va='center', bbox=dict(fc='white', ec='none', pad=0))

    save(fig, out)
