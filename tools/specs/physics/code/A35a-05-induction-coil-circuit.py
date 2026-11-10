from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.5, 7.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 7.1, "Induction Coil Circuit Diagram", fontsize=18, fontweight='bold', ha='center', color=INK)

    # 1. Soft iron core
    core = patches.Rectangle((3.0, 3.8), 4.2, 0.4, facecolor=GREY, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(core)
    ax.text(5.1, 4.0, "Soft Iron Core", fontsize=14, ha='center', va='center', color=INK, fontweight='bold')

    # 2. Secondary coil (many turns, wound over the core)
    sec_x_start = 3.4
    sec_x_end = 6.8
    n_sec_turns = 16
    sec_xs = np.linspace(sec_x_start, sec_x_end, n_sec_turns)
    sec_y_base = 4.35
    sec_h = 0.5

    for i in range(len(sec_xs) - 1):
        x1, x2 = sec_xs[i], sec_xs[i+1]
        arc_x = np.linspace(x1, x2, 20)
        arc_y = sec_y_base + np.sin(np.pi * (arc_x - x1) / (x2 - x1)) * sec_h
        ax.plot(arc_x, arc_y, color=DEEP['orange'], lw=2.5, zorder=3)

    # Secondary leads leading to an open spark gap
    ax.plot([sec_x_start, sec_x_start, 4.5], [sec_y_base, 5.8, 5.8], color=DEEP['orange'], lw=2.5)
    ax.plot([sec_x_end, sec_x_end, 5.7], [sec_y_base, 5.8, 5.8], color=DEEP['orange'], lw=2.5)

    # Open spark gap terminals (separated spheres/terminals, strictly open)
    ax.plot(4.5, 5.8, marker='o', markersize=9, color=INK, zorder=5)
    ax.plot(5.7, 5.8, marker='o', markersize=9, color=INK, zorder=5)

    ax.text(5.1, 6.25, "Spark Gap (Open)", fontsize=14, ha='center', va='bottom', color=INK,
            fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    ax.text(2.6, 5.0, "Secondary Coil\n(many turns)", fontsize=14, ha='right', va='center',
            color=DEEP['orange'], fontweight='bold', bbox=dict(fc='white', ec='none', pad=0.2))

    # 3. Primary coil (few turns, below the core)
    pri_x_start = 3.7
    pri_x_end = 6.5
    n_pri_turns = 6
    pri_xs = np.linspace(pri_x_start, pri_x_end, n_pri_turns)
    pri_y_base = 3.65
    pri_h = 0.45

    for i in range(len(pri_xs) - 1):
        x1, x2 = pri_xs[i], pri_xs[i+1]
        arc_x = np.linspace(x1, x2, 20)
        arc_y = pri_y_base - np.sin(np.pi * (arc_x - x1) / (x2 - x1)) * pri_h
        ax.plot(arc_x, arc_y, color=DEEP['blue'], lw=3.5, zorder=3)

    # Primary label placed clearly to avoid overlapping circuit wires
    ax.text(5.1, 2.7, "Primary Coil (few turns)", fontsize=14, ha='center', va='top',
            color=DEEP['blue'], fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # 4. Primary Circuit connections
    # Left end of primary connects down to battery at x = 1.2
    ax.plot([pri_x_start, 1.2, 1.2], [pri_y_base, pri_y_base, 2.0], color=INK, lw=2)

    # Battery (horizontal plates at x = 1.2, y between 1.3 and 1.9)
    bat_y = [1.9, 1.7, 1.5, 1.3]
    widths = [0.7, 0.35, 0.7, 0.35]
    for y, w in zip(bat_y, widths):
        ax.plot([1.2 - w/2, 1.2 + w/2], [y, y], color=INK, lw=2.5 if w > 0.4 else 4)

    # Battery label placed completely to the left without touching plates
    ax.text(0.1, 1.6, "Battery\n(+ / −)", fontsize=14, ha='left', va='center',
            color=INK, fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # Bottom wire from battery leading to the armature base
    ax.plot([1.2, 1.2, 8.8], [1.3, 0.5, 0.5], color=INK, lw=2)

    # Right end of primary connects to contact screw mount
    ax.plot([pri_x_end, 7.8, 7.8], [pri_y_base, pri_y_base, 2.2], color=INK, lw=2)

    # 5. Mechanical Interrupter: Contact screw & Armature (aligned with iron core end)
    # Armature spring attached to bottom wire at x=8.8, extending vertically to y=4.1
    ax.plot([8.8, 8.8], [0.5, 4.0], color=DEEP['green'], lw=3.5)
    # Soft iron armature hammer opposite to core end (x=7.2)
    armature_head = patches.Rectangle((8.3, 3.75), 0.5, 0.5, facecolor=GREY, edgecolor=INK, lw=2, zorder=4)
    ax.add_patch(armature_head)

    ax.text(9.1, 3.9, "Armature\n(Spring reed)", fontsize=14, ha='left', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))

    # Contact point on armature at y = 2.2
    ax.plot(8.8, 2.2, marker='o', markersize=6, color=INK, zorder=5)

    # Adjustable contact screw touching at x=8.75, y=2.2
    ax.plot([7.8, 8.7], [2.2, 2.2], color=INK, lw=3)
    ax.plot([8.7, 8.7], [2.05, 2.35], color=INK, lw=3)  # screw tip

    ax.text(7.7, 2.65, "Contact Screw", fontsize=14, ha='right', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))

    # Mechanical Interrupter overall annotation
    ax.annotate("Mechanical\nInterrupter", xy=(8.75, 2.2), xytext=(9.7, 2.2),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                fontsize=14, ha='left', va='center', color=INK,
                bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.25'))

    # 6. Capacitor wired in parallel across the interrupter contacts
    # Routed outward to the right side so it does not collide with wires or armature
    # Left plate connection from screw mount at (7.8, 1.4)
    ax.plot(7.8, 1.4, marker='o', markersize=5, color=INK)
    ax.plot([7.8, 7.8, 10.3], [2.2, 1.4, 1.4], color=INK, lw=2)
    ax.plot([10.3, 10.3], [1.4, 1.2], color=INK, lw=2)

    # Right plate connection from armature bottom wire at (8.8, 0.5)
    ax.plot(8.8, 0.5, marker='o', markersize=5, color=INK)
    ax.plot([8.8, 10.7, 10.7], [0.5, 0.5, 1.2], color=INK, lw=2)

    # Capacitor plates at x = 10.3 and x = 10.7, y = 1.2
    ax.plot([10.05, 10.55], [1.2, 1.2], color=DEEP['lav'], lw=3.5)
    ax.plot([10.45, 10.95], [1.0, 1.0], color=DEEP['lav'], lw=3.5)
    ax.plot([10.3, 10.3], [1.2, 1.2], color=DEEP['lav'], lw=3.5)
    ax.plot([10.7, 10.7], [0.5, 1.0], color=INK, lw=2)

    # Clean standard capacitor parallel plates representation:
    # Plate 1: (10.0 to 10.6 at y=1.2)
    # Plate 2: (10.0 to 10.6 at y=0.9)
    # Let's draw clean horizontal plates:
    ax.plot([9.9, 10.7], [1.2, 1.2], color=DEEP['lav'], lw=3.5, zorder=5)
    ax.plot([9.9, 10.7], [0.85, 0.85], color=DEEP['lav'], lw=3.5, zorder=5)
    # Adjust connect leads
    ax.plot([10.3, 10.3], [1.4, 1.2], color=INK, lw=2)
    ax.plot([10.3, 10.3], [0.85, 0.5], color=INK, lw=2)
    ax.plot([8.8, 10.3], [0.5, 0.5], color=INK, lw=2)

    ax.text(10.3, 0.2, "Capacitor", fontsize=14, ha='center', va='top',
            color=DEEP['lav'], fontweight='bold', bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.2'))

    save(fig, out)
