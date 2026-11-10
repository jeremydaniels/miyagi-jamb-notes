from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    # Canvas size: broad enough to prevent overlapping boxes and text
    fig = canvas(14, 12)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1.5, 12.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(7.0, 11.6, "Checks and Balances", fontsize=20, weight='bold', ha='center', va='center', color=INK)

    # Coordinates of the three main institutions (large triangle)
    pos = {
        'Exec': np.array([7.0, 9.2]),
        'Leg': np.array([2.2, 2.2]),
        'Jud': np.array([11.8, 2.2])
    }

    r = 1.45  # Radius of institution circles

    # Draw Nodes
    nodes_info = [
        ('Exec', "Executive", BLUE, DEEP['blue']),
        ('Leg', "Legislature", GREEN, DEEP['green']),
        ('Jud', "Judiciary", PINK, DEEP['pink'])
    ]

    for key, name, face_col, edge_col in nodes_info:
        p = pos[key]
        circle = patches.Circle(p, r, facecolor=face_col, edgecolor=edge_col, lw=2.5, zorder=4)
        ax.add_patch(circle)
        ax.text(p[0], p[1], name, fontsize=16, weight='bold', ha='center', va='center', color=INK, zorder=5)

    def draw_arrow(start, end, rad, color):
        arrow = patches.FancyArrowPatch(
            start, end,
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=8,head_width=5",
            lw=2.2,
            color=color,
            zorder=3
        )
        ax.add_patch(arrow)

    # ---------------------------------------------------------
    # 1. Executive <--> Legislature
    # Vector from Leg to Exec
    v_le = pos['Exec'] - pos['Leg']
    u_le = v_le / np.linalg.norm(v_le)
    # Perpendicular unit vector (points outward to the upper-left)
    perp_le = np.array([-u_le[1], u_le[0]])

    # Arrow: Executive -> Legislature ("Vetoes bills")
    # Outer arrow: shifted outwards by perpendicular offset
    start_el = (pos['Exec'] - u_le * r) + perp_le * 0.4
    end_el = (pos['Leg'] + u_le * r) + perp_le * 0.4
    draw_arrow(start_el, end_el, -0.08, DEEP['blue'])

    ax.text(3.3, 6.7, "Vetoes bills",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    # Arrow: Legislature -> Executive ("Approves budget, confirms appointments, impeachment")
    # Inner arrow: shifted inwards
    start_le = (pos['Leg'] + u_le * r) - perp_le * 0.4
    end_le = (pos['Exec'] - u_le * r) - perp_le * 0.4
    draw_arrow(start_le, end_le, -0.08, DEEP['green'])

    ax.text(5.5, 5.0, "Approves budget,\nconfirms appointments,\nimpeachment",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    # ---------------------------------------------------------
    # 2. Executive <--> Judiciary
    # Vector from Jud to Exec
    v_je = pos['Exec'] - pos['Jud']
    u_je = v_je / np.linalg.norm(v_je)
    # Perpendicular unit vector (points outward to the upper-right)
    perp_je = np.array([u_je[1], -u_je[0]])

    # Arrow: Executive -> Judiciary ("Appoints judges")
    # Outer arrow: shifted outwards
    start_ej = (pos['Exec'] - u_je * r) + perp_je * 0.4
    end_ej = (pos['Jud'] + u_je * r) + perp_je * 0.4
    draw_arrow(start_ej, end_ej, 0.08, DEEP['blue'])

    ax.text(10.7, 6.7, "Appoints judges",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    # Arrow: Judiciary -> Executive ("Judicial review (declares actions unconstitutional)")
    # Inner arrow: shifted inwards
    start_je = (pos['Jud'] + u_je * r) - perp_je * 0.4
    end_je = (pos['Exec'] - u_je * r) - perp_je * 0.4
    draw_arrow(start_je, end_je, 0.08, DEEP['pink'])

    ax.text(8.5, 5.0, "Judicial review\n(declares actions\nunconstitutional)",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    # ---------------------------------------------------------
    # 3. Legislature <--> Judiciary (Horizontal base)
    # Upper arrow: Legislature -> Judiciary ("Confirms judges")
    start_lj = pos['Leg'] + np.array([r, 0.35])
    end_lj = pos['Jud'] + np.array([-r, 0.35])
    draw_arrow(start_lj, end_lj, 0.0, DEEP['green'])

    ax.text(7.0, 3.0, "Confirms judges",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    # Lower arrow: Judiciary -> Legislature ("Judicial review (declares actions unconstitutional)")
    start_jl = pos['Jud'] + np.array([-r, -0.35])
    end_jl = pos['Leg'] + np.array([r, -0.35])
    draw_arrow(start_jl, end_jl, 0.0, DEEP['pink'])

    ax.text(7.0, 1.4, "Judicial review (declares actions unconstitutional)",
            fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=GREY, lw=1.2), zorder=6)

    save(fig, out)
