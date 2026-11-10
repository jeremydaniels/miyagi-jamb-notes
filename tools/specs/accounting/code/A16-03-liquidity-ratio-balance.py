from style import *
import matplotlib.pyplot as plt
import numpy as np

def draw_scale(ax, cx, cy, tilt_angle=0, left_items=[], right_items=[]):
    # Stand / Base
    base_w, base_h = 2.4, 0.35
    ax.fill([cx - base_w/2, cx + base_w/2, cx + base_w/2 - 0.2, cx - base_w/2 + 0.2],
            [cy - 3.2, cy - 3.2, cy - 3.2 + base_h, cy - 3.2 + base_h],
            color=GREY, ec=INK, lw=1.8, zorder=2)
    
    # Central pillar
    ax.plot([cx, cx], [cy - 3.2 + base_h, cy], color=INK, lw=3.5, zorder=2)
    # Fulcrum point
    ax.scatter([cx], [cy], s=120, color=DEEP["blue"], ec=INK, lw=1.8, zorder=4)

    # Beam
    beam_len = 4.4
    dx = (beam_len / 2) * np.cos(tilt_angle)
    dy = (beam_len / 2) * np.sin(tilt_angle)
    
    lx, ly = cx - dx, cy - dy
    rx, ry = cx + dx, cy + dy
    ax.plot([lx, rx], [ly, ry], color=INK, lw=3.5, zorder=3)

    # Left strings & pan
    string_len = 1.6
    pan_w = 2.2
    l_pan_x, l_pan_y = lx, ly - string_len
    ax.plot([lx, l_pan_x - pan_w/2], [ly, l_pan_y], color=DEEP["blue"], lw=1.5, zorder=2)
    ax.plot([lx, l_pan_x + pan_w/2], [ly, l_pan_y], color=DEEP["blue"], lw=1.5, zorder=2)
    
    # Left pan shape (arc)
    pan_arc_x = np.linspace(l_pan_x - pan_w/2, l_pan_x + pan_w/2, 40)
    pan_arc_y = l_pan_y - 0.25 * (1 - ((pan_arc_x - l_pan_x)/(pan_w/2))**2)
    ax.fill_between(pan_arc_x, pan_arc_y, l_pan_y, color=CREAM, ec=INK, lw=1.8, zorder=3)

    # Right strings & pan
    r_pan_x, r_pan_y = rx, ry - string_len
    ax.plot([rx, r_pan_x - pan_w/2], [ry, r_pan_y], color=DEEP["blue"], lw=1.5, zorder=2)
    ax.plot([rx, r_pan_x + pan_w/2], [ry, r_pan_y], color=DEEP["blue"], lw=1.5, zorder=2)
    
    # Right pan shape
    pan_arc_rx = np.linspace(r_pan_x - pan_w/2, r_pan_x + pan_w/2, 40)
    pan_arc_ry = r_pan_y - 0.25 * (1 - ((pan_arc_rx - r_pan_x)/(pan_w/2))**2)
    ax.fill_between(pan_arc_rx, pan_arc_ry, r_pan_y, color=CREAM, ec=INK, lw=1.8, zorder=3)

    return (l_pan_x, l_pan_y), (r_pan_x, r_pan_y)

def draw_icon_box(ax, x, y, w, h, label, fc, ec, crossed=False):
    # Box
    rect = plt.Rectangle((x - w/2, y), w, h, facecolor=fc, edgecolor=ec, lw=1.5, zorder=4)
    ax.add_patch(rect)
    ax.text(x, y + h/2, label, ha="center", va="center", fontsize=14, weight="bold", color=INK, zorder=5)
    
    if crossed:
        ax.plot([x - w/2 - 0.05, x + w/2 + 0.05], [y - 0.05, y + h + 0.05], color=DEEP["pink"], lw=3.5, zorder=6)
        ax.plot([x - w/2 - 0.05, x + w/2 + 0.05], [y + h + 0.05, y - 0.05], color=DEEP["pink"], lw=3.5, zorder=6)

