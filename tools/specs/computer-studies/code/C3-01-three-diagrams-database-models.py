from style import *
import numpy as np

def draw(out):
    fig = canvas(18, 7.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 7.5)

    def draw_box(x, y, w, h, text, bg_color=CREAM, border_color=INK):
        rect = plt.Rectangle((x - w/2, y - h/2), w, h, facecolor=bg_color,
                             edgecolor=border_color, linewidth=2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=14, color=INK,
                weight='bold', zorder=4)

    # Section 1: Hierarchical Model
    ax.text(3.0, 6.8, "Hierarchical Model", ha='center', va='center',
            fontsize=17, weight='bold', color=INK)
    ax.text(3.0, 6.3, "1:N Tree Structure", ha='center', va='center',
            fontsize=14, color=GREY)

    # Parent Box
    draw_box(3.0, 5.0, 2.4, 0.9, "Root\n(Parent)", bg_color=BLUE, border_color=DEEP['blue'])

    # Children Boxes
    child_xs = [1.2, 3.0, 4.8]
    child_labels = ["Child A", "Child B", "Child C"]
    for cx, clbl in zip(child_xs, child_labels):
        draw_box(cx, 2.2, 1.5, 0.8, clbl, bg_color=CREAM, border_color=GREY)
        ax.annotate('', xy=(cx, 2.6), xytext=(3.0, 4.55),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=2.0,
                                    shrinkA=2, shrinkB=2))

    # Section 2: Network Model
    ax.text(9.0, 6.8, "Network Model", ha='center', va='center',
            fontsize=17, weight='bold', color=INK)
    ax.text(9.0, 6.3, "M:N Graph / Web Structure", ha='center', va='center',
            fontsize=14, color=GREY)

    # Two Parents / Owners
    p1 = (7.8, 5.0)
    p2 = (10.2, 5.0)
    draw_box(p1[0], p1[1], 1.8, 0.8, "Owner 1", bg_color=LAV, border_color=DEEP['lav'])
    draw_box(p2[0], p2[1], 1.8, 0.8, "Owner 2", bg_color=LAV, border_color=DEEP['lav'])

    # Three Members / Children with multiple connections
    m1 = (7.3, 2.2)
    m2 = (9.0, 2.2)
    m3 = (10.7, 2.2)
    draw_box(m1[0], m1[1], 1.5, 0.8, "Member 1", bg_color=CREAM, border_color=GREY)
    draw_box(m2[0], m2[1], 1.5, 0.8, "Member 2", bg_color=CREAM, border_color=GREY)
    draw_box(m3[0], m3[1], 1.5, 0.8, "Member 3", bg_color=CREAM, border_color=GREY)

    # Connections (many-to-many web)
    net_edges = [
        (p1, m1),
        (p1, m2),
        (p2, m2),
        (p2, m3),
        (p1, m3)
    ]
    for start, end in net_edges:
        ax.annotate('', xy=(end[0], end[1] + 0.4), xytext=(start[0], start[1] - 0.4),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.8,
                                    shrinkA=2, shrinkB=2))

    # Section 3: Relational Model
    ax.text(15.0, 6.8, "Relational Model", ha='center', va='center',
            fontsize=17, weight='bold', color=INK)
    ax.text(15.0, 6.3, "Tables linked by Foreign Key", ha='center', va='center',
            fontsize=14, color=GREY)

    # Table 1: Customers (Top)
    t1_x, t1_y = 12.8, 4.6
    c_w, r_h = 1.45, 0.48
    t1_headers = ["Cust_ID (PK)", "Name"]
    t1_rows = [
        ["101", "Alice"],
        ["102", "Bob"]
    ]
    
    # Title above Table 1
    ax.text(t1_x + c_w, t1_y + 0.9, "Customers Table", ha='center', va='center',
            fontsize=14, weight='bold', color=INK)

    # Header Row Table 1
    for j, h in enumerate(t1_headers):
        rect = plt.Rectangle((t1_x + j*c_w, t1_y), c_w, r_h, facecolor=GREEN,
                             edgecolor=INK, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(t1_x + j*c_w + c_w/2, t1_y + r_h/2, h, ha='center', va='center',
                fontsize=14, weight='bold', color=INK)
    # Data Rows Table 1
    for i, row in enumerate(t1_rows):
        ry = t1_y - (i + 1) * r_h
        for j, val in enumerate(row):
            rect = plt.Rectangle((t1_x + j*c_w, ry), c_w, r_h, facecolor='white',
                                 edgecolor=INK, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(t1_x + j*c_w + c_w/2, ry + r_h/2, val, ha='center', va='center',
                    fontsize=14, color=INK)

    # Table 2: Orders (Bottom)
    t2_x, t2_y = 12.8, 1.9
    t2_headers = ["Order_ID", "Cust_ID (FK)"]
    t2_rows = [
        ["#501", "101"],
        ["#502", "102"]
    ]

    # Title above Table 2
    ax.text(t2_x + c_w, t2_y + 0.9, "Orders Table", ha='center', va='center',
            fontsize=14, weight='bold', color=INK)

    # Header Row Table 2
    for j, h in enumerate(t2_headers):
        rect = plt.Rectangle((t2_x + j*c_w, t2_y), c_w, r_h, facecolor=ORANGE,
                             edgecolor=INK, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(t2_x + j*c_w + c_w/2, t2_y + r_h/2, h, ha='center', va='center',
                fontsize=14, weight='bold', color=INK)
    # Data Rows Table 2
    for i, row in enumerate(t2_rows):
        ry = t2_y - (i + 1) * r_h
        for j, val in enumerate(row):
            rect = plt.Rectangle((t2_x + j*c_w, ry), c_w, r_h, facecolor='white',
                                 edgecolor=INK, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(t2_x + j*c_w + c_w/2, ry + r_h/2, val, ha='center', va='center',
                    fontsize=14, color=INK)

    # Link from Foreign Key to Primary Key
    key_start = (t2_x + 1.5 * c_w, t2_y + r_h)
    key_end = (t1_x + 0.5 * c_w, t1_y - 0.5 * r_h)

    ax.annotate('', xy=key_end, xytext=key_start,
                arrowprops=dict(arrowstyle="->", color=DEEP['pink'], lw=2.5,
                                connectionstyle="arc3,rad=-0.4", shrinkA=4, shrinkB=4))
    ax.text(14.8, 3.2, "Foreign Key\nReference", ha='center', va='center',
            fontsize=14, color=DEEP['pink'], weight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=DEEP['pink'], lw=1.2))

    # Dividing dashed lines between sections
    ax.plot([6.0, 6.0], [0.8, 7.0], color=GREY, lw=1.5, linestyle="--")
    ax.plot([12.0, 12.0], [0.8, 7.0], color=GREY, lw=1.5, linestyle="--")

    save(fig, out)
