from style import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    # Set limits
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4.5, 5.5)

    # Origin
    ox, oy = 0.0, 0.0

    # Angles for forces: F1, F2, F3
    # Lami's theorem: F1 / sin(alpha) = F2 / sin(beta) = F3 / sin(gamma)
    # where alpha is opposite F1 (between F2 and F3),
    # beta is opposite F2 (between F1 and F3),
    # gamma is opposite F3 (between F1 and F2).
    # Let's set directions (in degrees):
    # F1 pointing upwards and slightly right: 90 deg
    # F2 pointing downwards and left: 215 deg
    # F3 pointing downwards and right: 330 deg (-30 deg)
    theta1 = 90.0
    theta2 = 215.0
    theta3 = 330.0

    # Lengths of forces for visual balance
    r1, r2, r3 = 3.6, 3.4, 3.2

    # Vector coordinates
    v1 = np.array([r1 * np.cos(np.radians(theta1)), r1 * np.sin(np.radians(theta1))])
    v2 = np.array([r2 * np.cos(np.radians(theta2)), r2 * np.sin(np.radians(theta2))])
    v3 = np.array([r3 * np.cos(np.radians(theta3)), r3 * np.sin(np.radians(theta3))])

    # Draw force arrows
    arrow_props = dict(arrowstyle="-|>", mutation_scale=22, lw=3.0)
    
    # F1
    ax.annotate("", xy=v1, xytext=(ox, oy),
                arrowprops=dict(**arrow_props, color=DEEP["blue"]))
    # F2
    ax.annotate("", xy=v2, xytext=(ox, oy),
                arrowprops=dict(**arrow_props, color=DEEP["orange"]))
    # F3
    ax.annotate("", xy=v3, xytext=(ox, oy),
                arrowprops=dict(**arrow_props, color=DEEP["green"]))

    # Central point
    ax.plot(ox, oy, "o", color=INK, markersize=7, zorder=5)

    # Angle arcs:
    # gamma: between F1 (90) and F2 (215) -> span 125 deg
    # alpha: between F2 (215) and F3 (330) -> span 115 deg
    # beta: between F3 (330) and F1 (90 = 450) -> span 120 deg

    r_gamma = 1.3
    arc_gamma = Arc((ox, oy), 2*r_gamma, 2*r_gamma, angle=0, theta1=90, theta2=215,
                    color=INK, lw=1.8, ls="--")
    ax.add_patch(arc_gamma)

    r_alpha = 1.4
    arc_alpha = Arc((ox, oy), 2*r_alpha, 2*r_alpha, angle=0, theta1=215, theta2=330,
                    color=INK, lw=1.8, ls="--")
    ax.add_patch(arc_alpha)

    r_beta = 1.5
    arc_beta = Arc((ox, oy), 2*r_beta, 2*r_beta, angle=0, theta1=330, theta2=450,
                   color=INK, lw=1.8, ls="--")
    ax.add_patch(arc_beta)

    # Label positions for angles (mid-angles)
    mid_gamma = np.radians((90 + 215) / 2.0)
    mid_alpha = np.radians((215 + 330) / 2.0)
    mid_beta = np.radians((330 + 450) / 2.0)

    # Place angle labels
    bbox_style = dict(fc="white", ec="none", pad=1.5)
    ax.text((r_gamma + 0.45) * np.cos(mid_gamma), (r_gamma + 0.45) * np.sin(mid_gamma),
            r"$\gamma$", fontsize=18, color=INK, ha="center", va="center", bbox=bbox_style)

    ax.text((r_alpha + 0.45) * np.cos(mid_alpha), (r_alpha + 0.45) * np.sin(mid_alpha),
            r"$\alpha$", fontsize=18, color=INK, ha="center", va="center", bbox=bbox_style)

    ax.text((r_beta + 0.45) * np.cos(mid_beta), (r_beta + 0.45) * np.sin(mid_beta),
            r"$\beta$", fontsize=18, color=INK, ha="center", va="center", bbox=bbox_style)

    # Labels for forces
    ax.text(v1[0], v1[1] + 0.4, r"$F_1$", fontsize=18, color=DEEP["blue"],
            ha="center", va="bottom", weight="bold", bbox=bbox_style)
    ax.text(v2[0] - 0.4, v2[1] - 0.2, r"$F_2$", fontsize=18, color=DEEP["orange"],
            ha="right", va="top", weight="bold", bbox=bbox_style)
    ax.text(v3[0] + 0.4, v3[1] - 0.2, r"$F_3$", fontsize=18, color=DEEP["green"],
            ha="left", va="top", weight="bold", bbox=bbox_style)

    # Formula box for Lami's Theorem at the bottom
    formula_text = r"$\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}$"
    ax.text(0, -3.8, formula_text, fontsize=17, color=INK, ha="center", va="center",
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.5", lw=1.2))

    # Title
    ax.text(0, 4.8, "Lami's Theorem", fontsize=18, color=INK, ha="center", va="center", weight="bold")

    save(fig, out)
