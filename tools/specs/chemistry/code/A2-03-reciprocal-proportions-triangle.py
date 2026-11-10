from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(10, 8.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 9.5)
    ax.axis('off')

    # Title
    ax.text(5, 9.0, "Law of Reciprocal Proportions", fontsize=18, weight='bold', ha='center', color=INK)

    # Vertex coordinates: Triangle with S at top, H at bottom-left, O at bottom-right
    # Top: S at (5, 6.8)
    # Bottom Left: H at (2.0, 1.8)
    # Bottom Right: O at (8.0, 1.8)
    v_S = np.array([5.0, 6.8])
    v_H = np.array([2.0, 1.8])
    v_O = np.array([8.0, 1.8])

    # Draw connecting edges (double-headed arrows or thick lines)
    # We use annotate with double arrows
    def draw_edge(p1, p2, col):
        ax.annotate("", xy=p1, xytext=p2,
                    arrowprops=dict(arrowstyle="<->", color=col, lw=2.5, shrinkA=32, shrinkB=32))

    draw_edge(v_S, v_H, DEEP["blue"])
    draw_edge(v_S, v_O, DEEP["orange"])
    draw_edge(v_H, v_O, DEEP["green"])

    # Edge midpoints and labels
    # S - H edge (H2S)
    # Midpoint: (3.5, 4.3)
    ax.text(2.6, 4.7, "H₂S", fontsize=16, weight='bold', color=DEEP["blue"], ha='center',
            bbox=dict(fc=CREAM, ec=DEEP["blue"], boxstyle="round,pad=0.3", lw=1.5))
    ax.text(1.9, 4.0, "32g S + 2g H", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1))

    # S - O edge (SO2)
    # Midpoint: (6.5, 4.3)
    ax.text(7.4, 4.7, "SO₂", fontsize=16, weight='bold', color=DEEP["orange"], ha='center',
            bbox=dict(fc=CREAM, ec=DEEP["orange"], boxstyle="round,pad=0.3", lw=1.5))
    ax.text(8.1, 4.0, "32g S + 32g O", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", lw=1))

    # H - O edge (H2O)
    # Midpoint: (5.0, 1.8)
    ax.text(5.0, 2.35, "H₂O", fontsize=16, weight='bold', color=DEEP["green"], ha='center',
            bbox=dict(fc=CREAM, ec=DEEP["green"], boxstyle="round,pad=0.3", lw=1.5))
    ax.text(5.0, 1.15, "2g H + 16g O (which scales to 32g O)", fontsize=14, color=INK, ha='center',
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1))

    # Draw vertices (circles with element symbols)
    vertices = [
        (v_S, "S", "Sulfur", PINK, DEEP["pink"]),
        (v_H, "H", "Hydrogen", BLUE, DEEP["blue"]),
        (v_O, "O", "Oxygen", LAV, DEEP["lav"]),
    ]

    for pt, symbol, name, fill_col, border_col in vertices:
        circle = patches.Circle((pt[0], pt[1]), radius=0.6, fc=fill_col, ec=border_col, lw=2.5, zorder=5)
        ax.add_patch(circle)
        ax.text(pt[0], pt[1], symbol, fontsize=18, weight='bold', color=INK, ha='center', va='center', zorder=6)

    # Vertex labels outside circles
    ax.text(v_S[0], v_S[1] + 0.85, "Fixed mass: 32g", fontsize=14, ha='center', color=INK,
            bbox=dict(fc="white", ec="none", pad=0.1))
    ax.text(v_H[0] - 0.7, v_H[1], "2g H", fontsize=14, ha='right', va='center', color=INK)
    ax.text(v_O[0] + 0.7, v_O[1], "32g O", fontsize=14, ha='left', va='center', color=INK)

    # Ratio explanation note at the bottom
    summary_text = (
        "Ratio of masses of H and O combining with 32g S is 2 : 32 (or 1 : 16).\n"
        "In H₂O, the mass ratio of H to O is 2 : 16 = 1 : 8.\n"
        "Comparison of ratios: (1/16) : (1/8) = 1 : 2 (a simple whole-number ratio)."
    )
    ax.text(5.0, -0.2, summary_text, fontsize=14, ha='center', va='center', color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4", lw=1.2))

    save(fig, out)
