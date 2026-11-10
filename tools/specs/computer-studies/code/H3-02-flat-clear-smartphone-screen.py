import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style import *

def draw(out):
    fig = canvas(8, 10)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Phone dimensions
    px, py = 15, 5
    pw, ph = 50, 90
    corner_r = 5

    # Phone outer body (shadow/bezel)
    phone_outer = patches.FancyBboxPatch((px, py), pw, ph,
                                         boxstyle=f"round,pad=0,rounding_size={corner_r}",
                                         facecolor="#F3F4F6", edgecolor=INK, linewidth=3, zorder=1)
    ax.add_patch(phone_outer)

    # Phone screen
    sx, sy = px + 2.5, py + 3
    sw, sh = pw - 5, ph - 6
    screen = patches.FancyBboxPatch((sx, sy), sw, sh,
                                    boxstyle=f"round,pad=0,rounding_size={corner_r-1}",
                                    facecolor="#F9FAFB", edgecolor=GREY, linewidth=1.5, zorder=2)
    ax.add_patch(screen)

    # Clip path for screen contents
    screen_clip = patches.FancyBboxPatch((sx, sy), sw, sh,
                                         boxstyle=f"round,pad=0,rounding_size={corner_r-1}",
                                         transform=ax.transData)

    # Phone speaker / notch & camera
    ax.plot([px + pw/2 - 4, px + pw/2 + 4], [py + ph - 2, py + ph - 2], color=INK, lw=2.5, solid_capstyle='round', zorder=10)
    ax.plot([px + pw/2 + 7], [py + ph - 2], marker='o', color=INK, markersize=3, zorder=10)

    # Base map features (parks/blocks/water)
    # Park 1 (Green space)
    park1 = patches.Polygon([[sx+2, sy+40], [sx+14, sy+40], [sx+14, sy+58], [sx+2, sy+54]],
                            facecolor=GREEN, edgecolor="none", alpha=0.5, zorder=3)
    park1.set_clip_path(screen_clip)
    ax.add_patch(park1)

    # Park 2
    park2 = patches.Polygon([[sx+30, sy+18], [sx+43, sy+18], [sx+43, sy+32], [sx+30, sy+35]],
                            facecolor=GREEN, edgecolor="none", alpha=0.5, zorder=3)
    park2.set_clip_path(screen_clip)
    ax.add_patch(park2)

    # Minor grid roads (background)
    minor_roads = [
        # horizontal-ish
        [(sx, sy+25), (sx+sw, sy+25)],
        [(sx, sy+38), (sx+sw, sy+38)],
        [(sx, sy+52), (sx+sw, sy+52)],
        [(sx, sy+65), (sx+sw, sy+65)],
        # vertical-ish
        [(sx+12, sy), (sx+12, sy+sh)],
        [(sx+22, sy), (sx+22, sy+sh)],
        [(sx+32, sy), (sx+32, sy+sh)],
        [(sx+40, sy), (sx+40, sy+sh)],
    ]
    for r in minor_roads:
        line = ax.plot([r[0][0], r[1][0]], [r[0][1], r[1][1]], color="#E5E7EB", lw=5, solid_capstyle='round', zorder=3)[0]
        line.set_clip_path(screen_clip)

    # Main road network (under routes)
    # Origin and Destination coords
    orig_x, orig_y = sx + 8, sy + 15
    dest_x, dest_y = sx + 34, sy + 75

    # Red Congested Route: goes through central dense avenue
    red_route = [
        (orig_x, orig_y),
        (sx + 22, sy + 15),
        (sx + 22, sy + 48),
        (sx + 22, sy + 65),
        (dest_x, sy + 65),
        (dest_x, dest_y)
    ]
    rx_pts, ry_pts = zip(*red_route)

    # Blue Optimal Route: bypasses congestion to the east/north
    blue_route = [
        (orig_x, orig_y),
        (sx + 8, sy + 38),
        (sx + 14, sy + 38),
        (sx + 14, sy + 58),
        (sx + 34, sy + 58),
        (dest_x, dest_y)
    ]
    bx_pts, by_pts = zip(*blue_route)

    # Draw Red Route (Congested Route) - underneath where they diverge
    line_red = ax.plot(rx_pts, ry_pts, color=DEEP["pink"], lw=7, solid_capstyle='round',
                       solid_joinstyle='round', zorder=4, label="Congested Route")[0]
    line_red.set_clip_path(screen_clip)

    # Congestion icon/dots along the red line
    ax.text(sx + 22, sy + 38, "⚠", fontsize=15, ha='center', va='center', color=INK,
            bbox=dict(boxstyle="circle,pad=0.15", facecolor=PINK, edgecolor=DEEP["pink"], lw=1.5), zorder=6)

    # Draw Blue Route (Optimal Route)
    line_blue = ax.plot(bx_pts, by_pts, color=DEEP["blue"], lw=7, solid_capstyle='round',
                        solid_joinstyle='round', zorder=5, label="Optimal Route")[0]
    line_blue.set_clip_path(screen_clip)

    # Direction arrows on optimal route
    ax.annotate("", xy=(sx + 8, sy + 28), xytext=(sx + 8, sy + 24),
                arrowprops=dict(arrowstyle="->", color="white", lw=2.5), zorder=6)
    ax.annotate("", xy=(sx + 25, sy + 58), xytext=(sx + 21, sy + 58),
                arrowprops=dict(arrowstyle="->", color="white", lw=2.5), zorder=6)

    # Origin marker (Start)
    ax.plot(orig_x, orig_y, marker='o', markersize=10, markerfacecolor=DEEP["blue"], markeredgecolor="white", markeredgewidth=2.5, zorder=7)

    # Destination marker (Pin)
    ax.plot(dest_x, dest_y, marker='o', markersize=12, markerfacecolor=DEEP["pink"], markeredgecolor="white", markeredgewidth=2.5, zorder=7)
    ax.plot(dest_x, dest_y + 1, marker='v', markersize=9, color=DEEP["pink"], zorder=7)
    ax.plot(dest_x, dest_y + 1.2, marker='o', markersize=4, color="white", zorder=8)

    # Header search/status bar
    header_box = patches.FancyBboxPatch((sx + 3, sy + sh - 8), sw - 6, 6,
                                        boxstyle="round,pad=0,rounding_size=2",
                                        facecolor="white", edgecolor=GREY, linewidth=1.2, zorder=8)
    header_box.set_clip_path(screen_clip)
    ax.add_patch(header_box)
    ax.text(sx + 5.5, sy + sh - 5, "🔍 Navigating to Downtown...", fontsize=14, color=INK, va='center', zorder=9)

    # Route Labels on Map
    ax.text(sx + 23, sy + 44, "Congested Route\n(+18 min delay)", fontsize=14, color=DEEP["pink"],
            fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["pink"], lw=1),
            ha='left', va='center', zorder=8)

    ax.text(sx + 10, sy + 49, "Optimal Route\n(Fastest)", fontsize=14, color=DEEP["blue"],
            fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=DEEP["blue"], lw=1),
            ha='center', va='center', zorder=8)

    # AI-Calculated ETA Pop-up Card (at the bottom of the screen)
    popup_w = sw - 5
    popup_h = 16
    popup_x = sx + 2.5
    popup_y = sy + 3
    popup = patches.FancyBboxPatch((popup_x, popup_y), popup_w, popup_h,
                                   boxstyle="round,pad=0,rounding_size=3",
                                   facecolor="white", edgecolor=DEEP["blue"], linewidth=2, zorder=9)
    popup.set_clip_path(screen_clip)
    ax.add_patch(popup)

    # Content inside ETA Pop-up
    ax.text(popup_x + 3, popup_y + 12, "AI-Calculated ETA", fontsize=15, fontweight='bold', color=INK, va='center', zorder=10)
    
    # AI badge
    ai_badge = patches.FancyBboxPatch((popup_x + popup_w - 11, popup_y + 10.5), 8, 3.2,
                                      boxstyle="round,pad=0,rounding_size=1",
                                      facecolor=BLUE, edgecolor=DEEP["blue"], linewidth=1, zorder=10)
    ai_badge.set_clip_path(screen_clip)
    ax.add_patch(ai_badge)
    ax.text(popup_x + popup_w - 7, popup_y + 12.1, "AI Route", fontsize=14, color=DEEP["blue"], ha='center', va='center', fontweight='bold', zorder=11)

    # ETA stats
    ax.text(popup_x + 3, popup_y + 6.5, "18 min", fontsize=20, fontweight='bold', color=DEEP["green"], va='center', zorder=10)
    ax.text(popup_x + 16, popup_y + 6.5, "•  7.4 mi  •  5:42 PM", fontsize=14, color=INK, va='center', zorder=10)
    ax.text(popup_x + 3, popup_y + 2.5, "Saves 12 min vs congested route", fontsize=14, color=INK, va='center', zorder=10)

    save(fig, out)
