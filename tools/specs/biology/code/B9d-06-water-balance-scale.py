from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_teardrop(ax, cx, cy, rx, ry, fc=BLUE, ec=DEEP["blue"]):
    """Smooth, robust teardrop / water drop shape drawn using explicit perimeter points."""
    # Bottom half is a semicircle, top tapers smoothly to a point
    t = np.linspace(-np.pi / 2, 3 * np.pi / 2, 100)
    # Parametric drop: rounded bottom (y < 0) and pointed apex (y > 0)
    xs = cx + rx * np.cos(t) * (1 - 0.5 * np.sin(t))
    ys = cy + ry * np.sin(t)
    poly = patches.Polygon(np.column_stack([xs, ys]), closed=True,
                           facecolor=fc, edgecolor=ec, lw=1.5, zorder=3)
    ax.add_patch(poly)

def draw_mini_drop(ax, cx, cy, rx, ry, fc, ec):
    t = np.linspace(-np.pi / 2, 3 * np.pi / 2, 40)
    xs = cx + rx * np.cos(t) * (1 - 0.5 * np.sin(t))
    ys = cy + ry * np.sin(t)
    poly = patches.Polygon(np.column_stack([xs, ys]), closed=True,
                           facecolor=fc, edgecolor=ec, lw=1.0, zorder=5)
    ax.add_patch(poly)

