from style import *
import numpy as np

def draw(out):
    # Set up wide canvas with clean proportions
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-9, 7.5)
    ax.set_ylim(-4.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title - placed comfortably at top
    ax.text(-0.7, 5.0, 'Ray Diagram: Formation of Image by Convex Mirror',
            fontsize=17, ha='center', va='center', color=INK, fontweight='bold')

    # Principal axis
    ax.axhline(0, color=GREY, lw=1.5, zorder=1)

    # Mirror geometry
    # Pole P at (0,0), Center of curvature C at (5, 0), Focus F at (2.5, 0)
    # Circle equation: (x - 5)^2 + y^2 = 5^2 -> x = 5 - sqrt(25 - y^2)
    y_mirror = np.linspace(-3.5, 3.5, 200)
    x_mirror = 5 - np.sqrt(5**2 - y_mirror**2)

    # Silvered backing (hatching on the concave/inner side)
    ax.plot(x_mirror, y_mirror, color=INK, lw=3.2, zorder=4)
    for y_h in np.linspace(-3.3, 3.3, 28):
        x_h = 5 - np.sqrt(5**2 - y_h**2)
        ax.plot([x_h, x_h + 0.3], [y_h, y_h - 0.22], color=GREY, lw=1.2, zorder=3)

    # Key points: Pole P, Focus F, Centre of Curvature C
    ax.scatter([0, 2.5, 5.0], [0, 0, 0], color=INK, s=40, zorder=5)

    # Place labels with white bounding box to avoid overlapping the mirror curve or axis
    ax.text(-0.3, -0.4, 'P', fontsize=15, ha='right', va='top', color=INK, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=1.5))
    ax.text(2.5, -0.4, 'F', fontsize=15, ha='center', va='top', color=INK, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=1.5))
    ax.text(5.0, -0.4, 'C', fontsize=15, ha='center', va='top', color=INK, fontweight='bold',
            bbox=dict(fc='white', ec='none', pad=1.5))

    # Object
    x_obj = -6.5
    h_obj = 2.2
    # Object arrow
    ax.annotate('', xy=(x_obj, h_obj), xytext=(x_obj, 0),
                arrowprops=dict(arrowstyle='->', lw=3.0, color=DEEP['blue'], mutation_scale=20))
    ax.text(x_obj, h_obj + 0.3, 'Object', fontsize=15, ha='center', va='bottom',
            color=DEEP['blue'], fontweight='bold')

    # Ray 1: Parallel to principal axis
    # Hits mirror at (x_m1, h_obj)
    x_m1 = 5 - np.sqrt(5**2 - h_obj**2)
    y_m1 = h_obj

    # Incident Ray 1 (parallel to axis)
    ax.plot([x_obj, x_m1], [h_obj, h_obj], color=DEEP['orange'], lw=2.2, zorder=3)
    # Arrow showing forward direction
    ax.annotate('', xy=((x_obj + x_m1) / 2 + 0.25, h_obj), xytext=((x_obj + x_m1) / 2 - 0.25, h_obj),
                arrowprops=dict(arrowstyle='->', lw=2.0, color=DEEP['orange'], mutation_scale=15))

    # Reflected Ray 1: diverges along the line from F (2.5, 0) through (x_m1, y_m1)
    slope1 = (y_m1 - 0) / (x_m1 - 2.5)
    
    # End reflected ray safely below title
    y_refl_end = 4.2
    x_refl_end = x_m1 + (y_refl_end - y_m1) / slope1
    
    ax.plot([x_m1, x_refl_end], [y_m1, y_refl_end], color=DEEP['orange'], lw=2.2, zorder=3)

    # Arrow on reflected ray 1
    x_mid1 = (x_m1 + x_refl_end) / 2
    y_mid1 = (y_m1 + y_refl_end) / 2
    dx1 = x_refl_end - x_m1
    dy1 = y_refl_end - y_m1
    L1 = np.hypot(dx1, dy1)
    ax.annotate('', xy=(x_mid1 + 0.15*dx1/L1, y_mid1 + 0.15*dy1/L1),
                xytext=(x_mid1 - 0.15*dx1/L1, y_mid1 - 0.15*dy1/L1),
                arrowprops=dict(arrowstyle='->', lw=2.0, color=DEEP['orange'], mutation_scale=15))

    # Virtual extension of Ray 1 through virtual focus F
    ax.plot([x_m1, 2.5], [y_m1, 0], color=DEEP['orange'], lw=2.0, ls='--', zorder=2)

    # Ray 2: Directed towards Centre of Curvature C (5.0, 0)
    # Vector from C to Object tip: (x_obj - 5, h_obj)
    dist_obj_C = np.hypot(x_obj - 5.0, h_obj)
    t_mirror = 5.0 / dist_obj_C
    x_m2 = 5.0 + t_mirror * (x_obj - 5.0)
    y_m2 = 0.0 + t_mirror * h_obj

    # Incident Ray 2 towards mirror
    ax.plot([x_obj, x_m2], [h_obj, y_m2], color=DEEP['pink'], lw=2.2, zorder=3)
    # Inward arrow (towards C)
    x_mid2 = (x_obj + x_m2) / 2
    y_mid2 = (h_obj + y_m2) / 2
    dx2 = x_m2 - x_obj
    dy2 = y_m2 - h_obj
    L2 = np.hypot(dx2, dy2)
    ax.annotate('', xy=(x_mid2 + 0.3*dx2/L2, y_mid2 + 0.3*dy2/L2),
                xytext=(x_mid2 - 0.1*dx2/L2, y_mid2 - 0.1*dy2/L2),
                arrowprops=dict(arrowstyle='->', lw=2.0, color=DEEP['pink'], mutation_scale=15))
    # Outward arrow (reflected back on itself)
    ax.annotate('', xy=(x_mid2 - 0.8*dx2/L2, y_mid2 - 0.8*dy2/L2),
                xytext=(x_mid2 - 0.4*dx2/L2, y_mid2 - 0.4*dy2/L2),
                arrowprops=dict(arrowstyle='->', lw=2.0, color=DEEP['pink'], mutation_scale=15))

    # Virtual extension of Ray 2 towards C
    ax.plot([x_m2, 5.0], [y_m2, 0], color=DEEP['pink'], lw=2.0, ls='--', zorder=2)

    # Intersection of virtual rays = Virtual Image tip
    slope2 = (0 - h_obj) / (5.0 - x_obj)
    x_img = (2.5 * slope1 - 5.0 * slope2) / (slope1 - slope2)
    y_img = slope1 * (x_img - 2.5)

    # Virtual Image arrow
    ax.annotate('', xy=(x_img, y_img), xytext=(x_img, 0),
                arrowprops=dict(arrowstyle='->', lw=2.8, color=DEEP['green'], mutation_scale=16))
    ax.text(x_img, y_img + 0.3, 'Virtual\nImage', fontsize=14, ha='center', va='bottom',
            color=DEEP['green'], fontweight='bold', bbox=dict(fc='white', ec='none', pad=1))

    # Mirror label
    ax.text(0.8, 3.8, 'Convex Mirror', fontsize=15, ha='left', va='center',
            color=INK, fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.3'))

    # Legend / Explanatory box
    ax.text(-8.4, -3.5, 'P: Pole\nF: Virtual focus\nC: Centre of curvature',
            fontsize=14, color=INK, va='center', ha='left',
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.4'))

    save(fig, out)
