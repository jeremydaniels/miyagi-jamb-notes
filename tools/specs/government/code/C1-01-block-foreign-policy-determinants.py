from style import *
import numpy as np
import matplotlib.patches as patches
import matplotlib.path as mpath

def draw(out):
    fig = canvas(14, 9.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9.5)
    ax.axis("off")

    # Title
    ax.text(7, 8.9, "Determinants of Foreign Policy", ha="center", va="center",
            fontsize=20, weight="bold", color=INK)

    # Dividing central dashed line
    ax.plot([7, 7], [0.8, 8.2], color=GREY, lw=2, linestyle="--")

    # Column Headers
    # Left Header: Internal Factors
    left_header_box = patches.FancyBboxPatch((1.2, 7.7), 4.6, 0.7,
                                             boxstyle="round,pad=0.1,rounding_size=0.15",
                                             facecolor=BLUE, edgecolor=DEEP["blue"], lw=2)
    ax.add_patch(left_header_box)
    ax.text(3.5, 8.05, "Internal Factors", ha="center", va="center",
            fontsize=16, weight="bold", color=DEEP["blue"])

    # Right Header: External Factors
    right_header_box = patches.FancyBboxPatch((8.2, 7.7), 4.6, 0.7,
                                              boxstyle="round,pad=0.1,rounding_size=0.15",
                                              facecolor=ORANGE, edgecolor=DEEP["orange"], lw=2)
    ax.add_patch(right_header_box)
    ax.text(10.5, 8.05, "External Factors", ha="center", va="center",
            fontsize=16, weight="bold", color=DEEP["orange"])

    # Helper to draw an item container box
    def draw_card(cx, cy, w, h, bg_col, edge_col):
        box = patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                                     boxstyle="round,pad=0.08,rounding_size=0.2",
                                     facecolor=bg_col, edgecolor=edge_col, lw=1.5)
        ax.add_patch(box)

    # ----------------------------------------------------
    # LEFT SIDE: 4 Internal Factors (Geography, Economic Resources, Military, Population)
    # y-centers: 6.8, 5.1, 3.4, 1.7
    # ----------------------------------------------------
    left_y = [6.8, 5.1, 3.4, 1.7]

    # 1. Geography (Map icon)
    draw_card(3.5, left_y[0], 5.8, 1.45, CREAM, GREY)
    ax.text(3.0, left_y[0], "Geography", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(3.0, left_y[0] - 0.35, "Territory, location, natural borders", ha="left", va="center", fontsize=12, color=INK)
    # Map icon at (2.0, left_y[0])
    mx, my = 1.9, left_y[0]
    # Folded map polygons
    poly1 = patches.Polygon([[mx - 0.5, my - 0.4], [mx - 0.2, my - 0.3], [mx - 0.2, my + 0.4], [mx - 0.5, my + 0.3]],
                            facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    poly2 = patches.Polygon([[mx - 0.2, my - 0.3], [mx + 0.1, my - 0.45], [mx + 0.1, my + 0.25], [mx - 0.2, my + 0.4]],
                            facecolor=CREAM, edgecolor=DEEP["green"], lw=1.5)
    poly3 = patches.Polygon([[mx + 0.1, my - 0.45], [mx + 0.4, my - 0.35], [mx + 0.4, my + 0.35], [mx + 0.1, my + 0.25]],
                            facecolor=GREEN, edgecolor=DEEP["green"], lw=1.5)
    for p in [poly1, poly2, poly3]:
        ax.add_patch(p)
    # Location pin
    ax.plot([mx - 0.05], [my + 0.05], marker='o', markersize=6, color=DEEP["pink"])
    ax.plot([mx - 0.05, mx - 0.05], [my - 0.1, my + 0.05], color=DEEP["pink"], lw=1.5)

    # 2. Economic Resources (Oil drop & coins)
    draw_card(3.5, left_y[1], 5.8, 1.45, CREAM, GREY)
    ax.text(3.0, left_y[1], "Economic Resources", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(3.0, left_y[1] - 0.35, "Trade, industrial base, energy & capital", ha="left", va="center", fontsize=12, color=INK)
    # Oil drop & coins at (1.9, left_y[1])
    ox, oy = 1.9, left_y[1]
    # Coins (stacked ellipses)
    for dy in [-0.28, -0.16]:
        coin = patches.Ellipse((ox + 0.25, oy + dy), 0.38, 0.16, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.5)
        ax.add_patch(coin)
    # Oil drop path
    Path = mpath.Path
    drop_verts = [
        (ox - 0.22, oy + 0.32),
        (ox - 0.45, oy - 0.15),
        (ox + 0.01, oy - 0.15),
        (ox - 0.22, oy + 0.32),
    ]
    drop_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]
    drop_path = mpath.Path(drop_verts, drop_codes)
    drop_patch = patches.PathPatch(drop_path, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(drop_patch)
    drop_bot = patches.Ellipse((ox - 0.22, oy - 0.15), 0.46, 0.32, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(drop_bot)

    # 3. Military (Shield icon)
    draw_card(3.5, left_y[2], 5.8, 1.45, CREAM, GREY)
    ax.text(3.0, left_y[2], "Military", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(3.0, left_y[2] - 0.35, "Defense strength, strategic capabilities", ha="left", va="center", fontsize=12, color=INK)
    # Shield icon at (1.9, left_y[2])
    sx, sy = 1.9, left_y[2]
    shield_verts = [
        (sx - 0.35, sy + 0.35),
        (sx + 0.35, sy + 0.35),
        (sx + 0.35, sy),
        (sx, sy - 0.45),
        (sx - 0.35, sy),
        (sx - 0.35, sy + 0.35)
    ]
    shield_patch = patches.Polygon(shield_verts, closed=True, facecolor=PINK, edgecolor=DEEP["pink"], lw=1.8)
    ax.add_patch(shield_patch)
    # Shield emblem cross / chevron
    ax.plot([sx, sx], [sy - 0.35, sy + 0.25], color=DEEP["pink"], lw=1.5)
    ax.plot([sx - 0.25, sx + 0.25], [sy + 0.1, sy + 0.1], color=DEEP["pink"], lw=1.5)

    # 4. Population (Group of people)
    draw_card(3.5, left_y[3], 5.8, 1.45, CREAM, GREY)
    ax.text(3.0, left_y[3], "Population", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(3.0, left_y[3] - 0.35, "Demographics, morale, human capital", ha="left", va="center", fontsize=12, color=INK)
    # Group of people at (1.9, left_y[3])
    px, py = 1.9, left_y[3]
    # Person helper
    def draw_person(x, y, scale=1.0, col=LAV, edge_col=DEEP["lav"]):
        head = patches.Circle((x, y + 0.25 * scale), 0.13 * scale, facecolor=col, edgecolor=edge_col, lw=1.4)
        body = patches.Ellipse((x, y - 0.1 * scale), 0.36 * scale, 0.42 * scale, facecolor=col, edgecolor=edge_col, lw=1.4)
        ax.add_patch(head)
        ax.add_patch(body)

    # 3 silhouettes: back two, front one
    draw_person(px - 0.26, py + 0.05, scale=0.85, col=LAV, edge_col=DEEP["lav"])
    draw_person(px + 0.26, py + 0.05, scale=0.85, col=LAV, edge_col=DEEP["lav"])
    draw_person(px, py - 0.05, scale=1.0, col=GREEN, edge_col=DEEP["green"])

    # ----------------------------------------------------
    # RIGHT SIDE: 3 External Factors
    # (International Organizations, International Law, Global Power Structure)
    # y-centers: 6.4, 4.25, 2.1
    # ----------------------------------------------------
    right_y = [6.3, 4.25, 2.2]

    # 1. International Organizations (Globe surrounded by flags)
    draw_card(10.5, right_y[0], 5.8, 1.7, CREAM, GREY)
    ax.text(9.9, right_y[0], "International Organizations", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(9.9, right_y[0] - 0.38, "UN, WTO, alliances & regional pacts", ha="left", va="center", fontsize=12, color=INK)
    # Globe & flags at (8.8, right_y[0])
    gx, gy = 8.8, right_y[0]
    # Central globe
    globe = patches.Circle((gx, gy), 0.32, facecolor=BLUE, edgecolor=DEEP["blue"], lw=1.5)
    ax.add_patch(globe)
    # Latitude / longitude lines on globe
    lat1 = patches.Arc((gx, gy), 0.64, 0.32, angle=0, theta1=0, theta2=360, color=DEEP["blue"], lw=1.2)
    lat2 = patches.Arc((gx, gy), 0.64, 0.1, angle=0, theta1=0, theta2=360, color=DEEP["blue"], lw=1.2)
    ax.add_patch(lat1)
    ax.add_patch(lat2)
    ax.plot([gx, gx], [gy - 0.32, gy + 0.32], color=DEEP["blue"], lw=1.2)
    # Surrounding flags (3 small flags on poles)
    # Flag left
    ax.plot([gx - 0.48, gx - 0.48], [gy - 0.25, gy + 0.45], color=DEEP["orange"], lw=1.4)
    f1 = patches.Polygon([[gx - 0.48, gy + 0.45], [gx - 0.25, gy + 0.35], [gx - 0.48, gy + 0.25]],
                         facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.2)
    ax.add_patch(f1)
    # Flag right
    ax.plot([gx + 0.48, gx + 0.48], [gy - 0.25, gy + 0.45], color=DEEP["green"], lw=1.4)
    f2 = patches.Polygon([[gx + 0.48, gy + 0.45], [gx + 0.71, gy + 0.35], [gx + 0.48, gy + 0.25]],
                         facecolor=GREEN, edgecolor=DEEP["green"], lw=1.2)
    ax.add_patch(f2)
    # Flag top-left
    ax.plot([gx - 0.1, gx - 0.1], [gy + 0.32, gy + 0.68], color=DEEP["pink"], lw=1.4)
    f3 = patches.Polygon([[gx - 0.1, gy + 0.68], [gx + 0.15, gy + 0.58], [gx - 0.1, gy + 0.48]],
                         facecolor=PINK, edgecolor=DEEP["pink"], lw=1.2)
    ax.add_patch(f3)

    # 2. International Law (Judge's gavel)
    draw_card(10.5, right_y[1], 5.8, 1.7, CREAM, GREY)
    ax.text(9.9, right_y[1], "International Law", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(9.9, right_y[1] - 0.38, "Treaties, conventions & global norms", ha="left", va="center", fontsize=12, color=INK)
    # Gavel icon at (8.8, right_y[1])
    jx, jy = 8.8, right_y[1]
    # Gavel head (angled rectangle)
    # angle 35 deg
    rad = np.radians(35)
    ca, sa = np.cos(rad), np.sin(rad)
    # center of mallet head
    mx, my = jx - 0.15, jy + 0.2
    # Mallet head rectangle centered at mx, my
    hw, hh = 0.48, 0.22
    corners = np.array([[-hw/2, -hh/2], [hw/2, -hh/2], [hw/2, hh/2], [-hw/2, hh/2]])
    rot_corners = np.dot(corners, np.array([[ca, -sa], [sa, ca]])) + [mx, my]
    gavel_head = patches.Polygon(rot_corners, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.6)
    ax.add_patch(gavel_head)
    # Handle going down-right from mallet
    hx1, hy1 = mx, my
    hx2, hy2 = mx + 0.55 * sa, my - 0.55 * ca
    ax.plot([hx1, hx2], [hy1, hy2], color=DEEP["orange"], lw=3.5, solid_capstyle="round")
    # Sound block below
    sb = patches.FancyBboxPatch((jx - 0.5, jy - 0.38), 0.7, 0.15,
                                boxstyle="round,pad=0.03,rounding_size=0.05",
                                facecolor=CREAM, edgecolor=DEEP["orange"], lw=1.5)
    ax.add_patch(sb)

    # 3. Global Power Structure (Balancing scales)
    draw_card(10.5, right_y[2], 5.8, 1.7, CREAM, GREY)
    ax.text(9.9, right_y[2], "Global Power Structure", ha="left", va="center", fontsize=15, weight="bold", color=INK)
    ax.text(9.9, right_y[2] - 0.38, "Polarity, balance of power & hegemony", ha="left", va="center", fontsize=12, color=INK)
    # Scale icon at (8.8, right_y[2])
    bx, by = 8.8, right_y[2]
    # Central pole & base
    ax.plot([bx, bx], [by - 0.35, by + 0.35], color=DEEP["blue"], lw=2.5)
    ax.plot([bx - 0.3, bx + 0.3], [by - 0.35, by - 0.35], color=DEEP["blue"], lw=2.5)
    # Top fulcrum circle
    ax.plot([bx], [by + 0.35], marker='o', markersize=5, color=DEEP["blue"])
    # Beam
    beam_w = 0.5
    ax.plot([bx - beam_w, bx + beam_w], [by + 0.35, by + 0.35], color=DEEP["blue"], lw=2)
    # Hanging strings & pans left
    ax.plot([bx - beam_w, bx - beam_w - 0.15], [by + 0.35, by + 0.05], color=DEEP["blue"], lw=1.2)
    ax.plot([bx - beam_w, bx - beam_w + 0.15], [by + 0.35, by + 0.05], color=DEEP["blue"], lw=1.2)
    pan_l = patches.Arc((bx - beam_w, by + 0.05), 0.32, 0.18, angle=0, theta1=180, theta2=360, color=DEEP["blue"], lw=1.6)
    ax.add_patch(pan_l)
    # Hanging strings & pans right
    ax.plot([bx + beam_w, bx + beam_w - 0.15], [by + 0.35, by + 0.05], color=DEEP["blue"], lw=1.2)
    ax.plot([bx + beam_w, bx + beam_w + 0.15], [by + 0.35, by + 0.05], color=DEEP["blue"], lw=1.2)
    pan_r = patches.Arc((bx + beam_w, by + 0.05), 0.32, 0.18, angle=0, theta1=180, theta2=360, color=DEEP["blue"], lw=1.6)
    ax.add_patch(pan_r)

    save(fig, out)
