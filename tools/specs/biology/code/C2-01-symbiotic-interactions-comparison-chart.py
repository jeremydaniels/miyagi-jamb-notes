from style import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 8)
    
    # 2 rows, 4 columns
    # We will create 8 subplots
    axes = []
    w_box = 0.21
    h_box = 0.38
    x_starts = [0.04, 0.28, 0.52, 0.76]
    y_starts = [0.52, 0.07]
    
    panel_info = [
        # row 0
        {"title": "Mutualism", "symbols": "+  +", "desc": "Root nodules & bacteria"},
        {"title": "Cooperation", "symbols": "+  +", "desc": "Oxpecker & cow"},
        {"title": "Commensalism", "symbols": "+  0", "desc": "Remora & shark"},
        {"title": "Parasitism", "symbols": "+  −", "desc": "Tapeworm in intestine"},
        # row 1
        {"title": "Predation", "symbols": "+  −", "desc": "Hawk & chick"},
        {"title": "Amensalism", "symbols": "0  −", "desc": "Penicillium & bacteria"},
        {"title": "Competition", "symbols": "−  −", "desc": "Weed & maize roots"},
        {"title": "Neutralism", "symbols": "0  0", "desc": "Earthworm & grasshopper"}
    ]
    
    # Pre-calculate positions
    for row in range(2):
        for col in range(4):
            idx = row * 4 + col
            ax = fig.add_axes([x_starts[col], y_starts[row], w_box, h_box])
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            ax.set_xticks([])
            ax.set_yticks([])
            # Frame styling
            for spine in ax.spines.values():
                spine.set_color(GREY)
                spine.set_linewidth(1.2)
            axes.append(ax)
            
            # Common titles
            info = panel_info[idx]
            # Symbol badge at top right
            ax.text(8.8, 8.8, info["symbols"], fontsize=12.5, fontweight='bold', color=INK,
                    ha='center', va='center', bbox=dict(boxstyle='round,pad=0.25', facecolor=CREAM, edgecolor=GREY, lw=0.8))
            # Panel interaction name at top left
            ax.text(0.8, 8.8, info["title"].lower(), fontsize=13, fontweight='bold', color=INK, ha='left', va='center')

    # ----------------------------------------------------
    # Panel 0: Mutualism - Root nodules on groundnut root
    # ----------------------------------------------------
    ax0 = axes[0]
    # Main root
    yr = np.linspace(1.5, 7.5, 100)
    xr = 4.5 + 0.4 * np.sin(yr * 1.5)
    ax0.plot(xr, yr, color='#8B5A2B', lw=4, zorder=2)
    # Side branches
    ax0.plot([4.4, 2.5], [5.5, 4.0], color='#8B5A2B', lw=2.5, zorder=2)
    ax0.plot([4.6, 6.8], [4.5, 3.2], color='#8B5A2B', lw=2.5, zorder=2)
    ax0.plot([4.3, 3.0], [2.8, 1.8], color='#8B5A2B', lw=2, zorder=2)
    # Nodules (rounded pink/tan blobs)
    nodule_coords = [(4.3, 5.7), (2.8, 4.2), (4.7, 4.3), (6.0, 3.5), (4.2, 3.0), (3.3, 2.0)]
    for (nx, ny) in nodule_coords:
        nod = patches.Ellipse((nx, ny), 1.2, 0.9, angle=20, facecolor=PINK, edgecolor=DEEP['pink'], lw=1.5, zorder=3)
        ax0.add_patch(nod)
        # bacteria dots inside one magnified nodule
        if nx == 4.3 and ny == 5.7:
            # show dots
            for dx, dy in [(-0.25, 0.1), (0, 0), (0.25, -0.1), (-0.1, -0.2), (0.2, 0.18)]:
                ax0.plot(nx + dx, ny + dy, 'o', color=DEEP['pink'], ms=2.5, zorder=4)
    ax0.text(5.0, 1.0, "root nodules (bacteria)", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 1: Cooperation - Oxpecker on cow's back
    # ----------------------------------------------------
    ax1 = axes[1]
    # Cow back (stylized contour)
    cx = np.linspace(1, 9, 100)
    cy = 4.2 + 0.8 * np.sin((cx - 1) * np.pi / 8) - 0.1 * (cx - 5)**2
    ax1.fill_between(cx, 1.5, cy, color='#E8D8C8', zorder=1)
    ax1.plot(cx, cy, color='#8B5A2B', lw=2.5, zorder=2)
    # Cow patches
    cow_patch = patches.Ellipse((6.5, 3.2), 2.2, 1.2, angle=-10, facecolor='#6B4423', edgecolor='none', zorder=2)
    ax1.add_patch(cow_patch)
    cow_patch2 = patches.Ellipse((3.0, 2.8), 1.6, 1.0, angle=15, facecolor='#6B4423', edgecolor='none', zorder=2)
    ax1.add_patch(cow_patch2)
    
    # Oxpecker bird on the back
    # Legs
    ax1.plot([4.2, 4.3], [4.6, 4.9], color=INK, lw=1.5, zorder=3)
    ax1.plot([4.6, 4.6], [4.6, 4.9], color=INK, lw=1.5, zorder=3)
    # Body
    bird_body = patches.Ellipse((4.7, 5.3), 1.3, 0.7, angle=25, facecolor=DEEP['green'], edgecolor=INK, lw=1.2, zorder=4)
    ax1.add_patch(bird_body)
    # Head & beak
    bird_head = patches.Circle((5.3, 5.7), 0.35, facecolor=DEEP['green'], edgecolor=INK, lw=1.2, zorder=4)
    ax1.add_patch(bird_head)
    ax1.plot([5.55, 6.1], [5.65, 5.4], color=DEEP['orange'], lw=2.0, zorder=5) # beak pecking tick
    # Tick on back
    ax1.plot(6.1, 5.2, 'o', color=DEEP['pink'], ms=3, zorder=4)
    ax1.text(5.0, 1.0, "oxpecker & cow", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 2: Commensalism - Remora fish attached under shark
    # ----------------------------------------------------
    ax2 = axes[2]
    # Water tint
    ax2.axhspan(1.5, 7.5, color='#F0F8FF', zorder=0)
    # Shark body
    sx = np.array([1.5, 3.5, 6.5, 8.5, 7.8, 6.0, 3.5, 1.5])
    sy = np.array([5.5, 6.8, 6.2, 5.8, 5.4, 4.8, 4.8, 5.5])
    shark = patches.Polygon(np.column_stack([sx, sy]), closed=True, facecolor=BLUE, edgecolor=DEEP['blue'], lw=2, zorder=2)
    ax2.add_patch(shark)
    # Shark dorsal fin
    ax2.fill([4.5, 5.2, 5.8], [6.5, 7.5, 6.3], color=BLUE, ec=DEEP['blue'], lw=1.5, zorder=1)
    # Shark eye
    ax2.plot(2.3, 5.6, 'o', color=INK, ms=2.5, zorder=3)
    
    # Remora fish attached below shark belly
    rx = np.array([3.8, 5.5, 5.4, 3.8])
    ry = np.array([4.6, 4.6, 4.2, 4.4])
    remora = patches.Polygon(np.column_stack([rx, ry]), closed=True, facecolor=GREY, edgecolor=INK, lw=1.2, zorder=3)
    ax2.add_patch(remora)
    # Remora sucker disc on head
    ax2.plot([4.0, 4.6], [4.65, 4.65], color=DEEP['orange'], lw=2.5, zorder=4)
    
    ax2.text(5.0, 1.0, "remora attached to shark", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 3: Parasitism - Tapeworm inside intestine
    # ----------------------------------------------------
    ax3 = axes[3]
    # Intestine walls (cross section)
    ix = np.linspace(1.5, 8.5, 100)
    ax3.fill_between(ix, 6.2 + 0.3*np.sin(ix*2), 7.2, color=PINK, alpha=0.5, zorder=1)
    ax3.plot(ix, 6.2 + 0.3*np.sin(ix*2), color=DEEP['pink'], lw=2, zorder=2)
    
    ax3.fill_between(ix, 2.5, 3.5 + 0.3*np.sin(ix*2), color=PINK, alpha=0.5, zorder=1)
    ax3.plot(ix, 3.5 + 0.3*np.sin(ix*2), color=DEEP['pink'], lw=2, zorder=2)
    
    # Tapeworm undulating along the lumen
    tw_x = np.linspace(2.2, 8.0, 80)
    tw_y = 4.8 + 0.6 * np.sin(tw_x * 2.8)
    ax3.plot(tw_x, tw_y, color=CREAM, lw=5.0, zorder=3, solid_capstyle='round')
    ax3.plot(tw_x, tw_y, color='#B0A080', lw=1.2, zorder=4)
    # Segments (proglottids)
    for seg_x in tw_x[::4]:
        seg_y = 4.8 + 0.6 * np.sin(seg_x * 2.8)
        ax3.plot([seg_x, seg_x], [seg_y - 0.25, seg_y + 0.25], color='#908060', lw=1.0, zorder=5)
    # Scolex (head with hooks)
    ax3.plot(2.2, 4.8 + 0.6 * np.sin(2.2 * 2.8), 'o', color='#8B5A2B', ms=4, zorder=6)
    
    ax3.text(5.0, 1.0, "tapeworm in human gut", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 4: Predation - Hawk catching a chick
    # ----------------------------------------------------
    ax4 = axes[4]
    # Hawk swooping (wings spread)
    hx, hy = 4.0, 5.8
    # Wings
    ax4.plot([2.0, 3.8, 5.0], [6.8, 6.0, 6.2], color=DEEP['orange'], lw=2.5, zorder=2)
    ax4.plot([6.2, 4.5, 3.8], [6.8, 6.0, 6.2], color=DEEP['orange'], lw=2.5, zorder=2)
    # Body
    hawk_body = patches.Ellipse((hx, hy), 1.2, 1.6, angle=-25, facecolor='#A0522D', edgecolor=INK, lw=1.2, zorder=3)
    ax4.add_patch(hawk_body)
    # Talons reaching down
    ax4.plot([3.8, 4.2], [5.0, 4.0], color=DEEP['orange'], lw=2, zorder=3)
    ax4.plot([4.3, 4.8], [5.0, 4.1], color=DEEP['orange'], lw=2, zorder=3)
    
    # Chick on the ground
    ax4.axhline(2.2, color=GREEN, lw=2, zorder=1)
    chick_body = patches.Ellipse((5.5, 3.0), 1.1, 0.9, facecolor=CREAM, edgecolor='#C0A020', lw=1.5, zorder=3)
    ax4.add_patch(chick_body)
    chick_head = patches.Circle((6.1, 3.5), 0.4, facecolor=CREAM, edgecolor='#C0A020', lw=1.5, zorder=3)
    ax4.add_patch(chick_head)
    ax4.plot([6.4, 6.7], [3.5, 3.4], color=DEEP['orange'], lw=1.5, zorder=4) # beak
    
    ax4.text(5.0, 1.0, "hawk catching chick", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 5: Amensalism - Penicillium mould inhibiting bacteria
    # ----------------------------------------------------
    ax5 = axes[5]
    # Petri dish
    dish = patches.Circle((5.0, 4.8), 2.8, facecolor='#FAF9F6', edgecolor=GREY, lw=2, zorder=1)
    ax5.add_patch(dish)
    
    # Bacterial lawn (dots all around dish)
    np.random.seed(42)
    angles = np.random.uniform(0, 2*np.pi, 140)
    radii = np.random.uniform(0.5, 2.5, 140)
    bx = 5.0 + radii * np.cos(angles)
    by = 4.8 + radii * np.sin(angles)
    # Keep only those outside the clear zone (radius > 1.2 around center)
    mask = np.sqrt((bx - 5.0)**2 + (by - 4.8)**2) > 1.3
    ax5.plot(bx[mask], by[mask], '.', color='#D4A373', ms=3.5, zorder=2)
    
    # Clear inhibition zone (halo)
    clear_zone = patches.Circle((5.0, 4.8), 1.25, facecolor='white', edgecolor=DEEP['blue'], ls='--', lw=1.2, zorder=3)
    ax5.add_patch(clear_zone)
    
    # Penicillium mould colony in center
    mould = patches.Circle((5.0, 4.8), 0.55, facecolor=DEEP['green'], edgecolor=INK, lw=1.2, zorder=4)
    ax5.add_patch(mould)
    
    ax5.text(5.0, 1.0, "mould & clear bacterial zone", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 6: Competition - Weed and maize plant roots tangled
    # ----------------------------------------------------
    ax6 = axes[6]
    # Soil line
    ax6.axhline(4.8, color='#8B5A2B', lw=1.5, ls='--', zorder=1)
    
    # Maize shoot (tall, right)
    ax6.plot([6.5, 6.5], [4.8, 7.5], color=DEEP['green'], lw=3.5, zorder=2)
    ax6.plot([6.5, 8.2], [6.2, 7.0], color=DEEP['green'], lw=2.2, zorder=2) # maize leaf
    ax6.plot([6.5, 5.2], [5.5, 6.2], color=DEEP['green'], lw=2.2, zorder=2)
    
    # Weed shoot (bushy, left)
    ax6.plot([3.5, 3.5], [4.8, 6.5], color='#556B2F', lw=2.5, zorder=2)
    ax6.plot([3.5, 2.2], [5.6, 6.2], color='#556B2F', lw=1.8, zorder=2)
    ax6.plot([3.5, 4.6], [5.2, 5.8], color='#556B2F', lw=1.8, zorder=2)
    
    # Tangled roots below ground
    # Maize roots (orange/brown)
    ax6.plot([6.5, 5.5, 4.0], [4.8, 3.2, 2.0], color=DEEP['orange'], lw=2, zorder=2)
    ax6.plot([6.5, 7.0, 6.0], [4.8, 3.0, 1.8], color=DEEP['orange'], lw=2, zorder=2)
    # Weed roots (dark/tangled with maize)
    ax6.plot([3.5, 4.8, 6.2], [4.8, 3.5, 2.2], color='#8B4513', lw=1.8, zorder=3)
    ax6.plot([3.5, 3.0, 4.5], [4.8, 3.0, 1.9], color='#8B4513', lw=1.8, zorder=3)
    
    ax6.text(5.0, 1.0, "weed & maize tangled roots", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    # ----------------------------------------------------
    # Panel 7: Neutralism - Earthworm in soil below grasshopper
    # ----------------------------------------------------
    ax7 = axes[7]
    # Ground dividing line
    ax7.fill_between([1, 9], 1.5, 4.5, color='#F5EBE0', zorder=1)
    ax7.axhline(4.5, color='#8B5A2B', lw=1.8, zorder=2)
    
    # Grass tufts above ground
    ax7.plot([2.5, 2.2], [4.5, 5.8], color=GREEN, lw=2, zorder=2)
    ax7.plot([2.5, 2.8], [4.5, 6.2], color=GREEN, lw=2, zorder=2)
    ax7.plot([6.5, 6.8], [4.5, 6.0], color=GREEN, lw=2, zorder=2)
    
    # Grasshopper on grass
    gh_body = patches.Ellipse((4.5, 5.5), 1.4, 0.5, angle=10, facecolor=GREEN, edgecolor=DEEP['green'], lw=1.2, zorder=3)
    ax7.add_patch(gh_body)
    # Grasshopper legs
    ax7.plot([4.0, 3.5, 4.0], [5.5, 6.4, 4.6], color=DEEP['green'], lw=1.5, zorder=4)
    ax7.plot([4.8, 5.2], [5.4, 4.6], color=DEEP['green'], lw=1.2, zorder=4)
    # Antenna
    ax7.plot([5.1, 5.7], [5.7, 6.3], color=DEEP['green'], lw=1.0, zorder=4)
    
    # Earthworm burrowing underground
    ew_x = np.linspace(3.0, 7.5, 60)
    ew_y = 3.0 + 0.4 * np.sin(ew_x * 2.5)
    ax7.plot(ew_x, ew_y, color=PINK, lw=4.0, solid_capstyle='round', zorder=3)
    ax7.plot(ew_x, ew_y, color=DEEP['pink'], lw=1.0, zorder=4)
    # Clitellum band
    ax7.plot(ew_x[18:24], ew_y[18:24], color='#D88A8A', lw=5.5, solid_capstyle='round', zorder=5)
    
    ax7.text(5.0, 1.0, "earthworm & grasshopper", fontsize=11, color=INK, ha='center',
             bbox=dict(fc='white', ec='none', pad=1))

    save(fig, out)
