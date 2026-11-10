from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def draw(out):
    fig = canvas(14, 9)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Main Title
    ax.text(7, 8.45, "Natural Resources", ha="center", va="center",
            fontsize=20, weight="bold", color=INK)

    # Left Container (Renewable Resources)
    left_rect = patches.FancyBboxPatch(
        (0.6, 0.6), 6.1, 7.4,
        boxstyle="round,pad=0.2,rounding_size=0.3",
        linewidth=3, edgecolor=DEEP["green"], facecolor="#f4fbf6"
    )
    ax.add_patch(left_rect)

    # Right Container (Non-renewable Resources)
    BROWN = "#795548"
    right_rect = patches.FancyBboxPatch(
        (7.3, 0.6), 6.1, 7.4,
        boxstyle="round,pad=0.2,rounding_size=0.3",
        linewidth=3, edgecolor=BROWN, facecolor="#fdfaf7"
    )
    ax.add_patch(right_rect)

    # Headers and Subtitles
    ax.text(3.65, 7.6, "Renewable Resources", ha="center", va="center",
            fontsize=17, weight="bold", color=DEEP["green"])
    ax.text(3.65, 7.15, "Can be replaced naturally", ha="center", va="center",
            fontsize=14, style="italic", color=INK)

    ax.text(10.35, 7.6, "Non-renewable Resources", ha="center", va="center",
            fontsize=17, weight="bold", color=BROWN)
    ax.text(10.35, 7.15, "Cannot be easily replaced; limited supply", ha="center", va="center",
            fontsize=14, style="italic", color=INK)

    # ================= LEFT SIDE ICONS =================
    # 1. Sun (top-left: center 2.2, 5.4)
    cx, cy = 2.2, 5.5
    sun_circle = patches.Circle((cx, cy), 0.45, facecolor="#FDD835", edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(sun_circle)
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        r1, r2 = 0.55, 0.82
        x1, y1 = cx + r1 * np.cos(angle), cy + r1 * np.sin(angle)
        x2, y2 = cx + r2 * np.cos(angle), cy + r2 * np.sin(angle)
        ax.plot([x1, x2], [y1, y2], color=DEEP["orange"], lw=2.5, solid_capstyle="round")
    ax.text(cx, 4.35, "Sunlight\n(Solar)", ha="center", va="top", fontsize=14, color=INK)

    # 2. Tree (top-right: center 5.1, 5.5)
    tx, ty = 5.1, 5.5
    # Trunk
    trunk = patches.Rectangle((tx - 0.1, ty - 0.7), 0.2, 0.55, facecolor="#6D4C41", edgecolor="#4E342E", lw=1.5)
    ax.add_patch(trunk)
    # Foliage (three overlapping green circles)
    c_foliage1 = patches.Circle((tx - 0.28, ty - 0.15), 0.38, facecolor=GREEN, edgecolor=DEEP["green"], lw=2)
    c_foliage2 = patches.Circle((tx + 0.28, ty - 0.15), 0.38, facecolor=GREEN, edgecolor=DEEP["green"], lw=2)
    c_foliage3 = patches.Circle((tx, ty + 0.18), 0.44, facecolor="#81C784", edgecolor=DEEP["green"], lw=2)
    ax.add_patch(c_foliage1)
    ax.add_patch(c_foliage2)
    ax.add_patch(c_foliage3)
    ax.text(tx, 4.35, "Trees &\nTimber", ha="center", va="top", fontsize=14, color=INK)

    # 3. River (bottom-left: center 2.2, 2.7)
    rx, ry = 2.2, 2.7
    t_vals = np.linspace(-0.8, 0.8, 100)
    wave_y1 = ry + 0.25 + 0.12 * np.sin(4 * t_vals)
    wave_y2 = ry + 0.12 * np.sin(4 * t_vals)
    wave_y3 = ry - 0.25 + 0.12 * np.sin(4 * t_vals)
    ax.plot(rx + t_vals, wave_y1, color=DEEP["blue"], lw=3.5, solid_capstyle="round")
    ax.plot(rx + t_vals, wave_y2, color=BLUE, lw=3.5, solid_capstyle="round")
    ax.plot(rx + t_vals, wave_y3, color=DEEP["blue"], lw=3.5, solid_capstyle="round")
    ax.text(rx, 1.7, "Flowing\nWater", ha="center", va="top", fontsize=14, color=INK)

    # 4. Running Antelope (bottom-right: center 5.1, 2.7)
    ax_x, ax_y = 5.1, 2.7
    # Body
    body = patches.Ellipse((ax_x, ax_y + 0.05), 0.7, 0.32, angle=-8, facecolor="#D7CCC8", edgecolor="#5D4037", lw=2)
    ax.add_patch(body)
    # Neck and Head
    neck_path = Path([
        (ax_x + 0.25, ax_y + 0.1),
        (ax_x + 0.45, ax_y + 0.42),
        (ax_x + 0.65, ax_y + 0.45),
        (ax_x + 0.35, ax_y + 0.25)
    ], [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
    ax.add_patch(patches.PathPatch(neck_path, facecolor="#D7CCC8", edgecolor="#5D4037", lw=2))
    # Horns
    ax.plot([ax_x + 0.48, ax_x + 0.35], [ax_x_y := ax_y + 0.44, ax_y + 0.72], color="#3E2723", lw=2.5)
    ax.plot([ax_x + 0.52, ax_x + 0.42], [ax_y + 0.44, ax_y + 0.74], color="#3E2723", lw=2.5)
    # Legs (running posture)
    # Front legs extended forward
    ax.plot([ax_x + 0.25, ax_x + 0.45, ax_x + 0.65], [ax_y, ax_y - 0.2, ax_y - 0.4], color="#5D4037", lw=2.5)
    ax.plot([ax_x + 0.2, ax_x + 0.35, ax_x + 0.5], [ax_y, ax_y - 0.25, ax_y - 0.45], color="#5D4037", lw=2)
    # Back legs extended backward
    ax.plot([ax_x - 0.25, ax_x - 0.45, ax_x - 0.65], [ax_y, ax_y - 0.15, ax_y - 0.35], color="#5D4037", lw=2.5)
    ax.plot([ax_x - 0.2, ax_x - 0.35, ax_x - 0.55], [ax_y, ax_y - 0.2, ax_y - 0.4], color="#5D4037", lw=2)
    ax.text(ax_x, 1.7, "Wildlife &\nAnimals", ha="center", va="top", fontsize=14, color=INK)

    # ================= RIGHT SIDE ICONS =================
    # 1. Oil Drum (top-center: 10.35, 5.5)
    ox, oy = 10.35, 5.25
    drum_w, drum_h = 0.9, 1.15
    drum_body = patches.Rectangle((ox - drum_w/2, oy), drum_w, drum_h, facecolor="#37474F", edgecolor="#212121", lw=2)
    ax.add_patch(drum_body)
    # Top and bottom rims (ellipses)
    top_rim = patches.Ellipse((ox, oy + drum_h), drum_w, 0.25, facecolor="#546E7A", edgecolor="#212121", lw=2)
    bot_rim = patches.Arc((ox, oy), drum_w, 0.25, theta1=180, theta2=360, edgecolor="#212121", lw=2)
    ax.add_patch(top_rim)
    ax.add_patch(bot_rim)
    # Ribs on barrel
    ax.plot([ox - drum_w/2, ox + drum_w/2], [oy + 0.38, oy + 0.38], color="#212121", lw=2)
    ax.plot([ox - drum_w/2, ox + drum_w/2], [oy + 0.76, oy + 0.76], color="#212121", lw=2)
    # Drop symbol on barrel
    drop = patches.PathPatch(Path([
        (ox, oy + 0.68),
        (ox + 0.14, oy + 0.48),
        (ox - 0.14, oy + 0.48),
        (ox, oy + 0.68)
    ], [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]), facecolor="#FFA726", edgecolor=INK, lw=1)
    ax.add_patch(drop)
    ax.text(ox, 4.35, "Crude Oil\n(Petroleum)", ha="center", va="top", fontsize=14, color=INK)

    # 2. Lump of Dark Coal (bottom-left: center 8.9, 2.7)
    cx2, cy2 = 8.9, 2.7
    coal_verts = [
        (cx2 - 0.65, cy2 - 0.25),
        (cx2 - 0.75, cy2 + 0.1),
        (cx2 - 0.35, cy2 + 0.45),
        (cx2 + 0.2, cy2 + 0.5),
        (cx2 + 0.65, cy2 + 0.2),
        (cx2 + 0.6, cy2 - 0.25),
        (cx2 + 0.1, cy2 - 0.4),
        (cx2 - 0.4, cy2 - 0.35)
    ]
    coal = patches.Polygon(coal_verts, closed=True, facecolor="#263238", edgecolor="#102027", lw=2.5)
    ax.add_patch(coal)
    # Facet lines for crystal/rock look
    ax.plot([cx2 - 0.35, cx2 - 0.05, cx2 + 0.2], [cy2 + 0.45, cy2 + 0.05, cy2 + 0.5], color="#455A64", lw=2)
    ax.plot([cx2 - 0.05, cx2 + 0.6], [cy2 + 0.05, cy2 - 0.25], color="#455A64", lw=2)
    ax.plot([cx2 - 0.05, cx2 - 0.4], [cy2 + 0.05, cy2 - 0.35], color="#455A64", lw=2)
    ax.text(cx2, 1.7, "Coal &\nFossil Fuels", ha="center", va="top", fontsize=14, color=INK)

    # 3. Gold Bar (bottom-right: center 11.8, 2.7)
    gx, gy = 11.8, 2.65
    # Trapezoid top face and front face
    front_verts = [
        (gx - 0.65, gy - 0.3),
        (gx + 0.45, gy - 0.3),
        (gx + 0.35, gy + 0.05),
        (gx - 0.55, gy + 0.05)
    ]
    top_verts = [
        (gx - 0.55, gy + 0.05),
        (gx + 0.35, gy + 0.05),
        (gx + 0.55, gy + 0.35),
        (gx - 0.35, gy + 0.35)
    ]
    side_verts = [
        (gx + 0.45, gy - 0.3),
        (gx + 0.65, gy),
        (gx + 0.55, gy + 0.35),
        (gx + 0.35, gy + 0.05)
    ]
    ax.add_patch(patches.Polygon(front_verts, closed=True, facecolor="#FFB300", edgecolor="#B26A00", lw=2))
    ax.add_patch(patches.Polygon(top_verts, closed=True, facecolor="#FFD54F", edgecolor="#B26A00", lw=2))
    ax.add_patch(patches.Polygon(side_verts, closed=True, facecolor="#FFA000", edgecolor="#B26A00", lw=2))
    ax.text(gx - 0.1, gy - 0.15, "999.9", fontsize=14, weight="bold", color="#8D5B00", rotation=0, ha="center")
    ax.text(gx, 1.7, "Minerals\n& Metals", ha="center", va="top", fontsize=14, color=INK)

    save(fig, out)
