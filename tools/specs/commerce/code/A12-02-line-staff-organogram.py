from style import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Box styling helper
    def draw_box(x, y, w, h, text, bg_color=CREAM, border_color=INK):
        # centered at (x, y)
        rect = patches.FancyBboxPatch(
            (x - w / 2, y - h / 2), w, h,
            boxstyle="round,pad=0.1,rounding_size=0.15",
            facecolor=bg_color,
            edgecolor=border_color,
            linewidth=2,
            zorder=3
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=14, color=INK, weight='bold', zorder=4)

    # Coordinates
    top_x, top_y = 3.6, 5.8
    staff_x, staff_y = 7.0, 4.4
    prod_x, prod_y = 3.6, 3.0
    sup_y = 1.2
    sup_x1, sup_x2 = 2.1, 5.1

    box_w, box_h = 3.2, 0.8
    staff_w, staff_h = 2.6, 0.8
    sup_w, sup_h = 2.2, 0.7

    # Connectors
    # Line authority: MD to PM
    ax.plot([top_x, top_x], [top_y - box_h/2, prod_y + box_h/2], color=INK, lw=2.5, zorder=1)

    # Staff authority: junction to Legal Adviser
    junction_y = (top_y - box_h/2 + prod_y + box_h/2) / 2
    ax.plot([top_x, staff_x - staff_w/2], [junction_y, junction_y], color=DEEP["blue"], lw=2.5, linestyle='--', zorder=1)

    # Line authority: PM to Supervisors
    mid_sup_y = 2.1
    ax.plot([prod_x, prod_x], [prod_y - box_h/2, mid_sup_y], color=INK, lw=2.5, zorder=1)
    ax.plot([sup_x1, sup_x2], [mid_sup_y, mid_sup_y], color=INK, lw=2.5, zorder=1)
    ax.plot([sup_x1, sup_x1], [mid_sup_y, sup_y + sup_h/2], color=INK, lw=2.5, zorder=1)
    ax.plot([sup_x2, sup_x2], [mid_sup_y, sup_y + sup_h/2], color=INK, lw=2.5, zorder=1)

    # Draw boxes
    draw_box(top_x, top_y, box_w, box_h, "Managing Director", bg_color=CREAM)
    draw_box(staff_x, junction_y, staff_w, staff_h, "Legal Adviser\n(Staff)", bg_color=LAV, border_color=DEEP["blue"])
    draw_box(prod_x, prod_y, box_w, box_h, "Production Manager", bg_color=CREAM)
    draw_box(sup_x1, sup_y, sup_w, sup_h, "Supervisors", bg_color=CREAM)
    draw_box(sup_x2, sup_y, sup_w, sup_h, "Supervisors", bg_color=CREAM)

    # Title
    ax.text(4.5, 6.6, "Line and Staff Organogram", ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # Legend / Labels
    # Line authority legend
    leg_y1 = 0.4
    ax.plot([1.2, 2.2], [leg_y1, leg_y1], color=INK, lw=2.5)
    ax.text(2.4, leg_y1, "Line Authority (solid line)", ha='left', va='center', fontsize=14, color=INK)

    # Staff authority legend
    leg_y2 = 0.4
    ax.plot([5.5, 6.5], [leg_y2, leg_y2], color=DEEP["blue"], lw=2.5, linestyle='--')
    ax.text(6.7, leg_y2, "Staff/Advisory Authority (dashed line)", ha='left', va='center', fontsize=14, color=INK)

    save(fig, out)
