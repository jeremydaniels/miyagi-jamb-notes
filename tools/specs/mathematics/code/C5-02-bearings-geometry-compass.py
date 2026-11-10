from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(8, 8)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Center A at (0, 0)
    # Axes lines (N-S and E-W cross)
    axis_len = 4.0
    ax.annotate("", xy=(0, axis_len), xytext=(0, -axis_len),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0))
    ax.annotate("", xy=(axis_len, 0), xytext=(-axis_len, 0),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0))
    # Add backwards arrows for S and W
    ax.annotate("", xy=(0, -axis_len), xytext=(0, axis_len),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0))
    ax.annotate("", xy=(-axis_len, 0), xytext=(axis_len, 0),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=2.0))

    # Cardinal labels
    bbox_cardinal = dict(boxstyle="circle,pad=0.2", fc="white", ec="none")
    ax.text(0, axis_len + 0.35, "N", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, bbox=bbox_cardinal)
    ax.text(0, -axis_len - 0.35, "S", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, bbox=bbox_cardinal)
    ax.text(axis_len + 0.35, 0, "E", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, bbox=bbox_cardinal)
    ax.text(-axis_len - 0.35, 0, "W", ha="center", va="center", fontsize=16, fontweight="bold", color=INK, bbox=bbox_cardinal)

    # Line AB to South-East quadrant
    # Bearing 120° clockwise from North corresponds to mathematical angle: 90 - 120 = -30° (or 330°)
    theta_deg = -30
    theta_rad = np.radians(theta_deg)
    line_len = 4.2
    bx = line_len * np.cos(theta_rad)
    by = line_len * np.sin(theta_rad)

    # Plot line AB
    ax.plot([0, bx], [0, by], color=DEEP["blue"], lw=3.0, zorder=3)

    # Point A
    ax.plot(0, 0, marker="o", color=INK, markersize=8, zorder=5)
    ax.text(-0.35, 0.35, "A", fontsize=16, fontweight="bold", color=INK, ha="right", va="bottom")

    # Point B
    ax.plot(bx, by, marker="o", color=DEEP["blue"], markersize=8, zorder=5)
    ax.text(bx + 0.3, by - 0.2, "B", fontsize=16, fontweight="bold", color=DEEP["blue"], ha="left", va="center")

    # 1) True bearing: North (90°) clockwise to AB (-30°)
    # In standard angles: from 90° down to -30° (arc from 330° to 90° going ccw, but arrow goes cw from 90 to 330)
    r_true = 2.2
    t_true = np.linspace(np.radians(90), np.radians(-30), 100)
    ax.plot(r_true * np.cos(t_true), r_true * np.sin(t_true), color=DEEP["pink"], lw=2.2, zorder=4)

    # Arrowhead at 120° line pointing clockwise (direction tangent is [sin(theta), -cos(theta)] for clockwise at -30°)
    # Tangent to arc at -30° heading clockwise: (sin(-30°), -cos(-30°)) = (-0.5, -0.866)
    tip_x = r_true * np.cos(np.radians(-30))
    tip_y = r_true * np.sin(np.radians(-30))
    ax.annotate("", xy=(tip_x, tip_y),
                xytext=(tip_x - 0.15 * np.sin(np.radians(-30)), tip_y - 0.15 * (-np.cos(np.radians(-30)))),
                arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=2.5, mutation_scale=18),
                zorder=5)

    # True bearing label
    # Position along the arc (~30° standard angle)
    lbl_angle = np.radians(35)
    lbl_x = (r_true + 0.6) * np.cos(lbl_angle)
    lbl_y = (r_true + 0.6) * np.sin(lbl_angle)
    ax.text(lbl_x + 0.2, lbl_y + 0.2, "120° (True Bearing)",
            fontsize=14, color=DEEP["pink"], fontweight="bold", ha="left", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["pink"], lw=1.2))

    # 2) Compass bearing: South (-90° / 270°) counter-clockwise towards East to line AB (-30° / 330°)
    # This angle is 60°
    r_comp = 1.3
    t_comp = np.linspace(np.radians(-90), np.radians(-30), 60)
    ax.plot(r_comp * np.cos(t_comp), r_comp * np.sin(t_comp), color=DEEP["green"], lw=2.2, zorder=4)

    # Arrowhead at AB pointing counter-clockwise (towards line AB from South)
    # Tangent at -30° heading ccw: (-sin(-30°), cos(-30°)) = (0.5, 0.866)
    tip2_x = r_comp * np.cos(np.radians(-30))
    tip2_y = r_comp * np.sin(np.radians(-30))
    ax.annotate("", xy=(tip2_x, tip2_y),
                xytext=(tip2_x - 0.15 * (-np.sin(np.radians(-30))), tip2_y - 0.15 * np.cos(np.radians(-30))),
                arrowprops=dict(arrowstyle="->", color=DEEP["green"], lw=2.5, mutation_scale=18),
                zorder=5)

    # Compass bearing label
    c_lbl_angle = np.radians(-60)
    c_lbl_x = (r_comp + 0.45) * np.cos(c_lbl_angle)
    c_lbl_y = (r_comp + 0.45) * np.sin(c_lbl_angle)
    ax.text(c_lbl_x + 0.1, c_lbl_y, "60°\n(S60°E)",
            fontsize=14, color=DEEP["green"], fontweight="bold", ha="left", va="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP["green"], lw=1.2))

    save(fig, out)
