from style import *
import numpy as np
import matplotlib.patches as mpatches

def draw(out):
    fig = canvas(12, 11)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_xlim(1.5, 16.8)
    ax.set_ylim(3.0, 15.0)

    c_band1 = "#4A90E2"       # dark / rich blue along coast & Niger Delta
    c_band2 = "#82B7E9"       # lighter blue
    c_band3 = "#BDE4C2"       # pale green
    c_band4 = "#F7E8A4"       # pale yellow
    c_band5 = "#E8C29F"       # pale orange-brown (far north / northeast)

    poly_pts = nigeria_poly()
    clip_path = mpatches.Polygon(poly_pts, facecolor="none", edgecolor="none", closed=True)
    ax.add_patch(clip_path)

    y_breaks = [3.5, 6.3, 8.2, 10.3, 12.2, 15.0]
    band_colors = [c_band1, c_band2, c_band3, c_band4, c_band5]

    for i in range(len(band_colors)):
        y_low = y_breaks[i]
        y_high = y_breaks[i+1]
        band_rect = mpatches.Rectangle((1.5, y_low), 15.0, y_high - y_low,
                                      facecolor=band_colors[i], edgecolor="none", zorder=1)
        band_rect.set_clip_path(clip_path)
        ax.add_patch(band_rect)

    border = mpatches.Polygon(poly_pts, facecolor="none", edgecolor=INK, lw=2.2, zorder=3)
    ax.add_patch(border)

    lake_chad = mpatches.Polygon(
        [[13.5, 12.8], [14.0, 12.7], [14.7, 13.1], [14.9, 13.7], [14.4, 14.2], [13.7, 13.8], [13.4, 13.2]],
        closed=True, facecolor="#9AC7E8", edgecolor=DEEP["blue"], lw=1.5, zorder=4
    )
    ax.add_patch(lake_chad)
    ax.text(14.3, 13.4, "Lake Chad", fontsize=14, color=INK, ha="center", va="center", weight="bold",
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=2), zorder=5)

    ax.text(5.5, 3.6, "Atlantic Ocean", fontsize=16, color=DEEP["blue"], style="italic", weight="bold", ha="center")

    ax.annotate("", xy=(2.3, 13.5), xytext=(2.3, 4.8),
                arrowprops=dict(facecolor=ORANGE, edgecolor=DEEP["orange"], width=7, headwidth=18, headlength=16),
                zorder=6)
    ax.text(1.85, 9.1, "rainfall decreases northwards", fontsize=14, color=INK, weight="bold",
            rotation=90, ha="center", va="center",
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3", lw=1), zorder=7)

    ax.annotate("highest rainfall\n(over 3,000 mm in parts of\nthe Niger Delta)",
                xy=(6.0, 4.7), xytext=(8.8, 3.8),
                fontsize=14, color=INK, weight="bold", ha="left", va="center",
                bbox=dict(fc="white", ec=DEEP["blue"], boxstyle="round,pad=0.4", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=8)

    ax.annotate("moderate rainfall",
                xy=(8.0, 9.2), xytext=(11.6, 8.8),
                fontsize=14, color=INK, weight="bold", ha="left", va="center",
                bbox=dict(fc="white", ec=DEEP["green"], boxstyle="round,pad=0.4", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=8)

    ax.annotate("low rainfall\n(about 500 mm or less\nnear Lake Chad)",
                xy=(13.2, 12.8), xytext=(10.5, 14.3),
                fontsize=14, color=INK, weight="bold", ha="center", va="center",
                bbox=dict(fc="white", ec=DEEP["orange"], boxstyle="round,pad=0.4", lw=1.5),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.5), zorder=8)

    def draw_tree(cx, cy, s=0.35):
        trunk = mpatches.Rectangle((cx - 0.08 * s, cy - 0.7 * s), 0.16 * s, 0.6 * s,
                                   facecolor="#8B5A2B", edgecolor=INK, lw=1, zorder=10)
        ax.add_patch(trunk)
        ax.add_patch(mpatches.Circle((cx, cy + 0.1 * s), 0.45 * s, facecolor="#2E7D32", edgecolor=INK, lw=1, zorder=11))
        ax.add_patch(mpatches.Circle((cx - 0.3 * s, cy - 0.1 * s), 0.35 * s, facecolor="#388E3C", edgecolor=INK, lw=1, zorder=11))
        ax.add_patch(mpatches.Circle((cx + 0.3 * s, cy - 0.1 * s), 0.35 * s, facecolor="#388E3C", edgecolor=INK, lw=1, zorder=11))

    def draw_cocoa(cx, cy, s=0.35):
        pod = mpatches.Ellipse((cx, cy), 0.5 * s, 0.9 * s, angle=25, facecolor="#A04000", edgecolor=INK, lw=1.2, zorder=10)
        ax.add_patch(pod)
        rad = np.radians(25)
        dx, dy = 0.35 * s * np.sin(rad), 0.35 * s * np.cos(rad)
        ax.plot([cx - dx, cx + dx], [cy + dy, cy - dy], color="#6E2C00", lw=1, zorder=11)
        ax.plot([cx - 0.2 * s, cx - 0.3 * s], [cy + 0.4 * s, cy + 0.55 * s], color="#5D4037", lw=1.5, zorder=10)

    def draw_yam(cx, cy, s=0.35):
        tuber = mpatches.Ellipse((cx, cy), 0.9 * s, 0.45 * s, angle=-15, facecolor="#8D6E63", edgecolor=INK, lw=1.2, zorder=10)
        ax.add_patch(tuber)
        ax.plot([cx - 0.25 * s, cx + 0.25 * s], [cy - 0.05 * s, cy + 0.05 * s], color="#5D4037", lw=1, ls="--", zorder=11)

    def draw_cassava(cx, cy, s=0.35):
        p = mpatches.Polygon([[cx - 0.45 * s, cy + 0.1 * s], [cx + 0.45 * s, cy - 0.05 * s], [cx - 0.1 * s, cy - 0.2 * s]],
                             closed=True, facecolor="#6D4C41", edgecolor=INK, lw=1.2, zorder=10)
        ax.add_patch(p)
        ax.plot([cx - 0.4 * s, cx - 0.6 * s], [cy + 0.1 * s, cy + 0.3 * s], color="#2E7D32", lw=1.5, zorder=11)
        ax.plot([cx - 0.4 * s, cx - 0.45 * s], [cy + 0.1 * s, cy + 0.4 * s], color="#2E7D32", lw=1.5, zorder=11)
        ax.plot([cx - 0.4 * s, cx - 0.25 * s], [cy + 0.1 * s, cy + 0.35 * s], color="#2E7D32", lw=1.5, zorder=11)

    def draw_millet(cx, cy, s=0.35):
        ax.plot([cx, cx], [cy - 0.6 * s, cy + 0.5 * s], color="#F9A825", lw=2, zorder=10)
        spike = mpatches.Ellipse((cx, cy + 0.1 * s), 0.22 * s, 0.8 * s, facecolor="#FBC02D", edgecolor=INK, lw=1.2, zorder=11)
        ax.add_patch(spike)
        for dy in np.linspace(-0.25 * s, 0.45 * s, 5):
            ax.plot([cx - 0.1 * s, cx - 0.3 * s], [cy + dy, cy + dy + 0.15 * s], color=INK, lw=0.8, zorder=12)
            ax.plot([cx + 0.1 * s, cx + 0.3 * s], [cy + dy, cy + dy + 0.15 * s], color=INK, lw=0.8, zorder=12)

    def draw_groundnut(cx, cy, s=0.35):
        ax.add_patch(mpatches.Circle((cx - 0.2 * s, cy), 0.24 * s, facecolor="#D7CCC8", edgecolor=INK, lw=1.2, zorder=10))
        ax.add_patch(mpatches.Circle((cx + 0.2 * s, cy), 0.2 * s, facecolor="#D7CCC8", edgecolor=INK, lw=1.2, zorder=10))
        ax.plot([cx, cx - 0.25 * s], [cy + 0.1 * s, cy + 0.38 * s], color="#43A047", lw=1.5, zorder=11)
        ax.plot([cx, cx + 0.25 * s], [cy + 0.1 * s, cy + 0.38 * s], color="#43A047", lw=1.5, zorder=11)

    def draw_camel(cx, cy, s=0.45):
        body = mpatches.Ellipse((cx, cy), 0.8 * s, 0.5 * s, facecolor="#D2B48C", edgecolor=INK, lw=1.2, zorder=10)
        hump = mpatches.Ellipse((cx + 0.05 * s, cy + 0.3 * s), 0.42 * s, 0.38 * s, facecolor="#D2B48C", edgecolor=INK, lw=1.2, zorder=11)
        ax.add_patch(body)
        ax.add_patch(hump)
        ax.plot([cx - 0.3 * s, cx - 0.55 * s, cx - 0.7 * s], [cy + 0.1 * s, cy + 0.45 * s, cy + 0.42 * s],
                color=INK, lw=2.2, zorder=12)
        head = mpatches.Ellipse((cx - 0.7 * s, cy + 0.45 * s), 0.22 * s, 0.14 * s,
                                facecolor="#D2B48C", edgecolor=INK, lw=1, zorder=13)
        ax.add_patch(head)
        for lx in [-0.25 * s, -0.1 * s, 0.18 * s, 0.32 * s]:
            ax.plot([cx + lx, cx + lx], [cy - 0.2 * s, cy - 0.7 * s], color=INK, lw=1.8, zorder=9)

    bx, by = 4.8, 6.4
    rect_s = mpatches.FancyBboxPatch((bx - 1.8, by - 0.95), 4.0, 1.85,
                                     boxstyle="round,pad=0.15", facecolor="white", edgecolor=DEEP["blue"], lw=1.5, zorder=7)
    ax.add_patch(rect_s)
    draw_tree(bx - 1.1, by + 0.3, s=0.45)
    draw_cocoa(bx - 1.1, by - 0.4, s=0.55)
    ax.text(bx + 0.5, by + 0.3, "rainforest trees", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)
    ax.text(bx + 0.5, by - 0.4, "cocoa pods", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)

    bx, by = 5.8, 8.8
    rect_m = mpatches.FancyBboxPatch((bx - 1.7, by - 0.85), 3.4, 1.7,
                                     boxstyle="round,pad=0.15", facecolor="white", edgecolor=DEEP["green"], lw=1.5, zorder=7)
    ax.add_patch(rect_m)
    draw_yam(bx - 0.95, by + 0.32, s=0.6)
    draw_cassava(bx - 0.95, by - 0.32, s=0.6)
    ax.text(bx + 0.3, by + 0.32, "yam", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)
    ax.text(bx + 0.3, by - 0.32, "cassava", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)

    bx, by = 6.8, 11.4
    rect_n = mpatches.FancyBboxPatch((bx - 1.9, by - 0.95), 4.3, 1.85,
                                     boxstyle="round,pad=0.15", facecolor="white", edgecolor=DEEP["orange"], lw=1.5, zorder=7)
    ax.add_patch(rect_n)
    draw_millet(bx - 1.25, by + 0.3, s=0.6)
    draw_groundnut(bx - 1.25, by - 0.4, s=0.6)
    ax.text(bx + 0.6, by + 0.3, "millet heads", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)
    ax.text(bx + 0.6, by - 0.4, "groundnut plants", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)

    bx, by = 11.5, 11.1
    rect_c = mpatches.FancyBboxPatch((bx - 1.25, by - 0.65), 2.5, 1.3,
                                     boxstyle="round,pad=0.15", facecolor="white", edgecolor=DEEP["orange"], lw=1.5, zorder=7)
    ax.add_patch(rect_c)
    draw_camel(bx - 0.5, by, s=0.7)
    ax.text(bx + 0.45, by, "camel", fontsize=14, color=INK, va="center", ha="center", weight="bold", zorder=8)

    ax.text(8.5, 3.1, "Sketch map: zones are approximate", fontsize=14, color=GREY, style="italic", ha="center")

    save(fig, out)
