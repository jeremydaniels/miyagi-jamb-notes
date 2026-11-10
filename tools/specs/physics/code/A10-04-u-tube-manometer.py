from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 6.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Dimensions and positions
    flask_center = (2.2, 4.8)
    flask_radius = 1.3
    
    # Gas flask circle and interior
    flask_circle = patches.Circle(flask_center, flask_radius, facecolor=CREAM, edgecolor=INK, lw=2.5, zorder=4)
    ax.add_patch(flask_circle)
    
    # Label inside flask
    ax.text(flask_center[0], flask_center[1], 'Gas pressure\n($P_{gas}$)', 
            ha='center', va='center', fontsize=15, color=INK, fontweight='medium', zorder=6)

    # U-tube geometry
    cx = 6.2
    cy = 2.0
    r_in = 0.6
    r_out = 1.2
    
    # Levels
    y_low = 2.0   
    y_high = 4.2  
    
    # Parametric semicircles for lower bend:
    # theta from pi down to 0 gives y going downwards: y = cy - r * sin(theta)
    theta = np.linspace(np.pi, 0, 50)
    x_out_curve = cx - r_out * np.cos(theta)
    y_out_curve = cy - r_out * np.sin(theta)
    
    x_in_curve = cx - r_in * np.cos(theta)
    y_in_curve = cy - r_in * np.sin(theta)

    # --- Manometer Liquid (Blue polygon) ---
    liquid_x = np.concatenate([
        [5.0, 5.0],
        x_out_curve,
        [7.4, 7.4, 6.8, 6.8],
        x_in_curve[::-1],
        [5.6, 5.6, 5.0]
    ])
    liquid_y = np.concatenate([
        [y_low, cy],
        y_out_curve,
        [cy, y_high, y_high, cy],
        y_in_curve[::-1],
        [cy, y_low, y_low]
    ])
    liquid_poly = patches.Polygon(np.column_stack([liquid_x, liquid_y]),
                                  facecolor=BLUE, edgecolor=DEEP['blue'], lw=1.5, zorder=2)
    ax.add_patch(liquid_poly)

    # Meniscus lines
    ax.plot([5.0, 5.6], [y_low, y_low], color=DEEP['blue'], lw=2.5, zorder=3)
    ax.plot([6.8, 7.4], [y_high, y_high], color=DEEP['blue'], lw=2.5, zorder=3)

    # --- Glass Tubing Walls ---
    # Connector & Left arm outer wall:
    ax.plot([3.4, 5.0, 5.0], [4.5, 4.5, 2.0], color=INK, lw=2.5, zorder=5)
    # Outer bottom bend:
    ax.plot(x_out_curve, y_out_curve, color=INK, lw=2.5, zorder=5)
    # Right arm outer wall:
    ax.plot([7.4, 7.4], [2.0, 5.8], color=INK, lw=2.5, zorder=5)

    # Connector & Inner wall:
    ax.plot([3.4, 5.6, 5.6], [5.1, 5.1, 2.0], color=INK, lw=2.5, zorder=5)
    # Inner bottom bend:
    ax.plot(x_in_curve, y_in_curve, color=INK, lw=2.5, zorder=5)
    # Right arm inner wall:
    ax.plot([6.8, 6.8], [2.0, 5.8], color=INK, lw=2.5, zorder=5)

    # Fill connector neck interior with CREAM so flask border doesn't show
    neck_patch = patches.Rectangle((3.3, 4.52), 1.75, 0.56, facecolor=CREAM, edgecolor='none', zorder=4)
    ax.add_patch(neck_patch)

    # Horizontal dotted reference line across from left fluid level to right arm
    ax.plot([5.0, 7.9], [y_low, y_low], color=GREY, linestyle='--', lw=2, zorder=3)
    
    # Top level dotted line on right arm for bracket
    ax.plot([7.4, 7.9], [y_high, y_high], color=GREY, linestyle='--', lw=2, zorder=3)

    # Dimension / bracket for height difference 'h'
    hx = 8.1
    ax.annotate('', xy=(hx, y_high), xytext=(hx, y_low),
                arrowprops=dict(arrowstyle='<->', color=INK, lw=2, shrinkA=0, shrinkB=0), zorder=5)
    ax.plot([hx - 0.15, hx + 0.15], [y_high, y_high], color=INK, lw=2, zorder=5)
    ax.plot([hx - 0.15, hx + 0.15], [y_low, y_low], color=INK, lw=2, zorder=5)
    ax.text(hx + 0.35, (y_high + y_low) / 2, '$h$', ha='left', va='center', fontsize=17, color=INK, fontweight='bold')

    # Atmospheric pressure arrow pointing into open right arm
    ax.annotate('', xy=(7.1, 5.9), xytext=(7.1, 6.8),
                arrowprops=dict(arrowstyle='->', color=DEEP['orange'], lw=3, mutation_scale=20), zorder=5)
    ax.text(7.1, 7.05, 'Atmospheric pressure\n($P_{atm}$)', ha='center', va='bottom',
            fontsize=15, color=INK, fontweight='medium',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none'))

    # Liquid label with pointer arrow outside the tube to avoid overlapping borders
    ax.annotate('Liquid\n(mercury)', xy=(6.2, 1.1), xytext=(6.2, 0.25),
                ha='center', va='top', fontsize=14, color=DEEP['blue'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=DEEP['blue'], lw=1.8))

    save(fig, out)
