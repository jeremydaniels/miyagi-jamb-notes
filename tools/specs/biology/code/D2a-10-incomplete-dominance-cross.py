from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(9.5, 12.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 120)
    ax.axis('off')

    COLOR_RED = DEEP["pink"]       
    COLOR_WHITE = "#F8F9FA"        
    COLOR_PINK = "#F497A9"         
    EDGE_RED = "#9E1B32"
    EDGE_WHITE = GREY
    EDGE_PINK = "#C24968"

    def draw_flower(cx, cy, scale, ftype="pink"):
        if ftype == "red":
            fc, ec = COLOR_RED, EDGE_RED
            center_c = "#800F2F"
        elif ftype == "white":
            fc, ec = COLOR_WHITE, EDGE_WHITE
            center_c = "#D3D3D3"
        else:  
            fc, ec = COLOR_PINK, EDGE_PINK
            center_c = "#A3304E"

        tube_w = scale * 0.25
        base_y = cy - scale * 0.7
        top_y = cy + scale * 0.3
        
        rx = scale * 1.1
        ry = scale * 0.45
        
        t = np.linspace(0, 2*np.pi, 200)
        x_ell = cx + rx * np.cos(t)
        y_ell = top_y + ry * np.sin(t)
        
        y_sides = np.linspace(base_y, top_y, 50)
        w = tube_w + (rx - tube_w) * ((y_sides - base_y) / (top_y - base_y))**3
        
        xl = cx - w
        xr = cx + w
        
        body_x = np.concatenate([xl, xr[::-1]])
        body_y = np.concatenate([y_sides, y_sides[::-1]])
        
        ax.fill(body_x, body_y, color=fc, ec='none', zorder=2)
        ax.plot(xl, y_sides, color=ec, lw=1.5, zorder=3)
        ax.plot(xr, y_sides, color=ec, lw=1.5, zorder=3)
        ax.plot([cx-tube_w, cx+tube_w], [base_y, base_y], color=ec, lw=1.5, zorder=3)
        
        ax.fill(x_ell, y_ell, color=fc, ec=ec, lw=1.5, zorder=3)
        
        throat_x = cx + rx * 0.4 * np.cos(t)
        throat_y = top_y - 0.05 * scale + ry * 0.4 * np.sin(t)
        ax.fill(throat_x, throat_y, color=center_c, ec='none', alpha=0.5, zorder=4)

    ax.text(50, 114.5, "Mirabilis jalapa (four-o'clock)", fontsize=16, fontweight='bold',
            ha='center', va='center', color=INK, style='italic')
    
    ax.text(50, 105.5, "P: red (RR) × white (WW)", fontsize=13.5, fontweight='bold',
            ha='center', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.35', lw=1.2))

    draw_flower(32, 97.5, scale=4.0, ftype="red")
    ax.text(32, 89.2, "Red (RR)", fontsize=12, fontweight='bold', ha='center', va='center', color=INK)

    ax.text(50, 96.5, "×", fontsize=24, fontweight='bold', ha='center', va='center', color=INK)

    draw_flower(68, 97.5, scale=4.0, ftype="white")
    ax.text(68, 89.2, "White (WW)", fontsize=12, fontweight='bold', ha='center', va='center', color=INK)

    arrow_p = patches.FancyArrowPatch((50, 87.0), (50, 81.0),
                                      arrowstyle='-|> ', mutation_scale=14,
                                      color=INK, lw=1.5)
    ax.add_patch(arrow_p)

    ax.text(50, 78.5, "F1: all pink (RW)", fontsize=13.5, fontweight='bold',
            ha='center', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.35', lw=1.2))

    draw_flower(50, 70.5, scale=4.2, ftype="pink")
    ax.text(50, 62.0, "Pink (RW)", fontsize=12, fontweight='bold', ha='center', va='center', color=INK)

    arrow_f1 = patches.FancyArrowPatch((50, 56.0), (50, 50.5),
                                       arrowstyle='-|> ', mutation_scale=14,
                                       color=INK, lw=1.5)
    ax.add_patch(arrow_f1)

    ax.text(50, 47.5, "F2: 1 red : 2 pink : 1 white", fontsize=13.5, fontweight='bold',
            ha='center', va='center', color=INK,
            bbox=dict(fc='white', ec=GREY, boxstyle='round,pad=0.35', lw=1.2))

    x0, y0 = 33, 8.0
    w_box, h_box = 17, 14.0

    rect_tl = patches.Rectangle((x0, y0 + h_box), w_box, h_box, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
    rect_tr = patches.Rectangle((x0 + w_box, y0 + h_box), w_box, h_box, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
    rect_bl = patches.Rectangle((x0, y0), w_box, h_box, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)
    rect_br = patches.Rectangle((x0 + w_box, y0), w_box, h_box, facecolor=CREAM, edgecolor=GREY, lw=1.5, zorder=1)

    for r in [rect_tl, rect_tr, rect_bl, rect_br]:
        ax.add_patch(r)

    ax.text(x0 + w_box * 0.5, y0 + 2 * h_box + 3.2, "R", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(x0 + w_box * 1.5, y0 + 2 * h_box + 3.2, "W", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(x0 - 3.5, y0 + h_box * 1.5, "R", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(x0 - 3.5, y0 + h_box * 0.5, "W", fontsize=15, fontweight='bold', ha='center', va='center', color=INK)

    draw_flower(x0 + w_box * 0.5, y0 + h_box * 1.68, scale=2.8, ftype="red")
    ax.text(x0 + w_box * 0.5, y0 + h_box * 1.15, "RR", fontsize=13, fontweight='bold', ha='center', va='center', color=INK, bbox=dict(fc='white', ec='none', pad=0.1))

    draw_flower(x0 + w_box * 1.5, y0 + h_box * 1.68, scale=2.8, ftype="pink")
    ax.text(x0 + w_box * 1.5, y0 + h_box * 1.15, "RW", fontsize=13, fontweight='bold', ha='center', va='center', color=INK, bbox=dict(fc='white', ec='none', pad=0.1))

    draw_flower(x0 + w_box * 0.5, y0 + h_box * 0.68, scale=2.8, ftype="pink")
    ax.text(x0 + w_box * 0.5, y0 + h_box * 0.15, "RW", fontsize=13, fontweight='bold', ha='center', va='center', color=INK, bbox=dict(fc='white', ec='none', pad=0.1))

    draw_flower(x0 + w_box * 1.5, y0 + h_box * 0.68, scale=2.8, ftype="white")
    ax.text(x0 + w_box * 1.5, y0 + h_box * 0.15, "WW", fontsize=13, fontweight='bold', ha='center', va='center', color=INK, bbox=dict(fc='white', ec='none', pad=0.1))

    save(fig, out)
