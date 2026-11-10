from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    # Canvas setup - tall layout for vertical progression of 6 levels
    fig = canvas(11, 14)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 14)
    ax.axis("off")

    # Title & subtitle
    ax.text(5.5, 13.5, "Levels of Ecological Organisation", 
            ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
    ax.text(5.5, 13.15, "From individual organism to the global biosphere", 
            ha="center", va="center", fontsize=12, color=GREY, style="italic")

    # Box specifications: 6 panels arranged vertically from top (organism) to bottom (biosphere)
    # Each level grows wider to reflect expanding scale (nested ladder concept)
    levels = [
        {"name": "organism", "w": 4.6, "h": 1.45, "y": 11.35},
        {"name": "population", "w": 5.4, "h": 1.45, "y": 9.35},
        {"name": "community", "w": 6.2, "h": 1.45, "y": 7.35},
        {"name": "ecosystem", "w": 7.0, "h": 1.45, "y": 5.35},
        {"name": "biome", "w": 7.8, "h": 1.45, "y": 3.35},
        {"name": "biosphere", "w": 8.6, "h": 1.45, "y": 1.35}
    ]

    # Draw vertical connecting arrows between panels
    for i in range(len(levels) - 1):
        y_from = levels[i]["y"]
        y_to = levels[i+1]["y"] + levels[i+1]["h"]
        ax.annotate("", xy=(5.5, y_to), xytext=(5.5, y_from),
                    arrowprops=dict(arrowstyle="->", lw=2.2, color=DEEP["blue"],
                                   mutation_scale=16))

    # Helper function to draw a clear Tilapia fish
    def draw_tilapia(cx, cy, s=1.0, color=DEEP["blue"], body_fc=BLUE):
        body = patches.Ellipse((cx, cy), 0.55 * s, 0.28 * s, facecolor=body_fc, edgecolor=color, lw=1.5, zorder=4)
        ax.add_patch(body)
        tail = patches.Polygon([[cx - 0.25*s, cy], [cx - 0.42*s, cy + 0.16*s], [cx - 0.42*s, cy - 0.16*s]],
                               closed=True, facecolor=body_fc, edgecolor=color, lw=1.2, zorder=4)
        ax.add_patch(tail)
        dorsal = patches.Polygon([[cx - 0.15*s, cy + 0.12*s], [cx + 0.05*s, cy + 0.22*s], [cx + 0.16*s, cy + 0.1*s]],
                                 closed=True, facecolor=body_fc, edgecolor=color, lw=1.2, zorder=4)
        ax.add_patch(dorsal)
        ax.plot(cx + 0.16*s, cy + 0.04*s, 'o', color=INK, markersize=3.5*s, zorder=5)
        ax.plot([cx - 0.12*s, cx + 0.08*s], [cy, cy], lw=1.2, color=color, zorder=5)

    # 1. ORGANISM
    b1 = levels[0]
    rect1 = patches.FancyBboxPatch((5.5 - b1["w"]/2, b1["y"]), b1["w"], b1["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#f0f7f4", edgecolor=DEEP["green"], lw=1.8)
    ax.add_patch(rect1)
    ax.text(5.5 - b1["w"]/2 + 0.35, b1["y"] + b1["h"] - 0.35, "organism",
            fontsize=14, fontweight="bold", color=DEEP["green"], ha="left")
    ax.text(5.5 - b1["w"]/2 + 0.35, b1["y"] + 0.3, "Single Tilapia fish",
            fontsize=11, color=INK, ha="left")
    draw_tilapia(5.5 + 1.1, b1["y"] + b1["h"]/2, s=1.45)

    # 2. POPULATION
    b2 = levels[1]
    rect2 = patches.FancyBboxPatch((5.5 - b2["w"]/2, b2["y"]), b2["w"], b2["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#eef6fa", edgecolor=DEEP["blue"], lw=1.8)
    ax.add_patch(rect2)
    ax.text(5.5 - b2["w"]/2 + 0.35, b2["y"] + b2["h"] - 0.35, "population",
            fontsize=14, fontweight="bold", color=DEEP["blue"], ha="left")
    ax.text(5.5 - b2["w"]/2 + 0.35, b2["y"] + 0.3, "School of Tilapia fish",
            fontsize=11, color=INK, ha="left")
    # School of fish
    draw_tilapia(5.5 + 0.6, b2["y"] + 0.85, s=0.95)
    draw_tilapia(5.5 + 1.4, b2["y"] + 0.95, s=1.1)
    draw_tilapia(5.5 + 1.9, b2["y"] + 0.5, s=0.85)
    draw_tilapia(5.5 + 0.9, b2["y"] + 0.4, s=0.9)

    # 3. COMMUNITY
    b3 = levels[2]
    rect3 = patches.FancyBboxPatch((5.5 - b3["w"]/2, b3["y"]), b3["w"], b3["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#f2f9f5", edgecolor=DEEP["green"], lw=1.8)
    ax.add_patch(rect3)
    ax.text(5.5 - b3["w"]/2 + 0.35, b3["y"] + b3["h"] - 0.35, "community",
            fontsize=14, fontweight="bold", color=DEEP["green"], ha="left")
    ax.text(5.5 - b3["w"]/2 + 0.35, b3["y"] + 0.3, "Tilapia, lilies, frog,\ndragonfly & algae",
            fontsize=10.5, color=INK, ha="left")
    
    # Pond water background strip
    pw3 = patches.Rectangle((5.5 - 0.2, b3["y"] + 0.16), 3.1, 1.12,
                            facecolor=BLUE, alpha=0.35, edgecolor="none", zorder=1)
    ax.add_patch(pw3)
    # Floating algae clusters
    for ax_c, ay_c in [(5.5 + 0.05, b3["y"] + 0.4), (5.5 + 0.7, b3["y"] + 0.3), (5.5 + 2.5, b3["y"] + 0.35)]:
        ax.scatter([ax_c - 0.08, ax_c, ax_c + 0.08, ax_c - 0.04, ax_c + 0.05],
                   [ay_c, ay_c + 0.05, ay_c, ay_c - 0.05, ay_c + 0.04],
                   s=18, color=GREEN, alpha=0.9, zorder=2)
    # Tilapia fish in pond
    draw_tilapia(5.5 + 0.45, b3["y"] + 0.5, s=0.85)
    # Water lily pad & pink flower
    pad3 = patches.Circle((5.5 + 1.45, b3["y"] + 0.75), 0.26, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.3, zorder=3)
    ax.add_patch(pad3)
    ax.scatter([5.5 + 1.25, 5.5 + 1.35], [b3["y"] + 0.75, b3["y"] + 0.8], s=26, color=PINK, edgecolors=DEEP["pink"], lw=0.8, zorder=4)

    # Distinct Frog illustration resting on lily pad edge
    fx, fy = 5.5 + 1.55, b3["y"] + 0.8
    f_body = patches.Ellipse((fx, fy), 0.24, 0.18, angle=10, facecolor="#76c065", edgecolor=DEEP["green"], lw=1.3, zorder=5)
    ax.add_patch(f_body)
    f_head = patches.Ellipse((fx + 0.1, fy + 0.04), 0.14, 0.12, angle=15, facecolor="#76c065", edgecolor=DEEP["green"], lw=1.2, zorder=5)
    ax.add_patch(f_head)
    # Frog eyes
    ax.plot([fx + 0.08, fx + 0.14], [fy + 0.1, fy + 0.09], 'o', color=INK, markersize=3, zorder=6)
    # Frog legs
    f_leg = patches.Arc((fx - 0.08, fy - 0.04), 0.16, 0.14, angle=30, theta1=60, theta2=240, lw=1.6, color=DEEP["green"], zorder=5)
    ax.add_patch(f_leg)

    # Dragonfly hovering
    df_x, df_y = 5.5 + 2.45, b3["y"] + 0.95
    ax.plot([df_x - 0.12, df_x + 0.1], [df_y - 0.04, df_y + 0.04], lw=2.2, color=INK, zorder=5)
    ax.plot([df_x, df_x - 0.06], [df_y, df_y + 0.14], lw=1.3, color=DEEP["blue"], zorder=5)
    ax.plot([df_x + 0.02, df_x + 0.08], [df_y, df_y + 0.14], lw=1.3, color=DEEP["blue"], zorder=5)

    # 4. ECOSYSTEM
    b4 = levels[3]
    rect4 = patches.FancyBboxPatch((5.5 - b4["w"]/2, b4["y"]), b4["w"], b4["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#fcfbf7", edgecolor=DEEP["orange"], lw=1.8)
    ax.add_patch(rect4)
    ax.text(5.5 - b4["w"]/2 + 0.35, b4["y"] + b4["h"] - 0.35, "ecosystem",
            fontsize=14, fontweight="bold", color=DEEP["orange"], ha="left")
    ax.text(5.5 - b4["w"]/2 + 0.35, b4["y"] + 0.3, "Pond community with\nsun, water, mud & air",
            fontsize=10.5, color=INK, ha="left")

    # Abiotic + biotic scene:
    # Sun
    sun_x, sun_y = 5.5 - 0.1, b4["y"] + 0.98
    sun = patches.Circle((sun_x, sun_y), 0.18, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.3, zorder=3)
    ax.add_patch(sun)
    for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax.plot([sun_x + 0.22*np.cos(ang), sun_x + 0.31*np.cos(ang)],
                [sun_y + 0.22*np.sin(ang), sun_y + 0.31*np.sin(ang)], lw=1.4, color=DEEP["orange"], zorder=3)
    ax.text(sun_x, sun_y - 0.3, "sun", fontsize=11, fontweight="bold", color=DEEP["orange"], ha="center", zorder=5)

    # Mud layer at bottom
    mud = patches.Rectangle((5.5 + 0.6, b4["y"] + 0.15), 2.7, 0.25,
                            facecolor="#d2bba0", edgecolor="#82664b", lw=1.2, zorder=2)
    ax.add_patch(mud)
    ax.text(5.5 + 1.95, b4["y"] + 0.27, "mud", fontsize=11, fontweight="bold", color="#4d3520", ha="center", va="center", zorder=5)

    # Water layer
    water = patches.Rectangle((5.5 + 0.6, b4["y"] + 0.4), 2.7, 0.55,
                              facecolor=BLUE, alpha=0.5, edgecolor=DEEP["blue"], lw=1.2, zorder=2)
    ax.add_patch(water)
    ax.text(5.5 + 2.3, b4["y"] + 0.68, "water", fontsize=11, fontweight="bold", color=DEEP["blue"], ha="center", va="center", zorder=5)

    # Fish and lily in water
    draw_tilapia(5.5 + 1.25, b4["y"] + 0.62, s=0.65)
    ax.add_patch(patches.Circle((5.5 + 2.8, b4["y"] + 0.95), 0.18, facecolor=GREEN, edgecolor=DEEP["green"], lw=1, zorder=3))

    # Air label with high contrast and boxed highlight
    ax.text(5.5 + 1.95, b4["y"] + 1.15, "air", fontsize=11, fontweight="bold", color=INK,
            ha="center", va="center", bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2", lw=0.9), zorder=6)

    # 5. BIOME
    b5 = levels[4]
    rect5 = patches.FancyBboxPatch((5.5 - b5["w"]/2, b5["y"]), b5["w"], b5["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#f0f7f1", edgecolor=DEEP["green"], lw=1.8)
    ax.add_patch(rect5)
    ax.text(5.5 - b5["w"]/2 + 0.35, b5["y"] + b5["h"] - 0.35, "biome",
            fontsize=14, fontweight="bold", color=DEEP["green"], ha="left")
    ax.text(5.5 - b5["w"]/2 + 0.35, b5["y"] + 0.3, "Tropical rainforest landscape",
            fontsize=11, color=INK, ha="left")
    
    # Rainforest landscape drawing
    rx_start = 5.5 + 0.05
    # Distant mountain ridge
    ax.fill([rx_start, rx_start+0.9, rx_start+1.8, rx_start+2.8, rx_start+3.6, rx_start+3.6, rx_start],
            [b5["y"]+0.5, b5["y"]+1.08, b5["y"]+0.75, b5["y"]+1.12, b5["y"]+0.6, b5["y"]+0.15, b5["y"]+0.15],
            facecolor="#cde8cf", edgecolor="none", zorder=1)
    # Winding river
    river_x = [rx_start + 1.1, rx_start + 1.35, rx_start + 1.65, rx_start + 2.05, rx_start + 2.25]
    river_y = [b5["y"] + 0.15, b5["y"] + 0.35, b5["y"] + 0.5, b5["y"] + 0.65, b5["y"] + 0.75]
    ax.plot(river_x, river_y, lw=4, color=BLUE, alpha=0.85, solid_capstyle="round", zorder=2)
    # Dense rainforest tree canopies
    tree_locs = [(0.3, 0.45, 0.22), (0.7, 0.55, 0.26), (1.1, 0.45, 0.24),
                 (2.4, 0.4, 0.28), (2.9, 0.52, 0.25), (3.4, 0.42, 0.22),
                 (0.5, 0.25, 0.2), (1.5, 0.25, 0.2), (2.7, 0.25, 0.22)]
    for (tx, ty, tr) in tree_locs:
        ax.plot([rx_start + tx, rx_start + tx], [b5["y"] + 0.15, b5["y"] + ty], lw=1.6, color="#6b5344", zorder=3)
        crown = patches.Circle((rx_start + tx, b5["y"] + ty), tr, facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2, zorder=4)
        ax.add_patch(crown)

    # 6. BIOSPHERE
    b6 = levels[5]
    rect6 = patches.FancyBboxPatch((5.5 - b6["w"]/2, b6["y"]), b6["w"], b6["h"],
                                   boxstyle="round,pad=0.08,rounding_size=0.18",
                                   facecolor="#eff5f9", edgecolor=DEEP["blue"], lw=1.8)
    ax.add_patch(rect6)
    ax.text(5.5 - b6["w"]/2 + 0.35, b6["y"] + b6["h"] - 0.35, "biosphere",
            fontsize=14, fontweight="bold", color=DEEP["blue"], ha="left")
    ax.text(5.5 - b6["w"]/2 + 0.35, b6["y"] + 0.3, "The globe of the Earth",
            fontsize=11, color=INK, ha="left")

    # Globe of Earth
    gx, gy, gr = 5.5 + 2.1, b6["y"] + 0.72, 0.58
    # Atmosphere halo
    atmo = patches.Circle((gx, gy), gr + 0.08, facecolor=LAV, alpha=0.35, edgecolor=DEEP["lav"], lw=1, linestyle="--")
    ax.add_patch(atmo)
    # Ocean sphere
    globe = patches.Circle((gx, gy), gr, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.8)
    ax.add_patch(globe)
    
    # Continents sketched on globe (using clip path)
    africa = patches.Polygon([[gx - 0.1, gy + 0.35], [gx + 0.15, gy + 0.3], [gx + 0.25, gy + 0.05],
                              [gx + 0.1, gy - 0.35], [gx - 0.05, gy - 0.38], [gx - 0.18, gy - 0.1],
                              [gx - 0.22, gy + 0.1], [gx - 0.1, gy + 0.25]],
                             closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=1)
    africa.set_clip_path(globe)
    ax.add_patch(africa)
    
    americas = patches.Polygon([[gx - 0.52, gy + 0.35], [gx - 0.35, gy + 0.25], [gx - 0.42, gy - 0.05],
                                [gx - 0.3, gy - 0.3], [gx - 0.45, gy - 0.38], [gx - 0.55, gy - 0.1]],
                               closed=True, facecolor=GREEN, edgecolor=DEEP["green"], lw=1)
    americas.set_clip_path(globe)
    ax.add_patch(americas)

    # Latitude grid lines on globe
    lat1 = patches.Arc((gx, gy), gr*2, gr*0.6, angle=0, theta1=0, theta2=180, color=DEEP["blue"], lw=0.8, alpha=0.7)
    lat1.set_clip_path(globe)
    ax.add_patch(lat1)
    lat2 = patches.Arc((gx, gy), gr*2, gr*0.6, angle=0, theta1=180, theta2=360, color=DEEP["blue"], lw=0.8, alpha=0.7)
    lat2.set_clip_path(globe)
    ax.add_patch(lat2)

    save(fig, out)
