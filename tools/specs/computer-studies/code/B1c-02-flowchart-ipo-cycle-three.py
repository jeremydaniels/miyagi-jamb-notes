from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 8)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Main boxes configuration
    box_w = 2.8
    box_h = 2.4
    y_main = 4.6
    
    # Coordinates of boxes (center)
    x_input = 2.0
    x_proc = 6.0
    x_output = 10.0
    
    y_store = 1.3
    box_store_w = 2.8
    box_store_h = 1.5

    # Title
    ax.text(6.0, 7.4, "The IPO Cycle (Input - Process - Output)", 
            ha='center', va='center', fontsize=18, weight='bold', color=INK)

    # Helper: draw rounded box
    def draw_box(cx, cy, w, h, bg_color, border_color):
        rect = patches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.1,rounding_size=0.2",
            facecolor=bg_color, edgecolor=border_color,
            linewidth=2.5, zorder=2
        )
        ax.add_patch(rect)

    # 1. INPUT Box
    draw_box(x_input, y_main, box_w, box_h, BLUE, DEEP["blue"])
    ax.text(x_input, y_main + 0.8, "INPUT", ha='center', va='center', fontsize=16, weight='bold', color=INK, zorder=3)
    ax.text(x_input, y_main + 0.45, "(Raw Data)", ha='center', va='center', fontsize=14, color=INK, zorder=3)
    
    # Keyboard icon
    kb_w, kb_h = 1.0, 0.45
    kb_x, kb_y = x_input - 0.7, y_main - 0.6
    kb = patches.FancyBboxPatch((kb_x, kb_y), kb_w, kb_h, boxstyle="round,pad=0.03,rounding_size=0.05",
                                facecolor="white", edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    ax.add_patch(kb)
    for row in [0.12, 0.23, 0.34]:
        ax.plot([kb_x + 0.1, kb_x + kb_w - 0.1], [kb_y + row, kb_y + row], color=DEEP["blue"], lw=1.2, ls=':', zorder=5)

    # Mouse icon
    ms_w, ms_h = 0.35, 0.55
    ms_x, ms_y = x_input + 0.45, y_main - 0.65
    mouse = patches.FancyBboxPatch((ms_x, ms_y), ms_w, ms_h, boxstyle="round,pad=0.05,rounding_size=0.15",
                                   facecolor="white", edgecolor=DEEP["blue"], lw=1.5, zorder=4)
    ax.add_patch(mouse)
    ax.plot([ms_x + ms_w/2, ms_x + ms_w/2], [ms_y + ms_h*0.5, ms_y + ms_h], color=DEEP["blue"], lw=1.2, zorder=5)
    ax.plot([ms_x, ms_x + ms_w], [ms_y + ms_h*0.55, ms_y + ms_h*0.55], color=DEEP["blue"], lw=1.2, zorder=5)

    # 2. PROCESS Box
    draw_box(x_proc, y_main, box_w, box_h, ORANGE, DEEP["orange"])
    ax.text(x_proc, y_main + 0.8, "PROCESS", ha='center', va='center', fontsize=16, weight='bold', color=INK, zorder=3)
    ax.text(x_proc, y_main + 0.45, "(CPU)", ha='center', va='center', fontsize=14, color=INK, zorder=3)

    # Gear icon
    gear_cx, gear_cy = x_proc, y_main - 0.45
    r_hub = 0.22
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        tx = gear_cx + 0.35 * np.cos(angle)
        ty = gear_cy + 0.35 * np.sin(angle)
        tooth = patches.Rectangle((tx - 0.08, ty - 0.08), 0.16, 0.16, angle=np.degrees(angle),
                                  facecolor=DEEP["orange"], edgecolor=DEEP["orange"], zorder=4)
        ax.add_patch(tooth)
    gear_outer = patches.Circle((gear_cx, gear_cy), 0.35, facecolor="white", edgecolor=DEEP["orange"], lw=2.0, zorder=5)
    gear_inner = patches.Circle((gear_cx, gear_cy), 0.15, facecolor=ORANGE, edgecolor=DEEP["orange"], lw=1.8, zorder=6)
    ax.add_patch(gear_outer)
    ax.add_patch(gear_inner)

    # 3. OUTPUT Box
    draw_box(x_output, y_main, box_w, box_h, GREEN, DEEP["green"])
    ax.text(x_output, y_main + 0.8, "OUTPUT", ha='center', va='center', fontsize=16, weight='bold', color=INK, zorder=3)
    ax.text(x_output, y_main + 0.45, "(Information)", ha='center', va='center', fontsize=14, color=INK, zorder=3)

    # Monitor icon
    mon_w, mon_h = 1.0, 0.65
    mon_x, mon_y = x_output - mon_w/2, y_main - 0.6
    monitor = patches.FancyBboxPatch((mon_x, mon_y), mon_w, mon_h, boxstyle="round,pad=0.03,rounding_size=0.06",
                                     facecolor="white", edgecolor=DEEP["green"], lw=1.8, zorder=4)
    ax.add_patch(monitor)
    # Screen details
    screen = patches.Rectangle((mon_x + 0.08, mon_y + 0.08), mon_w - 0.16, mon_h - 0.16,
                               facecolor=GREEN, edgecolor=DEEP["green"], lw=1.0, zorder=5)
    ax.add_patch(screen)
    # Stand
    ax.plot([x_output - 0.12, x_output, x_output + 0.12], [mon_y - 0.18, mon_y, mon_y - 0.18],
            color=DEEP["green"], lw=2, zorder=4)
    ax.plot([x_output - 0.25, x_output + 0.25], [mon_y - 0.18, mon_y - 0.18],
            color=DEEP["green"], lw=2, zorder=4)

    # 4. STORAGE Box
    draw_box(x_proc, y_store, box_store_w, box_store_h, LAV, DEEP["lav"])
    ax.text(x_proc, y_store + 0.25, "STORAGE", ha='center', va='center', fontsize=16, weight='bold', color=INK, zorder=3)
    ax.text(x_proc, y_store - 0.2, "(Secondary Memory)", ha='center', va='center', fontsize=14, color=INK, zorder=3)

    # Connecting Arrows
    arrow_props = dict(arrowstyle="-|>", mutation_scale=20, lw=2.5, color=INK)
    
    # Input -> Process
    ax.annotate("", xy=(x_proc - box_w/2, y_main), xytext=(x_input + box_w/2, y_main),
                arrowprops=arrow_props, zorder=2)
    
    # Process -> Output
    ax.annotate("", xy=(x_output - box_w/2, y_main), xytext=(x_proc + box_w/2, y_main),
                arrowprops=arrow_props, zorder=2)
    
    # Two-way arrow Process <-> Storage
    two_way_props = dict(arrowstyle="<|-|>", mutation_scale=20, lw=2.5, color=INK)
    ax.annotate("", xy=(x_proc, y_main - box_h/2), xytext=(x_proc, y_store + box_store_h/2),
                arrowprops=two_way_props, zorder=2)

    save(fig, out)
