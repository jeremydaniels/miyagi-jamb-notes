from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(11, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 7.0, "Matrix Organisational Structure", ha='center', va='center',
            fontsize=17, fontweight='bold', color=INK)

    # Columns: functional managers
    col_x = [4.3, 6.7, 9.1]
    func_titles = ['Production\nManager', 'Marketing\nManager', 'Finance\nManager']
    func_colors = [BLUE, GREEN, ORANGE]
    func_edge_colors = [DEEP['blue'], DEEP['green'], DEEP['orange']]

    # Rows: project managers
    row_y = [4.1, 1.9]
    proj_titles = ['Project A\nManager', 'Project B\nManager']
    proj_colors = [LAV, PINK]
    proj_edge_colors = [DEEP['lav'], DEEP['pink']]

    box_w = 1.9
    box_h = 1.05

    # Draw Top Functional Manager Boxes
    top_y = 5.8
    for x, title, bg_col, edge_col in zip(col_x, func_titles, func_colors, func_edge_colors):
        rect = patches.FancyBboxPatch((x - box_w/2, top_y - box_h/2), box_w, box_h,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=bg_col, edgecolor=edge_col, lw=2.0)
        ax.add_patch(rect)
        ax.text(x, top_y, title, ha='center', va='center', fontsize=14, fontweight='bold', color=INK)

    # Draw Left Project Manager Boxes
    proj_x = 1.6
    for y, title, bg_col, edge_col in zip(row_y, proj_titles, proj_colors, proj_edge_colors):
        rect = patches.FancyBboxPatch((proj_x - box_w/2, y - box_h/2), box_w, box_h,
                                      boxstyle="round,pad=0.08,rounding_size=0.15",
                                      facecolor=bg_col, edgecolor=edge_col, lw=2.0)
        ax.add_patch(rect)
        ax.text(proj_x, y, title, ha='center', va='center', fontsize=14, fontweight='bold', color=INK)

    # Intersection boxes (Team members)
    inter_w = 1.75
    inter_h = 0.95

    # Draw dashed reporting grid lines behind boxes
    for x in col_x:
        ax.plot([x, x], [top_y - box_h/2, 0.9], color=GREY, linestyle='-', lw=1.8, zorder=1)

    for y in row_y:
        ax.plot([proj_x + box_w/2, 10.3], [y, y], color=GREY, linestyle='-', lw=1.8, zorder=1)

    # Draw Intersections & Dual Arrows
    arrow_props = dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=12)

    for r_idx, y in enumerate(row_y):
        for c_idx, x in enumerate(col_x):
            # Intersection team box
            rect = patches.FancyBboxPatch((x - inter_w/2, y - inter_h/2), inter_w, inter_h,
                                          boxstyle="round,pad=0.05,rounding_size=0.12",
                                          facecolor=CREAM, edgecolor=INK, lw=1.6, zorder=3)
            ax.add_patch(rect)
            
            p_label = "Project A" if r_idx == 0 else "Project B"
            f_label = ["Prod.", "Mktg.", "Fin."][c_idx]
            ax.text(x, y + 0.15, f"{p_label}", ha='center', va='center', fontsize=14, fontweight='bold', color=INK, zorder=4)
            ax.text(x, y - 0.2, f"{f_label} Team", ha='center', va='center', fontsize=13, color=INK, zorder=4)

            # Upward reporting arrow (towards functional manager)
            # Arrow pointing UP to functional head from team box
            ax.annotate('', xy=(x, top_y - box_h/2 - 0.05), xytext=(x, y + inter_h/2 + 0.05),
                        arrowprops=arrow_props, zorder=2)

            # Leftward reporting arrow (towards project manager)
            # Arrow pointing LEFT from team box towards project manager
            target_left = proj_x + box_w/2 if c_idx == 0 else col_x[c_idx-1] + inter_w/2
            ax.annotate('', xy=(target_left + 0.05, y), xytext=(x - inter_w/2 - 0.05, y),
                        arrowprops=arrow_props, zorder=2)

    # Legend / explanatory note at the bottom
    legend_text = "Arrows show dual reporting lines: vertically to Functional Heads and horizontally to Project Managers."
    ax.text(5.5, 0.5, legend_text, ha='center', va='center', fontsize=13.5, style='italic', color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc='white', ec=GREY, lw=1.2))

    save(fig, out)
