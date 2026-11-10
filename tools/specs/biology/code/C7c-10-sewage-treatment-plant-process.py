from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(16, 9.5)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    # Title
    ax.text(8.0, 9.15, "Sewage Treatment Plant Flow Diagram", 
            fontsize=16, fontweight='bold', ha='center', va='center', color=INK)

    # -------------------------------------------------------------
    # STAGE 1: Incoming Sewage Pipe & Vertical Metal Bar Screens
    # -------------------------------------------------------------
    # Incoming pipe
    ax.add_patch(patches.Rectangle((0.3, 6.7), 1.0, 0.5, facecolor=CREAM, edgecolor=INK, lw=1.5))
    ax.text(0.8, 7.45, "Incoming\nsewage", fontsize=11, ha='center', va='bottom', color=INK)
    ax.annotate("", xy=(1.3, 6.95), xytext=(0.4, 6.95), arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2))

    # Screen chamber
    ax.add_patch(patches.Rectangle((1.3, 6.2), 1.3, 1.5, facecolor=BLUE, alpha=0.25, edgecolor=INK, lw=1.5))
    
    # Strictly VERTICAL metal bar screens
    for bx in [1.75, 1.95, 2.15]:
        ax.plot([bx, bx], [6.25, 7.65], color=GREY, lw=3)
    # Rags and plastics caught on the vertical bars
    ax.scatter([1.75, 1.95, 2.15, 1.95], [7.0, 6.6, 7.2, 7.3], color=DEEP['orange'], s=45, zorder=5)
    ax.scatter([1.75, 2.15], [6.5, 6.8], color=DEEP['pink'], s=35, zorder=5)

    ax.text(1.95, 8.0, "Screens", fontsize=12, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(1.95, 5.75, "Rags & plastics\ncaught on bars", fontsize=10.5, ha='center', va='top', color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # Pipe to grit channel
    ax.annotate("", xy=(2.9, 6.95), xytext=(2.6, 6.95), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    # -------------------------------------------------------------
    # STAGE 2: Long Grit Channel with Sand Settling
    # -------------------------------------------------------------
    ax.add_patch(patches.Rectangle((2.9, 6.3), 1.6, 1.3, facecolor=BLUE, alpha=0.25, edgecolor=INK, lw=1.5))
    # Sand settling at bottom
    grit_x = np.linspace(2.95, 4.45, 25)
    grit_y = 6.32 + 0.04 * np.sin(grit_x * 12)
    ax.fill_between(grit_x, 6.3, grit_y + 0.08, color=ORANGE, alpha=0.7)
    np.random.seed(10)
    ax.scatter(np.random.uniform(3.0, 4.4, 20), np.random.uniform(6.32, 6.46, 20), s=7, color=DEEP['orange'])
    
    ax.text(3.7, 8.0, "Grit channel", fontsize=12, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(3.7, 5.75, "Sand settling", fontsize=10.5, ha='center', va='top', color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # Pipe to Primary Tank
    ax.annotate("", xy=(4.8, 6.95), xytext=(4.5, 6.95), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    # -------------------------------------------------------------
    # STAGE 3: Rectangular Primary Sedimentation Tank
    # -------------------------------------------------------------
    hopper_pts = np.array([
        [4.8, 7.6],
        [4.8, 6.3],
        [5.3, 5.65],
        [5.7, 5.65],
        [6.2, 6.3],
        [6.2, 7.6]
    ])
    ax.add_patch(patches.Polygon(hopper_pts, closed=True, facecolor=BLUE, alpha=0.25, edgecolor=INK, lw=1.5))
    
    # Sludge settling at the bottom
    sludge_pts = np.array([
        [5.05, 6.0],
        [5.3, 5.65],
        [5.7, 5.65],
        [5.95, 6.0]
    ])
    ax.add_patch(patches.Polygon(sludge_pts, closed=True, facecolor=DEEP['orange'], alpha=0.85))
    ax.text(5.5, 8.0, "Primary sedimentation tank", fontsize=12, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(5.5, 5.35, "Sludge", fontsize=11, fontweight='bold', ha='center', va='top', color=DEEP['orange'], 
            bbox=dict(fc="white", ec="none", pad=1.5))

    # -------------------------------------------------------------
    # STAGE 4: Biological Stage (Aeration tank & Circular Trickling filter)
    # -------------------------------------------------------------
    # Flow split from primary sedimentation tank
    ax.plot([6.2, 6.5, 6.5], [7.1, 7.1, 7.65], color=INK, lw=1.8)
    ax.annotate("", xy=(6.8, 7.65), xytext=(6.5, 7.65), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    ax.plot([6.5, 6.5], [7.1, 6.05], color=INK, lw=1.8)
    ax.annotate("", xy=(6.8, 6.05), xytext=(6.5, 6.05), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    # --- 4A: Aeration tank (activated sludge) ---
    ax.add_patch(patches.Rectangle((6.8, 7.0), 2.1, 1.4, facecolor=CREAM, edgecolor=INK, lw=1.5))
    # Brown liquid (activated sludge)
    ax.add_patch(patches.Rectangle((6.82, 7.02), 2.06, 1.25, facecolor=ORANGE, alpha=0.35, lw=0))
    # Air line & diffuser
    ax.plot([7.0, 7.0, 8.7], [8.2, 7.15, 7.15], color=GREY, lw=2)
    # Air bubbles rising
    np.random.seed(42)
    bx = np.random.uniform(7.1, 8.6, 32)
    by = np.random.uniform(7.22, 8.15, 32)
    ax.scatter(bx, by, s=np.random.uniform(10, 30, 32), facecolors='white', edgecolors=DEEP['blue'], lw=1.2, zorder=5)
    ax.text(7.85, 8.55, "Aeration tank (activated sludge)", fontsize=11.5, fontweight='bold', ha='center', va='bottom', color=INK)
    ax.text(8.75, 7.8, "Air bubbles", fontsize=10.5, ha='left', va='center', color=DEEP['blue'],
            bbox=dict(fc="white", ec="none", pad=1))

    # --- 4B: Circular Trickling Filter (isometric circle / cylinder) ---
    # Bottom stone basin shown as circular / cylinder
    tf_cx, tf_cy = 7.85, 5.75
    tf_rx, tf_ry = 1.0, 0.45
    # Stone bed base
    ax.add_patch(patches.Ellipse((tf_cx, tf_cy - 0.25), tf_rx * 2, tf_ry * 2, facecolor='#E2DFD8', edgecolor=INK, lw=1.5))
    ax.add_patch(patches.Ellipse((tf_cx, tf_cy + 0.1), tf_rx * 2, tf_ry * 2, facecolor='#EAE7DF', edgecolor=INK, lw=1.5))
    # Stones inside circular bed
    np.random.seed(7)
    for _ in range(35):
        sr = np.random.uniform(0, 0.85)
        st = np.random.uniform(0, 2 * np.pi)
        sx = tf_cx + sr * tf_rx * np.cos(st)
        sy = tf_cy + 0.1 + sr * tf_ry * np.sin(st)
        ax.add_patch(patches.Circle((sx, sy), 0.05, facecolor=GREY, edgecolor=INK, lw=0.6))
    # Central pillar
    ax.plot([tf_cx, tf_cx], [tf_cy + 0.1, tf_cy + 0.55], color=INK, lw=3)
    # Rotating spray arm (spanning across the circular bed)
    ax.plot([tf_cx - 0.85, tf_cx + 0.85], [tf_cy + 0.55, tf_cy + 0.55], color=INK, lw=2.2)
    # Spray droplets
    for spx in [tf_cx - 0.65, tf_cx - 0.3, tf_cx + 0.3, tf_cx + 0.65]:
        ax.plot([spx, spx - 0.07], [tf_cy + 0.53, tf_cy + 0.25], color=DEEP['blue'], lw=1.2, ls=':')
        ax.plot([spx, spx + 0.07], [tf_cy + 0.53, tf_cy + 0.25], color=DEEP['blue'], lw=1.2, ls=':')
    ax.text(tf_cx, 4.85, "Trickling filter", fontsize=11.5, fontweight='bold', ha='center', va='top', color=INK)

    # Combining lines into Secondary Settling Tank
    ax.plot([8.9, 9.25, 9.25], [7.65, 7.65, 6.95], color=INK, lw=1.8)
    ax.plot([8.9, 9.25, 9.25], [5.75, 5.75, 6.95], color=INK, lw=1.8)
    ax.annotate("", xy=(9.55, 6.95), xytext=(9.25, 6.95), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    # -------------------------------------------------------------
    # STAGE 5: Secondary Settling Tank
    # -------------------------------------------------------------
    sec_pts = np.array([
        [9.55, 7.6],
        [9.55, 6.3],
        [10.05, 5.65],
        [10.45, 5.65],
        [10.95, 6.3],
        [10.95, 7.6]
    ])
    ax.add_patch(patches.Polygon(sec_pts, closed=True, facecolor=BLUE, alpha=0.25, edgecolor=INK, lw=1.5))
    sec_sludge = np.array([
        [9.85, 6.0],
        [10.05, 5.65],
        [10.45, 5.65],
        [10.65, 6.0]
    ])
    ax.add_patch(patches.Polygon(sec_sludge, closed=True, facecolor=DEEP['orange'], alpha=0.85))
    ax.text(10.25, 8.0, "Secondary\nsettling tank", fontsize=12, fontweight='bold', ha='center', va='bottom', color=INK)

    # Effluent to Chlorination
    ax.annotate("", xy=(11.5, 6.95), xytext=(10.95, 6.95), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))

    # -------------------------------------------------------------
    # STAGE 6: Chlorination & River Outfall
    # -------------------------------------------------------------
    # Small chlorination unit
    ax.add_patch(patches.Rectangle((11.5, 6.3), 1.1, 1.3, facecolor=LAV, alpha=0.35, edgecolor=INK, lw=1.5))
    ax.text(12.05, 6.95, "Cl₂", fontsize=11.5, ha='center', va='center', fontweight='bold', color=DEEP['lav'])
    ax.text(12.05, 8.0, "Chlorination", fontsize=12, fontweight='bold', ha='center', va='bottom', color=INK)

    # Pipe to river
    ax.annotate("", xy=(13.2, 6.95), xytext=(12.6, 6.95), arrowprops=dict(arrowstyle="->", color=DEEP['blue'], lw=2.5))

    # Clean effluent flowing out into a river
    ax.fill([13.3, 15.6, 15.6, 13.3], [5.6, 5.6, 8.3, 8.3], color=BLUE, alpha=0.3)
    for ypos in np.linspace(5.9, 8.0, 5):
        wx = np.linspace(13.4, 15.5, 25)
        ax.plot(wx, ypos + 0.07 * np.sin(wx * 4.5), color=DEEP['blue'], alpha=0.6, lw=1.5)

    ax.text(14.45, 6.95, "Clean effluent to river", fontsize=11.5, fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc="white", ec=DEEP['blue'], boxstyle="round,pad=0.35"))

    # -------------------------------------------------------------
    # LOWER SECTION: Sludge Lines, Digester, Biogas & Fertiliser
    # -------------------------------------------------------------
    # Sludge pipes from Primary and Secondary settling tanks:
    # They route directly leftwards to the Sludge Digester at x ≈ 2.2
    # Primary sludge drops from (5.5, 5.65)
    ax.plot([5.5, 5.5, 3.6], [5.65, 2.6, 2.6], color=INK, lw=2, zorder=0)
    # Secondary sludge drops from (10.25, 5.65) and joins sludge line
    ax.plot([10.25, 10.25, 5.5], [5.65, 2.6, 2.6], color=INK, lw=2, zorder=0)
    ax.annotate("", xy=(3.4, 2.6), xytext=(3.9, 2.6), arrowprops=dict(arrowstyle="->", color=INK, lw=2), zorder=0)
    
    # Moved to the right to avoid the vertical biogas line
    ax.text(8.2, 2.8, "Pipe carrying sludge from tanks", fontsize=10.5, ha='center', va='bottom', color=INK,
            bbox=dict(fc="white", ec="none", pad=1.5))

    # Large closed, dome-topped sludge digester
    dig_x, dig_w = 1.0, 2.4
    dig_base = 0.6
    dig_cyl_h = 1.6
    # Cylinder body
    ax.add_patch(patches.Rectangle((dig_x, dig_base), dig_w, dig_cyl_h, facecolor=CREAM, edgecolor=INK, lw=1.6))
    ax.add_patch(patches.Rectangle((dig_x + 0.05, dig_base + 0.05), dig_w - 0.1, dig_cyl_h - 0.2,
                                  facecolor=ORANGE, alpha=0.45, lw=0))
    # Dome top
    dome_theta = np.linspace(0, np.pi, 50)
    dome_r = dig_w / 2.0
    dome_cx = dig_x + dome_r
    dome_cy = dig_base + dig_cyl_h
    dome_pts = [[dome_cx + dome_r * np.cos(t), dome_cy + 0.65 * np.sin(t)] for t in dome_theta]
    dome_pts.append([dig_x, dome_cy])
    ax.add_patch(patches.Polygon(dome_pts, closed=True, facecolor=CREAM, edgecolor=INK, lw=1.6))

    ax.text(dome_cx, 1.4, "Sludge digester (anaerobic)", fontsize=11.5, fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.25"))

    # Pipe releasing biogas from dome top to gas holder
    gas_x, gas_y, gas_w, gas_h = 5.6, 0.7, 2.2, 1.4
    ax.plot([dome_cx, dome_cx, gas_x], [dome_cy + 0.65, 3.6, 3.6], color=INK, lw=2)
    ax.plot([gas_x, gas_x + gas_w / 2, gas_x + gas_w / 2], [3.6, 3.6, gas_y + gas_h], color=INK, lw=2)
    ax.annotate("", xy=(gas_x + gas_w / 2, gas_y + gas_h), xytext=(gas_x + gas_w / 2, gas_y + gas_h + 0.4),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))

    # Biogas Holder
    ax.add_patch(patches.Rectangle((gas_x, gas_y), gas_w, gas_h, facecolor=LAV, alpha=0.4, edgecolor=INK, lw=1.5))
    ax.plot([gas_x - 0.1, gas_x + gas_w + 0.1], [gas_y + gas_h - 0.3, gas_y + gas_h - 0.3], color=INK, lw=2)
    ax.text(gas_x + gas_w / 2, gas_y + 0.55, "Biogas (methane)", fontsize=11.5, fontweight='bold', ha='center', va='center', color=INK)
    ax.text(gas_x + gas_w / 2, 3.8, "Biogas pipe to gas holder", fontsize=10.5, ha='center', va='bottom', color=INK,
            bbox=dict(fc="white", ec="none", pad=1))

    # Pipe carrying digested dried sludge out towards fertiliser field
    field_x, field_y = 11.0, 0.5
    ax.plot([dig_x + dig_w, dig_x + dig_w + 0.4, dig_x + dig_w + 0.4, field_x], 
            [dig_base + 0.3, dig_base + 0.3, 0.3, 0.3], color=INK, lw=2)
    ax.plot([field_x, field_x + 0.4, field_x + 0.4], [0.3, 0.3, field_y], color=INK, lw=2)
    ax.annotate("", xy=(field_x + 0.4, field_y), xytext=(field_x + 0.4, 0.3),
                arrowprops=dict(arrowstyle="->", color=INK, lw=2))
    ax.text(8.8, 0.12, "Dried sludge used as fertiliser", fontsize=10.5, ha='center', va='bottom', color=INK)

    # Agricultural field with fertiliser
    ax.add_patch(patches.Rectangle((field_x, field_y), 4.4, 1.6, facecolor=GREEN, alpha=0.25, edgecolor=DEEP['green'], lw=1.5))
    # Crops / plants
    for px in np.linspace(field_x + 0.4, field_x + 4.0, 8):
        ax.plot([px, px], [field_y + 0.2, field_y + 0.8], color=DEEP['green'], lw=2)
        ax.plot([px, px - 0.14], [field_y + 0.55, field_y + 0.85], color=DEEP['green'], lw=1.5)
        ax.plot([px, px + 0.14], [field_y + 0.6, field_y + 0.9], color=DEEP['green'], lw=1.5)
    # Fertiliser pellets on ground
    ax.scatter(np.linspace(field_x + 0.2, field_x + 4.2, 16), [field_y + 0.15] * 16, color=DEEP['orange'], s=18, zorder=4)
    ax.text(field_x + 2.2, field_y + 1.2, "Fertiliser", fontsize=12, fontweight='bold', ha='center', va='center', color=INK,
            bbox=dict(fc="white", ec=DEEP['green'], boxstyle="round,pad=0.25"))

    save(fig, out)
