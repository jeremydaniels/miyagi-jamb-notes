from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 7)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Divider line
    ax.plot([6, 6], [0.8, 6.2], color=GREY, lw=1.5, linestyle="--")

    # --- LEFT SIDE: Centralized State (Pyramid) ---
    ax.text(3, 6.3, "Centralized State", ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Pyramid tiers (from top to bottom)
    # Apex at (3, 5.5), base y=1.2, height = 4.3, half_width at base = 2.4
    # Levels:
    # 1. King (top): y from 4.5 to 5.5
    # 2. Council of Chiefs: y from 3.4 to 4.5
    # 3. Regional Governors: y from 2.3 to 3.4
    # 4. Common People (base): y from 1.2 to 2.3

    y_levels = [5.5, 4.4, 3.3, 2.2, 1.1]
    labels_left = [
        "King",
        "Council of Chiefs",
        "Regional Governors",
        "Common People"
    ]
    colors_left = [PINK, ORANGE, LAV, BLUE]
    deep_left = [DEEP["pink"], DEEP["orange"], DEEP["lav"], DEEP["blue"]]

    apex_x, apex_y = 3.0, 5.5
    base_w = 2.4
    tot_h = apex_y - 1.1

    for i in range(4):
        y_top = y_levels[i]
        y_bot = y_levels[i+1]
        
        # calculate half widths
        w_top = base_w * (apex_y - y_top) / tot_h
        w_bot = base_w * (apex_y - y_bot) / tot_h

        if i == 0:
            pts = np.array([
                [apex_x, apex_y],
                [apex_x + w_bot, y_bot],
                [apex_x - w_bot, y_bot]
            ])
        else:
            pts = np.array([
                [apex_x - w_top, y_top],
                [apex_x + w_top, y_top],
                [apex_x + w_bot, y_bot],
                [apex_x - w_bot, y_bot]
            ])

        poly = patches.Polygon(pts, closed=True, facecolor=colors_left[i], edgecolor=deep_left[i], lw=2)
        ax.add_patch(poly)

        # Label position
        y_text = (y_top + y_bot) / 2.0
        ax.text(apex_x, y_text, labels_left[i], ha="center", va="center", fontsize=14, weight="bold", color=INK)

    # Hierarchy arrow on left
    ax.annotate("", xy=(0.4, 5.2), xytext=(0.4, 1.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.text(0.2, 3.3, "Hierarchical Authority", rotation=90, ha="center", va="center", fontsize=14, color=INK)

    # --- RIGHT SIDE: Acephalous Society (Network) ---
    ax.text(9, 6.3, "Acephalous Society", ha="center", va="center", fontsize=18, weight="bold", color=INK)

    # Center is (9, 3.3)
    # Center node: Council of Elders
    # Surrounding nodes: Family A, Family B, Age Grades, and additional kin groups to show interconnectedness
    nodes = {
        "Council of Elders": (9.0, 3.3, CREAM, DEEP["orange"], 0.95),
        "Family A": (6.9, 4.6, GREEN, DEEP["green"], 0.8),
        "Family B": (11.1, 4.6, BLUE, DEEP["blue"], 0.8),
        "Age Grades": (9.0, 1.5, LAV, DEEP["lav"], 0.85),
        "Family C": (7.1, 2.2, PINK, DEEP["pink"], 0.75),
        "Family D": (10.9, 2.2, GREEN, DEEP["green"], 0.75)
    }

    # Connections (undirected network of equal peer relations)
    edges = [
        ("Council of Elders", "Family A"),
        ("Council of Elders", "Family B"),
        ("Council of Elders", "Age Grades"),
        ("Council of Elders", "Family C"),
        ("Council of Elders", "Family D"),
        ("Family A", "Family B"),
        ("Family A", "Family C"),
        ("Family B", "Family D"),
        ("Family C", "Age Grades"),
        ("Family D", "Age Grades")
    ]

    for start, end in edges:
        p1 = nodes[start]
        p2 = nodes[end]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=GREY, lw=2.2, zorder=1)

    for name, (nx, ny, bg_col, edge_col, radius) in nodes.items():
        # Draw circle
        circle = patches.Circle((nx, ny), radius=radius, facecolor=bg_col, edgecolor=edge_col, lw=2, zorder=2)
        ax.add_patch(circle)

        # Draw label
        if name == "Council of Elders":
            label_text = "Council of\nElders"
            fsize = 14
        elif name == "Age Grades":
            label_text = "Age\nGrades"
            fsize = 14
        elif "Family" in name and name not in ["Family A", "Family B"]:
            label_text = name
            fsize = 13
        else:
            label_text = name.replace(" ", "\n")
            fsize = 14

        ax.text(nx, ny, label_text, ha="center", va="center", fontsize=fsize, weight="bold", color=INK, zorder=3)

    save(fig, out)
