from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(13, 9)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9.5)
    ax.axis("off")

    # Pyramid center
    center_x = 4.2

    # Water background at base
    water_rect = patches.Rectangle((0.4, 0.4), 7.6, 0.9, facecolor=BLUE, edgecolor=DEEP["blue"],
                                   alpha=0.3, lw=1.5, linestyle="--", zorder=1)
    ax.add_patch(water_rect)
    ax.text(center_x, 0.85, "Water (very low DDT)", fontsize=13, weight="bold",
            color=DEEP["blue"], ha="center", va="center", zorder=3)
    
    # 2 sparse red dots in water
    ax.scatter([1.2, 7.2], [0.85, 0.85], color=DEEP["pink"], s=25, zorder=3)

    # Pyramid tiers definitions
    tiers = [
        {"y0": 1.5, "y1": 3.0, "w0": 7.4, "w1": 5.8, "name": "Plankton", "color": GREEN, "dots": 25, "dot_s": 20},
        {"y0": 3.2, "y1": 4.7, "w0": 5.6, "w1": 4.0, "name": "Small fish", "color": BLUE, "dots": 45, "dot_s": 24},
        {"y0": 4.9, "y1": 6.4, "w0": 3.8, "w1": 2.2, "name": "Large fish", "color": LAV, "dots": 70, "dot_s": 28},
        {"y0": 6.6, "y1": 8.5, "w0": 2.0, "w1": 0.5, "name": "Fish-eating bird\n(highest DDT)", "color": ORANGE, "dots": 95, "dot_s": 32}
    ]

    np.random.seed(42)

    for i, t in enumerate(tiers):
        y0, y1 = t["y0"], t["y1"]
        w0, w1 = t["w0"], t["w1"]
        x_bl, x_br = center_x - w0 / 2, center_x + w0 / 2
        x_tl, x_tr = center_x - w1 / 2, center_x + w1 / 2
        
        # Trapezoid polygon
        poly = patches.Polygon([[x_bl, y0], [x_br, y0], [x_tr, y1], [x_tl, y1]],
                               closed=True, facecolor=t["color"], edgecolor=GREY, lw=1.8, alpha=0.4, zorder=2)
        ax.add_patch(poly)

        # Red DDT dots inside the tier
        dots_placed = 0
        while dots_placed < t["dots"]:
            ry = np.random.uniform(y0 + 0.12, y1 - 0.12)
            frac = (ry - y0) / (y1 - y0)
            cur_w = (1 - frac) * w0 + frac * w1
            rx = np.random.uniform(center_x - cur_w / 2 + 0.12, center_x + cur_w / 2 - 0.12)
            ax.scatter(rx, ry, color=DEEP["pink"], s=t["dot_s"], alpha=0.85, edgecolors='none', zorder=4)
            dots_placed += 1

        # Tier Labels
        label_text = t["name"]
        
        # Adjust label placement for top tier so it doesn't obscure the bird graphic
        if i == 3:
            label_y = y1 + 0.35
        else:
            label_y = (y0 + y1) / 2
            
        ax.text(center_x, label_y, label_text, ha="center", va="center",
                fontsize=11.5, weight="bold", color=INK, zorder=6,
                bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25", alpha=0.9))

    # Helper function: draw a fish outline
    def draw_fish(cx, cy, length, height, flip=False, col=DEEP["blue"]):
        sgn = -1 if flip else 1
        t = np.linspace(0, 2 * np.pi, 60)
        # Body ellipse
        bx = cx + sgn * (length * 0.38) * np.cos(t)
        by = cy + (height * 0.5) * np.sin(t)
        ax.plot(bx, by, color=col, lw=1.6, zorder=5)
        ax.fill(bx, by, color="white", alpha=0.6, zorder=4.5)
        # Tail fin
        tx_base = cx - sgn * length * 0.38
        tx_tip = cx - sgn * length * 0.58
        ax.plot([tx_base, tx_tip, tx_tip, tx_base],
                [cy, cy + height * 0.6, cy - height * 0.6, cy],
                color=col, lw=1.6, zorder=5)
        ax.fill([tx_base, tx_tip, tx_tip, tx_base],
                [cy, cy + height * 0.6, cy - height * 0.6, cy],
                color="white", alpha=0.6, zorder=4.5)
        # Eye
        ax.scatter(cx + sgn * length * 0.22, cy + height * 0.12, color=INK, s=9, zorder=6)

    # Illustrations in tiers:
    # 1. Plankton in bottom tier (many tiny phytoplankton / zooplankton shapes)
    plankton_locs = [
        (1.2, 2.1), (1.8, 1.8), (2.2, 2.5), (2.8, 2.0),
        (5.6, 2.1), (6.2, 1.8), (6.6, 2.6), (7.1, 2.1),
        (3.0, 2.7), (5.3, 2.7)
    ]
    for px, py in plankton_locs:
        ax.scatter(px, py, marker='*', s=38, color=DEEP["green"], alpha=0.85, zorder=5)
        # Tiny radial hairs or ring around plankton
        ax.plot([px - 0.08, px + 0.08], [py, py], color=DEEP["green"], lw=0.9, zorder=5)
        ax.plot([px, px], [py - 0.08, py + 0.08], color=DEEP["green"], lw=0.9, zorder=5)

    # 2. Several small fish in tier 2 (y in [3.2, 4.7])
    draw_fish(2.1, 4.1, 0.7, 0.22, flip=False, col=DEEP["blue"])
    draw_fish(2.3, 3.5, 0.65, 0.20, flip=True, col=DEEP["blue"])
    draw_fish(6.1, 4.0, 0.7, 0.22, flip=True, col=DEEP["blue"])
    draw_fish(6.0, 3.4, 0.65, 0.20, flip=False, col=DEEP["blue"])

    # 3. Two larger fish in tier 3 (y in [4.9, 6.4])
    draw_fish(3.0, 5.8, 1.0, 0.35, flip=False, col=DEEP["lav"])
    draw_fish(5.4, 5.5, 1.0, 0.35, flip=True, col=DEEP["lav"])

    # 4. Fish-eating bird (osprey/eagle) silhouette/sketch in top tier
    # Draw flying raptor silhouette centered
    bx, by = center_x, 7.3
    wing_l_x = np.array([bx, bx - 0.25, bx - 0.55, bx - 0.75, bx - 0.5, bx - 0.2, bx])
    wing_l_y = np.array([by, by + 0.15, by + 0.22, by + 0.12, by + 0.02, by - 0.05, by])
    wing_r_x = 2 * bx - wing_l_x
    wing_r_y = wing_l_y
    ax.plot(wing_l_x, wing_l_y, color=INK, lw=1.8, zorder=6)
    ax.plot(wing_r_x, wing_r_y, color=INK, lw=1.8, zorder=6)
    ax.fill(wing_l_x, wing_l_y, color=INK, alpha=0.75, zorder=5.5)
    ax.fill(wing_r_x, wing_r_y, color=INK, alpha=0.75, zorder=5.5)
    # Head and beak
    ax.plot([bx, bx, bx + 0.08, bx], [by, by + 0.18, by + 0.13, by + 0.08], color=INK, lw=1.5, zorder=6)
    # Tail
    ax.fill([bx - 0.1, bx + 0.1, bx + 0.15, bx - 0.15], [by, by, by - 0.2, by - 0.2], color=INK, alpha=0.75, zorder=5.5)

    # Vertical Arrow showing biomagnification / concentration increase
    arrow_x = 8.1
    ax.annotate("", xy=(arrow_x, 8.2), xytext=(arrow_x, 1.3),
                arrowprops=dict(arrowstyle="-|>", lw=3.0, color=DEEP["pink"], mutation_scale=22), zorder=6)
    
    # 2-line annotation text next to arrow to prevent truncation
    ax.text(arrow_x + 0.25, 4.75, "DDT concentration increases\nup the food chain",
            va="center", ha="left", fontsize=12.5, weight="bold", color=DEEP["pink"])

    # Inset at the top right showing cracked thin eggshell in a nest
    inset_x, inset_y, inset_w, inset_h = 8.8, 6.0, 3.9, 3.2
    inset_box = patches.FancyBboxPatch((inset_x, inset_y), inset_w, inset_h,
                                        boxstyle="round,pad=0.1", fc=CREAM, ec=GREY, lw=1.5, zorder=7)
    ax.add_patch(inset_box)

    ax.text(inset_x + inset_w / 2, inset_y + inset_h - 0.35, "Thin, broken eggshell",
            fontsize=12, weight="bold", color=INK, ha="center", va="center", zorder=8)

    # Draw nest
    nest_cx = inset_x + inset_w / 2
    nest_cy = inset_y + 0.75
    # Twigs
    twig_angles = [-15, 12, -8, 18, -10, 5, -20]
    for idx, ta in enumerate(twig_angles):
        ox = (idx - 3) * 0.3
        rad = np.radians(ta)
        dx = 0.55 * np.cos(rad)
        dy = 0.55 * np.sin(rad)
        ax.plot([nest_cx + ox - dx, nest_cx + ox + dx],
                [nest_cy - 0.05 - dy, nest_cy - 0.05 + dy],
                color=DEEP["orange"], lw=2.2, zorder=8)
    
    nest_arc = patches.Arc((nest_cx, nest_cy + 0.15), 2.2, 0.9, angle=0, theta1=185, theta2=355,
                           color=DEEP["orange"], lw=3.2, zorder=8)
    ax.add_patch(nest_arc)

    # Draw cracked egg
    egg_cx, egg_cy = nest_cx, nest_cy + 0.65
    egg_patch = patches.Ellipse((egg_cx, egg_cy), 1.25, 1.55, facecolor="white", edgecolor=GREY, lw=2.0, zorder=9)
    ax.add_patch(egg_patch)

    # Jagged crack line on egg
    crack_x = [egg_cx - 0.25, egg_cx - 0.05, egg_cx - 0.18, egg_cx + 0.12, egg_cx + 0.02, egg_cx + 0.28]
    crack_y = [egg_cy + 0.55, egg_cy + 0.30, egg_cy + 0.05, egg_cy - 0.15, egg_cy - 0.38, egg_cy - 0.58]
    ax.plot(crack_x, crack_y, color=DEEP["pink"], lw=2.2, zorder=10)

    # Small crack branches
    ax.plot([egg_cx - 0.05, egg_cx + 0.15], [egg_cy + 0.30, egg_cy + 0.22], color=DEEP["pink"], lw=1.8, zorder=10)
    ax.plot([egg_cx - 0.18, egg_cx - 0.35], [egg_cy + 0.05, egg_cy + 0.0], color=DEEP["pink"], lw=1.8, zorder=10)

    # Connecting dashed line from top tier (bird) to inset
    ax.annotate("", xy=(inset_x, 7.3), xytext=(center_x + 0.8, 7.3),
                arrowprops=dict(arrowstyle="->", lw=1.5, color=GREY, linestyle="--"), zorder=6)

    save(fig, out)
