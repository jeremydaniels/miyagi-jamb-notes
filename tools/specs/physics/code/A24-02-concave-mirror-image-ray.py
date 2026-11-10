from style import *
import numpy as np

def draw(out):
    fig = canvas(10, 7)
    ax = fig.add_subplot(111)
    ax.axis('off')

    # Ray arrow helper
    def add_dir(x1, y1, x2, y2, c):
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        mag = np.hypot(dx, dy)
        ux, uy = dx / mag, dy / mag
        ax.annotate('', xy=(xm + ux * 0.1, ym + uy * 0.1), xytext=(xm - ux * 0.1, ym - uy * 0.1),
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.5, mutation_scale=15))

    # Points and Parameters
    # Object base is at x=2. Center of curvature C at x=4. Focal point F at x=6. Mirror vertex at x=8.
    C_x, F_x, M_x = 4, 6, 8
    Obj_x, Obj_y = 2, 2
    
    # Exact mirror curve: shallow parabola x = 8 + 0.02 * y^2
    y_m = np.linspace(-5, 3.5, 100)
    x_m = M_x + 0.02 * y_m**2
    ax.plot(x_m, y_m, color=INK, lw=3, zorder=5)
    
    # Hatch marks to indicate mirror surface
    for i in range(0, len(y_m), 4):
        ax.plot([x_m[i], x_m[i] + 0.15], [y_m[i], y_m[i]], color=INK, lw=1, zorder=4)

    # Principal axis
    ax.axhline(0, color=INK, lw=1.2, zorder=1)

    # Mark C and F
    ax.plot([C_x, F_x], [0, 0], 'o', color=INK, markersize=6, zorder=6)
    bbox = dict(fc='white', ec='none', pad=2)
    ax.text(C_x, -0.3, "C", ha='center', va='top', fontsize=16, color=INK, bbox=bbox, zorder=7)
    ax.text(F_x, -0.3, "F", ha='center', va='top', fontsize=16, color=INK, bbox=bbox, zorder=7)

    # Ray 1: Parallel to axis, reflects through F
    # Incident hits mirror at y = 2 -> x = 8 + 0.02*(2^2) = 8.08
    M1_x, M1_y = M_x + 0.02 * Obj_y**2, Obj_y
    # Reflected passes through F(6, 0)
    ray1_slope = (0 - M1_y) / (F_x - M1_x)
    ray1_end_x = 2.5
    ray1_end_y = M1_y + ray1_slope * (ray1_end_x - M1_x)
    
    # Draw Ray 1
    ax.plot([Obj_x, M1_x], [Obj_y, M1_y], color=DEEP['pink'], lw=1.5, zorder=2)
    ax.plot([M1_x, ray1_end_x], [M1_y, ray1_end_y], color=DEEP['pink'], lw=1.5, zorder=2)
    add_dir(Obj_x, Obj_y, M1_x, M1_y, DEEP['pink'])
    add_dir(M1_x, M1_y, ray1_end_x, ray1_end_y, DEEP['pink'])

    # Ray 2: Through C, reflects back along same path
    # Line from (2, 2) through (4, 0): slope is -1. Equation: y = -x + 4 -> x = 4 - y
    # Intersection with mirror x = 8 + 0.02*y^2
    # 4 - y = 8 + 0.02*y^2  => 0.02*y^2 + y + 4 = 0
    # Roots: y = (-1 + np.sqrt(1 - 0.32)) / 0.04
    M2_y = (-1 + np.sqrt(1 - 4 * 0.02 * 4)) / (2 * 0.02)
    M2_x = 4 - M2_y
    ray2_end_x = 2.5  # Don't extend further than needed, stop past intersection
    ray2_end_y = 4 - ray2_end_x
    
    # Draw Ray 2: Start from Obj tip to mirror, and reflect back
    ax.plot([Obj_x, M2_x], [Obj_y, M2_y], color=DEEP['blue'], lw=1.5, zorder=2)
    ax.plot([M2_x, ray2_end_x], [M2_y, ray2_end_y], color=DEEP['blue'], lw=1.5, zorder=2)
    
    # Forward direction arrow
    add_dir(Obj_x, Obj_y, (Obj_x + C_x)/2, (Obj_y + 0)/2, DEEP['blue'])
    # Reflected direction arrow (back from mirror)
    add_dir(M2_x, M2_y, Obj_x, Obj_y, DEEP['blue'])

    # Calculate exact Image Intersection
    # Ray 1: y - 0 = ray1_slope * (x - 6)
    # Ray 2: y = -x + 4
    # ray1_slope * (x - 6) = -x + 4  =>  (ray1_slope + 1) * x = 4 + 6 * ray1_slope
    Img_x = (4 + 6 * ray1_slope) / (ray1_slope + 1)
    Img_y = -Img_x + 4

    # Draw Object Arrow
    ax.annotate('', xy=(Obj_x, Obj_y), xytext=(Obj_x, 0),
                arrowprops=dict(arrowstyle='-|>', color=DEEP['green'], lw=2, mutation_scale=20),
                zorder=4)
    ax.text(Obj_x, Obj_y + 0.2, "Object", ha='center', va='bottom', fontsize=16, color=INK, bbox=bbox, zorder=7)

    # Draw Image Arrow
    ax.annotate('', xy=(Img_x, Img_y), xytext=(Img_x, 0),
                arrowprops=dict(arrowstyle='-|>', color=DEEP['orange'], lw=2, mutation_scale=20),
                zorder=4)
    ax.text(Img_x, Img_y - 0.2, "Image", ha='center', va='top', fontsize=16, color=INK, bbox=bbox, zorder=7)

    # Adjust limits
    ax.set_xlim(0.5, 9)
    ax.set_ylim(-5.5, 3.5)

    save(fig, out)