def draw(out):
    fig = canvas(14, 8)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(-0.5, 7.5)
    ax.axis("off")

    # Titles & Headers
    ax.text(7, 7.1, "Visual Analogy of Liquidity Ratios", ha="center", va="center", fontsize=18, weight="bold", color=INK)
    
    # Scale 1: Current Ratio
    cx1, cy1 = 3.5, 4.4
    ax.text(cx1, 6.2, "1. Current Ratio", ha="center", va="center", fontsize=16, weight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.text(cx1, 5.7, "Current Assets  vs  Current Liabilities", ha="center", va="center", fontsize=14, color=DEEP["blue"])
    
    lp1, rp1 = draw_scale(ax, cx1, cy1, tilt_angle=0.0)

    # Current Assets on lp1 (Left pan)
    # Stacked/clustered blocks: Cash, Bank, Debtors, Stock
    bw, bh = 0.95, 0.42
    draw_icon_box(ax, lp1[0] - 0.52, lp1[1] + 0.05, bw, bh, "Cash", GREEN, DEEP["green"])
    draw_icon_box(ax, lp1[0] + 0.52, lp1[1] + 0.05, bw, bh, "Bank", GREEN, DEEP["green"])
    draw_icon_box(ax, lp1[0] - 0.52, lp1[1] + 0.52, bw, bh, "Debtors", GREEN, DEEP["green"])
    draw_icon_box(ax, lp1[0] + 0.52, lp1[1] + 0.52, bw, bh, "Stock", ORANGE, DEEP["orange"])

    ax.text(lp1[0], lp1[1] - 0.6, "Current Assets\n(Cash, Bank, Debtors, Stock)",
            ha="center", va="top", fontsize=14, weight="bold", color=INK)

    # Current Liabilities on rp1 (Right pan)
    draw_icon_box(ax, rp1[0] - 0.52, rp1[1] + 0.05, bw, bh, "Bills", PINK, DEEP["pink"])
    draw_icon_box(ax, rp1[0] + 0.52, rp1[1] + 0.05, bw, bh, "Invoices", PINK, DEEP["pink"])

    ax.text(rp1[0], rp1[1] - 0.6, "Current Liabilities\n(Bills & Invoices)",
            ha="center", va="top", fontsize=14, weight="bold", color=INK)

    # Scale 2: Acid Test Ratio
    cx2, cy2 = 10.5, 4.4
    ax.text(cx2, 6.2, "2. Acid Test (Quick) Ratio", ha="center", va="center", fontsize=16, weight="bold", color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"))
    ax.text(cx2, 5.7, "Quick Assets (Excl. Stock)  vs  Current Liabilities", ha="center", va="center", fontsize=14, color=DEEP["blue"])

    lp2, rp2 = draw_scale(ax, cx2, cy2, tilt_angle=0.0)

    # Quick Assets on lp2 (Left pan)
    draw_icon_box(ax, lp2[0] - 0.52, lp2[1] + 0.05, bw, bh, "Cash", GREEN, DEEP["green"])
    draw_icon_box(ax, lp2[0] + 0.52, lp2[1] + 0.05, bw, bh, "Bank", GREEN, DEEP["green"])
    draw_icon_box(ax, lp2[0] - 0.52, lp2[1] + 0.52, bw, bh, "Debtors", GREEN, DEEP["green"])
    draw_icon_box(ax, lp2[0] + 0.52, lp2[1] + 0.52, bw, bh, "Stock", CREAM, GREY, crossed=True)

    ax.text(lp2[0], lp2[1] - 0.6, "Quick Assets\n(Stock is removed / excluded)",
            ha="center", va="top", fontsize=14, weight="bold", color=INK)

    # Current Liabilities on rp2 (Right pan)
    draw_icon_box(ax, rp2[0] - 0.52, rp2[1] + 0.05, bw, bh, "Bills", PINK, DEEP["pink"])
    draw_icon_box(ax, rp2[0] + 0.52, rp2[1] + 0.05, bw, bh, "Invoices", PINK, DEEP["pink"])

    ax.text(rp2[0], rp2[1] - 0.6, "Current Liabilities\n(Bills & Invoices)",
            ha="center", va="top", fontsize=14, weight="bold", color=INK)

    # Explanatory note banner at bottom
    ax.text(7, 0.2, "Stock is excluded from the Acid Test Ratio because it cannot be converted into cash immediately.",
            ha="center", va="center", fontsize=14, style="italic", color=INK,
            bbox=dict(fc=CREAM, ec=GREY, boxstyle="round,pad=0.4"))

    save(fig, out)