def draw(out):
    fig = canvas(12, 7.5)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # Title
    ax.text(6.0, 7.05, "Daily Water Balance in Humans", ha="center", va="center",
            fontsize=17, fontweight="bold", color=INK)

    # Scale Base and Stand
    base = patches.Polygon([[5.2, 1.3], [6.8, 1.3], [6.18, 3.2], [5.82, 3.2]],
                           closed=True, facecolor=GREY, edgecolor=INK, lw=2, zorder=2)
    ax.add_patch(base)
    # Ground support bar
    ax.plot([4.8, 7.2], [1.3, 1.3], color=INK, lw=3, solid_capstyle="round")

    # Central pivot / vertical pillar
    ax.plot([6.0, 6.0], [3.2, 4.3], color=INK, lw=4, solid_capstyle="round", zorder=2)
    # Pivot joint circle
    ax.plot(6.0, 4.3, marker='o', markersize=9, color=DEEP["blue"],
            markeredgecolor=INK, markeredgewidth=2, zorder=5)

    # Balance beam (perfectly level)
    beam_y = 4.3
    ax.plot([2.5, 9.5], [beam_y, beam_y], color=INK, lw=4, solid_capstyle="round", zorder=3)

    # Pans and hanger strings
    pan_rim_y = 2.6
    pan_w = 3.8
    pan_depth = 0.5

    for px in [2.5, 9.5]:
        left_edge = px - pan_w / 2
        right_edge = px + pan_w / 2
        ax.plot([px, left_edge + 0.15], [beam_y, pan_rim_y], color=GREY, lw=1.6, zorder=2)
        ax.plot([px, right_edge - 0.15], [beam_y, pan_rim_y], color=GREY, lw=1.6, zorder=2)

        t_pan = np.linspace(np.pi, 2 * np.pi, 50)
        pxs = px + (pan_w / 2) * np.cos(t_pan)
        pys = pan_rim_y + pan_depth * np.sin(t_pan)
        ax.fill(pxs, pys, color=CREAM, zorder=2)
        ax.plot(pxs, pys, color=INK, lw=2.2, zorder=3)
        ax.plot([left_edge, right_edge], [pan_rim_y, pan_rim_y], color=INK, lw=2.5, zorder=3)

    # Category Headers
    ax.text(2.5, 5.8, "water gained", ha="center", va="center",
            fontsize=15, fontweight="bold", color=DEEP["blue"],
            bbox=dict(fc=BLUE, ec=DEEP["blue"], boxstyle="round,pad=0.35", lw=1.5))
    ax.text(2.5, 5.3, "Total input: ~2500 mL/day", ha="center", va="center",
            fontsize=11.5, color=INK, style="italic")

    ax.text(9.5, 5.8, "water lost", ha="center", va="center",
            fontsize=15, fontweight="bold", color=DEEP["orange"],
            bbox=dict(fc=CREAM, ec=DEEP["orange"], boxstyle="round,pad=0.35", lw=1.5))
    ax.text(9.5, 5.3, "Total output: ~2500 mL/day", ha="center", va="center",
            fontsize=11.5, color=INK, style="italic")

    # Center label: gain equals loss
    ax.text(6.0, 2.3, "gain equals loss", ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=DEEP["green"],
            bbox=dict(fc=GREEN, ec=DEEP["green"], boxstyle="round,pad=0.35", lw=1.5))

    # --- LEFT PAN: 3 Sources (drinks, food, metabolic water) ---
    left_items = [
        {"x": 1.35, "name": "drinks", "sub": "(liquids)\n~1500 mL", "icon": "cup"},
        {"x": 2.5, "name": "food", "sub": "(water in food)\n~750 mL", "icon": "food"},
        {"x": 3.65, "name": "metabolic\nwater", "sub": "(respiration)\n~250 mL", "icon": "flame"},
    ]

    for item in left_items:
        cx = item["x"]
        drop_cy = 3.6
        draw_teardrop(ax, cx, drop_cy, 0.42, 0.52, fc=BLUE, ec=DEEP["blue"])

        if item["icon"] == "cup":
            ax.plot([cx - 0.16, cx - 0.12, cx + 0.12, cx + 0.16],
                    [drop_cy + 0.08, drop_cy - 0.14, drop_cy - 0.14, drop_cy + 0.08],
                    color=INK, lw=1.4, zorder=4)
            ax.plot([cx + 0.15, cx + 0.22, cx + 0.13],
                    [drop_cy + 0.04, drop_cy - 0.03, drop_cy - 0.1],
                    color=INK, lw=1.3, zorder=4)
        elif item["icon"] == "food":
            ax.plot([cx - 0.22, cx + 0.22], [drop_cy - 0.08, drop_cy - 0.08],
                    color=INK, lw=1.5, zorder=4)
            t_food = np.linspace(0, np.pi, 20)
            ax.plot(cx + 0.16 * np.cos(t_food), drop_cy - 0.08 + 0.12 * np.sin(t_food),
                    color=DEEP["orange"], lw=1.6, zorder=4)
        elif item["icon"] == "flame":
            cell = patches.Circle((cx, drop_cy - 0.02), 0.16, facecolor="white",
                                  edgecolor=DEEP["green"], lw=1.3, zorder=4)
            ax.add_patch(cell)
            ax.plot([cx, cx - 0.06, cx, cx + 0.06, cx],
                    [drop_cy - 0.12, drop_cy - 0.02, drop_cy + 0.1, drop_cy - 0.02, drop_cy - 0.12],
                    color=DEEP["orange"], lw=1.5, zorder=5)

        ax.text(cx, 2.05, item["name"], ha="center", va="top",
                fontsize=11.5, fontweight="bold", color=INK)
        ax.text(cx, 1.45, item["sub"], ha="center", va="top",
                fontsize=9.5, color=GREY)

    # --- RIGHT PAN: 4 Routes (urine, sweat, exhaled air, faeces) ---
    right_items = [
        {"x": 8.05, "name": "urine", "sub": "(kidneys)\n~1500 mL", "icon": "urine"},
        {"x": 9.0, "name": "sweat", "sub": "(skin)\n~500 mL", "icon": "sweat"},
        {"x": 9.95, "name": "exhaled\nair", "sub": "(lungs)\n~400 mL", "icon": "air"},
        {"x": 10.9, "name": "faeces", "sub": "(gut)\n~100 mL", "icon": "faeces"},
    ]

    for item in right_items:
        cx = item["x"]
        drop_cy = 3.6
        draw_teardrop(ax, cx, drop_cy, 0.36, 0.48, fc=CREAM, ec=DEEP["orange"])

        if item["icon"] == "urine":
            ax.plot([cx - 0.06, cx - 0.06, cx - 0.13, cx + 0.13, cx + 0.06, cx + 0.06],
                    [drop_cy + 0.12, drop_cy + 0.03, drop_cy - 0.12, drop_cy - 0.12, drop_cy + 0.03, drop_cy + 0.12],
                    color=INK, lw=1.3, zorder=4)
        elif item["icon"] == "sweat":
            # Sweat droplets on skin
            ax.plot([cx - 0.18, cx + 0.18], [drop_cy - 0.08, drop_cy - 0.08],
                    color=INK, lw=1.4, zorder=4)
            # tiny droplets
            draw_mini_drop(ax, cx - 0.08, drop_cy - 0.02, 0.03, 0.05, fc=BLUE, ec=DEEP["blue"])
            draw_mini_drop(ax, cx + 0.08, drop_cy + 0.03, 0.03, 0.05, fc=BLUE, ec=DEEP["blue"])
            draw_mini_drop(ax, cx, drop_cy - 0.05, 0.04, 0.06, fc=BLUE, ec=DEEP["blue"])
        elif item["icon"] == "air":
            # Face profile breathing out
            ax.plot([cx - 0.05, cx - 0.1, cx - 0.1, cx - 0.05, cx - 0.08, cx - 0.12, cx - 0.12],
                    [drop_cy + 0.15, drop_cy + 0.1, drop_cy - 0.02, drop_cy - 0.02, drop_cy - 0.07, drop_cy - 0.12, drop_cy - 0.18],
                    color=INK, lw=1.2, zorder=4)
            # Vapour clouds
            for dy in [0.0, 0.06, -0.06]:
                ax.plot([cx - 0.02, cx + 0.1], [drop_cy + dy, drop_cy + dy + 0.02], color=DEEP["blue"], lw=1.2, linestyle='--', zorder=4)
        elif item["icon"] == "faeces":
            # Simple poop icon (coiled shape)
            t_p = np.linspace(0, np.pi, 20)
            ax.fill_between(cx + 0.14 * np.cos(t_p), drop_cy - 0.12, drop_cy - 0.12 + 0.08 * np.sin(t_p), color=DEEP["orange"], zorder=4)
            ax.fill_between(cx + 0.10 * np.cos(t_p), drop_cy - 0.04, drop_cy - 0.04 + 0.07 * np.sin(t_p), color=DEEP["orange"], zorder=5)
            ax.fill_between(cx + 0.06 * np.cos(t_p), drop_cy + 0.03, drop_cy + 0.03 + 0.06 * np.sin(t_p), color=DEEP["orange"], zorder=6)
            # Outline
            ax.plot(cx + 0.14 * np.cos(t_p), drop_cy - 0.12 + 0.08 * np.sin(t_p), color=INK, lw=1, zorder=4)
            ax.plot(cx + 0.10 * np.cos(t_p), drop_cy - 0.04 + 0.07 * np.sin(t_p), color=INK, lw=1, zorder=5)
            ax.plot(cx + 0.06 * np.cos(t_p), drop_cy + 0.03 + 0.06 * np.sin(t_p), color=INK, lw=1, zorder=6)

        ax.text(cx, 2.05, item["name"], ha="center", va="top",
                fontsize=11.5, fontweight="bold", color=INK)
        ax.text(cx, 1.45, item["sub"], ha="center", va="top",
                fontsize=9.5, color=GREY)

    # Bottom summary box
    ax.text(6.0, 0.55,
            "Homeostasis keeps total daily intake equal to total daily output (~2500 mL/day).",
            ha="center", va="center", fontsize=11.5, color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.35", lw=1.0))

    save(fig, out)
