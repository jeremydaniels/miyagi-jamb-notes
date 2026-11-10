from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(12, 6.8)
    
    # Left Panel: Solid Core
    ax1 = fig.add_axes([0.05, 0.1, 0.42, 0.82])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Right Panel: Laminated Core
    ax2 = fig.add_axes([0.53, 0.1, 0.42, 0.82])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    # --- LEFT PANEL: Solid Core ---
    ax1.set_title("Solid Core", fontsize=18, color=INK, pad=12, weight='bold')
    
    # Solid block 3D isometric representation
    # Front face
    x0, y0, w, h = 1.5, 2.2, 6.0, 5.0
    front = patches.Rectangle((x0, y0), w, h, facecolor=CREAM, edgecolor=DEEP['blue'], lw=2.5, zorder=2)
    ax1.add_patch(front)
    
    # Top face
    dx, dy = 1.5, 1.3
    top_poly = patches.Polygon([[x0, y0 + h], [x0 + dx, y0 + h + dy], [x0 + w + dx, y0 + h + dy], [x0 + w, y0 + h]],
                               facecolor='#e6edf4', edgecolor=DEEP['blue'], lw=2.5, zorder=2)
    ax1.add_patch(top_poly)
    
    # Side face
    side_poly = patches.Polygon([[x0 + w, y0], [x0 + w + dx, y0 + dy], [x0 + w + dx, y0 + h + dy], [x0 + w, y0 + h]],
                                facecolor='#c9d8e8', edgecolor=DEEP['blue'], lw=2.5, zorder=2)
    ax1.add_patch(side_poly)
    
    # Large swirling eddy currents on the front face
    cx, cy = x0 + w/2, y0 + h/2
    # Outer eddy loop
    r1_x, r1_y = 2.4, 1.8
    # Draw circular arcs with arrows
    arc1 = patches.Arc((cx, cy), r1_x*2, r1_y*2, angle=0, theta1=20, theta2=340, color=DEEP['orange'], lw=3.5, zorder=3)
    ax1.add_patch(arc1)
    ax1.annotate('', xy=(cx + r1_x * np.cos(np.radians(20)), cy + r1_y * np.sin(np.radians(20))),
                 xytext=(cx + r1_x * np.cos(np.radians(25)), cy + r1_y * np.sin(np.radians(25)) - 0.2),
                 arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=3.5, mutation_scale=20), zorder=4)

    # Middle eddy loop
    r2_x, r2_y = 1.6, 1.1
    arc2 = patches.Arc((cx, cy), r2_x*2, r2_y*2, angle=0, theta1=20, theta2=340, color=DEEP['orange'], lw=3.0, zorder=3)
    ax1.add_patch(arc2)
    ax1.annotate('', xy=(cx + r2_x * np.cos(np.radians(20)), cy + r2_y * np.sin(np.radians(20))),
                 xytext=(cx + r2_x * np.cos(np.radians(25)), cy + r2_y * np.sin(np.radians(25)) - 0.2),
                 arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=3.0, mutation_scale=18), zorder=4)

    # Inner eddy loop
    r3_x, r3_y = 0.8, 0.5
    arc3 = patches.Arc((cx, cy), r3_x*2, r3_y*2, angle=0, theta1=20, theta2=340, color=DEEP['orange'], lw=2.5, zorder=3)
    ax1.add_patch(arc3)
    ax1.annotate('', xy=(cx + r3_x * np.cos(np.radians(20)), cy + r3_y * np.sin(np.radians(20))),
                 xytext=(cx + r3_x * np.cos(np.radians(25)), cy + r3_y * np.sin(np.radians(25)) - 0.15),
                 arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=2.5, mutation_scale=15), zorder=4)

    ax1.text(cx, y0 + 0.6, "Eddy current", color=DEEP['orange'], fontsize=14, ha='center', va='center', weight='bold',
             bbox=dict(fc="white", ec="none", pad=1.5), zorder=5)

    # Left bottom label
    ax1.text(5.0, 0.7, "Large eddy currents = High heat loss", fontsize=15, color=INK, ha='center', va='center', weight='bold',
             bbox=dict(fc="white", ec=DEEP['orange'], boxstyle="round,pad=0.5", lw=1.8))
    
    # --- RIGHT PANEL: Laminated Core ---
    ax2.set_title("Laminated Core", fontsize=18, color=INK, pad=12, weight='bold')

    # Draw laminated sheets
    num_sheets = 5
    sheet_gap = 0.16
    total_w = 6.0
    sheet_w = (total_w - (num_sheets - 1) * sheet_gap) / num_sheets
    
    for i in range(num_sheets):
        sx0 = x0 + i * (sheet_w + sheet_gap)
        
        # Front face of sheet
        s_front = patches.Rectangle((sx0, y0), sheet_w, h, facecolor=CREAM, edgecolor=DEEP['blue'], lw=2.0, zorder=2)
        ax2.add_patch(s_front)
        
        # Top face of sheet
        s_top = patches.Polygon([[sx0, y0 + h], [sx0 + dx, y0 + h + dy], [sx0 + sheet_w + dx, y0 + h + dy], [sx0 + sheet_w, y0 + h]],
                                facecolor='#e6edf4', edgecolor=DEEP['blue'], lw=2.0, zorder=2)
        ax2.add_patch(s_top)
        
        # Side face (drawn for the rightmost sheet or subtly for depth)
        if i == num_sheets - 1:
            s_side = patches.Polygon([[sx0 + sheet_w, y0], [sx0 + sheet_w + dx, y0 + dy], [sx0 + sheet_w + dx, y0 + h + dy], [sx0 + sheet_w, y0 + h]],
                                     facecolor='#c9d8e8', edgecolor=DEEP['blue'], lw=2.0, zorder=2)
            ax2.add_patch(s_side)
        
        # Insulating layer indicator between sheets
        if i < num_sheets - 1:
            insul = patches.Rectangle((sx0 + sheet_w, y0), sheet_gap, h, facecolor='#f8d7da', edgecolor='none', zorder=1)
            ax2.add_patch(insul)

        # Narrow, small eddy current loops inside each thin sheet
        scx = sx0 + sheet_w / 2
        for scy in [y0 + h * 0.72, y0 + h * 0.28]:
            sr_x, sr_y = sheet_w * 0.38, 0.9
            s_arc = patches.Arc((scx, scy), sr_x * 2, sr_y * 2, angle=0, theta1=20, theta2=340, color=DEEP['orange'], lw=2.2, zorder=3)
            ax2.add_patch(s_arc)
            ax2.annotate('', xy=(scx + sr_x * np.cos(np.radians(20)), scy + sr_y * np.sin(np.radians(20))),
                         xytext=(scx + sr_x * np.cos(np.radians(25)), scy + sr_y * np.sin(np.radians(25)) - 0.1),
                         arrowprops=dict(arrowstyle="->", color=DEEP['orange'], lw=2.2, mutation_scale=12), zorder=4)

    # Annotation for insulating layer
    ins_x = x0 + sheet_w + sheet_gap / 2
    ax2.annotate("Insulation layer", xy=(ins_x, y0 + h * 0.88), xytext=(x0 + 0.2, y0 + h + 1.2),
                 fontsize=14, color=INK, ha='center',
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.5),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.3"), zorder=5)

    # Right bottom label
    ax2.text(5.0, 0.7, "Small eddy currents = Low heat loss", fontsize=15, color=INK, ha='center', va='center', weight='bold',
             bbox=dict(fc="white", ec=DEEP['green'], boxstyle="round,pad=0.5", lw=1.8))
    
    save(fig, out)
