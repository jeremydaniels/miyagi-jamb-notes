from style import *
import numpy as np
from matplotlib.patches import FancyArrowPatch

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_subplot(111)
    
    # Setup world bounds
    ax.set_xlim(-180, 180)
    ax.set_ylim(-70, 80)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw simplified world continents
    polys = continent_polys('World')
    for p in polys:
        if hasattr(p, 'exterior'):
            ax.fill(*p.exterior.xy, fc=CREAM, ec=GREY, lw=1.2, zorder=1)
            for interior in p.interiors:
                ax.fill(*interior.xy, fc='white', ec=GREY, lw=1.2, zorder=1)
        elif isinstance(p, np.ndarray):
            ax.fill(p[:, 0], p[:, 1], fc=CREAM, ec=GREY, lw=1.2, zorder=1)
        elif isinstance(p, (list, tuple)):
            arr = np.array(p)
            ax.fill(arr[:, 0], arr[:, 1], fc=CREAM, ec=GREY, lw=1.2, zorder=1)

    # Equator and Tropics reference lines
    ax.axhline(0, color=GREY, lw=1, ls='--', alpha=0.7, zorder=0)
    ax.text(-175, 2, 'Equator', fontsize=14, color=GREY, va='bottom', ha='left')
    
    # Helper to draw curved flow arrows
    def draw_curved_arrow(x_pts, y_pts, color, lw=2.5):
        t = np.linspace(0, 1, len(x_pts))
        t_dense = np.linspace(0, 1, 30)
        x_dense = np.interp(t_dense, t, x_pts)
        y_dense = np.interp(t_dense, t, y_pts)
        ax.plot(x_dense, y_dense, color=color, lw=lw, zorder=2)
        
        arrow = FancyArrowPatch((x_dense[-4], y_dense[-4]), (x_dense[-1], y_dense[-1]),
                                arrowstyle='->,head_length=5,head_width=3.5',
                                color=color, lw=lw, zorder=3, mutation_scale=2)
        ax.add_patch(arrow)

    # Label helper with white background bbox
    def label(x, y, text, color=INK, ha='center', va='center'):
        ax.text(x, y, text, fontsize=14, fontweight='bold', color=color,
                ha=ha, va=va, zorder=5,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85))

    WARM = DEEP['pink']  # Red/warm currents
    COLD = DEEP['blue']  # Blue/cold currents

    # --- 1. NORTH ATLANTIC GYRE (Clockwise) ---
    draw_curved_arrow([-78, -70, -50, -30], [25, 33, 42, 48], WARM)
    label(-62, 38, 'Gulf Stream', WARM, ha='right')
    
    draw_curved_arrow([-25, -45, -70], [15, 12, 14], WARM)
    draw_curved_arrow([-20, -18, -20], [45, 32, 18], COLD)
    label(-12, 28, 'Canary', COLD, ha='left')
    
    draw_curved_arrow([-55, -50, -45], [62, 53, 44], COLD)
    label(-60, 56, 'Labrador', COLD, ha='right')

    # --- 2. SOUTH ATLANTIC GYRE (Anti-clockwise) ---
    draw_curved_arrow([0, -25, -38, -45], [-5, -8, -20, -35], WARM)
    label(-42, -26, 'Brazil', WARM, ha='right')
    
    draw_curved_arrow([-40, -15, 10], [-48, -48, -45], COLD)
    draw_curved_arrow([12, 10, 0], [-35, -22, -8], COLD)
    label(15, -22, 'Benguela', COLD, ha='left')

    # --- 3. NORTH PACIFIC GYRE (Clockwise) ---
    draw_curved_arrow([125, 133, 148, 170], [18, 28, 36, 40], WARM)
    label(138, 25, 'Kuroshio', WARM, ha='right')
    
    draw_curved_arrow([160, 175], [41, 42], WARM)
    draw_curved_arrow([-175, -155, -135], [43, 45, 42], WARM)
    draw_curved_arrow([-130, -122, -112], [40, 30, 18], COLD)
    label(-110, 30, 'California', COLD, ha='left')
    
    draw_curved_arrow([-115, -145, -175], [12, 12, 12], WARM)
    draw_curved_arrow([175, 155, 130], [12, 12, 12], WARM)

    draw_curved_arrow([160, 150, 144], [55, 48, 40], COLD)
    label(162, 50, 'Oyashio', COLD, ha='left')

    # --- 4. SOUTH PACIFIC GYRE (Anti-clockwise) ---
    draw_curved_arrow([-75, -80, -85], [-45, -30, -12], COLD)
    label(-73, -28, 'Peru', COLD, ha='left')
    
    draw_curved_arrow([-90, -135, -175], [-8, -8, -8], WARM)
    draw_curved_arrow([175, 160], [-8, -10], WARM)
    
    draw_curved_arrow([155, 158, 152], [-14, -26, -38], WARM)
    label(165, -30, 'East Australian', WARM, ha='left')
    
    draw_curved_arrow([160, 175], [-52, -54], COLD)
    draw_curved_arrow([-130, -100, -75], [-55, -55, -52], COLD)

    # --- 5. INDIAN OCEAN GYRE (Anti-clockwise) ---
    draw_curved_arrow([55, 48, 32], [-10, -20, -34], WARM)
    label(42, -34, 'Agulhas', WARM, ha='right')
    
    draw_curved_arrow([105, 108, 98], [-42, -30, -16], COLD)
    label(112, -26, 'West\nAustralian', COLD, ha='left')
    
    draw_curved_arrow([95, 75, 55], [-12, -12, -10], WARM)

    # Gyre rotation badges / text annotations
    label(-42, 30, 'Clockwise Gyre\n(North Atlantic)', INK)
    label(-20, -30, 'Anti-clockwise Gyre\n(South Atlantic)', INK)
    label(-150, 26, 'Clockwise Gyre\n(North Pacific)', INK)
    label(-130, -32, 'Anti-clockwise Gyre\n(South Pacific)', INK)
    label(75, -28, 'Anti-clockwise Gyre\n(Indian Ocean)', INK)

    # Title
    ax.text(0, 75, 'Major Surface Ocean Currents and Gyres', fontsize=18, fontweight='bold', ha='center', va='center')
    
    # Legend box
    leg_x, leg_y = -170, -56
    ax.plot([leg_x, leg_x + 16], [leg_y, leg_y], color=WARM, lw=3)
    arrow_w = FancyArrowPatch((leg_x + 10, leg_y), (leg_x + 16, leg_y),
                              arrowstyle='->,head_length=5,head_width=3.5', color=WARM, lw=3, mutation_scale=2)
    ax.add_patch(arrow_w)
    ax.text(leg_x + 20, leg_y, 'Warm Current', fontsize=15, va='center', ha='left', bbox=dict(fc='white', ec='none', pad=0))

    ax.plot([leg_x, leg_x + 16], [leg_y - 8, leg_y - 8], color=COLD, lw=3)
    arrow_c = FancyArrowPatch((leg_x + 10, leg_y - 8), (leg_x + 16, leg_y - 8),
                              arrowstyle='->,head_length=5,head_width=3.5', color=COLD, lw=3, mutation_scale=2)
    ax.add_patch(arrow_c)
    ax.text(leg_x + 20, leg_y - 8, 'Cold Current', fontsize=15, va='center', ha='left', bbox=dict(fc='white', ec='none', pad=0))

    ax.text(0, -66, 'Sketch map: zones and current tracks are approximate', fontsize=14, style='italic', color=GREY, ha='center')

    save(fig, out)
