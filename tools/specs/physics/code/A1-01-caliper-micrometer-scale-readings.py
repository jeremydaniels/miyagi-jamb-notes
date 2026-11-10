from style import *
import numpy as np
import matplotlib.pyplot as plt

def draw(out):
    # Generous dimensions for side-by-side reading illustrations
    fig = canvas(16, 10.5)
    
    # Left subplot: Vernier Caliper
    ax1 = fig.add_axes([0.05, 0.05, 0.43, 0.90])
    ax1.set_xlim(-0.2, 6.6)
    ax1.set_ylim(-1.2, 8.8)
    ax1.axis('off')
    
    # Right subplot: Micrometer Screw Gauge
    ax2 = fig.add_axes([0.52, 0.05, 0.43, 0.90])
    ax2.set_xlim(-0.2, 7.8)
    ax2.set_ylim(-1.2, 8.8)
    ax2.axis('off')
    
    # ------------------ LEFT: VERNIER CALIPER ------------------
    ax1.text(3.2, 8.2, "Vernier Caliper", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    
    # Main scale bar
    ms_rect = plt.Rectangle((0.2, 5.0), 6.0, 1.8, facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax1.add_patch(ms_rect)
    
    # Main scale markings:
    # 2.0 cm at x = 0.6. Pitch 1 mm = 0.18 units
    x_start = 0.6
    mm_pitch = 0.18
    for i in range(31):
        x_pos = x_start + i * mm_pitch
        cm_val = 2.0 + i * 0.1
        if i % 10 == 0:
            h = 0.65
            ax1.plot([x_pos, x_pos], [5.0, 5.0 + h], color=INK, lw=1.6)
            ax1.text(x_pos, 5.0 + h + 0.15, f"{int(round(cm_val))}", fontsize=14, ha='center', va='bottom', color=INK)
        elif i % 5 == 0:
            h = 0.45
            ax1.plot([x_pos, x_pos], [5.0, 5.0 + h], color=INK, lw=1.2)
        else:
            h = 0.3
            ax1.plot([x_pos, x_pos], [5.0, 5.0 + h], color=INK, lw=0.9)
            
    ax1.text(6.0, 6.3, "cm", fontsize=14, color=INK, ha='center')
    ax1.text(3.2, 7.2, "Main Scale", fontsize=16, fontweight='bold', ha='center', va='center', color=DEEP["blue"])

    # Vernier scale slide:
    # Vernier zero starts at 2.46 cm = x_start + 4.6 * mm_pitch
    # Pitch = 0.9 mm = 0.9 * mm_pitch
    v_zero = x_start + 4.6 * mm_pitch
    v_pitch = 0.9 * mm_pitch
    
    vs_rect = plt.Rectangle((v_zero - 0.25, 3.4), 2.15, 1.6, facecolor=BLUE, alpha=0.25, edgecolor=DEEP["blue"], lw=1.5)
    ax1.add_patch(vs_rect)
    
    for j in range(11):
        x_v = v_zero + j * v_pitch
        if j % 5 == 0:
            h = 0.55
            ax1.plot([x_v, x_v], [5.0 - h, 5.0], color=INK, lw=1.5)
            ax1.text(x_v, 5.0 - h - 0.22, f"{j}", fontsize=14, ha='center', va='top', color=INK)
        else:
            h = 0.35
            ax1.plot([x_v, x_v], [5.0 - h, 5.0], color=INK, lw=1.0)

    ax1.text(v_zero + 5 * v_pitch, 2.7, "Vernier Scale", fontsize=16, fontweight='bold', ha='center', va='center', color=DEEP["blue"])
    
    # Highlight alignment at 6th mark
    align_x = v_zero + 6 * v_pitch
    ax1.plot([align_x, align_x], [4.1, 5.9], color=DEEP["pink"], lw=2.2, linestyle='--')
    ax1.annotate("6th mark aligns\n(0.06 cm)", xy=(align_x, 5.9), xytext=(align_x + 0.6, 6.5),
                 fontsize=14, color=DEEP["pink"], fontweight='bold',
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5),
                 bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.2"))
                 
    # Highlight Vernier zero
    ax1.annotate("Vernier 0 is past 2.4 cm", xy=(v_zero, 4.8), xytext=(v_zero - 1.2, 3.8),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Calculation Box for Vernier Caliper
    calc_text_vernier = (
        "Main Scale Reading = 2.4 cm\n"
        "Vernier Mark Coinciding = 6th\n"
        "Vernier Reading = 6 × 0.01 = 0.06 cm\n"
        "Total Reading = 2.4 + 0.06 = 2.46 cm"
    )
    ax1.text(3.2, 0.9, calc_text_vernier, fontsize=14.5, ha='center', va='center',
             linespacing=1.6,
             bbox=dict(fc=CREAM, ec=DEEP["blue"], lw=1.5, boxstyle="round,pad=0.6"))

    # ------------------ RIGHT: MICROMETER SCREW GAUGE ------------------
    ax2.text(3.8, 8.2, "Micrometer Screw Gauge", fontsize=18, fontweight='bold', ha='center', va='center', color=INK)
    
    # Sleeve barrel (horizontal cylinder)
    datum_y = 5.0
    sleeve_rect = plt.Rectangle((0.3, datum_y - 0.9), 3.4, 1.8, facecolor=CREAM, edgecolor=GREY, lw=1.5)
    ax2.add_patch(sleeve_rect)
    
    # Datum line on sleeve
    ax2.plot([0.3, 3.7], [datum_y, datum_y], color=INK, lw=1.8)
    
    # Sleeve markings: 1 mm = 0.5 units
    # Top marks = whole mm (0 to 5)
    # Bottom marks = half mm (0.5 to 5.5)
    sl_start = 0.7
    dx_mm = 0.5
    for m in range(6):
        xm = sl_start + m * dx_mm
        ax2.plot([xm, xm], [datum_y, datum_y + 0.45], color=INK, lw=1.4)
        ax2.text(xm, datum_y + 0.55, f"{m}", fontsize=14, ha='center', va='bottom', color=INK)
        
        # half mm mark below datum line
        xh = xm + 0.5 * dx_mm
        ax2.plot([xh, xh], [datum_y - 0.45, datum_y], color=INK, lw=1.4)
        
    ax2.text(2.0, 6.7, "Sleeve", fontsize=16, fontweight='bold', ha='center', va='center', color=DEEP["green"])
    
    # Thimble shape
    thimble_x = 3.7
    thimble_points = np.array([
        [thimble_x, datum_y - 1.4],
        [thimble_x + 0.45, datum_y - 1.6],
        [thimble_x + 2.7, datum_y - 1.6],
        [thimble_x + 2.7, datum_y + 1.6],
        [thimble_x + 0.45, datum_y + 1.6],
        [thimble_x, datum_y + 1.4]
    ])
    thimble_poly = plt.Polygon(thimble_points, facecolor=GREEN, alpha=0.3, edgecolor=DEEP["green"], lw=1.5)
    ax2.add_patch(thimble_poly)
    
    # Prominent label for Thimble placed right above it
    ax2.text(thimble_x + 1.35, 7.1, "Thimble", fontsize=16, fontweight='bold', ha='center', va='center', color=DEEP["green"])

    # Thimble markings: circular scale aligned at 12th mark with datum line
    dy_thimble = 0.12
    for t in range(5, 21):
        yt = datum_y + (t - 12) * dy_thimble
        if datum_y - 1.35 <= yt <= datum_y + 1.35:
            if t % 5 == 0:
                ax2.plot([thimble_x, thimble_x + 0.4], [yt, yt], color=INK, lw=1.5)
                ax2.text(thimble_x + 0.5, yt, f"{t}", fontsize=14, ha='left', va='center', color=INK)
            else:
                ax2.plot([thimble_x, thimble_x + 0.25], [yt, yt], color=INK, lw=1.0)
                
    # Highlight alignment at 12th mark
    ax2.plot([thimble_x - 0.35, thimble_x + 0.55], [datum_y, datum_y], color=DEEP["pink"], lw=2.2, linestyle='--')
    ax2.annotate("12th mark aligns\nwith datum line", xy=(thimble_x + 0.35, datum_y), xytext=(thimble_x + 1.8, datum_y + 0.6),
                 fontsize=14, color=DEEP["pink"], fontweight='bold',
                 arrowprops=dict(arrowstyle="->", color=DEEP["pink"], lw=1.5),
                 bbox=dict(fc="white", ec=DEEP["pink"], boxstyle="round,pad=0.2"))
                 
    # Highlight sleeve 5.5 mm reading
    xh_55 = sl_start + 5.5 * dx_mm
    ax2.annotate("5.5 mm mark exposed", xy=(xh_55, datum_y - 0.45), xytext=(xh_55 - 1.8, datum_y - 1.8),
                 fontsize=14, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                 bbox=dict(fc="white", ec=GREY, boxstyle="round,pad=0.2"))

    # Calculation Box for Micrometer Screw Gauge
    calc_text_micrometer = (
        "Sleeve Reading = 5.5 mm\n"
        "Thimble Reading = 12 × 0.01 = 0.12 mm\n"
        "Total Reading = 5.5 + 0.12 = 5.62 mm"
    )
    ax2.text(3.8, 0.9, calc_text_micrometer, fontsize=14.5, ha='center', va='center',
             linespacing=1.6,
             bbox=dict(fc=CREAM, ec=DEEP["green"], lw=1.5, boxstyle="round,pad=0.6"))

    save(fig, out)
