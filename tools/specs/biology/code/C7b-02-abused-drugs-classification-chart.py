from style import *
import numpy as np
import matplotlib.patches as patches

def draw(out):
    fig = canvas(14, 11)
    
    # Define grid of 4 panels
    # Left, Bottom, Width, Height
    panel_coords = [
        (0.05, 0.52, 0.43, 0.43),  # Panel 1: Stimulants (top-left)
        (0.52, 0.52, 0.43, 0.43),  # Panel 2: Depressants (top-right)
        (0.05, 0.04, 0.43, 0.43),  # Panel 3: Narcotics (bottom-left)
        (0.52, 0.04, 0.43, 0.43),  # Panel 4: Hallucinogens (bottom-right)
    ]
    
    # ---------------- PANEL 1: STIMULANTS ----------------
    ax1 = fig.add_axes(panel_coords[0])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Background panel
    bg1 = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2",
                                fc=CREAM, ec=DEEP["orange"], lw=2, alpha=0.6)
    ax1.add_patch(bg1)
    # Header box
    hdr1 = patches.FancyBboxPatch((0.5, 8.7), 9.0, 0.9, boxstyle="round,pad=0.1",
                                 fc=ORANGE, ec=DEEP["orange"], lw=1.5)
    ax1.add_patch(hdr1)
    ax1.text(5.0, 9.15, "Stimulants", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')
    
    # 1. Coffee cup (Caffeine)
    cup = patches.Polygon([[1.2, 7.0], [2.4, 7.0], [2.2, 5.8], [1.4, 5.8]], closed=True,
                          fc="white", ec=DEEP["orange"], lw=2)
    saucer = patches.Ellipse((1.8, 5.75), 1.6, 0.25, fc="white", ec=DEEP["orange"], lw=2)
    handle = patches.Arc((2.4, 6.4), 0.6, 0.7, angle=0, theta1=270, theta2=90, color=DEEP["orange"], lw=2)
    # steam
    ax1.plot([1.6, 1.5, 1.7], [7.2, 7.5, 7.8], color=DEEP["orange"], lw=1.5)
    ax1.plot([2.0, 1.9, 2.1], [7.2, 7.5, 7.8], color=DEEP["orange"], lw=1.5)
    ax1.add_patch(cup)
    ax1.add_patch(saucer)
    ax1.add_patch(handle)
    ax1.text(1.8, 5.1, "Caffeine", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 2. Kolanut pod with nuts (Kolanut)
    pod = patches.Ellipse((5.0, 6.6), 1.8, 1.1, angle=15, fc=ORANGE, ec=DEEP["orange"], lw=2)
    nut1 = patches.Circle((4.7, 6.4), 0.35, fc="white", ec=DEEP["orange"], lw=1.8)
    nut2 = patches.Circle((5.3, 6.3), 0.38, fc=CREAM, ec=DEEP["orange"], lw=1.8)
    nut3 = patches.Circle((4.9, 5.9), 0.32, fc="white", ec=DEEP["orange"], lw=1.8)
    ax1.add_patch(pod)
    ax1.add_patch(nut1)
    ax1.add_patch(nut2)
    ax1.add_patch(nut3)
    ax1.text(5.0, 5.1, "Kolanut", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 3. Cigarette (Nicotine)
    cig_body = patches.Rectangle((7.0, 6.4), 1.5, 0.35, fc="white", ec=INK, lw=1.8)
    cig_filter = patches.Rectangle((8.5, 6.4), 0.6, 0.35, fc=ORANGE, ec=INK, lw=1.8)
    cig_tip = patches.Rectangle((6.85, 6.4), 0.15, 0.35, fc=GREY, ec=INK, lw=1.5)
    # smoke
    ax1.plot([6.7, 6.4, 6.6, 6.3], [6.6, 6.9, 7.3, 7.7], color=GREY, lw=1.5, ls="--")
    ax1.add_patch(cig_body)
    ax1.add_patch(cig_filter)
    ax1.add_patch(cig_tip)
    ax1.text(7.8, 5.1, "Nicotine", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 4. White powder heap (Cocaine)
    powder = patches.Polygon([[2.0, 2.6], [2.8, 3.5], [3.3, 3.6], [4.2, 2.6]],
                             closed=True, fc="white", ec=DEEP["orange"], lw=2)
    ax1.add_patch(powder)
    # small powder specks
    ax1.scatter([2.2, 2.5, 3.8, 4.0, 3.5], [2.4, 2.7, 2.5, 2.7, 2.8], color=DEEP["orange"], s=10)
    ax1.text(3.1, 1.8, "Cocaine", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 5. Clear crystal shards (Methamphetamine)
    s1 = patches.Polygon([[6.3, 2.5], [6.7, 3.7], [7.1, 3.4], [6.8, 2.5]], fc="white", ec=DEEP["orange"], lw=2)
    s2 = patches.Polygon([[7.0, 2.4], [7.3, 3.8], [7.8, 3.5], [7.6, 2.4]], fc=BLUE, ec=DEEP["orange"], lw=2, alpha=0.5)
    s3 = patches.Polygon([[7.5, 2.4], [8.0, 3.2], [8.3, 2.8], [7.8, 2.4]], fc="white", ec=DEEP["orange"], lw=1.8)
    ax1.add_patch(s1)
    ax1.add_patch(s2)
    ax1.add_patch(s3)
    ax1.text(7.3, 1.8, "Methamphetamine", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    
    # ---------------- PANEL 2: DEPRESSANTS ----------------
    ax2 = fig.add_axes(panel_coords[1])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    bg2 = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2",
                                fc=BLUE, ec=DEEP["blue"], lw=2, alpha=0.35)
    ax2.add_patch(bg2)
    hdr2 = patches.FancyBboxPatch((0.5, 8.7), 9.0, 0.9, boxstyle="round,pad=0.1",
                                 fc=BLUE, ec=DEEP["blue"], lw=1.5, alpha=0.8)
    ax2.add_patch(hdr2)
    ax2.text(5.0, 9.15, "Depressants", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')
    
    # 1. Beer bottle and palm wine gourd (Alcohol)
    # Bottle
    bottle_b = patches.Rectangle((1.1, 4.0), 0.7, 1.6, fc="white", ec=DEEP["blue"], lw=2)
    bottle_n = patches.Rectangle((1.3, 5.6), 0.3, 0.8, fc="white", ec=DEEP["blue"], lw=2)
    bottle_c = patches.Rectangle((1.25, 6.4), 0.4, 0.15, fc=DEEP["blue"], ec=DEEP["blue"], lw=1)
    ax2.add_patch(bottle_b)
    ax2.add_patch(bottle_n)
    ax2.add_patch(bottle_c)
    # Gourd (calabash)
    gourd_b = patches.Circle((2.7, 4.6), 0.75, fc=CREAM, ec=DEEP["blue"], lw=2)
    gourd_t = patches.Circle((2.7, 5.7), 0.45, fc=CREAM, ec=DEEP["blue"], lw=2)
    ax2.add_patch(gourd_b)
    ax2.add_patch(gourd_t)
    ax2.plot([2.55, 2.85], [6.15, 6.15], color=DEEP["blue"], lw=3)
    ax2.text(2.1, 3.2, "Alcohol", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 2. Tablet blister pack (Sedative tablets)
    pack = patches.FancyBboxPatch((5.8, 4.2), 2.8, 2.2, boxstyle="round,pad=0.1",
                                 fc="white", ec=DEEP["blue"], lw=2)
    ax2.add_patch(pack)
    for ix in [6.3, 7.2, 8.1]:
        for iy in [4.8, 5.8]:
            blist = patches.Circle((ix, iy), 0.3, fc=BLUE, ec=DEEP["blue"], lw=1.5, alpha=0.6)
            ax2.add_patch(blist)
    ax2.text(7.2, 3.2, "Sedative tablets", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 3. Glue tube (Inhalants)
    tube_body = patches.Polygon([[4.0, 1.8], [5.8, 2.2], [5.8, 1.4]], fc="white", ec=DEEP["blue"], lw=2)
    tube_nozzle = patches.Polygon([[3.7, 1.8], [4.0, 1.95], [4.0, 1.65]], fc=GREY, ec=DEEP["blue"], lw=2)
    tube_cap = patches.Rectangle((3.3, 1.7), 0.4, 0.2, fc=DEEP["blue"], ec=DEEP["blue"])
    ax2.add_patch(tube_body)
    ax2.add_patch(tube_nozzle)
    ax2.add_patch(tube_cap)
    # label band on tube
    ax2.plot([4.6, 4.6], [1.7, 1.95], color=DEEP["blue"], lw=2)
    # vapor lines
    ax2.plot([3.0, 2.7, 2.9], [1.8, 2.1, 2.4], color=DEEP["blue"], lw=1.5, ls=":")
    ax2.plot([3.1, 2.9, 3.1], [1.5, 1.3, 1.0], color=DEEP["blue"], lw=1.5, ls=":")
    ax2.text(5.0, 0.6, "Inhalants", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    
    # ---------------- PANEL 3: NARCOTICS (OPIOIDS) ----------------
    ax3 = fig.add_axes(panel_coords[2])
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.axis('off')
    
    bg3 = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2",
                                fc=PINK, ec=DEEP["pink"], lw=2, alpha=0.35)
    ax3.add_patch(bg3)
    hdr3 = patches.FancyBboxPatch((0.5, 8.7), 9.0, 0.9, boxstyle="round,pad=0.1",
                                 fc=PINK, ec=DEEP["pink"], lw=1.5, alpha=0.9)
    ax3.add_patch(hdr3)
    ax3.text(5.0, 9.15, "Narcotics (opioids)", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')
    
    # 1. Poppy flower with seed pod (Opium poppy)
    # Stem
    ax3.plot([2.5, 2.5], [4.6, 6.2], color=DEEP["green"], lw=2.5)
    # Pod
    pod_nar = patches.Circle((2.5, 6.4), 0.45, fc=GREEN, ec=DEEP["green"], lw=1.8)
    crown = patches.Polygon([[2.2, 6.8], [2.8, 6.8], [2.5, 6.6]], fc=DEEP["green"], ec=DEEP["green"])
    # Flower petals behind
    pet1 = patches.Ellipse((2.0, 7.1), 0.6, 0.9, angle=-30, fc=PINK, ec=DEEP["pink"], lw=1.5, alpha=0.8)
    pet2 = patches.Ellipse((3.0, 7.1), 0.6, 0.9, angle=30, fc=PINK, ec=DEEP["pink"], lw=1.5, alpha=0.8)
    pet3 = patches.Ellipse((2.5, 7.4), 0.9, 0.6, angle=0, fc=PINK, ec=DEEP["pink"], lw=1.5, alpha=0.8)
    ax3.add_patch(pet1)
    ax3.add_patch(pet2)
    ax3.add_patch(pet3)
    ax3.add_patch(pod_nar)
    ax3.add_patch(crown)
    ax3.text(2.5, 4.0, "Opium poppy", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 2. Cough syrup bottle without brand (Codeine syrup)
    s_bot = patches.Rectangle((6.7, 4.6), 1.4, 2.0, fc="white", ec=DEEP["pink"], lw=2)
    s_neck = patches.Rectangle((7.1, 6.6), 0.6, 0.5, fc="white", ec=DEEP["pink"], lw=2)
    s_cap = patches.Rectangle((7.0, 7.1), 0.8, 0.3, fc=DEEP["pink"], ec=DEEP["pink"])
    s_lbl = patches.Rectangle((6.9, 5.0), 1.0, 1.1, fc=CREAM, ec=GREY, lw=1)
    # cross icon on bottle label
    ax3.plot([7.4, 7.4], [5.3, 5.8], color=DEEP["pink"], lw=2)
    ax3.plot([7.2, 7.6], [5.55, 5.55], color=DEEP["pink"], lw=2)
    ax3.add_patch(s_bot)
    ax3.add_patch(s_neck)
    ax3.add_patch(s_cap)
    ax3.add_patch(s_lbl)
    ax3.text(7.4, 4.0, "Codeine syrup", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 3. Tablet strip (Tramadol)
    strip = patches.Rectangle((1.3, 1.4), 2.5, 1.3, fc="white", ec=DEEP["pink"], lw=2)
    ax3.add_patch(strip)
    for tx in [1.8, 2.5, 3.2]:
        tab = patches.Ellipse((tx, 2.05), 0.45, 0.7, fc=PINK, ec=DEEP["pink"], lw=1.5)
        ax3.add_patch(tab)
        ax3.plot([tx-0.15, tx+0.15], [2.05, 2.05], color=DEEP["pink"], lw=1.2)
    ax3.text(2.6, 0.6, "Tramadol", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    # 4. Syringe (Heroin)
    # Barrel
    barr = patches.Rectangle((6.3, 1.8), 2.0, 0.5, fc="white", ec=INK, lw=1.8)
    plung = patches.Rectangle((8.3, 1.9), 1.0, 0.3, fc=GREY, ec=INK, lw=1.5)
    p_end = patches.Rectangle((9.3, 1.75), 0.15, 0.6, fc=INK, ec=INK)
    ax3.plot([5.5, 6.3], [2.05, 2.05], color=INK, lw=1.8)
    ax3.add_patch(barr)
    ax3.add_patch(plung)
    ax3.add_patch(p_end)
    # Hash marks
    for hx in [6.7, 7.1, 7.5, 7.9]:
        ax3.plot([hx, hx], [2.05, 2.3], color=INK, lw=1.2)
    # fluid inside
    fluid = patches.Rectangle((6.3, 1.85), 1.1, 0.4, fc=PINK, ec="none", alpha=0.6)
    ax3.add_patch(fluid)
    ax3.text(7.4, 0.6, "Heroin", fontsize=12, fontweight='bold', color=INK, ha='center')
    
    
    # ---------------- PANEL 4: HALLUCINOGENS ----------------
    ax4 = fig.add_axes(panel_coords[3])
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.axis('off')
    
    bg4 = patches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle="round,pad=0.2",
                                fc=LAV, ec=DEEP["lav"], lw=2, alpha=0.35)
    ax4.add_patch(bg4)
    hdr4 = patches.FancyBboxPatch((0.5, 8.7), 9.0, 0.9, boxstyle="round,pad=0.1",
                                 fc=LAV, ec=DEEP["lav"], lw=1.5, alpha=0.8)
    ax4.add_patch(hdr4)
    ax4.text(5.0, 9.15, "Hallucinogens", fontsize=15, fontweight='bold', color=INK, ha='center', va='center')
    
    # 1. Cannabis leaf (Cannabis)
    cx, cy = 2.8, 4.8
    angles = [90, 65, 115, 40, 140]
    lengths = [1.8, 1.5, 1.5, 1.1, 1.1]
    widths = [0.4, 0.35, 0.35, 0.3, 0.3]
    for ang, leng, wid in zip(angles, lengths, widths):
        rad = np.radians(ang)
        leaf_patch = patches.Ellipse((cx + (leng*0.45)*np.cos(rad), cy + (leng*0.45)*np.sin(rad)),
                                     wid, leng, angle=ang-90, fc=GREEN, ec=DEEP["green"], lw=1.5)
        ax4.add_patch(leaf_patch)
    # stem
    ax4.plot([cx, cx], [cy - 0.7, cy], color=DEEP["green"], lw=3)
    ax4.text(cx, 3.0, "Cannabis", fontsize=13, fontweight='bold', color=INK, ha='center')
    
    # 2. Magic mushroom (Magic mushroom)
    mx, my = 7.2, 4.4
    # Stalk
    m_stalk = patches.Polygon([[mx-0.35, my], [mx-0.25, my+1.7], [mx+0.25, my+1.7], [mx+0.35, my]],
                              closed=True, fc="white", ec=DEEP["lav"], lw=2)
    # Cap (dome)
    theta = np.linspace(0, np.pi, 50)
    cap_x = mx + 1.3 * np.cos(theta)
    cap_y = (my + 1.6) + 1.1 * np.sin(theta)
    m_cap = patches.Polygon(np.column_stack([cap_x, cap_y]), closed=True,
                            fc=DEEP["lav"], ec=DEEP["lav"], lw=2)
    ax4.add_patch(m_stalk)
    ax4.add_patch(m_cap)
    # Spots on cap
    for sx, sy in [(mx-0.6, my+2.0), (mx, my+2.4), (mx+0.6, my+2.0), (mx-0.2, my+1.8), (mx+0.3, my+1.9)]:
        ax4.add_patch(patches.Circle((sx, sy), 0.12, fc="white", ec="none"))
    # Ring on stalk
    ax4.plot([mx-0.35, mx+0.35], [my+1.0, my+1.0], color=DEEP["lav"], lw=2.5)
    
    # Small companion mushroom
    smx, smy = mx + 1.2, my
    sm_stalk = patches.Polygon([[smx-0.2, smy], [smx-0.15, smy+1.0], [smx+0.15, smy+1.0], [smx+0.2, smy]],
                               closed=True, fc="white", ec=DEEP["lav"], lw=1.8)
    sm_cap_x = smx + 0.7 * np.cos(theta)
    sm_cap_y = (smy + 0.9) + 0.65 * np.sin(theta)
    sm_cap = patches.Polygon(np.column_stack([sm_cap_x, sm_cap_y]), closed=True,
                             fc=LAV, ec=DEEP["lav"], lw=1.8)
    ax4.add_patch(sm_stalk)
    ax4.add_patch(sm_cap)
    ax4.text(mx, 3.0, "Magic mushroom", fontsize=13, fontweight='bold', color=INK, ha='center')
    
    save(fig, out)
